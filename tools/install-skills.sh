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
  ln -sfn "${skill%/}" "$DEST/$name"
  echo "linked $DEST/$name -> ${skill%/}"
done
