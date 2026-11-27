# Command-line switches: `ui/views/views_switches`

Generated from `ui/views/views_switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--disable-input-event-activation-protection`

- Constant: `kDisableInputEventActivationProtectionForTesting`

Disables the disregarding of potentially unintended input events such as button clicks that happen instantly after the button is shown. Use this for integration tests that do automated clicks etc.

## `--draw-view-bounds-rects`

- Constant: `kDrawViewBoundsRects`

Draws a semitransparent red rect to indicate the bounds of each view. Also, draws a blue semitransparent rect when GetContentBounds() differs from GetLocalBounds().

## `--view-stack-traces`

- Constant: `kViewStackTraces`

Captures stack traces on View construction to provide better debug info.
