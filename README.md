# local-docs

An offline library of official documentation — libraries, packages, products and
APIs — stored by name and version, so Claude agents can look things up in the
exact docs for the version you use instead of relying on memory.

**New to the vocabulary? Read [GLOSSARY.md](GLOSSARY.md).** Catalogue of what's
here: **[INDEX.md](INDEX.md)**.

## Using it

In any Claude Code session, in any project:

| You say | What happens |
|---|---|
| "ingest the gitea 28 or later documentation into local-docs" | The `local-docs-ingest` skill works out the exact release, finds the official docs source, downloads and cleans it, writes a manifest and overview, and updates `INDEX.md`. |
| "refresh the zod docs in local-docs" | Same, replacing that version's copy. |
| "check local-docs for how Gitea Actions runners register" | The `local-docs` skill finds the right docs set and version, searches it, and cites the files it used. |

Claude also consults local-docs on its own when a task depends on a tool listed
in `INDEX.md` (see the pointer in `~/.claude/CLAUDE.md`).

## Searching

Every docs set is indexed for **hybrid search** — keyword (BM25) and meaning
(embeddings from a local Ollama model), stored in Milvus Lite — so agents can ask
plain questions *or* look up exact identifiers. Agents use it through the
`local-docs` MCP server (`docs_search`, `docs_read`, `docs_list`); people can use
the command line:

```bash
.venv/bin/python -m search search "how do I stop people signing up" -l gitea
```

Or search in a browser — start the page, then open http://127.0.0.1:7710:

```bash
.venv/bin/python -m search web
```

Details, model choice and test results: [search/README.md](search/README.md).

## How docs get in

The ingest skill tries sources in this order and records which it used:

1. Markdown docs in the project's git repo at the release tag/branch (`tools/git_docs.sh`)
2. An `llms-full.txt` file published by the docs site
3. Docs bundled inside the released package
4. A polite crawl of the versioned docs website, converted to Markdown (`tools/crawl.py`)
5. For APIs, also the OpenAPI/Swagger spec, plus generated per-endpoint pages (`tools/openapi2md.py`)

`tools/finalize.py` validates each set, writes its `TOC.md`, and rebuilds `INDEX.md`.

## Setup (already done on this machine)

```bash
tools/setup.sh          # Python virtualenv for crawl.py / openapi2md.py
tools/install-skills.sh # link the two skills into ~/.claude/skills
.venv/bin/python -m search index   # build the search index (Ollama must be running)
claude mcp add --scope user local-docs -- ~/local-docs/tools/docs-mcp.sh
```

## Layout

See [CLAUDE.md](CLAUDE.md#layout).

## Licence

This project's own code and docs are [MIT](LICENSE). Everything under
`libraries/` is third-party documentation redistributed under its own licence —
see each docs set's `manifest.json` — and belongs to its authors.
