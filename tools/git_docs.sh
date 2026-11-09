#!/usr/bin/env bash
# Copy one or more documentation folders out of a git repository at a tag/branch.
#
#   tools/git_docs.sh <repo-url> <ref> <dest-dir> <path>[=<subdir>] [...]
#
# Each <path> is copied into <dest-dir>/<subdir> (default: straight into
# <dest-dir>). One clone serves all paths. Example:
#   tools/git_docs.sh https://gitea.com/gitea/docs.git main libraries/gitea/28/content \
#       versioned_docs/version-28=docs runner-docs_versioned_docs/version-5=runner
#
# Uses a shallow, sparse, blob-less clone so only the requested folders are
# downloaded. Prints the resolved commit SHA on the last line (record it in
# manifest.json). Nothing from the repository is executed.
# To read a single file elsewhere in the repo (e.g. build config that defines
# version placeholders), fetch it directly instead, e.g.
#   gh api repos/OWNER/REPO/contents/PATH?ref=REF -q .content | base64 -d
set -euo pipefail
if [ $# -lt 4 ]; then
  sed -n '2,17p' "$0"; exit 2
fi
REPO="$1"; REF="$2"; DEST="$3"; shift 3
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/.staging"
WORK="$(mktemp -d "$ROOT/.staging/git.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

git -c advice.detachedHead=false clone --quiet --depth 1 --branch "$REF" \
    --filter=blob:none --sparse "$REPO" "$WORK/repo"
PATTERNS=()
for spec in "$@"; do
  p="${spec%%=*}"; p="${p%/}"
  [ "$p" = "." ] || PATTERNS+=("/$p/")
done
if [ ${#PATTERNS[@]} -gt 0 ]; then
  git -C "$WORK/repo" sparse-checkout set --no-cone "${PATTERNS[@]}"
fi

for spec in "$@"; do
  p="${spec%%=*}"; p="${p%/}"
  sub=""; [[ "$spec" == *=* ]] && sub="${spec#*=}"
  SRC="$WORK/repo/$p"
  [ -d "$SRC" ] || { echo "error: '$p' not found at $REF" >&2; exit 1; }
  OUT="$DEST${sub:+/$sub}"
  mkdir -p "$OUT"
  # -h dereferences symlinks so nothing in DEST points outside it.
  tar -C "$SRC" --exclude=.git -chf - . | tar -C "$OUT" -xf -
  echo "copied $(find "$SRC" -type f | wc -l) files: $p -> $OUT"
done
echo "commit $(git -C "$WORK/repo" rev-parse HEAD)"
