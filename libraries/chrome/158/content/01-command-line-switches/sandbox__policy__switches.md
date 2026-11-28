# Command-line switches: `sandbox/policy/switches`

Generated from `sandbox/policy/switches.h` and `sandbox/policy/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

25 switches.

## `--service-sandbox-type`

- Constant: `kServiceSandboxType`

Type of sandbox to apply to the process running the service, one of the values in the next block.

## `--allow-sandbox-debugging`

- Constant: `kAllowSandboxDebugging`

Flags owned by the service manager sandbox. Allows debugging of sandboxed processes (see zygote_main_linux.cc).

## `--disable-gpu-sandbox`

- Constant: `kDisableGpuSandbox`

Disables the GPU process sandbox.

## `--disable-landlock-sandbox`

- Constant: `kDisableLandlockSandbox`

Disables the Landlock sandbox (Android only).

## `--disable-namespace-sandbox`

- Constant: `kDisableNamespaceSandbox`

Disables usage of the namespace sandbox.

## `--disable-seccomp-filter-sandbox`

- Constant: `kDisableSeccompFilterSandbox`

Disable the seccomp filter sandbox (seccomp-bpf) (Linux only).

## `--disable-setuid-sandbox`

- Constant: `kDisableSetuidSandbox`

Disable the setuid sandbox (Linux only).

## `--disable-webnn-compiler-sandbox`

- Constant: `kDisableWebNNCompilerSandbox`

Disables the WebNN compiler process sandbox.

## `--gpu-sandbox-allow-sysv-shm`

- Constant: `kGpuSandboxAllowSysVShm`

Allows shmat() system call in the GPU sandbox.

## `--gpu-sandbox-failures-fatal`

- Constant: `kGpuSandboxFailuresFatal`

Makes GPU sandbox failures fatal.

## `--no-sandbox`

- Constant: `kNoSandbox`

Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only.

## `--no-zygote-sandbox`

- Constant: `kNoZygoteSandbox`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Instructs the zygote to launch without a sandbox. Processes forked from this type of zygote will apply their own custom sandboxes later.

## `--allow-third-party-modules`

- Constant: `kAllowThirdPartyModules`
- Condition: `BUILDFLAG(IS_WIN)`

Allows third party modules to inject by disabling the BINARY_SIGNATURE mitigation policy on Win10+. Also has other effects in ELF.

## `--add-xr-appcontainer-caps`

- Constant: `kAddXrAppContainerCaps`
- Condition: `BUILDFLAG(IS_WIN)`

Add additional capabilities to the AppContainer sandbox used for XR compositing.

## `--enable-sandbox-logging`

- Constant: `kEnableSandboxLogging`
- Condition: `BUILDFLAG(IS_MAC)`

Cause the OS X sandbox write to syslog every time an access to a resource is denied by the sandbox.

## `--disable-metal-shader-cache`

- Constant: `kDisableMetalShaderCache`
- Condition: `BUILDFLAG(IS_MAC)`

Disables Metal's shader cache, using the GPU sandbox to prevent access to it.

## `--type`

- Constant: `kProcessType`

Flags spied upon from other layers.

## `--gpu-process`

- Constant: `kGpuProcess`

_No description in the source._

## `--renderer`

- Constant: `kRendererProcess`

_No description in the source._

## `--utility`

- Constant: `kUtilityProcess`

_No description in the source._

## `--zygote`

- Constant: `kZygoteProcessType`

_No description in the source._

## `--relauncher`

- Constant: `kRelauncherProcessType`

_No description in the source._

## `--code-sign-clone-cleanup`

- Constant: `kCodeSignCloneCleanupProcessType`

_No description in the source._

## `--app-shim`

- Constant: `kAppShimProcessType`

_No description in the source._

## `--no-op-for-testing`

- Constant: `kNoOpForTestingProcessType`

_No description in the source._
