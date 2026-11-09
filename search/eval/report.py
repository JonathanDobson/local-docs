"""Summarise model-comparison results in .search/eval/ as Markdown tables.

  .venv/bin/python -m search.eval.report
"""
import json
from search.config import DATA


def main() -> None:
    rows = [json.loads(p.read_text())["summary"] for p in sorted((DATA / "eval").glob("*.json"))]
    groups: dict[str, list] = {}
    for r in rows:
        key = (f"{r.get('library') or 'all'} questions"
               + (", scoped to library" if r.get("scoped") else ""))
        groups.setdefault(key, []).append(r)
    for key, rs in groups.items():
        print(f"\n### {key}\n")
        print("| Model | Mode | R@1 | R@3 | R@5 | R@10 | MRR | Query ms |")
        print("|---|---|---|---|---|---|---|---|")
        for r in sorted(rs, key=lambda r: -max(m["mrr"] for m in r["modes"].values())):
            for mode, m in r["modes"].items():
                print(f"| {r['model']}{' d' + str(r['dimensions']) if r['dimensions'] else ''} | {mode} | "
                      f"{m['r@1']:.2f} | {m['r@3']:.2f} | {m['r@5']:.2f} | {m['r@10']:.2f} | {m['mrr']:.3f} | "
                      f"{r['avg_query_embed_ms']} |")


if __name__ == "__main__":
    main()
