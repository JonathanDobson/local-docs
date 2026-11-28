# Download old Headless Chrome as chrome-headless-shell

Source: https://developer.chrome.com/blog/chrome-headless-shell

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/)

<br />

Earlier this year, we announced the availability of [Chrome's new Headless mode (`--headless=new`)](https://developer.chrome.com/articles/new-headless) in Chrome 112. This mode enables developers to run Chrome in an unattended environment without any visible UI---useful for testing and automation use cases.

As part of this announcement, we mentioned our plans to remove the old Headless mode from the Chrome binary. This removal makes sense, as the old Headless is technically a separate browser, meaning we're currently shipping two browser binaries in one. At the same time, we acknowledge that there are distinct use cases for the old and the new Headless modes:

1. The old Headless mode is a lightweight wrapper around Chromium's `//content` module, and it therefore has substantially fewer dependencies. Specifically, it does not require X11/Wayland, D-Bus, and is in some ways more performant than the fully-fledged Chrome browser. This makes it suitable for use cases such as automated screenshotting or web scraping.
2. New Headless on the other hand is the real Chrome browser, and is thus more authentic, reliable, and offers more features. This makes it more suitable for high-accuracy end-to-end web app testing or browser extension testing.

In other words, there's a trade-off between performance and authenticity. Which Headless mode is most fitting for you? It depends on your use case.

![A diagram illustrating the information given in the preceding list.](https://developer.chrome.com/static/blog/chrome-headless-shell/image/chrome-headless-shell.svg)

Developers and testers who don't require full Chrome functionality for their automation use cases may want to use old Headless. Otherwise, new Headless is likely the best choice.

To ensure developers and testers continue to have the choice between these two options, we're happy to announce the old Headless implementation is now available as a standalone `chrome-headless-shell` binary. These new `chrome-headless-shell` binaries are generated for every user-facing Chrome release, and are available for download [via Chrome for Testing infrastructure](https://developer.chrome.com/blog/chrome-for-testing) starting with Chrome 120.

## How can I get `chrome-headless-shell` binaries?

As with other Chrome for Testing binaries, the easiest way to download `chrome-headless-shell` for your platform is by using [our `@puppeteer/browsers` command-line utility](https://pptr.dev/browsers-api), available using `npm`. Here are some examples:

    # Download the latest available `chrome-headless-shell` binary corresponding to the Stable channel.
    npx @puppeteer/browsers install chrome-headless-shell@stable

    # Download a specific `chrome-headless-shell` version.
    npx @puppeteer/browsers install chrome-headless-shell@120.0.6098.0

If you prefer to build your own automated scripts for downloading `chrome-headless-shell` binaries, we've got you covered. Chrome for Testing offers [JSON API endpoints](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints) with the latest available versions per Chrome release channel (Stable, Beta, Dev, and Canary). To get a quick overview of the latest status, consult [the Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/).

## Feedback

We look forward to hearing your feedback about `chrome-headless-shell`. If you run into any issues, please [report them](https://goo.gle/headless-bug).