# Milvus 3.0 — overview

Milvus is an open-source vector database: it stores vectors (embeddings) with
scalar fields and runs similarity search, filtering, BM25 full text search and
hybrid search over them. This docs set covers the **Milvus 3.0** release line;
the newest release at ingest time is **v3.0.5** (2026-10-30), which pairs with
**PyMilvus 3.0.2** and **Milvus Lite 3.2.2**. Sources: the English docs from the
`v3.0.x` branch of `github.com/milvus-io/milvus-docs` (what milvus.io/docs
serves), the PyMilvus and RESTful API references for 3.0.x from
`github.com/milvus-io/web-content`, the Milvus Lite `v3.2.2` README and design
notes from `github.com/milvus-io/milvus-lite`, and GitHub release notes for
PyMilvus 3.0.x and Milvus Lite 3.x. The site's `{{var.*}}` placeholders were
filled in (e.g. `3.0.5`, `3.0.2`, `3.2.2`, endpoint `http://localhost:19530`,
token `root:Milvus`); see `manifest.json` `notes`.

## Layout

- `content/docs/` — the milvus.io docs, same folders as the source:
  - `about/` — overview, comparison, **limitations** (`limitations.md`), roadmap.
  - `getstarted/` — `install-overview.md` (Lite vs Standalone vs Distributed),
    `milvus_lite.md`, `quickstart.md`, `install_SDKs/`, Docker/Docker Compose/
    binary/Windows (`run-milvus-docker/`), Kubernetes Helm/Operator
    (`run-milvus-k8s/`, `standalone/`), GPU, offline install.
  - `userGuide/` — the main manual:
    - `collections/`, `schema/` (field types incl. `text.md`, `sparse_vector.md`,
      `json-*`, `nullable-and-default.md`, StructArray), `schema/analyzer/`
      (analyzers, `tokenizer/`, `filter/`, multi-language, file resources).
    - `indexes/` (one page per index type: `floating-vector/`, `sparse/`,
      `binary/`, `scalar/`, `gpu/`, `faiss.md`) and `manage-indexes/`.
    - `search-query-get/` — single-vector, filtered, range, grouping, hybrid
      (`multi-vector-search.md`), `full-text-search.md`, `keyword-match.md`
      (Text Match), `phrase-match.md`, `text-highlighter.md`,
      `use-partition-key.md`, iterators, aggregation, snapshots, `boolean/`
      (filter expression syntax).
    - `embeddings-reranking/embedding-function/` (server-side Function module:
      BM25, MinHash, text embedding providers) and `.../reranking/` (RRF,
      weighted, boost, decay, model rankers).
    - `insert-and-delete/`, `data-import/`, `storage-optimization/`, `tools/`
      (Backup, CDC, Birdwatcher, CLI, WebUI).
  - `adminGuide/` — config via Docker/Helm/Operator, dependencies (etcd, object
    storage, message queues incl. Woodpecker), RBAC/TLS/auth, monitoring,
    scaling, upgrades, cloud deployments.
  - `reference/` — architecture, `index.md` (in-memory index list),
    `scalar_index.md`, `disk_index.md`, `multi_tenancy.md`, `schema.md`,
    consistency, glossary, and `sys_config/` (every `milvus.yaml` section).
  - `embeddings/`, `rerankers/` — the client-side PyMilvus model library
    (`pymilvus[model]`) embedding and rerank helpers.
  - `tutorials/`, `integrations/` (LangChain, LlamaIndex, Haystack, Ollama, …),
    `aiTools/` (prompts and guides for AI coding agents), `faq/`.
  - `release_notes.md` — Milvus server release notes v3.0-beta to v3.0.5.
  - `fragments/` — shared snippets the site includes in other pages (already
    inlined where used).
- `content/api-reference/pymilvus/` — PyMilvus 3.0.x reference: `MilvusClient/`
  (by area: `Collections/`, `Vector/`, `Management/`, `Partitions/`,
  `Database/`, `Authentication/`, `ResourceGroup/`, `Snapshot/`, `Client/`),
  `ORM/` (older ORM-style API), `EmbeddingModels/`, `Rerankers/`,
  `DataImport/`, `FileResource/`, `Exceptions/`.
- `content/api-reference/restful/` — RESTful API (`v2/` current, `v1/`
  deprecated), one page per operation with method, path, parameters, body and
  examples; `About.md` explains endpoints and auth.
- `content/milvus-lite/` — Milvus Lite 3.2.2 `README.md` (supported features,
  known limitations, BM25, sparse search, dump) and `docs/` design notes
  (`fts-design.md`, `sparse-vector-design.md`, `index-design.md`, …).
- `content/release-notes/` — `pymilvus/` (v3.0.0–v3.0.2) and `milvus-lite/`
  (v3.0.0–v3.2.2).

## Where to look for…

