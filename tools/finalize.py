#!/usr/bin/env python3
"""Validate an ingested docs set, write its TOC.md, and rebuild INDEX.md.

A set whose manifest says "local_only": true (docs whose licence doesn't allow
republishing) is listed in INDEX.local.md instead, which git ignores, and must
itself be ignored by git (list its folder in .gitignore) or validation fails.

  python3 tools/finalize.py <slug>/<version>   # one docs set, then the index
  python3 tools/finalize.py --index-only       # just rebuild INDEX.md
  python3 tools/finalize.py --check            # validate every docs set, change nothing

Standard library only. Exit status is non-zero if anything fails validation,
so an ingest is not finished until this passes.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBS = ROOT / "libraries"
REQUIRED = ["name", "slug", "version", "kind", "summary", "requested", "sources",
            "ingested_at", "coverage"]
KINDS = {"library", "framework", "api", "application", "tool", "language", "spec", "service"}
DOC_EXT = {".md", ".mdx", ".markdown", ".rst", ".txt", ".adoc"}
SPEC_EXT = {".json", ".yaml", ".yml", ".graphql", ".gql", ".proto"}
SOURCE_TYPES = {"git", "llms-txt", "package", "crawl", "openapi", "graphql",
                "release-notes", "other"}
CONTENT_DIRS = ["content", "api"]


def title_of(path: Path) -> str:
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    except OSError:
        return path.stem
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.M)
    if m and m.group(1).strip():
        return m.group(1).strip()
    m = re.search(r"^#{1,2}\s+(.+)$", head, re.M) or re.search(r"^(.+)\n[=]{3,}\s*$", head, re.M)
    return m.group(1).strip() if m else path.stem


def git_ignored(d: Path) -> bool:
    """True when git ignores the folder (or this isn't a git checkout)."""
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", str(d / "manifest.json")],
                           capture_output=True)
    except OSError:
        return True
    return r.returncode == 0 or r.returncode == 128


def validate(d: Path) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    mf = d / "manifest.json"
    if not mf.exists():
        return None, [f"{d.relative_to(ROOT)}: missing manifest.json"]
    try:
        m = json.loads(mf.read_text())
    except json.JSONDecodeError as exc:
        return None, [f"{mf.relative_to(ROOT)}: invalid JSON: {exc}"]
    for key in REQUIRED:
        if not m.get(key):
            errors.append(f"{mf.relative_to(ROOT)}: missing '{key}'")
    if m.get("kind") and m["kind"] not in KINDS:
        errors.append(f"{mf.relative_to(ROOT)}: kind '{m['kind']}' not one of {sorted(KINDS)}")
    if m.get("slug") and m["slug"] != d.parent.name:
        errors.append(f"{mf.relative_to(ROOT)}: slug '{m['slug']}' != folder '{d.parent.name}'")
    if m.get("version") and str(m["version"]) != d.name:
        errors.append(f"{mf.relative_to(ROOT)}: version '{m['version']}' != folder '{d.name}'")
    for i, s in enumerate(m.get("sources") or []):
        if not s.get("type") or not s.get("url"):
            errors.append(f"{mf.relative_to(ROOT)}: sources[{i}] needs 'type' and 'url'")
        elif s["type"] not in SOURCE_TYPES:
            errors.append(f"{mf.relative_to(ROOT)}: sources[{i}].type '{s['type']}' not one of {sorted(SOURCE_TYPES)}")
        if s.get("dest") and not (d / s["dest"]).exists():
            errors.append(f"{mf.relative_to(ROOT)}: sources[{i}].dest '{s['dest']}' does not exist")
    if m.get("local_only") and not git_ignored(d):
        errors.append(f"{d.relative_to(ROOT)}: local_only, but git doesn't ignore it — add "
                      f"'{d.parent.relative_to(ROOT)}/' to .gitignore")
    ov = d / "OVERVIEW.md"
    if not ov.exists() or len(ov.read_text().strip()) < 200:
        errors.append(f"{d.relative_to(ROOT)}: OVERVIEW.md missing or too thin")
    if not any((d / c).is_dir() and any((d / c).rglob("*")) for c in CONTENT_DIRS):
        errors.append(f"{d.relative_to(ROOT)}: no files under content/ or api/")
    return m, errors


