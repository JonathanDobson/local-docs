# Command-line switches: `components/input/switches`

Generated from `components/input/switches.h` and `components/input/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--disable-hang-monitor`

- Constant: `kDisableHangMonitor`

Suppresses hang monitor dialogs in renderer processes.  This may allow slow unload handlers on a page to prevent the tab from closing, but the Task Manager can be used to terminate the offending process in this case.

## `--disable-pinch`

- Constant: `kDisablePinch`

Disables compositor-accelerated touch-screen pinch gestures.

## `--validate-input-event-stream`

- Constant: `kValidateInputEventStream`

In debug builds, asserts that the stream of input events is valid.
