"""Local web page for searching local-docs by hand.

  .venv/bin/python -m search web            # http://127.0.0.1:7710
  .venv/bin/python -m search web --port 8000

Binds to 127.0.0.1 only and accepts only localhost Host headers. Standard
library HTTP server; shares the Milvus Lite index with the MCP server.
"""
from __future__ import annotations

import json
import os
import threading
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

os.environ.setdefault("GRPC_VERBOSITY", "NONE")

from search import config  # noqa: E402

PAGE = Path(__file__).with_name("web.html")
STATIC = Path(__file__).with_name("static")
STATIC_FILES = {"marked.umd.js": "text/javascript; charset=utf-8",
                "purify.min.js": "text/javascript; charset=utf-8"}
_lock = threading.Lock()
_deps: dict = {}


def _get_deps():
    if not _deps:
        from search.embed import Embedder
        from search.store import client
        s = config.load()
        _deps.update(s=s, emb=Embedder(s), client=client(s))
    return _deps


def libraries() -> list[dict]:
    out = []
    for mf in sorted(config.LIBS.glob("*/*/manifest.json")):
        m = json.loads(mf.read_text())
        out.append({"slug": mf.parent.parent.name, "version": mf.parent.name, "name": m.get("name"),
                    "release": m.get("release"), "summary": m.get("summary")})
    return out


def do_search(q: str, library: str | None, version: str | None, k: int, mode: str,
              doc_type: str | None = None) -> dict:
    from search.store import search
    d = _get_deps()
    with _lock:
        vec = None if mode == "bm25" else d["emb"].query(q)
        hits = search(d["client"], d["s"], vec, q, mode=mode, library=library, version=version,
                      doc_type=doc_type, limit=k)
    return {"model": d["s"].model, "mode": mode,
            "thresholds": {"strong": d["s"].sure_sim, "weak": d["s"].weak_sim},
            "hits": [{**{k: v for k, v in asdict(h).items() if k != "vec"}, "source": config.provenance(h.path)}
                     for h in hits]}


def read_file(path: str) -> dict | None:
    target = (config.ROOT / path).resolve()
    if config.LIBS.resolve() not in target.parents or not target.is_file():
        return None
    return {"path": path, "lines": target.read_text(encoding="utf-8", errors="replace").splitlines()}


class Handler(BaseHTTPRequestHandler):
    server_version = "local-docs"

    def log_message(self, fmt, *args):  # keep the terminal quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy",
                         "default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'unsafe-inline'; "
                         "connect-src 'self'; img-src 'self' data:")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj).encode(), "application/json; charset=utf-8")

    def do_GET(self):  # noqa: N802
        # Refuse requests addressed to other host names (DNS-rebinding protection).
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0]
        if host not in ("127.0.0.1", "localhost"):
            return self._send(403, b"forbidden", "text/plain")
        url = urlsplit(self.path)
        qs = {k: v[0] for k, v in parse_qs(url.query).items()}
        try:
            if url.path in ("/", "/view"):
                return self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
            if url.path.startswith("/static/"):
                name = url.path.removeprefix("/static/")
                if name not in STATIC_FILES:
                    return self._send(404, b"not found", "text/plain")
                return self._send(200, (STATIC / name).read_bytes(), STATIC_FILES[name])
            if url.path == "/api/libraries":
                return self._json(libraries())
            if url.path == "/api/search":
                q = qs.get("q", "").strip()
                if not q:
                    return self._json({"hits": []})
                mode = qs.get("mode", "hybrid")
                mode = mode if mode in ("hybrid", "dense", "bm25") else "hybrid"
                k = max(1, min(int(qs.get("k", "10") or 10), 50))
                dt = qs.get("type") or None
                dt = dt if dt in ("guide", "api", "release-notes") else None
                return self._json(do_search(q, qs.get("library") or None, qs.get("version") or None, k, mode, dt))
            if url.path == "/api/file":
                f = read_file(qs.get("path", ""))
                return self._json(f) if f else self._json({"error": "not a file under libraries/"}, 404)
            return self._send(404, b"not found", "text/plain")
        except SystemExit as exc:  # embedder/store report setup problems this way
            return self._json({"error": str(exc)}, 503)
        except Exception as exc:  # noqa: BLE001
            return self._json({"error": f"{type(exc).__name__}: {exc}"}, 500)


def serve(port: int = 7710) -> None:
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"local-docs search: http://127.0.0.1:{port}  (Ctrl+C to stop)", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
