# Debug in Headless mode

Source: https://developer.chrome.com/docs/automation-and-testing/debug-headless

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />

Because Chrome is effectively invisible in Headless mode, it might sound tricky
to solve an issue. It's possible to debug Headless Chrome in a way that's very
similar to headful Chrome.

Launch Chrome in Headless mode with the
`--remote-debugging-port` command-line flag.

```bash
chrome --headless --remote-debugging-port=0 https://developer.chrome.com/
```

This prints a unique WebSocket URL to `stdout`, for example:

    DevTools listening on ws://127.0.0.1:60926/devtools/browser/b4bd6eaa-b7c8-4319-8212-225097472fd9

In a headful Chrome instance, we can then use
[Chrome DevTools remote debugging](https://developer.chrome.com/docs/devtools/remote-debugging.md.txt) to connect
to the Headless target and inspect it.

1. Go to `chrome://inspect` and click the **Configure...** button.
2. Enter the IP address and port number from the WebSocket URL, for example, `127.0.0.1:60926`.
3. Click **Done**. You should see a Remote Target appear with all its tabs and other targets listed.
4. Click **inspect** to access to Chrome DevTools and inspect the remote Headless target, including a live view of the page.

![Chrome DevTools can inspect a remote Headless target page.](https://developer.chrome.com/static/docs/automation-and-testing/debug-headless/image/chrome-devtools-inspect-b740931c3aeeb.png)