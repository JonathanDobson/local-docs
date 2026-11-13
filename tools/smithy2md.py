#!/usr/bin/env python3
"""Turn an AWS Smithy JSON model (the API model an AWS SDK is generated from)
into searchable Markdown: the service's own API reference text, one page per
operation.

  .venv/bin/python tools/smithy2md.py <model.json> <out-dir> \\
      [--js-client @aws-sdk/client-s3]

Writes:
  <out-dir>/README.md               service description, protocol, operation list
  <out-dir>/operations/<Op>.md      one page per operation: HTTP binding, description,
                                    input and output members (type, required, where
                                    sent, description), errors, examples
  <out-dir>/shapes.md               every other structure, union and enum, with members

With --js-client, operation pages also name the SDK for JavaScript v3 command
(`GetObjectCommand` from `@aws-sdk/client-s3`). Documentation in the model is
HTML; it is converted to Markdown. Keep the model next to the pages: it is the
source of truth.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from markdownify import markdownify

DOC = "smithy.api#documentation"
PRELUDE = "smithy.api#"


def md(html: str | None) -> str:
    if not html:
        return ""
    text = markdownify(html, heading_style="ATX", bullets="-", strip=["note", "important"])
    text = re.sub(r"\n{3,}", "\n\n", text)
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def first_sentence(html: str | None, limit: int = 200) -> str:
    text = " ".join(md(html).split())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    text = m.group(1) if m else text
    return text if len(text) <= limit else text[:limit - 1] + "…"


class Model:
    def __init__(self, data: dict):
        self.shapes: dict = data["shapes"]

    def short(self, target: str) -> str:
        return target.split("#", 1)[-1]

    def type_name(self, target: str, depth: int = 0) -> str:
        """Human type: string, list<Tag>, map<string, string>, Bucket (structure)…"""
        if target.startswith(PRELUDE):
            return self.short(target).lower().replace("primitive", "")
        s = self.shapes.get(target, {})
        t = s.get("type", "?")
        if depth > 2:
            return self.short(target)
        if t == "list" or t == "set":
            return f"list<{self.type_name(s['member']['target'], depth + 1)}>"
        if t == "map":
            return f"map<{self.type_name(s['key']['target'], depth + 1)}, {self.type_name(s['value']['target'], depth + 1)}>"
        if t in ("structure", "union"):
            return self.short(target)
        if t in ("enum", "intEnum"):
            return f"{self.short(target)} (enum)"
        return t

    def members(self, target: str) -> list[tuple[str, dict]]:
        return list((self.shapes.get(target, {}).get("members") or {}).items())

    def enum_values(self, target: str) -> list[str]:
        s = self.shapes.get(target, {})
        if s.get("type") in ("enum", "intEnum"):
            out = []
            for name, m in (s.get("members") or {}).items():
                v = (m.get("traits") or {}).get("smithy.api#enumValue", name)
                out.append(str(v))
            return out
        return []


def member_block(model: Model, name: str, m: dict, level: str = "###") -> list[str]:
    traits = m.get("traits") or {}
    tname = model.type_name(m["target"])
    flags = []
    if "smithy.api#required" in traits:
        flags.append("**required**")
    where = [k.split("#")[1] for k in traits if k in ("smithy.api#httpLabel", "smithy.api#httpPayload")]
    for k in ("smithy.api#httpQuery", "smithy.api#httpHeader"):
        if k in traits:
            where.append(f"{k.split('#')[1].removeprefix('http').lower()} `{traits[k]}`")
    if where:
        flags.append("sent as " + ", ".join(where))
    if "smithy.api#default" in traits:
        flags.append(f"default `{json.dumps(traits['smithy.api#default'])}`")
    if "smithy.api#deprecated" in traits:
        flags.append("**deprecated**")
    out = [f"{level} `{name}` — {tname}" + (" · " + " · ".join(flags) if flags else ""), ""]
    doc = md(traits.get(DOC) or model.shapes.get(m["target"], {}).get("traits", {}).get(DOC))
    if doc:
        out += [doc, ""]
    values = model.enum_values(m["target"])
    if values:
        out += ["Values: " + ", ".join(f"`{v}`" for v in values[:60]) + (" …" if len(values) > 60 else ""), ""]
    return out


def operation_page(model: Model, op_id: str, service_title: str, js: str | None) -> str:
    op = model.shapes[op_id]
    name = model.short(op_id)
    traits = op.get("traits") or {}
    out = [f"# {name}", ""]
    meta = [f"Service: {service_title}"]
    if js:
        meta.append(f"SDK for JavaScript v3: `{name}Command` from `{js}`")
    http = traits.get("smithy.api#http")
    if http:
        meta.append(f"HTTP: `{http.get('method')} {http.get('uri')}`")
    if "smithy.api#paginated" in traits:
        p = traits["smithy.api#paginated"]
        meta.append("Paginated" + (f" (token `{p.get('inputToken')}` → `{p.get('outputToken')}`)" if p.get("inputToken") else ""))
    if "smithy.api#deprecated" in traits:
        meta.append("**Deprecated**")
    out += [" · ".join(meta), "", md(traits.get(DOC)), ""]
    for label, key in (("Input", "input"), ("Output", "output")):
        target = (op.get(key) or {}).get("target")
        mem = model.members(target) if target else []
        out += [f"## {label}" + (f" (`{model.short(target)}`)" if target else ""), ""]
        if not mem:
            out += ["_None._", ""]
        for n, m in mem:
            out += member_block(model, n, m)
    errs = op.get("errors") or []
    if errs:
        out += ["## Errors", ""]
        for e in errs:
            et = e["target"]
            out.append(f"- `{model.short(et)}` — {first_sentence(model.shapes.get(et, {}).get('traits', {}).get(DOC))}")
        out.append("")
    examples = traits.get("smithy.api#examples") or []
    if examples:
        out += ["## Examples", ""]
        for ex in examples:
            out += [f"### {ex.get('title', 'Example')}", ""]
            if ex.get("documentation"):
                out += [md(ex["documentation"]), ""]
            for k in ("input", "output"):
                if ex.get(k):
                    out += [f"{k.capitalize()}:", "", "```json", json.dumps(ex[k], indent=2), "```", ""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model")
    ap.add_argument("out")
    ap.add_argument("--js-client", help="npm package of the SDK for JavaScript v3 client, e.g. @aws-sdk/client-s3")
    a = ap.parse_args()
    data = json.loads(Path(a.model).read_text(encoding="utf-8"))
    model = Model(data)
    svc_id, svc = next((k, v) for k, v in model.shapes.items() if v["type"] == "service")
    st = svc.get("traits") or {}
    title = st.get("smithy.api#title") or model.short(svc_id)
    out = Path(a.out)
    (out / "operations").mkdir(parents=True, exist_ok=True)

    # Operations: the service's own list plus those reached through resources.
    ops = {o["target"] for o in svc.get("operations", [])}
    for k, v in model.shapes.items():
        if v["type"] == "resource":
            for key in ("create", "put", "read", "update", "delete", "list"):
                if v.get(key):
                    ops.add(v[key]["target"])
            ops |= {o["target"] for o in v.get("operations", []) + v.get("collectionOperations", [])}
    ops = sorted(o for o in ops if o in model.shapes)
    io = set()
    for o in ops:
        for key in ("input", "output"):
            if model.shapes[o].get(key):
                io.add(model.shapes[o][key]["target"])
        io |= {e["target"] for e in model.shapes[o].get("errors", [])}

    for o in ops:
        (out / "operations" / f"{model.short(o)}.md").write_text(operation_page(model, o, title, a.js_client), encoding="utf-8")

    proto = [k.split("#")[1] for k in st if k.startswith("aws.protocols#")]
    readme = [f"# {title} — API reference", "",
              f"API version `{svc.get('version')}`" + (f" · protocol {', '.join(proto)}" if proto else "")
              + (f" · SDK for JavaScript v3 client `{a.js_client}`" if a.js_client else ""), "",
              md(st.get(DOC)), "", f"## Operations ({len(ops)})", ""]
    readme += [f"- [`{model.short(o)}`](operations/{model.short(o)}.md) — "
               f"{first_sentence(model.shapes[o].get('traits', {}).get(DOC))}" for o in ops]
    (out / "README.md").write_text("\n".join(readme).rstrip() + "\n", encoding="utf-8")

    shapes = [f"# {title} — data types", "",
              "Structures, unions and enums used by the operations (operation inputs and outputs are on the operation pages).", ""]
    for k in sorted(model.shapes, key=model.short):
        v = model.shapes[k]
        if k in io or v["type"] not in ("structure", "union", "enum", "intEnum"):
            continue
        shapes += [f"## {model.short(k)} ({v['type']})", ""]
        doc = md((v.get("traits") or {}).get(DOC))
        if doc:
            shapes += [doc, ""]
        if v["type"] in ("enum", "intEnum"):
            shapes += ["Values: " + ", ".join(f"`{x}`" for x in model.enum_values(k)), ""]
            continue
        for n, m in model.members(k):
            shapes += member_block(model, n, m, "###")
    (out / "shapes.md").write_text("\n".join(shapes).rstrip() + "\n", encoding="utf-8")
    print(f"{title}: {len(ops)} operations -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
