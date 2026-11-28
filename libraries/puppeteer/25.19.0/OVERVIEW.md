# Puppeteer 25.19.0

Puppeteer is a Node.js library that drives Chrome or Firefox over the Chrome
DevTools Protocol (CDP) or WebDriver BiDi. This set is the official
documentation at the `puppeteer-v25.19.0` tag of
[github.com/puppeteer/puppeteer](https://github.com/puppeteer/puppeteer)
(commit `0e884d7`): the Markdown `docs/` folder that builds pptr.dev, including
the API reference generated from the source at that tag, plus the
`@puppeteer/browsers` 3.3.0 README and the GitHub release notes. At this tag
Puppeteer downloads Chrome for Testing **158.0.8127.88** (and
`chrome-headless-shell` of the same version) and Firefox **161.0**.

A sibling set, **`chrome`** (Chrome 158 command-line switches, DevTools
Protocol, headless mode, ChromeDriver), is being ingested alongside this one;
look there for browser-side flags and raw CDP domains.

## Layout

| Folder / file | What it holds |
|---|---|
| `content/index.md` | Landing page: install, quick example |
| `content/guides/` | 25 task guides (launching, page interactions, network interception, screenshots, PDF, Docker, configuration, debugging…) |
| `content/api-reference/` | Full `puppeteer` / `puppeteer-core` API, one page per class, member, interface and type (`puppeteer.page.goto.md`); `index.md` lists everything |
| `content/browsers-api-reference/` | `@puppeteer/browsers` API (`install`, `launch`, `computeExecutablePath`, `Browser`, `BrowserPlatform`…); `index.md` = README + API tables |
| `content/browsers/README.md` | `@puppeteer/browsers` CLI README (`npx @puppeteer/browsers install chrome@stable`, `chromedriver`, `--retry`) |
| `content/faq.md`, `troubleshooting.md` | FAQ; launch failures, sandbox, Linux deps, Windows, Docker issues |
| `content/supported-browsers.md` | Puppeteer version → Chrome/Firefox version table |
| `content/webdriver-bidi.md` | What works over WebDriver BiDi vs CDP |
| `content/examples.md`, `contributing.md` | Links to examples; repo contribution guide |
| `content/release-notes/` | GitHub release notes: `puppeteer-v25.19.0`, `puppeteer-core-v25.19.0`, `browsers-v3.3.0` |

## Where to look for…

| Task | File |
|---|---|
| Install; `puppeteer` vs `puppeteer-core` | `guides/installation.md`, `index.md` |
| Browser not downloaded / blocked install scripts | `index.md` (`npx puppeteer browsers install`), `troubleshooting.md` ("Could not find expected browser locally") |
| Config files (`.puppeteerrc.cjs`) and env vars (`PUPPETEER_CACHE_DIR`, `PUPPETEER_EXECUTABLE_PATH`, `PUPPETEER_SKIP_DOWNLOAD`) | `guides/configuration.md`, `api-reference/puppeteer.configuration.md` |
| Launch options (`headless`, `executablePath`, `args`, `userDataDir`) | `api-reference/puppeteer.launchoptions.md`, `api-reference/puppeteer.puppeteernode.launch.md` |
| Connect to an already running browser (`puppeteer.connect`, `browserWSEndpoint`) | `guides/browser-management.md`, `api-reference/puppeteer.connectoptions.md` |
| Headless vs `chrome-headless-shell` vs headful | `guides/headless-modes.md` |
| Clicking, typing, waiting: locators, `waitForSelector`, selector syntax (`::-p-text`, `::-p-aria`) | `guides/page-interactions.md`, `api-reference/puppeteer.locator.md` |
| Running JS in the page (`evaluate`) | `guides/javascript-execution.md` |
| Request interception, cooperative intercept mode | `guides/network-interception.md`, `api-reference/puppeteer.httprequest.md` |
| Screenshots / PDF | `guides/screenshots.md`, `guides/pdf-generation.md` |
| Cookies, files/downloads | `guides/cookies.md`, `guides/files.md` |
| Docker and Linux system requirements | `guides/docker.md`, `guides/system-requirements.md`, `troubleshooting.md` |
| Firefox / WebDriver BiDi | `webdriver-bidi.md`, `supported-browsers.md` |
| Raw CDP access (`createCDPSession`) | `api-reference/puppeteer.page.createcdpsession.md`, `api-reference/puppeteer.cdpsession.md` |
| Downloading Chrome for Testing / ChromeDriver from a CLI or code | `browsers/README.md`, `browsers-api-reference/browsers.install.md` |
| Which Chrome version goes with which Puppeteer | `supported-browsers.md` |

## Version notes (25.19.0, released 2026-11-25)

- Rolls to Chrome 158 (final 158.0.8127.88) and Firefox 161.0.
- New `Target.close()` (`api-reference/puppeteer.target.close.md`).
- Many fixes: BiDi network-idle waits use `defaultNavigationTimeout`;
  `Page.setViewport()`/`viewport()` copy the viewport; navigation ends at once
  when the page crashes; headful windows no longer hidden on Windows;
  cooperative intercept mode uses the highest-priority payload.
- `@puppeteer/browsers` 3.3.0 adds `install --retry`.
- Long-standing history the docs mention: Chrome for Testing since v20.0.0
  (before that, Chromium); the old headless mode became `chrome-headless-shell`
  (`headless: 'shell'`) and the new headless became default in v22; stable
  Firefox downloads since v23.0.0; browsers cached in `~/.cache/puppeteer`
  since v19.0.0.

## Search tips

- API pages are named `puppeteer.<class>.<member>.md`, all lower-case
  (`puppeteer.page.waitforselector.md`, `puppeteer.elementhandle.click.md`).
  `@puppeteer/browsers` pages are `browsers.<name>.md`.
- Puppeteer-specific selector pseudo-elements start with `::-p-`
  (`::-p-text(...)`, `::-p-aria(...)`, `::-p-xpath(...)`).
- "Chrome for Testing" is the browser build Puppeteer downloads;
  "chrome-headless-shell" is the old headless mode as a separate binary.
- Protocol choice: `protocol: 'webDriverBiDi'` or `'cdp'`; `browser: 'firefox'`
  uses WebDriver BiDi by default.
- Links inside pages point at pptr.dev paths (`../api/...`); locally those live
  under `content/api-reference/`.
