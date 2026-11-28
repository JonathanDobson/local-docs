# Command-line switches: `ui/gfx/switches`

Generated from `ui/gfx/switches.h` and `ui/gfx/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

9 switches.

## `--animation-duration-scale`

- Constant: `kAnimationDurationScale`

Scale factor to apply to every animation duration. Must be >= 0.0. This will only apply to LinearAnimation and its subclasses.

## `--disable-font-subpixel-positioning`

- Constant: `kDisableFontSubpixelPositioning`

Force disables font subpixel positioning. This affects the character glyph sharpness, kerning, hinting and layout.

## `--enable-native-gpu-memory-buffers`

- Constant: `kEnableNativeGpuMemoryBuffers`

Enable native CPU-mappable GPU memory buffer support on Linux.

## `--force-prefers-reduced-motion`

- Constant: `kForcePrefersReducedMotion`

Forces whether the user desires reduced motion, regardless of system settings.

## `--force-prefers-no-reduced-motion`

- Constant: `kForcePrefersNoReducedMotion`

Forces whether the user desires no reduced motion, regardless of system settings.

## `--headless`

- Constant: `kHeadless`

Run in headless mode, i.e., without a UI or display server dependencies.

## `--screen-info`

- Constant: `kScreenInfo`

Headless screen info in the format: {0,0 800x600}{800,0 600x800}. See //components/headless/screen_info/README.md for more details.

## `--display`

- Constant: `kX11Display`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Which X11 display to connect to. Emulates the GTK+ "--display=" command line argument. In use only with Ozone/X11.

## `--no-xshm`

- Constant: `kNoXshm`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Disables MIT-SHM extension. In use only with Ozone/X11.
