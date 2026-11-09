#!/usr/bin/env bash
# Compare embedding models on the local-docs question set.
#   search/eval/bakeoff.sh            # phase 1 (Gitea, all models) then phase 2 (everything, small models)
#   BAKEOFF_BIG= search/eval/bakeoff.sh   # same, without qwen3-embedding:4b
# Results land in .search/eval/*.json; summarise with: .venv/bin/python -m search.eval.report
set -uo pipefail
cd "$(dirname "$0")/../.."
PY=.venv/bin/python
export GRPC_VERBOSITY=NONE
SMALL="embeddinggemma embeddinggemma-2 qwen3-embedding:0.6b nomic-embed-text"
# Phase-1-only quality ceiling; BAKEOFF_BIG="" skips it (slow, 2.5 GB download).
BIG="${BAKEOFF_BIG-qwen3-embedding:4b}"
echo "== phase 1: Gitea only, all models"
for m in $SMALL $BIG; do
  echo "-- $m"
  LOCALDOCS_MODEL=$m $PY -m search index gitea/28 --quiet || { echo "index failed: $m"; continue; }
  LOCALDOCS_MODEL=$m $PY -m search eval --library gitea
done
echo "== phase 2: all docs sets, small models"
for m in $SMALL; do
  echo "-- $m"
  LOCALDOCS_MODEL=$m $PY -m search index --quiet || { echo "index failed: $m"; continue; }
  LOCALDOCS_MODEL=$m $PY -m search eval
  LOCALDOCS_MODEL=$m $PY -m search eval --scoped --modes hybrid
done
echo "== done"
