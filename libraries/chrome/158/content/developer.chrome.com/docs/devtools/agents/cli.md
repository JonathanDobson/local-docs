# Automate repeatable browser workflows with the Chrome DevTools CLI

Source: https://developer.chrome.com/docs/devtools/agents/cli

![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com) ![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social)

<br />

Chrome DevTools for agents includes a command-line interface (CLI) that lets
your coding agent, or you, run DevTools tools as standard shell commands.
Instead of calling tools dynamically through the MCP server, your agent writes
the same actions as shell commands and can chain them into a script that you can
rerun at any time. For example, your agent might generate a script like this:

```bash
chrome-devtools new_page "https://example.com"
chrome-devtools take_snapshot 1
chrome-devtools fill 1 "1_4" "hello"
```

Both the MCP server and the CLI connect to the same engine: a persistent
background daemon that talks to Chrome through the Chrome DevTools Protocol
(CDP). The difference is how your agent reaches that engine:

- **MCP server:** Your agent connects over standard input/output using JSON-RPC and treats every browser tool as an interactive function call.
- **CLI:** Your agent executes shell commands directly against the same background daemon.

You can use the CLI to do the following:

- **Persist a workflow:** Turn the actions your agent took during an exploratory debugging session into a reusable script.
- **Reproduce an application state:** Rerun a script to bring the browser back to a known state before debugging again.
- **Batch actions:** Run a sequence of navigation, input, emulation, and inspection commands without a conversation turn between each step.
- **Run scripts without an AI agent:** Execute the generated scripts from any terminal, subshell, or CI container that can execute shell scripts, without needing an active LLM session or MCP client.

## Choose between the CLI and the MCP server

Choosing between the CLI and the MCP server is an engineering decision about
cost, context, and workflow.

- **Context window cost:** When you register the MCP server, every tool definition and JSON schema is injected into your LLM's system prompt in every conversation. With the CLI skill, your agent only loads a compact Markdown summary and pays the token cost when it decides to read the full skill and construct the commands it needs. For long, multi-turn agent sessions, that difference adds up in both cost and latency.
- **Exploration versus execution:** MCP tools excel at dynamic, exploratory debugging, when neither you nor your agent know yet what you need to inspect. Because your agent knows about all available tools upfront, it is more likely to use them to reach its goal. When the path is already known, the CLI lets you run only the steps you need.
- **Reusability:** You can save a CLI script, reuse it in a skill, or run it manually outside of an agent loop. You can't do that with MCP tool calls.

| Use the MCP server when | Use the CLI when |
|---|---|
| You are investigating an unknown issue and need the full toolbox available. | You already know the steps and want to repeat them reliably. |
| You want live, dynamic problem-solving and deep browser introspection. | You want token-efficient agent skills or terminal-based automation. |
| Your agent runs in an IDE or client with MCP support. | Your environment doesn't support MCP clients. |

When using the CLI, keep the following in mind:

- **Tool coverage:** The CLI supports most of the Chrome DevTools for agents tools for shell-based automation. For the full list of commands, see the [CLI skill
  reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md).
- **Implicit startup:** The background server starts automatically on first use; you don't need to run `start`, `status`, or `stop` before each command.
- **Persistent state:** Browser state persists across commands, so a page you open in one command is still available in the next if not explicitly closed.
- **Page IDs and element UIDs:** Most commands take a page ID as their first argument. Run `chrome-devtools list_pages` to find it, and `chrome-devtools
  take_snapshot` to get the UIDs of elements you want to interact with.
