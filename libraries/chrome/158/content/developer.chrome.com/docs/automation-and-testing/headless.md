# Chrome Headless mode

Source: https://developer.chrome.com/docs/automation-and-testing/headless

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />

With Chrome Headless mode, you can run the browser in an unattended environment,
without any visible UI. Essentially, you can run Chrome without chrome.

> [!NOTE]
> **Note:** In Chrome 112, the Headless mode was updated so that Chrome creates, but doesn't display, any platform windows. All other functions, existing and future, are available with no limitations.

## Use Headless mode

To use Headless mode, pass the `--headless` command-line flag to a Chrome binary, for example:

### Linux

```bash
google-chrome --headless
```

### macOS

```bash
open -a "Google Chrome" --args --headless
```

### Windows

```bash
start chrome --headless
```

### Use old Headless mode

Previously, Headless mode was
[a separate, alternate browser implementation](https://source.chromium.org/chromium/chromium/src/+/main:headless/;drc=c67febd82ae3e18ac8db1397f4ccfa87b0da2ffc)
that happened to be shipped as part of the same Chrome binary. It didn't share
any of the Chrome browser code in
[`//chrome`](https://source.chromium.org/chromium/chromium/src/+/main:chrome/).

Chrome now has unified Headless and headful modes.

![Headless mode shares code with Chrome.](https://developer.chrome.com/static/docs/automation-and-testing/headless/image/the-chrome-headless-is-7ec2038d11f0b.svg)

Since Chrome 132.0.6793.0 the old Headless mode is only available as [a
standalone binary named `chrome-headless-shell`](https://developer.chrome.com/blog/chrome-headless-shell) which can be downloaded from [Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/).

### In Puppeteer

To use Headless mode in Puppeteer:

```javascript
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({
  headless: true,  // (default) enables Chrome Headless mode
  // `headless: 'shell'` enables Headless Shell (old headless)
  // `headless: false` enables "headful" mode
});

const page = await browser.newPage();
await page.goto('https://developer.chrome.com/');

// ...

await browser.close();
```

For more information on using Headless in Puppeteer, check out [Headless mode](https://pptr.dev/guides/headless-modes).

### In Selenium-WebDriver

To use Headless mode in Selenium-WebDriver:

```javascript
const driver = await env
  .builder()
  .setChromeOptions(options.addArguments('--headless'))
  .build();

await driver.get('https://developer.chrome.com/');

// ...

await driver.quit();
```

See the [Selenium team's blog post](https://www.selenium.dev/blog/2023/headless-is-going-away/#what-are-the-two-headless-modes) for more information, including examples using other language bindings.

## Feedback

We look forward to hearing your feedback about Headless mode. If you
encounter any issues, [file a bug](https://goo.gle/headless-bug).