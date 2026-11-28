# Chrome DevTools Protocol changelog — 2024-06

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-06, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1319565 — _2024-06-26T04:28:01.000Z_
######  Diff: [`549a18a...98a6075`](https://github.com/ChromeDevTools/devtools-protocol/compare/549a18a...98a6075)

```diff
@@ browser_protocol.pdl:12426 @@ experimental domain PWA
       # manifestId.
       optional string installUrlOrBundleUrl
 
-  # Uninstals the given manifest_id and closes any opened app windows.
+  # Uninstalls the given manifest_id and closes any opened app windows.
   command uninstall
     parameters
       string manifestId
@@ -12448,7 +12448,7 @@ experimental domain PWA
   # used to attach to via Target.attachToTarget or similar APIs.
   # If some files in the parameters cannot be handled by the web app, they will
   # be ignored. If none of the files can be handled, this API returns an error.
-  # If no files provided as the parameter, this API also returns an error.
+  # If no files are provided as the parameter, this API also returns an error.
   #
   # According to the definition of the file handlers in the manifest file, one
   # Target.TargetID may represent a page handling one or more files. The order
@@ -12465,7 +12465,39 @@ experimental domain PWA
 
   # Opens the current page in its web app identified by the manifest id, needs
   # to be called on a page target. This function returns immediately without
-  # waiting for the app finishing loading.
+  # waiting for the app to finish loading.
   command openCurrentPageInApp
     parameters
       string manifestId
+
+  # If user prefers opening the app in browser or an app window.
+  type DisplayMode extends string
+    enum
+      standalone
+      browser
+
+  # Changes user settings of the web app identified by its manifestId. If the
+  # app was not installed, this command returns an error. Unset parameters will
+  # be ignored; unrecognized values will cause an error.
+  #
+  # Unlike the ones defined in the manifest files of the web apps, these
+  # settings are provided by the browser and controlled by the users, they
+  # impact the way the browser handling the web apps.
+  #
+  # See the comment of each parameter.
+  command changeAppUserSettings
+    parameters
+      string manifestId
+      # If user allows the links clicked on by the user in the app's scope, or
+      # extended scope if the manifest has scope extensions and the flags
+      # `DesktopPWAsLinkCapturingWithScopeExtensions` and
+      # `WebAppEnableScopeExtensions` are enabled.
+      #
+      # Note, the API does not support resetting the linkCapturing to the
+      # initial value, uninstalling and installing the web app again will reset
+      # it.
+      #
+      # TODO(crbug.com/339453269): Setting this value on ChromeOS is not
+      # supported yet.
+      optional boolean linkCapturing
+      optional DisplayMode displayMode
```

## Roll protocol to r1317765 — _2024-06-21T04:27:31.000Z_
######  Diff: [`6859c96...549a18a`](https://github.com/ChromeDevTools/devtools-protocol/compare/6859c96...549a18a)

```diff
@@ browser_protocol.pdl:892 @@ experimental domain Audits
       ClientMetadataNoResponse
       ClientMetadataInvalidResponse
       ClientMetadataInvalidContentType
+      IdpNotPotentiallyTrustworthy
       DisabledInSettings
+      DisabledInFlags
       ErrorFetchingSignin
       InvalidSigninResponse
       AccountsHttpNotFound
@@ -915,6 +917,7 @@ experimental domain Audits
       NotSignedInWithIdp
       MissingTransientUserActivation
       ReplacedByButtonMode
+      InvalidFieldsSpecified
       RelyingPartyOriginIsOpaque
       TypeNotMatching
 
@@ -7121,6 +7124,9 @@ domain Network
       # The number of obtained Trust Tokens on a successful "Issuance" operation.
       optional integer issuedTokenCount
 
+  # Fired once security policy has been updated.
+  experimental event policyUpdated
+
   # Fired once when parsing the .wbn file has succeeded.
   # The event contains the information about the web bundle contents.
   experimental event subresourceWebBundleMetadataReceived
```

## Roll protocol to r1317198 — _2024-06-20T04:26:46.000Z_
######  Diff: [`210a6c6...6859c96`](https://github.com/ChromeDevTools/devtools-protocol/compare/210a6c6...6859c96)

```diff
@@ browser_protocol.pdl:1367 @@ domain Browser
       optional boolean userVisibleOnly
       # For "clipboard" permission, may specify allowWithoutSanitization.
       optional boolean allowWithoutSanitization
+      # For "fullscreen" permission, must specify allowWithoutGesture:true.
+      optional boolean allowWithoutGesture
       # For "camera" permission, may specify panTiltZoom.
       optional boolean panTiltZoom
 
@@ -7119,9 +7121,6 @@ domain Network
       # The number of obtained Trust Tokens on a successful "Issuance" operation.
       optional integer issuedTokenCount
 
-  # Fired once security policy has been updated.
-  experimental event policyUpdated
-
   # Fired once when parsing the .wbn file has succeeded.
   # The event contains the information about the web bundle contents.
   experimental event subresourceWebBundleMetadataReceived
```

