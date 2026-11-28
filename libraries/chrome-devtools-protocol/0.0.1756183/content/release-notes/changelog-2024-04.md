# Chrome DevTools Protocol changelog — 2024-04

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-04, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1294156 — _2024-04-30T04:26:41.000Z_
######  Diff: [`551dc5e...b80715b`](https://github.com/ChromeDevTools/devtools-protocol/compare/551dc5e...b80715b)

```diff
@@ browser_protocol.pdl:5864 @@ domain Network
 
   experimental type ServiceWorkerRouterInfo extends object
     properties
-      integer ruleIdMatched
-      ServiceWorkerRouterSource matchedSourceType
+      # ID of the rule matched. If there is a matched rule, this field will
+      # be set, otherwiser no value will be set.
+      optional integer ruleIdMatched
+      # The router source of the matched rule. If there is a matched rule, this
+      # field will be set, otherwise no value will be set.
+      optional ServiceWorkerRouterSource matchedSourceType
 
   # HTTP response data.
   type Response extends object
@@ -5904,7 +5908,10 @@ domain Network
       optional boolean fromPrefetchCache
       # Specifies that the request was served from the prefetch cache.
       optional boolean fromEarlyHints
-      # Information about how Service Worker Static Router was used.
+      # Information about how ServiceWorker Static Router API was used. If this
+      # field is set with `matchedSourceType` field, a matching rule is found.
+      # If this field is set without `matchedSource`, no matching rule is found.
+      # Otherwise, the API is not used.
       experimental optional ServiceWorkerRouterInfo serviceWorkerRouterInfo
       # Total number of bytes received for this request so far.
       number encodedDataLength
@@ -7918,9 +7925,7 @@ domain Page
       vertical-scroll
       web-printing
       web-share
-      # Alias for 'window-placement' (crbug.com/1328581).
       window-management
-      window-placement
       xr-spatial-tracking
 
   # Reason for a permissions policy feature to be disabled.
@@ -12343,3 +12348,24 @@ experimental domain PWA
       integer badgeCount
       array of FileHandler fileHandlers
 
+  # Installs the given manifest identity, optionally using the given install_url
+  # or IWA bundle location.
+  #
+  # TODO(crbug.com/337872319) Support IWA to meet the following specific
+  # requirement.
+  # IWA-specific install description: If the manifest_id is isolated-app://,
+  # install_url_or_bundle_url is required, and can be either an http(s) URL or
+  # file:// URL pointing to a signed web bundle (.swbn). The .swbn file’s
+  # signing key must correspond to manifest_id. If Chrome is not in IWA dev
+  # mode, the installation will fail, regardless of the state of the allowlist.
+  command install
+    parameters
+      string manifestId
+      # The location of the app or bundle overriding the one derived from the
+      # manifestId.
+      optional string installUrlOrBundleUrl
+
+  # Uninstals the given manifest_id and closes any opened app windows.
+  command uninstall
+    parameters
+      string manifestId
```

## Roll protocol to r1292262 — _2024-04-25T04:26:20.000Z_
######  Diff: [`a85be37...551dc5e`](https://github.com/ChromeDevTools/devtools-protocol/compare/a85be37...551dc5e)

```diff
@@ browser_protocol.pdl:3132 @@ domain DOM
       # NodeIds of top layer elements
       array of NodeId nodeIds
 
+  # Returns the NodeId of the matched element according to certain relations.
+  experimental command getElementByRelation
+    parameters
+      # Id of the node from which to query the relation.
+      NodeId nodeId
+      # Type of relation to get.
+      enum relation
+        # Get the popover target for a given element. In this case, this given
+        # element can only be an HTMLFormControlElement (<input>, <button>).
+        PopoverTarget
+    returns
+      # NodeId of the element matching the queried relation.
+      NodeId nodeId
+
   # Re-does the last undone action.
   experimental command redo
 
@@ -9267,6 +9281,7 @@ domain Page
       EmbedderExtensionMessaging
       EmbedderExtensionMessagingForOpenPort
       EmbedderExtensionSentMessageToCachedFrame
+      RequestedByWebViewClient
 
   # Types of not restored reasons for back-forward cache.
   experimental type BackForwardCacheNotRestoredReasonType extends string
```

