"""Milvus Lite storage: the local server, the collection schema, writes and hybrid search.

One Milvus Lite server process (bound to 127.0.0.1 only — Milvus Lite has no
authentication) serves the indexer and every Claude session's MCP server.
"""
from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
from dataclasses import dataclass

from pymilvus import AnnSearchRequest, DataType, Function, FunctionType, MilvusClient

from search.config import DATA, ROOT, Settings

TEXT_MAX = 8192
FIELDS_OUT = ["path", "library", "version", "breadcrumb", "start_line", "end_line", "text", "source_url"]


def _port_open(port: int) -> bool:
    with socket.socket() as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


def ensure_server(s: Settings, wait: float = 60) -> None:
    """Start the Milvus Lite server in the background if it isn't running."""
    if _port_open(s.milvus_port):
        return
    DATA.mkdir(parents=True, exist_ok=True)
    exe = os.path.join(os.path.dirname(sys.executable), "milvus-lite")
    log = open(DATA / "milvus-lite.log", "ab")
    proc = subprocess.Popen(
        [exe, "server", "--data-dir", str(DATA / "milvus"), "--host", "127.0.0.1", "--port", str(s.milvus_port)],
        stdout=log, stderr=log, stdin=subprocess.DEVNULL, start_new_session=True, cwd=ROOT)
    (DATA / "milvus-lite.pid").write_text(str(proc.pid))
    deadline = time.time() + wait
    while time.time() < deadline:
        if _port_open(s.milvus_port):
            return
        if proc.poll() is not None:
            raise SystemExit(f"Milvus Lite server exited; see {DATA / 'milvus-lite.log'}")
        time.sleep(0.3)
    raise SystemExit(f"Milvus Lite server did not start within {wait}s; see {DATA / 'milvus-lite.log'}")


def stop_server() -> bool:
    pidf = DATA / "milvus-lite.pid"
    if not pidf.exists():
        return False
    try:
        os.kill(int(pidf.read_text()), 15)
    except ProcessLookupError:
        pass
    pidf.unlink()
    return True


def client(s: Settings) -> MilvusClient:
    ensure_server(s)
    return MilvusClient(uri=s.uri)


def create_collection(c: MilvusClient, name: str, dim: int) -> None:
    schema = c.create_schema(auto_id=False)
    schema.add_field("id", DataType.VARCHAR, is_primary=True, max_length=32)
    schema.add_field("library", DataType.VARCHAR, max_length=64, is_partition_key=True)
    schema.add_field("version", DataType.VARCHAR, max_length=32)
    schema.add_field("path", DataType.VARCHAR, max_length=512)
    schema.add_field("file_hash", DataType.VARCHAR, max_length=40)
    schema.add_field("breadcrumb", DataType.VARCHAR, max_length=1024)
    schema.add_field("start_line", DataType.INT32)
    schema.add_field("end_line", DataType.INT32)
    schema.add_field("source_url", DataType.VARCHAR, max_length=1024)
    schema.add_field("text", DataType.VARCHAR, max_length=TEXT_MAX)
    # Keyword-search input: breadcrumb + text + identifier parts. Lite offers only
    # the "standard" analyzer (lower-cases, splits on word boundaries, no stemming).
    schema.add_field("lexical", DataType.VARCHAR, max_length=TEXT_MAX * 2, enable_analyzer=True,
                     analyzer_params={"type": "standard"})
    schema.add_field("dense", DataType.FLOAT_VECTOR, dim=dim)
    schema.add_field("sparse", DataType.SPARSE_FLOAT_VECTOR)
    schema.add_function(Function(name="bm25", input_field_names=["lexical"], output_field_names=["sparse"],
                                 function_type=FunctionType.BM25))
    ip = c.prepare_index_params()
    ip.add_index("dense", index_type="HNSW", metric_type="COSINE", params={"M": 16, "efConstruction": 200})
    ip.add_index("sparse", index_type="SPARSE_INVERTED_INDEX", metric_type="BM25",
                 params={"bm25_k1": 1.2, "bm25_b": 0.75})
    ip.add_index("path", index_type="INVERTED")
    ip.add_index("version", index_type="INVERTED")
    c.create_collection(name, schema=schema, index_params=ip)
    c.load_collection(name)


def _q(v: str) -> str:
    return "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'"


def scope_filter(library: str | None = None, version: str | None = None, path: str | None = None) -> str:
    parts = []
    if library:
        parts.append(f"library == {_q(library)}")
    if version:
        parts.append(f"version == {_q(version)}")
    if path:
        parts.append(f"path == {_q(path)}")
    return " and ".join(parts)


@dataclass
class Hit:
    score: float
    path: str
    library: str
    version: str
    breadcrumb: str
    start_line: int
    end_line: int
    text: str
    source_url: str


def _hits(res) -> list[Hit]:
    out = []
    for h in res[0]:
        e = h.get("entity", h)
        out.append(Hit(score=float(h["distance"]), **{k: e.get(k) for k in FIELDS_OUT}))
    return out


def search(c: MilvusClient, s: Settings, query_vec: list[float] | None, query_text: str, *,
           mode: str = "hybrid", library: str | None = None, version: str | None = None,
           limit: int = 10, candidates: int = 50) -> list[Hit]:
    expr = scope_filter(library, version)
    if mode == "dense":
        res = c.search(s.collection, data=[query_vec], anns_field="dense", limit=limit, filter=expr,
                       output_fields=FIELDS_OUT, search_params={"metric_type": "COSINE", "params": {"ef": 128}})
        return _hits(res)
    if mode == "bm25":
        res = c.search(s.collection, data=[query_text], anns_field="sparse", limit=limit, filter=expr,
                       output_fields=FIELDS_OUT, search_params={"metric_type": "BM25"})
        return _hits(res)
    reqs = [AnnSearchRequest(data=[query_vec], anns_field="dense", param={"ef": 128}, limit=candidates, expr=expr),
            AnnSearchRequest(data=[query_text], anns_field="sparse", param={}, limit=candidates, expr=expr)]
    ranker = Function(name="rrf", input_field_names=[], function_type=FunctionType.RERANK,
                      params={"reranker": "rrf", "k": s.rrf_k})
    return _hits(c.hybrid_search(s.collection, reqs=reqs, ranker=ranker, limit=limit, output_fields=FIELDS_OUT))
