# local-docs search engine

Hybrid search over every docs set in `libraries/`: **keyword (BM25)** and
**meaning (embeddings)** run together and are merged with **RRF (Reciprocal Rank
Fusion)**. Terms are explained in [../GLOSSARY.md](../GLOSSARY.md).

- **Store:** Milvus Lite 3.2.2 (pure Python, no Docker), running as one local
  server on `127.0.0.1:19541`, data in `.search/milvus/`.
- **Embeddings:** a local Ollama model — chosen by testing, see [Model choice](#model-choice).
- **Interfaces:** the `local-docs` MCP server for agents (`docs_search`,
  `docs_read`, `docs_list`), a search page for people
  (`python -m search web` → http://127.0.0.1:7710), and a command line.

## Commands

Run from `~/local-docs`:

```bash
.venv/bin/python -m search up                       # start the Milvus Lite server (auto-started when needed)
.venv/bin/python -m search index                    # index new/changed files in every docs set
.venv/bin/python -m search index gitea/28           # just one docs set
.venv/bin/python -m search search "question" -l gitea -k 5
.venv/bin/python -m search stats                    # collections and chunk counts
.venv/bin/python -m search eval                     # score against eval/questions.yaml
.venv/bin/python -m search web                      # search page at http://127.0.0.1:7710 (foreground)
tools/web.sh start|stop|restart|status              # same page in the background (PID, log in .search/)
.venv/bin/python -m search down                     # stop the server
```

The search page ([web.py](web.py), [web.html](web.html)) has a library filter,
hybrid / meaning / keyword modes, highlighted matches, and an "Open in file" view
that jumps to the matching lines. Markdown files open **formatted** (headings,
tables, code, callouts, working links between docs) with the matching section
highlighted; a toggle switches to the raw source with line numbers. Rendering
uses vendored copies of marked and DOMPurify ([static/](static/README.md)), so it
works offline, and every page is sanitized because the docs are downloaded
content. Remote images are shown as their caption text and never fetched. Searches are in the URL, so they can be
bookmarked. It listens on 127.0.0.1 only and refuses requests for other host
names or for files outside `libraries/`.

Register the MCP server once per machine:

```bash
claude mcp add --scope user local-docs -- ~/local-docs/tools/docs-mcp.sh
```

## How it works

| Stage | What happens | Code |
|---|---|---|
| Chunk | Markdown split at headings (levels 1–4); each chunk carries its heading path. Long sections are packed from whole paragraphs, lists, code blocks and tables (~2,400 characters max). One chunk per API endpoint. | [chunker.py](chunker.py) |
| Embed | Ollama `/api/embed`, with the query/document wording each model was trained on. | [embed.py](embed.py), [config.py](config.py) |
| Store | One row per chunk: library (partition key), version, path, lines, heading path, text, a dense vector, and a BM25 sparse vector built by Milvus from a keyword field (heading path + text + split identifiers, so `DISABLE_REGISTRATION` also matches "disable registration"). | [store.py](store.py) |
| Index | Re-embeds only files whose content hash changed; deletes chunks of removed files. | [indexer.py](indexer.py) |
| Search | Top 50 from each of BM25 and the dense index, filtered by library/version (a version like `16` or `16.4` also matches a folder named `16.4.5`) and optionally doc type, merged with RRF (k=60). API reference results are then scaled by `api_weight` (0.6) unless the question looks like an API question. | [store.py](store.py) |

Compared with a typical codebase semantic search: no syntax-tree (AST) code
splitting and no file watcher (docs only change when ingested), and keyword search
is added, which matters for docs because so many questions are exact identifiers.

## Doc types and API weighting

Every chunk is a **guide**, **API reference** or **release notes** page, worked
out from its path (no extra field, no re-embedding): `api/` or `api-reference/`
folders are API reference; `release-notes/`, `release_notes*` or `changelog*` are
release notes; everything else is a guide. The ingest skill files docs to match.

API reference pages are numerous and short (Gitea: 776 of 1,839 chunks are
endpoints or data models), so they crowd results for plain questions. Search
therefore multiplies API scores by `api_weight` in `settings.json` — unless the
question mentions an API, endpoint, HTTP verb, function call or CamelCase
identifier, or a doc type filter is set. Everywhere you search, you can also
filter to one type (`-t` on the CLI, `doc_type` in the MCP tool, the "All pages"
menu on the search page).

Measured on Gitea's 30 test questions with qwen3-embedding:0.6b: top-1 hits
0.70 → 0.73 and MRR 0.831 → 0.853 at any weight from 0.8 down to 0.25, with no
API question getting worse; 0.6 is used. To be re-checked on the full corpus.

## Model choice

**Status (2026-11-09): comparison complete** (four small models, both phases, all at
`api_weight` 0.6). The default in `settings.json` is now **`embeddinggemma`**
(was `qwen3-embedding:0.6b`), chosen from these results. Rerun with
`search/eval/bakeoff.sh` (`BAKEOFF_BIG= search/eval/bakeoff.sh` skips the 4B model),
summarise with `.venv/bin/python -m search.eval.report` (results land in
`.search/eval/`, which is not committed, so the numbers are recorded here).

Scores are MRR (mean reciprocal rank: 1.0 means the right page is always first)
and r@k (share of questions whose right page is in the top k). Phase-2 scores were
measured on both a GTX 1650 PC and an M1 Pro Mac: embeddinggemma matched to within
0.001 and qwen3-embedding:0.6b to within 0.005, but embeddinggemma-2 scored about
0.015–0.02 lower on the Mac. Treat MRR differences under ~0.02 as noise. The tables
show the Mac run.

### Phase 1 — Gitea only (1,839 chunks, 30 questions)

| Model | Hybrid MRR | Hybrid r@1 | Dense MRR | Index time, GTX 1650 | Index time, M1 Pro ¹ |
|---|---|---|---|---|---|
| qwen3-embedding:4b ² | **0.894** | 0.80 | 0.875 | ~44 min (spills to CPU) | not run |
| embeddinggemma | 0.883 | 0.77 | **0.903** | 2 min | 15 min |
| embeddinggemma-2 | 0.872 | **0.80** | 0.829 | 3 min | 11 min |
| qwen3-embedding:0.6b | 0.853 | 0.73 | 0.755 | ~11 min | 21 min |
| nomic-embed-text | 0.798 | 0.67 | 0.786 | 6 min | 5 min |
| BM25 only (no model) | 0.634 | 0.50 | — | — | — |

¹ The M1 Pro run shared Ollama with another indexing job and was short of memory
for the first three models, and Ollama's runner stalled twice (see [Limits](#limits)),
so its times are upper bounds, not a hardware comparison. ² Too slow on the GTX 1650
(4 GB) to index the whole library — about 6 hours for 15,503 chunks — so it is only a
quality ceiling.

### Phase 2 — all docs sets (Gitea 28, Milvus 3.0, Next.js 16.4.5: 15,503 chunks, 60 questions) ³

| Model | Hybrid MRR | Hybrid MRR, scoped ⁴ | Dense MRR | BM25 MRR | Index time, GTX 1650 | Index time, M1 Pro |
|---|---|---|---|---|---|---|
| embeddinggemma | 0.733 | **0.759** | **0.801** | 0.526 | **18 min** | **33 min** |
| embeddinggemma-2 | 0.721 | 0.748 | 0.725 | 0.526 | 40 min | 39 min |
| qwen3-embedding:0.6b | 0.711 | 0.715 | 0.672 | 0.526 | 61 min | 82 min (one stall) |
| nomic-embed-text | 0.649 | 0.652 | 0.687 | 0.526 | interrupted | 41 min |

³ The question set covers Gitea and Milvus only; Next.js is in the index as
distractor text. ⁴ Scoped: each question limited to its library. M1 Pro phase-2
times are for the 13,670 chunks not already indexed in phase 1.

### What it shows

- Hybrid beats BM25 alone by a wide margin with every model.
- **embeddinggemma is the best small model**: top or joint-top on every phase-2
  score and the fastest to index on both machines, so it is now the default.
  qwen3-embedding:0.6b, the previous default, is third on quality and the slowest
  to index — which matters every time a docs set is ingested. On a machine that
  has not run the bake-off, run `ollama pull embeddinggemma` and
  `python -m search index` once.
- On the full corpus, **meaning-only search beats hybrid search** for embeddinggemma
  (0.801 vs 0.733) and for nomic-embed-text (0.687 vs 0.649): BM25 adds noise there.
  Worth testing a weighted ranker (Milvus's `WeightedRanker`) or a different `rrf_k`
  instead of plain RRF before settling the search mode.
- The 4B model is only slightly better than embeddinggemma on Gitea (0.894 vs 0.883
  hybrid) and far slower, so it is not worth the cost on either machine.
- Next.js has no test questions yet; questions for it would make the corpus-wide
  numbers more representative.

## Limits

- Milvus Lite has only the `standard` analyzer — no stemming ("registering" won't
  keyword-match "registration"); meaning search covers that.
- BM25 word statistics are per storage segment, not global, in Milvus Lite.
- Ollama's model runner occasionally stalls mid-request (seen twice on an M1 Pro
  during the bake-off, with two indexing jobs sharing Ollama). The indexer then waits
  up to 10 minutes before retrying. `ollama stop <model>` clears it at once; the
  indexer's retry loads a fresh runner.
- Indexing speed is bound by the GPU (GTX 1650, 4 GB). See the throughput table.
- Moving to Milvus Standalone 3.0 later (for the text highlighter, global BM25
  statistics, more analyzers) needs only a different URI in `config.py`; the
  schema and code are the same.
