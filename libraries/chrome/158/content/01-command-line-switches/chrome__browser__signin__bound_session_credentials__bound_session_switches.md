# Command-line switches: `chrome/browser/signin/bound_session_credentials/bound_session_switches`

Generated from `chrome/browser/signin/bound_session_credentials/bound_session_switches.h` and `chrome/browser/signin/bound_session_credentials/bound_session_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

2 switches.

## `--bound-session-cookie-rotation-delay`

- Constant: `kCookieRotationDelay`

Used to add artificial delay to the cookie rotation request. It expects as value a number representing the delay in milliseconds.

## `--bound-session-cookie-rotation-result`

- Constant: `kCookieRotationResult`

Used to simulate the cookie rotation network request response. It expects as a value a number representing the enum value of `BoundSessionRefreshCookieFetcher::Result`. Note: This should be used to simulate error cases not success. If success `0` is used, bound cookies won't be set.
