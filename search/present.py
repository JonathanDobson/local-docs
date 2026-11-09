"""How search results are shown to agents (MCP) and on the command line."""
from __future__ import annotations

from search.chunker import closing_fence, fence_step
from search.config import provenance


def smart_cut(text: str, limit: int) -> str:
    """Cut `text` to at most `limit` characters at the best boundary that keeps
    at least half of it: before a code block, or after a paragraph, sentence,
    line or word. A code block that starts early and runs long is cut at a line
    and closed with its fence, so the snippet still shows code."""
    return _cut(text, limit)[0]


def _cut(text: str, limit: int) -> tuple[str, int]:
    """smart_cut, plus how many characters of `text` the result shows (it may end
    with an added closing fence that isn't in `text`)."""
    if len(text) <= limit:
        return text, len(text)
    cut = _cut_at(text, limit)
    if isinstance(cut, tuple):
        return cut
    return cut, len(cut)


def _scan(text: str, stop: int):
    """Walk the lines that end before offset `stop` (a line cut part-way doesn't count:
    half a closing fence closes nothing). Returns (offset where the code block open
    at `stop` began, its opening line), or (None, None) outside a block."""
    fence, opened, pos = None, None, 0
    while pos < stop:
        nl = text.find("\n", pos)
        nl = len(text) if nl == -1 else nl
        if nl > stop:
            break
        new = fence_step(fence, text[pos:nl])
        if fence is None and new is not None:
            opened = pos
        fence, pos = new, nl + 1
    return (opened, fence) if fence else (None, None)


def _block_end(text: str, opened: int) -> int | None:
    """Offset just after the line that closes the block opened at `opened`."""
    fence, pos = None, opened
    while pos < len(text):
        nl = text.find("\n", pos)
        nl = len(text) if nl == -1 else nl
        fence = fence_step(fence, text[pos:nl])
        if fence is None:
            return nl
        pos = nl + 1
    return None


def _cut_at(text: str, limit: int):
    win = text[:limit]
    floor = limit // 2
    opened, opener = _scan(text, limit)
    if opener:                                   # the window ends inside a code block
        if opened >= floor:
            return win[:opened].rstrip()
        # The block started early: keep it whole if it closes soon, else cut before it.
        end = _block_end(text, opened)
        if end is not None and end <= limit * 1.5:
            return text[:end]
        if win[:opened].strip() and opened >= limit // 5:
            return win[:opened].rstrip()
        # Little or nothing comes before the block: show its first lines, closed off.
        shown = win.rsplit("\n", 1)[0]
        return shown + "\n" + closing_fence(opener), len(shown)
    for sep, at_least in (("\n\n", floor), (". ", int(limit * 0.7)), ("\n", floor), (" ", floor)):
        i = win.rfind(sep)
        while i >= at_least:
            inside, _ = _scan(text, i + 1)
            if inside is None:
                return win[:i + (1 if sep == ". " else 0)].rstrip()
            i = win.rfind(sep, 0, inside)        # try again before that code block
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
        body, used = _cut(h.text, body_chars)
        if used < len(h.text):
            shown = h.start_line + h.text[:used].count("\n")
            body += (f"\n…(cut: {len(h.text) - used} more characters; read lines {shown + 1}-{h.end_line} "
                     f"with docs_read)")
        out.append("\n".join(lines) + "\n\n" + body)
    return "\n\n".join(out)
