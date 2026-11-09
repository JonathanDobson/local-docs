#!/usr/bin/env python3
"""Turn an OpenAPI 3 / Swagger 2 spec into greppable Markdown.

  .venv/bin/python tools/openapi2md.py <spec.json|spec.yaml> <out-dir> \
      [--base-path /api/v1] [--version 28.3.0]

--base-path / --version override what the spec says, for specs that ship
build-time placeholders (e.g. "/GITEA-API-APP-SUBURL/api/v1"). The spec file
itself is never modified.

Writes one file per tag (endpoints/<tag>.md: method, path, summary,
parameters, request body, responses) plus schemas.md (every model and its
fields). Keep the original spec next to it; the Markdown is for searching and
reading, the spec is the source of truth.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

METHODS = ["get", "post", "put", "patch", "delete", "head", "options"]


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        try:
            import yaml
        except ImportError:
            sys.exit("pyyaml missing: run tools/setup.sh and use .venv/bin/python")
        return yaml.safe_load(text)
    return json.loads(text)


def ref_name(schema: dict | None) -> str:
    if not schema:
        return ""
    if "$ref" in schema:
        return "`" + schema["$ref"].rsplit("/", 1)[-1] + "`"
    t = schema.get("type", "")
    if t == "array":
        return f"array of {ref_name(schema.get('items'))}"
    if "allOf" in schema or "oneOf" in schema or "anyOf" in schema:
        key = next(k for k in ("allOf", "oneOf", "anyOf") if k in schema)
        return f"{key}(" + ", ".join(ref_name(s) for s in schema[key]) + ")"
    fmt = schema.get("format")
    enum = schema.get("enum")
    s = t or "object"
    if fmt:
        s += f" ({fmt})"
    if enum:
        s += " enum: " + ", ".join(map(str, enum[:12]))
    return s


def resolve(spec: dict, obj: dict) -> tuple[dict, str]:
    """Follow a local $ref (e.g. #/components/responses/X); return (target, name)."""
    seen = 0
    name = ""
    while isinstance(obj, dict) and "$ref" in obj and obj["$ref"].startswith("#/") and seen < 10:
        name = obj["$ref"].rsplit("/", 1)[-1]
        node = spec
        for part in obj["$ref"][2:].split("/"):
            node = node.get(part, {}) if isinstance(node, dict) else {}
        obj, seen = node, seen + 1
    return obj, name


def cell(text) -> str:
    return re.sub(r"\s+", " ", str(text or "")).replace("|", "\\|").strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--base-path", help="path prefix to show before every endpoint")
    ap.add_argument("--version", help="API version to show in headings")
    args = ap.parse_args()
    spec = load(args.spec)
    out = args.out
    (out / "endpoints").mkdir(parents=True, exist_ok=True)
    swagger2 = "swagger" in spec
    if args.base_path is not None:
        base = args.base_path.rstrip("/")
    elif swagger2:
        base = spec.get("basePath", "").rstrip("/")
    else:
        servers = spec.get("servers") or [{}]
        base = re.sub(r"^[a-z]+://[^/]+", "", servers[0].get("url", "")).rstrip("/")
    info = dict(spec.get("info", {}))
    if args.version:
        info["version"] = args.version

    by_tag: dict[str, list[str]] = defaultdict(list)
    for path, item in (spec.get("paths") or {}).items():
        shared = item.get("parameters", [])
        for method in METHODS:
            op = item.get(method)
            if not op:
                continue
            tag = (op.get("tags") or ["untagged"])[0]
            lines = [f"## {method.upper()} {base}{path}", ""]
            if op.get("operationId"):
                lines.append(f"operationId: `{op['operationId']}`")
            if op.get("deprecated"):
                lines.append("**DEPRECATED**")
            if op.get("summary"):
                lines += ["", op["summary"]]
            if op.get("description") and op.get("description") != op.get("summary"):
                lines += ["", op["description"].strip()]
            params = shared + op.get("parameters", [])
            body_param = None
            rows = []
            for prm in params:
                prm, _ = resolve(spec, prm)
                if prm.get("in") == "body":
                    body_param = prm
                    continue
                typ = ref_name(prm.get("schema") or prm)
                rows.append(f"| `{prm.get('name')}` | {prm.get('in')} | {cell(typ)} | "
                            f"{'yes' if prm.get('required') else ''} | {cell(prm.get('description'))} |")
            if rows:
                lines += ["", "| Parameter | In | Type | Required | Description |",
                          "|---|---|---|---|---|", *rows]
            if body_param:
                lines += ["", f"Request body: {ref_name(body_param.get('schema'))}"]
            elif op.get("requestBody"):
                content = op["requestBody"].get("content", {})
                for ctype, media in content.items():
                    lines += ["", f"Request body ({ctype}): {ref_name(media.get('schema'))}"]
            resp = op.get("responses", {})
            if resp:
                lines += ["", "| Response | Description | Body |", "|---|---|---|"]
                for code, r in resp.items():
                    r, shared_resp = resolve(spec, r)
                    body = ref_name(r.get("schema")) if swagger2 else ", ".join(
                        ref_name(m.get("schema")) for m in (r.get("content") or {}).values())
                    desc = cell(r.get("description")) + (f" (`{shared_resp}`)" if shared_resp else "")
                    lines.append(f"| {code} | {desc} | {cell(body)} |")
            by_tag[tag].append("\n".join(lines))

    for tag, ops in sorted(by_tag.items()):
        slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-") or "untagged"
        header = f"# {info.get('title', 'API')} {info.get('version', '')} — {tag}\n\n"
        (out / "endpoints" / f"{slug}.md").write_text(header + "\n\n".join(ops) + "\n")

    schemas = spec.get("definitions") if swagger2 else (spec.get("components") or {}).get("schemas")
    parts = [f"# {info.get('title', 'API')} {info.get('version', '')} — schemas\n"]
    for name, sch in sorted((schemas or {}).items()):
        parts.append(f"## {name}\n")
        if sch.get("description"):
            parts.append(sch["description"].strip() + "\n")
        props = sch.get("properties") or {}
        req = set(sch.get("required") or [])
        if props:
            parts.append("| Field | Type | Required | Description |\n|---|---|---|---|")
            for fname, f in props.items():
                parts.append(f"| `{fname}` | {cell(ref_name(f))} | {'yes' if fname in req else ''} | "
                             f"{cell(f.get('description'))} |")
            parts.append("")
        else:
            parts.append(f"Type: {ref_name(sch)}\n")
    (out / "schemas.md").write_text("\n".join(parts) + "\n")
    n = sum(len(v) for v in by_tag.values())
    print(f"wrote {n} operations across {len(by_tag)} tags and {len(schemas or {})} schemas to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
