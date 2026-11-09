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
.venv/bin/python -m search web                      # search page at http://127.0.0.1:7710
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

**Status (2026-11-09): comparison still running.** `qwen3-embedding:0.6b` stays the
default until it finishes. Rerun with `search/eval/bakeoff.sh`, summarise with
`.venv/bin/python -m search.eval.report` (results land in `.search/eval/`, which
is not committed, so the numbers are recorded here).

Scores are MRR (mean reciprocal rank: 1.0 means the right page is always first)
and r@k (share of questions whose right page is in the top k).

### Phase 1 — Gitea only (1,839 chunks, 30 questions)

| Model | Hybrid MRR | Hybrid r@1 | Dense MRR | Index speed (chunks/s) | Query embed |
|---|---|---|---|---|---|
| qwen3-embedding:4b ¹ | **0.894** | 0.80 | 0.875 | 0.7 (spills to CPU) | 424 ms |
| embeddinggemma-2 | 0.867 | 0.77 | 0.856 | 11.3 | 70 ms |
| embeddinggemma | 0.861 | 0.73 | **0.903** | 15.8 | 68 ms |
| qwen3-embedding:0.6b | 0.831 (0.853 ¹) | 0.70 | 0.752 | ~2.9 | 86 ms |
| nomic-embed-text | 0.790 | 0.67 | 0.786 | 5.1 | 88 ms |
| BM25 only (no model) | 0.634 | 0.50 | — | — | — |

¹ Scored with `api_weight` 0.6; the other rows were scored before API weighting
existed (weight 1.0). They will be re-scored at both weights (eval only, no
re-indexing). The 4B model is too slow on this GPU (GTX 1650, 4 GB) to index the
whole library — about 6 hours for the 15,503 chunks — so it is only a quality ceiling.

### Phase 2 — all docs sets (Gitea 28, Milvus 3.0, Next.js 16.4.5: 15,503 chunks, 60 questions) ²

| Model | Hybrid MRR | Hybrid MRR, scoped ³ | Dense MRR | BM25 MRR | Index time |
|---|---|---|---|---|---|
| embeddinggemma | 0.733 | 0.758 | **0.801** | 0.526 | 18 min |
| embeddinggemma-2 | 0.741 | 0.757 | 0.739 | 0.526 | 40 min |
| qwen3-embedding:0.6b | 0.708 | 0.704 | 0.667 | 0.526 | 61 min |
| nomic-embed-text | _interrupted: Ollama stopped halfway; rerun bakeoff.sh_ | | | | |

² All at `api_weight` 0.6. The question set covers Gitea and Milvus only; Next.js
is in the index as distractor text. ³ Scoped: each question limited to its library.

### What it shows so far

- Hybrid beats BM25 alone by a wide margin with every model.
- On the larger corpus, **embeddinggemma's meaning-only search beats its hybrid
  search** (0.801 vs 0.733): BM25 now adds noise for that model. To check once
  all models are in — it may favour weighting the two lists (Milvus's weighted
  ranker) over plain RRF, or changing `rrf_k`.
- The current default, qwen3-embedding:0.6b, scores lowest of the three on the
  full corpus so far, and indexes 3× slower than embeddinggemma — which matters
  every time a docs set is ingested.

## Limits

- Milvus Lite has only the `standard` analyzer — no stemming ("registering" won't
  keyword-match "registration"); meaning search covers that.
- BM25 word statistics are per storage segment, not global, in Milvus Lite.
- Indexing speed is bound by the GPU (GTX 1650, 4 GB). See the throughput table.
- Moving to Milvus Standalone 3.0 later (for the text highlighter, global BM25
  statistics, more analyzers) needs only a different URI in `config.py`; the
  schema and code are the same.
