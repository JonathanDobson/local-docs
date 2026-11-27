# Command-line switches: `ui/accessibility/accessibility_switches`

Generated from `ui/accessibility/accessibility_switches.h` and `ui/accessibility/accessibility_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

8 switches.

## `--enable-experimental-accessibility-autoclick`

- Constant: `kEnableExperimentalAccessibilityAutoclick`

Shows additional automatic click features that haven't launched yet.

## `--enable-mac-accessibility-api-migration`

- Constant: `kEnableMacAccessibilityAPIMigration`

Enables the switchover to the newer NSAccessibility property-based API.

## `--generate-accessibility-test-expectations`

- Constant: `kGenerateAccessibilityTestExpectations`

For development / testing only. When enabled the switch generates expectations files upon running an ax_inspect test. For example, when running content_browsertests, it saves output of failing accessibility tests to their expectations files in content/test/data/accessibility/, overwriting existing file content.

## `--disable-renderer-accessibility`

- Constant: `kDisableRendererAccessibility`

Turns off the accessibility in the renderer.

## `--force-renderer-accessibility`

- Constant: `kForceRendererAccessibility`

Force renderer accessibility to be on instead of enabling it on demand when a screen reader is detected. The disable-renderer-accessibility switch overrides this if present. This switch has an optional parameter that forces an AXMode bundle. The three available bundle settings are: 'basic', 'form-controls', and 'complete'. If the bundle argument is invalid, then the forced AXMode will default to 'complete'. If the bundle argument is missing, then the initial AXMode will default to complete but allow changes to the AXMode during execution.

## `--enable-experimental-accessibility-labels-debugging`

- Constant: `kEnableExperimentalAccessibilityLabelsDebugging`

Enables support for visually debugging the accessibility labels feature, which provides images descriptions for screen reader users.

## `--enable-experimental-accessibility-switch-access-text`

- Constant: `kEnableExperimentalAccessibilitySwitchAccessText`

Enables in progress Switch Access features for text input.

## `--enable-magnifier-debug-draw-rect`

- Constant: `kEnableMagnifierDebugDrawRect`

Enables debug feature for drawing rectangle around magnified region, without zooming in.