## Roll protocol to r1316850 — _2024-06-19T04:27:32.000Z_
######  Diff: [`1e50e23...210a6c6`](https://github.com/ChromeDevTools/devtools-protocol/compare/1e50e23...210a6c6)

```diff
@@ browser_protocol.pdl:7119 @@ domain Network
       # The number of obtained Trust Tokens on a successful "Issuance" operation.
       optional integer issuedTokenCount
 
+  # Fired once security policy has been updated.
+  experimental event policyUpdated
+
   # Fired once when parsing the .wbn file has succeeded.
   # The event contains the information about the web bundle contents.
   experimental event subresourceWebBundleMetadataReceived
```

## Roll protocol to r1315554 — _2024-06-15T04:28:24.000Z_
######  Diff: [`db710ff...1e50e23`](https://github.com/ChromeDevTools/devtools-protocol/compare/db710ff...1e50e23)

```diff
@@ browser_protocol.pdl:156 @@ experimental domain Accessibility
       flowto
       labelledby
       owns
+      url
 
   # A node in the accessibility tree.
   type AXNode extends object
@@ -10508,6 +10509,7 @@ experimental domain Storage
       reportingOriginsPerSiteLimitReached
       exceedsMaxChannelCapacity
       exceedsMaxTriggerStateCardinality
+      destinationPerDayReportingLimitReached
 
   experimental event attributionReportingSourceRegistered
     parameters
```

## Roll protocol to r1312386 — _2024-06-08T04:27:15.000Z_
######  Diff: [`1db3824...db710ff`](https://github.com/ChromeDevTools/devtools-protocol/compare/1db3824...db710ff)

```diff
@@ browser_protocol.pdl:915 @@ experimental domain Audits
       MissingTransientUserActivation
       ReplacedByButtonMode
       RelyingPartyOriginIsOpaque
+      TypeNotMatching
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
@@ -6075,7 +6076,7 @@ domain Network
       # An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
       # This is a temporary ability and it will be removed in the future.
       experimental integer sourcePort
-      # Cookie partition key. 
+      # Cookie partition key.
       experimental optional CookiePartitionKey partitionKey
       # True if cookie partition key is opaque.
       experimental optional boolean partitionKeyOpaque
@@ -6496,8 +6497,8 @@ domain Network
       optional string domain
       # If specified, deletes only cookies with the exact path.
       optional string path
-      # If specified, deletes only cookies with the the given name and partitionKey where 
-      # where all partition key attributes match the cookie partition key attribute.
+      # If specified, deletes only cookies with the the given name and partitionKey where
+      # all partition key attributes match the cookie partition key attribute.
       experimental optional CookiePartitionKey partitionKey
 
   # Disables network tracking, prevents network events from being sent to the client.
@@ -9248,6 +9249,11 @@ domain Page
       HTTPAuthRequired
       CookieFlushed
       BroadcastChannelOnMessage
+      WebViewSettingsChanged
+      WebViewJavaScriptObjectChanged
+      WebViewMessageListenerInjected
+      WebViewSafeBrowsingAllowlistChanged
+      WebViewDocumentStartJavascriptChanged
       #Blocklisted features
       WebSocket
       WebTransport
```

## Roll protocol to r1311068 — _2024-06-06T04:27:10.000Z_
######  Diff: [`689e8cb...1db3824`](https://github.com/ChromeDevTools/devtools-protocol/compare/689e8cb...1db3824)

