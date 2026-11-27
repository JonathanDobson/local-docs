# Command-line switches: `components/one_time_tokens/core/common/one_time_token_switches`

Generated from `components/one_time_tokens/core/common/one_time_token_switches.h` and `components/one_time_tokens/core/common/one_time_token_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--one-time-token-service-base-url`

- Constant: `kOneTimeTokenServiceBaseUrl`

_No description in the source._

## `--https://onetimetoken.pa.googleapis.com`

- Constant: `kDefaultOneTimeTokenServiceBaseUrl`

_No description in the source._

## `--mock-otp-value`

- Constant: `kMockOtpValue`

Returns the specified mock OTP string value when retrieving OTP tokens. Note: In Actor OTP flows (AttemptOtpFillingTool), if actor::switches::kAttemptOtpFillingToolMockValueSkipsChecks is also present, it takes precedence and additionally bypasses consent and confirmation checks.
