#!/usr/bin/env python3
"""Crawl an HTML documentation site and save each page as Markdown.

Only follows links that start with --prefix, honours robots.txt, waits
--delay seconds between requests, and stops after --max-pages. Each page is
written to <out>/<url path>.md with a small front-matter block recording the
source URL and title, so every answer can be traced back to its page.

Run with the local-docs virtualenv (tools/setup.sh creates it):

  .venv/bin/python tools/crawl.py \
      --start https://docs.example.com/1.25/ \
      --prefix https://docs.example.com/1.25/ \
      --out libraries/example/1.25.0/content

Use --sitemap to seed from a sitemap.xml (filtered by --prefix), --exclude to
skip URL patterns (regex, repeatable), and --selector to name the CSS
selector of the main content when the defaults pick the wrong element.
A JSON report (pages saved, failures, skips) is written to <out>/../crawl-report.json.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

try:
    from bs4 import BeautifulSoup
    from markdownify import MarkdownConverter
except ImportError:
    sys.exit("missing dependencies: run tools/setup.sh and use .venv/bin/python")

USER_AGENT = "local-docs-ingest/1.0 (+offline documentation mirror)"
DEFAULT_SELECTORS = [
    "main article", "article", "main", "[role=main]", ".theme-doc-markdown",
    ".markdown-body", ".md-content", ".rst-content", ".document", "#content",
    ".content", "body",
]
STRIP = [
    "script", "style", "noscript", "nav", "footer", "header", "aside", "form",
    "iframe", "svg", "button", ".sidebar", ".toc", ".table-of-contents",
    ".breadcrumbs", ".pagination-nav", ".theme-edit-this-page", ".hash-link",
    "[aria-label=breadcrumbs]", ".headerlink",
]
SKIP_EXT = re.compile(
    r"\.(png|jpe?g|gif|svg|webp|ico|css|js|mjs|map|woff2?|ttf|eot|pdf|zip|"
    r"tar|gz|tgz|mp4|webm|mp3|xml|json|ya?ml|txt)$", re.I)


class Converter(MarkdownConverter):
    """markdownify with ```lang fences taken from class="language-xxx"."""

    def convert_pre(self, el, text, *args, **kwargs):
        lang = ""
        for node in [el, el.find("code")]:
            if node is None:
                continue
            for cls in node.get("class", []) or []:
                m = re.match(r"(?:language|lang|highlight)-(\S+)", cls)
                if m:
                    lang = m.group(1)
                    break
            if lang:
                break
        code = el.get_text()
        return f"\n\n```{lang}\n{code.rstrip()}\n```\n\n"


def to_markdown(html: str, selector: str | None) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title = (soup.title.get_text(strip=True) if soup.title else "")
    node = None
    for sel in ([selector] if selector else []) + DEFAULT_SELECTORS:
        node = soup.select_one(sel)
        if node is not None:
            break
    for sel in STRIP:
        for bad in node.select(sel):
            bad.decompose()
    h1 = node.find("h1")
    if h1 and h1.get_text(strip=True):
        title = h1.get_text(strip=True)
    md = Converter(heading_style="ATX", bullets="-", strip=["img"]).convert_soup(node)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return title, md


def normalise(url: str) -> str:
    url, _ = urllib.parse.urldefrag(url)
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path or "/", "", ""))


def out_path(url: str, prefix: str, out: Path) -> Path:
    rel = url[len(prefix):] if url.startswith(prefix) else urllib.parse.urlsplit(url).path
    rel = rel.strip("/")
    rel = re.sub(r"\.(html?|php|aspx?)$", "", rel)
    if not rel:
        rel = "index"
    elif url.endswith("/"):
        rel += "/index"
    rel = re.sub(r"[^A-Za-z0-9._/-]", "_", rel)
    target = (out / f"{rel}.md").resolve()
    if out.resolve() not in target.parents:
        raise ValueError(f"refusing path outside output dir: {url}")
    return target


def fetch(url: str, timeout: int = 30) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        ctype = resp.headers.get("Content-Type", "")
        body = resp.read(20_000_000)
        charset = resp.headers.get_content_charset() or "utf-8"
        return ctype, body.decode(charset, errors="replace")


def sitemap_urls(url: str, prefix: str, depth: int = 0) -> list[str]:
    _, xml = fetch(url)
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    found: list[str] = []
    for loc in locs:
        if loc.endswith(".xml") and depth < 2:
            try:
                found += sitemap_urls(loc, prefix, depth + 1)
            except Exception as exc:  # noqa: BLE001
                print(f"sitemap skip {loc}: {exc}", file=sys.stderr)
        elif normalise(loc).startswith(prefix):
            found.append(normalise(loc))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", action="append", default=[], help="start URL (repeatable)")
    ap.add_argument("--prefix", required=True, help="only follow URLs starting with this")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--sitemap", help="sitemap.xml URL to seed from")
    ap.add_argument("--exclude", action="append", default=[], help="regex of URLs to skip")
    ap.add_argument("--selector", help="CSS selector for the main content")
    ap.add_argument("--max-pages", type=int, default=1500)
    ap.add_argument("--delay", type=float, default=0.3)
    ap.add_argument("--ignore-robots", action="store_true",
                    help="only when the site owner permits it")
    args = ap.parse_args()

    prefix = args.prefix
    out: Path = args.out
    out.mkdir(parents=True, exist_ok=True)
    excludes = [re.compile(x) for x in args.exclude]

    robots = urllib.robotparser.RobotFileParser()
    p = urllib.parse.urlsplit(prefix)
    robots.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
    try:
        robots.read()
    except Exception:  # noqa: BLE001
        robots = None

    queue: deque[str] = deque()
    seen: set[str] = set()
    for u in args.start or [prefix]:
        queue.append(normalise(u))
    if args.sitemap:
        queue.extend(sitemap_urls(args.sitemap, prefix))

    saved, failed, skipped = [], [], []
    while queue and len(saved) < args.max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        if not url.startswith(prefix) or SKIP_EXT.search(urllib.parse.urlsplit(url).path):
            continue
        if any(x.search(url) for x in excludes):
            skipped.append({"url": url, "why": "exclude"})
            continue
        if robots and not args.ignore_robots and not robots.can_fetch(USER_AGENT, url):
            skipped.append({"url": url, "why": "robots.txt"})
            continue
        try:
            ctype, body = fetch(url)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            failed.append({"url": url, "error": str(exc)})
            continue
        finally:
            time.sleep(args.delay)

        try:
            target = out_path(url, prefix, out)
        except ValueError as exc:
            skipped.append({"url": url, "why": str(exc)})
            continue
        if "html" not in ctype:
            if "markdown" in ctype or "text/plain" in ctype:
                title, md = "", body
            else:
                skipped.append({"url": url, "why": f"content-type {ctype}"})
                continue
        else:
            soup_links = BeautifulSoup(body, "html.parser").find_all("a", href=True)
            for a in soup_links:
                nxt = normalise(urllib.parse.urljoin(url, a["href"]))
                if nxt.startswith(prefix) and nxt not in seen:
                    queue.append(nxt)
            title, md = to_markdown(body, args.selector)
        if len(md.strip()) < 40:
            skipped.append({"url": url, "why": "empty after extraction"})
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        safe_title = title.replace('"', "'")
        target.write_text(f'---\nsource: {url}\ntitle: "{safe_title}"\n---\n\n{md}', encoding="utf-8")
        saved.append({"url": url, "file": str(target.relative_to(out.resolve()))})
        if len(saved) % 50 == 0:
            print(f"... {len(saved)} pages, queue {len(queue)}", file=sys.stderr)

    report = {
        "crawled_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "prefix": prefix, "saved": len(saved), "failed": failed, "skipped": skipped,
        "hit_max_pages": len(saved) >= args.max_pages and bool(queue),
        "pages": saved,
    }
    (out.parent / "crawl-report.json").write_text(json.dumps(report, indent=2))
    print(f"saved {len(saved)} pages, {len(failed)} failed, {len(skipped)} skipped"
          + (" (STOPPED AT --max-pages; raise it)" if report["hit_max_pages"] else ""))
    return 0 if saved else 1


if __name__ == "__main__":
    sys.exit(main())
