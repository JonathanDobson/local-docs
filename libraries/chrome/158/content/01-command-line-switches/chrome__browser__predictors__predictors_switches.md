# Command-line switches: `chrome/browser/predictors/predictors_switches`

Generated from `chrome/browser/predictors/predictors_switches.h` and `chrome/browser/predictors/predictors_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--loading-predictor-allow-local-request-for-testing`

- Constant: `kLoadingPredictorAllowLocalRequestForTesting`

Allows the loading predictor to do prefetches to local IP addresses. This is needed for testing as such requests are blocked by default for security.
