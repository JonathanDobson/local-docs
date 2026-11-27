# Command-line switches: `gpu/config/gpu_switches`

Generated from `gpu/config/gpu_switches.h` and `gpu/config/gpu_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

50 switches.

## `--gpu-recent-crash-count`

- Constant: `kGpuRecentCrashCount`

Passes the number of recent GPU crashes to the GPU process.

## `--disable-gpu-rasterization`

- Constant: `kDisableGpuRasterization`

Disable GPU rasterization, i.e. rasterize on the CPU only. Overrides the kEnableGpuRasterization flag.

## `--disable-mipmap-generation`

- Constant: `kDisableMipmapGeneration`

Disables mipmap generation in Skia. Used a workaround for select low memory devices, see https://crbug.com/1138979 for details.

## `--enable-gpu-rasterization`

- Constant: `kEnableGpuRasterization`

Allow heuristics to determine when a layer tile should be drawn with the Skia GPU backend. Only valid with GPU accelerated compositing.

## `--gpu-blocklist-test-group`

- Constant: `kGpuBlocklistTestGroup`

Select a different set of GPU blocklist entries with the specified test_group ID.

## `--gpu-driver-bug-list-test-group`

- Constant: `kGpuDriverBugListTestGroup`

Enable an extra set of GPU driver bug list entries with the specified test_group ID. Note the default test group (group 0) is still active.

## `--gpu-preferences`

- Constant: `kGpuPreferences`

Passes encoded GpuPreferences to GPU process.

## `--ignore-gpu-blocklist`

- Constant: `kIgnoreGpuBlocklist`

Ignores GPU blocklist.

## `--gpu-disk-cache-size-kb`

- Constant: `kGpuDiskCacheSizeKB`

Allows explicitly specifying the shader disk cache size for embedded devices. Default value is 6MB. On Android, 2MB is default and 128KB for low-end devices.

## `--disable-gpu-shader-disk-cache`

- Constant: `kDisableGpuShaderDiskCache`

Disables the GPU shader on disk cache.

## `--disable-gpu-process-for-dx12-info-collection`

- Constant: `kDisableGpuProcessForDX12InfoCollection`

Disables the non-sandboxed GPU process for DX12 info collection

## `--enable-webgl-draft-extensions`

- Constant: `kEnableWebGLDraftExtensions`

Enables WebGL draft extensions (not yet approved by the community). This has side-effects in the GPU process, so the flag is here so that code in both gpu/ and content/ can access it.

## `--enable-unsafe-webgpu`

- Constant: `kEnableUnsafeWebGPU`

_No description in the source._

## `--force-high-performance-gpu`

- Constant: `kForceHighPerformanceGPU`

_No description in the source._

## `--enable-webgpu-developer-features`

- Constant: `kEnableWebGPUDeveloperFeatures`

Enables WebGPU developer features which are not generally exposed to the web platform.

## `--enable-dawn-backend-validation`

- Constant: `kEnableDawnBackendValidation`

Enable validation layers in Dawn backends.

## `--use-webgpu-adapter`

- Constant: `kUseWebGPUAdapter`

The adapter to use for WebGPU content.

## `--use-webgpu-power-preference`

- Constant: `kUseWebGPUPowerPreference`

The adapter selecting strategy related to GPUPowerPreference.

## `--force-webgpu-compat`

- Constant: `kForceWebGPUCompat`

Force all WebGPU content to run in WebGPU Compatibility mode.

## `--enable-dawn-features`

- Constant: `kEnableDawnFeatures`

Set the Dawn features(toggles) enabled on the creation of Dawn devices.

## `--disable-dawn-features`

- Constant: `kDisableDawnFeatures`

Set the Dawn features(toggles) disabled on the creation of Dawn devices.

## `--collect-dawn-info-eagerly`

- Constant: `kCollectDawnInfoEagerly`

Start the GPU process for Dawn info collection immediately after the browser starts. The default is to delay for 120 seconds.

## `--no-delay-for-dx12-vulkan-info-collection`

- Constant: `kNoDelayForDX12VulkanInfoCollection`

Start the non-sandboxed GPU process for DX12 and Vulkan info collection immediately after the browser starts. The default is to delay for 120 seconds.

## `--enable-gpu-blocked-time`

- Constant: `kEnableGpuBlockedTime`

Enables measures of how long GPU Main Thread was blocked between SwapBuffers

## `--gpu-vendor-id`

- Constant: `kGpuVendorId`

Passes the active graphics vendor id from browser process to info collection GPU process.

## `--gpu-device-id`

- Constant: `kGpuDeviceId`

Passes the active graphics device id from browser process to info collection GPU process.

## `--gpu-sub-system-id`

- Constant: `kGpuSubSystemId`

Passes the active graphics sub system id from browser process to info collection GPU process.

## `--gpu-revision`

- Constant: `kGpuRevision`

Passes the active graphics revision info from browser process to info collection GPU process.

## `--gpu-driver-version`

- Constant: `kGpuDriverVersion`

Passes the active graphics driver version from browser process to info collection GPU process.

## `--enable-vulkan-protected-memory`

- Constant: `kEnableVulkanProtectedMemory`

Enables using protected memory for vulkan resources.

## `--disable-vulkan-fallback-to-gl-for-testing`

- Constant: `kDisableVulkanFallbackToGLForTesting`

Disables falling back to GL based hardware rendering if initializing Vulkan fails. This is to allow tests to catch regressions in Vulkan.

## `--vulkan-heap-memory-limit-mb`

- Constant: `kVulkanHeapMemoryLimitMb`

Specifies the heap limit for Vulkan memory. TODO(crbug.com/40161102): Remove this switch.

## `--vulkan-sync-cpu-memory-limit-mb`

- Constant: `kVulkanSyncCpuMemoryLimitMb`

Specifies the sync CPU limit for total Vulkan memory. TODO(crbug.com/40161102): Remove this switch.

## `--force-browser-crash-on-gpu-crash`

- Constant: `kForceBrowserCrashOnGpuCrash`

Crash Chrome if GPU process crashes. This is to force a test to fail when GPU process crashes unexpectedly.

## `--gpu-watchdog-timeout-seconds`

- Constant: `kGpuWatchdogTimeoutSeconds`

Override value for the GPU watchdog timeout in seconds.

## `--force-separate-egl-display-for-webgl-testing`

- Constant: `kForceSeparateEGLDisplayForWebGLTesting`

Force the use of a separate EGL display for WebGL contexts. Used for testing multi-GPU pathways on devices with only one valid GPU.

## `--skia-graphite-dawn-backend`

- Constant: `kSkiaGraphiteDawnBackend`

Specify which Dawn backend to use for Skia Graphite.

## `--d3d11`

- Constant: `kSkiaGraphiteDawnBackendD3D11`

_No description in the source._

## `--d3d12`

- Constant: `kSkiaGraphiteDawnBackendD3D12`

_No description in the source._

## `--metal`

- Constant: `kSkiaGraphiteDawnBackendMetal`

_No description in the source._

## `--opengles`

- Constant: `kSkiaGraphiteDawnBackendOpenGLES`

_No description in the source._

## `--swiftshader`

- Constant: `kSkiaGraphiteDawnBackendSwiftshader`

_No description in the source._

## `--vulkan`

- Constant: `kSkiaGraphiteDawnBackendVulkan`

_No description in the source._

## `--skia-graphite-vulkan-backend`

- Constant: `kSkiaGraphiteVulkanBackend`

Specify using Skia Graphite with native Vulkan backend.

## `--disable-skia-graphite`

- Constant: `kDisableSkiaGraphite`

Force disabling/enabling Skia Graphite. Disabling will take precedence over enabling if both are specified.

## `--enable-skia-graphite`

- Constant: `kEnableSkiaGraphite`

_No description in the source._

## `--disable-skia-graphite-precompilation`

- Constant: `kDisableSkiaGraphitePrecompilation`

Force disabling/enabling Skia Graphite's Pipeline Precompilation. Disabling will take precedence over enabling if both are specified.

## `--enable-skia-graphite-precompilation`

- Constant: `kEnableSkiaGraphitePrecompilation`

_No description in the source._

## `--enable-gpu-main-time-keeper-metrics`

- Constant: `kEnableGpuMainTimeKeeperMetrics`

Enables ThreadControllerWithMessagePumpImpl's TimeKeeper UMA metrics using CrGpuMain as suffix.

## `--suppress-performance-logs`

- Constant: `kSuppressPerformanceLogs`

Suppresses GL_DEBUG_TYPE_PERFORMANCE log messages for web tests that can get sent to the JS console and cause unnecessary test failures due test output log expectation comparisons.
