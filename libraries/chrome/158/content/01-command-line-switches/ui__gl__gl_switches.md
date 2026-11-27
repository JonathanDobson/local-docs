# Command-line switches: `ui/gl/gl_switches`

Generated from `ui/gl/gl_switches.h` and `ui/gl/gl_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

58 switches.

## `--egl`

- Constant: `kGLImplementationEGLName`

The GL implementation names that can be passed to --use-gl.

## `--angle`

- Constant: `kGLImplementationANGLEName`

_No description in the source._

## `--mock`

- Constant: `kGLImplementationMockName`

_No description in the source._

## `--stub`

- Constant: `kGLImplementationStubName`

_No description in the source._

## `--disabled`

- Constant: `kGLImplementationDisabledName`

_No description in the source._

## `--default`

- Constant: `kANGLEImplementationDefaultName`

_No description in the source._

## `--d3d11`

- Constant: `kANGLEImplementationD3D11Name`

_No description in the source._

## `--d3d11on12`

- Constant: `kANGLEImplementationD3D11on12Name`

_No description in the source._

## `--d3d11-warp`

- Constant: `kANGLEImplementationD3D11WarpName`

_No description in the source._

## `--d3d11-warp-webgl`

- Constant: `kANGLEImplementationD3D11WarpForWebGLName`

_No description in the source._

## `--gl`

- Constant: `kANGLEImplementationOpenGLName`

_No description in the source._

## `--gl-egl`

- Constant: `kANGLEImplementationOpenGLEGLName`

_No description in the source._

## `--gles`

- Constant: `kANGLEImplementationOpenGLESName`

_No description in the source._

## `--gles-egl`

- Constant: `kANGLEImplementationOpenGLESEGLName`

_No description in the source._

## `--null`

- Constant: `kANGLEImplementationNullName`

_No description in the source._

## `--vulkan`

- Constant: `kANGLEImplementationVulkanName`

_No description in the source._

## `--swiftshader`

- Constant: `kANGLEImplementationSwiftShaderName`

_No description in the source._

## `--swiftshader-webgl`

- Constant: `kANGLEImplementationSwiftShaderForWebGLName`

_No description in the source._

## `--metal`

- Constant: `kANGLEImplementationMetalName`

_No description in the source._

## `--`

- Constant: `kANGLEImplementationNoneName`

_No description in the source._

## `--d3d11-null`

- Constant: `kANGLEImplementationD3D11NULLName`

Special switches for "NULL"/stub driver implementations.

## `--gl-null`

- Constant: `kANGLEImplementationOpenGLNULLName`

_No description in the source._

## `--gles-null`

- Constant: `kANGLEImplementationOpenGLESNULLName`

_No description in the source._

## `--vulkan-null`

- Constant: `kANGLEImplementationVulkanNULLName`

_No description in the source._

## `--metal-null`

- Constant: `kANGLEImplementationMetalNULLName`

_No description in the source._

## `--validating`

- Constant: `kCmdDecoderValidatingName`

The command decoder names that can be passed to --use-cmd-decoder.

## `--passthrough`

- Constant: `kCmdDecoderPassthroughName`

_No description in the source._

## `--nv12`

- Constant: `kSwapChainFormatNV12`

Swap chain formats for direct composition SDR video overlays.

## `--yuy2`

- Constant: `kSwapChainFormatYUY2`

_No description in the source._

## `--bgra`

- Constant: `kSwapChainFormatBGRA`

_No description in the source._

## `--p010`

- Constant: `kSwapChainFormatP010`

_No description in the source._

## `--disable-gpu-driver-bug-workarounds`

- Constant: `kDisableGpuDriverBugWorkarounds`

Disable workarounds for various GPU driver bugs.

## `--disable-gpu-vsync`

- Constant: `kDisableGpuVsync`

Stop the GPU from synchronizing presentation with vblank.

## `--enable-gpu-service-logging`

- Constant: `kEnableGPUServiceLogging`

Turns on GPU logging (debug build only).

## `--enable-gpu-service-tracing`

- Constant: `kEnableGPUServiceTracing`

Turns on calling TRACE for every GL call.

## `--gpu-no-context-lost`

- Constant: `kGpuNoContextLost`

Inform Chrome that a GPU context will not be lost in power saving mode, screen saving mode, etc.  Note that this flag does not ensure that a GPU context will never be lost in any situations, say, a GPU reset.

## `--use-angle`

- Constant: `kUseANGLE`

Select which ANGLE backend to use. Options are: default: Attempts several ANGLE renderers until one successfully initializes, varying ES support by platform. d3d9: Legacy D3D9 renderer, ES2 only. d3d11: D3D11 renderer, ES2 and ES3. warp: D3D11 renderer using software rasterization, ES2 and ES3. gl: Desktop GL renderer, ES2 and ES3. gles: GLES renderer, ES2 and ES3.

## `--use-dynamic-angle`

- Constant: `kUseDynamicAngle`
- Condition: `BUILDFLAG(USE_STATIC_ANGLE)`

Use ANGLE shared libraries even if ANGLE is built as a static library.

## `--use-cmd-decoder`

- Constant: `kUseCmdDecoder`

Use the Pass-through command decoder, skipping all validation and state tracking. Switch lives in ui/gl because it affects the GL binding initialization on platforms that would otherwise not default to using EGL bindings.

## `--enable-angle-features`

- Constant: `kEnableANGLEFeatures`

ANGLE features are defined per-backend in third_party/angle/include/platform Enables specified comma separated ANGLE features if found.

## `--disable-angle-features`

- Constant: `kDisableANGLEFeatures`

Disables specified comma separated ANGLE features if found.

## `--use-gl`

- Constant: `kUseGL`

Select which implementation of GL the GPU process should use. Options are: desktop: whatever desktop OpenGL the user has installed (Linux and Mac default). egl: whatever EGL / GLES2 the user has installed (Windows default - actually ANGLE). swiftshader: The SwiftShader software renderer.

## `--test-gl-lib`

- Constant: `kTestGLLib`

Flag used for Linux tests: for desktop GL bindings, try to load this GL library first, but fall back to regular library if loading fails.

## `--use-gpu-in-tests`

- Constant: `kUseGpuInTests`

Use hardware gpu, if available, for tests.

## `--enable-sgi-video-sync`

- Constant: `kEnableSgiVideoSync`

Enable use of the SGI_video_sync extension, which can have driver/sandbox/window manager compatibility issues.

## `--disable-gl-extensions`

- Constant: `kDisableGLExtensions`

Disables specified comma separated GL Extensions if found.

## `--disable-direct-composition`

- Constant: `kDisableDirectComposition`

Disable DirectComposition.

## `--enable-direct-composition-video-overlays`

- Constant: `kEnableDirectCompositionVideoOverlays`

Enable DirectComposition video overlays even if hardware doesn't support it.

## `--use-adapter-luid`

- Constant: `kUseAdapterLuid`

Initialize the GPU process using the adapter with the specified LUID. This is only used on Windows, as LUID is a Windows specific structure.

## `--enable-unsafe-swiftshader`

- Constant: `kEnableUnsafeSwiftShader`

Allow usage of SwiftShader for WebGL

## `--disable-d3d11-warp`

- Constant: `kDisableD3D11Warp`

Explicitly disable D3D11 WARP fallback. Some test suites prefer falling back to swiftshader.

## `--direct-composition-video-swap-chain-format`

- Constant: `kDirectCompositionVideoSwapChainFormat`

Used for overriding the swap chain format for direct composition SDR video overlays.

## `--tint-dc-layer`

- Constant: `kTintDcLayer`

Tint `SwapChainPresenter` with the following colors:  - Decode swap chain: blue - VP blit: magenta - VP blit w/ staging texture: orange - MF proxy surface: green  This is similar to `HKLM\Software\Microsoft\Windows\DWM` `OverlayTestMode=1` in DWM, but to help understand `SwapChainPresenter` state.

## `--webview-draw-functor-uses-vulkan`

- Constant: `kWebViewDrawFunctorUsesVulkan`

Indicate that the this is being used by Android WebView and its draw functor is using vulkan.

## `--disable-gl-drawing-for-tests`

- Constant: `kDisableGLDrawingForTests`

These flags are used by the test harness code, not passed in by users. Disables GL drawing operations which produce pixel output. With this the GL output will not be correct but tests will run faster.

## `--override-use-software-gl-for-tests`

- Constant: `kOverrideUseSoftwareGLForTests`

Forces the use of software GL instead of hardware gpu for tests.

## `--disable-android-native-fence-sync-for-testing`

- Constant: `kDisableAndroidNativeFenceSyncForTesting`
- Condition: `BUILDFLAG(IS_ANDROID)`

On some Android emulators with software GL, ANGLE is exposing the native fence sync extension but it doesn't actually work. This switch is used to disable the Android native fence sync during test to avoid crashes.  TODO(https://crbug.com/337886037): Remove this flag once the upstream ANGLE is fixed.

## `--fake-vsync-rate`

- Constant: `kFakeVsyncRate`
- Condition: `BUILDFLAG(IS_WIN)`

Report a fake vsync rate (in Hz) instead of the real display refresh rate, skipping the wait on the real hardware vsync signal. E.g. --fake-vsync-rate=240 paces BeginFrames as if the display were 240Hz, regardless of what it actually supports, while still feeding the same BeginFrame path a real vsync signal would. Implemented for Windows only; other platforms will get equivalent support in the future.
