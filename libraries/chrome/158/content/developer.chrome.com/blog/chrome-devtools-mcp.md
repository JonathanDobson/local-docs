# Chrome DevTools (MCP) for your AI agent

Source: https://developer.chrome.com/blog/chrome-devtools-mcp

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Michael Hablich](https://web.dev/images/authors/hablich.jpg) Michael Hablich [GitHub](https://github.com/natorion) [LinkedIn](https://www.linkedin.com/in/michael-hablich) [Bluesky](https://bsky.app/profile/mhablich.bsky.social) [Homepage](https://hablich.dev/)

<br />


Published: September 23, 2025

<br />

> [!IMPORTANT]
> **Important:** The Chrome DevTools MCP server is now part of [Devtools for agents](https://developer.chrome.com/docs/devtools/agents). To learn how to install it for any agent, see [Get started with Chrome DevTools for agents.](https://developer.chrome.com/docs/devtools/agents/get-started.md.txt)

We're launching today a public preview for the new [Chrome DevTools Model
Context Protocol (MCP)
server](https://github.com/ChromeDevTools/chrome-devtools-mcp/), bringing the
power of Chrome DevTools to AI coding assistants.

Coding agents face a fundamental problem: they are not able to see what the code
they generate actually does when it runs in the browser. They're effectively
programming with a blindfold on.

The Chrome DevTools MCP server changes this. AI coding assistants are able to
debug web pages directly in Chrome, and benefit from DevTools debugging
capabilities and performance insights. This improves their accuracy when
identifying and fixing issues.

See for yourself how it works:

## What is the Model Context Protocol (MCP)?

The [Model Context Protocol
(MCP)](https://www.anthropic.com/news/model-context-protocol) is an open-source
standard for connecting large language models (LLMs) to external tools and data
sources. The Chrome DevTools MCP server adds debugging capabilities to your AI
agent.

For example, the Chrome DevTools MCP server provides a tool called
`performance_start_trace`. When tasked to investigate the performance of your
website, an LLM can use this tool to start Chrome, open your website and use
Chrome DevTools to record a performance trace. The LLM can then analyze the
performance trace to suggest potential improvements. Using the MCP protocol, the
Chrome DevTools MCP server can bring new debugging capabilities to your coding
agent to make it better at building websites.

If you want to find out more about how MCP works, check out the [MCP
documentation](https://modelcontextprotocol.io/docs/getting-started/intro).

## What can you use it for?

Following are a few example prompts you can try out in the AI assistant of your
choice like Gemini CLI.

### Verify code changes in real-time

Generate a fix with your AI agent, and then automatically verify that the
solution works as intended with Chrome DevTools MCP.

Prompt to try:

    Verify in the browser that your change works as expected.

### Diagnose network and console errors

Empower your agent to analyze network requests to uncover CORS issues or inspect
console logs to understand why a feature isn't working as expected.

Prompt to try:

    A few images on localhost:8080 are not loading. What's happening?

### Simulate user behavior

Navigate, fill out forms, and click buttons to reproduce bugs and test complex
user flows---all while inspecting the runtime environment.

Prompt to try:

    Why does submitting the form fail after entering an email address?

### Debug live styling and layout issues

Ask your AI agent to connect to a live page, inspect the DOM and CSS, and get
concrete suggestions to fix complex layout problems like overflowing elements
based on live data from the browser.

Prompt to try:

    The page on localhost:8080 looks strange and off. Check what's happening there.

### Automate performance audits

Instruct your AI agent to run a performance trace, analyze the results, and
investigate specific performance issues like high LCP numbers.

Prompt to try:

    Localhost:8080 is loading slowly. Make it load faster.

See our [tool reference
documentation](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md)
for a list of all available tools.

## Get started

To try this out, add the following config entry to your MCP client:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}

```

To check if it works, run the following prompt in your coding agent:

    Please check the LCP of web.dev.

For more details, check out [the Chrome DevTools MCP
documentation](https://github.com/ChromeDevTools/chrome-devtools-mcp/?tab=readme-ov-file#chrome-devtools-mcp)
on GitHub.

## Get involved

We are building Chrome DevTools MCP incrementally, starting with the public
preview version we're releasing today. We're actively looking for feedback from
you and the community about which capabilities we should add next. Whether
you're a developer using AI coding assistants or a vendor building the next
generation of AI development tools, your insights will be invaluable and if
something is missing or not working, please file [an issue on
GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/new/choose).