# Chrome Headless command-line reference

Source: https://developer.chrome.com/docs/automation-and-testing/headless-cli

![Mathias Bynens](https://web.dev/images/authors/mathiasbynens.jpg) Mathias Bynens [X](https://twitter.com/mathias) [GitHub](https://github.com/mathiasbynens) [Homepage](https://mathiasbynens.be/) ![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />

The following command-line flags are available in Headless mode and in Headless shell.

## `--dump-dom`

The `--dump-dom` flag prints the serialized DOM of the target page to stdout.
For example:

```bash
chrome --headless --dump-dom https://developer.chrome.com/
```

This is different from printing the HTML source code, which you might do with
`curl`. To bring you the output of `--dump-dom`, Chrome first parses the HTML
code into a DOM, executes any `<script>` that might alter the DOM, then
turns that DOM back into a serialized string of HTML.

## `--screenshot`

The `--screenshot` flag takes a screenshot of the target page and saves it as
`screenshot.png` in the current working directory. This is especially useful in
combination with the `--window-size` flag.

For example:

```bash
chrome --headless --screenshot --window-size=412,892 https://developer.chrome.com/
```

## `--print-to-pdf`

The `--print-to-pdf` flag saves the target page as a PDF named `output.pdf` in
the current working directory. For example:

```bash
chrome --headless --print-to-pdf https://developer.chrome.com/
```

Optionally, you can add the `--no-pdf-header-footer` flag to omit the print
header (with the current date and time) and footer (with the URL and the page
number).

```bash
chrome --headless --print-to-pdf --no-pdf-header-footer https://developer.chrome.com/
```

> [!NOTE]
> **Note:** The functionality behind the `--no-pdf-header-footer` flag was previously available with the `--print-to-pdf-no-header` flag. You may need to fall back to the old flag name, if using a previous version.

## `--timeout`

The `--timeout` flag defines the maximum wait time (in milliseconds) after which
the page's content is captured by `--dump-dom`, `--screenshot`, and
`--print-to-pdf` even if the page is still loading.

```bash
chrome --headless --print-to-pdf --timeout=5000 https://developer.chrome.com/
```

The `--timeout=5000` flag tells Chrome to wait up to 5 seconds before printing
the PDF. Thus, this process takes at most 5 seconds to run.

## `--virtual-time-budget`

The `--virtual-time-budget` acts as a "fast-forward" for any time-dependent code
(for example, `setTimeout`/`setInterval`). It forces the browser to execute any
of the page's code as fast as possible while making the page believe that the
time actually goes by.

To illustrate its use, consider this demo, which
[increments, logs, and displays a counter every second](https://mathiasbynens.be/demo/time)
using `setTimeout(fn, 1000)`. Here's the relevant code:

```html
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
```

After one second, the page contains "1"; after two seconds, "2", and so on.
Here's how you'd capture the page's state after 42 seconds and save it as a PDF:

```bash
chrome --headless --print-to-pdf --virtual-time-budget=42000 https://mathiasbynens.be/demo/time
```

## `--allow-chrome-scheme-url`

The `--allow-chrome-scheme-url` flag is required to access `chrome://` URLs.
This flag is available from Chrome 123. Here's an example:

```bash
chrome --headless --print-to-pdf --allow-chrome-scheme-url chrome://gpu
```