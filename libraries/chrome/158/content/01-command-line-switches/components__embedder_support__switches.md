# Command-line switches: `components/embedder_support/switches`

Generated from `components/embedder_support/switches.h` and `components/embedder_support/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

8 switches.

## `--disable-popup-blocking`

- Constant: `kDisablePopupBlocking`

Disables pop-up blocking.

## `--headless`

- Constant: `kHeadless`

Enable headless mode.

## `--origin-trial-disabled-features`

- Constant: `kOriginTrialDisabledFeatures`

Contains a list of feature names for which origin trial experiments should be disabled. Names should be separated by "|" characters.

## `--origin-trial-disabled-tokens`

- Constant: `kOriginTrialDisabledTokens`

Contains a list of token signatures for which origin trial experiments should be disabled. Tokens should be separated by "|" characters.

## `--origin-trial-public-key`

- Constant: `kOriginTrialPublicKey`

Comma-separated list of keys which will override the default public keys for checking origin trial tokens.

## `--short-reporting-delay`

- Constant: `kShortReportingDelay`

Sets the Reporting API delay to under a second to allow much quicker reports.

## `--use-mobile-user-agent`

- Constant: `kUseMobileUserAgent`

Set when Chromium should use a mobile user agent.

## `--user-agent`

- Constant: `kUserAgent`

A string used to override the default user agent with a custom one.
