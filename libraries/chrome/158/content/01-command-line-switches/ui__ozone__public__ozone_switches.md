# Command-line switches: `ui/ozone/public/ozone_switches`

Generated from `ui/ozone/public/ozone_switches.h` and `ui/ozone/public/ozone_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

9 switches.

## `--ozone-platform`

- Constant: `kOzonePlatform`

Specify ozone platform implementation to use.

## `--ozone-dump-file`

- Constant: `kOzoneDumpFile`

Specify location for image dumps.

## `--enable-wayland-ime`

- Constant: `kEnableWaylandIme`

Try to enable wayland input method editor.

## `--disable-wayland-ime`

- Constant: `kDisableWaylandIme`

Disable wayland input method editor.

## `--wayland-text-input-version`

- Constant: `kWaylandTextInputVersion`

Specify wayland text-input protocol version. Defaults to "1" for text-input-v1. Can specify value "3" for experimental text-input-v3 support.

## `--use-wayland-explicit-grab`

- Constant: `kUseWaylandExplicitGrab`

Use explicit grab when opening popup windows. See https://crbug.com/1220274

## `--disable-explicit-dma-fences`

- Constant: `kDisableExplicitDmaFences`

Disable explicit DMA-fences

## `--ozone-override-screen-size`

- Constant: `kOzoneOverrideScreenSize`

Specifies ozone screen size.

## `--render-node-override`

- Constant: `kRenderNodeOverride`

Allows explicitly picking a DRM render node to create gbm_device for rendering.
