# Command-line switches: `components/component_updater/component_updater_switches`

Generated from `components/component_updater/component_updater_switches.h` and `components/component_updater/component_updater_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

5 switches.

## `--component-updater`

- Constant: `kComponentUpdater`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Comma-separated options to troubleshoot the component updater. Only valid for the browser process.

## `--component-updater-trust-tokens-component-path`

- Constant: `kComponentUpdaterTrustTokensComponentPath`

Optional testing override of the Trust Tokens key commitment component's path.

## `--campaigns-test-tag`

- Constant: `kCampaignsTestTag`

Switch to control which serving campaigns file versions to select in test cohort. Example: `--campaigns-test-tag=dev1` will select test cohort which tag matches dev1.

## `--demo-app-test-tag`

- Constant: `kDemoModeTestTag`

Switch to control which serving demo mode app versions to select in test cohort. Example: `--demo-app-test-tag=dev1` will select test cohort which tag matches dev1.

## `--enable-component-uninstall`

- Constant: `kEnableComponentUninstall`

Allows uninstalling components from the chrome://components page.
