# Vendored browser libraries

Copied unchanged from the npm packages (downloaded with `npm pack`, which checks
each package against the registry's checksum) so the search page works offline.

| File | Package | Licence |
|---|---|---|
| `marked.umd.js` | marked 18.1.2 (`lib/marked.umd.js`) | MIT — `marked.LICENSE` |
| `purify.min.js` | dompurify 3.4.17 (`dist/purify.min.js`) | MPL-2.0 or Apache-2.0 — `dompurify.LICENSE` |

marked turns Markdown into HTML; DOMPurify then removes anything unsafe from that
HTML (scripts, event handlers, `javascript:` links) before it is shown, because the
docs are downloaded content.

## Tab icon

`favicon.svg` (an open book with a search lens on a blue tile) is drawn for this project.
`favicon.ico` holds it at 16, 32 and 48 pixels as PNGs, rendered from the SVG in a headless
browser; browsers use the SVG where they can and the ICO otherwise (and for `/favicon.ico`).
