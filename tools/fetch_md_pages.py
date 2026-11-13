#!/usr/bin/env python3
"""Fetch the Markdown version of every page of a docs site that publishes one.

Many docs sites serve each page as Markdown at "<page URL>.md" (Docker, Next.js,
Mintlify sites; for ".html" pages, "page.html" becomes "page.md", as on docs.aws.amazon.com); it is rendered by the site itself, so includes, tabs and
generated reference pages come out exactly as published. This reads the page
list from --sitemap (filtered by --prefix and --exclude), fetches each page's
Markdown, and writes it to <out>/<url path>.md with front matter recording the
title and source URL.

  .venv/bin/python tools/fetch_md_pages.py \\
      --sitemap https://docs.docker.com/sitemap.xml \\
      --prefix https://docs.docker.com/ \\
      --exclude '/reference/api/engine/version/' \\
      --out libraries/docker/29.9/content

A page whose URL has pages below it is written to <path>/_index.md, as are
pages named "release-notes" (so search files them as release notes). Honours
robots.txt, waits --delay seconds between requests, and skips pages already
saved unless --refresh. A JSON report is written to <out>/../fetch-report.json.
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
from pathlib import Path

USER_AGENT = "local-docs-ingest/1.0 (+offline documentation mirror)"


def fetch(url: str, timeout: int = 30) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers.get("Content-Type", ""), r.read().decode("utf-8", errors="replace")


def sitemap_urls(url: str, depth: int = 0) -> list[str]:
    _, _, xml = fetch(url)
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    if "<sitemapindex" in xml and depth < 3:
        return [u for sm in locs for u in sitemap_urls(sm, depth + 1)]
    return locs


def page_path(url: str, prefix: str) -> str:
    """URL path below the prefix, without slashes at either end or a .html ending ('' for the root)."""
    path = urllib.parse.unquote(url[len(prefix):].split("#")[0].split("?")[0]).strip("/")
    return re.sub(r"\.html?$", "", path)


def md_url(url: str) -> str:
    """'<page>.md' ('page.html' becomes 'page.md'); the site root is '/index.md'."""
    base = url.split("#")[0].split("?")[0]
    parts = urllib.parse.urlparse(base)
    if parts.path in ("", "/"):
        return f"{parts.scheme}://{parts.netloc}/index.md"
    return re.sub(r"\.html?$", "", base.rstrip("/")) + ".md"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sitemap", required=True)
    ap.add_argument("--prefix", required=True, help="only pages whose URL starts with this")
    ap.add_argument("--exclude", action="append", default=[], help="regex of URLs to skip (repeatable)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--delay", type=float, default=0.3)
    ap.add_argument("--max-pages", type=int, default=5000)
    ap.add_argument("--refresh", action="store_true", help="fetch pages that are already saved")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    excl = [re.compile(x) for x in args.exclude]
    urls = sorted({u for u in sitemap_urls(args.sitemap)
                   if u.startswith(args.prefix) and not any(x.search(u) for x in excl)})
    paths = {page_path(u, args.prefix) for u in urls}
    has_children = {p for p in paths for q in paths if p and q.startswith(p + "/")}

    p = urllib.parse.urlparse(args.prefix)
    robots = urllib.robotparser.RobotFileParser()
    robots.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
    try:
        robots.read()
    except OSError:
        robots = None

    saved, failed, skipped = [], [], []
    for n, url in enumerate(urls[:args.max_pages], 1):
        path = page_path(url, args.prefix)
        name = path.rsplit("/", 1)[-1]
        if not path:
            dest = out / "_index.md"
        elif path in has_children or name.endswith("release-notes"):
            dest = out / path / "_index.md"
        else:
            dest = out / f"{path}.md"
        if dest.exists() and not args.refresh:
            skipped.append({"url": url, "why": "already saved"})
            continue
        src = md_url(url)
        if robots and not robots.can_fetch(USER_AGENT, src):
            skipped.append({"url": url, "why": "robots.txt"})
            continue
        try:
            status, ctype, body = fetch(src)
            if "html" in ctype.lower() or body.lstrip().lower().startswith(("<!doctype", "<html")):
                raise ValueError(f"got HTML, not Markdown ({ctype})")
        except (urllib.error.URLError, OSError, ValueError) as exc:
            failed.append({"url": url, "error": str(exc)})
            print(f"  fail {src}: {exc}", file=sys.stderr)
        else:
            m = re.search(r"^#\s+(.+)$", body, re.M)
            title = m.group(1).strip() if m else name
            front = f"---\ntitle: {json.dumps(title, ensure_ascii=False)}\nsource: {url}\n---\n\n"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(front + body.strip() + "\n", encoding="utf-8")
            saved.append({"url": url, "file": str(dest.relative_to(out))})
        if n % 100 == 0:
            print(f"  {n}/{len(urls)} pages, {len(saved)} saved, {len(failed)} failed", file=sys.stderr)
        time.sleep(args.delay)

    report = {"sitemap": args.sitemap, "prefix": args.prefix, "exclude": args.exclude, "pages": len(urls),
              "saved": len(saved), "failed": failed, "skipped": len(skipped)}
    (out.parent / "fetch-report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()}))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
