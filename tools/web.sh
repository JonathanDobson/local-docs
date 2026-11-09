#!/usr/bin/env bash
# Start, stop or check the local-docs search page (search/web.py) in the background.
#   tools/web.sh start      # http://127.0.0.1:7710
#   tools/web.sh stop
#   tools/web.sh restart
#   tools/web.sh status
#   PORT=8000 tools/web.sh start
# Works from any directory. The PID and log live in .search/ (git-ignored).
# The page listens on 127.0.0.1 only. The Milvus Lite server it searches starts
# on first use and keeps running after `stop`; stop it with `python -m search down`.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${PORT:-7710}"
PIDFILE="$ROOT/.search/web.pid"
LOG="$ROOT/.search/web.log"
URL="http://127.0.0.1:$PORT"

pid() { [ -f "$PIDFILE" ] && cat "$PIDFILE"; }
running() { local p; p="$(pid)" && [ -n "$p" ] && kill -0 "$p" 2>/dev/null; }
answering() { curl -s -o /dev/null -m 2 "$URL/"; }

start() {
  if running; then echo "already running (pid $(pid)): $URL"; return 0; fi
  rm -f "$PIDFILE"
  if answering; then echo "port $PORT is already in use by another program; try PORT=... $0 start" >&2; return 1; fi
  [ -x "$ROOT/.venv/bin/python" ] || { echo "no .venv: run tools/setup.sh first" >&2; return 1; }
  mkdir -p "$ROOT/.search"
  cd "$ROOT" || return 1
  GRPC_VERBOSITY=NONE nohup "$ROOT/.venv/bin/python" -m search web --port "$PORT" >"$LOG" 2>&1 &
  echo $! >"$PIDFILE"
  for _ in $(seq 1 50); do  # up to 10 s
    if answering; then echo "started (pid $(pid)): $URL"; return 0; fi
    running || break
    sleep 0.2
  done
  echo "failed to start; last lines of $LOG:" >&2
  tail -5 "$LOG" >&2
  stop >/dev/null
  return 1
}

stop() {
  if ! running; then rm -f "$PIDFILE"; echo "not running"; return 0; fi
  local p; p="$(pid)"
  kill "$p"
  for _ in $(seq 1 25); do  # up to 5 s, then force
    kill -0 "$p" 2>/dev/null || { rm -f "$PIDFILE"; echo "stopped"; return 0; }
    sleep 0.2
  done
  kill -9 "$p" 2>/dev/null
  rm -f "$PIDFILE"
  echo "stopped (forced)"
}

status() {
  if running; then echo "running (pid $(pid)): $URL"; else echo "not running"; return 3; fi
}

case "${1:-}" in
  start) start ;;
  stop) stop ;;
  restart) stop >/dev/null; start ;;
  status) status ;;
  *) echo "usage: $0 start|stop|restart|status   (PORT=7710 by default)" >&2; exit 2 ;;
esac
