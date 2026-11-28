#!/usr/bin/env python3
"""Turn a Chrome DevTools Protocol (CDP) JSON definition (browser_protocol.json
or js_protocol.json from github.com/ChromeDevTools/devtools-protocol) into
searchable Markdown, one page per domain -- the same content the protocol
viewer at chromedevtools.github.io/devtools-protocol renders.

  python3 tools/cdp2md.py <protocol.json> <out-dir> [--title "Browser protocol"]

Writes:
  <out-dir>/README.md        protocol version and the list of domains
  <out-dir>/<Domain>.md      description, dependencies, then every method
                             (`Domain.command`), event and type with its
                             parameters, return values, enums and status
                             (experimental / deprecated / optional)

Descriptions in the JSON are already plain text; they are copied unchanged.
Keep the JSON next to the pages: it is the source of truth.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def flags(obj: dict) -> str:
    out = []
    if obj.get("experimental"):
        out.append("**Experimental**")
    if obj.get("deprecated"):
        out.append("**Deprecated**")
    return " · ".join(out)


def type_of(p: dict, domain: str) -> str:
    if "$ref" in p:
        ref = p["$ref"]
        if "." in ref:
            d, t = ref.split(".", 1)
            return f"[{ref}]({d}.md#type-{t.lower()})"
        return f"[{domain}.{ref}](#type-{ref.lower()})"
    t = p.get("type", "")
    if t == "array" and "items" in p:
        return f"array of {type_of(p['items'], domain)}"
    return t


def one_line(text: str) -> str:
    return " ".join(text.split()).replace("|", "\\|")


def table(params: list[dict], domain: str) -> list[str]:
    rows = ["| Name | Type | Description |", "|---|---|---|"]
    for p in params:
        name = f"`{p['name']}`"
        if p.get("optional"):
            name += " (optional)"
        desc = one_line(p.get("description", ""))
        f = flags(p)
        if f:
            desc = f"{f} {desc}".strip()
        if p.get("enum"):
            desc += " Allowed values: " + ", ".join(f"`{v}`" for v in p["enum"])
        rows.append(f"| {name} | {type_of(p, domain)} | {desc.strip()} |")
    return rows


def member(kind: str, domain: str, item: dict) -> list[str]:
    full = f"{domain}.{item['name']}"
    lines = [f"### {full}", ""]
    f = flags(item)
    if f:
        lines += [f, ""]
    if item.get("description"):
        lines += [item["description"].strip(), ""]
    if item.get("redirect"):
        lines += [f"Implemented by the `{item['redirect']}` domain.", ""]
    params = item.get("parameters") or []
    if params:
        lines += ["**Parameters**" if kind == "method" else "**Event parameters**", ""]
        lines += table(params, domain) + [""]
    elif kind == "method":
        lines += ["No parameters.", ""]
    returns = item.get("returns") or []
    if returns:
        lines += ["**Return object**", ""] + table(returns, domain) + [""]
    return lines


def domain_page(dom: dict, title: str, version: str) -> str:
    name = dom["domain"]
    lines = [f"# {name} domain", "", f"Chrome DevTools Protocol, {title} (protocol {version}).", ""]
    f = flags(dom)
    if f:
        lines += [f, ""]
    if dom.get("description"):
        lines += [dom["description"].strip(), ""]
    if dom.get("dependencies"):
        lines += ["Depends on: " + ", ".join(f"[{d}]({d}.md)" for d in dom["dependencies"]), ""]

    cmds, evts, types = dom.get("commands", []), dom.get("events", []), dom.get("types", [])
    lines += [f"{len(cmds)} methods, {len(evts)} events, {len(types)} types.", ""]
    if cmds:
        lines += ["## Methods", ""]
        for c in cmds:
            lines += member("method", name, c)
    if evts:
        lines += ["## Events", ""]
        for e in evts:
            lines += member("event", name, e)
    if types:
        lines += ["## Types", ""]
        for t in types:
            lines += [f'<a id="type-{t["id"].lower()}"></a>', f"### {name}.{t['id']}", ""]
            f = flags(t)
            if f:
                lines += [f, ""]
            if t.get("description"):
                lines += [t["description"].strip(), ""]
            lines += [f"Type: {type_of(t, name)}", ""]
            if t.get("enum"):
                lines += ["Allowed values: " + ", ".join(f"`{v}`" for v in t["enum"]), ""]
            if t.get("properties"):
                lines += ["**Properties**", ""] + table(t["properties"], name) + [""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("out")
    ap.add_argument("--title", default="protocol")
    a = ap.parse_args()
    data = json.loads(Path(a.spec).read_text())
    v = data.get("version", {})
    version = f"{v.get('major', '?')}.{v.get('minor', '?')}"
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    index = [f"# Chrome DevTools Protocol — {a.title}", "",
             f"Generated from `{Path(a.spec).name}` (protocol version {version}). One page per domain.", "",
             "| Domain | Status | Methods | Events | Types | Summary |", "|---|---|---|---|---|---|"]
    for dom in sorted(data["domains"], key=lambda d: d["domain"]):
        (out / f"{dom['domain']}.md").write_text(domain_page(dom, a.title, version))
        summary = one_line(dom.get("description", "")).split(". ")[0][:160]
        index.append(f"| [{dom['domain']}]({dom['domain']}.md) | {flags(dom) or 'stable'} | "
                     f"{len(dom.get('commands', []))} | {len(dom.get('events', []))} | "
                     f"{len(dom.get('types', []))} | {summary} |")
    (out / "README.md").write_text("\n".join(index) + "\n")
    print(f"{len(data['domains'])} domains -> {out}")


if __name__ == "__main__":
    main()
