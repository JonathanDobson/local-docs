# Expose custom application states to AI agents with third-party tools

Source: https://developer.chrome.com/docs/devtools/agents/use-cases/third-party-tools

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

> [!WARNING]
> **Experimental:** This feature is experimental and requires the `--categoryExperimentalThirdParty=true` flag. See [Configuration](https://developer.chrome.com/docs/devtools/agents/get-started/configuration.md.txt) for details on how to set flags.

Third-party developer tools enable coding agents to see beyond the DOM, network
requests, and console logs. By exposing custom tools directly from your website
or framework, you allow your agent to interact with otherwise inaccessible
application state and data.

These tools are created through JavaScript and are automatically discovered by
Chrome DevTools for agents when your page loads.

## Understand third-party developer tools

In the context of coding agents, tools are ready-made functions for agents to
perform specific actions. For DevTools for agents specifically, such tools can
expose its internal runtime state directly to coding agents, bridging the gap
between rendered output and internal logic.

When using third-party tools, keep the following in mind:

- **Runtime discovery.** Tools are automatically detected when your application responds to the `devtoolstooldiscovery` event emitted by Chrome DevTools for agents on the global `window` object.
- **Context scope.** Tools execute only within the context of the page that defines them. They don't persist across origins and page reloads.
- **Tool specificity** . Tools are only an *additional* way for your agent to perform a task. It might prefer built-in tools, or bare model capabilities to fulfill a prompt. So make tool names and descriptions as descriptive as possible.

## Prerequisites

Before you implement third-party tools, ensure you meet the following
requirements:

- **Chrome DevTools for agents.** Use version 0.25.0 or later.

  > [!NOTE]
  > **Note:** Version requirements may vary based on specific features.

- **Enabled JavaScript.** Have JavaScript enabled and executing.

## Implement a tool

To implement a tool, you listen for a specific discovery event and respond with
your tool definitions. The following code represents a response that includes
tool definitions:

```javascript
window.addEventListener(
  'devtoolstooldiscovery',
  (event: DevtoolsToolDiscoveryEvent) => {
    event.respondWith({
      name: 'Page-specific DevTools',
      description: 'Provide runtime info directly from the JavaScript in the page.',
      tools: [
        {
          name: 'add',
          description: 'Calculates the sum of two numbers.',
          inputSchema: {
            type: 'object',
            properties: {
              a: {type: 'number'},
              b: {type: 'number'},
            },
            required: ['a', 'b'],
          },
          execute: async (input: {a: number; b: number}) => {
            return input.a + input.b;
          },
        },
      ],
    });
  },
);
```

To register tools in your application:

1. **Define your tool group.** Create a `ToolGroup` that contains a name, a
   description, and an array of individual tool definitions.

   ```javascript
   export interface ToolDefinition {
     name: string;
     description: string;
     inputSchema: JSONSchema7;
     execute: (args: Record<string, unknown>) => unknown;
   }
   export interface ToolGroup {
     name: string;
     description: string;
     tools: ToolDefinition[];
   }
   ```
2. **Listen for the discovery event.** Chrome DevTools for agents dispatches a
   custom `devtoolstooldiscovery` event on the global `window` object after
   each navigation and whenever it needs an updated list of available tools.

3. **Register your tools.** Call the event's `respondWith()` method to provide
   your tool group to the agent.

### Essential components for individual tools

Every tool definition you implement must include the following three parts:

- **Name and description.** These provide the instructions the agent uses to decide when and how to call your tool.
- **Input schema.** A JSON Schema that defines the structure and types of arguments the tool expects.
- **Execution function.** The actual JavaScript code that runs on the page when the agent invokes the tool.

The following example shows these three components in a single tool definition:

```javascript
{
  name: 'add',
  description: 'Calculates the sum of two numbers.',
  inputSchema: {
    type: 'object',
    properties: {
      a: {type: 'number'},
      b: {type: 'number'},
    },
    required: ['a', 'b'],
  },
  execute: async (input) => {
    return input.a + input.b;
  },
}
```

## Use cases for third-party developer tools

Instruct your agent to inspect deep application logic rather than just
surface-level UI elements. Use these custom tools to streamline debugging of
stateful or framework-heavy applications.

> [!NOTE]
> **Note:** Agent execution steps are examples of potential behavior. Your agent may act differently.

### Tips for tool discovery

Write *descriptive tool names and descriptions*. Agents use these descriptions
as context to decide which tool to use, clear language helps the agent
autonomously determine when a tool is appropriate for a task.

### Debug application-specific runtime metrics

Issues like silent cache misses or redundant API calls are often invisible to
standard inspection. By exposing internal statistics, your agent can explain why
a certain behavior occurred.

Suppose you have a function that exposes internal statistics; first, you have
to create a tool like this one:

```javascript
window.addEventListener('devtoolstooldiscovery', (event) => {
  event.respondWith({
    name: 'My app',
    description: 'Tools to debug my app',
    tools: [
      {
        name: 'getCacheStatistics',
        description: 'Exposes runtime cache hits and misses for the frontend API service.',
        inputSchema: {},
        execute: async () => {
          // Assuming window.__apiCacheService exists in your app
          return window.__apiCacheService.getStats();
        }
      }
    ]
  });
});
```

If your tool description is clear, your agent might use the tool autonomously
when it sees fit. You can prompt your agent to perform a task using the tool
like the following:

```text
When I reassign a lead to a new sales rep, the dashboard takes a second to
update. Please verify if the frontend is correctly updating the local cache,
or if it is doing a full cache miss and refetching the entire pipeline from the
database.
```

**Example agent execution:** Your agent detects the `getCacheStatistics` tool
exposed by your application. It invokes the tool, analyzes the returned hit to
miss ratio, and identifies that the frontend is unnecessarily refetching the
entire pipeline instead of updating the local cache.

### Checking feature flags

Define custom data points to expose the current environment variables or feature
flags active for a specific user session. This helps you debug why certain
features are or aren't visible to specific users. If a user reports a bug, the
agent can verify if they are in an experiment group that might be causing the
issue.

For example, create a tool like this one to return the internal feature flag
state:

```javascript
// Implementation for a website creator to expose feature flags
window.addEventListener('devtoolstooldiscovery', (event) => {
  event.respondWith({
    name: 'Application Configuration Tools',
    description: 'Tools for inspecting runtime environment and feature toggles',
    tools: [
      {
        name: 'getFeatureFlags',
        description: 'Returns a list of all active feature flags and their current values for the session.',
        inputSchema: {
          type: 'object',
          properties: {} // No input parameters required for this tool
        },
        execute: async () => {
          // This should return your internal feature flag state
          // Example: return window.AppConfig.getFlags();
          return {
            "new-ui-enabled": true,
            "beta-search-v2": false,
            "experiment-group": 'control',
            "log-level": 'debug'
          };
        }
      }
    ]
  });
});
```

If your tool description is clear, your agent might use the tool autonomously
when it sees fit. You can prompt your agent to perform a task using the tool
like the following:

```text
Check the active feature flags and tell me if the new-ui-enabled flag is set to
true for this session.
```

**Example agent execution** : Your agent invokes the `getFeatureFlags` tool,
confirms that the `new-ui-enabled` flag is active, and proceeds to debug the
components associated with the new interface.

### Inspect global application state

Expose your application's runtime state tree to help your agent understand
internal logic without fetching the entire DOM.

You could create a tool like this one to query specific paths in your state
tree, like the following:

```javascript
// Library-agnostic implementation for inspecting global application state
window.addEventListener('devtoolstooldiscovery', (event) => {
  event.respondWith({
    name: "Global State Inspector",
    description: 'Tools to inspect the runtime state tree of the application',
    tools: [
      {
        name: 'getGlobalState',
        description: "Returns the current application state. Use the 'path' parameter to drill down into specific sections (for example, 'auth.user' or 'cart.items'). ",
        inputSchema: {
          type: 'object',
          properties: {
            path: {
              type: 'string',
              description: 'Optional dot-notation path to a specific property in the state tree.'
            }
          }
        },
        execute: async (input) => {
          // Library-agnostic access:
          // Website creators can point this to whatever global store they use.
          const state = window.__APP_STATE__ ||
                        (window.store && typeof window.store.getState === 'function' ? window.store.getState() : null);

          if (!state) {
            return { error: 'Application state is not accessible via window.__APP_STATE__ or window.store.' };
          }

          if (!input.path) {
            return state;
          }

          // Helper to resolve a dot-notated path against the state object
          return input.path.split('.').reduce((acc, part) => {
            return acc && acc[part] !== undefined ? acc[part] : undefined;
          }, state);
        }
      }
    ]
  });
});
```

If your tool description is clear, your agent might use the tool autonomously
when it sees fit. You can prompt your agent to perform a task using the tool
like the following:

```text
The number of items in my cart is not updating. Inspect the global state at the
path cart.items and list the current items and their quantities, see if they are
the same.
```

**Example agent execution** : Your agent calls `getGlobalState` with the `path`
parameter. It retrieves the list of items from the cart and identifies a
discrepancy between the internal state and the items rendered on the page.

Some important notes regarding this tool example:

- **Decoupled logic** : The AI agent asks for "state". You, as the developer, decide how to map that request to your actual data structure in the `execute` function.
- **Targeted Debugging** : By including the `path` parameter, the agent can avoid pulling the entire state tree (which might be huge) and focus only on the relevant portion, saving tokens and improving performance.
- **Standardized interface** : Even if you switch state management libraries, as long as you update this one `execute` function, your AI debugging agent won't need any new instructions or tools.

### Inspect database Content

Verify that your backend data matches the UI state by querying database records
directly through a read-only debug endpoint.

Expose a safe debug endpoint and create a tool like this one to verify backend
records:

```javascript
// Framework-agnostic implementation for inspecting database content
window.addEventListener('devtoolstooldiscovery', (event) => {
  event.respondWith({
    name: 'Database Inspection Tools',
    description: 'Tools to query backend database records using existing browser session',
    tools: [
      {
        name: 'queryDatabaseTable',
        description: 'Retrieves a limited set of records from a specific table. Useful for verifying that backend data matches the UI state.',
        inputSchema: {
          type: 'object',
          properties: {
            tableName: {
              type: 'string',
              description: 'The name of the database table to inspect.'
            },
            limit: {
              type: 'number',
              default: 5,
              description: 'Maximum number of rows to return.'
            }
          },
          required: ['tableName']
        },
        execute: async (input) => {
          // This calls a generic debug endpoint you've set up on your server.
          // It's framework-agnostic because it just expects a JSON response.
          try {
            const response = await fetch(`/api/debug/db-inspect?table=${input.tableName}&limit=${input.limit}`);
            if (!response.ok) {
              return { error: `Backend returned ${response.status}: ${response.statusText}` };
            }
            return await response.json();
          } catch (error) {
            return { error: `Failed to connect to debug endpoint: ${error.message}` };
          }
        }
      }
    ]
  });
});
```

If your tool description is clear, your agent might use the tool autonomously
when it sees fit. You can prompt your agent to perform a task using the tool
like the following:

```text
The total price on the checkout page seems wrong. Query the orders table for my
last order to verify the subtotal and tax values and see what may be causing the
problem, if any.
```

**Example agent execution** : Your agent calls `queryDatabaseTable` for the
orders table. It retrieves the JSON record, identifies an error in the backend's
tax calculation, and suggests a fix for the server logic.

Some important notes regarding this tool example:

- **Security and authentication** : You don't need to pass database credentials to the AI agent. The `fetch` call uses the browser's current login session to authorize the request on your backend.
- **Actionable debugging** : If an AI agent identifies a UI bug, it can immediately call `queryDatabaseTable` to see if the error exists in the source data or the frontend calculation.
- **Minimal setup**: You only need to expose one "safe" (read-only) debug endpoint on your server that accepts a table name and returns JSON. The framework you use to build that endpoint doesn't matter.