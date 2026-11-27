# Configuration

Source: https://developer.chrome.com/docs/devtools/agents/get-started/configuration

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

[Video](https://www.youtube.com/watch?v=hokTkVqKujY)

You can configure Chrome DevTools for agents to customize how it interacts
with the browser, which tools are enabled, and how it handles data.

Configure the server by passing command-line flags in the `args` array of
your Model Context Protocol (MCP) client configuration file. This is typically
the `config.json` file.

For example, to run Chrome in headless mode and use the Canary channel, use
the following configuration:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--headless",
        "--channel=canary"
      ]
    }
  }
}
```

*** ** * ** ***

## Common configuration scenarios

The following scenarios describe common ways to configure Chrome DevTools for
agents.

### Run in headless mode

To perform background tasks without a visible browser window, run Chrome in
headless (no UI) mode. Add the `--headless` flag to your server arguments.

### Connect to an existing browser session

By default, DevTools for agents starts a new Chrome instance. However, you
can connect your agent to an existing browser session. This is useful if your
agent needs to investigate an issue in a session you've already started (for
example, if you are already signed in).

> [!CAUTION]
> **Caution:** When you connect to an existing session, your agent inherits your active session, including logged-in accounts, cookies, and other data. Only use this mode with agents you trust.

You can connect to an existing session in two ways:

#### Automatic connection (Chrome 144+)

If you use the `--autoConnect` flag, the MCP server automatically connects to an active Chrome instance.

1. In your running Chrome browser, navigate to `chrome://inspect/#remote-debugging` and enable **Remote Debugging**.
2. Add `--autoConnect` to your MCP configuration: `json
   "args": ["chrome-devtools-mcp@latest", "--autoConnect"]`
3. When the agent attempts to connect, Chrome shows a dialog asking for permission. Click **Allow**.

#### Manual connection

If you cannot use `--autoConnect` (for example, in a sandboxed environment),
you can manually start Chrome with a debugging port and connect using
`--browser-url`.

1. Start Chrome from the terminal with remote debugging enabled and a custom user data directory.
   - **macOS** : `shell
     /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-profile-stable`
   - **Windows** : `shell
     start chrome --remote-debugging-port=9222 --user-data-dir=%TEMP%\chrome-profile-stable`
   - **Linux** : `shell
     google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-profile-stable`
2. Configure your agent to connect to this port: `json
   "args": ["chrome-devtools-mcp@latest", "--browser-url=http://127.0.0.1:9222"]`

### Allow file access outside the temporary directory

Tools that read or write files (for example, saving screenshots, traces, or
loading extensions) can only access paths within the configured workspace
roots. The server uses the roots that your MCP client provides through the MCP
roots capability, plus any directories that you pass with `--filesystemRoot`
(alias `--workspace`). If your client doesn't provide roots and you don't set
`--filesystemRoot`, file access is limited to the OS temporary directory.
Requests for other paths fail with an `Access denied: ... is not within any of
the configured workspace roots` error.

To allow access to a project directory, add `--filesystemRoot` to your server
arguments. You can repeat the flag to allow multiple directories:

```json
"args": ["chrome-devtools-mcp@latest", "--filesystemRoot=/path/to/project"]
```

## Configuration options reference

