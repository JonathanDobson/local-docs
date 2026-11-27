# Command-line switches: `components/headless/command_handler/headless_command_switches`

Generated from `components/headless/command_handler/headless_command_switches.h` and `components/headless/command_handler/headless_command_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

9 switches.

## `--default-background-color`

- Constant: `kDefaultBackgroundColor`

The background color to be used if the page doesn't specify one. Provided as RGB or RGBA integer value in hex, e.g. 'ff0000ff' for red or '00000000' for transparent.

## `--dump-dom`

- Constant: `kDumpDom`

Print the serialized DOM (doctype + document.documentElement.outerHTML) to stdout.

## `--print-to-pdf`

- Constant: `kPrintToPDF`

Save a PDF file of the loaded page.

## `--no-pdf-header-footer`

- Constant: `kNoPDFHeaderFooter`

Do not display header and footer in the printed PDF file.

## `--disable-pdf-tagging`

- Constant: `kDisablePDFTagging`

Do not emit tags when printing PDFs.

## `--generate-pdf-document-outline`

- Constant: `kGeneratePDFDocumentOutline`

Embed the document outline into printed PDFs.

## `--screenshot`

- Constant: `kScreenshot`

Save a screenshot of the loaded page.

## `--timeout`

- Constant: `kTimeout`

Issues a stop after the specified number of milliseconds.  This cancels all navigation and causes the DOMContentLoaded event to fire.

## `--virtual-time-budget`

- Constant: `kVirtualTimeBudget`

If set the system waits the specified number of virtual milliseconds before deeming the page to be ready.  For determinism virtual time does not advance while there are pending network fetches (i.e no timers will fire). Once all network fetches have completed, timers fire and if the system runs out of virtual time is fastforwarded so the next timer fires immediately, until the specified virtual time budget is exhausted.
