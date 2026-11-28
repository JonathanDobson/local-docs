# Command-line switches: `components/sync/base/command_line_switches`

Generated from `components/sync/base/command_line_switches.h` and `components/sync/base/command_line_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

7 switches.

## `--disable-sync`

- Constant: `kDisableSync`

Disables syncing browser data to a Google Account.

## `--sync-deferred-startup-timeout-seconds`

- Constant: `kSyncDeferredStartupTimeoutSeconds`

Allows overriding the deferred init fallback timeout.

## `--sync-include-specifics`

- Constant: `kSyncIncludeSpecificsInProtocolLog`

Controls whether the initial state of the "Capture Specifics" flag on chrome://sync-internals is enabled.

## `--sync-protocol-log-buffer-size`

- Constant: `kSyncProtocolLogBufferSize`

Controls the number of ProtocolEvents that are buffered, and thus can be displayed on newly-opened chrome://sync-internals tabs.

## `--sync-url`

- Constant: `kSyncServiceURL`

Overrides the default server used for profile sync.

## `--sync-short-initial-retry-override`

- Constant: `kSyncShortInitialRetryOverride`

This flag causes sync to retry very quickly (see polling_constants.h) the when it encounters an error, as the first step towards exponential backoff.

## `--sync-short-nudge-delay-for-test`

- Constant: `kSyncShortNudgeDelayForTest`

This flag significantly shortens the delay between nudge cycles. Its primary purpose is to speed up integration tests. The normal delay allows coalescing and prevention of server overload, so don't use this unless you're really sure that it's what you want.
