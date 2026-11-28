# All command-line switches (A–Z)

1258 switches from 97 source files. Find the switch, then open its page for the full description.

| Switch | Page | Summary |
|---|---|---|
| `--` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--3d-display-mode` | [remoting__host__base__switches](remoting__host__base__switches.md) | Executes Evaluate3dDisplayMode() function. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--?` | [remoting__host__base__switches](remoting__host__base__switches.md) | "--?" prints the usage message. |
| `--accept-empty-variations-seed-signature` | [components__variations__variations_switches](components__variations__variations_switches.md) | Accept an empty signature when loading a variations seed |
| `--accept-lang` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies Accept-Language to send to servers and expose to JavaScript via the navigator.language DOM property |
| `--accept-lang` | [headless__public__switches](headless__public__switches.md) | Specifies Accept-Language to send to servers and expose to JavaScript via the navigator.language DOM property |
| `--actor-sensitive-sites` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | Specifies a comma-separated list of SchemefulSite strings that should be treated as sensitive sites by the actor execution engine (bypassing the optimization gu |
| `--actor-trace-path` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | File or directory path where actor traces should be recorded. |
| `--adaboost` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--add-xr-appcontainer-caps` | [sandbox__policy__switches](sandbox__policy__switches.md) | Add additional capabilities to the AppContainer sandbox used for XR compositing. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--additional-private-state-token-key-commitments` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Manually sets additional Private State Tokens key commitments in the network service to the given value, which should be a JSON dictionary satisfying the requir |
| `--agent-permission-service-endpoint` | [components__password_manager__core__browser__remote_actor__remote_actor_switches](components__password_manager__core__browser__remote_actor__remote_actor_switches.md) | Overrides the default endpoint URL for the Agentic Permission Service (APS). |
| `--agent-status` | [remoting__host__base__switches](remoting__host__base__switches.md) | Reports the AI agent state to the running host via Mojo IPC. |
| `--ai-overlay-dialog-test-mode` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables test mode for the AI overlay dialog, which automatically opens the dialog on browser startup and exposes programmatic test APIs to WebUI. |
| `--allarticles` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--allow-appshim-signature-mismatch-for-tests` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Only if we're running in an unsigned build, passing this flag will allow app shims whose code signature does not match what chrome is expecting to still connect *(only if `BUILDFLAG(IS_MAC)`)* |
| `--allow-chrome-scheme-url` | [chrome__browser__headless__headless_mode_switches](chrome__browser__headless__headless_mode_switches.md) | Allows headless mode to access any URL whose scheme is chrome://. |
| `--allow-command-line-plugins` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows plugins to be loaded in the command line for testing. |
| `--allow-cross-origin-auth-prompt` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows third-party content included on a page to prompt for a HTTP basic auth username/password pair. |
| `--allow-file-access-from-files` | [content__public__common__content_switches](content__public__common__content_switches.md) | All switches in alphabetical order |
| `--allow-future-manifest-version` | [extensions__common__switches](extensions__common__switches.md) | Mute extension errors while working with new manifest version. |
| `--allow-http-background-page` | [extensions__common__switches](extensions__common__switches.md) | Allows non-https URL for background_page for hosted apps. |
| `--allow-http-screen-capture` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allow non-secure origins to use the screen capture API and the desktopCapture extension API. |
| `--allow-insecure-localhost` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables TLS/SSL errors on localhost to be ignored (no interstitial, no blocking of requests). |
| `--allow-legacy-extension-manifests` | [extensions__common__switches](extensions__common__switches.md) | Allows the browser to load extensions that lack a modern manifest when that would otherwise be forbidden. |
| `--allow-loopback-in-peer-connection` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows loopback interface to be added in network list for peer connection. |
| `--allow-ra-in-dev-mode` | [media__base__media_switches](media__base__media_switches.md) | Allows remote attestation (RA) in dev mode for testing purpose *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--allow-running-insecure-content` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | By default, an https page cannot run JavaScript, CSS or plugins from http URLs |
| `--allow-sandbox-debugging` | [sandbox__policy__switches](sandbox__policy__switches.md) | Flags owned by the service manager sandbox |
| `--allow-silent-push` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows Web Push notifications that do not show a notification. |
| `--allow-third-party-modules` | [sandbox__policy__switches](sandbox__policy__switches.md) | Allows third party modules to inject by disabling the BINARY_SIGNATURE mitigation policy on Win10+ *(only if `BUILDFLAG(IS_WIN)`)* |
| `--allow-unpacked-perfetto-extension` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows an unpacked Perfetto UI extension to be trusted. |
| `--allow-unsafe-devtools-remote-file-loading` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows DevTools frontend from remote origins to load local file:// resources |
| `--allow-video-codecs` | [headless__public__switches](headless__public__switches.md) | A comma-separated, case-insenitive list of video codecs to allow |
| `--allow-webui-test-in-component-extensions` | [extensions__common__switches](extensions__common__switches.md) | Test-only |
| `--allowlisted-extension-id` | [extensions__common__switches](extensions__common__switches.md) | Adds the given extension ID to all the permission allowlists. |
| `--alsa-input-device` | [media__base__media_switches](media__base__media_switches.md) | The Alsa device to use when opening an audio input stream. *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS) \|\| BUILDFLAG(IS_FREEBSD) \|\| \`)* |
| `--alsa-output-device` | [media__base__media_switches](media__base__media_switches.md) | The Alsa device to use when opening an audio stream. *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS) \|\| BUILDFLAG(IS_FREEBSD) \|\| \`)* |
| `--alwaystrue` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--android-entra-sso-allow-debug-brokers` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If enabled Entra SSO will accept authentication headers from a specific list of non-production Microsoft Authentication broker apps. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--android-skip-child-service-init-for-testing` | [base__base_switches](base__base_switches.md) | For testing, do not initialize child service process but also do not exit (until requested by browser). *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--angle` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--animation-duration-scale` | [ui__gfx__switches](ui__gfx__switches.md) | Scale factor to apply to every animation duration |
| `--app` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies that the associated value should be launched in "application" mode. |
| `--app-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies that the extension-app with the specified id should be launched according to its configuration. |
| `--app-launch-url-for-shortcuts-menu-item` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the launch url of an app with the specified url |
| `--app-run-on-os-login-mode` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This is used along with kAppId to indicate an app was launched during OS login, and which mode the app was launched in. |
| `--app-shim` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | A process type (switches::kProcessType) that is used by App Shim processes |
| `--app-shim` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--apps-gallery-download-url` | [extensions__common__switches](extensions__common__switches.md) | Overrides the URL that the webstore APIs download extensions from |
| `--apps-gallery-update-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the update url used by webstore extensions. |
| `--apps-gallery-url` | [extensions__common__switches](extensions__common__switches.md) | Overrides the url that the browser treats as the webstore, granting it the webstore APIs and giving it some special protections. |
| `--apps-keep-chrome-alive-in-tests` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Prevents Chrome from quitting when Chrome Apps are open. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--arcore` | [content__public__common__content_switches](content__public__common__content_switches.md) | The following are the runtimes that WebXr supports. |
| `--as-browser` | [content__public__common__content_switches](content__public__common__content_switches.md) | Flag to launch tests in the browser process. |
| `--ash-enable-software-mirroring` | [ui__display__display_switches](ui__display__display_switches.md) | Keep sorted |
| `--ash-enable-unified-desktop` | [ui__display__display_switches](ui__display__display_switches.md) | Enables unified desktop mode. *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--ash-host-window-bounds` | [ui__display__display_switches](ui__display__display_switches.md) | TODO(kylechar): This overlaps with --screen-config |
| `--attempt-form-filling-tool-skips-ui` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | Bypasses the selection of the data to be filled by the `AttemptFormFillingTool` and just picks the first suggestion for each form section |
| `--attempt-otp-filling-tool-mock-value-skips-checks` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | Supplies a mock OTP value for the `AttemptOtpFillingTool` and bypasses Google Account consent fetching, opt-in dialogs, and user confirmation dialogs, filling t |
| `--audio-buffer-size` | [media__base__media_switches](media__base__media_switches.md) | Allow users to specify a custom buffer size for debugging purpose. |
| `--audio-capturer-with-echo-cancellation` | [media__base__media_switches](media__base__media_switches.md) | Forces AudioManagerFuchsia to assume that the AudioCapturer implements echo cancellation *(only if `BUILDFLAG(IS_FUCHSIA)`)* |
| `--audio-codecs-from-edid` | [media__base__media_switches](media__base__media_switches.md) | Audio codecs supported by the HDMI sink is retrieved from the audio service process *(only if `BUILDFLAG(ENABLE_PASSTHROUGH_AUDIO_CODECS)`)* |
| `--audio-process-high-priority` | [content__public__common__content_switches](content__public__common__content_switches.md) | Use high priority for the audio process. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--auth-server-allowlist` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allowlist for Negotiate Auth servers |
| `--auth-server-allowlist` | [headless__public__switches](headless__public__switches.md) | Allowlist for Negotiate Auth servers. |
| `--auth-spnego-account-type` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Android authentication account type for SPNEGO authentication *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--auto` | [content__public__common__content_switches](content__public__common__content_switches.md) | The values the kTouchEventFeatureDetection switch may have, as in --touch-events=disabled |
| `--auto` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) |  |
| `--auto-accept-browser-signin-for-tests` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Automatically signs the user into Chrome when signing in to other Google services on the web |
| `--auto-accept-camera-and-microphone-capture` | [content__public__common__content_switches](content__public__common__content_switches.md) | Bypasses the dialog prompting the user for permission to capture cameras and microphones |
| `--auto-accept-this-tab-capture` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | These flags make Chrome auto-accept/reject requests to capture the current tab |
| `--auto-grant-captured-surface-control-prompt` | [media__base__media_switches](media__base__media_switches.md) | Skip the permission prompt for Captured Surface Control. |
| `--auto-grant-email-verification-permission-for-testing` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Automatically grants permission prompts for email verification for testing. |
| `--auto-open-devtools-for-tabs` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-open DevTools window for each tab |
| `--auto-reject-capture` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-reject requests capture a tab/window/screen. |
| `--auto-reject-this-tab-capture` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--auto-select-desktop-capture-source` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-select the provided choice when an extension asks permission to start desktop capture |
| `--auto-select-screen-capture-source` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-select any screen when an extension asks permission to start desktop capture |
| `--auto-select-tab-capture-source-by-title` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-select a tab with the provided title when the media-picker should otherwise be displayed to the user |
| `--auto-select-window-capture-source-by-title` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag makes Chrome auto-select a window with the provided title when the media-picker should otherwise be displayed to the user |
| `--autofill-api-key` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | All switches in alphabetical order |
| `--autofill-server-url` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Override the default autofill server URL with "scheme://host[:port]/prefix/". |
| `--autofill-upload-throttling-period-in-days` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | The number of days after which to reset the registry of autofill events for which an upload has been sent. |
| `--autoplay-policy` | [media__base__media_switches](media__base__media_switches.md) | Command line flag name to set the autoplay policy. |
| `--background-thread-pool-field-trial` | [base__base_switches](base__base_switches.md) | Configure the background threadpool field trial. |
| `--background-tracing-output-path` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Sets a local folder destination for tracing data |
| `--bgra` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--binary-upload-service-url` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) |  |
| `--block-new-web-contents` | [headless__public__switches](headless__public__switches.md) | If true, then all pop-ups and calls to window.open will fail. |
| `--bootstrap` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Values for the kExtensionContentVerification flag |
| `--bound-session-cookie-rotation-delay` | [chrome__browser__signin__bound_session_credentials__bound_session_switches](chrome__browser__signin__bound_session_credentials__bound_session_switches.md) | Used to add artificial delay to the cookie rotation request |
| `--bound-session-cookie-rotation-result` | [chrome__browser__signin__bound_session_credentials__bound_session_switches](chrome__browser__signin__bound_session_credentials__bound_session_switches.md) | Used to simulate the cookie rotation network request response |
| `--browser-startup-dialog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the browser process to display a dialog on launch. |
| `--browser-subprocess-path` | [content__public__common__content_switches](content__public__common__content_switches.md) | Path to the exe to run for the renderer and plugin subprocesses. |
| `--browser-test` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Browser test mode for the \|kStartStackProfiler\| switch |
| `--browser-test` | [content__public__common__content_switches](content__public__common__content_switches.md) | Tells whether the code is running browser tests (this changes the startup URL used by the content shell and also disables features that can make tests flaky [li |
| `--browser-ui-tests-verify-pixels` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes tests to attempt to verify pixel output. |
| `--bypass-account-already-used-by-another-profile-check` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If specified, allows syncing multiple profiles to the same account |
| `--campaigns-test-tag` | [components__component_updater__component_updater_switches](components__component_updater__component_updater_switches.md) | Switch to control which serving campaigns file versions to select in test cohort |
| `--canvas-2d-layers` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable in-progress canvas 2d API methods BeginLayer and EndLayer. |
| `--cardboard` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--cast-developer-certificate-path` | [components__media_router__common__providers__cast__certificate__switches](components__media_router__common__providers__cast__certificate__switches.md) | When enabled by build flags, passing this argument allows the Cast authentication utils to use a custom root developer certificate in the trust store instead of |
| `--cast-log-device-cert-chain` | [components__media_router__common__providers__cast__certificate__switches](components__media_router__common__providers__cast__certificate__switches.md) | When enabled, prints a PEM-encoded the device certificate chain at VLOG level 3. |
| `--cast-mirroring-target-playout-delay` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If enabled, overrides the target playout delay for a casting mirroring session *(only if `!BUILDFLAG(IS_ANDROID) \|\| BUILDFLAG(ENABLE_DESKTOP_ANDROID_EXTENSIONS)`)* |
| `--cast-streaming-force-disable-hardware-av1` | [media__base__media_switches](media__base__media_switches.md) | NOTE: callers should always use the free functions in /media/cast/encoding/encoding_support.h instead of accessing these features directly |
| `--cast-streaming-force-disable-hardware-h264` | [media__base__media_switches](media__base__media_switches.md) | If enabled, completely disables use of H264 hardware encoding for Cast Streaming sessions |
| `--cast-streaming-force-disable-hardware-hevc` | [media__base__media_switches](media__base__media_switches.md) | If enabled, completely disables use of HEVC hardware encoding for Cast Streaming sessions |
| `--cast-streaming-force-disable-hardware-vp8` | [media__base__media_switches](media__base__media_switches.md) | If enabled, completely disables use of VP8 hardware encoding for Cast Streaming sessions |
| `--cast-streaming-force-disable-hardware-vp9` | [media__base__media_switches](media__base__media_switches.md) | If enabled, completely disables use of VP9 hardware encoding for Cast Streaming sessions |
| `--cast-streaming-force-enable-hardware-av1` | [media__base__media_switches](media__base__media_switches.md) | If enabled, allows use of AV1 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues |
| `--cast-streaming-force-enable-hardware-h264` | [media__base__media_switches](media__base__media_switches.md) | If enabled, allows use of H264 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues |
| `--cast-streaming-force-enable-hardware-hevc` | [media__base__media_switches](media__base__media_switches.md) | If enabled, allows use of HEVC hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues |
| `--cast-streaming-force-enable-hardware-vp8` | [media__base__media_switches](media__base__media_switches.md) | If enabled, allows use of VP8 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues |
| `--cast-streaming-force-enable-hardware-vp9` | [media__base__media_switches](media__base__media_switches.md) | If enabled, allows use of VP9 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues |
| `--cast-streaming-receiver-port` | [components__cast_streaming__browser__cast_streaming_switches](components__cast_streaming__browser__cast_streaming_switches.md) | If set, allows to use a specific UDP port for Cast Streaming sessions on the receiver side |
| `--cc-layer-tree-test-long-timeout` | [cc__base__switches](cc__base__switches.md) | Increases timeout for memory checkers. |
| `--cc-layer-tree-test-no-timeout` | [cc__base__switches](cc__base__switches.md) | Test related |
| `--cc-scroll-animation-duration-in-seconds` | [cc__base__switches](cc__base__switches.md) | Controls the duration of the scroll animation curve. |
| `--change-stack-guard-on-fork` | [content__public__common__content_switches](content__public__common__content_switches.md) | After a zygote forks a new process, change the stack canary |
| `--check-accessibility-permission` | [remoting__host__base__switches](remoting__host__base__switches.md) | Command line switch to check for Accessibility permission. *(only if `BUILDFLAG(IS_APPLE)`)* |
| `--check-damage-early` | [cc__base__switches](cc__base__switches.md) | Checks damage early and aborts the frame if no damage, so that clients like Android WebView don't invalidate unnecessarily. |
| `--check-for-update-interval` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | How often (in seconds) to check for updates |
| `--check-permission` | [remoting__host__base__switches](remoting__host__base__switches.md) | NativeMessagingHost switch to check for required OS permissions and request them if necessary. *(only if `BUILDFLAG(IS_APPLE)`)* |
| `--check-screen-recording-permission` | [remoting__host__base__switches](remoting__host__base__switches.md) | Command line switch to check for Screen Recording permission. *(only if `BUILDFLAG(IS_APPLE)`)* |
| `--child-module-user-path-component` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | The user path component identifying the directory in which the staged child module resides (see child_module::GetModulesDirForUser()) *(only if `BUILDFLAG(IS_WIN)`)* |
| `--child-module-version` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | The version for the staged child module. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--cipher-suite-blacklist` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Comma-separated list of SSL cipher suites to disable. |
| `--class` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | The same as the --class argument in X applications *(only if `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`)* |
| `--clear-key-cdm-path-for-testing` | [media__base__media_switches](media__base__media_switches.md) | Specifies the path to the Clear Key CDM for testing, which is necessary to support External Clear Key key system when library CDM is enabled |
| `--clear-token-service` | [components__signin__public__base__signin_switches](components__signin__public__base__signin_switches.md) | Clears the token service before using it |
| `--code-sign-clone-cleanup` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | A process type (switches::kProcessType) that cleans up the browser's temporary code sign clone. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--code-sign-clone-cleanup` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--collect-dawn-info-eagerly` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Start the GPU process for Dawn info collection immediately after the browser starts |
| `--compensate-for-unstable-pinch-zoom` | [ui__events__event_switches](ui__events__event_switches.md) | Enable compensation for unstable pinch zoom |
| `--compile-shader-always-succeeds` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Always return success when compiling a shader |
| `--component-updater` | [components__component_updater__component_updater_switches](components__component_updater__component_updater_switches.md) | All switches in alphabetical order |
| `--component-updater-trust-tokens-component-path` | [components__component_updater__component_updater_switches](components__component_updater__component_updater_switches.md) | Optional testing override of the Trust Tokens key commitment component's path. |
| `--content-shell-hide-toolbar` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Hides toolbar from content_shell's host window. |
| `--content-shell-host-window-size` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Size for the content_shell's host window (i.e |
| `--controller` | [remoting__host__base__switches](remoting__host__base__switches.md) | Values for kProcessTypeSwitchName. |
| `--crash-dumps-dir` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | The directory Crashpad should store minidumps in |
| `--crash-dumps-dir` | [headless__public__switches](headless__public__switches.md) | The directory breakpad should store minidumps in. |
| `--crash-loop-before` | [components__crash__core__app__crash_switches](components__crash__core__app__crash_switches.md) | A time_t *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--crash-server-pipe-handle` | [remoting__host__base__switches](remoting__host__base__switches.md) | A server pipe handle used by the child process to initialize crash reporting. |
| `--crash-test` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the browser process to crash on startup. |
| `--crashpad-handler` | [components__crash__core__app__crash_switches](components__crash__core__app__crash_switches.md) | A process type (switches::kProcessType) that indicates chrome.exe or setup.exe is being launched as crashpad_handler |
| `--crashpad-handler-pid` | [components__crash__core__app__crash_switches](components__crash__core__app__crash_switches.md) | The process ID of the Crashpad handler. *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--crashpad-handler-pid` | [remoting__host__base__switches](remoting__host__base__switches.md) | *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--crashpad-handler-socket-fd` | [remoting__host__base__switches](remoting__host__base__switches.md) | Used to pass inherited Crashpad handler socket descriptor and PID. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--create-profile-email-if-not-exists` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If provided with kProfileEmail, prompts the user to create a new profile with kProfileEmail as the email address if that email is not found in any existing prof |
| `--credits` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Prints licensing information (same content as found in about:credits) and quits. |
| `--csd-debug-feature-directory` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag that can be used to write extracted CSD features to disk |
| `--csd-model-override-path` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag that can be used to override the current CSD model |
| `--custom-action-iph` | [extensions__common__switches](extensions__common__switches.md) | When the user has no extensions installed, display a custom action IPH that upon triggering, opens a new tab to the Chrome Web Store. |
| `--custom-devtools-frontend` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the http:// endpoint which will be used to serve devtools://devtools/custom/<path> Or a file:// URL to specify a custom file path to load from for dev |
| `--custom-ui-chip-iph` | [extensions__common__switches](extensions__common__switches.md) | When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip |
| `--custom-ui-chip-iph-v2` | [extensions__common__switches](extensions__common__switches.md) | When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip |
| `--custom-ui-chip-iph-v3` | [extensions__common__switches](extensions__common__switches.md) | When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip |
| `--custom-ui-plain-link-iph` | [extensions__common__switches](extensions__common__switches.md) | When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a plain t |
| `--custom_summary` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces a custom summary to be displayed below the update menu item. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--d3d-support` | [remoting__host__base__switches](remoting__host__base__switches.md) | Executes EvaluateD3D() function. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--d3d11` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--d3d11` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--d3d11-null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Special switches for "NULL"/stub driver implementations. |
| `--d3d11-warp` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--d3d11-warp-webgl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--d3d11on12` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--d3d12` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--daemon` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--data-sharing-debug-logs` | [components__data_sharing__public__switches](components__data_sharing__public__switches.md) | Switch for whether or not data sharing logs are stored at startup instead of only being stored/logged when chrome://data-sharing-internals is open. |
| `--deadline-to-synchronize-surfaces` | [components__viz__common__switches](components__viz__common__switches.md) | Keep list in alphabetical order |
| `--debug-packed-apps` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Adds debugging entries such as Inspect Element to context menus of packed apps. |
| `--debug-print` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables support to debug printing subsystem. *(only if `BUILDFLAG(ENABLE_PRINT_PREVIEW) && !defined(OFFICIAL_BUILD)`)* |
| `--default` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--default-background-color` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | The background color to be used if the page doesn't specify one |
| `--default-country-code` | [base__base_switches](base__base_switches.md) | Default country code to be used for search engine localization. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--default-trace-buffer-size-limit-in-kb` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | This is only used when we did not set buffer size in trace config and will be used for all trace sessions |
| `--DEFAULT_EEA` | [components__regional_capabilities__regional_capabilities_switches](components__regional_capabilities__regional_capabilities_switches.md) | Special value for the `kSearchEngineChoiceCountry` command-line flag |
| `--delegated-ink-renderer` | [components__viz__common__switches](components__viz__common__switches.md) | Force the use of a Delegated Ink renderer as specified by the command line argument, rather than using system details |
| `--delegated-task` | [chrome__browser__platform_experience__delegated_tasks__peh_switches](chrome__browser__platform_experience__delegated_tasks__peh_switches.md) |  |
| `--demo-app-test-tag` | [components__component_updater__component_updater_switches](components__component_updater__component_updater_switches.md) | Switch to control which serving demo mode app versions to select in test cohort |
| `--deny-permission-prompts` | [components__permissions__switches](components__permissions__switches.md) | Prevents permission prompts from appearing by denying instead of showing prompts. |
| `--desktop` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | *(only if `BUILDFLAG(IS_WIN)`)* |
| `--desktop` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--deterministic-mode` | [headless__public__switches](headless__public__switches.md) | A meta flag |
| `--device-authorization-key-server-url` | [components__webauthn__core__browser__device_authorization__device_authorization_switches](components__webauthn__core__browser__device_authorization__device_authorization_switches.md) |  |
| `--device-management-url` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Specifies the URL at which to communicate with the device management backend to fetch configuration policies and perform other device tasks. |
| `--device-scale-factor` | [content__public__common__content_switches](content__public__common__content_switches.md) | This switch contains the device scale factor passed to certain processes like renderers, etc *(only if `BUILDFLAG(IS_WIN)`)* |
| `--devtools-flags` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Passes command line parameters to the DevTools front-end. |
| `--devtools-navigation-gating-rules` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies a stringified JSON dictionary defining allowlist and blocklist pattern rules for DevTools-controlled navigations |
| `--diagnostics` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Triggers a plethora of diagnostic modes. |
| `--diagnostics-format` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Sets the output format for diagnostic modes enabled by diagnostics flag. |
| `--diagnostics-recovery` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Tells the diagnostics mode to do the requested recovery step(s). |
| `--direct-composition-video-swap-chain-format` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Used for overriding the swap chain format for direct composition SDR video overlays. |
| `--disable` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--disable-2d-canvas-clip-aa` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable antialiasing on 2d canvas clips |
| `--disable-3d-apis` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables client-visible 3D APIs, in particular WebGL |
| `--disable-accelerated-2d-canvas` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable gpu-accelerated 2d canvas. |
| `--disable-accelerated-mjpeg-decode` | [media__base__media_switches](media__base__media_switches.md) | Disable hardware acceleration of mjpeg decode for captured frame, where available. |
| `--disable-accelerated-video-decode` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables hardware acceleration of video decode, where available |
| `--disable-accelerated-video-encode` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables hardware acceleration of video encode, where available. |
| `--disable-actor-safety-checks` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | Bypasses several of the actor's safety checks, such as requiring SafeBrowsing to be enabled and the blocklist |
| `--disable-adpf` | [components__viz__common__switches](components__viz__common__switches.md) | Disables reporting of frame timing via ADPF, even if supported on the device. |
| `--disable-android-native-fence-sync-for-testing` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | On some Android emulators with software GL, ANGLE is exposing the native fence sync extension but it doesn't actually work *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-angle-features` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Disables specified comma separated ANGLE features if found. |
| `--disable-app-content-verification` | [extensions__common__switches](extensions__common__switches.md) | Whether to disable app content verification when testing changes locally on Chromebox for Meetings hardware. |
| `--disable-audio-input` | [media__base__media_switches](media__base__media_switches.md) | Forces input and output stream creation to use fake audio streams. |
| `--disable-audio-output` | [media__base__media_switches](media__base__media_switches.md) |  |
| `--disable-auto-maximize-for-tests` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables the auto maximize feature on ChromeOS so that a browser window always starts in normal state *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--disable-auto-reload` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable auto-reload of pages on top-level error. |
| `--disable-back-forward-cache` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the BackForwardCache feature. |
| `--disable-background-media-suspend` | [media__base__media_switches](media__base__media_switches.md) | Do not immediately suspend media in background tabs. |
| `--disable-background-networking` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable several subsystems which run network requests in the background |
| `--disable-background-timer-throttling` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable task throttling of timer tasks from background pages. |
| `--disable-backgrounding-occluded-windows` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable backgrounding renders for occluded windows |
| `--disable-backing-store-limit` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable limits on the number of backing stores |
| `--disable-best-effort-tasks` | [content__public__common__content_switches](content__public__common__content_switches.md) | Delays execution of TaskPriority::BEST_EFFORT tasks until shutdown. |
| `--disable-blink-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable one or more Blink runtime-enabled features |
| `--disable-breakpad` | [base__base_switches](base__base_switches.md) | Disables the crash reporting. |
| `--disable-cancel-all-touches` | [ui__events__event_switches](ui__events__event_switches.md) | Disable CancelAllTouches() function for the implementation on cancel single touches. *(only if `BUILDFLAG(IS_OZONE)`)* |
| `--disable-canvas-aa` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable antialiasing on 2d canvas. |
| `--disable-checker-imaging` | [cc__base__switches](cc__base__switches.md) | Disabled defering all image decodes to the image decode service, ignoring DecodingMode preferences specified on PaintImage. |
| `--disable-chrome-tracing-computation` | [services__resource_coordinator__memory_instrumentation__switches](services__resource_coordinator__memory_instrumentation__switches.md) | All switches in alphabetical order |
| `--disable-component-extensions-with-background-pages` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable default component extensions with background pages - useful for performance tests where these pages may interfere with perf results. |
| `--disable-component-update` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--disable-composited-antialiasing` | [cc__base__switches](cc__base__switches.md) | Disables layer-edge anti-aliasing in the compositor. |
| `--disable-cookie-encryption` | [headless__public__switches](headless__public__switches.md) | Whether cookies stored as part of user profile are encrypted. |
| `--disable-crash-on-component-extension-js-error` | [extensions__common__switches](extensions__common__switches.md) | Disables crashing on JavaScript errors in component extensions |
| `--disable-crash-reporter` | [headless__public__switches](headless__public__switches.md) | Disable crash reporter for headless |
| `--disable-crashpad-for-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables crashpad initialization for testing |
| `--disable-d3d11-warp` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Explicitly disable D3D11 WARP fallback |
| `--disable-dawn-features` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Set the Dawn features(toggles) disabled on the creation of Dawn devices. |
| `--disable-default-apps` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables installation of default apps on first run |
| `--disable-default-browser-promo` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable the default browser promo. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-dev-shm-usage` | [base__base_switches](base__base_switches.md) | The /dev/shm partition is too small in certain VM environments, causing Chrome to fail or crash (see http://crbug.com/715363) *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--disable-dinosaur-easter-egg` | [components__error_page__common__error_page_switches](components__error_page__common__error_page_switches.md) | Disables the dinosaur easter egg on the offline interstitial. |
| `--disable-direct-composition` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Disable DirectComposition. |
| `--disable-domain-blocking-for-3d-apis` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable the per-domain blocking for 3D APIs after GPU reset |
| `--disable-domain-reliability` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables Domain Reliability Monitoring. |
| `--disable-dump-without-crashing-on-angle-portability-messages` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Disable DumpWithoutCrashing on ANGLE portability messages |
| `--disable-explicit-dma-fences` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Disable explicit DMA-fences |
| `--disable-extensions` | [extensions__common__switches](extensions__common__switches.md) | Disables extensions. |
| `--disable-extensions-except` | [extensions__common__switches](extensions__common__switches.md) | Disable extensions except those specified in a comma-separated list. |
| `--disable-extensions-file-access-check` | [extensions__common__switches](extensions__common__switches.md) | Disable checking for user opt-in for extensions that want to inject script into file URLs (ie, always allow it) |
| `--disable-extensions-http-throttling` | [extensions__common__switches](extensions__common__switches.md) | Disable the net::URLRequestThrottlerManager functionality for requests originating from extensions. |
| `--disable-features` | [base__base_switches](base__base_switches.md) | Comma-separated list of feature names to disable |
| `--disable-field-trial-config` | [components__variations__variations_switches](components__variations__variations_switches.md) | Disable field trial tests configured in fieldtrial_testing_config.json. |
| `--disable-file-system` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable FileSystem API. |
| `--disable-font-subpixel-positioning` | [ui__gfx__switches](ui__gfx__switches.md) | Force disables font subpixel positioning |
| `--disable-frame-rate-limit` | [components__viz__common__switches](components__viz__common__switches.md) | Disables begin frame limiting in both cc scheduler and display scheduler |
| `--disable-gesture-requirement-for-presentation` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable user gesture requirement for presentation. |
| `--disable-gl-drawing-for-tests` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | These flags are used by the test harness code, not passed in by users |
| `--disable-gl-error-limit` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Disable the GL error log limit. |
| `--disable-gl-extensions` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Disables specified comma separated GL Extensions if found. |
| `--disable-glsl-translator` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Disable the GLSL translator. |
| `--disable-gpu` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables GPU hardware acceleration |
| `--disable-gpu-compositing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Prevent the compositor from using its GPU implementation. |
| `--disable-gpu-driver-bug-workarounds` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Disable workarounds for various GPU driver bugs. |
| `--disable-gpu-early-init` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable proactive early init of GPU process. |
| `--disable-gpu-memory-buffer-compositor-resources` | [content__public__common__content_switches](content__public__common__content_switches.md) | Do not force that all compositor resources be backed by GPU memory buffers. |
| `--disable-gpu-memory-buffer-video-frames` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable GpuMemoryBuffer backed VideoFrames. |
| `--disable-gpu-process-crash-limit` | [content__public__common__content_switches](content__public__common__content_switches.md) | For tests, to disable the limit on the number of times the GPU process may be restarted. |
| `--disable-gpu-process-for-dx12-info-collection` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Disables the non-sandboxed GPU process for DX12 info collection |
| `--disable-gpu-rasterization` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Disable GPU rasterization, i.e |
| `--disable-gpu-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables the GPU process sandbox. |
| `--disable-gpu-shader-disk-cache` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Disables the GPU shader on disk cache. |
| `--disable-gpu-vsync` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Stop the GPU from synchronizing presentation with vblank. |
| `--disable-gpu-watchdog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable the thread that crashes the GPU process if it stops responding to messages. |
| `--disable-gtk-ime` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Disables GTK IME integration. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--disable-hang-monitor` | [components__input__switches](components__input__switches.md) | Suppresses hang monitor dialogs in renderer processes |
| `--disable-hid-blocklist` | [services__device__public__cpp__hid__hid_switches](services__device__public__cpp__hid__hid_switches.md) | Disable the HID blocklist. |
| `--disable-highres-timer` | [base__base_switches](base__base_switches.md) | Disable high-resolution timer on Windows. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--disable-histogram-customizer` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable the RenderThread's HistogramCustomizer. |
| `--disable-http2-grease-settings` | [components__network_session_configurator__common__network_switches](components__network_session_configurator__common__network_switches.md) |  |
| `--disable-ignore-duplicate-navs-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the IgnoreDuplicateNavs feature |
| `--disable-in-process-stack-traces` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the in-process stack traces. |
| `--disable-infobars` | [components__infobars__core__infobars_switches](components__infobars__core__infobars_switches.md) |  |
| `--disable-input-event-activation-protection` | [ui__views__views_switches](ui__views__views_switches.md) | Disables the disregarding of potentially unintended input events such as button clicks that happen instantly after the button is shown |
| `--disable-ipc-flooding-protection` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the IPC flooding protection |
| `--disable-javascript-harmony-shipping` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable latest shipping ECMAScript 6 features. |
| `--disable-kill-after-bad-ipc` | [content__public__common__content_switches](content__public__common__content_switches.md) | Don't kill a child process when it sends a bad IPC message |
| `--disable-landlock-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables the Landlock sandbox (Android only). |
| `--disable-layer-tree-host-memory-pressure` | [cc__base__switches](cc__base__switches.md) | Switches for LayerTreeHost |
| `--disable-lazy-loading` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables lazy loading of images and frames. |
| `--disable-lazy-loading` | [headless__public__switches](headless__public__switches.md) | Disables lazy loading of images and frames. |
| `--disable-lcd-text` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables LCD text. |
| `--disable-legacy-window` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable the Legacy Window which corresponds to the size of the WebContents. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--disable-local-storage` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable LocalStorage. |
| `--disable-logging` | [content__public__common__content_switches](content__public__common__content_switches.md) | Force logging to be disabled |
| `--disable-low-end-device-mode` | [base__base_switches](base__base_switches.md) | Force disabling of low-end device mode when set. |
| `--disable-low-latency-dxva` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables using CODECAPI_AVLowLatencyMode when creating DXVA decoders. |
| `--disable-main-frame-before-activation` | [cc__base__switches](cc__base__switches.md) | Disables sending the next BeginMainFrame before the previous commit activates |
| `--disable-main-thread-name-override` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables renaming the main browser thread to "CrBrowserMain" during browser startup |
| `--disable-media-session-api` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable Media Session API *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-metal-shader-cache` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables Metal's shader cache, using the GPU sandbox to prevent access to it. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--disable-mipmap-generation` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Disables mipmap generation in Skia |
| `--disable-modal-animations` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Disable animations for showing and hiding modal dialogs. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--disable-mojo-broker` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables Mojo broker capabilities in the browser during Mojo initialization. |
| `--disable-namespace-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables usage of the namespace sandbox. |
| `--disable-new-content-rendering-timeout` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables clearing the rendering output of a renderer when it didn't commit new output for a while after a top-frame navigation. |
| `--disable-notifications` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the Web Notification and the Push APIs. |
| `--disable-nv12-dxgi-video` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the video decoder from drawing to an NV12 textures instead of ARGB. |
| `--disable-oopr-debug-crash-dump` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables debug crash dumps for OOPR. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-origin-trial-controlled-blink-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables all RuntimeEnabledFeatures that can be enabled via OriginTrials. |
| `--disable-pdf-tagging` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Do not emit tags when printing PDFs. |
| `--disable-pinch` | [components__input__switches](components__input__switches.md) | Disables compositor-accelerated touch-screen pinch gestures. |
| `--disable-platform-accessibility-integration` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the activation of browser and web accessibility via interactions with the platform's accessibility integration (i.e., a screenreader will not be able t |
| `--disable-policy-key-verification` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Disables the verification of policy signing keys *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--disable-popup-blocking` | [components__embedder_support__switches](components__embedder_support__switches.md) | Disables pop-up blocking. |
| `--disable-presentation-api` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the Presentation API. |
| `--disable-print-preview` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables print preview (For testing, and for users who don't like us |
| `--disable-prompt-on-repost` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Normally when the user attempts to navigate to a page that was the result of a post we prompt to make sure they want to |
| `--disable-pull-to-refresh-effect` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Disable the pull-to-refresh effect when vertically overscrolling content. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-pushstate-throttle` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables throttling of history.pushState/replaceState calls. |
| `--disable-reading-from-canvas` | [content__public__common__content_switches](content__public__common__content_switches.md) | Taints all <canvas> elements, regardless of origin. |
| `--disable-remote-fonts` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables remote web font support |
| `--disable-remote-playback-api` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the RemotePlayback API. |
| `--disable-renderer-accessibility` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Turns off the accessibility in the renderer. |
| `--disable-renderer-backgrounding` | [content__public__common__content_switches](content__public__common__content_switches.md) | Prevent renderer process backgrounding when set |
| `--disable-resource-scheduler` | [content__public__common__content_switches](content__public__common__content_switches.md) | Whether the ResourceScheduler is disabled |
| `--disable-rtc-smoothness-algorithm` | [media__base__media_switches](media__base__media_switches.md) | Disables the new rendering algorithm for webrtc, which is designed to improve the rendering smoothness. |
| `--disable-screen-orientation-lock` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable the locking feature of the screen orientation API. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-scroll-to-text-fragment` | [content__public__common__content_switches](content__public__common__content_switches.md) | This switch disables the ScrollToTextFragment feature. |
| `--disable-search-engine-choice-screen` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) | Disable the search engine choice screen for testing / autmation. |
| `--disable-seccomp-filter-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disable the seccomp filter sandbox (seccomp-bpf) (Linux only). |
| `--disable-setuid-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disable the setuid sandbox (Linux only). |
| `--disable-shader-name-hashing` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Turn off user-defined name hashing in shaders. |
| `--disable-shared-dictionary-storage-cleanup-for-testing` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | The switch to disable the shared dictionary storage clean up task |
| `--disable-shared-workers` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable shared workers. |
| `--disable-signin-promo-on-avatar-pill-for-testing` | [components__signin__public__base__signin_switches](components__signin__public__base__signin_switches.md) | Disables the sign-in promo on the avatar pill for tests by default, as it has impact on the startup behavior *(only if `BUILDFLAG(ENABLE_DICE_SUPPORT)`)* |
| `--disable-site-isolation-for-policy` | [content__public__common__content_switches](content__public__common__content_switches.md) | Just like kDisableSiteIsolation, but doesn't show the "stability and security will suffer" butter bar warning. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-site-isolation-trials` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables site isolation |
| `--disable-skia-graphite` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Force disabling/enabling Skia Graphite |
| `--disable-skia-graphite-precompilation` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Force disabling/enabling Skia Graphite's Pipeline Precompilation |
| `--disable-skia-runtime-opts` | [content__public__common__content_switches](content__public__common__content_switches.md) | Do not use runtime-detected high-end CPU optimizations in Skia |
| `--disable-smooth-scrolling` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable smooth scrolling for testing. |
| `--disable-software-compositing-fallback` | [content__public__common__content_switches](content__public__common__content_switches.md) | For tests, to disable falling back to software compositing if the GPU Process has crashed, and reached the GPU Process crash limit. |
| `--disable-software-rasterizer` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the use of a 3D software rasterizer. |
| `--disable-speech-api` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the Web Speech API (both speech recognition and synthesis). |
| `--disable-speech-synthesis-api` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the speech synthesis part of Web Speech API. |
| `--disable-stack-profiler` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable stack profiling |
| `--disable-sync` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | Disables syncing browser data to a Google Account. |
| `--disable-sync-invalidation-optimizations` | [components__browser_sync__browser_sync_switches](components__browser_sync__browser_sync_switches.md) | Disables the optimizations flags in Commit requests for sync invalidations |
| `--disable-system-font-check` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Disables the check for the system font when specified. |
| `--disable-threaded-animation` | [cc__base__switches](cc__base__switches.md) | Switches for the renderer compositor only. |
| `--disable-threaded-compositing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable multithreaded GPU compositing of web content. |
| `--disable-timeouts-for-profiling` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable timeouts that may cause the browser to die when running slowly *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--disable-updater-scheduler` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disable startup of the updater process. |
| `--disable-usb-keyboard-detect` | [base__base_switches](base__base_switches.md) | Disables the USB keyboard detection for blocking the OSK on Windows. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--disable-v8-idle-tasks` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable V8 idle tasks. |
| `--disable-variations-safe-mode` | [components__variations__variations_switches](components__variations__variations_switches.md) | Disable variations safe mode. |
| `--disable-variations-seed-fetch` | [components__variations__variations_switches](components__variations__variations_switches.md) | Disable fetching of variations seed from the server for testing. |
| `--disable-variations-seed-fetch-throttling` | [components__variations__variations_switches](components__variations__variations_switches.md) | Disables throttling for fetching the variations seed on mobile platforms |
| `--disable-video-capture-use-gpu-memory-buffer` | [media__capture__capture_switches](media__capture__capture_switches.md) | This is for the same feature controlled by kVideoCaptureUseGpuMemoryBuffer |
| `--disable-vsync-for-tests` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--disable-vulkan-fallback-to-gl-for-testing` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Disables falling back to GL based hardware rendering if initializing Vulkan fails |
| `--disable-vulkan-surface` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Disables VK_KHR_surface extension |
| `--disable-wayland-ime` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Disable wayland input method editor. |
| `--disable-web-security` | [content__public__common__content_switches](content__public__common__content_switches.md) | Don't enforce the same-origin policy; meant for website testing only |
| `--disable-webgl` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable all versions of WebGL. |
| `--disable-webgl2` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable WebGL2. |
| `--disable-webnn-compiler-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables the WebNN compiler process sandbox. |
| `--disable-webrtc-encryption` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables encryption of RTP Media for WebRTC |
| `--disable-yuv-image-decoding` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disable YUV image decoding for those formats and cases where it's supported |
| `--disabled` | [content__public__common__content_switches](content__public__common__content_switches.md) | disabled: touch events are disabled. |
| `--disabled` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) |  |
| `--disabled` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--disallow-non-exact-resource-reuse` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Test related |
| `--disallow-v8-feature-flag-overrides` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disallows overriding of v8 feature flags. |
| `--discoverability` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--disk-cache-dir` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Use a specific disk cache location, rather than one derived from the UserDatadir. |
| `--disk-cache-dir` | [headless__public__switches](headless__public__switches.md) | Use a specific disk cache location, rather than one derived from the UserDatadir. |
| `--disk-cache-size` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces the maximum disk space to be used by the disk cache, in bytes. |
| `--display` | [ui__gfx__switches](ui__gfx__switches.md) | Which X11 display to connect to *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--display-properties` | [ui__display__display_switches](ui__display__display_switches.md) | Additional display properties are provided through this switch that are beyond what is available via EDID encoded as JSON *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--dmg-device` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | When switches::kProcessType is switches::kRelauncherProcess, if this switch is also present, the relauncher process will unmount and eject a mounted disk image  *(only if `BUILDFLAG(IS_MAC)`)* |
| `--do-not-create-nsapp-for-tests` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Skips initializing the shares NSApplication instance in ChromeTestSuite. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--do-not-de-elevate` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Do not de-elevate the browser on launch |
| `--document-user-activation-required` | [media__base__media_switches](media__base__media_switches.md) | Autoplay policy that requires a document user activation. |
| `--dom-automation` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies if the \|DOMAutomationController\| needs to be bound in the renderer |
| `--double-buffer-compositing` | [components__viz__common__switches](components__viz__common__switches.md) | Sets the number of max pending frames in the GL buffer queue to 1. |
| `--draw-view-bounds-rects` | [ui__views__views_switches](ui__views__views_switches.md) | Draws a semitransparent red rect to indicate the bounds of each view |
| `--drm-virtual-connector-is-external` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Treats DRM virtual connector as external to enable display mode change in VM. |
| `--dump-browser-histograms` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Requests that a running browser process dump its collected histograms to a given file |
| `--dump-compositor-frame` | [cc__base__switches](cc__base__switches.md) | Debug data dump |
| `--dump-dom` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Print the serialized DOM (doctype + document.documentElement.outerHTML) to stdout. |
| `--edge-touch-filtering` | [ui__events__event_switches](ui__events__event_switches.md) | Tells Chrome to do edge touch filtering *(only if `BUILDFLAG(IS_OZONE)`)* |
| `--EEA_ALL` | [components__regional_capabilities__regional_capabilities_switches](components__regional_capabilities__regional_capabilities_switches.md) | Special value for the `kSearchEngineChoiceCountry` command-line flag |
| `--egl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | The GL implementation names that can be passed to --use-gl. |
| `--elevate` | [remoting__host__base__switches](remoting__host__base__switches.md) | "--elevate=<binary>" requests \|binary\| to be launched elevated (possibly causing a UAC prompt). |
| `--embedded-extension-options` | [extensions__common__switches](extensions__common__switches.md) | Enables extension options to be embedded in chrome://extensions rather than a new tab. |
| `--enable` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--enable-actor-journal-vlog` | [components__actor__core__actor_switches](components__actor__core__actor_switches.md) | Forces logging of the actor aggregated journal events in VLOG(1) |
| `--enable-adaptive-selection-handle-orientation` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable inverting of selection handles so that they are not clipped by the viewport boundaries. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--enable-aggressive-domstorage-flushing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable the aggressive flushing of DOM Storage to minimize data loss. |
| `--enable-angle-features` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | ANGLE features are defined per-backend in third_party/angle/include/platform Enables specified comma separated ANGLE features if found. |
| `--enable-audio-debug-recordings-from-extension` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If the WebRTC logging private API is active, enables audio debug recordings. |
| `--enable-auto-reload` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enable auto-reload of pages on top-level error. |
| `--enable-automation` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable indication that browser is controlled by automation. |
| `--enable-background-tracing` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Enables background tracing by passing a scenarios config as an argument |
| `--enable-begin-frame-control` | [headless__public__switches](headless__public__switches.md) | Whether or not begin frames should be issued over DevToolsProtocol (experimental). |
| `--enable-benchmarking` | [base__base_switches](base__base_switches.md) | See flag_descriptions.cc for more details. |
| `--enable-benchmarking-api` | [components__variations__variations_switches](components__variations__variations_switches.md) | Enables the benchmarking JavaScript API. |
| `--enable-bfcache` | [headless__public__switches](headless__public__switches.md) | Enable Back Forward Cache support |
| `--enable-ble-advertising-in-apps` | [extensions__common__switches](extensions__common__switches.md) | Enable BLE Advertising in apps. |
| `--enable-blink-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable one or more Blink runtime-enabled features |
| `--enable-blink-test-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables blink runtime enabled features with status:"test" or status:"experimental", which are enabled when running web tests. |
| `--enable-bookmark-undo` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables the multi-level undo system for bookmarks. |
| `--enable-caret-browsing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable native caret browsing, in which a moveable cursor is placed on a web page, allowing a user to select and navigate through non-editable text using just a  |
| `--enable-chrome-browser-cloud-management` | [components__enterprise__browser__enterprise_switches](components__enterprise__browser__enterprise_switches.md) | Enables the Chrome Browser Cloud Management integration on Chromium builds *(only if `!BUILDFLAG(IS_CHROMEOS)`)* |
| `--enable-component-uninstall` | [components__component_updater__component_updater_switches](components__component_updater__component_updater_switches.md) | Allows uninstalling components from the chrome://components page. |
| `--enable-corp-messaging` | [remoting__host__base__switches](remoting__host__base__switches.md) | Indicates whether Corp Messaging should be enabled for signaling. |
| `--enable-crash-reporter` | [base__base_switches](base__base_switches.md) | Indicates that crash reporting should be enabled |
| `--enable-crash-reporter` | [headless__public__switches](headless__public__switches.md) | Enable crash reporter for headless. |
| `--enable-crash-reporter-for-testing` | [base__base_switches](base__base_switches.md) | Used for turning on Breakpad crash reporting in a debug environment where crash reporting is typically compiled but disabled. *(only if `BUILDFLAG(IS_POSIX)`)* |
| `--enable-crx-hash-check` | [extensions__common__switches](extensions__common__switches.md) | Enable package hash check: the .crx file sha256 hash sum should be equal to the one received from update manifest. |
| `--enable-dawn-backend-validation` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enable validation layers in Dawn backends. |
| `--enable-dawn-features` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Set the Dawn features(toggles) enabled on the creation of Dawn devices. |
| `--enable-devtools-pwa-handler` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If enabled, DevTools will allow creating pwa_handler, to enable executing CDP methods (i.e *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--enable-dinosaur-easter-egg-alt-images` | [components__error_page__common__error_page_switches](components__error_page__common__error_page_switches.md) | Enable the dinosaur easter egg alternative images. |
| `--enable-direct-composition-video-overlays` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Enable DirectComposition video overlays even if hardware doesn't support it. |
| `--enable-distillability-service` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--enable-dom-distiller` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--enable-domain-reliability` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables Domain Reliability Monitoring. |
| `--enable-edge-to-edge-debug-layers` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Enables drawing debug layers for edge-to-edge components to highlight the system insets those components are drawing into *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--enable-encryption-selection` | [components__password_manager__core__browser__password_manager_switches](components__password_manager__core__browser__password_manager_switches.md) | Enables the feature of allowing the user to disable the backend via a setting. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--enable-exclusive-audio` | [media__base__media_switches](media__base__media_switches.md) | Use exclusive mode audio streaming for Windows Vista and higher *(only if `BUILDFLAG(IS_WIN)`)* |
| `--enable-experimental-accessibility-autoclick` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Shows additional automatic click features that haven't launched yet. |
| `--enable-experimental-accessibility-labels-debugging` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Enables support for visually debugging the accessibility labels feature, which provides images descriptions for screen reader users. |
| `--enable-experimental-accessibility-switch-access-text` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Enables in progress Switch Access features for text input. |
| `--enable-experimental-cookie-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Flag that turns on a group of experimental/newly added cookie-related features together, as a convenience for e.g |
| `--enable-experimental-extension-apis` | [extensions__common__switches](extensions__common__switches.md) | Enables extension APIs that are in development. |
| `--enable-experimental-web-platform-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables Web Platform features that are in development. |
| `--enable-experimental-webassembly-features` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables experimental WebAssembly features. |
| `--enable-extension-activity-log-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--enable-extension-activity-logging` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables logging for extension activity. |
| `--enable-extension-actor-api` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Name of the command line flag to allow the experimental actor API. |
| `--enable-extension-ai-data-collection` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Name of the command line flag to allow the ai data collection extension API. |
| `--enable-features` | [base__base_switches](base__base_switches.md) | Comma-separated list of feature names to enable |
| `--enable-field-trial-config` | [components__variations__variations_switches](components__variations__variations_switches.md) | Enable field trial tests configured in fieldtrial_testing_config.json |
| `--enable-finch-seed-delta-compression` | [components__variations__variations_switches](components__variations__variations_switches.md) | Enables delta-compression when fetching a new seed via the "first run" code path on Android. |
| `--enable-gpu` | [chrome__browser__headless__headless_mode_switches](chrome__browser__headless__headless_mode_switches.md) | Enable hardware GPU support |
| `--enable-gpu` | [headless__public__switches](headless__public__switches.md) | Enable hardware GPU support |
| `--enable-gpu-benchmarking` | [cc__base__switches](cc__base__switches.md) | Switches for both the renderer and ui compositors |
| `--enable-gpu-blocked-time` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enables measures of how long GPU Main Thread was blocked between SwapBuffers |
| `--enable-gpu-client-logging` | [gpu__command_buffer__client__gpu_switches](gpu__command_buffer__client__gpu_switches.md) | Enable GPU client logging. |
| `--enable-gpu-client-tracing` | [gpu__command_buffer__client__gpu_switches](gpu__command_buffer__client__gpu_switches.md) | Enables TRACE for GL calls in the renderer. |
| `--enable-gpu-command-logging` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Turn on Logging GPU commands. |
| `--enable-gpu-debugging` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Turn on Calling GL Error after every command. |
| `--enable-gpu-driver-debug-logging` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Enable logging of GPU driver debug messages. |
| `--enable-gpu-main-time-keeper-metrics` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enables ThreadControllerWithMessagePumpImpl's TimeKeeper UMA metrics using CrGpuMain as suffix. |
| `--enable-gpu-memory-buffer-video-frames` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable GpuMemoryBuffer backed VideoFrames. |
| `--enable-gpu-rasterization` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Allow heuristics to determine when a layer tile should be drawn with the Skia GPU backend |
| `--enable-gpu-service-logging` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Enable GPU service logging |
| `--enable-gpu-service-logging` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Turns on GPU logging (debug build only). |
| `--enable-gpu-service-tracing` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Turns on calling TRACE for every GL call. |
| `--enable-hangout-services-extension-for-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Force enabling HangoutServicesExtension. |
| `--enable-hardware-overlays` | [components__viz__common__switches](components__viz__common__switches.md) | Enable compositing individual elements via hardware overlays when permitted by device |
| `--enable-idle-tracing` | [base__base_switches](base__base_switches.md) | Adds additional thread idle time information into the trace event output. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--enable-isolated-web-apps-in-renderer` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables Isolated Web Apps (IWAs) in a renderer process |
| `--enable-lcd-text` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables LCD text. |
| `--enable-live-caption-pref-for-testing` | [media__base__media_switches](media__base__media_switches.md) | Sets the default value for the kLiveCaptionEnabled preference to true. |
| `--enable-local-sync-backend` | [components__browser_sync__browser_sync_switches](components__browser_sync__browser_sync_switches.md) | Enabled the local sync backend implemented by the LoopbackServer. |
| `--enable-logging` | [content__public__common__content_switches](content__public__common__content_switches.md) | Force logging to be enabled |
| `--enable-longpress-drag-selection` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable drag manipulation of longpress-triggered text selections. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--enable-low-end-device-mode` | [base__base_switches](base__base_switches.md) | Force low-end device mode when set. |
| `--enable-mac-accessibility-api-migration` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Enables the switchover to the newer NSAccessibility property-based API. |
| `--enable-magnifier-debug-draw-rect` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Enables debug feature for drawing rectangle around magnified region, without zooming in. |
| `--enable-main-frame-before-activation` | [cc__base__switches](cc__base__switches.md) | Enables sending the next BeginMainFrame before the previous commit activates. |
| `--enable-microphone-mute-switch-device` | [ui__events__event_switches](ui__events__event_switches.md) | Enables logic to detect microphone mute switch device state, which disables internal audio input when toggled. *(only if `BUILDFLAG(IS_OZONE)`)* |
| `--enable-native-gpu-memory-buffers` | [ui__gfx__switches](ui__gfx__switches.md) | Enable native CPU-mappable GPU memory buffer support on Linux. |
| `--enable-net-benchmarking` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables the network-related benchmarking extensions. |
| `--enable-network-information-downlink-max` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables the type, downlinkMax attributes of the NetInfo API |
| `--enable-ntp-search-engine-country-detection` | [components__ntp_tiles__switches](components__ntp_tiles__switches.md) | Enables using the default search engine country to show country specific popular sites on the NTP. |
| `--enable-page-content-annotations-logging` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) |  |
| `--enable-pixel-output-in-tests` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) | Forces tests to produce pixel output when they normally wouldn't. |
| `--enable-plugin-placeholder-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables testing features of the Plugin Placeholder |
| `--enable-potentially-annoying-security-features` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables a number of potentially annoying security features (strict mixed content mode, powerful feature restrictions, etc.) |
| `--enable-precise-memory-info` | [content__public__common__content_switches](content__public__common__content_switches.md) | Make the values returned to window.performance.memory more granular and more up to date in shared worker |
| `--enable-primary-node-access-for-vkms-testing` | [media__base__media_switches](media__base__media_switches.md) | This is needed for V4L2/VAAPI testing using VISL or libfake (virtual drivers) on cros VMs *(only if `BUILDFLAG(USE_V4L2_CODEC) \|\| BUILDFLAG(USE_VAAPI)`)* |
| `--enable-privacy-sandbox-ads-apis` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables Privacy Sandbox APIs: Attribution Reporting, Fledge, Topics, Fenced Frames, Shared Storage, Private Aggregation, and their associated features. |
| `--enable-profile-shortcut-manager` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Force-enables the profile shortcut manager *(only if `BUILDFLAG(IS_WIN)`)* |
| `--enable-protected-video-buffers` | [media__base__media_switches](media__base__media_switches.md) | Enables protected buffers for encrypted video streams. *(only if `BUILDFLAG(IS_FUCHSIA)`)* |
| `--enable-sandbox-logging` | [sandbox__policy__switches](sandbox__policy__switches.md) | Cause the OS X sandbox write to syslog every time an access to a resource is denied by the sandbox. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--enable-scaling-clipped-images` | [cc__base__switches](cc__base__switches.md) | Allows scaling clipped images in GpuImageDecodeCache |
| `--enable-service-binary-launcher` | [content__public__common__content_switches](content__public__common__content_switches.md) | If true the ServiceProcessLauncher is used to launch services |
| `--enable-service-manager-tracing` | [services__service_manager__switches](services__service_manager__switches.md) | All switches in alphabetical order |
| `--enable-sgi-video-sync` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Enable use of the SGI_video_sync extension, which can have driver/sandbox/window manager compatibility issues. |
| `--enable-share-button-unbranded` | [components__password_manager__core__browser__password_manager_switches](components__password_manager__core__browser__password_manager_switches.md) | Enables Password Sharing button in password details UI in settings when running unbranded builds. |
| `--enable-skia-benchmarking` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables the Skia benchmarking extension. |
| `--enable-skia-graphite` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--enable-skia-graphite-precompilation` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--enable-smooth-scrolling` | [content__public__common__content_switches](content__public__common__content_switches.md) | On platforms that support it, enables smooth scroll animation. |
| `--enable-spatial-navigation` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable spatial navigation |
| `--enable-speech-dispatcher` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows sending text-to-speech requests to speech-dispatcher, a common Linux speech service *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--enable-stats-collection-bindings` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies if the \|StatsCollectionController\| needs to be bound in the renderer |
| `--enable-strict-mixed-content-checking` | [content__public__common__content_switches](content__public__common__content_switches.md) | Blocks all insecure requests from secure contexts, and prevents the user from overriding that decision. |
| `--enable-threaded-texture-mailboxes` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Simulates shared textures when share groups are not available |
| `--enable-trace-app-source` | [extensions__common__switches](extensions__common__switches.md) | Pass launch source to platform apps. |
| `--enable-tracing` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) |  |
| `--enable-tracing-format` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) |  |
| `--enable-tracing-fraction` | [content__public__common__content_switches](content__public__common__content_switches.md) | When specified along with a value in the range (0,1] will --enable-tracing for (roughly) that percentage of tests being run |
| `--enable-tracing-output` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Similar to the flag above, with the following differences: - A more detailed basename will be generated |
| `--enable-ttc-test-api` | [chrome__browser__ttc__core__switches](chrome__browser__ttc__core__switches.md) | Enables the TTC evaluation test harness API on eval harness WebUI. |
| `--enable-ui-devtools` | [components__ui_devtools__switches](components__ui_devtools__switches.md) | Enables DevTools server for UI (mus, ash, etc) |
| `--enable-unsafe-swiftshader` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Allow usage of SwiftShader for WebGL |
| `--enable-unsafe-webgpu` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--enable-user-metrics` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enable user metrics from within the installer. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--enable-usermedia-screen-capturing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable screen capturing support for MediaStream API. |
| `--enable-viewport` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables the use of the @viewport CSS rule, which allows pages to control aspects of their own layout |
| `--enable-vtune-support` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable the Vtune profiler support. |
| `--enable-vulkan-protected-memory` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enables using protected memory for vulkan resources. |
| `--enable-wayland-ime` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Try to enable wayland input method editor. |
| `--enable-webgl-developer-extensions` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables WebGL developer extensions which are not generally exposed to the web platform. |
| `--enable-webgl-draft-extensions` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enables WebGL draft extensions (not yet approved by the community) |
| `--enable-webgpu-developer-features` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enables WebGPU developer features which are not generally exposed to the web platform. |
| `--enable-wtmpdb` | [remoting__host__base__switches](remoting__host__base__switches.md) | Used to record client sessions to wtmpd. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--enabled` | [content__public__common__content_switches](content__public__common__content_switches.md) | enabled: touch events always enabled. |
| `--enabled` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) |  |
| `--encrypted-reporting-url` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Specifies the URL at which to upload encrypted reports. |
| `--enforce` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--enforce-gl-minimums` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Enforce GL minimums. |
| `--enforce_strict` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--ensure-forced-color-profile` | [ui__display__display_switches](ui__display__display_switches.md) | Crash the browser at startup if the display's color profile does not match the forced color profile |
| `--enterprise-signin-dialog-behavior-for-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the behavior of the sign-in dialog when creating a new profile for an enterprise account *(only if `BUILDFLAG(CHROME_FOR_TESTING)`)* |
| `--evaluate-type` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--evaluate_capability` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--experimental-ai-stable-channel` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows experimental ai extension APIs to be used in stable channel |
| `--explicitly-allowed-ports` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Allows overriding the list of restricted ports by passing a comma-separated list of port numbers. |
| `--explicitly-allowed-ports` | [headless__public__switches](headless__public__switches.md) | Allows overriding the list of restricted ports by passing a comma-separated list of port numbers. |
| `--export-ukm-logs-to-file` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Enables the observing of all UKM logs created during the session and automatically exports them to the passed file path on shutdown (the file is created if it d |
| `--export-uma-logs-to-file` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Enables the observing of all UMA logs created during the session and automatically exports them to the passed file path on shutdown (the file is created if it d |
| `--expose-internals-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Exposes the window.internals object in JavaScript for testing. |
| `--extension-content-verification` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Name of the command line flag to force content verification to be on in one of various modes. |
| `--extension-force-channel` | [chrome__browser__extensions__updater__extension_updater_switches](chrome__browser__extensions__updater__extension_updater_switches.md) | Forces a chrome channel during update requests. |
| `--extension-process` | [extensions__common__switches](extensions__common__switches.md) | Marks a renderer as extension process. |
| `--extension-test-api-on-web-pages` | [extensions__common__switches](extensions__common__switches.md) | Allow the chrome.test API to be exposed on web page contexts for testing |
| `--extension-test-api-standardized-behavior` | [extensions__common__switches](extensions__common__switches.md) | Forces the `chrome.test` API to use standardized behavior matching the `browser.test` proposal. |
| `--extension-updater-test-request` | [chrome__browser__extensions__updater__extension_updater_switches](chrome__browser__extensions__updater__extension_updater_switches.md) | Add "testrequest" to the update check request. |
| `--extension-zero-state-iph-variant` | [extensions__common__switches](extensions__common__switches.md) | The feature parameter name that controls the variant of IPH shown when the user has no extensions installed. |
| `--extensions-install-verification` | [extensions__common__switches](extensions__common__switches.md) | Turns on extension install verification if it would not otherwise have been turned on. |
| `--extensions-not-webstore` | [extensions__common__switches](extensions__common__switches.md) | Specifies a comma-separated list of extension ids that should be forced to be treated as not from the webstore when doing install verification. |
| `--extensions-on-chrome-urls` | [extensions__common__switches](extensions__common__switches.md) | Enables extensions running scripts on chrome:// URLs |
| `--extensions-on-extension-urls` | [extensions__common__switches](extensions__common__switches.md) | Enables extensions running scripts on chrome-extension:// URLs |
| `--extra-search-query-params` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) | Additional query params to insert in the search and instant URLs |
| `--fail-audio-stream-creation` | [media__base__media_switches](media__base__media_switches.md) | Causes the AudioManager to fail creating audio streams |
| `--fake-background-blur-toggle-period` | [media__base__media_switches](media__base__media_switches.md) | Inserts fake background blur state into `VideoFrameMetadata` |
| `--fake-variations-channel` | [components__variations__variations_switches](components__variations__variations_switches.md) | Fakes the channel of the browser for purposes of Variations filtering |
| `--fake-variations-platform` | [components__variations__variations_switches](components__variations__variations_switches.md) | Fakes the platform of the browser for variations seed fetching and field trial filtering |
| `--fake-vsync-rate` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Report a fake vsync rate (in Hz) instead of the real display refresh rate, skipping the wait on the real hardware vsync signal *(only if `BUILDFLAG(IS_WIN)`)* |
| `--fallback` | [device__vr__public__cpp__switches](device__vr__public__cpp__switches.md) |  |
| `--feedback-server` | [components__feedback__feedback_switches](components__feedback__feedback_switches.md) | All switches in alphabetical order |
| `--field-trial-handle` | [base__base_switches](base__base_switches.md) | Handle to the shared memory segment containing field trial state that is to be shared between processes |
| `--file-storage-server-upload-url` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Specifies the URL at which to communicate with File Storage Server (go/crosman-file-storage-server) to upload log and support packet files. |
| `--file-url-path-alias` | [content__public__common__content_switches](content__public__common__content_switches.md) | Define an alias root directory which is replaced with the replacement string in file URLs |
| `--file_chooser` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--flag-switches-begin` | [components__webui__flags__flags_ui_switches](components__webui__flags__flags_ui_switches.md) | These two flags are added around the switches about:flags adds to the command line |
| `--flag-switches-end` | [components__webui__flags__flags_ui_switches](components__webui__flags__flags_ui_switches.md) |  |
| `--focus` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Activates an existing tab or app window by URL or app id before creating anything new |
| `--focus-result-file` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies a file path to write JSON focus result information. |
| `--font-cache-shared-handle` | [content__public__common__content_switches](content__public__common__content_switches.md) | Switch to pass the font cache shared memory handle to the renderer *(only if `BUILDFLAG(IS_WIN)`)* |
| `--font-render-hinting` | [headless__public__switches](headless__public__switches.md) | Sets font render hinting when running headless, affects Skia rendering and whether glyph subpixel positioning is enabled |
| `--force-app-mode` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the variation of Zero State extensions toolbar recommendation to show |
| `--force-browser-crash-on-gpu-crash` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Crash Chrome if GPU process crashes |
| `--force-caption-style` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Forces the caption style for WebVTT captions. |
| `--force-color-profile` | [ui__display__display_switches](ui__display__display_switches.md) | Force all monitors to be treated as though they have the specified color profile |
| `--force-dark-mode` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Forces dark mode in UI for platforms that support it. |
| `--force-desktop-android` | [base__base_switches](base__base_switches.md) | Forces the DeviceInfo.isDesktop() check to return true *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-device-ownership` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-device-scale-factor` | [ui__display__display_switches](ui__display__display_switches.md) | Overrides the device scale factor for the browser UI and the contents. |
| `--force-disable-variation-ids` | [components__variations__variations_switches](components__variations__variations_switches.md) | Forces to remove Chrome Variation Ids from being sent in X-Client-Data header, specified as a 64-bit encoded list of numeric experiment ids |
| `--force-effective-connection-type` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Forces Network Quality Estimator (NQE) to return a specific effective connection type. |
| `--force-enable-metrics-reporting` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Forces metrics reporting to be enabled |
| `--force-enable-night-mode` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces the night mode to be enabled. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-fieldtrial-params` | [components__variations__variations_switches](components__variations__variations_switches.md) | This option can be used to force parameters of field trials when testing changes locally |
| `--force-fieldtrials` | [base__base_switches](base__base_switches.md) | This option can be used to force field trials when testing changes locally |
| `--force-first-run` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Displays the First Run experience when the browser is started, regardless of whether or not it's actually the First Run (this overrides kNoFirstRun). |
| `--force-fre-default-browser-step` | [components__signin__public__base__signin_switches](components__signin__public__base__signin_switches.md) | Force enable the default browser step in the first run experience on Desktop. *(only if `BUILDFLAG(ENABLE_DICE_SUPPORT)`)* |
| `--force-fre-feature-showcase-steps` | [components__signin__public__base__signin_switches](components__signin__public__base__signin_switches.md) | Overrides the eligible steps in the Feature Showcase step of the first run experience *(only if `BUILDFLAG(ENABLE_DICE_SUPPORT)`)* |
| `--force-gpu-mem-discardable-limit-mb` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Sets the maximum GPU memory to use for discardable caches. |
| `--force-high-contrast` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Forces high-contrast mode for native UI and web content, regardless of system settings. |
| `--force-high-performance-gpu` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--force-high-res-timeticks` | [base__base_switches](base__base_switches.md) | Forces the use of QPC for TimeTicks even if cpuid doesn't report the presence of an invariant TSC. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--force-max-texture-size` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Sets the maximum texture size in pixels. |
| `--force-msbb-setting-on-for-ukm` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Forces MSBB setting to be on for UKM recording |
| `--force-navigation-timeline-ukm-recording-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Forces recording of NavigationTimeline UKM |
| `--force-new-browsing-instance` | [headless__public__switches](headless__public__switches.md) | Forces each navigation to use a new BrowsingInstance. |
| `--force-online-connection-state-for-indicator` | [content__public__common__content_switches](content__public__common__content_switches.md) | Prevent the offline indicator from showing. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-permission-policy-unload-default-enabled` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | If set, the unload event cannot be disabled by default by Permissions-Policy. |
| `--force-prefers-no-reduced-motion` | [ui__gfx__switches](ui__gfx__switches.md) | Forces whether the user desires no reduced motion, regardless of system settings. |
| `--force-prefers-reduced-motion` | [ui__gfx__switches](ui__gfx__switches.md) | Forces whether the user desires reduced motion, regardless of system settings. |
| `--force-presentation-receiver-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | This forces pages to be loaded as presentation receivers |
| `--force-protected-video-output-buffers` | [media__base__media_switches](media__base__media_switches.md) | Forces protected memory for all output video buffers generated by FuchsiaVideoDecoder, including unencrypted streams *(only if `BUILDFLAG(IS_FUCHSIA)`)* |
| `--force-raster-color-profile` | [ui__display__display_switches](ui__display__display_switches.md) | Force rastering to take place in the specified color profile |
| `--force-renderer-accessibility` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | Force renderer accessibility to be on instead of enabling it on demand when a screen reader is detected |
| `--force-reporting-destination-attested` | [headless__public__switches](headless__public__switches.md) | Force reporting destination attested for headless shell. |
| `--force-search-engine-choice-screen` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) | Force-enable showing the search engine choice screen for testing regardless of region or choice already having been made. |
| `--force-separate-egl-display-for-webgl-testing` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Force the use of a separate EGL display for WebGL contexts |
| `--force-show-update-menu-badge` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces the update menu badge to show. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-text-direction` | [base__i18n__base_i18n_switches](base__i18n__base_i18n_switches.md) | Force the text rendering to a specific direction |
| `--force-ui-direction` | [base__i18n__base_i18n_switches](base__i18n__base_i18n_switches.md) | Force the UI to a specific direction |
| `--force-update-menu-type` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces the update menu type to a specific type. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--force-variation-ids` | [components__variations__variations_switches](components__variations__variations_switches.md) | Forces additional Chrome Variation Ids that will be sent in X-Client-Data header, specified as a 64-bit encoded list of numeric experiment ids |
| `--force-video-overlays` | [media__base__media_switches](media__base__media_switches.md) | Force media player using SurfaceView instead of SurfaceTexture on Android |
| `--force-wave-audio` | [media__base__media_switches](media__base__media_switches.md) | Use Windows WaveOut/In audio API even if Core Audio is supported. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--force-webgpu-compat` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Force all WebGPU content to run in WebGPU Compatibility mode. |
| `--force-webrtc-ip-handling-policy` | [content__public__common__content_switches](content__public__common__content_switches.md) | Override WebRTC IP handling policy to mimic the behavior when WebRTC IP handling policy is specified in Preferences. |
| `--force-webxr-runtime` | [content__public__common__content_switches](content__public__common__content_switches.md) | Forcibly enable and select the specified runtime for webxr |
| `--force-whats-new` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Displays the What's New experience when the browser is started if it has not yet been shown for the current milestone (this overrides kNoFirstRun, without showi |
| `--forced-translate-language` | [components__translate__core__common__translate_switches](components__translate__core__common__translate_switches.md) | Overrides the target language for translation and forces translation of all pages to the new target language. |
| `--from-browser-switcher` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that this launch of the browser originated from the Legacy Browser Support for Edge extension's native host *(only if `BUILDFLAG(IS_WIN)`)* |
| `--from-installer` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that this launch of the browser originated from the installer (i.e., following a successful new install or over-install) *(only if `BUILDFLAG(IS_WIN)`)* |
| `--full-memory-crash-report` | [base__base_switches](base__base_switches.md) | Generates full memory crash dump. |
| `--gaia-config` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the path to a config file containing GAIA urls |
| `--gaia-config-contents` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies a string containing the JSON config for GAIA urls |
| `--gaia-url` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the path for GAIA authentication URL |
| `--gamepad-polling-interval` | [device__gamepad__public__cpp__gamepad_switches](device__gamepad__public__cpp__gamepad_switches.md) | All switches in alphabetical order |
| `--gcm-checkin-url` | [google_apis__gcm__engine__gservices_switches](google_apis__gcm__engine__gservices_switches.md) | Sets the checkin service endpoint that will be used for performing Google Cloud Messaging checkins. |
| `--gcm-mcs-endpoint` | [google_apis__gcm__engine__gservices_switches](google_apis__gcm__engine__gservices_switches.md) | Sets the Mobile Connection Server endpoint that will be used for Google Cloud Messaging. |
| `--gcm-registration-url` | [google_apis__gcm__engine__gservices_switches](google_apis__gcm__engine__gservices_switches.md) | Sets the registration endpoint that will be used for creating new Google Cloud Messaging registrations. |
| `--gcpw-signin` | [services__device__public__cpp__hid__hid_switches](services__device__public__cpp__hid__hid_switches.md) | Enable HID device access for the GCPW sign-in process. |
| `--geic-always-skip-fre` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Treats the GEiC FRE as completed without persisting anything |
| `--geic-guest-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the GEiC guest URL. |
| `--geic-reset-fre` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Clears all GEiC FRE status at startup |
| `--generate-accessibility-test-expectations` | [ui__accessibility__accessibility_switches](ui__accessibility__accessibility_switches.md) | For development / testing only |
| `--generate-pdf-document-outline` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Embed the document outline into printed PDFs. |
| `--gl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--gl-egl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--gl-null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--gl-shader-interm-output` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Include ANGLE's intermediate representation (AST) output in shader compilation info logs. |
| `--gles` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--gles-egl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--gles-null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--glic-admin-redirect-patterns` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | List of URL patterns in the glic webview to redirect to an admin blocked panel, as a space-separated list. |
| `--glic-always-open-fre` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-always-show-web-actuation-toggle` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Whether to show web actuation toggle in the Chrome AI settings page. |
| `--glic-always-skip-fre` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-automation` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Automation is intended to be passed in addition to glic-dev |
| `--glic-dev` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Dev mode for glic only exposed via command line flag. |
| `--glic-experimental-fre-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-guest-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the glic guest URL. |
| `--glic-guest-url-preset-autopush` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Configure preset guest URLs for manual testing |
| `--glic-guest-url-preset-preprod` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-guest-url-preset-prod` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-guest-url-preset-staging` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-host-logging` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Whether additional logging is enabled in the glic api host. |
| `--glic-open-on-startup` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Use --glic-open-on-startup=attached or --glic-open-on-startup=detached. |
| `--glic-shortcuts-learn-more-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--glic-skip-reload-after-navigation` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If this flag is set, then the page navigating will not trigger a reload. |
| `--glic-webui-allowed-origins` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | List of allowed origins in the glic webview, as a space-separated list. |
| `--google-apis-url` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the backend server used for Google API calls |
| `--google-base-suggestion-url` | [components__google__core__common__google_switches](components__google__core__common__google_switches.md) | All switches in alphabetical order |
| `--google-base-url` | [components__google__core__common__google_switches](components__google__core__common__google_switches.md) | Specifies an alternate URL to use for speaking to Google |
| `--google-doodle-url` | [components__search_provider_logos__switches](components__search_provider_logos__switches.md) | Overrides the URL used to fetch the current Google Doodle |
| `--google-url` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the domain of the SAPISID cookie |
| `--gpu-blocklist-test-group` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Select a different set of GPU blocklist entries with the specified test_group ID. |
| `--gpu-channel-request-start-time-ticks` | [content__public__common__content_switches](content__public__common__content_switches.md) | Time the browser process requested the GPU channel for the renderer (in TimeTicks). |
| `--gpu-client-id` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--gpu-device-id` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the active graphics device id from browser process to info collection GPU process. |
| `--gpu-disk-cache-size-kb` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Allows explicitly specifying the shader disk cache size for embedded devices |
| `--gpu-driver-bug-list-test-group` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Enable an extra set of GPU driver bug list entries with the specified test_group ID |
| `--gpu-driver-version` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the active graphics driver version from browser process to info collection GPU process. |
| `--gpu-launcher` | [content__public__common__content_switches](content__public__common__content_switches.md) | Extra command line options for launching the GPU process (normally used for debugging) |
| `--gpu-no-context-lost` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Inform Chrome that a GPU context will not be lost in power saving mode, screen saving mode, etc |
| `--gpu-preferences` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes encoded GpuPreferences to GPU process. |
| `--gpu-process` | [content__public__common__content_switches](content__public__common__content_switches.md) | Makes this process a GPU sub-process. |
| `--gpu-process` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--gpu-program-cache-size-kb` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Sets the maximum size of the in-memory gpu program cache, in kb |
| `--gpu-recent-crash-count` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the number of recent GPU crashes to the GPU process. |
| `--gpu-revision` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the active graphics revision info from browser process to info collection GPU process. |
| `--gpu-sandbox-allow-sysv-shm` | [sandbox__policy__switches](sandbox__policy__switches.md) | Allows shmat() system call in the GPU sandbox. |
| `--gpu-sandbox-failures-fatal` | [sandbox__policy__switches](sandbox__policy__switches.md) | Makes GPU sandbox failures fatal. |
| `--gpu-sandbox-start-early` | [content__public__common__content_switches](content__public__common__content_switches.md) | Starts the GPU sandbox before creating a GL context. |
| `--gpu-startup-dialog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the GPU process to display a dialog on launch. |
| `--gpu-sub-system-id` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the active graphics sub system id from browser process to info collection GPU process. |
| `--gpu-vendor-id` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Passes the active graphics vendor id from browser process to info collection GPU process. |
| `--gpu-watchdog-timeout-seconds` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Override value for the GPU watchdog timeout in seconds. |
| `--gpu2-startup-dialog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the second GPU process used for gpu info collection to display a dialog on launch. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--gtk-version` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Specify the GTK version to be loaded. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--guest` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes the browser to launch directly in guest mode. *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS) \|\| BUILDFLAG(IS_MAC) \|\| \`)* |
| `--h` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | *(only if `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`)* |
| `--hardware-video-decode-framerate` | [media__base__media_switches](media__base__media_switches.md) | Some (Qualcomm only at the moment) V4L2 video decoders require setting the framerate so that the hardware decoder can scale the clocks efficiently *(only if `BUILDFLAG(USE_V4L2_CODEC)`)* |
| `--hardware-video-device-path` | [media__base__media_switches](media__base__media_switches.md) | Allows explicitly picking a device path to find the device for VA-API video decoding and encoding. *(only if `BUILDFLAG(USE_VAAPI)`)* |
| `--headless` | [components__embedder_support__switches](components__embedder_support__switches.md) | Enable headless mode. |
| `--headless` | [ui__gfx__switches](ui__gfx__switches.md) | Run in headless mode, i.e., without a UI or display server dependencies. |
| `--help` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | These flags show the man page on Linux *(only if `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`)* |
| `--help` | [remoting__host__base__switches](remoting__host__base__switches.md) | "--help" prints the usage message. |
| `--hide-crash-restore-bubble` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Does not show the crash restore bubble when the browser is started during the system startup phase in ChromeOS, if the ChromeOS full restore feature is enabled, |
| `--hide-icons` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Makes Windows happy by allowing it to show "Enable access to this program" checkbox in Add/Remove Programs->Set Program Access and Defaults *(only if `BUILDFLAG(IS_WIN)`)* |
| `--hide-scrollbars` | [content__public__common__content_switches](content__public__common__content_switches.md) | Prevents creating scrollbars for web content |
| `--homepage` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies which page will be displayed in newly-opened tabs |
| `--host-resolver-rules` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | These mappings only apply to the host resolver. |
| `--host-rules` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Deprecated alias for backwards compatibility, now does the same thing as --host-resolver-rules which should be used instead |
| `--http2-grease-settings` | [components__network_session_configurator__common__network_switches](components__network_session_configurator__common__network_switches.md) | `kEnableHttp2GreaseSettings` does not include the word "enable" for historical reasons. |
| `--https://chromesyncpasswords-pa.googleapis.com/v1/users/me/deviceAuthorizationKey` | [components__webauthn__core__browser__device_authorization__device_authorization_switches](components__webauthn__core__browser__device_authorization__device_authorization_switches.md) |  |
| `--https://onetimetoken.pa.googleapis.com` | [components__one_time_tokens__core__common__one_time_token_switches](components__one_time_tokens__core__common__one_time_token_switches.md) |  |
| `--https://securitydomain-pa.googleapis.com/v1/` | [components__trusted_vault__command_line_switches](components__trusted_vault__command_line_switches.md) |  |
| `--ignore-autocomplete-off-autofill` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Ignores autocomplete="off" for Autofill data (profiles + credit cards). |
| `--ignore-bad-message-for-testing` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | The switch to ignore bad mojo message reports |
| `--ignore-certificate-errors-spki-list` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | A set of public key hashes for which to ignore certificate-related errors |
| `--ignore-google-port-numbers` | [components__google__core__common__google_switches](components__google__core__common__google_switches.md) | When set, this will ignore the PortPermission passed in the google_util.h methods and ignore the port numbers |
| `--ignore-gpu-blocklist` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Ignores GPU blocklist. |
| `--ignore-no-first-run-for-search-engine-choice-screen` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) | Override the --no-first-run dialog suppression for the search dialog for testing |
| `--ignore-profile-directory-if-not-exists` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If provided with kProfileDirectory, does not create the profile if the profile directory doesn't exist. |
| `--import-passwords` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Triggers the import of passwords on startup. *(only if `!BUILDFLAG(IS_ANDROID)`)* |
| `--in-process-gpu` | [content__public__common__content_switches](content__public__common__content_switches.md) | Run the GPU process as a thread in the browser process. |
| `--incognito` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes the initial browser opened to be in incognito mode |
| `--incognito` | [headless__public__switches](headless__public__switches.md) | Forces Incognito mode even if user data directory is specified using the --user-data-dir switch. |
| `--init-isolate-as-foreground` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies that the main-thread Isolate should initialize in foreground mode |
| `--initialize-client-hints-storage` | [components__client_hints__common__switches](components__client_hints__common__switches.md) | Pre-load the client hint storage |
| `--input` | [remoting__host__base__switches](remoting__host__base__switches.md) | Name of the pipe used to communicate from the parent to the child process. |
| `--install-autogenerated-theme` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Installs an autogenerated theme based on the given RGB value |
| `--install-chrome-app` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes Chrome to initiate an installation flow for the given app. |
| `--install-isolated-web-app-from-file` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes Chrome to install the unsigned Web Bundle at the given path as a developer mode Isolated Web App. |
| `--install-isolated-web-app-from-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes Chrome to install a developer mode Isolated Web App whose contents are hosted at the given HTTP(S) URL. |
| `--instant-process` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Marks a renderer as an Instant process. |
| `--ip-address-space-overrides` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Specifies manual overrides to the IP endpoint -> IP address space mapping |
| `--ipc-connection-timeout` | [content__public__common__content_switches](content__public__common__content_switches.md) | Overrides the timeout, in seconds, that a child process waits for a connection from the browser before killing itself. |
| `--ipc-dump-directory` | [content__public__common__content_switches](content__public__common__content_switches.md) | Dumps IPC messages sent from renderer processes to the browser process to the given directory *(only if `defined(ENABLE_IPC_FUZZER)`)* |
| `--ipc-fuzzer-testcase` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies the testcase used by the IPC fuzzer. *(only if `defined(ENABLE_IPC_FUZZER)`)* |
| `--isolate-origins` | [content__public__common__content_switches](content__public__common__content_switches.md) | Require dedicated processes for a set of origins, specified as a comma-separated list |
| `--isolated` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies that the browser is running isolated and should not attempt to start a second isolated browser. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--isolated-context-origins` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Enables APIs guarded with the [IsolatedContext] IDL attribute for the given comma-separated list of origins. |
| `--javaless-renderers` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables/disables javaless renderers based on value given *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--javascript-harmony` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables experimental Harmony (ECMAScript 6) features. |
| `--keep-alive-for-test` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Used for testing - keeps browser alive after last browser window closes. |
| `--kiosk` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enable kiosk mode |
| `--kiosk-printing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enable automatically pressing the print button in print preview. |
| `--lang` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | The language file that we want to try to open |
| `--launch-time-ticks` | [content__public__common__content_switches](content__public__common__content_switches.md) | Time the browser launched the renderer process (in TimeTicks). |
| `--layer` | [cc__base__switches](cc__base__switches.md) |  |
| `--list-apps` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Writes open and installed web apps for each profile to the specified file without launching a new browser window or tab *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_MAC) \|\| BUILDFLAG(IS_WIN)`)* |
| `--list-audio-devices` | [remoting__host__base__switches](remoting__host__base__switches.md) | Command line switch to list all audio devices and their UID. *(only if `BUILDFLAG(IS_APPLE)`)* |
| `--load-and-launch-app` | [apps__switches](apps__switches.md) | All switches in alphabetical order |
| `--load-apps` | [extensions__common__switches](extensions__common__switches.md) | Comma-separated list of paths to apps to load at startup |
| `--load-extension` | [extensions__common__switches](extensions__common__switches.md) | Comma-separated list of paths to extensions to load at startup. |
| `--load-guest-mode-test-extension` | [extensions__common__switches](extensions__common__switches.md) | Path to the unpacked test extension to load into guest mode *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--load-signin-profile-test-extension` | [extensions__common__switches](extensions__common__switches.md) | Path to the unpacked test extension to load into the signin profile *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--load-webui-from-disk` | [content__public__common__content_switches](content__public__common__content_switches.md) | Flag used to load WebUI files directly from disk instead of pak files *(only if `BUILDFLAG(LOAD_WEBUI_FROM_DISK)`)* |
| `--loading-predictor-allow-local-request-for-testing` | [chrome__browser__predictors__predictors_switches](chrome__browser__predictors__predictors_switches.md) | Allows the loading predictor to do prefetches to local IP addresses |
| `--local-network-access-permissions-policy-default-enabled` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | If set, Local Network Access (LNA) permissions policy features will be default enabled in all frames, rather than requiring explicit delegation. |
| `--local-sync-backend-dir` | [components__browser_sync__browser_sync_switches](components__browser_sync__browser_sync_switches.md) | Specifies the local sync backend directory |
| `--log-best-effort-tasks` | [base__base_switches](base__base_switches.md) | Logs information about all tasks posted with TaskPriority::BEST_EFFORT |
| `--log-file` | [content__public__common__content_switches](content__public__common__content_switches.md) | Overrides the default file name to use for general-purpose logging (does not affect which events are logged). |
| `--log-file-handle` | [chrome__windows_services__service_program__switches](chrome__windows_services__service_program__switches.md) | A switch conveying a handle value for the file to which the service should emit its logs. |
| `--log-file-source` | [chrome__windows_services__service_program__switches](chrome__windows_services__service_program__switches.md) | A switch conveying the PID of the process in which the log file handle value is valid. |
| `--log-gpu-control-list-decisions` | [content__public__common__content_switches](content__public__common__content_switches.md) | Logs GPU control list decisions when enforcing blocklist rules. |
| `--log-level` | [content__public__common__content_switches](content__public__common__content_switches.md) | Sets the minimum log level |
| `--log-missing-unload-ack` | [content__public__common__content_switches](content__public__common__content_switches.md) | Log an error whenever the unload timeout for a render frame is exceeded. |
| `--log-net-log` | [net__base__switches](net__base__switches.md) |  |
| `--log-on-ui-double-background-blur` | [cc__base__switches](cc__base__switches.md) | Checks and logs double background blur as an error if any. *(only if `DCHECK_IS_ON()`)* |
| `--lso-url` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the backend server used for lso authentication calls |
| `--ltr` | [base__i18n__base_i18n_switches](base__i18n__base_i18n_switches.md) |  |
| `--make-chrome-default` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates whether Chrome should be set as the default browser during installation. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--make-default-browser` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Makes Chrome default browser |
| `--mangle-localized-strings` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Transform localized strings to be longer, with beginning and end markers to make truncation visually apparent. |
| `--mark_as_allowlisted_for_phish_guard` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated URLs to mark as present on the password protection allowlist |
| `--mark_as_allowlisted_for_real_time` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated URLs to mark as present on the high-confidence allowlist. |
| `--mark_as_enterprise_blocked` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag for caching an artificial blocked enterprise lookup verdict. |
| `--mark_as_enterprise_warned` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag for caching an artificial flagged enterprise lookup verdict. |
| `--mark_as_malware` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated URLs to mark as malware for local database checks. |
| `--mark_as_phish_guard_phishing` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag for caching an artificial PhishGuard unsafe verdict. |
| `--mark_as_phishing` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated URLs to mark as phishing for local database checks. |
| `--mark_as_real_time_phishing` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag for caching an artificial phishing verdict for URL real-time lookups. |
| `--mark_as_uws` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated URLs to mark as unwanted software for local database checks. |
| `--mark_as_v5_search_hashes_phishing` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag for caching an artificial phishing verdict for V5 SearchHashes. |
| `--market-url-for-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Sets the market URL for Chrome for use in testing. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--max-active-webgl-contexts` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows user to override maximum number of active WebGL contexts per renderer process. |
| `--max-decoded-image-size-mb` | [content__public__common__content_switches](content__public__common__content_switches.md) | Sets the maximium decoded image size limitation. |
| `--max-gum-fps` | [content__public__common__content_switches](content__public__common__content_switches.md) | Override the maximum framerate as can be specified in calls to getUserMedia |
| `--max-web-media-player-count` | [content__public__common__content_switches](content__public__common__content_switches.md) | Sets the maximum number of WebMediaPlayers allowed per frame. |
| `--message-loop-type-ui` | [content__public__common__content_switches](content__public__common__content_switches.md) | Indicates the utility process should run with a message loop type of UI. |
| `--metal` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--metal` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--metal-null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--metrics-client-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This is how the metrics client ID is passed from the browser process to its children *(only if `BUILDFLAG(IS_MAC)`)* |
| `--metrics-recording-only` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Enables the recording of metrics reports but disables reporting |
| `--metrics-shmem-handle` | [base__base_switches](base__base_switches.md) | Handle to the shared memory segment a child process should use to transmit histograms back to the browser process. |
| `--metrics-upload-interval` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Override the standard time interval between each metrics report upload for UMA and UKM |
| `--min-video-decoder-output-buffer-size` | [media__base__media_switches](media__base__media_switches.md) | Minimum size for buffer size used for output video frames in FuchsiaVideoDecoder *(only if `BUILDFLAG(IS_FUCHSIA)`)* |
| `--mock` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--mock-cert-verifier-default-result-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Set the default result for MockCertVerifier |
| `--mock-otp-value` | [components__one_time_tokens__core__common__one_time_token_switches](components__one_time_tokens__core__common__one_time_token_switches.md) | Returns the specified mock OTP string value when retrieving OTP tokens |
| `--mojo-local-storage` | [content__public__common__content_switches](content__public__common__content_switches.md) | Use a Mojo-based LocalStorage implementation. |
| `--mojo-pipe-token` | [remoting__host__base__switches](remoting__host__base__switches.md) | Token used to create a message pipe between a pair of child and parent processes. |
| `--mse-audio-buffer-size-limit-mb` | [media__base__media_switches](media__base__media_switches.md) | Allows explicitly specifying MSE audio/video buffer sizes as megabytes |
| `--mse-video-buffer-size-limit-mb` | [media__base__media_switches](media__base__media_switches.md) |  |
| `--multistep-filter-allow-http-for-testing` | [components__multistep_filter__core__switches](components__multistep_filter__core__switches.md) | Allows HTTP URLs for extraction and suggestions during browser testing. |
| `--multistep-filter-bypass-capability-check` | [components__multistep_filter__core__switches](components__multistep_filter__core__switches.md) | Bypass the capability checks for local testing. |
| `--mute-audio` | [media__base__media_switches](media__base__media_switches.md) | Mutes audio sent to the audio device so it is not audible during automated testing. |
| `--native` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) |  |
| `--native-messaging-connect-extension` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Requests a native messaging connection be established between the extension with ID specified by this switch and the native messaging host named by the kNativeM |
| `--native-messaging-connect-host` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Requests a native messaging connection be established between the native messaging host named by this switch and the extension with ID specified by kNativeMessa |
| `--native-messaging-connect-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | If set when kNativeMessagingConnectHost and kNativeMessagingConnectExtension are specified, is reflected to the native messaging host as a command line paramete |
| `--nearby-share-certificate-validity-period-hours` | [chrome__browser__nearby_sharing__common__nearby_share_switches](chrome__browser__nearby_sharing__common__nearby_share_switches.md) | All switches in alphabetical order |
| `--nearby-share-device-id` | [chrome__browser__nearby_sharing__common__nearby_share_switches](chrome__browser__nearby_sharing__common__nearby_share_switches.md) | Overrides the default device ID to provide a stable ID in test environments |
| `--nearby-share-num-private-certificates` | [chrome__browser__nearby_sharing__common__nearby_share_switches](chrome__browser__nearby_sharing__common__nearby_share_switches.md) | Overrides the default number of private certificates generated |
| `--nearbysharing-http-host` | [chrome__browser__nearby_sharing__common__nearby_share_switches](chrome__browser__nearby_sharing__common__nearby_share_switches.md) | Overrides the default URL for Google APIs (https://www.googleapis.com) used by Nearby Share |
| `--net-log-capture-mode` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Sets the granularity of events to capture in the network log |
| `--net-log-duration` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Specifies the duration (in seconds) for network logging |
| `--net-log-file-format` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Sets the format used for the network log file |
| `--net-log-max-size-mb` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Sets the maximum size, in megabytes |
| `--network` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--new-window` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Launches URL in new browser window. |
| `--no-default-browser-check` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables the default browser check |
| `--no-delay-for-dx12-vulkan-info-collection` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Start the non-sandboxed GPU process for DX12 and Vulkan info collection immediately after the browser starts |
| `--no-experiments` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables all experiments set on about:flags |
| `--no-first-run` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Skip First Run tasks as well as not showing additional dialogs, prompts or bubbles |
| `--no-network-profile-warning` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Whether or not the browser should warn if the profile is on a network share *(only if `BUILDFLAG(IS_WIN)`)* |
| `--no-op-for-testing` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | A process type that exits cleanly with code 0 without performing work. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--no-op-for-testing` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--no-pdf-header-footer` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Do not display header and footer in the printed PDF file. |
| `--no-pings` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Don't send hyperlink auditing pings |
| `--no-pre-read-main-dll` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Whether this process should PrefetchVirtualMemory on the contents of Chrome.dll *(only if `BUILDFLAG(IS_WIN)`)* |
| `--no-proxy-server` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Don't use a proxy server, always make direct connections |
| `--no-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Disables the sandbox for all process types that are normally sandboxed |
| `--no-startup-window` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Does not automatically open a browser window on startup (used when launching Chrome for the purpose of hosting background apps). |
| `--no-system-proxy-config-service` | [headless__public__switches](headless__public__switches.md) | Do not use system proxy configuration service. |
| `--no-unsandboxed-zygote` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the unsandboxed zygote |
| `--no-user-gesture-required` | [media__base__media_switches](media__base__media_switches.md) | Autoplay policy that does not require any user gesture. |
| `--no-xr-runtime` | [content__public__common__content_switches](content__public__common__content_switches.md) | Tell WebXr to assume that it does not support any runtimes. |
| `--no-xshm` | [ui__gfx__switches](ui__gfx__switches.md) | Disables MIT-SHM extension *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--no-zygote` | [content__public__common__content_switches](content__public__common__content_switches.md) | Disables the use of a zygote process for forking child processes |
| `--no-zygote-sandbox` | [sandbox__policy__switches](sandbox__policy__switches.md) | Instructs the zygote to launch without a sandbox *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--NO_REPROMPT` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) | The string that's passed to `switches::kSearchEngineChoiceTriggerRepromptParams` so that we don't reprompt users with the choice screen. |
| `--noerrdialogs` | [base__base_switches](base__base_switches.md) | Suppresses all error dialogs when present. |
| `--none` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--none` | [device__vr__public__cpp__switches](device__vr__public__cpp__switches.md) |  |
| `--notebook-home-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides the default URL for the Notebook Home WebUI. |
| `--notification-inline-reply` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Used in combination with kNotificationLaunchId to specify the inline reply entered in the toast in the Windows Action Center. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--notification-launch-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Used for launching Chrome when a toast displayed in the Windows Action Center has been activated *(only if `BUILDFLAG(IS_WIN)`)* |
| `--ntp-process` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Marks a renderer as a New Tab Page process. |
| `--null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--num-raster-threads` | [cc__base__switches](cc__base__switches.md) | Switches for raster |
| `--nv12` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Swap chain formats for direct composition SDR video overlays. |
| `--oauth-account-manager-url` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies the backend server used for OAuth issue token calls |
| `--oauth2-client-id` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies custom OAuth2 client id for testing purposes. |
| `--oauth2-client-secret` | [google_apis__gaia__gaia_switches](google_apis__gaia__gaia_switches.md) | Specifies custom OAuth2 client secret for testing purposes. |
| `--offer-in-settings` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--offscreen-document-testing` | [extensions__common__switches](extensions__common__switches.md) | Allows the use of the `testing` reason in offscreen documents. |
| `--omnibox-everywhere` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Directly launches the Omnibox Everywhere desktop UI widget. |
| `--on-the-fly-mhtml-hash-computation` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Calculate the hash of an MHTML file as it is being saved |
| `--one-time-token-service-base-url` | [components__one_time_tokens__core__common__one_time_token_switches](components__one_time_tokens__core__common__one_time_token_switches.md) |  |
| `--open-in-background` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Opens the URLs given on the command line as background tabs, without activating or raising the browser window they are added to, so that handing a URL to an alr |
| `--opengles` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--opengraph` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--openxr` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--orientation-sensors` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--origin-trial-disabled-features` | [components__embedder_support__switches](components__embedder_support__switches.md) | Contains a list of feature names for which origin trial experiments should be disabled |
| `--origin-trial-disabled-tokens` | [components__embedder_support__switches](components__embedder_support__switches.md) | Contains a list of token signatures for which origin trial experiments should be disabled |
| `--origin-trial-public-key` | [components__embedder_support__switches](components__embedder_support__switches.md) | Comma-separated list of keys which will override the default public keys for checking origin trial tokens. |
| `--output` | [remoting__host__base__switches](remoting__host__base__switches.md) | Name of the pipe used to communicate from the child to the parent process. |
| `--override-enabled-cdm-interface-version` | [media__base__media_switches](media__base__media_switches.md) | Overrides the default enabled library CDM interface version(s) with the one specified with this switch, which will be the only version enabled |
| `--override-hardware-secure-codecs-for-testing` | [media__base__media_switches](media__base__media_switches.md) | Overrides hardware secure codecs support for testing |
| `--override-language-detection` | [content__public__common__content_switches](content__public__common__content_switches.md) | Overrides the language detection result determined based on the page contents. |
| `--override-use-software-gl-for-tests` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Forces the use of software GL instead of hardware gpu for tests. |
| `--ozone-dump-file` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Specify location for image dumps. |
| `--ozone-override-screen-size` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Specifies ozone screen size. |
| `--ozone-platform` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Specify ozone platform implementation to use. |
| `--p010` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--pack-extension` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Packages an extension to a .crx installable file from a given directory. |
| `--pack-extension-key` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Optional PEM private key to use in signing packaged .crx. |
| `--page-content-annotations-skip-fcp-wait-for-testing` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) | If enabled, page content annotations requests will not wait for FCP. |
| `--page-content-annotations-validation-batch-size` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) |  |
| `--page-content-annotations-validation-content-visibility` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) | Enables the specific annotation type to run validation at startup after a delay |
| `--page-content-annotations-validation-startup-delay-seconds` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) |  |
| `--page-content-annotations-validation-write-to-file` | [components__page_content_annotations__core__page_content_annotations_switches](components__page_content_annotations__core__page_content_annotations_switches.md) | Writes the output of page content annotation validations to the given file. |
| `--parent-window` | [remoting__host__base__switches](remoting__host__base__switches.md) | Used to pass the HWND for the parent process to a child process. |
| `--partition-alloc-scheduler-loop-quarantine` | [base__base_switches](base__base_switches.md) | Specifies the JSON configuration for PartitionAlloc's scheduler loop quarantine. |
| `--passbox-endpoint` | [components__password_manager__core__browser__remote_actor__remote_actor_switches](components__password_manager__core__browser__remote_actor__remote_actor_switches.md) | Overrides the default endpoint URL for the Passbox credential store service. |
| `--passthrough` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--password-change-url` | [components__password_manager__core__browser__password_manager_switches](components__password_manager__core__browser__password_manager_switches.md) | This switch allows testing password change feature on provided URL |
| `--password-store` | [components__password_manager__core__browser__password_manager_switches](components__password_manager__core__browser__password_manager_switches.md) | Specifies which encryption storage backend to use *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--password-store` | [headless__public__switches](headless__public__switches.md) | Specifies which encryption storage backend to use |
| `--pdf-renderer` | [content__public__common__content_switches](content__public__common__content_switches.md) | Renderer process that runs the non-PPAPI PDF plugin. |
| `--peer_connection` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--pen-devices` | [ui__events__event_switches](ui__events__event_switches.md) | Tells chrome to interpret events from these devices as pen events *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--perfetto-disable-interning` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Repeat internable data for each TraceEvent in the perfetto proto format. |
| `--policy` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Set policy value by command line. |
| `--policy-verification-key` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Replace the original verification_key with the one provided by the command line flag |
| `--pre-crashpad-crash-test` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes the browser process to crash very early in startup, just before crashpad (or breakpad) is initialized. |
| `--prediction-service-mock-likelihood` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Used to mock the response received from the Web Permission Prediction Service |
| `--preinstalled-web-apps-dir` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | A directory where Chrome looks for json files describing default/preinstalled web apps |
| `--prevent-resizing-contents-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | For mobile devices, tests should include a viewport meta tag to specify page dimension adjustments *(only if `BUILDFLAG(IS_IOS)`)* |
| `--print-to-pdf` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Save a PDF file of the loaded page. |
| `--privet-ipv6-only` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Use IPv6 only for privet HTTP. |
| `--probability` | [components__signin__public__base__signin_switches](components__signin__public__base__signin_switches.md) | Feature param to pass probability for identity surveys. *(only if `BUILDFLAG(IS_WIN) \|\| BUILDFLAG(IS_MAC) \|\| BUILDFLAG(IS_LINUX) \|\| \`)* |
| `--process-per-site` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable the "Process Per Site" process model for all domains |
| `--process-per-tab` | [content__public__common__content_switches](content__public__common__content_switches.md) | Runs each set of script-connected tabs (i.e., a BrowsingInstance) in its own renderer process |
| `--product-version` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Outputs the product version information and quit |
| `--profile-base-name` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Pass the basename of the profile directory to specify which profile to get information *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_MAC) \|\| BUILDFLAG(IS_WIN)`)* |
| `--profile-directory` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Selects directory of profile to associate with the first browser launched. |
| `--profile-email` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Like kProfileDirectory, but selects the profile by email address |
| `--profile-management-attributes` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Domains and associated SAML attributes for which third-party profile management should be enabled *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_MAC) \|\| BUILDFLAG(IS_WIN)`)* |
| `--profiling-at-start` | [base__base_switches](base__base_switches.md) | Starts the sampling based profiler for the browser process at startup |
| `--profiling-file` | [base__base_switches](base__base_switches.md) | Specifies a location for profiling output |
| `--profiling-flush` | [base__base_switches](base__base_switches.md) | Controls whether profile data is periodically flushed to a file |
| `--proxy-auto-detect` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces proxy auto-detection. |
| `--proxy-bypass-list` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies a list of hosts for whom we bypass proxy settings and use direct connections |
| `--proxy-bypass-list` | [headless__public__switches](headless__public__switches.md) | Specifies a list of hosts for whom we bypass proxy settings and use direct connections |
| `--proxy-pac-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Uses the pac script at the given URL |
| `--proxy-pac-url` | [headless__public__switches](headless__public__switches.md) | Uses the PAC script at the specified URL to pick proxies, overrides system settings |
| `--proxy-server` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Uses a specified proxy server, overrides system settings. |
| `--proxy-server` | [headless__public__switches](headless__public__switches.md) | Uses a specified proxy server, overrides system settings |
| `--pseudonymization-salt-handle` | [content__public__common__content_switches](content__public__common__content_switches.md) | Handle to shared memory containing the pseudonymization salt, passed to child processes at launch |
| `--pwa-launcher-version` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the version of the Progressive-Web-App launcher that launched Chrome, used to determine whether to update all launchers *(only if `BUILDFLAG(IS_WIN)`)* |
| `--qt-version` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Specify the QT version to be loaded. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--quicken-site-search-expiry-for-testing` | [components__search_engines__search_engines_switches](components__search_engines__search_engines_switches.md) |  |
| `--raise-timer-frequency` | [content__public__common__content_switches](content__public__common__content_switches.md) | Raise the timer interrupt frequency in all Chrome processes, for experimental purposes *(only if `BUILDFLAG(IS_WIN)`)* |
| `--rdp_desktop_session` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--reader-mode-feedback` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--reader-mode-heuristics` | [components__dom_distiller__core__dom_distiller_switches](components__dom_distiller__core__dom_distiller_switches.md) |  |
| `--realtime-reporting-url` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Specifies the URL at which to upload real-time reports. |
| `--reduce-accept-language` | [content__public__common__content_switches](content__public__common__content_switches.md) | Reduce the accept-language for HTTP header and JS navigator.languages, and only most preferred language: https://github.com/Tanych/accept-language. |
| `--reduce-accept-language-http` | [content__public__common__content_switches](content__public__common__content_switches.md) | Reduce the accept-language for HTTP header, and only send most preferred language in the request header: https://github.com/Tanych/accept-language. |
| `--reduce-user-agent-minor-version` | [content__public__common__content_switches](content__public__common__content_switches.md) | Reduce the minor version number in the User-Agent string |
| `--refresh-component-extension-service-workers` | [extensions__common__switches](extensions__common__switches.md) | Forces component extensions' service workers to be re-registered on every load, instead of reusing the registration persisted in the profile. |
| `--refresh-platform-policy` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Forces immediate platform policy refresh (not cloud policy) when Chrome is already running |
| `--relauncher` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | A process type (switches::kProcessType) that relaunches the browser *(only if `BUILDFLAG(IS_MAC)`)* |
| `--relauncher` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--remote-allow-origins` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables web socket connections from the specified origins only |
| `--remote-debugging-address` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Use the given address instead of the default loopback for accepting remote debugging connections |
| `--remote-debugging-io-pipes` | [content__public__common__content_switches](content__public__common__content_switches.md) | Pipe names for the incoming and outbound messages *(only if `BUILDFLAG(IS_WIN)`)* |
| `--remote-debugging-pipe` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables remote debug over stdio pipes [in=3, out=4] or over the remote pipes specified in the 'remote-debugging-io-pipes' switch |
| `--remote-debugging-port` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables remote debug over HTTP on the specified port. |
| `--remote-debugging-socket-name` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables remote debug over HTTP on the specified socket name. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--remote-debugging-targets` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Provides a list of addresses to discover DevTools remote debugging targets |
| `--render-node-override` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Allows explicitly picking a DRM render node to create gbm_device for rendering. |
| `--renderer` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the process to run as renderer instead of as browser. |
| `--renderer` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--renderer-client-id` | [content__public__common__content_switches](content__public__common__content_switches.md) |  |
| `--renderer-cmd-prefix` | [content__public__common__content_switches](content__public__common__content_switches.md) | The contents of this flag are prepended to the renderer command line |
| `--renderer-process-limit` | [content__public__common__content_switches](content__public__common__content_switches.md) | Overrides the default/calculated limit to the number of renderer processes |
| `--renderer-startup-dialog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the renderer process to display a dialog on launch |
| `--renderer-wait-for-java-debugger` | [content__public__common__content_switches](content__public__common__content_switches.md) | Block ChildProcessMain thread of the renderer's ChildProcessService until a Java debugger is attached. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--renderpass` | [cc__base__switches](cc__base__switches.md) | Parameters for kUIShowCompositedLayerBorders. |
| `--repair-all-valid-extensions` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that all corrupted extensions should be repaired if they are are enabled by policy |
| `--report-vp9-as-an-unsupported-mime-type` | [media__base__media_switches](media__base__media_switches.md) | Force to report VP9 as an unsupported MIME type. |
| `--request-desktop-sites` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Force enable user agent overrides to request desktop sites in Clank. *(only if `BUILDFLAG(IS_ANDROID)`)* |
| `--reset-variation-state` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Forces a reset of the one-time-randomized FieldTrials on this client, also known as the Chrome Variations state. |
| `--restart` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that Chrome was restarted (e.g., after a flag change) |
| `--restore-last-session` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates the last session should be restored on startup |
| `--rtl` | [base__i18n__base_i18n_switches](base__i18n__base_i18n_switches.md) |  |
| `--run-all-compositor-stages-before-draw` | [components__viz__common__switches](components__viz__common__switches.md) | Effectively disables pipelining of compositor frame production stages by waiting for each stage to finish before completing a frame. |
| `--run-manual` | [content__public__common__content_switches](content__public__common__content_switches.md) | Manual tests only run when --run-manual is specified |
| `--run-web-tests` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Runs Content Shell in web test mode, injecting test-only behaviour for blink web tests. |
| `--runtime` | [device__vr__public__cpp__switches](device__vr__public__cpp__switches.md) |  |
| `--safe-browsing-no-protection-duration-seconds` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line override for the temporary No Protection duration in seconds. |
| `--safe-browsing-skip-csd-allowlist` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | If present, indicates that the client-side detection allowlist check should be skipped (it is treated as no match). |
| `--safe-browsing-skip-high-confidence-allowlist` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | If the switch is present, any high-confidence allowlist check will return that it does not match the allowlist. |
| `--safe-browsing-treat-user-as-advanced-protection` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) |  |
| `--safebrowsing-enable-enhanced-protection` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Enable Safe Browsing Enhanced Protection. |
| `--safebrowsing-fast-initial-lists-update` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Command-line flag that reduces the initial delay for Safe Browsing database updates for manual testing purposes. |
| `--safebrowsing-manual-download-blacklist` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | List of comma-separated sha256 hashes of executable files which the download-protection service should treat as "dangerous."  For a file to show a warning, it a |
| `--same-tab` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that the URL in the command line should open in the active tab instead of a new tab |
| `--sandbox-ipc` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the process to run as a sandbox IPC subprocess. |
| `--save-page-as-mhtml` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Enables saving webpages as MHTML (Webpage, Single) by default, instead of saving as HTML with a directory of sub-resources *(only if `!BUILDFLAG(IS_CHROMEOS)`)* |
| `--scheduler-boost-urgent` | [base__base_switches](base__base_switches.md) | Override the default scheduling boosting value for urgent tasks *(only if `BUILDFLAG(IS_CHROMEOS)`)* |
| `--screen-config` | [ui__display__display_switches](ui__display__display_switches.md) | Specifies the initial screen configuration, or state of all displays, for FakeDisplayDelegate, see class for format details. |
| `--screen-info` | [headless__public__switches](headless__public__switches.md) | Headless screen info in the format: {0,0 800x600}{800,0 600x800} |
| `--screen-info` | [ui__gfx__switches](ui__gfx__switches.md) | Headless screen info in the format: {0,0 800x600}{800,0 600x800} |
| `--screenshot` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Save a screenshot of the loaded page. |
| `--search-engine-choice-country` | [components__regional_capabilities__regional_capabilities_switches](components__regional_capabilities__regional_capabilities_switches.md) | Overrides the profile country (which is among other things used for search engine choice region checks for example) |
| `--search-provider-logo-url` | [components__search_provider_logos__switches](components__search_provider_logos__switches.md) | Use a static URL for the logo of the default search engine |
| `--secondary-display-layout` | [ui__display__display_switches](ui__display__display_switches.md) | Specifies the layout mode and offsets for the secondary display for testing |
| `--secure-connect-api-url` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | Specifies the base URL to contact the secure connect Api. |
| `--service-name` | [services__service_manager__public__cpp__service_executable__switches](services__service_manager__public__cpp__service_executable__switches.md) | All switches in alphabetical order |
| `--service-request-attachment-name` | [services__service_manager__public__cpp__service_executable__switches](services__service_manager__public__cpp__service_executable__switches.md) | The name of the \|mojo::PendingReceiver<service_manager::mojom::Service>\| message pipe handle that is attached to the incoming Mojo invitation received by the se |
| `--service-sandbox-type` | [sandbox__policy__switches](sandbox__policy__switches.md) | Type of sandbox to apply to the process running the service, one of the values in the next block. |
| `--set-extension-throttle-test-params` | [extensions__common__switches](extensions__common__switches.md) | Set the parameters for ExtensionURLLoaderThrottleBrowserTest. |
| `--setup` | [remoting__host__base__switches](remoting__host__base__switches.md) | Used in combination with \|kProcessTypeUrlForwarderConfigurator\| to set up the URL forwarder on Windows. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--shared-array-buffer-unrestricted-access-allowed` | [content__public__common__content_switches](content__public__common__content_switches.md) | *(only if `!BUILDFLAG(IS_ANDROID)`)* |
| `--shared-files` | [content__public__common__content_switches](content__public__common__content_switches.md) | Describes the file descriptors passed to a child process in the following list format:  <file_id>:<descriptor_id>,<file_id>:<descriptor_id>,.. |
| `--short-reporting-delay` | [components__embedder_support__switches](components__embedder_support__switches.md) | Sets the Reporting API delay to under a second to allow much quicker reports. |
| `--show-aggregated-damage` | [components__viz__common__switches](components__viz__common__switches.md) | Adds a DebugBorderDrawQuad to the top of the root RenderPass showing the damage rect after surface aggregation |
| `--show-autofill-signatures` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Annotates forms and fields with Autofill signatures. |
| `--show-autofill-type-predictions` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Annotates forms with Autofill field type predictions. |
| `--show-component-extension-options` | [extensions__common__switches](extensions__common__switches.md) | Makes component extensions appear in chrome://settings/extensions. |
| `--show-composited-layer-borders` | [cc__base__switches](cc__base__switches.md) | Debug visualizations |
| `--show-dc-layer-debug-borders` | [components__viz__common__switches](components__viz__common__switches.md) | kShowDCLayerDebugBorders shows the debug borders of the overlays and the damage rect after using overlays on Windows |
| `--show-fps-counter` | [cc__base__switches](cc__base__switches.md) | Draws a heads-up-display showing Frames Per Second as well as GPU memory usage |
| `--show-icons` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | See kHideIcons. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--show-layer-animation-bounds` | [cc__base__switches](cc__base__switches.md) | Renders a border that represents the bounding box for the layer's animation. |
| `--show-mac-overlay-borders` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Show borders around CALayers corresponding to overlays and partial damage. *(only if `BUILDFLAG(IS_MAC)`)* |
| `--show-overdraw-feedback` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Visualize overdraw by color-coding elements based on if they have other elements drawn underneath |
| `--show-property-changed-rects` | [cc__base__switches](cc__base__switches.md) | Show rects in the HUD around layers whose properties have changed. |
| `--show-screenspace-rects` | [cc__base__switches](cc__base__switches.md) | Show rects in the HUD around the screen-space transformed bounds of every layer. |
| `--show-surface-damage-rects` | [cc__base__switches](cc__base__switches.md) | Show rects in the HUD around damage as it is recorded into each render surface. |
| `--signed-out-ntp-modules` | [chrome__browser__new_tab_page__modules__modules_switches](chrome__browser__new_tab_page__modules__modules_switches.md) | Enables NTP modules on the signed out user experience |
| `--silent-debugger-extension-api` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Does not show an infobar when an extension attaches to a page using chrome.debugger page |
| `--silent-launch` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes Chrome to launch without opening any windows by default |
| `--simulate-browsing-data-lifetime` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Sets the BrowsingDataLifetime policy to a very short value (shorter than normally possible) for testing purposes. |
| `--simulate-critical-update` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Simulates a critical update being available. |
| `--simulate-idle-timeout` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Sets the IdleTimeout policy to a very short value (shorter than normally possible) for testing purposes. |
| `--simulate-lock-screen-smart-restart` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Causes the browser to simulate a screen lock event shortly after startup *(only if `!BUILDFLAG(IS_ANDROID)`)* |
| `--simulate-outdated` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Simulates that current version is outdated. |
| `--simulate-outdated-no-au` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Simulates that current version is outdated and auto-update is off. |
| `--simulate-update-error-code` | [chrome__browser__google__switches](chrome__browser__google__switches.md) | Simulates a GoogleUpdateErrorCode error by the update check |
| `--simulate-update-hresult` | [chrome__browser__google__switches](chrome__browser__google__switches.md) | Simulates a specific HRESULT error code returned by the update check |
| `--simulate-upgrade` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Simulates an update being available. |
| `--single-process` | [content__public__common__content_switches](content__public__common__content_switches.md) | Runs the renderer and plugins in the same process as the browser |
| `--single_process_host` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--site-per-process` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enforces a one-site-per-process security policy: * Each renderer process, for its whole lifetime, is dedicated to rendering pages for just one site |
| `--skia-font-cache-limit-mb` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies the max number of bytes that should be used by the skia font cache |
| `--skia-graphite-dawn-backend` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Specify which Dawn backend to use for Skia Graphite. |
| `--skia-graphite-vulkan-backend` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Specify using Skia Graphite with native Vulkan backend. |
| `--skia-resource-cache-limit-mb` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies the max number of bytes that should be used by the skia resource cache |
| `--skills-v2-origin` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) |  |
| `--slow-down-compositing-scale-factor` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Re-draw everything multiple times to simulate a much slower machine |
| `--slow-down-raster-scale-factor` | [cc__base__switches](cc__base__switches.md) | Re-rasters everything multiple times to simulate a much slower machine |
| `--source-app-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | When rendezvousing with an existing process, used to indicate that the StartupInfoW of the new Chrome process had dwFlags == STARTF_TITLEISAPPID *(only if `BUILDFLAG(IS_WIN)`)* |
| `--source-shortcut` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | When rendezvousing with an existing process, used to pass the path of the shortcut that launched the new Chrome process *(only if `BUILDFLAG(IS_WIN)`)* |
| `--source-shortcut-location` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the origin location of the shortcut that launched Chrome (e.g *(only if `BUILDFLAG(IS_WIN)`)* |
| `--ssl-key-log-file` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Causes SSL key material to be logged to the specified file for debugging purposes |
| `--ssl-version-max` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the maximum SSL/TLS version ("tls1.2" or "tls1.3"). |
| `--ssl-version-min` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the minimum SSL/TLS version ("tls1.2" or "tls1.3"). |
| `--start-fullscreen` | [content__public__common__content_switches](content__public__common__content_switches.md) | Specifies if the browser should start in fullscreen mode, like if the user had pressed F11 right after startup. |
| `--start-maximized` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Starts the browser maximized, regardless of any previous settings. |
| `--start-menu` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | *(only if `BUILDFLAG(IS_WIN)`)* |
| `--start-stack-profiler` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Starts the stack sampling profiler in the child process. |
| `--startup-foreground-launch` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Identifies Chrome instances that start in foreground mode at startup to record related metrics. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--storage-pressure-notification-interval` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Interval, in minutes, used for storage pressure notification throttling |
| `--stub` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--subproc-heap-profiling` | [components__heap_profiling__in_process__switches](components__heap_profiling__in_process__switches.md) | All switches in alphabetical order |
| `--suppress-performance-logs` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Suppresses GL_DEBUG_TYPE_PERFORMANCE log messages for web tests that can get sent to the JS console and cause unnecessary test failures due test output log expe |
| `--surface` | [cc__base__switches](cc__base__switches.md) |  |
| `--swiftshader` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) |  |
| `--swiftshader` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--swiftshader` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--swiftshader-webgl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--sync-deferred-startup-timeout-seconds` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | Allows overriding the deferred init fallback timeout. |
| `--sync-include-specifics` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | Controls whether the initial state of the "Capture Specifics" flag on chrome://sync-internals is enabled. |
| `--sync-protocol-log-buffer-size` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | Controls the number of ProtocolEvents that are buffered, and thus can be displayed on newly-opened chrome://sync-internals tabs. |
| `--sync-short-initial-retry-override` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | This flag causes sync to retry very quickly (see polling_constants.h) the when it encounters an error, as the first step towards exponential backoff. |
| `--sync-short-nudge-delay-for-test` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | This flag significantly shortens the delay between nudge cycles |
| `--sync-url` | [components__sync__base__command_line_switches](components__sync__base__command_line_switches.md) | Overrides the default server used for profile sync. |
| `--system-aec-enabled` | [media__base__media_switches](media__base__media_switches.md) | Enforce system audio echo cancellation. *(only if `BUILDFLAG(USE_CRAS)`)* |
| `--system-audio-capture-default_checked` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag sets the checkboxes for sharing system audio during window or screen capture to on by default |
| `--system-font-family` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Specifies system font family name *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--tab-capture-audio-default-unchecked` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | This flag sets the checkboxes for sharing audio during tab capture to off by default |
| `--TAIYAKI` | [components__regional_capabilities__regional_capabilities_switches](components__regional_capabilities__regional_capabilities_switches.md) | Special value for the `kSearchEngineChoiceCountry` command-line flag |
| `--target-device-scale-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows web tests to specify the target device scale for the test cases. |
| `--task-definition-file` | [components__record_replay__core__common__record_replay_switches](components__record_replay__core__common__record_replay_switches.md) |  |
| `--taskbar` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | *(only if `BUILDFLAG(IS_WIN)`)* |
| `--terminal-id` | [remoting__host__base__switches](remoting__host__base__switches.md) | Specifies the terminal ID associated with `--agent-status` or `--terminal-title`. |
| `--terminal-title` | [remoting__host__base__switches](remoting__host__base__switches.md) | Sets the title of the terminal tab via Mojo IPC. |
| `--test-child-process` | [base__base_switches](base__base_switches.md) | When running certain tests that spawn child processes, this switch indicates to the test framework that the current process is a child process. |
| `--test-gl-lib` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Flag used for Linux tests: for desktop GL bindings, try to load this GL library first, but fall back to regular library if loading fails. |
| `--test-memory-log-delay-in-minutes` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Custom delay for memory log |
| `--test-register-standard-scheme` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Register the provided scheme as a standard scheme. |
| `--test-third-party-cookie-phaseout` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) |  |
| `--test-type` | [content__public__common__content_switches](content__public__common__content_switches.md) | Type of the current test harness ("browser" or "ui" or "gpu"). |
| `--text-contrast` | [skia__ext__switches](skia__ext__switches.md) |  |
| `--text-gamma` | [skia__ext__switches](skia__ext__switches.md) |  |
| `--third-party-doodle-url` | [components__search_provider_logos__switches](components__search_provider_logos__switches.md) | Overrides the Doodle URL to use for third-party search engines |
| `--timeout` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | Issues a stop after the specified number of milliseconds |
| `--tint-composited-content` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Tint composited color. |
| `--tint-composited-content-modulate` | [components__viz__common__switches](components__viz__common__switches.md) | Modulates the debug compositor tint color so that damage and page flip updates are made clearly visible |
| `--tint-dc-layer` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Tint `SwapChainPresenter` with the following colors:  - Decode swap chain: blue - VP blit: magenta - VP blit w/ staging texture: orange - MF proxy surface: gree |
| `--tls1.2` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | TLS 1.2 mode for \|kSSLVersionMax\| and \|kSSLVersionMin\| switches. |
| `--tls1.3` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | TLS 1.3 mode for \|kSSLVersionMax\| and \|kSSLVersionMin\| switches. |
| `--top-chrome-touch-ui` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Controls touch-optimized UI layout for top chrome. |
| `--top-chrome-webui` | [content__public__common__content_switches](content__public__common__content_switches.md) | Indicates that this RenderProcess is hosting a Top Chrome WebUI. |
| `--top-controls-hide-threshold` | [cc__base__switches](cc__base__switches.md) | Percentage of the browser controls need to be hidden before they will auto hide. |
| `--top-controls-show-threshold` | [cc__base__switches](cc__base__switches.md) | Percentage of the browser controls need to be shown before they will auto show. |
| `--touch-devices` | [ui__events__event_switches](ui__events__event_switches.md) | Tells chrome to interpret events from these devices as touch events *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--touch-events` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable support for touch event feature detection. |
| `--touch-slop-distance` | [ui__events__event_switches](ui__events__event_switches.md) | Overrides touch slop distance for gesture detection |
| `--trace-buffer-handle` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Handle to the shared memory segment a child process should use to transmit tracing data back to the tracing service |
| `--trace-config-file` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Enables startup tracing by passing a file path containing the chrome Json tracing config as an argument |
| `--trace-config-handle` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Causes TRACE_EVENT flags to be recorded from startup, passing a SMB handle containing the serialized perfetto config |
| `--trace-perfetto-config` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Enables startup tracing by passing the perfetto config as an argument |
| `--trace-perfetto-config-file` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Enables startup tracing by passing a file path containing the perfetto config as an argument |
| `--trace-process-track-uuid` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Child process track uuid used by perfetto; this is chosen by the browser process and sent to child processes to get predictable track uuid. |
| `--trace-smb-size` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Configures the size of the shared memory buffer used for tracing |
| `--trace-startup` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Causes TRACE_EVENT flags to be recorded from startup |
| `--trace-startup-duration` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Sets the time in seconds until startup tracing ends |
| `--trace-startup-file` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | If supplied, sets the file which startup tracing will be stored into, if omitted the default will be used "chrome.pftrace" in the current directory |
| `--trace-startup-format` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Sets the output format for the trace, valid values are "json" and "proto" |
| `--trace-startup-owner` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | Specifies the coordinator of the startup tracing session |
| `--trace-startup-record-mode` | [components__tracing__common__tracing_switches](components__tracing__common__tracing_switches.md) | If supplied, sets the tracing record mode and options; otherwise, the default "record-until-full" mode will be used. |
| `--trace-to-file` | [base__base_switches](base__base_switches.md) | Sends trace events from these categories to a file |
| `--trace-to-file-name` | [base__base_switches](base__base_switches.md) | Specifies the file name for --trace-to-file |
| `--translate-ranker-model-url` | [components__translate__core__common__translate_switches](components__translate__core__common__translate_switches.md) | Overrides the URL from which the translate ranker model is downloaded. |
| `--translate-script-url` | [components__translate__core__common__translate_switches](components__translate__core__common__translate_switches.md) | Overrides the default server used for Google Translate. |
| `--translate-security-origin` | [components__translate__core__common__translate_switches](components__translate__core__common__translate_switches.md) | Overrides security-origin with which Translate runs in an isolated world. |
| `--trusted-download-sources` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Identifies a list of download sources as trusted, but only if proper group policy is set. |
| `--trusted-vault-service-url` | [components__trusted_vault__command_line_switches](components__trusted_vault__command_line_switches.md) | Specifies the vault server used for trusted vault passphrase. |
| `--try-supported-channel-layouts` | [media__base__media_switches](media__base__media_switches.md) | Instead of always using the hardware channel layout, check if a driver supports the source channel layout *(only if `BUILDFLAG(IS_WIN)`)* |
| `--ttc-bundle-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the TalkToChrome bundle URL. |
| `--type` | [content__public__common__content_switches](content__public__common__content_switches.md) | The value of this switch determines whether the process is started as a renderer or plugin host |
| `--type` | [remoting__host__base__switches](remoting__host__base__switches.md) | Used to specify the type of the process |
| `--type` | [sandbox__policy__switches](sandbox__policy__switches.md) | Flags spied upon from other layers. |
| `--ui-disable-partial-swap` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Disable partial swap which is needed for some OpenGL drivers / emulators. |
| `--ui-disable-zero-copy` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--ui-enable-rgba-4444-textures` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--ui-enable-zero-copy` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--ui-show-composited-layer-borders` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-show-fps-counter` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-show-layer-animation-bounds` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-show-paint-rects` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--ui-show-property-changed-rects` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-show-screenspace-rects` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-show-surface-damage-rects` | [cc__base__switches](cc__base__switches.md) |  |
| `--ui-slow-animations` | [ui__compositor__compositor_switches](ui__compositor__compositor_switches.md) |  |
| `--ui-toolkit` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Specify the toolkit used to construct the Linux GUI. *(only if `BUILDFLAG(IS_LINUX)`)* |
| `--ukm-server-url` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Overrides the URL of the server that UKM reports are uploaded to |
| `--uma-insecure-server-url` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Overrides the URL of the server that UMA reports are uploaded to when the connection to the default secure URL fails (see \|kUmaServerUrl\|) |
| `--uma-server-url` | [components__metrics__metrics_switches](components__metrics__metrics_switches.md) | Overrides the URL of the server that UMA reports are uploaded to |
| `--unattended-test` | [chrome__windows_services__service_program__switches](chrome__windows_services__service_program__switches.md) | A switch that indicates that the service is running on behalf of an unattended test (i.e., one for which CHROME_HEADLESS is set in its environment block). |
| `--unbounded-window-debug` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables debug mode for unbounded windows (draws a red border). |
| `--uninstall` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Runs un-installation steps that were done by chrome first-run. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--uninstall-app-id` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies that the WebApp with the specified id should be uninstalled. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--unique-temp-dir-suffix` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | When switches::kProcessType is switches::kCodeSignCloneCleanupProcess this switch is required *(only if `BUILDFLAG(IS_MAC)`)* |
| `--universal-optout-history-json-path` | [components__universal_optout__switches](components__universal_optout__switches.md) | Specifies a path to a JSON file containing custom eligibility history to override `prefs::kUniversalOptOutEligibilityHistory` for testing |
| `--unlimited-storage` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Overrides per-origin quota settings to unlimited storage for any apps/origins |
| `--unsafely-allow-protected-media-identifier-for-domain` | [media__base__media_switches](media__base__media_switches.md) | For automated testing of protected content, this switch allows specific domains (e.g |
| `--unsafely-disable-devtools-self-xss-warnings` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Disables warnings about self-XSS attacks when pasting into the DevTools console. |
| `--unsafely-treat-insecure-origin-as-secure` | [net__base__switches](net__base__switches.md) |  |
| `--unsafely-treat-insecure-origin-as-secure` | [services__network__public__cpp__network_switches](services__network__public__cpp__network_switches.md) | Treat given (insecure) origins as secure origins |
| `--url-filtering-endpoint` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) | Alternate URL to use for ChromeEnterpriseRealTimeUrlLookupService real-time lookups. |
| `--url_forwarder_configurator` | [remoting__host__base__switches](remoting__host__base__switches.md) |  |
| `--use-adapter-luid` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Initialize the GPU process using the adapter with the specified LUID |
| `--use-angle` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Select which ANGLE backend to use |
| `--use-cmd-decoder` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Use the Pass-through command decoder, skipping all validation and state tracking |
| `--use-context-snapshot` | [content__public__common__content_switches](content__public__common__content_switches.md) | Switch supplied to the renderer if the feature `kUseContextSnapshot` is enabled *(only if `BUILDFLAG(IS_ANDROID) && BUILDFLAG(INCLUDE_BOTH_V8_SNAPSHOTS)`)* |
| `--use-cras` | [media__base__media_switches](media__base__media_switches.md) | Use CRAS, the ChromeOS audio server. *(only if `BUILDFLAG(USE_CRAS)`)* |
| `--use-dynamic-angle` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Use ANGLE shared libraries even if ANGLE is built as a static library. *(only if `BUILDFLAG(USE_STATIC_ANGLE)`)* |
| `--use-fake-codec-for-peer-connection` | [content__public__common__content_switches](content__public__common__content_switches.md) | Replaces the existing codecs supported in peer connection with a single fake codec entry that create a fake video encoder and decoder. |
| `--use-fake-device-for-media-stream` | [media__base__media_switches](media__base__media_switches.md) | Use fake device for Media Stream to replace actual camera and microphone |
| `--use-fake-dmserver` | [components__policy__core__common__policy_switches](components__policy__core__common__policy_switches.md) | *(only if `!BUILDFLAG(GOOGLE_CHROME_BRANDING)`)* |
| `--use-fake-mjpeg-decode-accelerator` | [media__base__media_switches](media__base__media_switches.md) | Use a fake device for accelerated decoding of MJPEG |
| `--use-fake-ui-for-digital-identity` | [content__public__common__content_switches](content__public__common__content_switches.md) | Bypass the digital-identity-credential OS call |
| `--use-fake-ui-for-fedcm` | [content__public__common__content_switches](content__public__common__content_switches.md) | Bypass the FedCM account selection dialog |
| `--use-fake-ui-for-media-stream` | [content__public__common__content_switches](content__public__common__content_switches.md) | Bypass the media stream infobar by selecting the default device for media streams (e.g |
| `--use-file-for-fake-audio-capture` | [media__base__media_switches](media__base__media_switches.md) | Play a .wav file as the microphone |
| `--use-file-for-fake-video-capture` | [media__base__media_switches](media__base__media_switches.md) | Use an .y4m file to play as the webcam |
| `--use-first-display-as-internal` | [ui__display__display_switches](ui__display__display_switches.md) | Uses the 1st display in --ash-host-window-bounds as internal display |
| `--use-gl` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Select which implementation of GL the GPU process should use |
| `--use-gpu-in-tests` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Use hardware gpu, if available, for tests. |
| `--use-mobile-user-agent` | [components__embedder_support__switches](components__embedder_support__switches.md) | Set when Chromium should use a mobile user agent. |
| `--use-mock-cert-verifier-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Use the MockCertVerifier |
| `--use-mock-keychain` | [components__os_crypt__common__os_crypt_switches](components__os_crypt__common__os_crypt_switches.md) | Uses mock keychain for testing purposes, which prevents blocking dialogs from causing timeouts. *(only if `BUILDFLAG(IS_APPLE)`)* |
| `--use-peer-connection-process` | [remoting__host__base__switches](remoting__host__base__switches.md) | TODO(crbug.com/502281489): Remove this switch once the PC process is enabled by default *(only if `BUILDFLAG(IS_WIN)`)* |
| `--use-system-clipboard` | [ui__base__ui_base_switches](ui__base__ui_base_switches.md) | Enables the ozone x11 clipboard for linux-chromeos. |
| `--use-system-default-printer` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Uses the system default printer as the initially selected destination in print preview, instead of the most recently used destination. *(only if `!BUILDFLAG(IS_CHROMEOS) && !BUILDFLAG(IS_ANDROID)`)* |
| `--use-system-proxy-resolver` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Uses the operating system to resolve proxies instead of using Chromium's normal proxy resolution logic |
| `--use-va-dev-keys` | [components__enterprise__device_trust__core__attestation__attestation_switches](components__enterprise__device_trust__core__attestation__attestation_switches.md) |  |
| `--use-vulkan` | [gpu__command_buffer__service__gpu_switches](gpu__command_buffer__service__gpu_switches.md) | Enable Vulkan support and select Vulkan implementation, must also have ENABLE_VULKAN defined |
| `--use-wayland-explicit-grab` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Use explicit grab when opening popup windows |
| `--use-webgpu-adapter` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | The adapter to use for WebGPU content. |
| `--use-webgpu-power-preference` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | The adapter selecting strategy related to GPUPowerPreference. |
| `--user-agent` | [components__embedder_support__switches](components__embedder_support__switches.md) | A string used to override the default user agent with a custom one. |
| `--user-agent` | [headless__public__switches](headless__public__switches.md) | A string used to override the default user agent with a custom one. |
| `--user-data-dir` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies the user data directory, which is where the browser will look for all of its state. |
| `--user-data-dir` | [components__password_manager__core__browser__password_manager_switches](components__password_manager__core__browser__password_manager_switches.md) | Specifies the user data directory, which is where the browser will look for all of its state |
| `--user-data-dir` | [content__shell__common__shell_switches](content__shell__common__shell_switches.md) | Makes Content Shell use the given path for its data directory |
| `--user-data-dir` | [headless__public__switches](headless__public__switches.md) | Directory where the browser stores the user profile |
| `--user-data-migrated` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Indicates that this process is the product of a relaunch following migration of User Data. *(only if `BUILDFLAG(ENABLE_DOWNGRADE_PROCESSING)`)* |
| `--user-gesture-required` | [media__base__media_switches](media__base__media_switches.md) | Autoplay policy to require a user gesture in order to play. |
| `--utility` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the process to run as a utility subprocess. |
| `--utility` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--utility-cmd-prefix` | [content__public__common__content_switches](content__public__common__content_switches.md) | The contents of this flag are prepended to the utility process command line |
| `--utility-immediate-crash-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Crash the Utility process early in start-up, for testing. |
| `--utility-startup-dialog` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the utility process to display a dialog on launch. |
| `--utility-sub-type` | [content__public__common__content_switches](content__public__common__content_switches.md) | This switch indicates the type of a utility process |
| `--v` | [base__base_switches](base__base_switches.md) | Gives the default maximal active V-logging level; 0 is the default |
| `--v8-cache-options` | [content__public__common__content_switches](content__public__common__content_switches.md) | Set options to cache V8 data |
| `--validate-crx` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Examines a .crx for validity and prints the result. |
| `--validate-input-event-stream` | [components__input__switches](components__input__switches.md) | In debug builds, asserts that the stream of input events is valid. |
| `--validating` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | The command decoder names that can be passed to --use-cmd-decoder. |
| `--variations-insecure-server-url` | [components__variations__variations_switches](components__variations__variations_switches.md) | Specifies a custom URL for the server to use as an insecure fallback when requests to \|kVariationsServerURL\| fail |
| `--variations-override-country` | [components__variations__variations_switches](components__variations__variations_switches.md) | Allows overriding the country used for evaluating variations |
| `--variations-override-geo-level-1` | [components__variations__variations_switches](components__variations__variations_switches.md) | Allows overriding the administrative area code used for evaluating variations and regional eligibility features. |
| `--variations-seed-corpus` | [components__variations__variations_switches](components__variations__variations_switches.md) | Specifies the value of the variations seed corpus to use |
| `--variations-seed-fetch-interval` | [components__variations__variations_switches](components__variations__variations_switches.md) | Override the time interval between each variation seed fetches |
| `--variations-seed-version` | [components__variations__variations_switches](components__variations__variations_switches.md) | Used to share variations seed version with child processes. |
| `--variations-server-url` | [components__variations__variations_switches](components__variations__variations_switches.md) | Specifies a custom URL for the server which reports variation data to the client |
| `--variations-state-file` | [components__variations__variations_switches](components__variations__variations_switches.md) | Use features defined in the value |
| `--variations-test-seed-path` | [components__variations__variations_switches](components__variations__variations_switches.md) | Specifies the location of a seed file for Local State's seed to be populated from |
| `--version` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Prints version information and quits. |
| `--version` | [headless__public__switches](headless__public__switches.md) | Prints version information and quits. |
| `--version` | [remoting__host__base__switches](remoting__host__base__switches.md) | The command line switch used to get version of the daemon. |
| `--video-capture-use-gpu-memory-buffer` | [media__capture__capture_switches](media__capture__capture_switches.md) | Enables GpuMemoryBuffer-based buffer pool. |
| `--video-capture-use-virtual-devices-only` | [media__capture__capture_switches](media__capture__capture_switches.md) | Makes the video capture service ignore devices from the wrapped factory and expose only registered virtual devices. |
| `--video-image-texture-target` | [content__public__common__content_switches](content__public__common__content_switches.md) | Texture target for CHROMIUM_image backed video frame textures. |
| `--video-threads` | [media__base__media_switches](media__base__media_switches.md) | Set number of threads to use for video decoding. |
| `--view-stack-traces` | [ui__views__views_switches](ui__views__views_switches.md) | Captures stack traces on View construction to provide better debug info. |
| `--virtual-time-budget` | [components__headless__command_handler__headless_command_switches](components__headless__command_handler__headless_command_switches.md) | If set the system waits the specified number of virtual milliseconds before deeming the page to be ready |
| `--viz-demo-use-gpu` | [components__viz__demo__common__switches](components__viz__demo__common__switches.md) |  |
| `--vmodule` | [base__base_switches](base__base_switches.md) | Gives the per-module maximal V-logging levels to override the value given by --v |
| `--vulkan` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) |  |
| `--vulkan` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--vulkan-heap-memory-limit-mb` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Specifies the heap limit for Vulkan memory |
| `--vulkan-null` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--vulkan-sync-cpu-memory-limit-mb` | [gpu__config__gpu_switches](gpu__config__gpu_switches.md) | Specifies the sync CPU limit for total Vulkan memory |
| `--wait-for-debugger` | [base__base_switches](base__base_switches.md) | Will wait for 60 seconds for a debugger to come to attach to the process. |
| `--wait-for-debugger-children` | [content__public__common__content_switches](content__public__common__content_switches.md) | Will add kWaitForDebugger to every child processes |
| `--wait-for-debugger-on-navigation` | [content__public__common__content_switches](content__public__common__content_switches.md) | On every navigation a message with the renderer's URL will be logged and the renderer will wait for a debugger to be attached or SIGUSR1 to be sent to continue  |
| `--wait-for-debugger-webui` | [content__public__common__content_switches](content__public__common__content_switches.md) | Flag used by WebUI test runners to wait for debugger to be attached. |
| `--wait-for-parent-handle` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Passes the Win32 HANDLE value (as an integer) of the parent process to wait for during relaunch. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--wallet-service-use-sandbox` | [components__autofill__core__common__autofill_switches](components__autofill__core__common__autofill_switches.md) | Use the sandbox Online Wallet service URL (for developer testing). |
| `--waveout-buffers` | [media__base__media_switches](media__base__media_switches.md) | Number of buffers to use for WaveOut. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--wayland-text-input-version` | [ui__ozone__public__ozone_switches](ui__ozone__public__ozone_switches.md) | Specify wayland text-input protocol version |
| `--web-otp-backend` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables specified backend for the Web OTP API. |
| `--web-otp-backend-auto` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables auto backend selection for Web OTP API. |
| `--web-otp-backend-sms-verification` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables Sms Verification backend for Web OTP API which requires app hash in SMS body. |
| `--web-otp-backend-user-consent` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enables User Consent backend for Web OTP API. |
| `--web-settings-for-testing` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows web tests to specify additional web settings for the test cases. |
| `--webapk-server-url` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Custom WebAPK server URL for the sake of testing. *(only if `BUILDFLAG(IS_CHROMEOS) \|\| BUILDFLAG(IS_ANDROID)`)* |
| `--webauthn-gpm-magic-arch-url` | [chrome__browser__webauthn__webauthn_switches](chrome__browser__webauthn__webauthn_switches.md) | The domain for Magic Arch. |
| `--webauthn-permit-enterprise-attestation` | [chrome__browser__webauthn__webauthn_switches](chrome__browser__webauthn__webauthn_switches.md) | A list of origins that are permitted to request enterprise attestation when creating a WebAuthn credential. |
| `--webauthn-remote-desktop-support` | [content__public__common__content_switches](content__public__common__content_switches.md) | Allows trusted remote desktop clients to make WebAuthn requests on behalf of other origins |
| `--webauthn-remote-proxied-requests-allowed-additional-origin` | [chrome__browser__webauthn__webauthn_switches](chrome__browser__webauthn__webauthn_switches.md) | Allows specifying one additional origin for the WebAuthenticationRemoteProxiedRequestsAllowed enterprise policy |
| `--webgl-antialiasing-mode` | [content__public__common__content_switches](content__public__common__content_switches.md) | Set the antialiasing method used for webgl |
| `--webgl-msaa-sample-count` | [content__public__common__content_switches](content__public__common__content_switches.md) | Set a default sample count for webgl if msaa is enabled. |
| `--webnn-compiler-ep-device-info` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Used internally to pass the target EP device info from the browser process to the WebNN Compiler utility process, alongside `kWebNNCompilerEpLibrary` *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-compiler-ep-library` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Used internally to pass the target EP library path from the browser process to the WebNN Compiler utility process *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-coreml-dump-model` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Copy the generated Core ML model to the folder specified by --webnn-coreml-dump-model, note: folder needs to be accessible from the GPU sandbox or use --no-sand *(only if `BUILDFLAG(IS_MAC)`)* |
| `--webnn-ort-allow-all-compiler-devices` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Allow all EP devices to be selected for the Compiler process, regardless of whether `kKnownEPs` declares offline compilation support for them *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-disable-cpu-fallback` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | This switch allows us to disable the fallback to default ORT CPU EP which is enabled by default *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-disable-virtual-devices` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Disable ORT virtual devices in the Compiler process, requiring actual hardware devices for compilation instead *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-dump-model` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Set the folder specified by --webnn-ort-dump-model for ONNX Runtime to save optimized models after graph level transformations *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-enable-profiling` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | This switch allows us to collect ORT profile data for performance analysis *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-ep-device` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Force ONNX Runtime to only select one specific execution provider (EP) device which matches the given EP name, hardware vendor id and hardware device id for Web *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-ep-library-path-for-testing` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Specify one or more ORT EP name and library path pairs via this switch for testing development EP builds *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-graph-optimization-level` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Configure the graph optimization level of ONNX Runtime *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-ignore-ep-blocklist` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Enable all execution providers, ignoring the enabled flag blocklist. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-ignore-ihv-eps` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Ignore all IHV execution providers, only the default CPUExecutionProvider and DmlExecutionProvider will be used. *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-library-path-for-testing` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Force onnxruntime.dll to be loaded from a location specified by the switch for testing development ORT build *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-logging-level` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Configure the logging severity level of ONNX Runtime *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-ort-session-config-entries-for-testing` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Add arbitrary ONNX Runtime session configuration entries for testing *(only if `BUILDFLAG(IS_WIN)`)* |
| `--webnn-tflite-dump-model` | [services__webnn__webnn_switches](services__webnn__webnn_switches.md) | Save the generated TFLite model file to the folder specified by --webnn-tflite-dump-model *(only if `BUILDFLAG(WEBNN_USE_TFLITE) \|\| BUILDFLAG(WEBNN_USE_LITERT)`)* |
| `--webrtc-event-log-proactive-pruning-delta` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Sets the delay (in seconds) between proactive prunings of remote-bound WebRTC event logs which are pending upload |
| `--webrtc-event-log-upload-delay-ms` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | WebRTC event logs will only be uploaded if the conditions hold for this many milliseconds. |
| `--webrtc-event-log-upload-no-suppression` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Normally, remote-bound WebRTC event logs are uploaded only when no peer connections are active |
| `--webrtc-event-logging` | [content__public__common__content_switches](content__public__common__content_switches.md) | Enable capture and local storage of WebRTC event logs without visiting chrome://webrtc-internals |
| `--webrtc-ip-handling-policy` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Override WebRTC IP handling policy to mimic the behavior when WebRTC IP handling policy is specified in Preferences. |
| `--webview-draw-functor-uses-vulkan` | [ui__gl__gl_switches](ui__gl__gl_switches.md) | Indicate that the this is being used by Android WebView and its draw functor is using vulkan. |
| `--webxr-hand-anonymization-strategy` | [device__vr__public__cpp__switches](device__vr__public__cpp__switches.md) |  |
| `--webxr-max-framebuffer-scale` | [device__vr__public__cpp__switches](device__vr__public__cpp__switches.md) |  |
| `--whats-new-use-staging` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Force What's New on Desktop to request from the staging environment. |
| `--win-jumplist-action` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specifies which category option was clicked in the Windows Jumplist that resulted in a browser startup. |
| `--window-name` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specify the initial window user title: --window-name="My custom title" |
| `--window-position` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specify the initial window position: --window-position=x,y |
| `--window-size` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specify the initial window size: --window-size=w,h |
| `--window-size` | [headless__public__switches](headless__public__switches.md) | Sets the initial window size |
| `--window-workspace` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Specify the initial window workspace: --window-workspace=id |
| `--winhttp-proxy-resolver` | [chrome__common__chrome_switches](chrome__common__chrome_switches.md) | Uses WinHTTP to fetch and evaluate PAC scripts |
| `--wipe-recordings` | [components__record_replay__core__common__record_replay_switches](components__record_replay__core__common__record_replay_switches.md) |  |
| `--wm-window-animations-disabled` | [ui__wm__core__wm_core_switches](ui__wm__core__wm_core_switches.md) | Please keep alphabetized |
| `--wp-max-file-opening-threads` | [components__safe_browsing__core__common__safebrowsing_switches](components__safe_browsing__core__common__safebrowsing_switches.md) |  |
| `--xsession_chooser` | [remoting__host__base__switches](remoting__host__base__switches.md) | *(only if `BUILDFLAG(IS_LINUX) \|\| BUILDFLAG(IS_CHROMEOS)`)* |
| `--yuy2` | [ui__gl__gl_switches](ui__gl__gl_switches.md) |  |
| `--zygote` | [content__public__common__content_switches](content__public__common__content_switches.md) | Causes the process to run as a zygote. |
| `--zygote` | [sandbox__policy__switches](sandbox__policy__switches.md) |  |
| `--zygote-cmd-prefix` | [content__public__common__content_switches](content__public__common__content_switches.md) | The prefix used when starting the zygote process |
