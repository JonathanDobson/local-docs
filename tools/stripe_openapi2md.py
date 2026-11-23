#!/usr/bin/env python3
"""Turn Stripe's OpenAPI spec (github.com/stripe/openapi, spec3.json) into
searchable Markdown, one page per API resource.

  python3 tools/stripe_openapi2md.py <spec3.json> <out-dir>

The generic tools/openapi2md.py doesn't suit Stripe's spec: it has no tags (so
every operation lands in one file), and Stripe puts request parameters in an
inline application/x-www-form-urlencoded body schema that the generic tool only
names as "object". This script writes:

  <out>/resources/<resource>.md   every operation under /v1/<resource>
                                  (test helpers under /v1/test_helpers/<x>),
                                  with query parameters and every request-body
                                  field flattened to form-encoding names
                                  (items[].price, payment_settings.save_default_payment_method),
                                  enums and descriptions; then the object(s)
                                  those operations return, field by field.
  <out>/objects/<schema>.md       every other schema (sub-objects).

The spec file itself is never modified. Uses only the standard library.
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

METHODS = ("get", "post", "delete", "put", "patch")
MAX_DEPTH = 5


def md(text: str | None) -> str:
    """Stripe descriptions mix HTML and Markdown; make them plain Markdown."""
    if not text:
        return ""
    t = text
    t = re.sub(r'<a href="(/[^"]*)">', lambda m: f'<a href="https://stripe.com{m.group(1)}">', t)
    t = re.sub(r'<a href="([^"]*)">(.*?)</a>', r"[\2](\1)", t, flags=re.S)
    t = re.sub(r"\]\((/docs[^)]*)\)", r"](https://stripe.com\1)", t)
    t = re.sub(r"</?code>", "`", t)
    t = re.sub(r"</?(strong|b)>", "**", t)
    t = re.sub(r"</?(em|i)>", "*", t)
    t = re.sub(r"<li>", "\n- ", t)
    t = re.sub(r"</p>\s*<p>", "\n\n", t)
    t = re.sub(r"</?(p|ul|ol|li|br ?/?)>", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return html.unescape(t).strip()


def cell(text) -> str:
    return md(str(text or "")).replace("\n\n", "<br>").replace("\n", " ").replace("|", "\\|")


def refname(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def type_of(sch: dict) -> str:
    if not sch:
        return ""
    if "$ref" in sch:
        return f"`{refname(sch['$ref'])}`"
    for key in ("anyOf", "oneOf"):
        if key in sch:
            parts = []
            for sub in sch[key]:
                if sub.get("enum") == [""]:
                    parts.append('"" (to unset)')
                else:
                    parts.append(type_of(sub))
            return " or ".join(dict.fromkeys(parts))
    t = sch.get("type", "object" if "properties" in sch else "")
    if t == "array":
        return f"array of {type_of(sch.get('items') or {})}"
    if sch.get("enum") and sch["enum"] != [""]:
        return f"enum: {', '.join('`%s`' % e for e in sch['enum'])}"
    if sch.get("format") == "unix-time":
        return "timestamp (Unix seconds)"
    if t == "object" and sch.get("additionalProperties") and not sch.get("properties"):
        return "map (key → value)"
    if sch.get("x-stripeBypassValidation"):
        t += " (open enum)"
    return t or "any"


def flatten(name: str, sch: dict, required: bool, depth: int, rows: list) -> None:
    """Emit one row per field, recursing into inline objects/arrays of objects."""
    desc = sch.get("description", "")
    rows.append((name, type_of(sch), required, desc))
    if depth >= MAX_DEPTH:
        return
    subs = []
    if sch.get("properties"):
        subs.append((name, sch))
    if sch.get("type") == "array" and (sch.get("items") or {}).get("properties"):
        subs.append((name + "[]", sch["items"]))
    for key in ("anyOf", "oneOf"):
        for sub in sch.get(key, []):
            if sub.get("properties"):
                subs.append((name, sub))
            elif sub.get("type") == "array" and (sub.get("items") or {}).get("properties"):
                subs.append((name + "[]", sub["items"]))
    for prefix, obj in subs:
        req = set(obj.get("required") or [])
        for k, v in (obj.get("properties") or {}).items():
            flatten(f"{prefix}.{k}", v, k in req, depth + 1, rows)


def field_table(rows) -> list[str]:
    out = ["| Field | Type | Required | Description |", "|---|---|---|---|"]
    for n, t, r, d in rows:
        out.append(f"| `{n}` | {cell(t)} | {'yes' if r else ''} | {cell(d)} |")
    return out


def object_section(name: str, sch: dict, level: str = "##") -> list[str]:
    lines = [f"{level} The `{name}` object", ""]
    if sch.get("description"):
        lines += [md(sch["description"]), ""]
    if sch.get("x-expandableFields"):
        lines += ["Expandable fields (pass `expand[]=<field>`): "
                  + ", ".join(f"`{f}`" for f in sch["x-expandableFields"]), ""]
    props = sch.get("properties") or {}
    if props:
        rows = []
        req = set(sch.get("required") or [])
        for k, v in props.items():
            # nested objects are named by type; their own page lists their fields
            rows.append((k, type_of(v), k in req, v.get("description", "")))
        lines += field_table(rows) + [""]
    else:
        lines += [f"Type: {type_of(sch)}", ""]
    return lines


def resource_key(path: str) -> str:
    parts = path.strip("/").split("/")
    if parts[0] != "v1":
        return parts[0]
    if len(parts) > 2 and parts[1] in ("test_helpers",):
        return f"test_helpers.{parts[2]}"
    return parts[1] if len(parts) > 1 else "root"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    spec = json.load(open(sys.argv[1]))
    out = Path(sys.argv[2])
    version = spec["info"]["version"]
    schemas = spec["components"]["schemas"]
    (out / "resources").mkdir(parents=True, exist_ok=True)
    (out / "objects").mkdir(parents=True, exist_ok=True)

    ops_by_res: dict[str, list[str]] = defaultdict(list)
    returns_by_res: dict[str, list[str]] = defaultdict(list)
    n_ops = 0
    for path, item in spec["paths"].items():
        res = resource_key(path)
        for method in METHODS:
            op = item.get(method)
            if not op:
                continue
            n_ops += 1
            lines = [f"## {method.upper()} {path}", ""]
            summary = op.get("summary") or ""
            if summary:
                lines += [f"**{md(summary)}**", ""]
            lines += [f"operationId: `{op.get('operationId', '')}`", ""]
            if op.get("deprecated"):
                lines += ["**Deprecated.**", ""]
            if op.get("description") and op.get("description") != summary:
                lines += [md(op["description"]), ""]
            rows = []
            for prm in item.get("parameters", []) + op.get("parameters", []):
                if prm.get("in") == "path":
                    rows.append((f"{prm['name']} (path)", type_of(prm.get("schema", {})), True,
                                 prm.get("description", "")))
                elif prm.get("in") == "query":
                    flatten(prm["name"], prm.get("schema", {}) | (
                        {"description": prm["description"]} if prm.get("description") else {}),
                        prm.get("required", False), 0, rows)
            body = (op.get("requestBody") or {}).get("content", {})
            form = body.get("application/x-www-form-urlencoded", {}).get("schema", {})
            req = set(form.get("required") or [])
            for k, v in (form.get("properties") or {}).items():
                flatten(k, v, k in req, 0, rows)
            if rows:
                lines += ["Parameters (query string for GET/DELETE, form-encoded body for POST):", ""]
                lines += field_table(rows) + [""]
            ok = (op.get("responses") or {}).get("200", {})
            rsch = (ok.get("content") or {}).get("application/json", {}).get("schema", {})
            lines += [f"Returns: {type_of(rsch) or 'see spec'}"]
            if "$ref" in rsch:
                returns_by_res[res].append(refname(rsch["$ref"]))
            for sub in rsch.get("anyOf", []):
                if "$ref" in sub:
                    returns_by_res[res].append(refname(sub["$ref"]))
            ops_by_res[res].append("\n".join(lines))

    used = set()
    for res, ops in sorted(ops_by_res.items()):
        title = res.replace("_", " ").replace(".", " / ")
        page = [f"# Stripe API {version} — {title}", "",
                f"Operations under `/v1/{res.replace('.', '/')}` for API version {version}, "
                f"generated from Stripe's OpenAPI spec (spec3.json).", ""]
        page += ["\n\n".join(ops), ""]
        objs = [o for o in dict.fromkeys(returns_by_res[res])
                if o in schemas and schemas[o].get("x-resourceId")]
        if objs:
            page += ["# Objects returned", ""]
            for o in objs:
                page += object_section(o, schemas[o])
                used.add(o)
        (out / "resources" / f"{res}.md").write_text("\n".join(page) + "\n")

    for name, sch in sorted(schemas.items()):
        if name in used:
            continue
        page = [f"# Stripe API {version} — `{name}` object", ""]
        page += object_section(name, sch)[2:]  # drop the "The `x` object" heading
        (out / "objects" / f"{name}.md").write_text("\n".join(page) + "\n")

    print(f"wrote {n_ops} operations in {len(ops_by_res)} resource pages "
          f"and {len(schemas) - len(used)} object pages to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
