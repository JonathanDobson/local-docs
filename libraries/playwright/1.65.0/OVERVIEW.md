# Playwright 1.65.0 (Node.js) — overview

Playwright is a browser automation library (Chromium, Firefox, WebKit) with an optional
end-to-end test runner, Playwright Test (`@playwright/test`). This set is the **Node.js**
documentation for **v1.65.0**, taken from the rendered playwright.dev docs
(`microsoft/playwright.dev`, `nodejs/versioned_docs/version-stable`), which were generated
from upstream commit `a1f35e1` = the `v1.65.0` tag. It covers both the plain library
(`playwright` / `playwright-core`, e.g. `chromium.launch()` scripts) and the test runner.

## Layout

- `content/*.mdx` — 73 guides: getting started, library usage, locators, actions,
  actionability, assertions, network/mocking, auth, emulation, and all the Playwright Test
  guides (`test-*.mdx`).
- `content/api/class-*.mdx` — 74 API class pages. Library: `class-browsertype`, `class-browser`,
  `class-browsercontext`, `class-page`, `class-locator`, `class-frame`, `class-route`,
  `class-request`, `class-response`, … Assertions: `class-locatorassertions`,
  `class-pageassertions`, `class-genericassertions`, `class-apiresponseassertions`. Test runner:
  `class-test`, `class-testconfig`, `class-testoptions`, `class-testinfo`, `class-fixtures`,
  `class-reporter`, ….
- `content/release-notes/` — `release-notes.mdx` (every version, newest first) and `v1.65.0.md`
  (the GitHub release body).

## Where to look for…

| Task | File |
|---|---|
| Using Playwright as a library without the test runner (`chromium.launch`, `newContext`, `newPage`) | `content/library.mdx` |
| Launch options (headless, `executablePath`, `proxy`, `args`, `timeout`) | `content/api/class-browsertype.mdx` (`launch`) |
| Contexts and isolation | `content/browser-contexts.mdx`, `content/api/class-browsercontext.mdx` |
| Page navigation and waiting for load | `content/navigations.mdx`, `content/api/class-page.mdx` (`goto`, `waitForURL`) |
| Finding elements (`getByRole`, `getByText`, `getByTestId`, filtering) | `content/locators.mdx`, `content/other-locators.mdx`, `content/api/class-locator.mdx` |
| Auto-waiting / actionability checks (Visible, Stable, Enabled, Editable, Not Inert, Receives Events), `force` | `content/actionability.mdx` |
| Clicking, filling, keyboard, uploads | `content/input.mdx` |
| Web-first assertions (`toBeVisible`, `toHaveText`, `expect.poll`, `toPass`, soft assertions) | `content/test-assertions.mdx`, `content/api/class-locatorassertions.mdx`, `class-pageassertions.mdx` |
| Default timeouts and changing them (`setDefaultTimeout`, test/expect/global timeouts) | `content/test-timeouts.mdx`, `class-page.mdx`, `class-browsercontext.mdx` |
| Intercepting / mocking network (`page.route`) | `content/network.mdx`, `content/mock.mdx`, `content/api/class-route.mdx` |
| Login state reuse (`storageState`) | `content/auth.mdx` |
| Screenshots, videos, traces | `content/screenshots.mdx`, `content/videos.mdx`, `content/trace-viewer.mdx` |
| Installing browsers, `PLAYWRIGHT_BROWSERS_PATH`, system requirements | `content/browsers.mdx`, `content/intro.mdx` |
| Test runner config (`playwright.config.ts`, projects, `webServer`, retries, workers) | `content/test-configuration.mdx`, `content/test-use-options.mdx`, `content/test-projects.mdx`, `content/test-webserver.mdx`, `content/test-retries.mdx`, `content/test-parallel.mdx` |
| Fixtures, global setup/teardown, CLI, reporters, CI | `content/test-fixtures.mdx`, `content/test-global-setup-teardown.mdx`, `content/test-cli.mdx`, `content/test-reporters.mdx`, `content/ci.mdx` |

## Version notes (1.65)

From `content/release-notes/release-notes.mdx` (## Version 1.65):

- Test runner can run under Bun (`bunx --bun playwright test`), with listed limitations.
- New `failures` reporter; `onlyFailures` option for the HTML, JSON and JUnit reporters.
- New APIs: `timeout` and `signal` options for `cdpSession.send()`; `testRun.mode()`.
- **Breaking:** actions such as `locator.click()`, `check()`, `fill()`, `clear()`,
  `selectOption()` now also wait for the element to be **not inert** (new actionability check).
- **Breaking:** cookie matching follows RFC 6265 (`browserContext.cookies()` with a URL no
  longer returns host-only cookies for subdomains); proxy credentials are no longer sent to
  websites (use `httpCredentials`); `params` values in `APIRequestContext` requests are
  appended to the URL's existing query; TypeScript class fields follow
  `useDefineForClassFields`; a sharded run with no tests anywhere fails unless
  `--pass-with-no-tests`.
- Node.js 20 is no longer tested; use Node.js 22, 24 or 26.
- Browsers: Chromium 158.0.8127.18, Firefox 159.0, WebKit 27.2.

## Search tips

- API anchors look like `#page-goto`, `#locator-click`, `#browser-type-launch-option-proxy`;
  headings in API pages are `### launch {/* #browser-type-launch */}`.
- Code samples come in `<Tabs>` with TypeScript and JavaScript variants; both are in the text.
- "Web-first assertions" / "auto-retrying assertions" = `expect(locator)…` matchers that retry
  until the expect timeout; "actionability" = the checks actions wait for before acting.
- The docs rarely name `playwright-core`; library pages import from `playwright`. The
  `chromium`/`firefox`/`webkit` BrowserType API in `class-browsertype.mdx` is what both expose.
  `browsers.mdx` notes browsers can be placed in `node_modules/playwright-core/.local-browsers`
  with `PLAYWRIGHT_BROWSERS_PATH=0`.
- Test runner timeouts (30 s per test, 5 s per assertion by default) apply only to Playwright
  Test, not to library scripts.
