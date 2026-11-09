"""Split documentation files into chunks for indexing.

Markdown-family files are split at headings (levels 1-4), and every chunk
carries its heading path ("Config Cheat Sheet › Service (service)") so a
section called "Options" still says what it is about. Long sections are
packed from whole blocks — paragraphs, lists, code fences, tables — so code
and tables are never cut mid-way unless a single block is itself too long,
in which case it is split by lines (tables repeat their header row).
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
FENCE = re.compile(r"^\s*(```|~~~)")
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
    blocks, cur, in_fence = [], [], False
    for ln, s in lines:
        if FENCE.match(s):
            in_fence = not in_fence
            cur.append((ln, s))
            continue
        if not in_fence and not s.strip():
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append((ln, s))
    if cur:
        blocks.append(cur)
    return blocks


def _split_big(block: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    """Split one over-long block by lines; tables repeat their header."""
    is_table = len(block) > 2 and block[0][1].lstrip().startswith("|") and re.match(r"^\s*\|?\s*:?-{2,}", block[1][1])
    header = block[:2] if is_table else []
    body = block[2:] if is_table else block
    out, cur, size = [], list(header), sum(len(s) for _, s in header)
    # A single line longer than the limit (minified output, long tables cells) is cut.
    body = [(ln, s[i:i + MAX_CHARS]) for ln, s in body for i in range(0, max(len(s), 1), MAX_CHARS)]
    for ln, s in body:
        if size + len(s) > MAX_CHARS and len(cur) > len(header):
            out.append(cur)
            cur, size = list(header), sum(len(x) for _, x in header)
        cur.append((ln, s))
        size += len(s) + 1
    if len(cur) > len(header):
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
    in_fence = False
    for ln, s in lines:
        if FENCE.match(s):
            in_fence = not in_fence
        m = HEADING.match(s) if (is_md and not in_fence) else None
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
            nums = [ln for ln, _ in piece]
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
