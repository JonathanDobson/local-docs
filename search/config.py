"""Settings, paths and the embedding-model registry.

`search/settings.json` holds the chosen model; environment variables
LOCALDOCS_MODEL / LOCALDOCS_DIMS override it (used by the model comparison).
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBS = ROOT / "libraries"
DATA = ROOT / ".search"
SETTINGS = Path(__file__).resolve().parent / "settings.json"

# Query/document wording each model was trained with. Getting this wrong
# silently costs quality, so it lives in one place and the indexer and the
# search both use it.
QWEN_TASK = ("Given a question about software documentation, retrieve the "
             "documentation passages that answer it")


@dataclass(frozen=True)
class ModelSpec:
    query: str      # format string with {q}
    doc: str        # format string with {title} and {text}
    native_dims: int


MODELS: dict[str, ModelSpec] = {
    "qwen3-embedding": ModelSpec(f"Instruct: {QWEN_TASK}\nQuery: {{q}}", "{title}\n\n{text}", 0),
    "embeddinggemma": ModelSpec("task: search result | query: {q}", "title: {title} | text: {text}", 768),
    "embeddinggemma-2": ModelSpec("task: search result | query: {q}", "title: {title} | text: {text}", 512),
    "nomic-embed-text": ModelSpec("search_query: {q}", "search_document: {title}\n\n{text}", 768),
    "nomic-embed-text-v2-moe": ModelSpec("search_query: {q}", "search_document: {title}\n\n{text}", 768),
}


def model_family(model: str) -> str:
    return model.split(":", 1)[0]


def spec_for(model: str) -> ModelSpec:
    fam = model_family(model)
    if fam not in MODELS:
        raise SystemExit(f"no prompt format registered for '{model}' — add it to MODELS in search/config.py")
    return MODELS[fam]


@dataclass(frozen=True)
class Settings:
    model: str
    dimensions: int | None
    ollama_url: str
    milvus_port: int
    rrf_k: int                  # RRF k for natural-language queries (lower = top ranks count for more)
    api_weight: float
    dense_weight: float = 1.0   # how much the meaning list counts against the keyword list, for natural-language queries
    ident_rrf_k: int = 60       # RRF k for identifier-shaped queries (keywords and meaning weighted equally)
    intro_weight: float = 1.0   # hybrid score multiplier for a page's intro chunk (text before its first heading)
    dup_sim: float = 0.97       # hits whose vectors are at least this similar are collapsed into one
    sure_sim: float = 0.0       # meaning-similarity at or above which a hit is labelled "strong" (0 = no labels)
    weak_sim: float = 0.0       # below this a hit is labelled "weak"; if the top hit is weak, there is no confident match

    @property
    def uri(self) -> str:
        return f"http://127.0.0.1:{self.milvus_port}"

    @property
    def collection(self) -> str:
        """One collection per model+size, so models can be compared side by side."""
        slug = re.sub(r"[^a-z0-9]+", "_", self.model.lower()).strip("_")
        return f"docs_{slug}" + (f"_d{self.dimensions}" if self.dimensions else "")


def load() -> Settings:
    raw = json.loads(SETTINGS.read_text())
    model = os.environ.get("LOCALDOCS_MODEL", raw["model"])
    dims_env = os.environ.get("LOCALDOCS_DIMS")
    if dims_env is not None:
        dims = int(dims_env) or None
    else:
        dims = raw.get("dimensions") if model == raw["model"] else None
    api_weight = float(os.environ.get("LOCALDOCS_API_WEIGHT", raw.get("api_weight", 1.0)))
    env = lambda k, d: float(os.environ.get(f"LOCALDOCS_{k.upper()}", raw.get(k, d)))
    # Similarity thresholds belong to one model; for any other model, labels are off.
    same = model == raw["model"]
    return Settings(model=model, dimensions=dims, ollama_url=raw["ollama_url"],
                    milvus_port=int(raw["milvus_port"]), rrf_k=int(env("rrf_k", 60)), api_weight=api_weight,
                    dense_weight=env("dense_weight", 1.0), ident_rrf_k=int(env("ident_rrf_k", 60)),
                    intro_weight=env("intro_weight", 1.0), dup_sim=env("dup_sim", 0.97),
                    sure_sim=env("sure_sim", 0.0) if same else 0.0, weak_sim=env("weak_sim", 0.0) if same else 0.0)


_manifests: dict[str, dict] = {}


def provenance(path: str) -> str:
    """Where a docs file came from, for citing: "<ref> @<commit>" from the manifest
    source whose `dest` folder holds the file (a file `dest` counts as its folder),
    else "ingested <date>". `path` is relative to the local-docs root."""
    parts = path.split("/")
    if len(parts) < 4 or parts[0] != "libraries":
        return ""
    key = "/".join(parts[1:3])
    if key not in _manifests:
        try:
            _manifests[key] = json.loads((LIBS / key / "manifest.json").read_text())
        except (OSError, ValueError):
            _manifests[key] = {}
    m = _manifests[key]
    rel = "/".join(parts[3:])
    best, best_len = None, -1
    for src in m.get("sources", []):
        dest = (src.get("dest") or "").rstrip("/")
        if "." in dest.rsplit("/", 1)[-1]:      # a file, e.g. api/v1-openapi3.json
            dest = dest.rsplit("/", 1)[0] if "/" in dest else ""
        if (not dest or rel == dest or rel.startswith(dest + "/")) and len(dest) > best_len:
            best, best_len = src, len(dest)
    if best and best.get("commit"):
        return f"{best.get('ref') or 'commit'} @{best['commit'][:7]}"
    return f"ingested {m['ingested_at']}" if m.get("ingested_at") else ""
