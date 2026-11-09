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
| Search | Top 50 from each of BM25 and the dense index, filtered by library/version (and optionally doc type), merged with RRF (k=60). API reference results are then scaled by `api_weight` (0.6) unless the question looks like an API question. | [store.py](store.py) |

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

_Filled in from the comparison run — see below._

## Limits

- Milvus Lite has only the `standard` analyzer — no stemming ("registering" won't
  keyword-match "registration"); meaning search covers that.
- BM25 word statistics are per storage segment, not global, in Milvus Lite.
- Indexing speed is bound by the GPU (GTX 1650, 4 GB). See the throughput table.
- Moving to Milvus Standalone 3.0 later (for the text highlighter, global BM25
  statistics, more analyzers) needs only a different URI in `config.py`; the
  schema and code are the same.
