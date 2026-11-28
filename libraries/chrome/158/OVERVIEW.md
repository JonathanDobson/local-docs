# Google Chrome 158: command line, headless, DevTools Protocol and automation

How to control Google Chrome / Chromium from outside the browser, for
**Chrome 158 (158.0.8127.88)**, the Stable release on 2026-11-28. It brings
several official sources together:

- every command-line switch, generated from the Chromium source at tag
  `158.0.8127.88`;
- the full Chrome DevTools Protocol (CDP) for that exact release, from the PDL
  definition files in Chromium plus V8 15.8.62.31's `js_protocol.pdl`;
- Chromium's own docs on headless mode, ChromeDriver and Chrome for Testing;
- developer.chrome.com pages on automation and testing, Headless, ChromeDriver
  and "Chrome DevTools for agents" (taken 2026-11-28, not versioned);
- the chrome-devtools-mcp 1.14.0 docs (MCP server and `chrome-devtools` CLI).

There is **no official, hand-written switch reference** for Chrome. The switch
pages are the source comments, often terse, and many switches are
developer- or test-only. Puppeteer is a separate set
(`libraries/puppeteer/25.19.0`, which drives Chrome 158.0.8127.88).
Playwright is `libraries/playwright/1.65.0`.
The latest development (tip-of-tree, Chrome 160) protocol and the protocol
changelog are in `libraries/chrome-devtools-protocol/0.0.1756183`.

## Layout