## Roll protocol to r1291694 — _2024-04-24T04:26:06.000Z_
######  Diff: [`385db00...a85be37`](https://github.com/ChromeDevTools/devtools-protocol/compare/385db00...a85be37)

```diff
@@ browser_protocol.pdl:741 @@ experimental domain Audits
       NoRegisterOsSourceHeader
       NoRegisterOsTriggerHeader
 
+  type SharedDictionaryError extends string
+    enum
+      UseErrorCrossOriginNoCorsRequest
+      UseErrorDictionaryLoadFailure
+      UseErrorMatchingDictionaryNotUsed
+      UseErrorUnexpectedContentDictionaryHeader
+      WriteErrorCossOriginNoCorsRequest
+      WriteErrorDisallowedBySettings
+      WriteErrorExpiredResponse
+      WriteErrorFeatureDisabled
+      WriteErrorInsufficientResources
+      WriteErrorInvalidMatchField
+      WriteErrorInvalidStructuredHeader
+      WriteErrorNavigationRequest
+      WriteErrorNoMatchField
+      WriteErrorNonListMatchDestField
+      WriteErrorNonSecureContext
+      WriteErrorNonStringIdField
+      WriteErrorNonStringInMatchDestList
+      WriteErrorNonStringMatchField
+      WriteErrorNonTokenTypeField
+      WriteErrorRequestAborted
+      WriteErrorShuttingDown
+      WriteErrorTooLongIdField
+      WriteErrorUnsupportedType
+
   # Details for issues around "Attribution Reporting API" usage.
   # Explainer: https://github.com/WICG/attribution-reporting-api
   type AttributionReportingIssueDetails extends object
@@ -767,6 +793,11 @@ experimental domain Audits
       string url
       optional SourceCodeLocation location
 
+  type SharedDictionaryIssueDetails extends object
+    properties
+      SharedDictionaryError sharedDictionaryError
+      AffectedRequest request
+
   type GenericIssueErrorType extends string
     enum
       CrossOriginPortalPostMessageError
@@ -972,6 +1003,7 @@ experimental domain Audits
       StylesheetLoadingIssue
       FederatedAuthUserInfoRequestIssue
       PropertyRuleIssue
+      SharedDictionaryIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -998,6 +1030,7 @@ experimental domain Audits
       optional StylesheetLoadingIssueDetails stylesheetLoadingIssueDetails
       optional PropertyRuleIssueDetails propertyRuleIssueDetails
       optional FederatedAuthUserInfoRequestIssueDetails federatedAuthUserInfoRequestIssueDetails
+      optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
```

## Roll protocol to r1289136 — _2024-04-18T04:26:02.000Z_
######  Diff: [`e52e967...385db00`](https://github.com/ChromeDevTools/devtools-protocol/compare/e52e967...385db00)

```diff
@@ browser_protocol.pdl:1059 @@ experimental domain Audits
     parameters
       InspectorIssue issue
 
+# Defines commands and events for browser extensions. Available if the client
+# is connected using the --remote-debugging-pipe flag and
+# the --enable-unsafe-extension-debugging flag is set.
+experimental domain Extensions
+  # Installs an unpacked extension from the filesystem similar to
+  # --load-extension CLI flags. Returns extension ID once the extension
+  # has been installed.
+  command loadUnpacked
+    parameters
+      # Absolute file path.
+      string path
+    returns
+      # Extension id.
+      string id
+
 # Defines commands and events for Autofill.
 experimental domain Autofill
   type CreditCard extends object
@@ -8440,7 +8455,7 @@ domain Page
   #   This API always waits for the manifest to be loaded.
   #   If manifestId is provided, and it does not match the manifest of the
   #     current document, this API errors out.
-  #   If there isn’t a loaded page, this API errors out immediately.
+  #   If there is not a loaded page, this API errors out immediately.
   command getAppManifest
     parameters
       optional string manifestId
```

## Roll protocol to r1286932 — _2024-04-13T04:24:25.000Z_
######  Diff: [`78bb0d0...e52e967`](https://github.com/ChromeDevTools/devtools-protocol/compare/78bb0d0...e52e967)

