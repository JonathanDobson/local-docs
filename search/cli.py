"""Command line for the local-docs search engine.

  .venv/bin/python -m search up                      start the Milvus Lite server (background)
  .venv/bin/python -m search down                    stop it
  .venv/bin/python -m search index [slug[/version]]  index new/changed docs (all sets by default)
          [--rebuild]                                drop and rebuild the collection
  .venv/bin/python -m search search "question" [-l slug] [-v version] [-k 8] [-t guide|api|release-notes]
          [--mode hybrid|dense|bm25]
  .venv/bin/python -m search stats                   what is indexed
  .venv/bin/python -m search eval [--modes hybrid,dense,bm25]   score search on search/eval/questions.yaml
  .venv/bin/python -m search web [--port 7710]       search page for people at http://127.0.0.1:7710
  .venv/bin/python -m search mcp                     run the MCP server on stdio (Claude Code starts this)

Set LOCALDOCS_MODEL / LOCALDOCS_DIMS to try another embedding model without
changing search/settings.json (each model gets its own collection).
"""
from __future__ import annotations

import argparse
import json
import sys
import time

from search import config


def _fmt(hits, width: int = 300) -> str:
    out = []
    for i, h in enumerate(hits, 1):
        snippet = " ".join(h.text.split())[:width]
        conf = f", {h.confidence} {h.sim:.2f}" if h.confidence else ""
        also = f"\n   same text also in: {', '.join(h.also)}" if h.also else ""
        out.append(f"{i}. [{h.library} {h.version} · {h.doc_type}] {h.path}:{h.start_line}-{h.end_line}  (score {h.score:.4f}{conf})\n"
                   f"   {h.breadcrumb}{also}\n   {snippet}")
    if hits and hits[0].confidence == "weak":
        out.insert(0, "no confident match (top hit is weak); weak hits follow")
    return "\n".join(out) or "no results"


def cmd_search(s, a):
    from search.embed import Embedder
    from search.store import client, search
    vec = None if a.mode == "bm25" else Embedder(s).query(a.query)
    hits = search(client(s), s, vec, a.query, mode=a.mode, library=a.library, version=a.version,
                  doc_type=a.type, limit=a.k)
    print(_fmt(hits))


def cmd_stats(s, a):
    from search.store import client
    c = client(s)
    print(f"server  {s.uri}\nmodel   {s.model}" + (f" ({s.dimensions} dims)" if s.dimensions else ""))
    for name in sorted(c.list_collections()):
        st = c.get_collection_stats(name)
        mark = "  <- active" if name == s.collection else ""
        print(f"{name}: {st.get('row_count')} chunks{mark}")


