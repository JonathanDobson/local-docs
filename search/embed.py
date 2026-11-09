"""Embeddings from a local Ollama server (POST /api/embed)."""
from __future__ import annotations

import http.client
import json
import time
import urllib.error
import urllib.request

from search.config import Settings, spec_for


class Embedder:
    def __init__(self, s: Settings):
        self.s = s
        self.spec = spec_for(s.model)
        self._dim: int | None = None

    def _call(self, texts: list[str]) -> list[list[float]]:
        body = {"model": self.s.model, "input": texts, "truncate": True, "keep_alive": "10m"}
        if self.s.dimensions:
            body["dimensions"] = self.s.dimensions
        req = urllib.request.Request(f"{self.s.ollama_url}/api/embed", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=600) as r:
                    return json.loads(r.read())["embeddings"]
            except (urllib.error.URLError, http.client.HTTPException, ConnectionError) as exc:  # incl. Ollama dropping mid-request
                if attempt == 3:
                    raise SystemExit(f"Ollama embed failed at {self.s.ollama_url}: {exc} — is `ollama serve` running "
                                     f"and is '{self.s.model}' pulled?")
                time.sleep(2 * (attempt + 1))
        raise AssertionError

    @property
    def dim(self) -> int:
        if self._dim is None:
            self._dim = len(self._call(["dimension probe"])[0])
        return self._dim

    def documents(self, items: list[tuple[str, str]], batch: int = 32) -> list[list[float]]:
        """items: (title, text) pairs."""
        texts = [self.spec.doc.format(title=t or "none", text=x) for t, x in items]
        out: list[list[float]] = []
        for i in range(0, len(texts), batch):
            out.extend(self._call(texts[i:i + batch]))
        return out

    def query(self, q: str) -> list[float]:
        return self._call([self.spec.query.format(q=q)])[0]
