# Command-line switches: `ui/base/ui_base_switches`

Generated from `ui/base/ui_base_switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

25 switches.

## `--disable-pull-to-refresh-effect`

- Constant: `kDisablePullToRefreshEffect`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disable the pull-to-refresh effect when vertically overscrolling content.

## `--enable-edge-to-edge-debug-layers`

- Constant: `kEnableEdgeToEdgeDebugLayers`
- Condition: `BUILDFLAG(IS_ANDROID)`

Enables drawing debug layers for edge-to-edge components to highlight the system insets those components are drawing into. LINT.IfChange(EnableEdgeToEdgeDebugLayers)

## `--disable-modal-animations`

- Constant: `kDisableModalAnimations`
- Condition: `BUILDFLAG(IS_MAC)`

Disable animations for showing and hiding modal dialogs.

## `--show-mac-overlay-borders`

- Constant: `kShowMacOverlayBorders`
- Condition: `BUILDFLAG(IS_MAC)`

Show borders around CALayers corresponding to overlays and partial damage.

## `--system-font-family`

- Constant: `kSystemFontFamily`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Specifies system font family name. Improves determinism when rendering pages in headless mode.

## `--ui-toolkit`

- Constant: `kUiToolkitFlag`
- Condition: `BUILDFLAG(IS_LINUX)`

Specify the toolkit used to construct the Linux GUI.

## `--gtk-version`

- Constant: `kGtkVersionFlag`
- Condition: `BUILDFLAG(IS_LINUX)`

Specify the GTK version to be loaded.

## `--qt-version`

- Constant: `kQtVersionFlag`
- Condition: `BUILDFLAG(IS_LINUX)`

Specify the QT version to be loaded.

## `--disable-gtk-ime`

- Constant: `kDisableGtkIme`
- Condition: `BUILDFLAG(IS_LINUX)`

Disables GTK IME integration.

## `--drm-virtual-connector-is-external`

- Constant: `kDRMVirtualConnectorIsExternal`

Treats DRM virtual connector as external to enable display mode change in VM.

## `--force-caption-style`

- Constant: `kForceCaptionStyle`

Forces the caption style for WebVTT captions.

## `--force-dark-mode`

- Constant: `kForceDarkMode`

Forces dark mode in UI for platforms that support it.

## `--force-high-contrast`

- Constant: `kForceHighContrast`

Forces high-contrast mode for native UI and web content, regardless of system settings.

## `--lang`

- Constant: `kLang`

The language file that we want to try to open. Of the form language[-country] where language is the 2 letter code from ISO-639. On Linux, this flag does not work; use the LC_*/LANG environment variables instead.

## `--show-overdraw-feedback`

- Constant: `kShowOverdrawFeedback`

Visualize overdraw by color-coding elements based on if they have other elements drawn underneath. This is good for showing where the UI might be doing more rendering work than necessary. The colors are hinting at the amount of overdraw on your screen for each pixel, as follows:  True color: No overdraw. Blue: Overdrawn once. Green: Overdrawn twice. Pink: Overdrawn three times. Red: Overdrawn four or more times.

## `--slow-down-compositing-scale-factor`

- Constant: `kSlowDownCompositingScaleFactor`

Re-draw everything multiple times to simulate a much slower machine. Give a slow down factor to cause renderer to take that many times longer to complete, such as --slow-down-compositing-scale-factor=2.

## `--tint-composited-content`

- Constant: `kTintCompositedContent`

Tint composited color.

## `--top-chrome-touch-ui`

- Constant: `kTopChromeTouchUi`

Controls touch-optimized UI layout for top chrome.

## `--auto`

- Constant: `kTopChromeTouchUiAuto`

_No description in the source._

## `--disabled`

- Constant: `kTopChromeTouchUiDisabled`

_No description in the source._

## `--enabled`

- Constant: `kTopChromeTouchUiEnabled`

_No description in the source._

## `--ui-disable-partial-swap`

- Constant: `kUIDisablePartialSwap`

Disable partial swap which is needed for some OpenGL drivers / emulators.

## `--use-system-clipboard`

- Constant: `kUseSystemClipboard`

Enables the ozone x11 clipboard for linux-chromeos.

## `--disallow-non-exact-resource-reuse`

- Constant: `kDisallowNonExactResourceReuse`

Test related. Disable re-use of non-exact resources to fulfill ResourcePool requests. Intended only for use in layout or pixel tests to reduce noise.

## `--mangle-localized-strings`

- Constant: `kMangleLocalizedStrings`

Transform localized strings to be longer, with beginning and end markers to make truncation visually apparent.
