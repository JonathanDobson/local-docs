#!/usr/bin/env python3
"""Turn Chrome DevTools Protocol `.pdl` files into Markdown, one page per domain.

    python3 tools/pdl2md.py <out-dir> <file.pdl> [<file.pdl> ...]

PDL ("protocol definition language") is the indented text format Chromium and
V8 use to define the DevTools Protocol (browser_protocol.pdl + domains/*.pdl,
js_protocol.pdl). `include` lines are followed relative to the including file.
This is a small, independent reader of that format (nothing from the
downloaded tree is executed). Writes <Domain>.md for each domain plus
README.md (an index of domains, commands and events).
"""
import re
import sys
from pathlib import Path

MODS = ("experimental", "deprecated", "optional")


def lines_of(path: Path, seen=None):
    seen = seen if seen is not None else set()
    path = path.resolve()
    if path in seen:
        return
    seen.add(path)
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^include\s+(\S+)", raw)
        if m:
            yield from lines_of(path.parent / m.group(1), seen)
        else:
            yield raw


def mods(words):
    flags = []
    while words and words[0] in MODS:
        flags.append(words.pop(0))
    return flags, words


def parse(all_lines):
    domains = []
    dom = None          # current domain dict
    item = None         # current type/command/event
    block = None        # list being filled: properties/parameters/returns
    field = None        # last field (for inline enum values)
    enum_target = None  # list collecting enum values
    enum_indent = None
    desc: list[str] = []
    for raw in all_lines:
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        s = raw.strip()
        if s.startswith("#"):
            desc.append(s[1:].strip())
            continue
        if enum_target is not None and indent > enum_indent:
            enum_target.append(s)
            desc = []
            continue
        enum_target = None
        words = s.split()
        if indent == 0:
            if words[0] == "version":
                desc = []
                continue
            flags, w = mods(words)
            if w and w[0] == "domain":
                dom = {"name": w[1], "flags": flags, "desc": " ".join(desc),
                       "depends": [], "types": [], "commands": [], "events": []}
                domains.append(dom)
                item = block = None
            desc = []
            continue
        if dom is None:
            desc = []
            continue
        if indent == 2:
            flags, w = mods(words)
            kind = w[0]
            if kind == "depends":
                dom["depends"].append(w[-1])
            elif kind == "type":
                item = {"name": w[1], "flags": flags, "desc": " ".join(desc),
                        "extends": " ".join(w[3:]), "props": [], "enum": []}
                dom["types"].append(item)
            elif kind in ("command", "event"):
                item = {"name": w[1], "flags": flags, "desc": " ".join(desc),
                        "params": [], "returns": [], "redirect": None}
                dom[kind + "s"].append(item)
            block = None
            desc = []
            continue
        if indent == 4 and item is not None:
            if words[0] in ("properties", "parameters"):
                block = item.get("props") if words[0] == "properties" else item["params"]
            elif words[0] == "returns":
                block = item["returns"]
            elif words[0] == "enum":
                enum_target, enum_indent = item["enum"], indent
            elif words[0] == "redirect":
                item["redirect"] = words[1]
            desc = []
            continue
        if indent >= 6 and block is not None:
            flags, w = mods(words)
            arr = False
            if len(w) >= 3 and w[0] == "array" and w[1] == "of":
                arr, w = True, w[2:]
            typ, name = w[0], w[1] if len(w) > 1 else "?"
            field = {"name": name, "type": typ, "array": arr, "flags": flags,
                     "desc": " ".join(desc), "enum": []}
            block.append(field)
            if typ == "enum":
                enum_target, enum_indent = field["enum"], indent
            desc = []
            continue
        desc = []
    return domains


def badge(flags):
    return "".join(f" *({f})*" for f in flags if f != "optional")


def tref(t, dom):
    prim = {"string", "integer", "number", "boolean", "object", "any", "binary", "enum"}
    if t in prim:
        return t
    if "." in t:
        d, n = t.split(".", 1)
        return f"[{t}]({d}.md#type-{n.lower()})"
    return f"[{t}](#type-{t.lower()})"


def field_rows(fields, dom):
    out = ["| Name | Type | Description |", "|---|---|---|"]
    for f in fields:
        t = tref(f["type"], dom)
        if f["array"]:
            t = "array of " + t
        if f["enum"]:
            t += ": " + ", ".join(f"`{v}`" for v in f["enum"])
        name = f"`{f['name']}`" + (" (optional)" if "optional" in f["flags"] else "")
        name += badge(f["flags"])
        d = f["desc"].replace("|", "\\|")
        out.append(f"| {name} | {t.replace('|', '\\|')} | {d} |")
    return out


def render(dom):
    n = dom["name"]
    L = [f"# {n} domain{badge(dom['flags'])}", ""]
    if dom["desc"]:
        L += [dom["desc"], ""]
    if dom["depends"]:
        L += ["Depends on: " + ", ".join(f"[{d}]({d}.md)" for d in dom["depends"]), ""]
    L += [f"Methods are called as `{n}.<command>` and events arrive as `{n}.<event>`.", ""]
    for sect, key in (("Commands", "commands"), ("Events", "events")):
        if not dom[key]:
            continue
        L += [f"## {sect}", ""]
        for c in dom[key]:
            L += [f"### {n}.{c['name']}{badge(c['flags'])}", ""]
            if c["desc"]:
                L += [c["desc"], ""]
            if c["redirect"]:
                L += [f"Redirects to `{c['redirect']}`.", ""]
            if c["params"]:
                L += ["**Parameters**", ""] + field_rows(c["params"], n) + [""]
            if c["returns"]:
                L += ["**Returns**", ""] + field_rows(c["returns"], n) + [""]
    if dom["types"]:
        L += ["## Types", ""]
        for t in dom["types"]:
            L += [f'<a id="type-{t["name"].lower()}"></a>',
                  f"### {n}.{t['name']}{badge(t['flags'])}", "",
                  f"Type: {t['extends']}", ""]
            if t["desc"]:
                L += [t["desc"], ""]
            if t["enum"]:
                L += ["Allowed values: " + ", ".join(f"`{v}`" for v in t["enum"]), ""]
            if t["props"]:
                L += ["**Properties**", ""] + field_rows(t["props"], n) + [""]
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    domains = []
    for f in sys.argv[2:]:
        domains += parse(lines_of(Path(f)))
    domains.sort(key=lambda d: d["name"])
    idx = ["# Chrome DevTools Protocol: domains", "",
           f"{len(domains)} domains, generated from the protocol's PDL definition files. "
           "Each page lists the domain's commands (with parameters and return values), "
           "events and types.", "",
           "| Domain | Commands | Events | Description |", "|---|---|---|---|"]
    nc = ne = 0
    for d in domains:
        (out / f"{d['name']}.md").write_text(render(d), encoding="utf-8")
        nc += len(d["commands"])
        ne += len(d["events"])
        desc = d["desc"].split(". ")[0].replace("|", "\\|")
        idx.append(f"| [{d['name']}]({d['name']}.md){badge(d['flags'])} | "
                   f"{len(d['commands'])} | {len(d['events'])} | {desc} |")
    (out / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"wrote {len(domains)} domains, {nc} commands, {ne} events -> {out}")


if __name__ == "__main__":
    main()