| Path | What it holds |
|---|---|
| `content/01-command-line-switches/` | One page per Chromium `*_switches.{h,cc}` file (97 files, 1,258 switches). Each switch has its `--name`, the C++ constant, the source comment and any platform `#if` condition. **`ALL-SWITCHES.md` is the A–Z index.** The most useful pages are `chrome__common__chrome_switches.md`, `content__public__common__content_switches.md`, `base__base_switches.md`, `headless__public__switches.md`, `components__headless__command_handler__headless_command_switches.md` and `sandbox__policy__switches.md`. |
| `content/00-devtools-protocol-overview.md` | The CDP site's home page: scope and support policy, the stable 1.3 and tip-of-tree protocol versions, the HTTP endpoints (`/json/version`, `/json` or `/json/list`, `/json/new?{url}`, `/json/activate/{targetId}`, `/json/close/{targetId}`, `/json/protocol`), WebSocket URLs, and security (`--remote-allow-origins`). |
| `api/cdp/` | The CDP reference: one page per domain (`Page.md`, `Runtime.md`, `Target.md`, `Network.md`, `Input.md`, `Emulation.md`, `Browser.md`, `Fetch.md`…), each listing commands with parameters and return values, events and types. `README.md` lists all 59 domains. |
| `api/pdl/` | The raw protocol definitions: `browser_protocol.pdl`, `domains/*.pdl` and `js_protocol.pdl`. |
| `content/02-chromium-source-docs/` | Docs from the Chromium tree at the tag: `headless/README.md` (headless library and shell), `chromedriver/` (README, design notes), `chrome_for_testing/`, `gpu/` (GPUs in headless Chrome), `user_data_dir.md` (profile locations per OS), `devtools_protocol/` (README and SECURITY of the protocol definitions). |
| `content/developer.chrome.com/docs/automation-and-testing/` | Headless mode (`headless.md`), the Headless command-line reference (`headless-cli.md`), `chrome-headless-shell` (`headless-chrome-shell.md`), debugging headless (`debug-headless.md`), screen configuration (`headless-screen-config.md`), Chrome for Testing, release channels. |
| `content/developer.chrome.com/docs/chromedriver/` | ChromeDriver: get started, capabilities and `goog:chromeOptions`, logging and the performance log, mobile emulation, extensions, downloads and version selection, security, help pages (Chrome doesn't start, crashes, clicking issues, keyboard). |
| `content/developer.chrome.com/docs/devtools/agents/` | Chrome DevTools for agents: get started and configuration, the CLI, extensions, memory, use cases (auto-connect to a running Chrome, emulation, Lighthouse audits, third-party tools). |
| `content/developer.chrome.com/docs/devtools/` | `protocol-monitor.md` (watch and send CDP messages from DevTools) and `remote-debugging/` (Android devices, port forwarding, WebViews). |
| `content/developer.chrome.com/blog/` | Background posts: `headless-chrome.md`, `chrome-headless-shell.md`, `removing-headless-old-from-chrome.md`, `chrome-for-testing.md`, `remote-debugging-port.md`, the WebDriver BiDi posts, the chrome-devtools-mcp posts, `cdp-command-editor.md`. |
| `content/03-chrome-for-testing/README.md` | The Chrome for Testing JSON API (`last-known-good-versions(-with-downloads).json`, `known-good-versions…`, `latest-versions-per-milestone…`, per-version `<version>.json`) and download URLs. |
| `content/04-chrome-devtools-mcp/` | chrome-devtools-mcp 1.14.0: `README.md`, `docs/tool-reference.md` (every MCP tool), `docs/slim-tool-reference.md`, `docs/cli.md` (the `chrome-devtools` command), `docs/configuration.md`, `docs/client-configurations.md`, `docs/troubleshooting.md`, `CHANGELOG.md`. |
| `content/release-notes/chrome-158-beta.md` | The Chrome 158 beta announcement (web platform changes). |

## Where to look for…

| Task | Look in |
|---|---|
| What a switch does / does a switch exist | `content/01-command-line-switches/ALL-SWITCHES.md`, then the linked page |
| Start Chrome so a script can drive it over CDP | `--remote-debugging-port` / `--remote-debugging-pipe` in `content__public__common__content_switches.md`; `developer.chrome.com/blog/remote-debugging-port.md` (from Chrome 136 these need a non-default `--user-data-dir`); `00-devtools-protocol-overview.md` for `/json/version` and the WebSocket URL |
| Allow a WebSocket client from another origin | `--remote-allow-origins` in `00-devtools-protocol-overview.md` and `content__public__common__content_switches.md` |
| Run headless; screenshot, PDF or DOM from the shell | `developer.chrome.com/docs/automation-and-testing/headless.md` and `headless-cli.md` (`--dump-dom`, `--screenshot`, `--print-to-pdf`, `--virtual-time-budget`…); `components__headless__command_handler__headless_command_switches.md` |
| New Headless vs `chrome-headless-shell` vs `--headless=old` | `blog/removing-headless-old-from-chrome.md` (old mode removed from Chrome in 132), `docs/automation-and-testing/headless-chrome-shell.md`, `blog/chrome-headless-shell.md` |
| Profiles and where Chrome keeps state | `02-chromium-source-docs/user_data_dir.md`; `--user-data-dir`, `--profile-directory`, `--incognito` |
| Send a CDP command (navigate, screenshot, evaluate JS, input) | `api/cdp/Page.md` (`Page.navigate`, `Page.captureScreenshot`, `Page.printToPDF`), `api/cdp/Runtime.md` (`Runtime.evaluate`), `api/cdp/Input.md`, `api/cdp/Target.md` (`Target.createTarget`, `Target.attachToTarget`, `Target.getTargets`) |
| Intercept or mock network requests | `api/cdp/Fetch.md`, `api/cdp/Network.md` |
| Emulate device, viewport, geolocation, timezone | `api/cdp/Emulation.md`; ChromeDriver `mobile-emulation.md` |
| Selenium / WebDriver with Chrome | `developer.chrome.com/docs/chromedriver/` (`capabilities.md` for `goog:chromeOptions`, `args`, `debuggerAddress`) |
| Download a pinned Chrome / ChromeDriver for CI | `03-chrome-for-testing/README.md`, `docs/automation-and-testing/chrome-for-testing.md`, `blog/chrome-for-testing.md` (`npx @puppeteer/browsers install chrome@stable`) |
| Let an AI agent / MCP client control Chrome | `04-chrome-devtools-mcp/README.md`, `docs/tool-reference.md`, `docs/cli.md`; `developer.chrome.com/docs/devtools/agents/` |
| Turn features on or off | `--enable-features` / `--disable-features` in `base__base_switches.md` (feature names themselves are not listed) |
| Chrome crashes in Docker / CI | `--no-sandbox` (`sandbox__policy__switches.md`), `--disable-dev-shm-usage` (`base__base_switches.md`), `chromedriver/help/chrome-doesnt-start.md` |
| GPU in headless Linux | `02-chromium-source-docs/gpu/` |

## Version notes

- **Chrome 158.0.8127.88**, Chromium branch position 1727472, V8 15.8.62.31.
  CDP is protocol version 1.3 (the `version` block in `browser_protocol.pdl`).
  Experimental and deprecated items are marked in the CDP pages.
- **Chrome 136**: `--remote-debugging-port` and `--remote-debugging-pipe` are
  ignored for the default Chrome data directory. They must now come with
  `--user-data-dir` pointing at a non-standard directory
  (`blog/remote-debugging-port.md`).
- **Chrome 132**: the old Headless mode was removed from the Chrome binary.
  `--headless=old` now prints an error. The old mode lives on as the separate
  `chrome-headless-shell` binary (`blog/removing-headless-old-from-chrome.md`).
- The CDP site says CDP is **not a supported public API** and has no
  backwards-compatibility promise. It points third-party tools to Chrome
  DevTools for agents, Puppeteer or ChromeDriver (`00-devtools-protocol-overview.md`).
- The google-chrome installed on this machine is **151.0.7922.71**, older than
  this set.

## Search tips

- Switches are written without dashes in the source. Pages show them as
  `` `--name` `` headings, and the constant as `kName` (e.g.
  `kRemoteDebuggingPort`). Search for either.
- The same switch can be defined in several components, e.g. `--headless`,
  `--user-data-dir`, `--window-size`, `--proxy-server`, `--user-agent`. Each
  page header names its source file. `headless__public__*` and
  `content__shell__*` are for the headless shell and content shell, not for
  `google-chrome` itself.
- CDP methods are `Domain.method` (`Page.navigate`). Events are
  `Domain.eventName` (`Page.loadEventFired`, `Target.attachedToTarget`). Types
  are `Domain.Type` (`Runtime.RemoteObject`).
- "Chrome for Testing" (CfT) is a separate Chrome build for automation, not
  for browsing. "Headless shell" means `chrome-headless-shell`. "BiDi" means
  WebDriver BiDi, the W3C cross-browser successor protocol to CDP-style
  automation.
- "Chrome DevTools for agents" and "chrome-devtools-mcp" are the same product.
  The CLI binary is `chrome-devtools`, installed from the `chrome-devtools-mcp`
  npm package.