def cmd_eval(s, a):
    import yaml
    from search.embed import Embedder
    from search.store import client, search
    qs = yaml.safe_load(open(config.ROOT / "search" / "eval" / "questions.yaml"))
    if a.library:
        qs = [q for q in qs if q["library"] == a.library]
    c, emb = client(s), Embedder(s)
    modes = a.modes.split(",")
    results = {m: [] for m in modes}
    t_embed = 0.0
    for q in qs:
        prefix = f"libraries/{q['library']}/{q['version']}/"
        expect = {prefix + e for e in q["expect"]}
        t = time.time()
        vec = emb.query(q["q"]) if any(m != "bm25" for m in modes) else None
        t_embed += time.time() - t
        lib = q["library"] if a.scoped else None
        for m in modes:
            hits = search(c, s, vec, q["q"], mode=m, library=lib, limit=50, dedupe=not a.no_dedupe)
            # Rank by distinct file; a hit also counts for the duplicates folded into it.
            files: list[set[str]] = []
            seen: set[str] = set()
            rank, hit_sim = None, None
            for h in hits:
                if h.path in seen:
                    continue
                seen.add(h.path)
                files.append({h.path, *h.also})
                if rank is None and len(files) <= 10 and files[-1] & expect:
                    rank, hit_sim = len(files), h.sim
            top_sim = hits[0].sim if hits else None
            results[m].append({"id": q["id"], "kind": q.get("kind"), "rank": rank,
                               "top_sim": top_sim, "hit_sim": hit_sim})

    def score(rows):
        n = len(rows)
        r = lambda k: sum(1 for x in rows if x["rank"] and x["rank"] <= k) / n
        mrr = sum(1 / x["rank"] for x in rows if x["rank"]) / n
        return {"n": n, "r@1": round(r(1), 3), "r@3": round(r(3), 3), "r@5": round(r(5), 3),
                "r@10": round(r(10), 3), "mrr": round(mrr, 3)}

    summary = {"model": s.model, "dimensions": s.dimensions, "collection": s.collection, "library": a.library,
               "api_weight": s.api_weight, "intro_weight": s.intro_weight, "dedupe": not a.no_dedupe,
               "scoped": a.scoped, "avg_query_embed_ms": round(1000 * t_embed / len(qs), 1),
               "modes": {m: score(r) for m, r in results.items()},
               "by_kind": {m: {k: score([x for x in r if x["kind"] == k])
                               for k in sorted({x["kind"] for x in r})} for m, r in results.items()},
               "misses": {m: [x["id"] for x in r if not x["rank"] or x["rank"] > 5] for m, r in results.items()}}
    out = config.DATA / "eval" / (f"{s.collection}{'_' + a.library if a.library else ''}"
                                  f"{'_scoped' if a.scoped else ''}{f'_w{s.api_weight:g}' if s.api_weight != 1 else ''}"
                                  f"{f'_i{s.intro_weight:g}' if s.intro_weight != 1 else ''}{'_nodup' if a.no_dedupe else ''}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"summary": summary, "detail": results}, indent=2))
    print(f"{s.model}  ({len(qs)} questions, {(a.library + ' only') if a.library else 'all libraries'}{', scoped' if a.scoped else ''})")
    for m, sc in summary["modes"].items():
        print(f"  {m:7s} r@1 {sc['r@1']:.2f}  r@3 {sc['r@3']:.2f}  r@5 {sc['r@5']:.2f}  r@10 {sc['r@10']:.2f}  mrr {sc['mrr']:.3f}")
    print(f"  query embed {summary['avg_query_embed_ms']} ms avg; saved {out.relative_to(config.ROOT)}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m search", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("up")
    sub.add_parser("down")
    p = sub.add_parser("index")
    p.add_argument("selector", nargs="?")
    p.add_argument("--rebuild", action="store_true")
    p.add_argument("--quiet", action="store_true")
    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("-l", "--library")
    p.add_argument("-v", "--version")
    p.add_argument("-k", type=int, default=8)
    p.add_argument("--mode", default="hybrid", choices=["hybrid", "dense", "bm25"])
    p.add_argument("-t", "--type", choices=["guide", "api", "release-notes"], help="only this kind of document")
    sub.add_parser("stats")
    p = sub.add_parser("eval")
    p.add_argument("--modes", default="hybrid,dense,bm25")
    p.add_argument("--scoped", action="store_true", help="filter each question to its library")
    p.add_argument("--library", help="only questions about this library")
    p.add_argument("--no-dedupe", action="store_true", help="keep near-duplicate hits (to compare)")
    sub.add_parser("mcp")
    p = sub.add_parser("web")
    p.add_argument("--port", type=int, default=7710)
    a = ap.parse_args(argv)
    s = config.load()

    if a.cmd == "up":
        from search.store import ensure_server
        ensure_server(s)
        print(f"Milvus Lite listening on {s.uri} (data in .search/milvus)")
    elif a.cmd == "down":
        from search.store import stop_server
        print("stopped" if stop_server() else "not running (no pid file)")
    elif a.cmd == "index":
        from search.indexer import index
        print(json.dumps(index(s, a.selector, a.rebuild, a.quiet)))
    elif a.cmd == "search":
        cmd_search(s, a)
    elif a.cmd == "stats":
        cmd_stats(s, a)
    elif a.cmd == "eval":
        cmd_eval(s, a)
    elif a.cmd == "web":
        from search.web import serve
        serve(a.port)
    elif a.cmd == "mcp":
        from search.mcp_server import run
        run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
