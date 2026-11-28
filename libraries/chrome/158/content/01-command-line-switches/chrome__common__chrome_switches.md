# Command-line switches: `chrome/common/chrome_switches`

Generated from `chrome/common/chrome_switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

242 switches.

## `--accept-lang`

- Constant: `kAcceptLang`

Specifies Accept-Language to send to servers and expose to JavaScript via the navigator.language DOM property. language[-country] where language is the 2 letter code from ISO-639.

## `--allow-appshim-signature-mismatch-for-tests`

- Constant: `kAllowAppShimSignatureMismatchForTests`
- Condition: `BUILDFLAG(IS_MAC)`

Only if we're running in an unsigned build, passing this flag will allow app shims whose code signature does not match what chrome is expecting to still connect to chrome. This is used by some tests to allow the test to pretend to be a valid app shim.

## `--allow-cross-origin-auth-prompt`

- Constant: `kAllowCrossOriginAuthPrompt`

Allows third-party content included on a page to prompt for a HTTP basic auth username/password pair.

## `--allow-http-screen-capture`

- Constant: `kAllowHttpScreenCapture`

Allow non-secure origins to use the screen capture API and the desktopCapture extension API.

## `--allow-running-insecure-content`

- Constant: `kAllowRunningInsecureContent`

By default, an https page cannot run JavaScript, CSS or plugins from http URLs. This provides an override to get the old insecure behavior.

## `--allow-silent-push`

- Constant: `kAllowSilentPush`

Allows Web Push notifications that do not show a notification.

## `--allow-unpacked-perfetto-extension`

- Constant: `kAllowUnpackedPerfettoExtension`

Allows an unpacked Perfetto UI extension to be trusted.

## `--allow-unsafe-devtools-remote-file-loading`

- Constant: `kAllowUnsafeDevToolsRemoteFileLoading`

Allows DevTools frontend from remote origins to load local file:// resources. This should only be enabled when explicitly needed for remote debugging with local source maps.

## `--app`

- Constant: `kApp`

Specifies that the associated value should be launched in "application" mode.

## `--app-id`

- Constant: `kAppId`

Specifies that the extension-app with the specified id should be launched according to its configuration.

## `--app-launch-url-for-shortcuts-menu-item`

- Constant: `kAppLaunchUrlForShortcutsMenuItem`

Overrides the launch url of an app with the specified url. This is used along with kAppId to launch a given app with the url corresponding to an item in the app's shortcuts menu.

## `--app-run-on-os-login-mode`

- Constant: `kAppRunOnOsLoginMode`

This is used along with kAppId to indicate an app was launched during OS login, and which mode the app was launched in.

## `--app-shim`

- Constant: `kAppShim`

A process type (switches::kProcessType) that is used by App Shim processes. See chrome/app_shim/app_shim_main_delegate.mm.

## `--apps-gallery-update-url`

- Constant: `kAppsGalleryUpdateURL`

Overrides the update url used by webstore extensions.

## `--auth-server-allowlist`

- Constant: `kAuthServerAllowlist`

Allowlist for Negotiate Auth servers

## `--auto-open-devtools-for-tabs`

- Constant: `kAutoOpenDevToolsForTabs`

This flag makes Chrome auto-open DevTools window for each tab. It is intended to be used by developers and automation to not require user interaction for opening DevTools.

## `--auto-select-desktop-capture-source`

- Constant: `kAutoSelectDesktopCaptureSource`

This flag makes Chrome auto-select the provided choice when an extension asks permission to start desktop capture. Should only be used for tests. For instance, --auto-select-desktop-capture-source="Entire screen" will automatically select sharing the entire screen in English locales. The switch value only needs to be substring of the capture source name, i.e. "display" would match "Built-in display" and "External display", whichever comes first.

## `--auto-select-screen-capture-source`

- Constant: `kAutoSelectScreenCaptureSource`

This flag makes Chrome auto-select any screen when an extension asks permission to start desktop capture. Should only be used for tests. kAutoSelectDesktopCaptureSource (see above) can be also be used to auto-select screens. But it have the problem that you need to know the name of a screen to auto-select it. The name of screens can't be set, are different for different platforms, and are different if you have one or several screens. So it's hard to use for auto-selecting screens. This flag does not care what the screen name is, but it also gives no control. Any screen could be chosen. It is useful in tests where we don't care which screen is auto-selected.

## `--auto-select-tab-capture-source-by-title`

- Constant: `kAutoSelectTabCaptureSourceByTitle`

This flag makes Chrome auto-select a tab with the provided title when the media-picker should otherwise be displayed to the user. This switch is very similar to kAutoSelectDesktopCaptureSource, but limits selection to tabs. This solves the issue of kAutoSelectDesktopCaptureSource being liable to accidentally capturing the Chromium window instead of the tab, as both have the same title if the tab is focused.

## `--auto-select-window-capture-source-by-title`

- Constant: `kAutoSelectWindowCaptureSourceByTitle`

This flag makes Chrome auto-select a window with the provided title when the media-picker should otherwise be displayed to the user. This switch is very similar to kAutoSelectDesktopCaptureSource, but limits selection to the window.

## `--auto-accept-browser-signin-for-tests`

- Constant: `kBrowserSigninAutoAccept`

Automatically signs the user into Chrome when signing in to other Google services on the web. This makes it easier for automated browsers to sign in.

## `--bypass-account-already-used-by-another-profile-check`

- Constant: `kBypassAccountAlreadyUsedByAnotherProfileCheck`

If specified, allows syncing multiple profiles to the same account. Used for multi-client E2E tests.

## `--auto-reject-capture`

- Constant: `kCaptureAutoReject`

This flag makes Chrome auto-reject requests capture a tab/window/screen.

## `--check-for-update-interval`

- Constant: `kCheckForUpdateIntervalSec`

How often (in seconds) to check for updates. Should only be used for testing purposes.

## `--cipher-suite-blacklist`

- Constant: `kCipherSuiteBlacklist`

Comma-separated list of SSL cipher suites to disable.

## `--credits`

- Constant: `kCredits`

Prints licensing information (same content as found in about:credits) and quits.

## `--custom-devtools-frontend`

- Constant: `kCustomDevtoolsFrontend`

Specifies the http:// endpoint which will be used to serve devtools://devtools/custom/<path> Or a file:// URL to specify a custom file path to load from for devtools://devtools/bundled/<path>

## `--debug-packed-apps`

- Constant: `kDebugPackedApps`

Adds debugging entries such as Inspect Element to context menus of packed apps.

## `--devtools-flags`

- Constant: `kDevToolsFlags`

Passes command line parameters to the DevTools front-end.

## `--devtools-navigation-gating-rules`

- Constant: `kDevToolsNavigationGatingRules`

Specifies a stringified JSON dictionary defining allowlist and blocklist pattern rules for DevTools-controlled navigations. If an allowlist is provided (even if empty), all top-level navigations to non-matching URLs are blocked. If both allowlist and blocklist match a URL, the more specific pattern determines the outcome. Example: '{ \ "allowlist": ["[*.]foo.com"], \ "blocklist": ["[*.]bar.com"] \ }'

## `--diagnostics`

- Constant: `kDiagnostics`

Triggers a plethora of diagnostic modes.

## `--diagnostics-format`

- Constant: `kDiagnosticsFormat`

Sets the output format for diagnostic modes enabled by diagnostics flag.

## `--diagnostics-recovery`

- Constant: `kDiagnosticsRecovery`

Tells the diagnostics mode to do the requested recovery step(s).

## `--disable-auto-maximize-for-tests`

- Constant: `kDisableAutoMaximizeForTests`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Disables the auto maximize feature on ChromeOS so that a browser window always starts in normal state. This is used by tests that do not want this auto maximizing behavior.

## `--disable-auto-reload`

- Constant: `kDisableAutoReload`

Disable auto-reload of pages on top-level error.

## `--disable-background-networking`

- Constant: `kDisableBackgroundNetworking`

Disable several subsystems which run network requests in the background. This is for use when doing network performance testing to avoid noise in the measurements.

## `--disable-component-extensions-with-background-pages`

- Constant: `kDisableComponentExtensionsWithBackgroundPages`

Disable default component extensions with background pages - useful for performance tests where these pages may interfere with perf results.

## `--disable-component-update`

- Constant: `kDisableComponentUpdate`

_No description in the source._

## `--disable-crashpad-for-testing`

- Constant: `kDisableCrashpadForTesting`

Disables crashpad initialization for testing. The crashpad binary will not run, and thus will not detect and symbolize crashes.

## `--disable-default-apps`

- Constant: `kDisableDefaultApps`

Disables installation of default apps on first run. This is used during automated testing.

## `--disable-domain-reliability`

- Constant: `kDisableDomainReliability`

Disables Domain Reliability Monitoring.

## `--disable-lazy-loading`

- Constant: `kDisableLazyLoading`

Disables lazy loading of images and frames.

## `--disable-print-preview`

- Constant: `kDisablePrintPreview`

Disables print preview (For testing, and for users who don't like us. :[ )

## `--disable-prompt-on-repost`

- Constant: `kDisablePromptOnRepost`

Normally when the user attempts to navigate to a page that was the result of a post we prompt to make sure they want to. This switch may be used to disable that check. This switch is used during automated testing.

## `--disable-stack-profiler`

- Constant: `kDisableStackProfiler`

Disable stack profiling. Stack profiling may change performance. Disabling stack profiling is beneficial when comparing performance metrics with a build that has it disabled by default.

## `--disable-updater-scheduler`

- Constant: `kDisableUpdaterScheduler`

Disable startup of the updater process.

## `--disk-cache-dir`

- Constant: `kDiskCacheDir`

Use a specific disk cache location, rather than one derived from the UserDatadir.

## `--disk-cache-size`

- Constant: `kDiskCacheSize`

Forces the maximum disk space to be used by the disk cache, in bytes.

## `--do-not-create-nsapp-for-tests`

- Constant: `kDoNotCreateNSAppForTests`
- Condition: `BUILDFLAG(IS_MAC)`

Skips initializing the shares NSApplication instance in ChromeTestSuite.

## `--do-not-de-elevate`

- Constant: `kDoNotDeElevateOnLaunch`

Do not de-elevate the browser on launch. Used after de-elevating to prevent infinite loops.

## `--dump-browser-histograms`

- Constant: `kDumpBrowserHistograms`

Requests that a running browser process dump its collected histograms to a given file. The file is overwritten if it exists.

## `--enable-audio-debug-recordings-from-extension`

- Constant: `kEnableAudioDebugRecordingsFromExtension`

If the WebRTC logging private API is active, enables audio debug recordings.

## `--enable-auto-reload`

- Constant: `kEnableAutoReload`

Enable auto-reload of pages on top-level error.

## `--enable-bookmark-undo`

- Constant: `kEnableBookmarkUndo`

Enables the multi-level undo system for bookmarks.

## `--enable-domain-reliability`

- Constant: `kEnableDomainReliability`

Enables Domain Reliability Monitoring.

## `--enable-devtools-pwa-handler`

- Constant: `kEnableDevToolsPwaHandler`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

If enabled, DevTools will allow creating pwa_handler, to enable executing CDP methods (i.e. PWA.install) on browsers connected remotely

## `--enable-extension-activity-logging`

- Constant: `kEnableExtensionActivityLogging`

Enables logging for extension activity.

## `--enable-extension-activity-log-testing`

- Constant: `kEnableExtensionActivityLogTesting`

_No description in the source._

## `--enable-hangout-services-extension-for-testing`

- Constant: `kEnableHangoutServicesExtensionForTesting`

Force enabling HangoutServicesExtension.

## `--enable-net-benchmarking`

- Constant: `kEnableNetBenchmarking`

Enables the network-related benchmarking extensions.

## `--enable-potentially-annoying-security-features`

- Constant: `kEnablePotentiallyAnnoyingSecurityFeatures`

Enables a number of potentially annoying security features (strict mixed content mode, powerful feature restrictions, etc.)

## `--ai-overlay-dialog-test-mode`

- Constant: `kAiOverlayDialogTestMode`

Enables test mode for the AI overlay dialog, which automatically opens the dialog on browser startup and exposes programmatic test APIs to WebUI.

## `--experimental-ai-stable-channel`

- Constant: `kExperimentalAiStableChannel`

Allows experimental ai extension APIs to be used in stable channel. This disables chrome sign-in if set, regardless of channel.

## `--explicitly-allowed-ports`

- Constant: `kExplicitlyAllowedPorts`

Allows overriding the list of restricted ports by passing a comma-separated list of port numbers.

## `--enable-extension-ai-data-collection`

- Constant: `kExtensionAiDataCollection`

Name of the command line flag to allow the ai data collection extension API.

## `--extension-content-verification`

- Constant: `kExtensionContentVerification`

Name of the command line flag to force content verification to be on in one of various modes.

## `--bootstrap`

- Constant: `kExtensionContentVerificationBootstrap`

Values for the kExtensionContentVerification flag. See ContentVerifierDelegate::Mode for more explanation.

## `--enforce`

- Constant: `kExtensionContentVerificationEnforce`

_No description in the source._

## `--enforce_strict`

- Constant: `kExtensionContentVerificationEnforceStrict`

_No description in the source._

## `--enable-extension-actor-api`

- Constant: `kExtensionExperimentalActor`

Name of the command line flag to allow the experimental actor API.

## `--force-app-mode`

- Constant: `kForceAppMode`

Specifies the variation of Zero State extensions toolbar recommendation to show. When a user with zero extensions installed clicks on the extensions puzzle piece in the Chrome toolbar, Chrome displays a submenu suggesting the user to explore the Chrome Web Store. Forces application mode. This hides certain system UI elements and forces the app to be installed if it hasn't been already.

## `--force-first-run`

- Constant: `kForceFirstRun`

Displays the First Run experience when the browser is started, regardless of whether or not it's actually the First Run (this overrides kNoFirstRun).

## `--refresh-platform-policy`

- Constant: `kRefreshPlatformPolicy`

Forces immediate platform policy refresh (not cloud policy) when Chrome is already running. The switch prevents a new browser window from opening and only triggers the policy refresh. Useful for testing and automation to avoid waiting for the next scheduled refresh interval. No-op if Chrome is not already running.

## `--force-whats-new`

- Constant: `kForceWhatsNew`

Displays the What's New experience when the browser is started if it has not yet been shown for the current milestone (this overrides kNoFirstRun, without showing the First Run experience).

## `--hide-crash-restore-bubble`

- Constant: `kHideCrashRestoreBubble`

Does not show the crash restore bubble when the browser is started during the system startup phase in ChromeOS, if the ChromeOS full restore feature is enabled, because the ChromeOS full restore notification is shown for the user to select restore or not.

## `--homepage`

- Constant: `kHomePage`

Specifies which page will be displayed in newly-opened tabs. We need this for testing purposes so that the UI tests don't depend on what comes up for http://google.com.

## `--simulate-lock-screen-smart-restart`

- Constant: `kSimulateLockScreenSmartRestart`
- Condition: `!BUILDFLAG(IS_ANDROID)`

Causes the browser to simulate a screen lock event shortly after startup. Optional value specifies the delay in seconds (defaults to 5). Used for manual testing of Smart Restart.

## `--import-passwords`

- Constant: `kImportPasswords`
- Condition: `!BUILDFLAG(IS_ANDROID)`

Triggers the import of passwords on startup.

## `--incognito`

- Constant: `kIncognito`

Causes the initial browser opened to be in incognito mode. Further browsers may or may not be in incognito mode; see `IncognitoModePrefs`.

## `--init-isolate-as-foreground`

- Constant: `kInitIsolateAsForeground`

Specifies that the main-thread Isolate should initialize in foreground mode. If not specified, the the Isolate will start in background mode for extension processes and foreground mode otherwise.

## `--install-autogenerated-theme`

- Constant: `kInstallAutogeneratedTheme`

Installs an autogenerated theme based on the given RGB value. The format is "r,g,b", where r, g, b are a numeric values from 0 to 255.

## `--install-chrome-app`

- Constant: `kInstallChromeApp`

Causes Chrome to initiate an installation flow for the given app.

## `--install-isolated-web-app-from-file`

- Constant: `kInstallIsolatedWebAppFromFile`

Causes Chrome to install the unsigned Web Bundle at the given path as a developer mode Isolated Web App.

## `--install-isolated-web-app-from-url`

- Constant: `kInstallIsolatedWebAppFromUrl`

Causes Chrome to install a developer mode Isolated Web App whose contents are hosted at the given HTTP(S) URL.

## `--instant-process`

- Constant: `kInstantProcess`

Marks a renderer as an Instant process.

## `--keep-alive-for-test`

- Constant: `kKeepAliveForTest`

Used for testing - keeps browser alive after last browser window closes.

## `--kiosk`

- Constant: `kKioskMode`

Enable kiosk mode. Please note this is not Chrome OS kiosk mode.

## `--kiosk-printing`

- Constant: `kKioskModePrinting`

Enable automatically pressing the print button in print preview.

## `--make-default-browser`

- Constant: `kMakeDefaultBrowser`

Makes Chrome default browser

## `--native-messaging-connect-host`

- Constant: `kNativeMessagingConnectHost`

Requests a native messaging connection be established between the native messaging host named by this switch and the extension with ID specified by kNativeMessagingConnectExtension.

## `--native-messaging-connect-extension`

- Constant: `kNativeMessagingConnectExtension`

Requests a native messaging connection be established between the extension with ID specified by this switch and the native messaging host named by the kNativeMessagingConnectHost switch.

## `--native-messaging-connect-id`

- Constant: `kNativeMessagingConnectId`

If set when kNativeMessagingConnectHost and kNativeMessagingConnectExtension are specified, is reflected to the native messaging host as a command line parameter.

## `--no-default-browser-check`

- Constant: `kNoDefaultBrowserCheck`

Disables the default browser check. Useful for UI/browser tests where we want to avoid having the default browser info-bar displayed.

## `--no-experiments`

- Constant: `kNoExperiments`

Disables all experiments set on about:flags. Does not disable about:flags itself. Useful if an experiment makes chrome crash at startup: One can start chrome with --no-experiments, disable the problematic lab at about:flags and then restart chrome without this switch again.

## `--no-first-run`

- Constant: `kNoFirstRun`

Skip First Run tasks as well as not showing additional dialogs, prompts or bubbles. Suppressing dialogs, prompts, and bubbles is important as this switch is used by automation (including performance benchmarks) where it's important only a browser window is shown.  This may not actually be the first run or the What's New page. Its effect can be partially ignored by adding kForceFirstRun (for FRE), kForceWhatsNew (for What's New) and/or kIgnoreNoFirstRunForSearchEngineChoiceScreen (for the DSE choice screen). This does not drop the First Run sentinel and thus doesn't prevent first run from occurring the next time chrome is launched without this flag. It also does not update the last What's New milestone, so does not prevent What's New from occurring the next time chrome is launched without this flag.

## `--no-pings`

- Constant: `kNoPings`

Don't send hyperlink auditing pings

## `--no-proxy-server`

- Constant: `kNoProxyServer`

Don't use a proxy server, always make direct connections. Overrides any other proxy server flags that are passed.

## `--no-startup-window`

- Constant: `kNoStartupWindow`

Does not automatically open a browser window on startup (used when launching Chrome for the purpose of hosting background apps).

## `--notebook-home-url`

- Constant: `kNotebookHomeURL`

Overrides the default URL for the Notebook Home WebUI.

## `--ntp-process`

- Constant: `kNtpProcess`

Marks a renderer as a New Tab Page process.

## `--on-the-fly-mhtml-hash-computation`

- Constant: `kOnTheFlyMhtmlHashComputation`

Calculate the hash of an MHTML file as it is being saved. The browser process will write the serialized MHTML contents to a file and calculate its hash as it is streamed back from the renderer via a Mojo data pipe.

## `--omnibox-everywhere`

- Constant: `kOmniboxEverywhere`

Directly launches the Omnibox Everywhere desktop UI widget.

## `--open-in-background`

- Constant: `kOpenInBackground`

Opens the URLs given on the command line as background tabs, without activating or raising the browser window they are added to, so that handing a URL to an already-running browser does not take the user's focus. A window created to host the URLs is still shown and activated, and so is the first tab added to an empty window.

## `--new-window`

- Constant: `kOpenInNewWindow`

Launches URL in new browser window.

## `--focus`

- Constant: `kFocus`

Activates an existing tab or app window by URL or app id before creating anything new. Syntax: comma-ordered selectors. Bare URLs are exact. Add a trailing * for prefix. app:<app-id> targets PWAs. Example: --focus=https://meet.google.com/*,app:abc123

## `--focus-result-file`

- Constant: `kFocusResultFile`

Specifies a file path to write JSON focus result information.

## `--pack-extension`

- Constant: `kPackExtension`

Packages an extension to a .crx installable file from a given directory.

## `--pack-extension-key`

- Constant: `kPackExtensionKey`

Optional PEM private key to use in signing packaged .crx.

## `--pre-crashpad-crash-test`

- Constant: `kPreCrashpadCrashTest`

Causes the browser process to crash very early in startup, just before crashpad (or breakpad) is initialized.

## `--prediction-service-mock-likelihood`

- Constant: `kPredictionServiceMockLikelihood`

Used to mock the response received from the Web Permission Prediction Service. Used for testing.

## `--preinstalled-web-apps-dir`

- Constant: `kPreinstalledWebAppsDir`

A directory where Chrome looks for json files describing default/preinstalled web apps. This overrides any default directory to load preinstalled web apps from.

## `--privet-ipv6-only`

- Constant: `kPrivetIPv6Only`

Use IPv6 only for privet HTTP.

## `--product-version`

- Constant: `kProductVersion`

Outputs the product version information and quit. Used as an internal api to detect the installed version of Chrome on Linux.

## `--profile-directory`

- Constant: `kProfileDirectory`

Selects directory of profile to associate with the first browser launched.

## `--ignore-profile-directory-if-not-exists`

- Constant: `kIgnoreProfileDirectoryIfNotExists`

If provided with kProfileDirectory, does not create the profile if the profile directory doesn't exist.

## `--profile-email`

- Constant: `kProfileEmail`

Like kProfileDirectory, but selects the profile by email address. If the email is not found in any existing profile, this switch has no effect. If both kProfileDirectory and kProfileEmail are specified, kProfileDirectory takes priority.

## `--create-profile-email-if-not-exists`

- Constant: `kCreateProfileEmailIfNotExists`

If provided with kProfileEmail, prompts the user to create a new profile with kProfileEmail as the email address if that email is not found in any existing profile.

## `--proxy-auto-detect`

- Constant: `kProxyAutoDetect`

Forces proxy auto-detection.

## `--proxy-bypass-list`

- Constant: `kProxyBypassList`

Specifies a list of hosts for whom we bypass proxy settings and use direct connections. Ignored if --proxy-auto-detect or --no-proxy-server are also specified. This is a comma-separated list of bypass rules. See: "net/proxy_resolution/proxy_host_matching_rules.h" for the format of these rules.

## `--proxy-pac-url`

- Constant: `kProxyPacUrl`

Uses the pac script at the given URL

## `--proxy-server`

- Constant: `kProxyServer`

Uses a specified proxy server, overrides system settings.

## `--remote-debugging-targets`

- Constant: `kRemoteDebuggingTargets`

Provides a list of addresses to discover DevTools remote debugging targets. The format is <host>:<port>,...,<host>:port.

## `--repair-all-valid-extensions`

- Constant: `kRepairAllValidExtensions`

Indicates that all corrupted extensions should be repaired if they are are enabled by policy. This is mainly used after a user data downgrade.

## `--restart`

- Constant: `kRestart`

Indicates that Chrome was restarted (e.g., after a flag change). This is used to ignore the launch when recording the Launch.Mode2 metric.

## `--restore-last-session`

- Constant: `kRestoreLastSession`

Indicates the last session should be restored on startup. This overrides the preferences value. Note that this does not force automatic session restore following a crash, so as to prevent a crash loop. This switch is used to implement support for OS-specific "continue where you left off" functionality on OS X and Windows.

## `--same-tab`

- Constant: `kSameTab`

Indicates that the URL in the command line should open in the active tab instead of a new tab. In case of multiple URLS given as arguments, the first one will replace the active tab.

## `--silent-debugger-extension-api`

- Constant: `kSilentDebuggerExtensionAPI`

Does not show an infobar when an extension attaches to a page using chrome.debugger page. Required to attach to extension background pages.

## `--silent-launch`

- Constant: `kSilentLaunch`

Causes Chrome to launch without opening any windows by default. Useful if one wishes to use Chrome as an ash server.

## `--simulate-browsing-data-lifetime`

- Constant: `kSimulateBrowsingDataLifetime`

Sets the BrowsingDataLifetime policy to a very short value (shorter than normally possible) for testing purposes.

## `--simulate-critical-update`

- Constant: `kSimulateCriticalUpdate`

Simulates a critical update being available.

## `--simulate-outdated`

- Constant: `kSimulateOutdated`

Simulates that current version is outdated.

## `--simulate-outdated-no-au`

- Constant: `kSimulateOutdatedNoAU`

Simulates that current version is outdated and auto-update is off.

## `--simulate-upgrade`

- Constant: `kSimulateUpgrade`

Simulates an update being available.

## `--simulate-idle-timeout`

- Constant: `kSimulateIdleTimeout`

Sets the IdleTimeout policy to a very short value (shorter than normally possible) for testing purposes.

## `--ssl-version-max`

- Constant: `kSSLVersionMax`

Specifies the maximum SSL/TLS version ("tls1.2" or "tls1.3").

## `--ssl-version-min`

- Constant: `kSSLVersionMin`

Specifies the minimum SSL/TLS version ("tls1.2" or "tls1.3").

## `--tls1.2`

- Constant: `kSSLVersionTLSv12`

TLS 1.2 mode for |kSSLVersionMax| and |kSSLVersionMin| switches.

## `--tls1.3`

- Constant: `kSSLVersionTLSv13`

TLS 1.3 mode for |kSSLVersionMax| and |kSSLVersionMin| switches.

## `--start-maximized`

- Constant: `kStartMaximized`

Starts the browser maximized, regardless of any previous settings.

## `--start-stack-profiler`

- Constant: `kStartStackProfiler`

Starts the stack sampling profiler in the child process.

## `--browser-test`

- Constant: `kStartStackProfilerBrowserTest`

Browser test mode for the |kStartStackProfiler| switch. Limits the profile durations to be significantly less than the test timeout. On ChromeOS, forces the stack sampling profiler to run on all processes as well.

## `--storage-pressure-notification-interval`

- Constant: `kStoragePressureNotificationInterval`

Interval, in minutes, used for storage pressure notification throttling. Useful for developers testing applications that might use non-trivial amounts of disk space.

## `--system-audio-capture-default_checked`

- Constant: `kSystemAudioCaptureDefaultChecked`

This flag sets the checkboxes for sharing system audio during window or screen capture to on by default. It is primarily intended to be used for tests.

## `--tab-capture-audio-default-unchecked`

- Constant: `kTabCaptureAudioDefaultUnchecked`

This flag sets the checkboxes for sharing audio during tab capture to off by default. It is primarily intended to be used for tests.

## `--auto-accept-this-tab-capture`

- Constant: `kThisTabCaptureAutoAccept`

These flags make Chrome auto-accept/reject requests to capture the current tab. It should only be used for tests.

## `--auto-reject-this-tab-capture`

- Constant: `kThisTabCaptureAutoReject`

_No description in the source._

## `--test-memory-log-delay-in-minutes`

- Constant: `kTestMemoryLogDelayInMinutes`

Custom delay for memory log. This should be used only for testing purpose.

## `--trusted-download-sources`

- Constant: `kTrustedDownloadSources`

Identifies a list of download sources as trusted, but only if proper group policy is set.

## `--ttc-bundle-url`

- Constant: `kTtcBundleUrl`

Specifies the TalkToChrome bundle URL.

## `--unlimited-storage`

- Constant: `kUnlimitedStorage`

Overrides per-origin quota settings to unlimited storage for any apps/origins.  This should be used only for testing purpose.

## `--unsafely-disable-devtools-self-xss-warnings`

- Constant: `kUnsafelyDisableDevToolsSelfXssWarnings`

Disables warnings about self-XSS attacks when pasting into the DevTools console.

## `--user-data-dir`

- Constant: `kUserDataDir`

Specifies the user data directory, which is where the browser will look for all of its state.

## `--use-system-proxy-resolver`

- Constant: `kUseSystemProxyResolver`

Uses the operating system to resolve proxies instead of using Chromium's normal proxy resolution logic. On Windows this uses WinHttp, on macOS this uses CFNetwork, and on Linux this uses the org.freedesktop.portal.ProxyResolver XDG desktop portal.  TODO(crbug.com/40111093): Only use the system resolver whenever Chrome is exclusively using system proxy configs.

## `--validate-crx`

- Constant: `kValidateCrx`

Examines a .crx for validity and prints the result.

## `--version`

- Constant: `kVersion`

Prints version information and quits.

## `--webrtc-event-log-proactive-pruning-delta`

- Constant: `kWebRtcRemoteEventLogProactivePruningDelta`

Sets the delay (in seconds) between proactive prunings of remote-bound WebRTC event logs which are pending upload. All positive values are legal. All negative values are illegal, and ignored. If set to 0, the meaning is "no proactive pruning".

## `--webrtc-event-log-upload-delay-ms`

- Constant: `kWebRtcRemoteEventLogUploadDelayMs`

WebRTC event logs will only be uploaded if the conditions hold for this many milliseconds.

## `--webrtc-event-log-upload-no-suppression`

- Constant: `kWebRtcRemoteEventLogUploadNoSuppression`

Normally, remote-bound WebRTC event logs are uploaded only when no peer connections are active. With this flag, the upload is never suppressed.

## `--webrtc-ip-handling-policy`

- Constant: `kWebRtcIPHandlingPolicy`

Override WebRTC IP handling policy to mimic the behavior when WebRTC IP handling policy is specified in Preferences.

## `--whats-new-use-staging`

- Constant: `kWhatsNewUseStaging`

Force What's New on Desktop to request from the staging environment.

## `--window-name`

- Constant: `kWindowName`

Specify the initial window user title: --window-name="My custom title"

## `--window-position`

- Constant: `kWindowPosition`

Specify the initial window position: --window-position=x,y

## `--window-size`

- Constant: `kWindowSize`

Specify the initial window size: --window-size=w,h

## `--window-workspace`

- Constant: `kWindowWorkspace`

Specify the initial window workspace: --window-workspace=id

## `--winhttp-proxy-resolver`

- Constant: `kWinHttpProxyResolver`

Uses WinHTTP to fetch and evaluate PAC scripts. Otherwise the default is to use Chromium's network stack to fetch, and V8 to evaluate.

## `--win-jumplist-action`

- Constant: `kWinJumplistAction`

Specifies which category option was clicked in the Windows Jumplist that resulted in a browser startup.

## `--android-entra-sso-allow-debug-brokers`

- Constant: `kAndroidEntraSsoAllowDebugBrokers`
- Condition: `BUILDFLAG(IS_ANDROID)`

If enabled Entra SSO will accept authentication headers from a specific list of non-production Microsoft Authentication broker apps.

## `--auth-spnego-account-type`

- Constant: `kAuthAndroidNegotiateAccountType`
- Condition: `BUILDFLAG(IS_ANDROID)`

Android authentication account type for SPNEGO authentication

## `--disable-default-browser-promo`

- Constant: `kDisableDefaultBrowserPromo`
- Condition: `BUILDFLAG(IS_ANDROID)`

Disable the default browser promo.

## `--force-enable-night-mode`

- Constant: `kForceEnableNightMode`
- Condition: `BUILDFLAG(IS_ANDROID)`

Forces the night mode to be enabled.

## `--force-show-update-menu-badge`

- Constant: `kForceShowUpdateMenuBadge`
- Condition: `BUILDFLAG(IS_ANDROID)`

Forces the update menu badge to show.

## `--custom_summary`

- Constant: `kForceShowUpdateMenuItemCustomSummary`
- Condition: `BUILDFLAG(IS_ANDROID)`

Forces a custom summary to be displayed below the update menu item.

## `--force-update-menu-type`

- Constant: `kForceUpdateMenuType`
- Condition: `BUILDFLAG(IS_ANDROID)`

Forces the update menu type to a specific type.

## `--market-url-for-testing`

- Constant: `kMarketUrlForTesting`
- Condition: `BUILDFLAG(IS_ANDROID)`

Sets the market URL for Chrome for use in testing.

## `--request-desktop-sites`

- Constant: `kRequestDesktopSites`
- Condition: `BUILDFLAG(IS_ANDROID)`

Force enable user agent overrides to request desktop sites in Clank.

## `--cast-mirroring-target-playout-delay`

- Constant: `kCastMirroringTargetPlayoutDelay`
- Condition: `!BUILDFLAG(IS_ANDROID) || BUILDFLAG(ENABLE_DESKTOP_ANDROID_EXTENSIONS)`

If enabled, overrides the target playout delay for a casting mirroring session. The value will be parsed as milliseconds. Lowering this value will result in a lower end to end latency, but could come at the cost of other quality standards such as dropped frames or FPS.

## `--save-page-as-mhtml`

- Constant: `kSavePageAsMHTML`
- Condition: `!BUILDFLAG(IS_CHROMEOS)`

Enables saving webpages as MHTML (Webpage, Single) by default, instead of saving as HTML with a directory of sub-resources. (Webpage, Complete). See http://crbug.com/40179885 for how to remove this switch.

## `--help`

- Constant: `kHelp`
- Condition: `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`

These flags show the man page on Linux. They are equivalent to each other.

## `--h`

- Constant: `kHelpShort`
- Condition: `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`

_No description in the source._

## `--class`

- Constant: `kWmClass`
- Condition: `BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS)`

The same as the --class argument in X applications.  Overrides the WM_CLASS window property with the given value.

## `--apps-keep-chrome-alive-in-tests`

- Constant: `kAppsKeepChromeAliveInTests`
- Condition: `BUILDFLAG(IS_MAC)`

Prevents Chrome from quitting when Chrome Apps are open.

## `--enable-user-metrics`

- Constant: `kEnableUserMetrics`
- Condition: `BUILDFLAG(IS_MAC)`

Enable user metrics from within the installer.

## `--metrics-client-id`

- Constant: `kMetricsClientID`
- Condition: `BUILDFLAG(IS_MAC)`

This is how the metrics client ID is passed from the browser process to its children. With Crashpad, the metrics client ID is distinct from the crash client ID.

## `--relauncher`

- Constant: `kRelauncherProcess`
- Condition: `BUILDFLAG(IS_MAC)`

A process type (switches::kProcessType) that relaunches the browser. See chrome/browser/mac/relauncher.h.

## `--dmg-device`

- Constant: `kRelauncherProcessDMGDevice`
- Condition: `BUILDFLAG(IS_MAC)`

When switches::kProcessType is switches::kRelauncherProcess, if this switch is also present, the relauncher process will unmount and eject a mounted disk image and move its disk image file to the trash.  The argument's value must be a BSD device name of the form "diskN" or "diskNsM".

## `--make-chrome-default`

- Constant: `kMakeChromeDefault`
- Condition: `BUILDFLAG(IS_MAC)`

Indicates whether Chrome should be set as the default browser during installation.

## `--code-sign-clone-cleanup`

- Constant: `kCodeSignCloneCleanupProcess`
- Condition: `BUILDFLAG(IS_MAC)`

A process type (switches::kProcessType) that cleans up the browser's temporary code sign clone.

## `--unique-temp-dir-suffix`

- Constant: `kUniqueTempDirSuffix`
- Condition: `BUILDFLAG(IS_MAC)`

When switches::kProcessType is switches::kCodeSignCloneCleanupProcess this switch is required. The value must be the unique suffix portion of the temporary directory that contains the clone. The full path will be reconstructed by the cleanup process.

## `--no-op-for-testing`

- Constant: `kNoOpForTestingProcess`
- Condition: `BUILDFLAG(IS_MAC)`

A process type that exits cleanly with code 0 without performing work.

## `--child-module-version`

- Constant: `kChildModuleVersion`
- Condition: `BUILDFLAG(IS_WIN)`

The version for the staged child module.

## `--child-module-user-path-component`

- Constant: `kChildModuleUserPathComponent`
- Condition: `BUILDFLAG(IS_WIN)`

The user path component identifying the directory in which the staged child module resides (see child_module::GetModulesDirForUser()). The browser computes this on behalf of renderers, which cannot.

## `--enable-profile-shortcut-manager`

- Constant: `kEnableProfileShortcutManager`
- Condition: `BUILDFLAG(IS_WIN)`

Force-enables the profile shortcut manager. This is needed for tests since they use a custom-user-data-dir which disables this.

## `--from-browser-switcher`

- Constant: `kFromBrowserSwitcher`
- Condition: `BUILDFLAG(IS_WIN)`

Indicates that this launch of the browser originated from the Legacy Browser Support for Edge extension's native host. This is recorded in UMA.

## `--from-installer`

- Constant: `kFromInstaller`
- Condition: `BUILDFLAG(IS_WIN)`

Indicates that this launch of the browser originated from the installer (i.e., following a successful new install or over-install). This triggers browser behaviors for this specific launch, such as a welcome announcement for accessibility software (see https://crbug.com/40685905).

## `--hide-icons`

- Constant: `kHideIcons`
- Condition: `BUILDFLAG(IS_WIN)`

Makes Windows happy by allowing it to show "Enable access to this program" checkbox in Add/Remove Programs->Set Program Access and Defaults. This only shows an error box because the only way to hide Chrome is by uninstalling it.

## `--no-network-profile-warning`

- Constant: `kNoNetworkProfileWarning`
- Condition: `BUILDFLAG(IS_WIN)`

Whether or not the browser should warn if the profile is on a network share. This flag is only relevant for Windows currently.

## `--no-pre-read-main-dll`

- Constant: `kNoPreReadMainDll`
- Condition: `BUILDFLAG(IS_WIN)`

Whether this process should PrefetchVirtualMemory on the contents of Chrome.dll. This warms up the pages in memory to speed up startup but might not be required in later renderers and/or GPU. For experiment info see crbug.com/40234091.

## `--notification-inline-reply`

- Constant: `kNotificationInlineReply`
- Condition: `BUILDFLAG(IS_WIN)`

Used in combination with kNotificationLaunchId to specify the inline reply entered in the toast in the Windows Action Center.

## `--notification-launch-id`

- Constant: `kNotificationLaunchId`
- Condition: `BUILDFLAG(IS_WIN)`

Used for launching Chrome when a toast displayed in the Windows Action Center has been activated. Should contain the launch ID encoded by Chrome.

## `--pwa-launcher-version`

- Constant: `kPwaLauncherVersion`
- Condition: `BUILDFLAG(IS_WIN)`

Specifies the version of the Progressive-Web-App launcher that launched Chrome, used to determine whether to update all launchers. NOTE: changing this switch requires adding legacy handling for the previous method, as older PWA launchers still using this switch will rely on Chrome to update them to use the new method.

## `--show-icons`

- Constant: `kShowIcons`
- Condition: `BUILDFLAG(IS_WIN)`

See kHideIcons.

## `--source-app-id`

- Constant: `kSourceAppId`
- Condition: `BUILDFLAG(IS_WIN)`

When rendezvousing with an existing process, used to indicate that the StartupInfoW of the new Chrome process had dwFlags == STARTF_TITLEISAPPID. This is used to record launch metrics.

## `--source-shortcut`

- Constant: `kSourceShortcut`
- Condition: `BUILDFLAG(IS_WIN)`

When rendezvousing with an existing process, used to pass the path of the shortcut that launched the new Chrome process. This is used to record launch metrics.

## `--source-shortcut-location`

- Constant: `kSourceShortcutLocation`
- Condition: `BUILDFLAG(IS_WIN)`

Specifies the origin location of the shortcut that launched Chrome (e.g. desktop, start-menu, taskbar). Used to record launch metrics when launched with an AppId.

## `--desktop`

- Constant: `kSourceShortcutLocationDesktop`
- Condition: `BUILDFLAG(IS_WIN)`

_No description in the source._

## `--start-menu`

- Constant: `kSourceShortcutLocationStartMenu`
- Condition: `BUILDFLAG(IS_WIN)`

_No description in the source._

## `--taskbar`

- Constant: `kSourceShortcutLocationTaskbar`
- Condition: `BUILDFLAG(IS_WIN)`

_No description in the source._

## `--startup-foreground-launch`

- Constant: `kStartupForegroundLaunch`
- Condition: `BUILDFLAG(IS_WIN)`

Identifies Chrome instances that start in foreground mode at startup to record related metrics.

## `--uninstall`

- Constant: `kUninstall`
- Condition: `BUILDFLAG(IS_WIN)`

Runs un-installation steps that were done by chrome first-run.

## `--uninstall-app-id`

- Constant: `kUninstallAppId`
- Condition: `BUILDFLAG(IS_WIN)`

Specifies that the WebApp with the specified id should be uninstalled.

## `--isolated`

- Constant: `kIsolated`
- Condition: `BUILDFLAG(IS_WIN)`

Specifies that the browser is running isolated and should not attempt to start a second isolated browser.

## `--wait-for-parent-handle`

- Constant: `kWaitForParentHandle`
- Condition: `BUILDFLAG(IS_WIN)`

Passes the Win32 HANDLE value (as an integer) of the parent process to wait for during relaunch.

## `--debug-print`

- Constant: `kDebugPrint`
- Condition: `BUILDFLAG(ENABLE_PRINT_PREVIEW) && !defined(OFFICIAL_BUILD)`

Enables support to debug printing subsystem.

## `--guest`

- Constant: `kGuest`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_MAC) || \`

Causes the browser to launch directly in guest mode.

## `--glic-guest-url`

- Constant: `kGlicGuestURL`

Overrides the glic guest URL.

## `--geic-guest-url`

- Constant: `kGeicGuestURL`

Overrides the GEiC guest URL.

## `--geic-always-skip-fre`

- Constant: `kGeicAlwaysSkipFre`

Treats the GEiC FRE as completed without persisting anything. GEiC counterpart of `--glic-always-skip-fre`.

## `--geic-reset-fre`

- Constant: `kGeicResetFre`

Clears all GEiC FRE status at startup. `--geic-always-skip-fre` wins over it.

## `--skills-v2-origin`

- Constant: `kSkillsV2Origin`

_No description in the source._

## `--glic-always-open-fre`

- Constant: `kGlicAlwaysOpenFre`

_No description in the source._

## `--glic-always-skip-fre`

- Constant: `kGlicAlwaysSkipFre`

_No description in the source._

## `--glic-experimental-fre-url`

- Constant: `kGlicExperimentalFreURL`

_No description in the source._

## `--glic-shortcuts-learn-more-url`

- Constant: `kGlicShortcutsLearnMoreURL`

_No description in the source._

## `--glic-open-on-startup`

- Constant: `kGlicOpenOnStartup`

Use --glic-open-on-startup=attached or --glic-open-on-startup=detached.

## `--glic-webui-allowed-origins`

- Constant: `kGlicAllowedOrigins`

List of allowed origins in the glic webview, as a space-separated list.

## `--glic-automation`

- Constant: `kGlicAutomation`

Automation is intended to be passed in addition to glic-dev. It further disables functionality to make basic testing easier.

## `--glic-dev`

- Constant: `kGlicDev`

Dev mode for glic only exposed via command line flag.

## `--glic-skip-reload-after-navigation`

- Constant: `kGlicSkipReloadAfterNavigation`

If this flag is set, then the page navigating will not trigger a reload.

## `--glic-host-logging`

- Constant: `kGlicHostLogging`

Whether additional logging is enabled in the glic api host.

## `--glic-admin-redirect-patterns`

- Constant: `kGlicAdminRedirectPatterns`

List of URL patterns in the glic webview to redirect to an admin blocked panel, as a space-separated list.

## `--glic-always-show-web-actuation-toggle`

- Constant: `kGlicAlwaysShowWebActuationToggle`

Whether to show web actuation toggle in the Chrome AI settings page.

## `--glic-guest-url-preset-autopush`

- Constant: `kGlicGuestUrlPresetAutopush`

Configure preset guest URLs for manual testing. These are saved to local state prefs and can be selected to override the default glic guest URL through corresponding entries in chrome://flags.

## `--glic-guest-url-preset-staging`

- Constant: `kGlicGuestUrlPresetStaging`

_No description in the source._

## `--glic-guest-url-preset-preprod`

- Constant: `kGlicGuestUrlPresetPreprod`

_No description in the source._

## `--glic-guest-url-preset-prod`

- Constant: `kGlicGuestUrlPresetProd`

_No description in the source._

## `--list-apps`

- Constant: `kListApps`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN)`

