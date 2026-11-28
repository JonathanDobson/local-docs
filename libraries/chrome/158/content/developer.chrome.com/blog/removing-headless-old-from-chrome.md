# Removing --headless=old from Chrome

Source: https://developer.chrome.com/blog/removing-headless-old-from-chrome

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />


Published: October 23, 2024

<br />

In early 2023, we announced the availability of [Chrome's new Headless mode (`--headless=new`)](https://developer.chrome.com/docs/chromium/headless)
in Chrome 112. Later that year, [we made the old Headless mode available as a standalone `chrome-headless-shell` binary](https://developer.chrome.com/blog/chrome-headless-shell).

Both announcements also noted our plans to eventually remove the old Headless
mode from the Chrome binary. We're happy to announce that the old Headless mode
will be removed in Chrome 132.

From Chrome 132:

- Running Chrome with `--headless=old` now prints a helpful error message instead of launching the old Headless mode.
- Running Chrome with `--headless` or `--headless=new` runs the new Headless mode.

If you are using old Headless functionality you should now migrate to
`chrome-headless-shell` (to retain old Headless functionality) or to the new
Headless mode, which continues to be provided by the Chrome binary.

We look forward to hearing your feedback about Headless mode. If you encounter
any issues, [file a bug](https://goo.gle/headless-bug).