```diff
@@ browser_protocol.pdl:876 @@ experimental domain Audits
       SilentMediationFailure
       ThirdPartyCookiesBlocked
       NotSignedInWithIdp
+      MissingTransientUserActivation
+      ReplacedByButtonMode
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
@@ -8325,15 +8327,132 @@ domain Page
   # Enables page domain notifications.
   command enable
 
+  # The manifest of a webapp, see
+  # https://www.w3.org/TR/appmanifest/#dfn-manifest.
+  # Some fields do not appear in the standard since the API is designed to
+  # expose more browser internal states.
+
+  experimental type FileFilter extends object
+    properties
+      optional string name
+      optional array of string accepts
+
+  experimental type FileHandler extends object
+    properties
+      string action
+      string name
+      optional array of ImageResource icons
+      # Mimic a map, name is the key, accepts is the value.
+      optional array of FileFilter accepts
+      # Won't repeat the enums, using string for easy comparison. Same as the
+      # other enums below.
+      string launchType
+
+  # The image definition used in both icon and screenshot.
+  experimental type ImageResource extends object
+    properties
+      # The src field in the definition, but changing to url in favor of
+      # consistency.
+      string url
+      optional string sizes
+      optional string type
+
+  experimental type LaunchHandler extends object
+    properties
+      string clientMode
+
+  experimental type ProtocolHandler extends object
+    properties
+      string protocol
+      string url
+
+  experimental type RelatedApplication extends object
+    properties
+      optional string id
+      string url
+
+  experimental type ScopeExtension extends object
+    properties
+      # Instead of using tuple, this field always returns the serialized string
+      # for easy understanding and comparison.
+      string origin
+      boolean hasOriginWildcard
+
+  experimental type Screenshot extends object
+    properties
+      ImageResource image
+      string formFactor
+      optional string label
+
+  experimental type ShareTarget extends object
+    properties
+      string action
+      string method
+      string enctype
+      # Embed the ShareTargetParams
+      optional string title
+      optional string text
+      optional string url
+      optional array of FileFilter files
+
+  experimental type Shortcut extends object
+    properties
+      string name
+      string url
+
+  experimental type WebAppManifest extends object
+    properties
+      optional string backgroundColor
+      # The extra description provided by the manifest.
+      optional string description
+      optional string dir
+      optional string display
+      # The overrided display mode controlled by the user.
+      optional array of string displayOverrides
+      # The handlers to open files.
+      optional array of FileHandler fileHandlers
+      optional array of ImageResource icons
+      optional string id
+      optional string lang
+      # TODO(crbug.com/1231886): This field is non-standard and part of a Chrome
+      # experiment. See:
+      # https://github.com/WICG/web-app-launch/blob/main/launch_handler.md
+      optional LaunchHandler launchHandler
+      optional string name
+      optional string orientation
+      optional boolean preferRelatedApplications
+      # The handlers to open protocols.
+      optional array of ProtocolHandler protocolHandlers
+      optional array of RelatedApplication relatedApplications
+      optional string scope
+      # Non-standard, see
+      # https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md
+      optional array of ScopeExtension scopeExtensions
+      # The screenshots used by chromium.
+      optional array of Screenshot screenshots
+      optional ShareTarget shareTarget
+      optional string shortName
+      optional array of Shortcut shortcuts
+      optional string startUrl
+      optional string themeColor
+
+  # Gets the processed manifest for this current document.
+  #   This API always waits for the manifest to be loaded.
+  #   If manifestId is provided, and it does not match the manifest of the
+  #     current document, this API errors out.
+  #   If there isn’t a loaded page, this API errors out immediately.
   command getAppManifest
+    parameters
+      optional string manifestId
     returns
       # Manifest location.
       string url
       array of AppManifestError errors
       # Manifest content.
       optional string data
-      # Parsed manifest properties
-      experimental optional AppManifestParsedProperties parsed
+      # Parsed manifest properties. Deprecated, use manifest instead.
+      experimental deprecated optional AppManifestParsedProperties parsed
+      experimental WebAppManifest manifest
 
   experimental command getInstallabilityErrors
     returns
@@ -12160,3 +12279,4 @@ experimental domain PWA
     returns
       integer badgeCount
       array of FileHandler fileHandlers
+
```

