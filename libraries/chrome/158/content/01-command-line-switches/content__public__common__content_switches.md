# Command-line switches: `content/public/common/content_switches`

Generated from `content/public/common/content_switches.h` and `content/public/common/content_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

226 switches.

## `--allow-file-access-from-files`

- Constant: `kAllowFileAccessFromFiles`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. By default, file:// URIs cannot read other file:// URIs. This is an override for developers who need the old behavior for testing.

## `--allow-insecure-localhost`

- Constant: `kAllowInsecureLocalhost`

Enables TLS/SSL errors on localhost to be ignored (no interstitial, no blocking of requests).

## `--allow-loopback-in-peer-connection`

- Constant: `kAllowLoopbackInPeerConnection`

Allows loopback interface to be added in network list for peer connection.

## `--allow-command-line-plugins`

- Constant: `kAllowCommandLinePlugins`

Allows plugins to be loaded in the command line for testing.

## `--auto-accept-camera-and-microphone-capture`

- Constant: `kAutoAcceptCameraAndMicrophoneCapture`

Bypasses the dialog prompting the user for permission to capture cameras and microphones. Useful in automatic tests of video-conferencing Web applications. This is nearly identical to kUseFakeUIForMediaStream, with the exception being that this flag does NOT affect screen-capture.

## `--crash-test`

- Constant: `kBrowserCrashTest`

Causes the browser process to crash on startup.

## `--browser-startup-dialog`

- Constant: `kBrowserStartupDialog`

Causes the browser process to display a dialog on launch.

## `--browser-subprocess-path`

- Constant: `kBrowserSubprocessPath`

Path to the exe to run for the renderer and plugin subprocesses.

## `--browser-test`

- Constant: `kBrowserTest`

Tells whether the code is running browser tests (this changes the startup URL used by the content shell and also disables features that can make tests flaky [like monitoring of memory pressure]).

## `--change-stack-guard-on-fork`

- Constant: `kChangeStackGuardOnFork`

After a zygote forks a new process, change the stack canary. This switch is useful so not all forked processes use the same canary (a secret value), which can be vulnerable to information leaks and brute force attacks. See https://crbug.com/1206626. This requires that all functions on the stack at the time content::RunZygote() is called be compiled without stack canaries. Valid values are "enable" or "disable".

## `--enable`

- Constant: `kChangeStackGuardOnForkEnabled`

_No description in the source._

## `--disable`

- Constant: `kChangeStackGuardOnForkDisabled`

_No description in the source._

## `--disable-canvas-aa`

- Constant: `kDisable2dCanvasAntialiasing`

Disable antialiasing on 2d canvas.

## `--disable-3d-apis`

- Constant: `kDisable3DAPIs`

Disables client-visible 3D APIs, in particular WebGL. This is controlled by policy and is kept separate from the other enable/disable switches to avoid accidentally regressing the policy support for controlling access to these APIs.

## `--disable-accelerated-2d-canvas`

- Constant: `kDisableAccelerated2dCanvas`

Disable gpu-accelerated 2d canvas.

## `--disable-accelerated-video-decode`

- Constant: `kDisableAcceleratedVideoDecode`

Disables hardware acceleration of video decode, where available. Warning: do not remove or rename this flag, as it is used inside ChromeOS code to implement the DeviceHardwareVideoDecodingEnabled policy.

## `--disable-yuv-image-decoding`

- Constant: `kDisableYUVImageDecoding`

Disable YUV image decoding for those formats and cases where it's supported. Has no effect unless GPU rasterization is enabled.

## `--disable-accelerated-video-encode`

- Constant: `kDisableAcceleratedVideoEncode`

Disables hardware acceleration of video encode, where available.

## `--disable-backing-store-limit`

- Constant: `kDisableBackingStoreLimit`

Disable limits on the number of backing stores. Can prevent blinking for users with many windows/tabs and lots of memory.

## `--disable-background-timer-throttling`

- Constant: `kDisableBackgroundTimerThrottling`

Disable task throttling of timer tasks from background pages.

## `--disable-back-forward-cache`

- Constant: `kDisableBackForwardCache`

Disables the BackForwardCache feature.

## `--disable-best-effort-tasks`

- Constant: `kDisableBestEffortTasks`

Delays execution of TaskPriority::BEST_EFFORT tasks until shutdown.

## `--disable-blink-features`

- Constant: `kDisableBlinkFeatures`

Disable one or more Blink runtime-enabled features. Use names from runtime_enabled_features.json5, separated by commas. Applied after kEnableBlinkFeatures, and after other flags that change these features.

## `--disable-domain-blocking-for-3d-apis`

- Constant: `kDisableDomainBlockingFor3DAPIs`

Disable the per-domain blocking for 3D APIs after GPU reset. This switch is intended only for tests.

## `--disable-in-process-stack-traces`

- Constant: `kDisableInProcessStackTraces`

Disables the in-process stack traces.

## `--disable-webgl`

- Constant: `kDisableWebGL`

Disable all versions of WebGL.

## `--disable-webgl2`

- Constant: `kDisableWebGL2`

Disable WebGL2.

## `--disable-file-system`

- Constant: `kDisableFileSystem`

Disable FileSystem API.

## `--disable-gesture-requirement-for-presentation`

- Constant: `kDisableGestureRequirementForPresentation`

Disable user gesture requirement for presentation.

## `--disable-gpu`

- Constant: `kDisableGpu`

Disables GPU hardware acceleration.  If software renderer is not in place, then the GPU process won't launch.

## `--disable-gpu-compositing`

- Constant: `kDisableGpuCompositing`

Prevent the compositor from using its GPU implementation.

## `--disable-gpu-early-init`

- Constant: `kDisableGpuEarlyInit`

Disable proactive early init of GPU process.

## `--disable-gpu-memory-buffer-compositor-resources`

- Constant: `kDisableGpuMemoryBufferCompositorResources`

Do not force that all compositor resources be backed by GPU memory buffers.

## `--disable-gpu-memory-buffer-video-frames`

- Constant: `kDisableGpuMemoryBufferVideoFrames`

Disable GpuMemoryBuffer backed VideoFrames.

## `--disable-gpu-process-crash-limit`

- Constant: `kDisableGpuProcessCrashLimit`

For tests, to disable the limit on the number of times the GPU process may be restarted.

## `--disable-scroll-to-text-fragment`

- Constant: `kDisableScrollToTextFragment`

This switch disables the ScrollToTextFragment feature.

## `--disable-software-compositing-fallback`

- Constant: `kDisableSoftwareCompositingFallback`

For tests, to disable falling back to software compositing if the GPU Process has crashed, and reached the GPU Process crash limit.

## `--disable-gpu-watchdog`

- Constant: `kDisableGpuWatchdog`

Disable the thread that crashes the GPU process if it stops responding to messages.

## `--disable-ipc-flooding-protection`

- Constant: `kDisableIpcFloodingProtection`

Disables the IPC flooding protection. It is activated by default. Some javascript functions can be used to flood the browser process with IPC. This protection limits the rate at which they can be used.

## `--disable-ignore-duplicate-navs-for-testing`

- Constant: `kDisableIgnoreDuplicateNavsForTesting`

Disables the IgnoreDuplicateNavs feature. This prevent navigations from being unintentionally ignored in tests.

## `--disable-javascript-harmony-shipping`

- Constant: `kDisableJavaScriptHarmonyShipping`

Disable latest shipping ECMAScript 6 features.

## `--disable-low-latency-dxva`

- Constant: `kDisableLowLatencyDxva`

Disables using CODECAPI_AVLowLatencyMode when creating DXVA decoders.

## `--disable-histogram-customizer`

- Constant: `kDisableHistogramCustomizer`

Disable the RenderThread's HistogramCustomizer.

## `--disable-lcd-text`

- Constant: `kDisableLCDText`

Disables LCD text.

## `--disable-kill-after-bad-ipc`

- Constant: `kDisableKillAfterBadIPC`

Don't kill a child process when it sends a bad IPC message.  Apart from testing, it is a bad idea from a security perspective to enable this switch.

## `--disable-local-storage`

- Constant: `kDisableLocalStorage`

Disable LocalStorage.

## `--disable-logging`

- Constant: `kDisableLogging`

Force logging to be disabled.  Logging is enabled by default in debug builds.

## `--disable-main-thread-name-override`

- Constant: `kDisableMainThreadNameOverride`

Disables renaming the main browser thread to "CrBrowserMain" during browser startup. The internally mapped thread name is being emitted to Perfetto traces, which means that the main thread is identified as "CrBrowserMain" instead of the process name. Enabling this switch will prevent the thread from being named, which fixes the Perfetto trace issue.

## `--disable-mojo-broker`

- Constant: `kDisableMojoBroker`

Disables Mojo broker capabilities in the browser during Mojo initialization.

## `--disable-new-content-rendering-timeout`

- Constant: `kDisableNewContentRenderingTimeout`

Disables clearing the rendering output of a renderer when it didn't commit new output for a while after a top-frame navigation.

## `--disable-notifications`

- Constant: `kDisableNotifications`

Disables the Web Notification and the Push APIs.

## `--disable-nv12-dxgi-video`

- Constant: `kDisableNv12DxgiVideo`

Disables the video decoder from drawing to an NV12 textures instead of ARGB.

## `--disable-origin-trial-controlled-blink-features`

- Constant: `kDisableOriginTrialControlledBlinkFeatures`

Disables all RuntimeEnabledFeatures that can be enabled via OriginTrials.

## `--disable-platform-accessibility-integration`

- Constant: `kDisablePlatformAccessibilityIntegration`

Disables the activation of browser and web accessibility via interactions with the platform's accessibility integration (i.e., a screenreader will not be able to function with the browser).

## `--disable-presentation-api`

- Constant: `kDisablePresentationAPI`

Disables the Presentation API.

## `--disable-pushstate-throttle`

- Constant: `kDisablePushStateThrottle`

Disables throttling of history.pushState/replaceState calls.

## `--disable-reading-from-canvas`

- Constant: `kDisableReadingFromCanvas`

Taints all <canvas> elements, regardless of origin.

## `--disable-remote-fonts`

- Constant: `kDisableRemoteFonts`

Disables remote web font support. SVG font should always work whether this option is specified or not.

## `--disable-remote-playback-api`

- Constant: `kDisableRemotePlaybackAPI`

Disables the RemotePlayback API.

## `--disable-renderer-backgrounding`

- Constant: `kDisableRendererBackgrounding`

Prevent renderer process backgrounding when set. Renderer processes keep a foreground priority at the OS level, and renderers are never told that they are backgrounded or hidden.  The browser still computes each renderer process's priority as usual (e.g. RenderProcessHost::GetPriority()), so that tests can verify the priority policy without being slowed down by actual backgrounding.

## `--disable-resource-scheduler`

- Constant: `kDisableResourceScheduler`

Whether the ResourceScheduler is disabled.  Note this is only useful for C++ Headless embedders who need to implement their own resource scheduling.

## `--disable-shared-workers`

- Constant: `kDisableSharedWorkers`

Disable shared workers.

## `--disable-skia-runtime-opts`

- Constant: `kDisableSkiaRuntimeOpts`

Do not use runtime-detected high-end CPU optimizations in Skia.  This is useful for forcing a baseline code path for e.g. web tests.

## `--disable-smooth-scrolling`

- Constant: `kDisableSmoothScrolling`

Disable smooth scrolling for testing.

## `--disable-software-rasterizer`

- Constant: `kDisableSoftwareRasterizer`

Disables the use of a 3D software rasterizer.

## `--disable-speech-api`

- Constant: `kDisableSpeechAPI`

Disables the Web Speech API (both speech recognition and synthesis).

## `--disable-speech-synthesis-api`

- Constant: `kDisableSpeechSynthesisAPI`

Disables the speech synthesis part of Web Speech API.

## `--disable-threaded-compositing`

- Constant: `kDisableThreadedCompositing`

Disable multithreaded GPU compositing of web content.

## `--disable-v8-idle-tasks`

- Constant: `kDisableV8IdleTasks`

Disable V8 idle tasks.

## `--disable-webrtc-encryption`

- Constant: `kDisableWebRtcEncryption`

Disables encryption of RTP Media for WebRTC. When Chrome embeds Content, it ignores this switch on its stable and beta channels.

## `--disable-web-security`

- Constant: `kDisableWebSecurity`

Don't enforce the same-origin policy; meant for website testing only. This switch has no effect unless --user-data-dir (as defined by the content embedder) is also present.

## `--dom-automation`

- Constant: `kDomAutomationController`

Specifies if the |DOMAutomationController| needs to be bound in the renderer. This binding happens on per-frame basis and hence can potentially be a performance bottleneck. One should only enable it when automating dom based tests.

## `--disable-2d-canvas-clip-aa`

- Constant: `kDisable2dCanvasClipAntialiasing`

Disable antialiasing on 2d canvas clips

## `--enable-aggressive-domstorage-flushing`

- Constant: `kEnableAggressiveDOMStorageFlushing`

Enable the aggressive flushing of DOM Storage to minimize data loss.

## `--enable-automation`

- Constant: `kEnableAutomation`

Enable indication that browser is controlled by automation.

## `--enable-blink-features`

- Constant: `kEnableBlinkFeatures`

Enable one or more Blink runtime-enabled features. Use names from runtime_enabled_features.json5, separated by commas. Applied before kDisableBlinkFeatures, and after other flags that change these features.

## `--enable-caret-browsing`

- Constant: `kEnableCaretBrowsing`

Enable native caret browsing, in which a moveable cursor is placed on a web page, allowing a user to select and navigate through non-editable text using just a keyboard. See https://crbug.com/977390 for links to i2i.

## `--enable-experimental-cookie-features`

- Constant: `kEnableExperimentalCookieFeatures`

Flag that turns on a group of experimental/newly added cookie-related features together, as a convenience for e.g. testing, to avoid having to set multiple switches individually which may be error-prone (not to mention tedious). There is not a corresponding switch to disable all these features, because that is discouraged, and for testing purposes you'd need to switch them off individually to identify the problematic feature anyway.  At present this turns on: net::features::kSameSiteDefaultChecksMethodRigorously net::features::kCookieSameSiteConsidersRedirectChain net::features::kEnablePortBoundCookies net::features::kEnableSchemeBoundCookies

## `--enable-experimental-webassembly-features`

- Constant: `kEnableExperimentalWebAssemblyFeatures`

Enables experimental WebAssembly features.

## `--enable-experimental-web-platform-features`

- Constant: `kEnableExperimentalWebPlatformFeatures`

Enables Web Platform features that are in development.

## `--enable-blink-test-features`

- Constant: `kEnableBlinkTestFeatures`

Enables blink runtime enabled features with status:"test" or status:"experimental", which are enabled when running web tests.

## `--expose-internals-for-testing`

- Constant: `kExposeInternalsForTesting`

Exposes the window.internals object in JavaScript for testing.

## `--enable-gpu-memory-buffer-video-frames`

- Constant: `kEnableGpuMemoryBufferVideoFrames`

Enable GpuMemoryBuffer backed VideoFrames.

## `--enable-isolated-web-apps-in-renderer`

- Constant: `kEnableIsolatedWebAppsInRenderer`

Enables Isolated Web Apps (IWAs) in a renderer process. There are two ways to enable the IWAs: by feature flag and by enterprise policy. If IWAs are enabled by any of the mentioned above ways then this flag is passed to the renderer process. This flag should not be used from command line. To enable IWAs from command line one should use kIsolatedWebApps feature flag.

## `--enable-lcd-text`

- Constant: `kEnableLCDText`

Enables LCD text.

## `--enable-logging`

- Constant: `kEnableLogging`

Force logging to be enabled.  Logging is disabled by default in release builds.

## `--enable-network-information-downlink-max`

- Constant: `kEnableNetworkInformationDownlinkMax`

Enables the type, downlinkMax attributes of the NetInfo API. Also, enables triggering of change attribute of the NetInfo API when there is a change in the connection type.

## `--canvas-2d-layers`

- Constant: `kEnableCanvas2DLayers`

Enable in-progress canvas 2d API methods BeginLayer and EndLayer.

## `--enable-plugin-placeholder-testing`

- Constant: `kEnablePluginPlaceholderTesting`

Enables testing features of the Plugin Placeholder. For internal use only.

## `--enable-precise-memory-info`

- Constant: `kEnablePreciseMemoryInfo`

Make the values returned to window.performance.memory more granular and more up to date in shared worker. Without this flag, the memory information is still available, but it is bucketized and updated less frequently. This flag also applys to workers.

## `--enable-privacy-sandbox-ads-apis`

- Constant: `kEnablePrivacySandboxAdsApis`

Enables Privacy Sandbox APIs: Attribution Reporting, Fledge, Topics, Fenced Frames, Shared Storage, Private Aggregation, and their associated features.

## `--enable-service-binary-launcher`

- Constant: `kEnableServiceBinaryLauncher`

If true the ServiceProcessLauncher is used to launch services. This allows for service binaries to be loaded rather than using the utility process. This is only useful for tests.

## `--enable-skia-benchmarking`

- Constant: `kEnableSkiaBenchmarking`

Enables the Skia benchmarking extension.

## `--enable-smooth-scrolling`

- Constant: `kEnableSmoothScrolling`

On platforms that support it, enables smooth scroll animation.

## `--enable-spatial-navigation`

- Constant: `kEnableSpatialNavigation`

Enable spatial navigation

## `--enable-strict-mixed-content-checking`

- Constant: `kEnableStrictMixedContentChecking`

Blocks all insecure requests from secure contexts, and prevents the user from overriding that decision.

## `--enable-tracing-fraction`

- Constant: `kEnableTracingFraction`

When specified along with a value in the range (0,1] will --enable-tracing for (roughly) that percentage of tests being run. This is done in a stable manner such that the same tests are chosen each run, and under the assumption that tests hash equally across the range of possible values. The flag will enable all tracing categories for those tests, and none for the rest. This flag could be used with other tracing switches like --enable-tracing-format, but any other switches that will enable tracing will turn tracing on for all tests.

## `--enable-usermedia-screen-capturing`

- Constant: `kEnableUserMediaScreenCapturing`

Enable screen capturing support for MediaStream API.

## `--enable-viewport`

- Constant: `kEnableViewport`

Enables the use of the @viewport CSS rule, which allows pages to control aspects of their own layout. This also turns on touch-screen pinch gestures.

## `--enable-vtune-support`

- Constant: `kEnableVtune`

Enable the Vtune profiler support.

## `--enable-webgl-developer-extensions`

- Constant: `kEnableWebGLDeveloperExtensions`

Enables WebGL developer extensions which are not generally exposed to the web platform.

## `--file-url-path-alias`

- Constant: `kFileUrlPathAlias`

Define an alias root directory which is replaced with the replacement string in file URLs. The format is "/alias=/replacement", which would turn file:///alias/some/path.html into file:///replacement/some/path.html.

## `--force-presentation-receiver-for-testing`

- Constant: `kForcePresentationReceiverForTesting`

This forces pages to be loaded as presentation receivers.  Useful for testing behavior specific to presentation receivers. Spec: https://www.w3.org/TR/presentation-api/#interface-presentationreceiver

## `--force-webrtc-ip-handling-policy`

- Constant: `kForceWebRtcIPHandlingPolicy`

Override WebRTC IP handling policy to mimic the behavior when WebRTC IP handling policy is specified in Preferences.

## `--gpu-launcher`

- Constant: `kGpuLauncher`

Extra command line options for launching the GPU process (normally used for debugging). Use like renderer-cmd-prefix.

## `--gpu-client-id`

- Constant: `kGpuClientId`

_No description in the source._

## `--gpu-process`

- Constant: `kGpuProcess`

Makes this process a GPU sub-process.

## `--gpu-sandbox-start-early`

- Constant: `kGpuSandboxStartEarly`

Starts the GPU sandbox before creating a GL context.

## `--gpu-startup-dialog`

- Constant: `kGpuStartupDialog`

Causes the GPU process to display a dialog on launch.

## `--hide-scrollbars`

- Constant: `kHideScrollbars`

Prevents creating scrollbars for web content. Useful for taking consistent screenshots.

## `--in-process-gpu`

- Constant: `kInProcessGPU`

Run the GPU process as a thread in the browser process.

## `--ipc-connection-timeout`

- Constant: `kIPCConnectionTimeout`

Overrides the timeout, in seconds, that a child process waits for a connection from the browser before killing itself.

## `--isolate-origins`

- Constant: `kIsolateOrigins`

Require dedicated processes for a set of origins, specified as a comma-separated list. For example: --isolate-origins=https://www.foo.com,https://www.bar.com

## `--javascript-harmony`

- Constant: `kJavaScriptHarmony`

Enables experimental Harmony (ECMAScript 6) features.

## `--as-browser`

- Constant: `kLaunchAsBrowser`

Flag to launch tests in the browser process.

## `--load-webui-from-disk`

- Constant: `kLoadWebUIfromDisk`
- Condition: `BUILDFLAG(LOAD_WEBUI_FROM_DISK)`

Flag used to load WebUI files directly from disk instead of pak files. Meant to be used during local development only (requires a local checkout and build), and only works if used along with the GN load_webui_from_disk=true GN flag.

## `--log-gpu-control-list-decisions`

- Constant: `kLogGpuControlListDecisions`

Logs GPU control list decisions when enforcing blocklist rules.

## `--log-level`

- Constant: `kLoggingLevel`

Sets the minimum log level. Valid values are from 0 to 3: INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3.

## `--log-file`

- Constant: `kLogFile`

Overrides the default file name to use for general-purpose logging (does not affect which events are logged).

## `--log-missing-unload-ack`

- Constant: `kLogMissingUnloadACK`

Log an error whenever the unload timeout for a render frame is exceeded.

## `--max-active-webgl-contexts`

- Constant: `kMaxActiveWebGLContexts`

Allows user to override maximum number of active WebGL contexts per renderer process.

## `--max-decoded-image-size-mb`

- Constant: `kMaxDecodedImageSizeMb`

Sets the maximium decoded image size limitation.

## `--max-web-media-player-count`

- Constant: `kMaxWebMediaPlayerCount`

Sets the maximum number of WebMediaPlayers allowed per frame.

## `--message-loop-type-ui`

- Constant: `kMessageLoopTypeUi`

Indicates the utility process should run with a message loop type of UI.

## `--mock-cert-verifier-default-result-for-testing`

- Constant: `kMockCertVerifierDefaultResultForTesting`

Set the default result for MockCertVerifier. This only works in test code.

## `--mojo-local-storage`

- Constant: `kMojoLocalStorage`

Use a Mojo-based LocalStorage implementation.

## `--no-unsandboxed-zygote`

- Constant: `kNoUnsandboxedZygote`

Disables the unsandboxed zygote. Note: this flag should not be used on most platforms. It is introduced because some platforms (e.g. Cast) have very limited memory and binaries won't be updated when the browser process is running.

## `--no-zygote`

- Constant: `kNoZygote`

Disables the use of a zygote process for forking child processes. Instead, child processes will be forked and exec'd directly. Note that --no-sandbox should also be used together with this flag because the sandbox needs the zygote to work.

## `--override-language-detection`

- Constant: `kOverrideLanguageDetection`

Overrides the language detection result determined based on the page contents.

## `--pdf-renderer`

- Constant: `kPdfRenderer`

Renderer process that runs the non-PPAPI PDF plugin.

## `--process-per-site`

- Constant: `kProcessPerSite`

Enable the "Process Per Site" process model for all domains. This mode consolidates same-site pages so that they share a single process.  More details here: - https://www.chromium.org/developers/design-documents/process-models - The class comment in site_instance.h, listing the supported process models.  IMPORTANT: This isn't to be confused with --site-per-process (which is about isolation, not consolidation). You probably want the other one.

## `--process-per-tab`

- Constant: `kProcessPerTab`

Runs each set of script-connected tabs (i.e., a BrowsingInstance) in its own renderer process.  We default to using a renderer process for each site instance (i.e., group of pages from the same registered domain with script connections to each other). TODO(creis): This flag is currently a no-op.  We should refactor it to avoid "unnecessary" process swaps for cross-site navigations but still swap when needed for security (e.g., isolated origins).

## `--type`

- Constant: `kProcessType`

The value of this switch determines whether the process is started as a renderer or plugin host.  If it's empty, it's the browser.

## `--pseudonymization-salt-handle`

- Constant: `kPseudonymizationSaltHandle`

Handle to shared memory containing the pseudonymization salt, passed to child processes at launch. See https://crbug.com/40850085.

## `--reduce-accept-language`

- Constant: `kReduceAcceptLanguage`

Reduce the accept-language for HTTP header and JS navigator.languages, and only most preferred language: https://github.com/Tanych/accept-language.

## `--reduce-accept-language-http`

- Constant: `kReduceAcceptLanguageHTTP`

Reduce the accept-language for HTTP header, and only send most preferred language in the request header: https://github.com/Tanych/accept-language.

## `--reduce-user-agent-minor-version`

- Constant: `kReduceUserAgentMinorVersion`

Reduce the minor version number in the User-Agent string. This flag implements phase 4 of User-Agent reduction: https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html.

## `--remote-debugging-pipe`

- Constant: `kRemoteDebuggingPipe`

Enables remote debug over stdio pipes [in=3, out=4] or over the remote pipes specified in the 'remote-debugging-io-pipes' switch. Optionally, specifies the format for the protocol messages, can be either "JSON" (the default) or "CBOR".

## `--remote-debugging-port`

- Constant: `kRemoteDebuggingPort`

Enables remote debug over HTTP on the specified port.

## `--remote-allow-origins`

- Constant: `kRemoteAllowOrigins`

Enables web socket connections from the specified origins only. '*' allows any origin.

## `--renderer-client-id`

- Constant: `kRendererClientId`

_No description in the source._

## `--renderer-cmd-prefix`

- Constant: `kRendererCmdPrefix`

The contents of this flag are prepended to the renderer command line. Useful values might be "valgrind" or "xterm -e gdb --args".

## `--renderer`

- Constant: `kRendererProcess`

Causes the process to run as renderer instead of as browser.

## `--launch-time-ticks`

- Constant: `kRendererProcessLaunchTimeTicks`

Time the browser launched the renderer process (in TimeTicks).

## `--renderer-process-limit`

- Constant: `kRendererProcessLimit`

Overrides the default/calculated limit to the number of renderer processes. Very high values for this setting can lead to high memory/resource usage or instability.

## `--renderer-startup-dialog`

- Constant: `kRendererStartupDialog`

Causes the renderer process to display a dialog on launch. Passing this flag also adds sandbox::policy::kNoSandbox on Windows non-official builds, since that's needed to show a dialog.

## `--gpu-channel-request-start-time-ticks`

- Constant: `kGpuChannelRequestStartTimeTicks`

Time the browser process requested the GPU channel for the renderer (in TimeTicks).

## `--run-manual`

- Constant: `kRunManualTestsFlag`

Manual tests only run when --run-manual is specified. This allows writing tests that don't run automatically but are still in the same test binary. This is useful so that a team that wants to run a few tests doesn't have to add a new binary that must be compiled on all builds.

## `--sandbox-ipc`

- Constant: `kSandboxIPCProcess`

Causes the process to run as a sandbox IPC subprocess.

## `--shared-array-buffer-unrestricted-access-allowed`

- Constant: `kSharedArrayBufferUnrestrictedAccessAllowed`
- Condition: `!BUILDFLAG(IS_ANDROID)`

_No description in the source._

## `--shared-files`

- Constant: `kSharedFiles`

Describes the file descriptors passed to a child process in the following list format:  <file_id>:<descriptor_id>,<file_id>:<descriptor_id>,...  where <file_id> is an ID string from the manifest of the service being launched and <descriptor_id> is the numeric identifier of the descriptor for the child process can use to retrieve the file descriptor from the global descriptor table.

## `--single-process`

- Constant: `kSingleProcess`

Runs the renderer and plugins in the same process as the browser

## `--site-per-process`

- Constant: `kSitePerProcess`

Enforces a one-site-per-process security policy: * Each renderer process, for its whole lifetime, is dedicated to rendering pages for just one site. * Thus, pages from different sites are never in the same process. * A renderer process's access rights are restricted based on its site. * All cross-site navigations force process swaps. * <iframe>s are rendered out-of-process whenever the src= is cross-site.  More details here: - https://www.chromium.org/developers/design-documents/site-isolation - https://www.chromium.org/developers/design-documents/process-models - The class comment in site_instance.h, listing the supported process models.  IMPORTANT: this isn't to be confused with --process-per-site (which is about process consolidation, not isolation). You probably want this one.

## `--disable-site-isolation-trials`

- Constant: `kDisableSiteIsolation`

Disables site isolation.  Note that the opt-in (to site-per-process, isolate-origins, etc.) via enterprise policy and/or cmdline takes precedence over the kDisableSiteIsolation switch (i.e. the opt-in takes effect despite potential presence of kDisableSiteIsolation switch).  Note that for historic reasons the name of the switch misleadingly mentions "trials", but the switch also disables the default site isolation that ships on desktop since M67.  The name of the switch is preserved for backcompatibility of chrome://flags.

## `--start-fullscreen`

- Constant: `kStartFullscreen`

Specifies if the browser should start in fullscreen mode, like if the user had pressed F11 right after startup.

## `--enable-stats-collection-bindings`

- Constant: `kStatsCollectionController`

Specifies if the |StatsCollectionController| needs to be bound in the renderer. This binding happens on per-frame basis and hence can potentially be a performance bottleneck. One should only enable it when running a test that needs to access the provided statistics.

## `--skia-font-cache-limit-mb`

- Constant: `kSkiaFontCacheLimitMb`

Specifies the max number of bytes that should be used by the skia font cache. If the cache needs to allocate more, skia will purge previous entries.

## `--skia-resource-cache-limit-mb`

- Constant: `kSkiaResourceCacheLimitMb`

Specifies the max number of bytes that should be used by the skia resource cache. The previous entries are purged from the cache when the memory useage exceeds this limit.

## `--target-device-scale-for-testing`

- Constant: `kTargetDeviceScaleForTesting`

Allows web tests to specify the target device scale for the test cases.

## `--test-type`

- Constant: `kTestType`

Type of the current test harness ("browser" or "ui" or "gpu").

## `--top-chrome-webui`

- Constant: `kTopChromeWebUI`

Indicates that this RenderProcess is hosting a Top Chrome WebUI.

## `--touch-events`

- Constant: `kTouchEventFeatureDetection`

Enable support for touch event feature detection.

## `--auto`

- Constant: `kTouchEventFeatureDetectionAuto`

The values the kTouchEventFeatureDetection switch may have, as in --touch-events=disabled. auto: enabled at startup when an attached touchscreen is present.

## `--enabled`

- Constant: `kTouchEventFeatureDetectionEnabled`

enabled: touch events always enabled.

## `--disabled`

- Constant: `kTouchEventFeatureDetectionDisabled`

disabled: touch events are disabled.

## `--unbounded-window-debug`

- Constant: `kUnboundedWindowDebug`

Enables debug mode for unbounded windows (draws a red border).

## `--use-fake-codec-for-peer-connection`

- Constant: `kUseFakeCodecForPeerConnection`

Replaces the existing codecs supported in peer connection with a single fake codec entry that create a fake video encoder and decoder.

## `--use-fake-ui-for-digital-identity`

- Constant: `kUseFakeUIForDigitalIdentity`

Bypass the digital-identity-credential OS call. Simulate the user accepting the OS-presented dialog.

## `--use-fake-ui-for-fedcm`

- Constant: `kUseFakeUIForFedCM`

Bypass the FedCM account selection dialog. If a value is provided for this switch, that account ID is selected, otherwise the first account is chosen.

## `--use-fake-ui-for-media-stream`

- Constant: `kUseFakeUIForMediaStream`

Bypass the media stream infobar by selecting the default device for media streams (e.g. WebRTC). Works with --use-fake-device-for-media-stream. Prefer --auto-accept-camera-and-microphone-capture which does not interact with screen/tab capture.

## `--video-image-texture-target`

- Constant: `kVideoImageTextureTarget`

Texture target for CHROMIUM_image backed video frame textures.

## `--use-context-snapshot`

- Constant: `kUseContextSnapshotSwitch`
- Condition: `BUILDFLAG(IS_ANDROID) && BUILDFLAG(INCLUDE_BOTH_V8_SNAPSHOTS)`

Switch supplied to the renderer if the feature `kUseContextSnapshot` is enabled. A switch is used as at the time the renderer needs this information features have not yet been loaded.

## `--use-mock-cert-verifier-for-testing`

- Constant: `kUseMockCertVerifierForTesting`

Use the MockCertVerifier. This only works in test code.

## `--utility-cmd-prefix`

- Constant: `kUtilityCmdPrefix`

The contents of this flag are prepended to the utility process command line. Useful values might be "valgrind" or "xterm -e gdb --args".

## `--utility`

- Constant: `kUtilityProcess`

Causes the process to run as a utility subprocess.

## `--utility-startup-dialog`

- Constant: `kUtilityStartupDialog`

Causes the utility process to display a dialog on launch.

## `--utility-sub-type`

- Constant: `kUtilitySubType`

This switch indicates the type of a utility process. It does not affect the services offered by the process, but is added to the command line to make it easier to identify the purpose of the utility process.

## `--utility-immediate-crash-for-testing`

- Constant: `kUtilityImmediateCrashForTesting`

Crash the Utility process early in start-up, for testing.

## `--v8-cache-options`

- Constant: `kV8CacheOptions`

Set options to cache V8 data. (none, code, or default)

## `--disallow-v8-feature-flag-overrides`

- Constant: `kDisallowV8FeatureFlagOverrides`

Disallows overriding of v8 feature flags.

## `--browser-ui-tests-verify-pixels`

- Constant: `kVerifyPixels`

Causes tests to attempt to verify pixel output.

## `--wait-for-debugger-children`

- Constant: `kWaitForDebuggerChildren`

Will add kWaitForDebugger to every child processes. If a value is passed, it will be used as a filter to determine if the child process should have the kWaitForDebugger flag passed on or not.

## `--wait-for-debugger-on-navigation`

- Constant: `kWaitForDebuggerOnNavigation`

On every navigation a message with the renderer's URL will be logged and the renderer will wait for a debugger to be attached or SIGUSR1 to be sent to continue execution.

## `--wait-for-debugger-webui`

- Constant: `kWaitForDebuggerWebUI`

Flag used by WebUI test runners to wait for debugger to be attached.

## `--webauthn-remote-desktop-support`

- Constant: `kWebAuthRemoteDesktopSupport`

Allows trusted remote desktop clients to make WebAuthn requests on behalf of other origins. This switch only controls availability of the `remoteDesktopClientOverride` extension but doesn't by itself enable any origin to use it.

## `--webgl-antialiasing-mode`

- Constant: `kWebglAntialiasingMode`

Set the antialiasing method used for webgl. (none, explicit, implicit)

## `--webgl-msaa-sample-count`

- Constant: `kWebglMSAASampleCount`

Set a default sample count for webgl if msaa is enabled.

## `--web-otp-backend`

- Constant: `kWebOtpBackend`

Enables specified backend for the Web OTP API.

## `--web-otp-backend-sms-verification`

- Constant: `kWebOtpBackendSmsVerification`

Enables Sms Verification backend for Web OTP API which requires app hash in SMS body.

## `--web-otp-backend-user-consent`

- Constant: `kWebOtpBackendUserConsent`

Enables User Consent backend for Web OTP API.

## `--web-otp-backend-auto`

- Constant: `kWebOtpBackendAuto`

Enables auto backend selection for Web OTP API.

## `--webrtc-event-logging`

- Constant: `kWebRtcLocalEventLogging`

Enable capture and local storage of WebRTC event logs without visiting chrome://webrtc-internals. This is useful for automated testing. It accepts the path to which the local logs would be stored. Disabling is not possible without restarting the browser and relaunching without this flag.

## `--max-gum-fps`

- Constant: `kWebRtcMaxCaptureFramerate`

Override the maximum framerate as can be specified in calls to getUserMedia. This flag expects a value.  Example: --max-gum-fps=17.5

## `--web-settings-for-testing`

- Constant: `kWebSettingsForTesting`

Allows web tests to specify additional web settings for the test cases.

## `--force-webxr-runtime`

- Constant: `kWebXrForceRuntime`

Forcibly enable and select the specified runtime for webxr. Note that this provides an alternative means of enabling a runtime, and will also functionally disable all other runtimes.

## `--no-xr-runtime`

- Constant: `kWebXrRuntimeNone`

Tell WebXr to assume that it does not support any runtimes.

## `--arcore`

- Constant: `kWebXrRuntimeArCore`

The following are the runtimes that WebXr supports.

## `--cardboard`

- Constant: `kWebXrRuntimeCardboard`

_No description in the source._

## `--orientation-sensors`

- Constant: `kWebXrRuntimeOrientationSensors`

_No description in the source._

## `--openxr`

- Constant: `kWebXrRuntimeOpenXr`

_No description in the source._

## `--zygote-cmd-prefix`

- Constant: `kZygoteCmdPrefix`

The prefix used when starting the zygote process. (i.e. 'gdb --args')

## `--zygote`

- Constant: `kZygoteProcess`

Causes the process to run as a zygote.

## `--disable-media-session-api`

- Constant: `kDisableMediaSessionAPI`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disable Media Session API

## `--disable-oopr-debug-crash-dump`

- Constant: `kDisableOoprDebugCrashDump`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disables debug crash dumps for OOPR.

## `--disable-screen-orientation-lock`

- Constant: `kDisableScreenOrientationLock`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disable the locking feature of the screen orientation API.

## `--disable-site-isolation-for-policy`

- Constant: `kDisableSiteIsolationForPolicy`
- Condition: `BUILDFLAG(IS_ANDROID)`

Just like kDisableSiteIsolation, but doesn't show the "stability and security will suffer" butter bar warning.

## `--disable-timeouts-for-profiling`

- Constant: `kDisableTimeoutsForProfiling`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disable timeouts that may cause the browser to die when running slowly. This is useful if running with profiling (such as debug malloc).

## `--enable-adaptive-selection-handle-orientation`

- Constant: `kEnableAdaptiveSelectionHandleOrientation`
- Condition: `BUILDFLAG(IS_ANDROID)`

Enable inverting of selection handles so that they are not clipped by the viewport boundaries.

## `--enable-longpress-drag-selection`

- Constant: `kEnableLongpressDragSelection`
- Condition: `BUILDFLAG(IS_ANDROID)`

Enable drag manipulation of longpress-triggered text selections.

## `--force-online-connection-state-for-indicator`

- Constant: `kForceOnlineConnectionStateForIndicator`
- Condition: `BUILDFLAG(IS_ANDROID)`

Prevent the offline indicator from showing.

## `--remote-debugging-socket-name`

- Constant: `kRemoteDebuggingSocketName`
- Condition: `BUILDFLAG(IS_ANDROID)`

Enables remote debug over HTTP on the specified socket name.

## `--renderer-wait-for-java-debugger`

- Constant: `kRendererWaitForJavaDebugger`
- Condition: `BUILDFLAG(IS_ANDROID)`

Block ChildProcessMain thread of the renderer's ChildProcessService until a Java debugger is attached.

## `--javaless-renderers`

- Constant: `kJavalessRenderers`
- Condition: `BUILDFLAG(IS_ANDROID)`

Enables/disables javaless renderers based on value given. "enabled" or "disabled" are valid values.

## `--prevent-resizing-contents-for-testing`

- Constant: `kPreventResizingContentsForTesting`
- Condition: `BUILDFLAG(IS_IOS)`

For mobile devices, tests should include a viewport meta tag to specify page dimension adjustments. Omitting the tag can lead to automatic resizing to the standard mobile fallback size (980), which results in content shrinking as it first expands to 980, then scales down to 800 to fit the screen, as observed in the issue at https://crrev.com/c/4615623. This flag is intended for use in tests that do not include a viewport meta tag. When enabled, it ensures the viewport size matches the standard mobile fallback size, thereby helping to prevent content resizing in such tests.

## `--enable-speech-dispatcher`

- Constant: `kEnableSpeechDispatcher`
- Condition: `BUILDFLAG(IS_LINUX)`

Allows sending text-to-speech requests to speech-dispatcher, a common Linux speech service. Because it's buggy, the user must explicitly enable it so that visiting a random webpage can't cause instability.

## `--device-scale-factor`

- Constant: `kDeviceScaleFactor`
- Condition: `BUILDFLAG(IS_WIN)`

This switch contains the device scale factor passed to certain processes like renderers, etc. Device scale factor passed to certain processes like renderers, etc.

## `--disable-legacy-window`

- Constant: `kDisableLegacyIntermediateWindow`
- Condition: `BUILDFLAG(IS_WIN)`

Disable the Legacy Window which corresponds to the size of the WebContents.

## `--font-cache-shared-handle`

- Constant: `kFontCacheSharedHandle`
- Condition: `BUILDFLAG(IS_WIN)`

Switch to pass the font cache shared memory handle to the renderer. DirectWrite FontCache is shared by browser to renderers using shared memory. This switch allows us to pass the shared memory handle to the renderer.

## `--raise-timer-frequency`

- Constant: `kRaiseTimerFrequency`
- Condition: `BUILDFLAG(IS_WIN)`

Raise the timer interrupt frequency in all Chrome processes, for experimental purposes. This feature is needed because as of Windows 10 2004 the scheduling effects of changing the timer interrupt frequency are not global, and this lets us prove/disprove whether this matters. See https://crbug.com/1128917

## `--gpu2-startup-dialog`

- Constant: `kGpu2StartupDialog`
- Condition: `BUILDFLAG(IS_WIN)`

Causes the second GPU process used for gpu info collection to display a dialog on launch.

## `--audio-process-high-priority`

- Constant: `kAudioProcessHighPriority`
- Condition: `BUILDFLAG(IS_WIN)`

Use high priority for the audio process.

## `--remote-debugging-io-pipes`

- Constant: `kRemoteDebuggingIoPipes`
- Condition: `BUILDFLAG(IS_WIN)`

Pipe names for the incoming and outbound messages. Specifies pipe names for the incoming and outbound messages on the Windows platform. This is a comma separated list of two pipe handles serialized as unsigned integers, e.g. "--remote-debugging-io-pipes=3,4".

## `--ipc-dump-directory`

- Constant: `kIpcDumpDirectory`
- Condition: `defined(ENABLE_IPC_FUZZER)`

Dumps IPC messages sent from renderer processes to the browser process to the given directory. Used primarily to gather samples for IPC fuzzing.

## `--ipc-fuzzer-testcase`

- Constant: `kIpcFuzzerTestcase`
- Condition: `defined(ENABLE_IPC_FUZZER)`

Specifies the testcase used by the IPC fuzzer.

## `--disable-backgrounding-occluded-windows`

- Constant: `kDisableBackgroundingOccludedWindowsForTesting`

Disable backgrounding renders for occluded windows. Done for tests to avoid nondeterministic behavior.

## `--force-navigation-timeline-ukm-recording-for-testing`

- Constant: `kForceNavigationTimelineUkmRecordingForTesting`

Forces recording of NavigationTimeline UKM. Useful for testing NavigationTimeline UKM recording in browser tests.
