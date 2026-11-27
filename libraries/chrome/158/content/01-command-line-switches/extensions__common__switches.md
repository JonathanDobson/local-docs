# Command-line switches: `extensions/common/switches`

Generated from `extensions/common/switches.h` and `extensions/common/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

39 switches.

## `--allow-http-background-page`

- Constant: `kAllowHTTPBackgroundPage`

Allows non-https URL for background_page for hosted apps.

## `--allow-legacy-extension-manifests`

- Constant: `kAllowLegacyExtensionManifests`

Allows the browser to load extensions that lack a modern manifest when that would otherwise be forbidden.

## `--allowlisted-extension-id`

- Constant: `kAllowlistedExtensionID`

Adds the given extension ID to all the permission allowlists.

## `--allow-webui-test-in-component-extensions`

- Constant: `kAllowWebUITestInComponentExtensions`

Test-only. Allows built-in (kComponent) extensions to load scripts from chrome://webui-test, which only exists in browser tests. This does not change any other browser behavior. ExtensionMochaBrowserTest appends it.  This switch is specific to extensions. WebUI pages do not need it: their CSP always allows chrome://webui-test, and that host is only registered in tests. Component extensions are gated anyway, as defense in depth, because they are the most privileged extensions. This is not a precedent for gating chrome://webui-test in WebUI.

## `--disable-app-content-verification`

- Constant: `kDisableAppContentVerification`

Whether to disable app content verification when testing changes locally on Chromebox for Meetings hardware.

## `--disable-crash-on-component-extension-js-error`

- Constant: `kDisableCrashOnComponentExtensionJsError`

Disables crashing on JavaScript errors in component extensions. Used for development.

## `--disable-extensions-file-access-check`

- Constant: `kDisableExtensionsFileAccessCheck`

Disable checking for user opt-in for extensions that want to inject script into file URLs (ie, always allow it). This is used during automated testing.

## `--disable-extensions`

- Constant: `kDisableExtensions`

Disables extensions.

## `--disable-extensions-except`

- Constant: `kDisableExtensionsExcept`

Disable extensions except those specified in a comma-separated list.

## `--disable-extensions-http-throttling`

- Constant: `kDisableExtensionsHttpThrottling`

Disable the net::URLRequestThrottlerManager functionality for requests originating from extensions.

## `--embedded-extension-options`

- Constant: `kEmbeddedExtensionOptions`

Enables extension options to be embedded in chrome://extensions rather than a new tab.

## `--enable-experimental-extension-apis`

- Constant: `kEnableExperimentalExtensionApis`

Enables extension APIs that are in development.

## `--enable-ble-advertising-in-apps`

- Constant: `kEnableBLEAdvertising`

Enable BLE Advertising in apps.

## `--extension-process`

- Constant: `kExtensionProcess`

Marks a renderer as extension process.

## `--extensions-on-chrome-urls`

- Constant: `kExtensionsOnChromeURLs`

Enables extensions running scripts on chrome:// URLs. Extensions still need to explicitly request access to chrome:// URLs in the manifest.

## `--extensions-on-extension-urls`

- Constant: `kExtensionsOnExtensionURLs`

Enables extensions running scripts on chrome-extension:// URLs. Extensions still need to explicitly request access to chrome-extension:// URLs in the manifest.

## `--load-apps`

- Constant: `kLoadApps`

Comma-separated list of paths to apps to load at startup. The first app in the list will be launched.

## `--load-extension`

- Constant: `kLoadExtension`

Comma-separated list of paths to extensions to load at startup.

## `--load-signin-profile-test-extension`

- Constant: `kLoadSigninProfileTestExtension`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Path to the unpacked test extension to load into the signin profile. The ID extension loaded must match kTestSigninProfileExtensionId.

## `--load-guest-mode-test-extension`

- Constant: `kLoadGuestModeTestExtension`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Path to the unpacked test extension to load into guest mode. The extension ID must match kGuestModeTestExtensionId.

## `--offscreen-document-testing`

- Constant: `kOffscreenDocumentTesting`

Allows the use of the `testing` reason in offscreen documents.

## `--refresh-component-extension-service-workers`

- Constant: `kRefreshComponentExtensionServiceWorkers`

Forces component extensions' service workers to be re-registered on every load, instead of reusing the registration persisted in the profile.

## `--set-extension-throttle-test-params`

- Constant: `kSetExtensionThrottleTestParams`

Set the parameters for ExtensionURLLoaderThrottleBrowserTest.

## `--show-component-extension-options`

- Constant: `kShowComponentExtensionOptions`

Makes component extensions appear in chrome://settings/extensions.

## `--enable-trace-app-source`

- Constant: `kTraceAppSource`

Pass launch source to platform apps.

## `--enable-crx-hash-check`

- Constant: `kEnableCrxHashCheck`

Enable package hash check: the .crx file sha256 hash sum should be equal to the one received from update manifest.

## `--allow-future-manifest-version`

- Constant: `kAllowFutureManifestVersion`

Mute extension errors while working with new manifest version.

## `--extension-test-api-on-web-pages`

- Constant: `kExtensionTestApiOnWebPages`

Allow the chrome.test API to be exposed on web page contexts for testing. TODO(tjudkins): This will need to be added to the list of flags that get copied from the browser to the renderer in ChromeContentBrowserClient to actually use it in browser tests.

## `--extension-test-api-standardized-behavior`

- Constant: `kExtensionTestApiStandardizedBehavior`

Forces the `chrome.test` API to use standardized behavior matching the `browser.test` proposal.

## `--extension-zero-state-iph-variant`

- Constant: `kZeroStatePromoIphVariantParamName`

The feature parameter name that controls the variant of IPH shown when the user has no extensions installed.

## `--custom-action-iph`

- Constant: `kZeroStatePromoCustomActionIph`

When the user has no extensions installed, display a custom action IPH that upon triggering, opens a new tab to the Chrome Web Store.

## `--custom-ui-chip-iph`

- Constant: `kZeroStatePromoCustomUiChipIphV1`

When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip button.

## `--custom-ui-chip-iph-v2`

- Constant: `kZeroStatePromoCustomUiChipIphV2`

When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip button. This variation has a different color scheme to highlight the chips.

## `--custom-ui-chip-iph-v3`

- Constant: `kZeroStatePromoCustomUiChipIphV3`

When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a cr-chip button. This variation has a different color scheme to highlight the chips. The ordering and selection of the chips are slightly different than variation 2.

## `--custom-ui-plain-link-iph`

- Constant: `kZeroStatePromoCustomUiPlainLinkIph`

When the user has no extensions installed, display a custom UI IPH that presents the user with different collections of extensions to explore, each in a plain text link.

## `--extensions-install-verification`

- Constant: `kExtensionsInstallVerification`

Turns on extension install verification if it would not otherwise have been turned on.

## `--extensions-not-webstore`

- Constant: `kExtensionsNotWebstore`

Specifies a comma-separated list of extension ids that should be forced to be treated as not from the webstore when doing install verification.

## `--apps-gallery-url`

- Constant: `kAppsGalleryURL`

Overrides the url that the browser treats as the webstore, granting it the webstore APIs and giving it some special protections.

## `--apps-gallery-download-url`

- Constant: `kAppsGalleryDownloadURL`

Overrides the URL that the webstore APIs download extensions from. Note: the URL must contain one '%s' for the extension ID.
