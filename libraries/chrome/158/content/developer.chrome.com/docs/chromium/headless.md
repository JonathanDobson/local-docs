# Chrome Headless mode

Source: https://developer.chrome.com/docs/chromium/headless

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />

With Chrome Headless mode, you can run the browser in an unattended environment,
without any visible UI. Essentially, you can run Chrome without chrome.

Headless mode is a popular choice for browser automation, through projects like
[Puppeteer](https://developer.chrome.com/docs/puppeteer) or [ChromeDriver](https://chromedriver.chromium.org/).

> [!NOTE]
> **Note:** In Chrome 112, we updated Headless mode so that Chrome creates, but doesn't display, any platform windows. All other functions, existing and future, are available with no limitations.

## Use Headless mode

To use Headless mode, pass the `--headless` command-line flag:

    chrome --headless

### Use old Headless mode

Previously, Headless mode was
[a separate, alternate browser implementation](https://source.chromium.org/chromium/chromium/src/+/main:headless/;drc=c67febd82ae3e18ac8db1397f4ccfa87b0da2ffc)
that happened to be shipped as part of the same Chrome binary. It didn't share
any of the Chrome browser code in
[`//chrome`](https://source.chromium.org/chromium/chromium/src/+/main:chrome/).

Chrome now has unified Headless and headful modes.

![Headless mode shares code with Chrome.](https://developer.chrome.com/static/docs/chromium/headless/image/the-chrome-headless-is-7ec2038d11f0b.svg)

Since Chrome 132.0.6793.0 the old Headless mode is only available as [a
standalone binary named `chrome-headless-shell`](https://developer.chrome.com/blog/chrome-headless-shell) which can be downloaded [here](https://googlechromelabs.github.io/chrome-for-testing/).

### In Puppeteer

To use Headless mode in Puppeteer:

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

For more information on using Headless in Puppeteer, you can refer to the
resources located [here](https://pptr.dev/guides/headless-modes).

### In Selenium-WebDriver

To use Headless mode in Selenium-WebDriver:

    const driver = await env
      .builder()
      .setChromeOptions(options.addArguments('--headless'))
      .build();

    await driver.get('https://developer.chrome.com/');

    // ...

    await driver.quit();

See the [Selenium team's blog post](https://www.selenium.dev/blog/2023/headless-is-going-away/#what-are-the-two-headless-modes) for more information, including examples using other language bindings.

### Command-line flags

The following command-line flags are available in Headless mode and in Headless shell.

#### `--dump-dom`

The `--dump-dom` flag prints the serialized DOM of the target page to stdout.
For example:

    chrome --headless --dump-dom https://developer.chrome.com/

This is different from printing the HTML source code, which you might do with
`curl`. To bring you the output of `--dump-dom`, Chrome first parses the HTML
code into a DOM, executes any `<script>` that might alter the DOM, then
turns that DOM back into a serialized string of HTML.

#### `--screenshot`

The `--screenshot` flag takes a screenshot of the target page and saves it as
`screenshot.png` in the current working directory. This is especially useful in
combination with the `--window-size` flag.

For example:

    chrome --headless --screenshot --window-size=412,892 https://developer.chrome.com/

#### `--print-to-pdf`

The `--print-to-pdf` flag saves the target page as a PDF named `output.pdf` in
the current working directory. For example:

    chrome --headless --print-to-pdf https://developer.chrome.com/

Optionally, you can add the `--no-pdf-header-footer` flag to omit the print
header (with the current date and time) and footer (with the URL and the page
number).

    chrome --headless --print-to-pdf --no-pdf-header-footer https://developer.chrome.com/

Not: The functionality behind the `--no-pdf-header-footer` flag was previously
available with the `--print-to-pdf-no-header` flag. You may need to fall back to
the old flag name, if using a previous version.

#### `--timeout`

The `--timeout` flag defines the maximum wait time (in milliseconds) after which
the page's content is captured by `--dump-dom`, `--screenshot`, and
`--print-to-pdf` even if the page is still loading.

    chrome --headless --print-to-pdf --timeout=5000 https://developer.chrome.com/

The `--timeout=5000` flag tells Chrome to wait up to 5 seconds before printing
the PDF. Thus, this process takes at most 5 seconds to run.

#### `--virtual-time-budget`

The `--virtual-time-budget` acts as a "fast-forward" for any time-dependent code
(for example, `setTimeout`/`setInterval`). It forces the browser to execute any
of the page's code as fast as possible while making the page believe that the
time actually goes by.

To illustrate its use, consider this demo, which
[increments, logs, and displays a counter every second](https://mathiasbynens.be/demo/time)
using `setTimeout(fn, 1000)`. Here's the relevant code:

    <output>0</output>
    <script>
      const element = document.querySelector('output');
      let counter = 0;
      setInterval(() => {
        counter++;
        console.log(counter);
        element.textContent = counter;
      }, 1_000);
    </script>

After one second, the page contains "1"; after two seconds, "2", and so on.
Here's how you'd capture the page's state after 42 seconds and save it as a PDF:

    chrome --headless --print-to-pdf --virtual-time-budget=42000 https://mathiasbynens.be/demo/time

#### `--allow-chrome-scheme-url`

The `--allow-chrome-scheme-url` flag is required to access `chrome://` URLs.
This flag is available from Chrome 123. Here's an example:

    chrome --headless --print-to-pdf --allow-chrome-scheme-url chrome://gpu

## Debug

Because Chrome is effectively invisible in Headless mode, it might sound tricky
to solve an issue. It's possible to debug Headless Chrome in a way that's very
similar to headful Chrome.

Launch Chrome in Headless mode with the
`--remote-debugging-port` command-line flag.

    chrome --headless --remote-debugging-port=0 https://developer.chrome.com/

This prints a unique WebSocket URL to stdout, for example:

    DevTools listening on ws://127.0.0.1:60926/devtools/browser/b4bd6eaa-b7c8-4319-8212-225097472fd9

In a headful Chrome instance, we can then use
[Chrome DevTools remote debugging](https://developer.chrome.com/docs/devtools/remote-debugging) to connect
to the Headless target and inspect it.

1. Go to `chrome://inspect` and click the **Configure...** button.
2. Enter the IP address and port number from the WebSocket URL.
   - In the previous example, I entered `127.0.0.1:60926`.
3. Click **Done**. You should see a Remote Target appear with all its tabs and other targets listed.
4. Click **inspect** to access to Chrome DevTools and inspect the remote Headless target, including a live view of the page.

![Chrome DevTools can inspect a remote Headless target page](https://developer.chrome.com/static/docs/chromium/headless/image/chrome-devtools-inspect-b740931c3aeeb.png)

## Feedback

We look forward to hearing your feedback about Headless mode. If you
encounter any issues, [file a bug](https://goo.gle/headless-bug).