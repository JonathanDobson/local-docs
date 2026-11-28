# Command-line switches: `chrome/browser/headless/headless_mode_switches`

Generated from `chrome/browser/headless/headless_mode_switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

2 switches.

## `--allow-chrome-scheme-url`

- Constant: `kAllowChromeSchemeUrl`

Allows headless mode to access any URL whose scheme is chrome://.

## `--enable-gpu`

- Constant: `kEnableGPU`

Enable hardware GPU support. Headless uses swiftshader by default for consistency across headless environments. This flag just turns forcing of swiftshader off and lets us revert to regular driver selection logic. Alternatively, specific drivers may be forced with --use-gl or --use-angle. Nethier approach guarantees that hardware GPU support will be enabled, as this is still conditional on headless having access to X display etc.
