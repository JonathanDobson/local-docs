"""How search results are shown to agents (MCP) and on the command line."""
from __future__ import annotations

import re

from search.config import provenance

FENCE = re.compile(r"^\s*(```|~~~)", re.M)


def smart_cut(text: str, limit: int) -> str:
    """Cut `text` to at most `limit` characters at the best boundary that keeps
    at least half of it: never inside a code block, else after a paragraph,
    sentence, line or word."""
    if len(text) <= limit:
        return text
    win = text[:limit]
    floor = limit // 2
    fences = [m.start() for m in FENCE.finditer(win)]
    if len(fences) % 2:                          # the window ends inside a code block
        opened = fences[-1]
        if opened >= floor:
            return win[:opened].rstrip()
        # The block started early: keep it whole if it closes soon, else cut before it.
        m = FENCE.search(text, opened + 3)
        if m:
            end = text.find("\n", m.start())
            end = len(text) if end == -1 else end
            if end <= limit * 1.5:
                return text[:end]
        return win[:opened].rstrip() if opened else win.rsplit("\n", 1)[0]
    for sep, at_least in (("\n\n", floor), (". ", int(limit * 0.7)), ("\n", floor), (" ", floor)):
        i = win.rfind(sep)
        if i >= at_least:
            return win[:i + (1 if sep == ". " else 0)].rstrip()
    return win


def for_agent(hits, s, query: str, scope: str = "", body_chars: int = 1500) -> str:
    """Markdown result list for the MCP tool."""
    if not hits:
        return f"No results{scope}. Check docs_list for available libraries and versions."
    out = []
    top = hits[0]
    if top.confidence == "weak":
        out.append(f"**No confident match{scope}.** The best hit is only weakly related (similarity "
                   f"{top.sim:.2f}). The docs may not cover this, or use other words: retry in the docs' own "
                   f"terms, try mode=\"dense\", or check docs_list. Weak hits follow.\n")
    for i, h in enumerate(hits, 1):
        tag = f" [{h.confidence}, similarity {h.sim:.2f}]" if h.confidence else ""
        src = provenance(h.path)
        lines = [f"### {i}. {h.library} {h.version} ({h.doc_type}) — {h.breadcrumb}{tag}",
                 f"file: {h.path} lines {h.start_line}-{h.end_line}" + (f" · {src}" if src else "")]
        if h.also:
            lines.append("same text also in: " + ", ".join(h.also))
        if h.source_url:
            lines.append(f"web: {h.source_url}")
        body = smart_cut(h.text, body_chars)
        if len(body) < len(h.text):
            shown = h.start_line + body.count("\n")
            body += (f"\n…(cut: {len(h.text) - len(body)} more characters; read lines {shown + 1}-{h.end_line} "
                     f"with docs_read)")
        out.append("\n".join(lines) + "\n\n" + body)
    return "\n\n".join(out)
