# Debug Chrome extensions with AI agents

Source: https://developer.chrome.com/docs/devtools/agents/extensions

![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com) ![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social)

<br />

Chrome DevTools for agents enables your agent to start a browser session and
install or interact with Chrome extensions using an MCP server. This lets your
coding agent control the extension lifecycle: installing, reloading, and
triggering actions.

Instead of manually loading an unpacked extension, clicking the reload button in
the extensions management page every time you change the code, and manually
triggering the extension to test it, instruct your AI agent to manage the entire
process autonomously. This bridges the gap between static code generation and
live extension testing.

You can use the extensions tools to do the following:

- **Install extensions:** Install an unpacked Chrome extension from a local directory path.
- **List extensions:** Retrieve a list of all installed Chrome extensions, including their name, ID, version, and enabled status.
- **Reload extensions:** Reload an unpacked Chrome extension by its ID to instantly apply code changes.
- **Trigger actions:** Trigger the default action of an extension by its ID, such as opening a menu or executing a background script action (see, [chrome.action in the API
  documentation](https://developer.chrome.com/docs/extensions/reference/api/action)).
  - **Uninstall extensions:** Remove a Chrome extension from the browser session by its ID.

## Prerequisites

Before you use the extension tools, ensure you have the following:

- **Experimental flag:** The Extensions category is not active by default in DevTools for Agents. You must [configure the MCP
  server](https://developer.chrome.com/docs/devtools/agents/get-started/configuration) with the `--categoryExtensions` flag.
- **Unpacked extensions:** Tools like `install_extension` require an absolute path to the unpacked extension folder, making them ideal for local development.
- **File access to the extension folder:** The server can only read files
  within its workspace roots. These are the roots that your MCP client
  provides, such as your project directory. If your client doesn't provide
  roots, the server can only access the OS temporary directory. On macOS, this
  directory isn't `/tmp`. If the extension folder is outside these roots,
  `install_extension` fails with an `Access denied` error. To allow another
  folder, add the `--filesystemRoot` flag (alias `--workspace`) to your server
  arguments:

  ```json
  "args": ["chrome-devtools-mcp@latest", "--categoryExtensions", "--filesystemRoot=/path/to/extensions"]
  ```

  For more details, see [Allow file access outside the temporary
  directory](https://developer.chrome.com/docs/devtools/agents/get-started/configuration#filesystem-root).

## Use cases for Chrome extensions tools

Instruct your agent to manage your extension lifecycle while developing and
fixing bugs.
> **Note:** Agent execution steps are examples of potential behavior. Your agent
> might act differently.

### Rapidly iterate and reload an extension

Manually reloading an extension after every file change slows down development.
Instruct your agent to apply a code fix and immediately reload the extension to
verify the new behavior without manual intervention.

**Example prompt:**

You can use a general approach:

    Verify the extension has access to the active tab.

Or you can be more detailed:

    Update the manifest.json to include the "activeTab" permission. Then, reload the extension with ID 'abc123xyz' and trigger its default action to ensure it works.

**Example agent execution:** Your agent edits the `manifest.json` file on your
file system. It then invokes the `reload_extension` tool using the provided ID.
Finally, it calls the `trigger_extension_action` tool to activate the extension
and verify that no permission errors are thrown in the console.

### Test an extension's default action on a target page

You often need to test how a content script or extension action interacts with a
specific website. Automate this process by instructing your agent to navigate to
the site, install the extension, and trigger it.

**Example prompt:**

You can use a general approach:

    Test my extension on example.com and verify it works correctly.

Or you can be more detailed:

    Navigate to example.com, install the unpacked extension located at '/Users/dev/my-extension', and trigger the extension action. Check the console logs to verify the content script executed correctly.

**Example agent execution:** Your agent navigates to the target URL using
`navigate_page`. It then uses `install_extension` with the provided absolute
path. After the extension is loaded, it executes `trigger_extension_action` to
simulate a user click. Finally, it uses `list_console_messages` to confirm the
content script ran and produced the expected output.

### Verify installed extensions and clean up

During automated testing, you might need to verify if an extension is correctly
loaded with the right version, or remove it to ensure a clean state for the next
test.

**Example prompt:**

    Uninstall 'My Test Extension' from the browser.

**Example agent execution:** Your agent uses the `list_extensions` tool to
retrieve the list of installed extensions and their metadata. It parses the
output to identify the ID associated with "My Test Extension". It then uses the
`uninstall_extension` tool with that ID to safely remove it from the browser.

### Create a new extension and test it

Starting a new Chrome extension from scratch usually requires creating
boilerplate files and manually loading the unpacked directory into the browser
to test it. Skip this manual setup by instructing your agent to generate the
initial code, load the extension, and verify its basic functionality,
end-to-end, in a single step.

**Example prompt:**

    Build a Chrome extension that turns the page background gray when I click its icon. Save the files to a 'gray-bg-ext' folder in my project, navigate to example.com, load the extension, and verify that it works.

**Example agent execution:** Your agent creates a basic Manifest V3
`manifest.json` and a background service worker that listens for the
`chrome.action.onClicked` event. It then navigates to the test page, invokes
`install_extension`, and uses `trigger_extension_action` to simulate a user
click. Finally, it inspects the DOM or takes a screenshot to confirm the
background turned gray, proving the boilerplate is functional.