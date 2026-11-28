# Get started with Chrome DevTools for agents

Source: https://developer.chrome.com/docs/devtools/agents/get-started

> Documentation index: https://developer.chrome.com/docs/devtools/agents/get-started/llms.txt

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

Chrome DevTools for agents is a suite of tools that brings the power of Chrome
DevTools to your AI coding workflows. By installing Chrome DevTools for agents,
you gain access to:

- **MCP Server** : Connects your AI agent to a live browser instance using the open-source [Model Context
  Protocol](https://modelcontextprotocol.io/docs/getting-started/intro).
- **Chrome DevTools CLI**: An interface to interact with the browser directly from your terminal.
- **Agentic Skills**: Expert instructions that teach your agent how to coordinate multiple tools for complex tasks like accessibility or performance debugging.

In the context of web development, Chrome DevTools for agents integrates
debugging capabilities into your AI agent.

For example, an agent can use the tools to record and evaluate performance
traces to analyze the performance of a website and identify potential
improvements. Beyond web development, DevTools for agents also allows your agent
to browse the live web instead of just retrieving static HTML.

## Setup

This guide shows you how to set up Chrome DevTools for agents to help your
coding agent control and inspect a live Chrome browser.

Use the `chrome-devtools-mcp` package to control and inspect a live
Chrome browser from your coding agent (such as Gemini, Claude, Cursor, or
Copilot). Note that while Chrome DevTools for agents provides the full suite of
tools, the CLI only supports a targeted subset for shell-based automation.

### Supported IDEs and models

Chrome DevTools for agents supports any tool or IDE that supports the MCP
protocol. This includes Antigravity, Gemini CLI, Claude Code, Cursor, Copilot,
and more.

### Security considerations

> [!WARNING]
> **Warning:** Chrome DevTools for agents exposes your browser content to your agent. This allows your agent to read, inspect, debug, and modify any data in the browser or DevTools.

Because your agent will be able to view and interact with the pages it accesses,
it can effectively act on your behalf if you connect it to a browser with an
active, authenticated session. Avoid sharing sensitive or personal information
that you don't want to share with agents.

### Prerequisites

Before you install Chrome DevTools for agents, ensure your environment meets the
following requirements:

- [Node.js](https://nodejs.org/) (latest LTS version) and [npm](https://www.npmjs.com/)
- [Chrome](https://www.google.com/intl/de/chrome/) (current stable version)

To set up Chrome DevTools for agents, choose the method that matches your
preferred coding environment. While some agents require manual installation,
others come with the tools pre-integrated.

### Antigravity

Chrome DevTools for agents comes pre-bundled with [Antigravity
2.0](https://antigravity.google/). You can start using it immediately with the
*browser sub-agent*. Try using a slash command such as:

```bash
/browser Navigate to the Google homepage
```

To access specialized agent skills, we recommend installing the DevTools plugin
during the **Build with Google** step of the initial setup or within the
application settings. For more information, check out the [Antigravity Browser
Subagent documentation](https://antigravity.google/docs/browser-subagent).

### Install using CLI

To set up Chrome DevTools for agents, you can use a JSON configuration file or a
CLI command to install the server directly if your agent supports it. Some
agents also offer official extensions or plugins that include agent skills,
expert instructions that help your agent use DevTools features.

If your agent is not listed here, you can find how to install it in the [Chrome
DevTools for Agents GitHub
repository](https://github.com/ChromeDevTools/chrome-devtools-mcp#mcp-client-configuration).

To add Chrome DevTools for agents to a command-line agent, use the built-in CLI
commands for your specific agent:

#### Gemini CLI

Install the Gemini CLI extension that includes the MCP package and the
accompanying skills using the following command:

```bash
# Gemini extension (MCP+Skills)
  gemini extensions install --auto-update https://github.com/ChromeDevTools/chrome-devtools-mcp
```

Install only the MCP package with the following command:

```bash
# MCP only
gemini mcp add chrome-devtools npx chrome-devtools-mcp@latest
```

#### Claude Code

To install Chrome DevTools for agents as a Claude Code Plugin use the following
slash commands in Claude Code. Add the marketplace registry:

```bash
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
```

And install the plugin from the marketplace registry:

```bash
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

See the official [Chrome DevTools Claude Plugin
page](https://claude.com/plugins/chrome-devtools-mcp) for more information.

#### Codex

```bash
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

### Install using JSON configuration

For other agents that support the `mcpServers` configuration key, manually add
this entry and make sure to install DevTools for agents through `npm i
chrome-devtools-mcp`.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

### Install in other agents

To configure for an agent that is not listed, see the
[Chrome DevTools MCP GitHub
repository](https://github.com/ChromeDevTools/chrome-devtools-mcp?tab=readme-ov-file#mcp-client-configuration).

## Test your setup

Enter the following prompt in your agent to check if everything is working:

    Check the performance of https://developers.chrome.com

Your agent should open a browser window and record a performance trace.

## Troubleshoot your setup

[Video](https://www.youtube.com/watch?v=1AD81ZselPk)

If your agent fails to run tools and has access to Chrome DevTools skills, it
might attempt to fix the problem automatically. If it doesn't, you can
explicitly prompt the agent:

    Use the Chrome DevTools troubleshooting skill to fix my setup.

Or you can be more specific:

    I'm having trouble with Chrome DevTools for agents. I tried to run [Tool Name]
    but got the error: [Error Message]. I am on [OS Name]. Use the Chrome DevTools
    troubleshooting skill to fix my setup.

## Add official Chrome documentation to your agent

The [Developer Knowledge MCP server](https://developers.google.com/knowledge/mcp)
is a remote server that searches live, official Google developer
documentation, including `developer.chrome.com` and `web.dev`, so your agent
can ground its answers in current docs. It provides the `search_documents`,
`get_documents`, and `answer_query` tools and complements the Chrome DevTools
MCP server: Chrome DevTools for agents lets your agent inspect what's
happening in the browser, and the Developer Knowledge MCP server lets it look
up *why*---for example, what a DevTools panel reports, how a performance metric
is defined, or how a Chrome API behaves.

To add it to your agent, follow
[Configure your IDE or coding agent](https://developers.google.com/knowledge/mcp#configure-ide)
and select your client. To help your agent know when to search the docs, also
install the
[`retrieving-developer-knowledge`](https://developers.google.com/knowledge/mcp#agent-skill)
agent skill.

You can then combine both tools in one prompt:

    Record a performance trace of https://developers.chrome.com, then look up the
    official Chrome docs on Interaction to Next Paint and suggest fixes for the
    slowest interaction.

## Next steps

To customize your setup, see [Configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt).