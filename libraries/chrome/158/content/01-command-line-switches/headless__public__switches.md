# Command-line switches: `headless/public/switches`

Generated from `headless/public/switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

29 switches.

## `--accept-lang`

- Constant: `kAcceptLang`

Specifies Accept-Language to send to servers and expose to JavaScript via the navigator.language DOM property. language[-country] where language is the 2 letter code from ISO-639.

## `--allow-video-codecs`

- Constant: `kAllowVideoCodecs`

A comma-separated, case-insenitive list of video codecs to allow. If specified, codecs not matching the list will not be used. '*' will match everything, '-' at the start of an entry means codec is disallowed. First entry that matches determines the outcome. Codec names are as returned by `GetCodecName()` in media/base/video_codecs.cc

## `--auth-server-allowlist`

- Constant: `kAuthServerAllowlist`

Allowlist for Negotiate Auth servers.

## `--block-new-web-contents`

- Constant: `kBlockNewWebContents`

If true, then all pop-ups and calls to window.open will fail.

## `--crash-dumps-dir`

- Constant: `kCrashDumpsDir`

The directory breakpad should store minidumps in.

## `--deterministic-mode`

- Constant: `kDeterministicMode`

A meta flag. This sets a number of flags which put the browser into deterministic mode where begin frames should be issued over DevToolsProtocol (experimental).

## `--disable-cookie-encryption`

- Constant: `kDisableCookieEncryption`

Whether cookies stored as part of user profile are encrypted.

## `--disable-crash-reporter`

- Constant: `kDisableCrashReporter`

Disable crash reporter for headless. It is enabled by default in official builds.

## `--disable-lazy-loading`

- Constant: `kDisableLazyLoading`

Disables lazy loading of images and frames.

## `--disk-cache-dir`

- Constant: `kDiskCacheDir`

Use a specific disk cache location, rather than one derived from the UserDatadir.

## `--enable-bfcache`

- Constant: `kEnableBackForwardCache`

Enable Back Forward Cache support

## `--enable-begin-frame-control`

- Constant: `kEnableBeginFrameControl`

Whether or not begin frames should be issued over DevToolsProtocol (experimental).

## `--enable-crash-reporter`

- Constant: `kEnableCrashReporter`

Enable crash reporter for headless.

## `--enable-gpu`

- Constant: `kEnableGPU`

Enable hardware GPU support. Headless uses swiftshader by default for consistency across headless environments. This flag just turns forcing of swiftshader off and lets us revert to regular driver selection logic. Alternatively, specific drivers may be forced with --use-gl or --use-angle. Nethier approach guarantees that hardware GPU support will be enabled, as this is still conditional on headless having access to X display etc.

## `--explicitly-allowed-ports`

- Constant: `kExplicitlyAllowedPorts`

Allows overriding the list of restricted ports by passing a comma-separated list of port numbers.

## `--font-render-hinting`

- Constant: `kFontRenderHinting`

Sets font render hinting when running headless, affects Skia rendering and whether glyph subpixel positioning is enabled. Possible values: none|slight|medium|full|max. Default: full.

## `--force-new-browsing-instance`

- Constant: `kForceNewBrowsingInstance`

Forces each navigation to use a new BrowsingInstance.

## `--force-reporting-destination-attested`

- Constant: `kForceReportingDestinationAttested`

Force reporting destination attested for headless shell.

## `--incognito`

- Constant: `kIncognito`

Forces Incognito mode even if user data directory is specified using the --user-data-dir switch.

## `--no-system-proxy-config-service`

- Constant: `kNoSystemProxyConfigService`

Do not use system proxy configuration service.

## `--password-store`

- Constant: `kPasswordStore`

Specifies which encryption storage backend to use. Possible values are kwallet, kwallet5, gnome-libsecret, basic. Any other value will lead to Chrome detecting the best backend automatically. TODO(crbug.com/40449930): Once PasswordStore no longer uses KWallet for storing passwords, rename this flag to stop referencing passwords. Do not rename it sooner, though; developers and testers might rely on it keeping large amounts of testing passwords out of their KWallets.

## `--proxy-bypass-list`

- Constant: `kProxyBypassList`

Specifies a list of hosts for whom we bypass proxy settings and use direct connections. Ignored unless --proxy-server is also specified. This is a comma-separated list of bypass rules. See: "net/proxy_resolution/proxy_host_matching_rules.h" for the format of these rules.

## `--proxy-pac-url`

- Constant: `kProxyPacUrl`

Uses the PAC script at the specified URL to pick proxies, overrides system settings. Takes precedence over --proxy-server.

## `--proxy-server`

- Constant: `kProxyServer`

Uses a specified proxy server, overrides system settings. This switch only affects HTTP and HTTPS requests.

## `--screen-info`

- Constant: `kScreenInfo`

Headless screen info in the format: {0,0 800x600}{800,0 600x800}. See //components/headless/screen_info/README.md for more details.

## `--user-agent`

- Constant: `kUserAgent`

A string used to override the default user agent with a custom one.

## `--user-data-dir`

- Constant: `kUserDataDir`

Directory where the browser stores the user profile. Note that if this switch is added, the session will no longer be Incognito, unless Incognito mode is forced with --incognito switch.

## `--version`

- Constant: `kVersion`

Prints version information and quits.

## `--window-size`

- Constant: `kWindowSize`

Sets the initial window size. Provided as string in the format "800,600". This also defines the headless screen size in lieu of --screen-info.
