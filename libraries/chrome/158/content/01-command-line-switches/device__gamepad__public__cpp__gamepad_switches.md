# Command-line switches: `device/gamepad/public/cpp/gamepad_switches`

Generated from `device/gamepad/public/cpp/gamepad_switches.h` and `device/gamepad/public/cpp/gamepad_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--gamepad-polling-interval`

- Constant: `kGamepadPollingInterval`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Overrides the gamepad polling interval. Decreasing the interval improves input latency of buttons and axes but may negatively affect performance due to more CPU time spent in the input polling thread.
