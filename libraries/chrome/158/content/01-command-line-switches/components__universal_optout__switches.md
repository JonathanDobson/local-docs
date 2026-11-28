# Command-line switches: `components/universal_optout/switches`

Generated from `components/universal_optout/switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--universal-optout-history-json-path`

- Constant: `kUniversalOptOutHistoryJsonPath`

Specifies a path to a JSON file containing custom eligibility history to override `prefs::kUniversalOptOutEligibilityHistory` for testing. The JSON file must contain a dictionary with the following format: { "universal_optout.eligibility_history": { "YYYY-MM-DD": true, "YYYY-MM-DD": false, ... } }