The following sections list the available configuration flags. For the latest
options and updates, see the [Chrome DevTools MCP GitHub
repository](https://github.com/ChromeDevTools/chrome-devtools-mcp#configuration).

### Connection options

Use these options to configure how the server connects to Chrome.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--autoConnect` or `--auto-connect` | boolean | `false` | Automatically connects to a locally running Chrome (144+) instance. Requires remote debugging to be enabled using `chrome://inspect/#remote-debugging`. |
| `--browserUrl` or `--browser-url` `-u` | string | `false` | Connect to a running, debuggable Chrome instance (for example, `http://127.0.0.1:9222`). |
| `--wsEndpoint` or `--ws-endpoint` `-w` | string | `false` | WebSocket endpoint to connect to a running Chrome instance (for example, `ws://127.0.0.1:9222/devtools/browser/<id>`). Alternative to `--browserUrl`. |
| `--wsHeaders` or `--ws-headers` | string | `false` | Custom headers for WebSocket connection in JSON format (for example, `'{"Authorization":"Bearer token"}'`). Only works with `--wsEndpoint`. |

### Browser launch options

These options apply when the MCP server starts Chrome.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--headless` | boolean | `false` | Runs Chrome in headless (no UI) mode. |
| `--channel` | string | `stable` | Specifies the Chrome channel to use. Choices: `canary`, `dev`, `beta`, and `stable`. |
| `--executablePath` or `--executable-path` `-e` | string | `false` | Path to a custom Chrome executable. |
| `--userDataDir` or `--user-data-dir` | string | See description | Path to the user data directory. Default is `$HOME/.cache/chrome-devtools-mcp/chrome-profile$CHANNEL_SUFFIX_IF_NON_STABLE`. |
| `--isolated` | boolean | `false` | Creates a temporary user data directory that is automatically cleaned up when the browser closes. |
| `--viewport` | string | `false` | Initial viewport size (for example, `1280x720`). In headless mode, max size is `3840x2160`. |
| `--proxyServer` or `--proxy-server` | string | `false` | Proxy server configuration passed to Chrome. |
| `--chromeArg` or `--chrome-arg` | array | `false` | Additional arguments to pass to Chrome. |
| `--ignoreDefaultChromeArg` or `--ignore-default-chrome-arg` | array | `false` | Explicitly disable default arguments for Chrome. |

### Security and privacy options

Use these options to manage security settings and data privacy.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--acceptInsecureCerts` or `--accept-insecure-certs` | boolean | `false` | Ignores errors related to self-signed and expired certificates. Use with caution. |
| `--blockedUrlPattern` or `--blocked-url-pattern` | array | `false` | Restricts network access by blocking specified URL patterns (uses [URLPattern](https://urlpattern.spec.whatwg.org/)). Blocks navigations and subresources. |
| `--allowedUrlPattern` or `--allowed-url-pattern` | array | `false` | Restricts network access by allowing only specified URL patterns. Requires Chrome 149+. |
| `--redactNetworkHeaders` or `--redact-network-headers` | boolean | `false` | Redacts sensitive network headers before returning them to the client. |
| `--usageStatistics` or `--usage-statistics` | boolean | `true` | Enables collection of usage statistics to improve the tool. Can also be disabled using the `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` or `CI` environment variables. |
| `--performanceCrux` or `--performance-crux` | boolean | `true` | Sends URLs from performance traces to the Google CrUX API to fetch real-user experience data. |
| `--javascriptEvaluation` or `--javascript-evaluation` | boolean | `true` | Set to `false` to disable JavaScript execution. When disabled, the script evaluation tools are disabled, the `initScript` parameter of `navigate_page` is turned off, and navigating to `javascript:`, `data:`, or `vbscript:` URLs is disallowed. |
| `--filesystemRoot` or `--filesystem-root` `--workspace` | array | OS temporary directory | A directory that file-accessing tools are allowed to use, in addition to the roots provided by the MCP client. Can be specified more than once. See [Allow file access outside the temporary directory](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt#filesystem-root). |
| `--allowUnrestrictedPaths` or `--allow-unrestricted-paths` | boolean | `false` | **Deprecated** : Use `--workspace=/` instead. Disables the path restriction that applies when the MCP client doesn't provide roots. |

### Feature categories

You can enable or disable groups of tools using these flags.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--categoryInput` or `--category-input` | boolean | `true` | Enables tools related to input. |
| `--categoryNavigation` or `--category-navigation` | boolean | `true` | Enables tools related to navigation. |
| `--categoryEmulation` or `--category-emulation` | boolean | `true` | Enables tools related to emulation. |
| `--categoryNetwork` or `--category-network` | boolean | `true` | Enables tools related to network. |
| `--categoryPerformance` or `--category-performance` | boolean | `true` | Enables tools related to performance. |
| `--categoryDebugging` or `--category-debugging` | boolean | `true` | Enables tools related to debugging. |
| `--categoryMemory` or `--category-memory` | boolean | `true` | Enables tools related to memory. |
| `--categoryExtensions` or `--category-extensions` | boolean | `false` | Enables tools related to extensions. Only supported with pipe connection. |
| `--categoryPwa` or `--category-pwa` | boolean | `false` | Enables tools for automating Progressive Web Apps (install, launch, uninstall, and OS state). Only supported with pipe connection. |
| `--categoryExperimentalThirdParty` or `--category-experimental-third-party` | boolean | `false` | Enables [third-party developer tools](https://developer.chrome.com/docs/devtools/agents/use-cases/third-party-tools.md.txt) exposed by the inspected page. |
| `--categoryExperimentalWebmcp` or `--category-experimental-webmcp` | boolean | `false` | Enables debugging WebMCP tools. Requires Chrome 149+ with WebMCP features enabled. |
| `--memoryDebugging` or `--memory-debugging` | boolean | `false` | Enables memory debugging tools. |

### Screenshot options

Use these options to customize how the agent captures screenshots.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--screenshotFormat` or `--screenshot-format` | string | `false` | Overrides the default output format (`png`). Choices: `jpeg`, `png`, and `webp`. The `jpeg` and `webp` formats are smaller, which helps reduce context size in AI conversations. |
| `--screenshotQuality` or `--screenshot-quality` | number | `false` | Overrides compression quality (0-100) for `jpeg` and `webp`. |
| `--screenshotMaxWidth` or `--screenshot-max-width` | number | `false` | Maximum width in pixels. Larger screenshots are downscaled. |
| `--screenshotMaxHeight` or `--screenshot-max-height` | number | `false` | Maximum height in pixels. Larger screenshots are downscaled. |

### Experimental options

Use these options to enable experimental features that are under development.

> [!WARNING]
> **Experimental:** These options are experimental and may change or be removed in future versions.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--experimentalDevtools` or `--experimental-devtools` | boolean | `false` | Enables automation over DevTools targets. |
| `--experimentalVision` or `--experimental-vision` | boolean | `false` | Enables coordinate-based tools (for example, `click_at`). Usually requires a computer-use model that can produce accurate coordinates by looking at screenshots. |
| `--experimentalStructuredContent` or `--experimental-structured-content` | boolean | `false` | Outputs structured formatted content. |
| `--experimentalIncludeAllPages` or `--experimental-include-all-pages` | boolean | `false` | Includes all kinds of pages (for example, webviews and background pages). |
| `--experimentalScreencast` or `--experimental-screencast` | boolean | `false` | Exposes screencast tools (requires `ffmpeg` in PATH). |
| `--experimentalFfmpegPath` or `--experimental-ffmpeg-path` | string | `false` | Path to `ffmpeg` executable. |
| `--experimentalScreencastFps` or `--experimental-screencast-fps` | number | `false` | Frames per second for screencast recording. Lower values can reduce memory pressure on pages that produce frames faster than `ffmpeg` can encode them. |

### Other options

Use these options to configure logging, page routing, and source maps, or to
enable a simplified set of tools.

| Flag | Type | Default | Description |
|---|---|---|---|
| `--slim` | boolean | `false` | Exposes a slim set of three tools (navigation, script execution, and screenshots). Useful for basic browser tasks. |
| `--pageIdRouting` or `--page-id-routing` | boolean | `true` | Requires `pageId` on page-scoped tools and routes requests by page ID, which is useful for concurrent agent sessions. Use `--no-page-id-routing` to disable. |
| `--sourceMaps` or `--source-maps` | boolean | `true` | Enables source maps in DevTools. Use `--no-source-maps` to disable. |
| `--logFile` or `--log-file` | string | `false` | Path to a file to write debug logs to. Set the `NODE_DEBUG` environment variable to `*` to enable verbose logs. |
| `--config` | string | `false` | Path to a JSON configuration file. |

## Environment variables

You can also use the following environment variables to configure the server:

- `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS`: If set, disables usage statistics collection (equivalent to `--no-usage-statistics`).
- `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS`: If set, disables periodic checks for updates.
- `CI`: If set, disables usage statistics collection.
- `NODE_DEBUG`: Set to `*` to enable verbose debug logging (works in conjunction with `--logFile`).