# Command-line switches: `gpu/command_buffer/service/gpu_switches`

Generated from `gpu/command_buffer/service/gpu_switches.h` and `gpu/command_buffer/service/gpu_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

19 switches.

## `--disable-gl-error-limit`

- Constant: `kDisableGLErrorLimit`

Disable the GL error log limit.

## `--disable-glsl-translator`

- Constant: `kDisableGLSLTranslator`

Disable the GLSL translator.

## `--disable-shader-name-hashing`

- Constant: `kDisableShaderNameHashing`

Turn off user-defined name hashing in shaders.

## `--enable-gpu-command-logging`

- Constant: `kEnableGPUCommandLogging`

Turn on Logging GPU commands.

## `--enable-gpu-debugging`

- Constant: `kEnableGPUDebugging`

Turn on Calling GL Error after every command.

## `--enforce-gl-minimums`

- Constant: `kEnforceGLMinimums`

Enforce GL minimums.

## `--force-max-texture-size`

- Constant: `kForceMaxTextureSize`

Sets the maximum texture size in pixels.

## `--gpu-program-cache-size-kb`

- Constant: `kGpuProgramCacheSizeKb`

Sets the maximum size of the in-memory gpu program cache, in kb

## `--gl-shader-interm-output`

- Constant: `kGLShaderIntermOutput`

Include ANGLE's intermediate representation (AST) output in shader compilation info logs.

## `--use-vulkan`

- Constant: `kUseVulkan`

Enable Vulkan support and select Vulkan implementation, must also have ENABLE_VULKAN defined. This only initializes Vulkan, the flag --enable-features=Vulkan must also be used to select Vulkan for compositing and rasterization.

## `--disable-vulkan-surface`

- Constant: `kDisableVulkanSurface`

Disables VK_KHR_surface extension. Instead of using swapchain, bitblt will be used for present render result on screen.

## `--compile-shader-always-succeeds`

- Constant: `kCompileShaderAlwaysSucceeds`

Always return success when compiling a shader. Linking will still fail.

## `--enable-gpu-service-logging`

- Constant: `kEnableGPUServiceLoggingGPU`

Enable GPU service logging. Note: This is the same switch as the one in gl_switches.cc. It's defined here again to avoid dependencies between dlls.

## `--enable-gpu-driver-debug-logging`

- Constant: `kEnableGPUDriverDebugLogging`

Enable logging of GPU driver debug messages.

## `--force-gpu-mem-discardable-limit-mb`

- Constant: `kForceGpuMemDiscardableLimitMb`

Sets the maximum GPU memory to use for discardable caches.

## `--enable-threaded-texture-mailboxes`

- Constant: `kEnableThreadedTextureMailboxes`

Simulates shared textures when share groups are not available. Not available everywhere.

## `--native`

- Constant: `kVulkanImplementationNameNative`

_No description in the source._

## `--swiftshader`

- Constant: `kVulkanImplementationNameSwiftshader`

_No description in the source._

## `--disable-dump-without-crashing-on-angle-portability-messages`

- Constant: `kDisableDumpWithoutCrashingOnAnglePortabilityMessages`

Disable DumpWithoutCrashing on ANGLE portability messages. This should be used by GPU integration tests to avoid failures on bots.
