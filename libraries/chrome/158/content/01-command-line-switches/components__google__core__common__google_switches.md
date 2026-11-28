# Command-line switches: `components/google/core/common/google_switches`

Generated from `components/google/core/common/google_switches.h` and `components/google/core/common/google_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--google-base-suggestion-url`

- Constant: `kGoogleBaseSuggestionURL`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Specifies an alternate suggestion URL to use for speaking to Google. Useful for testing.

## `--google-base-url`

- Constant: `kGoogleBaseURL`

Specifies an alternate URL to use for speaking to Google. Useful for testing.

## `--ignore-google-port-numbers`

- Constant: `kIgnoreGooglePortNumbers`

When set, this will ignore the PortPermission passed in the google_util.h methods and ignore the port numbers. This makes it easier to run tests for features that use these methods (directly or indirectly) with the EmbeddedTestServer, which is more representative of production.
