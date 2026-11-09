#!/usr/bin/env bash
# One-time (idempotent) setup: creates local-docs/.venv with the HTML->Markdown
# and YAML libraries the Python tools need. Safe to re-run.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ ! -x "$ROOT/.venv/bin/python" ]; then
  python3 -m venv "$ROOT/.venv"
fi
"$ROOT/.venv/bin/pip" install --quiet --upgrade pip
"$ROOT/.venv/bin/pip" install --quiet -r "$ROOT/tools/requirements.txt"
echo "ready: $ROOT/.venv/bin/python"
