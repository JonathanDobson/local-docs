# Connect your AI agent to your personal browser with auto-connect

Source: https://developer.chrome.com/docs/devtools/agents/use-cases/auto-connect

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

Connect your AI agent directly to your active browser instance with the
auto-connect feature. This allows your agent to bypass sandbox limitations by
inheriting your current tabs, browser extensions, and live application state.

Inheriting your workflow context lets your agent move from writing code to
debugging your live browser state without losing session data. This is useful
when you have already reached a specific application state (such as a complex
checkout flow or a manually reproduced error) and want your agent to take over
the technical investigation without re-executing those steps manually.

Consider the following before enabling auto-connect:

- **Security and privacy:** When auto-connect is active, your agent has access to all data in your browser profile, including open tabs, session storage, local storage, cookies, and other data surfaced through JavaScript APIs.
- **Data sent to Google:** The Chrome DevTools for agents server runs as a
  local process. However, by default, it sends the following data to Google,
  regardless of the connection mode:

  - **Usage statistics** , such as tool invocation success rates, latency, and environment information. To opt out, use the `--no-usage-statistics` flag or set the `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` environment variable.
  - **URLs from performance traces** , which are sent to the Chrome UX Report (CrUX) API to fetch real-user experience data. To opt out, use the `--no-performance-crux` flag.

  For more information, see
  [Security and privacy options](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt#security-and-privacy-options).
- **Trust and prompts:** Use this mode only with agents you trust and be
  careful with the information you include in prompts.

## Prerequisites

Before you use the auto-connect feature, ensure you have the following:

- **Chrome 144+**: Auto-connect requires modern debugging protocols found in current versions of Chrome.
- **Correct Chrome channel** : Your agent connects to Chrome Stable by default. To use Canary or Beta, specify the channel in your [configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt#browser-launch-options).
- **Remote debugging enabled**: Manually enable the bridge between your browser and the agent.
- **Correct configuration** : You must update the MCP configuration to include the `--autoConnect` flag. See [Configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt#connection-options) for details.

## Set up auto-connect

To configure the auto-connect feature in your MCP server, do the following:

1. In your running Chrome browser, navigate to `chrome://inspect/#remote-debugging` and enable remote debugging.
2. Update your MCP configuration to include the `--autoConnect` flag:

   ```json
   {
     "mcpServers": {
       "chrome-devtools": {
         "command": "npx",
         "args": ["chrome-devtools-mcp@latest", "--autoConnect"]
       }
     }
   }
   ```

   To opt out of sending usage statistics and performance trace URLs to
   Google, also add the `--no-usage-statistics` and `--no-performance-crux`
   flags to `args`.
3. Prompt your agent to interact with your open Chrome app. When Chrome asks
   for permission to allow the session, click **Allow**.

Your agent now uses the MCP server to interact with your running Chrome
application. For more information on configuration options, see the [Configuration guide](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt).

## Use cases for auto-connect

Auto-connect lets you use tools or states that can't be used on sandboxed
Chrome sessions. For example, instead of asking your agent to sign in, which
often fails, you can navigate to the page yourself and sign in. Then, ask your
agent to take over.

The following sections include some examples of use cases for the auto-connect
feature.

> [!NOTE]
> **Note:** Agent execution steps are examples of potential behavior. Your agent may act differently.

### Debug authenticated dashboards

Internal tools and private dashboards often sit behind complex single sign-on
(SSO) or virtual private network (VPN) layers. A sandboxed browser usually
requires a sign-in that your agent can't bypass. With auto-connect, your agent
inherits your active session.

**Example prompt:**

    I have my company's staging dashboard open in the next tab. Can you look at the
    User Analytics chart, find the SVG element for the Friday data point, and tell
    me why the tooltip isn't appearing on hover?

**Example agent execution:** Your agent identifies your existing Chrome process,
finds the active tab, and inspects the accessibility tree to locate the
elements. It may also use JavaScript APIs to evaluate specific conflicts.

### Live-fix your current tab

Avoid manually reproducing errors. Instead of translating reproduction steps
into a new prompt for a sandboxed agent, you can ask your agent to fix the bug
on the active page where you already encountered it.

**Example prompt:**

    Look at the current page. The Submit button overlaps with the footer on this
    screen size. Generate a fix for the layout and verify it by injecting the CSS
    directly into this tab.

**Example agent execution:** Because it's connected to your active window, your
agent analyzes your layout and applies the fix instantly. You see the button
move on your screen, which confirms the fix works before you update the source
code.