- **Output format:** Output defaults to plain Markdown-like text. Pass `--output-format=json` if you want to consume the results in other scripts or CI pipelines.
- **File access:** By default the CLI has full file system access for file-saving parameters and `upload_file`. Pass `--allowUnrestrictedPaths=false` to restrict file access to the OS temp directory.
- **Lighthouse in CI:** You can run `lighthouse_audit` from the CLI, but the standalone [Lighthouse CLI](https://github.com/googlechrome/lighthouse) and its GitHub Actions are a more lightweight fit if you only need Lighthouse scores in CI.
- **Simpler abstraction than browser automation scripts:** Unlike writing full Puppeteer or Playwright scripts in JavaScript or TypeScript, the DevTools CLI provides a limited, highly targeted API surface. This shell syntax is easier for humans to read and maintain, and significantly easier for even low-tier models to generate reliably without hallucinations.

## Prerequisites

Before you use the CLI, ensure you have the following:

- **Chrome DevTools for agents installed:** Follow the [Get started
  guide](https://developer.chrome.com/docs/devtools/agents/get-started). Agent-specific plugins and extensions (for example, the Gemini CLI extension) include the agentic skills alongside the MCP server.
- **The CLI available in your shell:** Installation is a one-time step and isn't part of the regular agent workflow. See the [installation
  reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/references/installation.md).
- **The `chrome-devtools-cli` skill (installed with Chrome DevTools for
  agents):** This skill teaches your agent how to write shell scripts or run shell commands with the CLI.

## Command structure

Commands follow the pattern `chrome-devtools <tool> [arguments] [flags]`.
Required arguments are positional and optional arguments use flags. Use `--help`
on any command for details.

For example:

```bash
chrome-devtools new_page "https://example.com"      # Open a page
chrome-devtools list_pages                          # Find the page ID
chrome-devtools take_snapshot 1                     # Get element UIDs for page 1
chrome-devtools fill 1 "1_4" "hello"                # Fill an input
chrome-devtools click 1 "1_7" --includeSnapshot true
chrome-devtools list_console_messages 1 --types error
chrome-devtools take_screenshot 1 --filePath "result.png"
```

## Use cases for the Chrome DevTools CLI

Instruct your agent to capture the steps it already figured out as a script,
instead of re-solving the same browser flow in every session.

> [!NOTE]
> **Note:** Agent execution steps are examples of potential behavior. As there are many different types of agents and agents are non-deterministic, you may see different results.

### Persist a debugging session as a reusable script

After an exploratory debugging session over MCP, you often can't guarantee the
same issue won't appear again. Rather than re-explaining the reproduction steps
next time, ask your agent to write down the flow it just executed.

**Example prompt:**

    Please write a chrome-devtools CLI script for this user flow, and save it as test.sh.

**Example agent execution:** Your agent reviews the navigation, input, and
inspection steps it took during the session and translates them into a sequence
of `chrome-devtools` commands, for example `new_page`, `take_snapshot`, `fill`,
`click`, and `list_console_messages`. It saves the script as `test.sh`. The next
time you debug this area, you can point your agent to the script to reach the
same state again, or run it outside an agent loop to debug manually.

### Reproduce an application state before investigating

Complex states, such as a multi-step checkout or a filtered dashboard, are
expensive for an agent to rebuild conversationally every time. Use a saved
script as the starting point for a new investigation.

**Example prompt:**

    Run ./scripts/checkout-flow.sh to get the browser into the payment step, then check why the "Pay now" button stays disabled after I select Google Pay.

**Example agent execution:** Your agent runs the script, which navigates to the
checkout, fills the address form, and selects a shipping option. Because browser
state persists across commands, your agent then uses `take_snapshot` and
`evaluate_script` on the same page to inspect the button's state and the event
handlers attached to the payment selector.

### Batch visual checks across viewports

Verifying a layout change across several screen sizes is repetitive and usually
done by hand. Ask your agent for a script that applies emulation settings and
captures evidence for each one in a single run.

**Example prompt:**

    Write a chrome-devtools CLI script that opens http://localhost:3000/pricing, captures a full-page screenshot at 375x667, 768x1024, and 1920x1080, and saves them to ./screenshots with the viewport size in the filename.

**Example agent execution:** Your agent writes a loop that calls
`chrome-devtools emulate 1 --viewport "<size>"` followed by `chrome-devtools
take_screenshot 1 --fullPage true --filePath "./screenshots/pricing-<size>.png"`
for each viewport. You can rerun the script after every CSS change without
opening a conversation.

### Smoke-test a flow where no MCP client is available

Some environments, such as CI containers or locked-down enterprise setups, don't
support MCP clients. Virtually every terminal, subshell, CI container, and agent
framework supports running standard shell scripts and reading stdout, which
makes the CLI a fit for lightweight checks in those places.

**Example prompt:**

    Create a shell script that opens the sign-up page on the staging URL passed as the first argument, submits the form with test data, and exits with a non-zero code if any console errors are logged. Use --output-format=json so the script can parse the result.

**Example agent execution:** Your agent writes a script that uses `new_page`,
`take_snapshot`, `fill`, and `click`, then calls `list_console_messages 1
--types error --output-format=json` and parses the JSON output to decide the
exit code.

> [!NOTE]
> **Note:** For Lighthouse scores in CI specifically, prefer the standalone Lighthouse CLI or GitHub Actions.

### Package a workflow as a lightweight skill

If a flow is useful across projects or teammates, your agent can wrap the script
in a skill. That's the DevTools CLI skill: a lightweight reference that lets
your agent run specific browser commands without paying the upfront token cost
for all tools.

**Example prompt:**

    Turn ./scripts/checkout-flow.sh into a skill named "reproduce-checkout" with a short description of when to use it, so I can invoke it in future sessions.

**Example agent execution:** Your agent creates a `SKILL.md` with a name, a
one-line description of when the skill applies, and instructions that reference
the script. In later sessions, the agent reads the full skill only when the task
matches its description.

## Next steps

- For the complete list of CLI commands and flags, see the [CLI skill
  reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md).
- To configure the underlying server (headless mode, channels, experimental categories), see [Configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt).