#!/usr/bin/env python3
"""Turn Chromium `*_switches.{h,cc}` source files into Markdown reference pages.

    python3 tools/switches2md.py <chromium-checkout> <out-dir> <file> [<file> ...]

Each <file> is a path relative to the checkout (a .h or .cc). A header and its
.cc twin are merged into one page, keyed by the constant name (kFooBar), so a
comment written on either side is kept. For every switch the page shows the
command-line spelling (--foo-bar), the constant, the comment above it in the
source, and the preprocessor condition it sits under (#if BUILDFLAG(IS_WIN) …).

The files are only read as text; nothing is compiled or executed. Writes one
page per switches file plus an alphabetical index (ALL-SWITCHES.md).
"""
import re
import sys
from pathlib import Path

DECL = re.compile(
    r'^\s*(?:(?:inline|extern|static|COMPONENT_EXPORT\([^)]*\)|[A-Z_]+_EXPORT)\s+)*'
    r'(?:constexpr\s+|const\s+)+char\s+(k\w+)\[\]\s*(?:=\s*(.*))?;?\s*$')
STR = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parse(path: Path):
    """Return {const: {"switch", "comment", "cond"}} in source order."""
    out = {}
    comment: list[str] = []
    conds: list[str] = []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        i += 1
        if s.startswith("//"):
            text = s[2:].strip()
            if text.startswith("NOLINT") or text.startswith("clang-format"):
                continue
            comment.append(text)
            continue
        if s.startswith("#if"):
            conds.append(s[s.index(" ") + 1:].strip() if " " in s else s)
            comment = []
            continue
        if s.startswith("#elif"):
            if conds:
                conds[-1] = "!(" + conds[-1] + ") && " + s.split(None, 1)[1]
            comment = []
            continue
        if s.startswith("#else"):
            if conds:
                conds[-1] = "!(" + conds[-1] + ")"
            comment = []
            continue
        if s.startswith("#endif"):
            if conds:
                conds.pop()
            comment = []
            continue
        if not s:
            comment = []
            continue
        m = DECL.match(line)
        if m:
            name, rhs = m.group(1), m.group(2) or ""
            # the string literal may continue on the next line(s)
            while rhs is not None and ";" not in rhs and "=" in line and i < len(lines):
                rhs += " " + lines[i].strip()
                i += 1
            strs = STR.findall(rhs)
            val = "".join(strs) if strs else None
            conds_txt = " && ".join(c for c in conds
                                    if not re.search(r'(_H_|_SWITCHES_H)', c))
            out[name] = {"switch": val, "comment": " ".join(comment).strip(),
                         "cond": conds_txt}
            comment = []
            continue
        comment = []
    return out


def merge(h: dict, cc: dict):
    names = list(h) + [n for n in cc if n not in h]
    res = []
    for n in names:
        a, b = h.get(n, {}), cc.get(n, {})
        sw = a.get("switch") or b.get("switch")
        if sw is None:
            continue
        com = a.get("comment") or ""
        if b.get("comment") and b["comment"] not in com:
            com = (com + " " + b["comment"]).strip()
        res.append({"const": n, "switch": sw, "comment": com,
                    "cond": a.get("cond") or b.get("cond") or ""})
    return res


def md_escape(t: str) -> str:
    return t.replace("|", "\\|")


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(2)
    root, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    stems = {}
    for f in sys.argv[3:]:
        stems.setdefault(str(Path(f).with_suffix("")), []).append(f)
    allsw = []
    for stem, files in sorted(stems.items()):
        h = parse(root / (stem + ".h")) if (root / (stem + ".h")).exists() else {}
        cc = parse(root / (stem + ".cc")) if (root / (stem + ".cc")).exists() else {}
        items = merge(h, cc)
        if not items:
            continue
        page = stem.replace("/", "__") + ".md"
        srcs = [p for p in (stem + ".h", stem + ".cc") if (root / p).exists()]
        lines = [f"# Command-line switches: `{stem}`", "",
                 "Generated from " + " and ".join(f"`{p}`" for p in srcs) +
                 " in the Chromium source. Each switch is passed to the browser as "
                 "`--name` or `--name=value`. The description is the source comment "
                 "verbatim; *Condition* is the build/platform `#if` it is defined under.",
                 "", f"{len(items)} switches.", ""]
        for it in items:
            lines.append(f"## `--{it['switch']}`")
            lines.append("")
            lines.append(f"- Constant: `{it['const']}`")
            if it["cond"]:
                lines.append(f"- Condition: `{it['cond']}`")
            lines.append("")
            lines.append(it["comment"] or "_No description in the source._")
            lines.append("")
            allsw.append((it["switch"], page, it["comment"], it["cond"]))
        (out / page).write_text("\n".join(lines), encoding="utf-8")
    allsw.sort(key=lambda x: (x[0].lower(), x[1]))
    idx = ["# All command-line switches (A–Z)", "",
           f"{len(allsw)} switches from {len(set(p for _, p, _, _ in allsw))} source files. "
           "Find the switch, then open its page for the full description.", "",
           "| Switch | Page | Summary |", "|---|---|---|"]
    for sw, page, com, cond in allsw:
        summ = com.split(". ")[0][:160] if com else ""
        if cond:
            summ = (summ + f" *(only if `{cond}`)*").strip()
        idx.append(f"| `--{md_escape(sw)}` | [{page[:-3]}]({page}) | {md_escape(summ)} |")
    (out / "ALL-SWITCHES.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"wrote {len(set(p for _, p, _, _ in allsw))} pages, {len(allsw)} switches -> {out}")


if __name__ == "__main__":
    main()
