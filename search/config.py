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
    rrf_k: int
    api_weight: float

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
    return Settings(model=model, dimensions=dims, ollama_url=raw["ollama_url"],
                    milvus_port=int(raw["milvus_port"]), rrf_k=int(raw["rrf_k"]), api_weight=api_weight)
