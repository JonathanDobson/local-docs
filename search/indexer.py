"""Index docs sets into Milvus, re-embedding only files that changed.

A small state file (.search/state/<collection>.json) remembers each file's
content hash. Changed or new files have their old chunks deleted and new
ones inserted; files that disappeared have their chunks deleted.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from search.chunker import SKIP_NAMES, TEXT_EXT, Chunk, chunk_file, chunk_id, file_hash, identifier_parts
from search.config import DATA, LIBS, ROOT, Settings
from search.embed import Embedder
from search.store import TEXT_MAX, client, create_collection, scope_filter

FLUSH_CHUNKS = 128


def _clip(text: str, max_bytes: int) -> str:
    b = text.encode("utf-8")
    return text if len(b) <= max_bytes else b[:max_bytes].decode("utf-8", errors="ignore")


def docs_sets(selector: str | None = None) -> list[Path]:
    sets = sorted(p.parent for p in LIBS.glob("*/*/manifest.json"))
    if selector:
        sel = selector.strip("/").removeprefix("libraries/")
        sets = [d for d in sets if f"{d.parent.name}/{d.name}" == sel or d.parent.name == sel]
        if not sets:
            raise SystemExit(f"no docs set matches '{selector}' (see INDEX.md)")
    return sets


def files_of(d: Path) -> list[Path]:
    out = [d / "OVERVIEW.md"] if (d / "OVERVIEW.md").exists() else []
    for sub in ("content", "api"):
        base = d / sub
        if base.is_dir():
            out += sorted(p for p in base.rglob("*")
                          if p.is_file() and p.suffix.lower() in TEXT_EXT and p.name not in SKIP_NAMES)
    return out


def _state_path(s: Settings) -> Path:
    return DATA / "state" / f"{s.collection}.json"


def index(s: Settings, selector: str | None = None, rebuild: bool = False, quiet: bool = False) -> dict:
    log = (lambda *a: None) if quiet else (lambda *a: print(*a, file=sys.stderr))
    emb = Embedder(s)
    c = client(s)
    sp = _state_path(s)
    sp.parent.mkdir(parents=True, exist_ok=True)
    if rebuild and c.has_collection(s.collection) and not selector:
        c.drop_collection(s.collection)
    if not c.has_collection(s.collection):
        create_collection(c, s.collection, emb.dim)
        state: dict[str, str] = {}
    else:
        state = json.loads(sp.read_text()) if sp.exists() else {}
    c.load_collection(s.collection)

    t0 = time.time()
    stats = {"files_seen": 0, "files_indexed": 0, "files_removed": 0, "chunks": 0}
    sets = docs_sets(selector)
    seen: set[str] = set()
    pending: list[tuple[Chunk, dict]] = []
    pending_files: dict[str, str] = {}

    def flush():
        if not pending:
            return
        vecs = emb.documents([(m["title"], ch.text) for ch, m in pending])
        rows = []
        for (ch, m), v in zip(pending, vecs):
            crumb = m["title"]
            rows.append({
                "id": chunk_id(ch.path, ch.start_line, ch.end_line),
                "library": m["library"], "version": m["version"], "path": ch.path,
                "file_hash": m["hash"], "breadcrumb": _clip(crumb, 1000),
                "start_line": ch.start_line, "end_line": ch.end_line,
                "source_url": _clip(ch.source_url, 1000), "text": _clip(ch.text, TEXT_MAX),
                "lexical": _clip(f"{crumb}\n{ch.text}\n{identifier_parts(crumb + ' ' + ch.text)}", TEXT_MAX * 2),
                "dense": v,
            })
        c.upsert(s.collection, rows)
        stats["chunks"] += len(rows)
        state.update(pending_files)
        sp.write_text(json.dumps(state))
        pending.clear()
        pending_files.clear()

    for d in sets:
        manifest = json.loads((d / "manifest.json").read_text())
        lib, ver = d.parent.name, d.name
        label = f"{manifest.get('name', lib)} {ver}"
        files = files_of(d)
        log(f"{lib}/{ver}: {len(files)} files")
        for i, p in enumerate(files, 1):
            rel = str(p.relative_to(ROOT))
            seen.add(rel)
            stats["files_seen"] += 1
            h = file_hash(p)
            if state.get(rel) == h:
                continue
            if rel in state:
                c.delete(s.collection, filter=scope_filter(lib, None, rel))
            for ch in chunk_file(p, rel):
                pending.append((ch, {"library": lib, "version": ver, "hash": h,
                                     "title": " › ".join(x for x in [label, ch.breadcrumb] if x)}))
            pending_files[rel] = h
            stats["files_indexed"] += 1
            if len(pending) >= FLUSH_CHUNKS:
                flush()
                log(f"  {i}/{len(files)} files, {stats['chunks']} chunks, {time.time() - t0:.0f}s")
        flush()

    prefixes = tuple(f"libraries/{d.parent.name}/{d.name}/" for d in sets)
    for rel in [r for r in state if r not in seen and (not selector or r.startswith(prefixes))]:
        c.delete(s.collection, filter=scope_filter(path=rel))
        del state[rel]
        stats["files_removed"] += 1
    sp.write_text(json.dumps(state))
    stats["seconds"] = round(time.time() - t0, 1)
    stats["collection"] = s.collection
    return stats
