"""Split documentation files into chunks for indexing.

Markdown-family files are split at headings (levels 1-4), and every chunk
carries its heading path ("Config Cheat Sheet › Service (service)") so a
section called "Options" still says what it is about. Long sections are
packed from whole blocks — paragraphs, lists, code fences, tables — so code
and tables are never cut mid-way unless a single block is itself too long,
in which case it is split by lines (tables repeat their header row, and a
code block is closed and reopened at the cut).
Other text files (.rst, .txt, .adoc) use the same packing without headings.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

MAX_CHARS = 2400      # ~600 tokens: room for a whole config section or endpoint
MIN_CHARS = 40        # drop fragments with no real content
MD_EXT = {".md", ".mdx", ".markdown"}
TEXT_EXT = MD_EXT | {".rst", ".txt", ".adoc"}
SKIP_NAMES = {"TOC.md"}

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


def fence_step(opener: str | None, line: str) -> str | None:
    """Track fenced code blocks line by line. `opener` is the line that opened the
    block we're in (None outside one); returns the state after `line`. As in
    CommonMark, only a fence of the same character, at least as long, with nothing
    after it closes a block, so a ```` block can contain ``` examples."""
    m = FENCE.match(line)
    if not m:
        return opener
    if opener is None:
        return line
    run = FENCE.match(opener).group(1)
    if m.group(1)[0] == run[0] and len(m.group(1)) >= len(run) and not m.group(2).strip():
        return None
    return opener
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


@dataclass
class Chunk:
    path: str                # relative to the local-docs root
    start_line: int          # 1-based, inclusive
    end_line: int
    heading_path: list[str]
    text: str
    title: str = ""
    source_url: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def breadcrumb(self) -> str:
        return " › ".join(h for h in [self.title, *self.heading_path] if h)


def _front_matter(text: str) -> tuple[dict, str, int]:
    m = FRONT.match(text)
    if not m:
        return {}, text, 0
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    consumed = m.group(0).count("\n")
    return meta, text[m.end():], consumed


def _blocks(lines: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    """Group (line_no, text) into blocks separated by blank lines; fences stay whole."""
    blocks, cur, fence = [], [], None
    for ln, s in lines:
        before, fence = fence, fence_step(fence, s)
        if before is None and fence is None and not s.strip():
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append((ln, s))
    if cur:
        blocks.append(cur)
    return blocks


def closing_fence(opener: str) -> str:
    m = re.match(r"^(\s*)(`{3,}|~{3,})", opener)
    return m.group(1) + m.group(2) if m else "```"


def _split_big(block: list[tuple[int, str]]) -> list[list[tuple[int | None, str]]]:
    """Split one over-long block by lines. Every piece stays readable on its own:
    tables repeat their header row, and a code block cut in two is closed at the end
    of one piece and reopened (with its language) at the start of the next.
    Repeated lines are copies, numbered None, so they don't move a chunk's line range."""
    is_table = len(block) > 2 and block[0][1].lstrip().startswith("|") and re.match(r"^\s*\|?\s*:?-{2,}", block[1][1])
    header = block[:2] if is_table else []
    body = block[2:] if is_table else block
    # A single line longer than the limit (minified output, long tables cells) is cut.
    body = [(ln, s[i:i + MAX_CHARS]) for ln, s in body for i in range(0, max(len(s), 1), MAX_CHARS)]
    out: list[list[tuple[int | None, str]]] = []
    cur: list[tuple[int | None, str]] = list(header)
    size, added = sum(len(s) + 1 for _, s in header), 0
    opener: str | None = None          # the fence line of a code block open at this point
    for ln, s in body:
        close = len(closing_fence(opener)) + 1 if opener else 0
        if size + len(s) + close > MAX_CHARS and added:
            carry = []
            if opener and cur[-1] == (cur[-1][0], opener) and cur[-1][0] is not None and added > 1:
                carry = [cur.pop()]    # don't end a piece on a block's opening line
                added -= 1
            elif opener:
                cur.append((None, closing_fence(opener)))
            out.append(cur)
            cur = [(None, x) for _, x in header]
            cur += carry or ([(None, opener)] if opener else [])
            size, added = sum(len(x) + 1 for _, x in cur), len(carry)
        cur.append((ln, s))
        size += len(s) + 1
        added += 1
        opener = fence_step(opener, s)
    if added:
        out.append(cur)
    return out