## Roll protocol to r1285609 — _2024-04-11T04:26:18.000Z_
######  Diff: [`adb454e...78bb0d0`](https://github.com/ChromeDevTools/devtools-protocol/compare/adb454e...78bb0d0)

```diff
@@ browser_protocol.pdl:475 @@ experimental domain Animation
       # Animation that was started.
       Animation animation
 
+  # Event for animation that has been updated.
+  event animationUpdated
+    parameters
+      # Animation that was updated.
+      Animation animation
+
 # Audits domain allows investigation of page violations and possible improvements.
 experimental domain Audits
   depends on Network
```

## Roll protocol to r1284279 — _2024-04-09T04:26:29.000Z_
######  Diff: [`85c9096...91c5005`](https://github.com/ChromeDevTools/devtools-protocol/compare/85c9096...91c5005)

```diff
@@ browser_protocol.pdl:2575 @@ domain DOM
       grammar-error
       highlight
       first-line-inherited
+      scroll-marker
+      scroll-markers
       scrollbar
       scrollbar-thumb
       scrollbar-button
```

## Roll protocol to r1282316 — _2024-04-04T04:27:08.000Z_
######  Diff: [`5f4d1e6...85c9096`](https://github.com/ChromeDevTools/devtools-protocol/compare/5f4d1e6...85c9096)

```diff
@@ browser_protocol.pdl:12123 @@ experimental domain FedCm
   # Resets the cooldown time, if any, to allow the next FedCM call to show
   # a dialog even if one was recently dismissed by the user.
   command resetCooldown
+
+# This domain allows interacting with the browser to control PWAs.
+experimental domain PWA
+
+  # The following types are the replica of
+  # https://crsrc.org/c/chrome/browser/web_applications/proto/web_app_os_integration_state.proto;drc=9910d3be894c8f142c977ba1023f30a656bc13fc;l=67
+  type FileHandlerAccept extends object
+    properties
+      # New name of the mimetype according to
+      # https://www.iana.org/assignments/media-types/media-types.xhtml
+      string mediaType
+      array of string fileExtensions
+
+  type FileHandler extends object
+    properties
+      string action
+      array of FileHandlerAccept accepts
+      string displayName
+
+  # Returns the following OS state for the given manifest id.
+  command getOsAppState
+    parameters
+      # The id from the webapp's manifest file, commonly it's the url of the
+      # site installing the webapp. See
+      # https://web.dev/learn/pwa/web-app-manifest.
+      string manifestId
+    returns
+      integer badgeCount
+      array of FileHandler fileHandlers
```

## Roll protocol to r1281655 — _2024-04-03T04:26:30.000Z_
######  Diff: [`a0b1761...5f4d1e6`](https://github.com/ChromeDevTools/devtools-protocol/compare/a0b1761...5f4d1e6)

```diff
@@ browser_protocol.pdl:6123 @@ domain Network
     properties
       # The reason the cookie was exempted.
       CookieExemptionReason exemptionReason
+      # The string representing this individual cookie as it would appear in the header.
+      string cookieLine
       # The cookie object representing the cookie.
       Cookie cookie
 
@@ -6957,6 +6959,16 @@ domain Network
       # the response with the corresponding reason.
       optional array of ExemptedSetCookieWithReason exemptedCookies
 
+  # Fired when 103 Early Hints headers is received in addition to the common response.
+  # Not every responseReceived event will have an responseReceivedEarlyHints fired.
+  # Only one responseReceivedEarlyHints may be fired for eached responseReceived event.
+  experimental event responseReceivedEarlyHints
+    parameters
+      # Request identifier. Used to match this information to another responseReceived event.
+      RequestId requestId
+      # Raw response headers as they were received over the wire.
+      Headers headers
+
   # Fired exactly once for each Trust Token operation. Depending on
   # the type of the operation and whether the operation succeeded or
   # failed, the event is fired before the corresponding request was sent
```