Writes open and installed web apps for each profile to the specified file without launching a new browser window or tab. Pass a absolute file path to specify where to output the information. Can be used together with optional --profile-base-name switch to only write information for a given profile.

## `--profile-base-name`

- Constant: `kProfileBaseName`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN)`

Pass the basename of the profile directory to specify which profile to get information. Only relevant when used with --list-apps switch.

## `--profile-management-attributes`

- Constant: `kProfileManagementAttributes`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN)`

Domains and associated SAML attributes for which third-party profile management should be enabled. Input should be in JSON format.

## `--webapk-server-url`

- Constant: `kWebApkServerUrl`
- Condition: `BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_ANDROID)`

Custom WebAPK server URL for the sake of testing.

## `--use-system-default-printer`

- Constant: `kUseSystemDefaultPrinter`
- Condition: `!BUILDFLAG(IS_CHROMEOS) && !BUILDFLAG(IS_ANDROID)`

Uses the system default printer as the initially selected destination in print preview, instead of the most recently used destination.

## `--user-data-migrated`

- Constant: `kUserDataMigrated`
- Condition: `BUILDFLAG(ENABLE_DOWNGRADE_PROCESSING)`

Indicates that this process is the product of a relaunch following migration of User Data.

## `--enterprise-signin-dialog-behavior-for-testing`

- Constant: `kEnterpriseSigninDialogBehaviorForTesting`
- Condition: `BUILDFLAG(CHROME_FOR_TESTING)`

Overrides the behavior of the sign-in dialog when creating a new profile for an enterprise account. Valid values are "accept-new-profile", "accept-current-profile", and "cancel".