def _pack(lines: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    pieces: list[list[tuple[int, str]]] = []
    cur: list[tuple[int, str]] = []
    size = 0
    for blk in _blocks(lines):
        blen = sum(len(s) + 1 for _, s in blk)
        if blen > MAX_CHARS:
            if cur:
                pieces.append(cur)
                cur, size = [], 0
            pieces.extend(_split_big(blk))
            continue
        if size + blen > MAX_CHARS and cur:
            pieces.append(cur)
            cur, size = [], 0
        if cur:
            cur.append((blk[0][0], ""))  # keep paragraph break
        cur.extend(blk)
        size += blen
    if cur:
        pieces.append(cur)
    return pieces


def chunk_file(path: Path, rel: str) -> list[Chunk]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body, offset = _front_matter(raw)
    title = meta.get("title", "")
    source = meta.get("source", "")
    lines = [(i + 1 + offset, s) for i, s in enumerate(body.splitlines())]
    is_md = path.suffix.lower() in MD_EXT

    # Sections: (heading_path, [(line_no, text), ...])
    sections: list[tuple[list[str], list[tuple[int, str]]]] = []
    stack: list[tuple[int, str]] = []
    cur: list[tuple[int, str]] = []
    fence = None
    for ln, s in lines:
        before, fence = fence, fence_step(fence, s)
        m = HEADING.match(s) if (is_md and before is None and fence is None) else None
        if m and len(m.group(1)) <= 4:
            sections.append(([h for _, h in stack], cur))
            level = len(m.group(1))
            heading = re.sub(r"\{#[^}]*\}|<[^>]+>|`", "", m.group(2)).strip()
            stack = [(lv, h) for lv, h in stack if lv < level] + [(level, heading)]
            if not title and level == 1:
                title = heading
            cur = [(ln, s)]
        else:
            cur.append((ln, s))
    sections.append(([h for _, h in stack], cur))

    chunks: list[Chunk] = []
    for hpath, sec in sections:
        content = [x for x in sec if x[1].strip()]
        # A section that is only its heading adds nothing: its children carry the path.
        if not content or (len(content) == 1 and HEADING.match(content[0][1])):
            continue
        for piece in _pack(sec):
            text = "\n".join(s for _, s in piece).strip()
            if len(re.sub(r"\s+", "", text)) < MIN_CHARS:
                continue
            nums = [ln for ln, _ in piece if ln is not None]
            chunks.append(Chunk(path=rel, start_line=min(nums), end_line=max(nums),
                                heading_path=[h for h in hpath if h != title] if hpath else [],
                                text=text, title=title, source_url=source))
    return chunks


IDENT = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[_.\-/:][A-Za-z0-9]+)+|[a-z]+[A-Z][A-Za-z0-9]*|[A-Z]{2,}[a-z][A-Za-z0-9]*")


def identifier_parts(text: str) -> str:
    """Split identifiers so keyword search can match their parts.

    DISABLE_REGISTRATION -> "disable registration"; hybridSearch -> "hybrid search";
    RRFRanker -> "rrf ranker". Lite's analyzer keeps the whole identifier as one
    word; this adds the parts alongside it.
    """
    parts = []
    for ident in set(IDENT.findall(text)):
        words = re.split(r"[_.\-/:]+", ident)
        words = [w for x in words for w in re.findall(r"[A-Z]+(?=[A-Z][a-z]|\d|\b)|[A-Z]?[a-z]+|[A-Z]+|\d+", x)]
        if len(words) > 1:
            parts.append(" ".join(w.lower() for w in words))
    return "\n".join(sorted(parts))


def file_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()


def chunk_id(rel: str, start: int, end: int) -> str:
    return hashlib.sha1(f"{rel}:{start}:{end}".encode()).hexdigest()[:24]