```diff
@@ browser_protocol.pdl:6032 @@ domain Network
       # Set if another request triggered this request (e.g. preflight).
       optional RequestId requestId
 
+  # cookiePartitionKey object
+  # The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.
+  experimental type CookiePartitionKey extends object
+    properties
+      # The site of the top-level URL the browser was visiting at the start
+      # of the request to the endpoint that set the cookie.
+      string topLevelSite
+      # Indicates if the cookie has any ancestors that are cross-site to the topLevelSite.
+      boolean hasCrossSiteAncestor
+
   # Cookie object
   type Cookie extends object
     properties
@@ -6065,9 +6075,8 @@ domain Network
       # An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
       # This is a temporary ability and it will be removed in the future.
       experimental integer sourcePort
-      # Cookie partition key. The site of the top-level URL the browser was visiting at the start
-      # of the request to the endpoint that set the cookie.
-      experimental optional string partitionKey
+      # Cookie partition key. 
+      experimental optional CookiePartitionKey partitionKey
       # True if cookie partition key is opaque.
       experimental optional boolean partitionKeyOpaque
 
@@ -6283,10 +6292,8 @@ domain Network
       # An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
       # This is a temporary ability and it will be removed in the future.
       experimental optional integer sourcePort
-      # Cookie partition key. The site of the top-level URL the browser was visiting at the start
-      # of the request to the endpoint that set the cookie.
-      # If not set, the cookie will be set as not partitioned.
-      experimental optional string partitionKey
+      # Cookie partition key. If not set, the cookie will be set as not partitioned.
+      experimental optional CookiePartitionKey partitionKey
 
   # Authorization challenge for HTTP status code 401 or 407.
   experimental type AuthChallenge extends object
@@ -6489,9 +6496,9 @@ domain Network
       optional string domain
       # If specified, deletes only cookies with the exact path.
       optional string path
-      # If specified, deletes only cookies with the the given name and partitionKey where domain
-      # matches provided URL.
-      experimental optional string partitionKey
+      # If specified, deletes only cookies with the the given name and partitionKey where 
+      # where all partition key attributes match the cookie partition key attribute.
+      experimental optional CookiePartitionKey partitionKey
 
   # Disables network tracking, prevents network events from being sent to the client.
   command disable
@@ -6668,10 +6675,8 @@ domain Network
       # An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
       # This is a temporary ability and it will be removed in the future.
       experimental optional integer sourcePort
-      # Cookie partition key. The site of the top-level URL the browser was visiting at the start
-      # of the request to the endpoint that set the cookie.
-      # If not set, the cookie will be set as not partitioned.
-      experimental optional string partitionKey
+      # Cookie partition key. If not set, the cookie will be set as not partitioned.
+      experimental optional CookiePartitionKey partitionKey
     returns
       # Always set to true. If an error occurs, the response indicates protocol error.
       deprecated boolean success
@@ -7063,7 +7068,7 @@ domain Network
       optional string headersText
       # The cookie partition key that will be used to store partitioned cookies set in this response.
       # Only sent when partitioned cookies are enabled.
-      optional string cookiePartitionKey
+      experimental optional CookiePartitionKey cookiePartitionKey
       # True if partitioned cookies are enabled, but the partition key is not serializable to string.
       optional boolean cookiePartitionKeyOpaque
       # A list of cookies which should have been blocked by 3PCD but are exempted and stored from
@@ -7910,6 +7915,7 @@ domain Page
       clipboard-write
       compute-pressure
       cross-origin-isolated
+      deferred-fetch
       direct-sockets
       display-capture
       document-domain
```

## Roll protocol to r1310407 — _2024-06-05T04:28:24.000Z_
######  Diff: [`2064bda...689e8cb`](https://github.com/ChromeDevTools/devtools-protocol/compare/2064bda...689e8cb)

```diff
@@ browser_protocol.pdl:622 @@ experimental domain Audits
       CoopSandboxedIFrameCannotNavigateToCoopPage
       CorpNotSameOrigin
       CorpNotSameOriginAfterDefaultedToSameOriginByCoep
+      CorpNotSameOriginAfterDefaultedToSameOriginByDip
+      CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip
       CorpNotSameSite
 
   # Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
@@ -5755,6 +5757,8 @@ domain Network
       coop-sandboxed-iframe-cannot-navigate-to-coop-page
       corp-not-same-origin
       corp-not-same-origin-after-defaulted-to-same-origin-by-coep
+      corp-not-same-origin-after-defaulted-to-same-origin-by-dip
+      corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip
       corp-not-same-site
 
   # The reason why request was blocked.
```

## Roll protocol to r1309774 — _2024-06-04T04:27:00.000Z_
######  Diff: [`24f369f...2064bda`](https://github.com/ChromeDevTools/devtools-protocol/compare/24f369f...2064bda)

```diff
@@ browser_protocol.pdl:12406 @@ experimental domain PWA
       string manifestId
 
   # Launches the installed web app, or an url in the same web app instead of the
-  # default start url if it is provided. Returns a tab / web contents based
-  # Target.TargetID which can be used to attach to via Target.attachToTarget or
-  # similar APIs.
+  # default start url if it is provided. Returns a page Target.TargetID which
+  # can be used to attach to via Target.attachToTarget or similar APIs.
   command launch
     parameters
       string manifestId
@@ -12419,16 +12418,15 @@ experimental domain PWA
 
   # Opens one or more local files from an installed web app identified by its
   # manifestId. The web app needs to have file handlers registered to process
-  # the files. The API returns one or more tabs / web contents' based
-  # Target.TargetIDs which can be used to attach to via Target.attachToTarget or
-  # similar APIs.
+  # the files. The API returns one or more page Target.TargetIDs which can be
+  # used to attach to via Target.attachToTarget or similar APIs.
   # If some files in the parameters cannot be handled by the web app, they will
   # be ignored. If none of the files can be handled, this API returns an error.
   # If no files provided as the parameter, this API also returns an error.
   #
   # According to the definition of the file handlers in the manifest file, one
-  # Target.TargetID may represent a tab handling one or more files. The order of
-  # the returned Target.TargetIDs is also not guaranteed.
+  # Target.TargetID may represent a page handling one or more files. The order
+  # of the returned Target.TargetIDs is not guaranteed.
   #
   # TODO(crbug.com/339454034): Check the existences of the input files.
   command launchFilesInApp
@@ -12438,3 +12436,10 @@ experimental domain PWA
     returns
       # IDs of the tab targets created as the result.
       array of Target.TargetID targetIds
+
+  # Opens the current page in its web app identified by the manifest id, needs
+  # to be called on a page target. This function returns immediately without
+  # waiting for the app finishing loading.
+  command openCurrentPageInApp
+    parameters
+      string manifestId
```
