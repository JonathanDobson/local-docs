# Analyze memory leaks with AI agents

Source: https://developer.chrome.com/docs/devtools/agents/memory

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

Chrome DevTools for agents lets your coding agent analyze and fix client-side
memory leaks (including JavaScript and WebAssembly) in your application. By
automating the collection and analysis of heap snapshots, your agent can
pinpoint objects that are not being properly garbage collected and suggest
targeted code refactoring.

In an agentic workflow, your coding agent takes multiple snapshots across
different application states and uses specialized analysis tools.

## Enable memory debugging tools

By default, Chrome DevTools for agents only exposes the `take_heapsnapshot`
tool. The tools that analyze heap snapshots (for example,
`compare_heapsnapshots`, `get_heapsnapshot_summary`, and
`get_heapsnapshot_retaining_paths`) are only available when you start the
server with the `--memoryDebugging` flag. Without this flag, your agent can
capture snapshots but can't analyze them.

To enable the memory debugging tools, add `--memoryDebugging` to your server
arguments:

```json
"args": ["chrome-devtools-mcp@latest", "--memoryDebugging"]
```

For more options, see
[Configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt).

## Common memory leak patterns

Memory analysis focuses on finding common leak patterns, including:

- **Uncleared event listeners:** Event listeners attached to global objects (like `window` or `document`) that prevent garbage collection.
- **Detached DOM nodes:** Nodes removed from the document tree but still referenced by a JavaScript variable.
- **Unintentional global variables:** Variables declared without proper scoping that remain in memory forever.
- **Closures:** Closures that unintentionally keep references to large objects in their own scope.
- **Unbounded data structures:** Data structures used for caching that grow without limits.

## Considerations for memory analysis

When using memory analysis, keep the following in mind:

- **Do not read raw snapshots directly:** Do not let your agent read raw
  `.heapsnapshot` files directly. They are too large and exceed context
  limits. The memory leak debugging skill explicitly instructs agents to avoid
  reading these files.

  > [!NOTE]
  > **Note:** For more details on how agents are instructed to handle memory, review the [memory leak debugging
  > skill](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/memory-leak-debugging/SKILL.md) definition in the GitHub repository.

- **The three-snapshot methodology:** To find leaks reliably, your agent
  generally needs to capture three snapshots: a baseline before the action, a
  target after the action, and a final snapshot after reverting the action.
  Note that some actions, such as those triggered by timers (`setTimeout`) or
  animations (`requestAnimationFrame`), occur without user interaction and
  might not require a reversal step.

  Note that some actions, such as those triggered by timers (`setTimeout`) or
  animations (`requestAnimationFrame`), occur without user interaction and
  might still increase memory usage.
- **Verify before fixing:** Always review the agent's findings to ensure its
  proposed actions are applicable and correct for your application's logic.
  For example, confirm whether a detached node is part of an intentional cache
  before instructing the agent to nullify the references.

## Use cases for memory leak analysis

Instruct your agent to profile memory during repetitive actions, including
timers and user interactions, instead of manually taking snapshots and diffing
them by hand. Integrate memory analysis into your debugging process with these
workflows.
> **Note:** Agent execution steps are examples of potential behavior. Your agent
> may act differently.

### Detect uncleared event listeners during navigation

Single-page applications (SPAs) often leak memory when developers forget to
remove global event listeners after a component unmounts. You can task your
agent to verify that memory is correctly freed when navigating between views.

**Example prompt:**

    Navigate from the home page to the dashboard and back to the home page. Use the take_heapsnapshot tool to check if we have any uncleared event listeners causing memory leaks.

**Example agent execution:** Your agent takes a baseline heap snapshot on the
home page, navigates to the dashboard, and navigates back to the home page to
take a final snapshot. It then uses internal analysis tools to evaluate
snapshots, detects that a `scroll` listener attached to the `window` object was
never cleared, and provides the specific code to call `removeEventListener` in
your component's cleanup function.

### Identify detached DOM nodes in UI components

Modals, dropdowns, and complex UI components frequently leave behind detached
DOM nodes if references to them are kept in JavaScript variables after they are
removed from the DOM.

**Example prompt:**

    Open the user settings modal and close it 5 times. Analyze the heap snapshots and tell me if there are any detached DOM nodes left behind. If there are, ask me if they are intentional before writing a fix.

**Example agent execution:** Your agent interacts with the settings modal while
collecting the required baseline, target, and final snapshots. The analysis
reveals several growing objects labeled as Detached HTMLDivElement. The agent
informs you of the finding and asks for your confirmation before changing the
code to set the variables holding the DOM references to `null`.

### Find unbounded caches in continuous interactions

Features like infinite scrolling or continuous data fetching can leak memory if
the underlying arrays or maps grow indefinitely without a cap.

**Example prompt:**

    Scroll down the infinite feed list to load more items three times. Check if our LRU cache is unbounded and leaking memory, and suggest a fix.

**Example agent execution:** Your agent analyzes the memory state before and
after scrolling. It identifies a closure that unintentionally captures a large
array that grows without limits. The agent suggests implementing caching limits
or using a WeakMap for data associated with the object life cycles to allow
proper garbage collection.

### Debug memory leaks in background processes

Animation and background timers can leak memory without explicit user
interaction. You can instruct your agent to monitor memory growth over time to
find memory leaks for these processes.

**Example prompt:**

    Explore this canvas application and monitor memory usage. Help me determine areas of improvement around reusing objects and textures.

**Example agent execution:** Your agent explores the canvas application and
automatically takes periodic snapshots to monitor memory usage over time. It
analyzes the heap and identifies that the rendering loop pushes new WebGL meshes
to an array on every frame without garbage collecting the previous ones,
suggesting optimizations for object reuse.