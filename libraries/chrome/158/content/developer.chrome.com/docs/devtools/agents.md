# Chrome DevTools for agents

Source: https://developer.chrome.com/docs/devtools/agents

> Documentation index: https://developer.chrome.com/docs/devtools/llms.txt

![](http://developer.chrome.com/static/docs/devtools/agents/images/cd4a-hero.png)

# Chrome DevTools for agents

<br />

<br />

Help your agent build, debug, and verify your code correctly. With Chrome DevTools for agents, your AI agent can interact with the Chrome browser to test code, emulate users, and catch bugs using Chrome DevTools' capabilities before shipping. [Get started](http://developer.chrome.com/docs/devtools/agents/get-started.md.txt) [View on GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

## Install now

[Before installing, read the disclaimer and see all installation options on GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp#mcp-client-configuration)

### ![](https://developer.chrome.com/static/docs/devtools/agents/images/antigravity.svg)Antigravity

Chrome DevTools for agents comes pre-bundled with [Antigravity 2.0](https://antigravity.google/). You can start using it immediately with the *browser sub-agent*. Try using a slash command such as:

```
  /browser Navigate to the Google homepage
```

To access specialized agent skills, install the DevTools plugin during the **Build with Google** step of the initial setup or within the application settings.

### ![](https://developer.chrome.com/static/docs/devtools/agents/images/antigravity.svg)Antigravity CLI

```
  # Install as an Antigravity plugin (MCP+Skills).
  # Start Antigravity CLI and use:
  /plugin install chrome-devtools-plugin
```

### ![](https://developer.chrome.com/static/docs/devtools/agents/images/claude.svg)Claude Code

```
  # Install as a plugin (MCP+Skills)
  # Add the marketplace registry:
  /plugin marketplace add ChromeDevTools/chrome-devtools-mcp
  # Install
  /plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

### ![](https://developer.chrome.com/static/docs/devtools/agents/images/codex.svg)Codex

```
  codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```
If you are using any other coding agent like Copilot or OpenCode, follow the instructions [on our GitHub repository](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/client-configurations.md).
![Modern Web Guidance](https://developer.chrome.com/static/docs/modern-web-guidance/image/mwg-logo.svg)

**Looking to explore more of Chrome's agent tooling?** Use [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance.md.txt) to embed 200+ expert-vetted web platform skills and Baseline compatibility data directly into your coding agent.

## What can your agent do?

Give your agent the ability to interact with the web browser.
![](http://developer.chrome.com/static/docs/devtools/agents/images/emulate-user-experiences.png)

### Emulate user experiences

Test responsive designs, different geolocations, and real user flows. [Learn more](https://developer.chrome.com/docs/devtools/agents/use-cases/emulation.md.txt). ![](http://developer.chrome.com/static/docs/devtools/agents/images/debug-live.png)

### Debug your live browser

Connect to your active Chrome session to inspect, pause, and troubleshoot in real-time. [Learn more](https://developer.chrome.com/docs/devtools/agents/use-cases/auto-connect.md.txt). ![](http://developer.chrome.com/static/docs/devtools/agents/images/lighthouse-qa.png)

### Proactive QA with Lighthouse

Run audits for A11y, SEO, and performance to provide actionable checklists before you push code to production. [Learn more](https://developer.chrome.com/docs/devtools/agents/use-cases/lighthouse-audit.md.txt).

### Automate workflows with the CLI

Run fast, token-efficient browser commands directly from terminal scripts, CI/CD pipelines, or agent skills without MCP protocol overhead. [Explore the CLI](https://developer.chrome.com/docs/devtools/agents/cli.md.txt).

### Analyze memory leaks

Capture heap snapshots and allocation timelines so your agent can pinpoint detached DOM trees and memory retainers automatically. [Debug memory leaks](https://developer.chrome.com/docs/devtools/agents/memory.md.txt).

### Debug Chrome extensions

Sideload unpacked extensions, inspect background service workers, and test extension popups and content scripts in Chrome. [Debug extensions](https://developer.chrome.com/docs/devtools/agents/extensions.md.txt).

### Debug WebMCP tools

Discover, invoke, and validate structured WebMCP tools exposed by web pages so browser agents can interact reliably with your site. [Debug WebMCP](https://developer.chrome.com/docs/devtools/agents/webmcp-debugging.md.txt).

## Prompts that drive better user experiences

Give your AI agent the power to navigate websites, interact with buttons, explore pages, and run instant accessibility audits, all through a fully managed browser instance.

### Emulate Experiences

```
Go to developer.chrome.com on mobile, click the burger menu, and check for top-level navigation items.
```

```
Go to https://chrome.dev/devtools-store-locator. Simulate your location is Berlin and check if the store locator shows the Rosenthaler Strasse branch.
```

### Proactive QA (Lighthouse)

```
Run a Lighthouse accessibility audit and suggest fixes for any low-contrast elements.
```

```
Perform an SEO audit and verify all images have descriptive alt text.
```

## See Chrome's agentic tooling in action

Watch how to set up Chrome DevTools for agents and how it pairs with Modern Web Guidance to close the build-and-verify loop. [Watch all videos](https://www.youtube.com/watch?v=mogYbZ4CFB8&list=PLKkLHHhafabo) [Video](https://www.youtube.com/watch?v=hokTkVqKujY)

### Set up Chrome DevTools for agents

Learn how to set up Chrome DevTools for agents and see agents debugging and verifying autonomously. This video covers installation, handshake, and using the CLI for batch actions. [Video](https://www.youtube.com/watch?v=mogYbZ4CFB8)

### Agentic web development with Modern Web Guidance \& DevTools

See how Modern Web Guidance steers coding agents toward modern web features upfront while Chrome DevTools for agents verifies the rendered UI in a live browser. [![](http://developer.chrome.com/static/docs/modern-web-guidance/image/card-guide-catalog.png)](http://developer.chrome.com/docs/modern-web-guidance.md.txt)

### [Pair live browser verification with Modern Web Guidance](http://developer.chrome.com/docs/modern-web-guidance.md.txt)

Combine [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance.md.txt) with Chrome DevTools for agents to close the build-and-verify loop. Modern Web Guidance embeds 200+ expert-vetted skills, Baseline browser compatibility data, and a legacy refactoring workflow into your coding agent so it writes modern HTML, CSS, and JavaScript upfront---while Chrome DevTools for agents tests and verifies the live page in Chrome.

**Install Modern Web Guidance alongside DevTools for agents:**

```bash
npx modern-web-guidance@latest install
```
[Explore Modern Web Guidance](http://developer.chrome.com/docs/modern-web-guidance.md.txt) [![](http://developer.chrome.com/static/blog/policybazaar-agentic-audit/images/hero.png)](http://developer.chrome.com/blog/policybazaar-agentic-audit.md.txt)

### [Policybazaar \& Pensionbazaar: 92% less auditing effort](http://developer.chrome.com/blog/policybazaar-agentic-audit.md.txt)

Combined Chrome DevTools for agents with Modern Web Guidance to cut manual Core Web Vitals auditing overhead by 92% and new page turnaround by over 90%. [![](http://developer.chrome.com/static/blog/wetv-agentic-performance-debugging/images/wetv-hero.png)](http://developer.chrome.com/blog/wetv-agentic-performance-debugging.md.txt)

### [WeTV: 87% faster performance debugging in CI/CD](http://developer.chrome.com/blog/wetv-agentic-performance-debugging.md.txt)

Integrated Chrome DevTools for agents and Modern Web Guidance into CI/CD to automatically diagnose and fix 90% of recurring CLS regressions. [![](http://developer.chrome.com/static/docs/modern-web-guidance/image/card-modernization.png)](http://developer.chrome.com/docs/modern-web-guidance/modernization-workflow.md.txt)

### [Modernize codebases with the refactor skill](http://developer.chrome.com/docs/modern-web-guidance/modernization-workflow.md.txt)

Pair `npx modern-web-guidance@latest legacy-scan` with live DevTools verification to safely migrate legacy UI patterns to modern web features.