def stats_and_toc(d: Path, m: dict) -> None:
    files, size = [], 0
    for c in CONTENT_DIRS:
        base = d / c
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file():
                size += p.stat().st_size
                files.append(p)
    docs = [p for p in files if p.suffix.lower() in DOC_EXT]
    specs = [p for p in files if p.suffix.lower() in SPEC_EXT and p.parent.name != "endpoints"
             and p.is_relative_to(d / "api")]
    m["stats"] = {"files": len(files), "doc_files": len(docs), "spec_files": len(specs),
                  "megabytes": round(size / 1_000_000, 2)}
    (d / "manifest.json").write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")

    lines = [f"# {m['name']} {m['version']} — table of contents", "",
             "Generated by tools/finalize.py. One line per document: path, then title.", ""]
    current = None
    for p in docs:
        rel = p.relative_to(d)
        folder = str(rel.parent)
        if folder != current:
            lines += ["", f"## {folder}/", ""]
            current = folder
        lines.append(f"- `{rel}` — {title_of(p)}")
    (d / "TOC.md").write_text("\n".join(lines).replace("\n\n\n", "\n\n") + "\n")


def all_sets() -> list[Path]:
    return sorted(p.parent for p in LIBS.glob("*/*/manifest.json"))


def _row(d: Path, m: dict) -> str:
    src = ", ".join(sorted({s.get("type", "?") for s in m.get("sources", [])}))
    stats = m.get("stats", {})
    return (f"| {m.get('name')} | {m.get('version')}"
            + (f" ({m['release']})" if m.get("release") and m["release"] != m.get("version") else "")
            + f" | {m.get('kind')} | "
            f"`libraries/{d.parent.name}/{d.name}/` | {src} | {stats.get('doc_files', '?')} | "
            f"{m.get('ingested_at')} | {str(m.get('summary', '')).replace('|', '/')} |")


HEADER = ["| Name | Version | Kind | Path | Sources | Docs | Ingested | Summary |",
          "|---|---|---|---|---|---|---|---|"]


def build_index() -> list[str]:
    """INDEX.md lists the shareable sets; INDEX.local.md (git-ignored) the local-only ones."""
    public, local, errors = [], [], []
    for d in all_sets():
        m, errs = validate(d)
        errors += errs
        if not m:
            continue
        (local if m.get("local_only") else public).append((m.get("name", d.parent.name).lower(), d.name, _row(d, m)))
    public.sort(); local.sort()
    out = [
        "# Local docs index",
        "",
        "Every documentation set stored in this folder. Read this first, pick the",
        "row whose name and version match what you are working with, then open that",
        "folder's `OVERVIEW.md`. Generated by `tools/finalize.py` — do not edit by hand.",
        "Sets kept on this machine only are listed in `INDEX.local.md`, if it exists.",
        "",
        f"Last rebuilt: {date.today().isoformat()} · {len(public)} docs set(s)",
        "",
        *HEADER,
        *[r[2] for r in public],
    ]
    if not public:
        out.append("| _(nothing ingested yet)_ | | | | | | | |")
    (ROOT / "INDEX.md").write_text("\n".join(out) + "\n")
    loc = ROOT / "INDEX.local.md"
    if local:
        loc.write_text("\n".join([
            "# Local-only docs sets",
            "",
            "Docs sets kept on this machine only (`\"local_only\": true` in the manifest),",
            "because their licence doesn't allow republishing. Git ignores them and this",
            "file. Generated by `tools/finalize.py` — do not edit by hand.",
            "",
            f"Last rebuilt: {date.today().isoformat()} · {len(local)} docs set(s)",
            "",
            *HEADER,
            *[r[2] for r in local],
        ]) + "\n")
    elif loc.exists():
        loc.unlink()
    return errors


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    if argv[0] == "--check":
        errors = [e for d in all_sets() for e in validate(d)[1]]
    elif argv[0] == "--index-only":
        errors = build_index()
    else:
        d = (LIBS / argv[0].strip("/").removeprefix("libraries/")).resolve()
        if LIBS.resolve() not in d.parents:
            print(f"not a docs set under libraries/: {argv[0]}")
            return 2
        m, errors = validate(d)
        if m and not errors:
            stats_and_toc(d, m)
            print(f"{d.relative_to(ROOT)}: {m['stats']}")
            print(f"next: index it for search -> .venv/bin/python -m search index "
                  f"{d.parent.name}/{d.name}")
        errors = errors + [e for e in build_index() if e not in errors]
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