| Task | File |
|---|---|
| Choose Lite vs Standalone vs Distributed; feature comparison table | `content/docs/getstarted/install-overview.md` |
| Run Milvus Lite (`MilvusClient("./x.db")`), its limits, migrating off it | `content/docs/getstarted/milvus_lite.md`, `content/milvus-lite/README.md` |
| Run Milvus Standalone with Docker Compose | `content/docs/getstarted/run-milvus-docker/install_standalone-docker-compose.md` |
| Connect a client, URI and token | `content/docs/getstarted/connect-to-milvus-server.md` |
| BM25 full text search (schema, BM25 function, `SPARSE_INVERTED_INDEX` with metric `BM25`, `bm25_k1`/`bm25_b`) | `content/docs/userGuide/search-query-get/full-text-search.md`, `.../embedding-function/bm25-function.md` |
| Analyzers, tokenizers, filters (stop words, stemming, synonyms) | `content/docs/userGuide/schema/analyzer/` (start at `analyzer-overview.md`, `choose-the-right-analyzer-for-your-use-case.md`) |
| Keyword filtering with `TEXT_MATCH`, phrase matching | `content/docs/userGuide/search-query-get/keyword-match.md`, `phrase-match.md` |
| Highlight matched terms in results | `content/docs/userGuide/search-query-get/text-highlighter.md` |
| Hybrid search (dense + sparse/BM25) and fusion | `content/docs/userGuide/search-query-get/multi-vector-search.md`, `.../reranking/rrf-ranker.md`, `weighted-ranker.md` |
| Model rerankers (TEI, vLLM, Cohere, Voyage, …), boost and decay rankers | `content/docs/userGuide/embeddings-reranking/reranking/` (`model-ranker-overview.md`, `boost-ranker.md`, `decay-ranker-overview.md`) |
| Server-side text embedding functions and provider credentials | `content/docs/userGuide/embeddings-reranking/embedding-function/embedding-function-overview.md` + one page per provider |
| Pick a vector index; per-index parameters | `content/docs/userGuide/indexes/index-explained.md`, `content/docs/reference/index.md`, `content/docs/userGuide/indexes/floating-vector/*.md` |
| Sparse vectors | `content/docs/userGuide/schema/sparse_vector.md`, `content/docs/userGuide/indexes/sparse/sparse-inverted-index.md` |
| JSON fields, JSON path indexes, JSON shredding | `content/docs/userGuide/schema/json-field-overview.md`, `json-indexing.md`, `json-shredding.md` |
| Multi-tenancy, partition keys | `content/docs/reference/multi_tenancy.md`, `content/docs/userGuide/search-query-get/use-partition-key.md` |
| A PyMilvus method's signature (e.g. `search`, `hybrid_search`, `create_index`) | `content/api-reference/pymilvus/MilvusClient/` (e.g. `MilvusClient/Vector/hybrid_search.md`; `rg -l "^# hybrid_search\(" content/api-reference/pymilvus`) |
| A RESTful endpoint | `content/api-reference/restful/v2/<Area> (v2)/<Operation>.md` |
| A `milvus.yaml` setting | `content/docs/reference/sys_config/configure_<section>.md` |
| What changed / upgrade notes | `content/docs/release_notes.md`, `content/docs/adminGuide/upgrade_milvus_standalone-docker.md` |
| Known limits (name lengths, max dims, …) | `content/docs/about/limitations.md` |

## Version notes

From `content/docs/release_notes.md` (v3.0.0 section) unless noted:

- New in 3.0: External Collection (query Parquet/Lance/Iceberg/Vortex data in
  place), Snapshot, Storage V3 ("Loon"), query/search ORDER BY, query
  aggregation and Search Aggregation, MinHash function + `MINHASH_LSH`, nullable
  vectors, entity TTL, FileResource (cluster-managed dictionaries, synonym and
  stop-word lists for analyzers), Force Merge, Function Chain reranking,
  `TEXT` long-text fields, FAISS index passthrough, sparse index overhaul
  (SINDI, Block-Max WAND, Block-Max MaxScore).
- **Storage V3 is disabled by default**; Snapshot and `TEXT` fields need
  `common.storage.useLoonFFI` set to `true` (`content/docs/userGuide/schema/text.md`).
- New index algorithms are opt-in: raise `dataCoord.targetVecIndexVersion`
  (and the scalar equivalent).
- 2.6 → 3.0 rollback is supported until a feature that changes the serialized
  data format is used.
- GPU images moved to CUDA 12.9.
- **Milvus Lite 3.x is a pure-Python rewrite** and cannot open 2.x `.db` files;
  `MilvusClient("./x.db")` now creates a directory. Export with
  `milvus-lite dump` (`content/docs/getstarted/milvus_lite.md`).
- Many pages carry a `beta:` front-matter tag with the version that introduced
  the feature (e.g. Phrase Match 2.5.17+, Boost Ranker 2.6.2+, Text Highlighter
  2.6.8+, MinHash Function / Search Aggregation / Text Field 3.0.x).

## Search tips

- Config file is `milvus.yaml`; sections are documented in
  `reference/sys_config/configure_<section>.md`.
- "Function" is Milvus's server-side transform: `FunctionType.BM25`,
  `FunctionType.TEXTEMBEDDING` (REST type `TEXTEMBEDDING`), `FunctionType.RERANK`,
  MinHash. Rerankers are Functions with `params.reranker` = `"model"`,
  `"decay"`, …
- "Text Match" = `TEXT_MATCH(field, '...')` filter (needs `enable_match=True`);
  "Full Text Search" = BM25 ranking (needs `enable_analyzer=True` + BM25
  function). They are different features.
- "Hybrid search" is `hybrid_search()` with several `AnnSearchRequest`s and a
  ranker; the file is `multi-vector-search.md`.
- "Partition Key" (`is_partition_key=True`) is the recommended pattern for many
  tenants; see `multi_tenancy.md`.
- `embeddings/` and `rerankers/` at the top of the docs are the **client-side**
  `pymilvus[model]` helpers; `userGuide/embeddings-reranking/` is the
  **server-side** Function module. Different things with similar names.
- Milvus Lite is configured by the `.db` path in `MilvusClient`; it has no
  `milvus.yaml`. Its feature list is in `content/milvus-lite/README.md`
  ("Supported Features", "Known Limitations").
- Code samples are multi-language blocks (Python, Java, Go, NodeJS, C++, cURL);
  grep for ```` ```python ```` to find the Python one.
