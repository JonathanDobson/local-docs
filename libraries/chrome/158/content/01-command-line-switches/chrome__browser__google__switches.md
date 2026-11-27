# Command-line switches: `chrome/browser/google/switches`

Generated from `chrome/browser/google/switches.h` and `chrome/browser/google/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

2 switches.

## `--simulate-update-hresult`

- Constant: `kSimulateUpdateHresult`

Simulates a specific HRESULT error code returned by the update check. If the switch value is not specified (as hex) then it defaults to E_FAIL.

## `--simulate-update-error-code`

- Constant: `kSimulateUpdateErrorCode`

Simulates a GoogleUpdateErrorCode error by the update check. Must be supplied with |kSimulateUpdateHresult| switch.
