# Chrome DevTools Protocol (CDP) — 0.0.1756183

The Chrome DevTools Protocol is the JSON-over-WebSocket protocol that DevTools,
Puppeteer, ChromeDriver and Lighthouse use to inspect, debug and automate Chromium.
This set is the **tip-of-tree** protocol at Chromium revision **r1756183**
(git tag `v0.0.1756183` of
[ChromeDevTools/devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol),
the same number as the `devtools-protocol` npm package; schema version 1.3), which is
after the Chrome 159 branch point, so it matches the Chrome 160 dev/canary line.
It holds the raw protocol JSON, one generated page per domain (the content the
[protocol viewer](https://chromedevtools.github.io/devtools-protocol/) shows), the
viewer's landing page and the protocol changelog.

## Layout

| Path | What it holds |
|---|---|
| `api/browser_protocol.json`, `api/js_protocol.json` | The protocol definitions, unchanged. The source of truth. |
| `api/browser-protocol/<Domain>.md` | 53 browser domains: `Page`, `Network`, `Target`, `Fetch`, `Input`, `Emulation`, `DOM`, `CSS`, `Storage`, `Tracing`, `Browser`… `README.md` lists them all with method/event/type counts. |
| `api/js-protocol/<Domain>.md` | 6 V8 inspector domains (the protocol used to debug and profile Node.js too): `Runtime`, `Debugger`, `Profiler`, `HeapProfiler`, `Console`, `Schema`. |
| `content/index.md` | The viewer's landing page: scope and support policy, Protocol Monitor, `chrome.debugger`, FAQ, **HTTP endpoints** (`/json/version`, `/json/list`…) and their security rules. |
| `content/devtools-protocol-README.md` | Where the JSON, PDL and TypeScript types come from. |
| `content/release-notes/changelog-YYYY-MM.md` | Every protocol roll since 2024-03, with the PDL diff, one file per month. |

Each domain page has `## Methods` (`### Domain.method` with Parameters and Return
object tables), `## Events` and `## Types`. Status is marked **Experimental** /
**Deprecated** on domains, methods and individual parameters.

## Where to look for…

| Task | Look in |
|---|---|
| Connect to Chrome; what `--remote-debugging-port` exposes | `content/index.md` → "HTTP endpoints" |
| Get the browser-level WebSocket URL | `content/index.md` → `/json/version` (`webSocketDebuggerUrl`), `DevToolsActivePort` |
| Why a WebSocket gets `403` or the HTTP endpoint `500` | `content/index.md` → "Security and origin restrictions" (`--remote-allow-origins`, Host header) |
| Attach to tabs, iframes, workers; sessions | `api/browser-protocol/Target.md` (`Target.attachToTarget`, `flatten`, `sessionId`, `Target.setAutoAttach`) |
| Run JavaScript in the page | `api/js-protocol/Runtime.md` (`Runtime.evaluate`, `Runtime.callFunctionOn`) |
| Navigate, screenshot, PDF, lifecycle events | `api/browser-protocol/Page.md` (`Page.navigate`, `Page.captureScreenshot`, `Page.printToPDF`) |
| Intercept or mock requests | `api/browser-protocol/Fetch.md` (`Fetch.enable`, `Fetch.requestPaused`, `Fetch.fulfillRequest`) |
| Watch network traffic, headers, bodies | `api/browser-protocol/Network.md` (`Network.enable`, `Network.requestWillBeSent`, `Network.getResponseBody`) |
| Cookies and storage | `api/browser-protocol/Storage.md` (`Storage.getCookies`), `Network.md` (`Network.getCookies`) |
| Mouse, keyboard, touch | `api/browser-protocol/Input.md` (`Input.dispatchMouseEvent`, `Input.dispatchKeyEvent`) |
| Device, viewport, geolocation, timezone emulation | `api/browser-protocol/Emulation.md` (`Emulation.setDeviceMetricsOverride`) |
| Performance traces | `api/browser-protocol/Tracing.md` (`Tracing.start`), `Performance.md` |
| Browser-wide actions, downloads, permissions | `api/browser-protocol/Browser.md` |
| When a method/parameter was added or changed | `content/release-notes/` (grep the name) |
| Use CDP from DevTools itself or an extension | `content/index.md` → "Using Protocol Monitor", "DevTools protocol via Chrome extension" |

## Version notes

- **Tip-of-tree, no compatibility promise.** The landing page states CDP is not a
  public or supported API and syntax may change without notice; third parties are
  pointed at Puppeteer, ChromeDriver or Chrome DevTools for agents instead.
- **Stable vs experimental.** Only 14 browser domains are not marked experimental
  (`Browser`, `DOM`, `DOMDebugger`, `Emulation`, `Fetch`, `IO`, `Input`, `Log`,
  `Network`, `Page`, `Performance`, `Security`, `Target`, `Tracing`), plus `Runtime`,
  `Debugger`, `Profiler` in the JS protocol. `Console` and `Schema` are deprecated.
  Many methods inside "stable" domains are still experimental — check the flag.
- **Newer than stable Chrome.** Something here may not exist in the Chrome you run.
  Puppeteer 25.19.0 pins protocol `0.0.1724436` (Chrome 158 line); grep the
  changelog for a method to see when it landed.
- Recent changelog activity (Sept–Nov 2026) is mostly in `Network`, `Audits`,
  `Browser`, `Preload`, `Page` and the experimental `WebMCP` domain.
- `Target.attachToTarget` `flatten`: the docs say flat mode (passing `sessionId` on
  each message) will become the default and non-flat mode will be retired.
- The old "stable 1.3" (Chrome 64) snapshot is no longer published and isn't here.

## Search tips

- Name things the way the protocol does: `Domain.method` (`Page.navigate`),
  `Domain.event` (`Network.responseReceived`), `Domain.Type` (`Network.Request`).
  Types referenced from another domain link to that domain's page.
- Many domains deliver events only after `<Domain>.enable` (e.g. `Network.enable`: "network events will now be delivered").
- "Target" means anything debuggable (page, iframe, worker, service worker, the
  browser itself); a "session" is one attachment to a target.
- The JSON describes the protocol; the `.pdl` files and TypeScript types (not
  included) carry the same content.
- Chromium revisions are written `rNNNNNNN`; the package version `0.0.NNNNNNN` is
  that revision.
