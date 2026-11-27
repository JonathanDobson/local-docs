# Command-line switches: `content/shell/common/shell_switches`

Generated from `content/shell/common/shell_switches.h` and `content/shell/common/shell_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

9 switches.

## `--user-data-dir`

- Constant: `kContentShellUserDataDir`

Makes Content Shell use the given path for its data directory.  NOTE: "user-data-dir" is used to align with Chromedriver's behavior. Please do NOT change this to another value.  NOTE: The same value is also used at Java-side in ContentShellBrowserTestActivity.java#getUserDataDirectoryCommandLineSwitch().

## `--crash-dumps-dir`

- Constant: `kCrashDumpsDir`

The directory Crashpad should store minidumps in.  iOS and tvOS default to app's cache directory.

## `--disable-system-font-check`

- Constant: `kDisableSystemFontCheck`

Disables the check for the system font when specified.

## `--content-shell-host-window-size`

- Constant: `kContentShellHostWindowSize`

Size for the content_shell's host window (i.e. "800x600").

## `--content-shell-hide-toolbar`

- Constant: `kContentShellHideToolbar`

Hides toolbar from content_shell's host window.

## `--isolated-context-origins`

- Constant: `kIsolatedContextOrigins`

Enables APIs guarded with the [IsolatedContext] IDL attribute for the given comma-separated list of origins.

## `--remote-debugging-address`

- Constant: `kRemoteDebuggingAddress`

Use the given address instead of the default loopback for accepting remote debugging connections. Note that the remote debugging protocol does not perform any authentication, so exposing it too widely can be a security risk.

## `--run-web-tests`

- Constant: `kRunWebTests`

Runs Content Shell in web test mode, injecting test-only behaviour for blink web tests.

## `--test-register-standard-scheme`

- Constant: `kTestRegisterStandardScheme`

Register the provided scheme as a standard scheme.
