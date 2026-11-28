# Command-line switches: `ui/display/display_switches`

Generated from `ui/display/display_switches.h` and `ui/display/display_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

11 switches.

## `--ash-enable-software-mirroring`

- Constant: `kEnableSoftwareMirroring`

Keep sorted. Enables software based mirroring.

## `--ensure-forced-color-profile`

- Constant: `kEnsureForcedColorProfile`

Crash the browser at startup if the display's color profile does not match the forced color profile. This is necessary on Mac because Chrome's pixel output is always subject to the color conversion performed by the operating system. On all other platforms, this is a no-op.

## `--force-device-scale-factor`

- Constant: `kForceDeviceScaleFactor`

Overrides the device scale factor for the browser UI and the contents.

## `--force-color-profile`

- Constant: `kForceDisplayColorProfile`

Force all monitors to be treated as though they have the specified color profile. Accepted values are "srgb" and "generic-rgb" (currently used by Mac layout tests) and "color-spin-gamma24" (used by layout tests).

## `--force-raster-color-profile`

- Constant: `kForceRasterColorProfile`

Force rastering to take place in the specified color profile. Accepted values are the same as for the kForceDisplayColorProfile case above.

## `--ash-host-window-bounds`

- Constant: `kHostWindowBounds`

TODO(kylechar): This overlaps with --screen-config. Unify flags and remove. Sets a window size, optional position, optional scale factor and optional panel radii. "1024x768" creates a window of size 1024x768. "100+200-1024x768" positions the window at 100,200. "1024x768*2" sets the scale factor to 2 for a high DPI display. "1024x768~15|15|12|12" sets the radii of the panel corners as (upper_left=15px,upper_right=15px, lower_right=12px, upper_left=12px) "800,0+800-800x800" for two displays at 800x800 resolution. "800,0+800-800x800,0+1600-800x800" for three displays at 800x800 resolution.

## `--screen-config`

- Constant: `kScreenConfig`

Specifies the initial screen configuration, or state of all displays, for FakeDisplayDelegate, see class for format details.

## `--secondary-display-layout`

- Constant: `kSecondaryDisplayLayout`

Specifies the layout mode and offsets for the secondary display for testing. The format is "<t|r|b|l>,<offset>" where t=TOP, r=RIGHT, b=BOTTOM and L=LEFT. For example, 'r,-100' means the secondary display is positioned on the right with -100 offset. (above than primary)

## `--use-first-display-as-internal`

- Constant: `kUseFirstDisplayAsInternal`

Uses the 1st display in --ash-host-window-bounds as internal display. This is for debugging on linux desktop.

## `--display-properties`

- Constant: `kDisplayProperties`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Additional display properties are provided through this switch that are beyond what is available via EDID encoded as JSON. Please see `https://chromium.googlesource.com/chromiumos/platform2/+/dd10a5ae3618bb9dc5fb47ac415ebef6e9a3827d/chromeos-config/README.md#displays` for the data format.

## `--ash-enable-unified-desktop`

- Constant: `kEnableUnifiedDesktop`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Enables unified desktop mode.
