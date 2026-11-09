#!/usr/bin/env bash
# One-time (idempotent) setup: creates local-docs/.venv with the HTML->Markdown
# and YAML libraries the Python tools need. Safe to re-run.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# milvus-lite needs Python 3.10+; macOS's /usr/bin/python3 is 3.9, so pick the
# first suitable interpreter (override with PYTHON=/path/to/python).
ok() { "$1" -c 'import sys; sys.exit(sys.version_info < (3, 10))' 2>/dev/null; }
if [ -x "$ROOT/.venv/bin/python" ] && ! ok "$ROOT/.venv/bin/python"; then
  echo "removing .venv: built with Python older than 3.10"
  rm -rf "$ROOT/.venv"
fi
if [ ! -x "$ROOT/.venv/bin/python" ]; then
  PY="${PYTHON:-}"
  if [ -z "$PY" ]; then
    for c in python3.13 python3.12 python3.11 python3.10 python3; do
      if command -v "$c" >/dev/null && ok "$c"; then PY="$c"; break; fi
    done
  fi
  [ -n "$PY" ] || { echo "need Python 3.10+ (set PYTHON=...)" >&2; exit 1; }
  "$PY" -m venv "$ROOT/.venv"
fi
"$ROOT/.venv/bin/pip" install --quiet --upgrade pip
"$ROOT/.venv/bin/pip" install --quiet -r "$ROOT/tools/requirements.txt"
echo "ready: $ROOT/.venv/bin/python"
