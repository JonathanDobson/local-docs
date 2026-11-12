#!/usr/bin/env bash
# Link this repo's skills into ~/.claude/skills so every Claude Code session can use them.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$DEST"
for skill in "$ROOT"/skills/*/; do
  name="$(basename "$skill")"
  if [ -e "$DEST/$name" ] && [ ! -L "$DEST/$name" ]; then
    echo "skip $name: $DEST/$name exists and is not a link" >&2; continue
  fi
  # Never silently repoint a link that belongs to something else (a skill of
  # the same name from another project). FORCE=1 overrides.
  if [ -L "$DEST/$name" ] && [ "$(readlink "$DEST/$name")" != "${skill%/}" ] && [ "${FORCE:-0}" != 1 ]; then
    echo "skip $name: $DEST/$name already links to $(readlink "$DEST/$name") (FORCE=1 to replace)" >&2; continue
  fi
  ln -sfn "${skill%/}" "$DEST/$name"
  echo "linked $DEST/$name -> ${skill%/}"
done
