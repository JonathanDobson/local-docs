#!/usr/bin/env bash
# Launch the docs-library MCP server (stdio). Claude Code runs this; it works from any directory.
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 1
export GRPC_VERBOSITY=NONE
exec "$ROOT/.venv/bin/python" -m search mcp
