# Chrome DevTools Protocol changelog — 2025-02

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-02, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1425554 — _2025-02-27T04:29:43.000Z_
######  Diff: [`d45566d...044de40`](https://github.com/ChromeDevTools/devtools-protocol/compare/d45566d...044de40)

```diff
@@ browser_protocol.pdl:8235 @@ domain Page
       PerformanceProfile
 
   # All Permissions Policy features. This enum should match the one defined
-  # in third_party/blink/renderer/core/permissions_policy/permissions_policy_features.json5.
+  # in services/network/public/cpp/permissions_policy/permissions_policy_features.json5.
   experimental type PermissionsPolicyFeature extends string
     enum
       accelerometer
```

## Roll protocol to r1423531 — _2025-02-22T04:29:31.000Z_
######  Diff: [`43b22be...d45566d`](https://github.com/ChromeDevTools/devtools-protocol/compare/43b22be...d45566d)

```diff
@@ browser_protocol.pdl:8811 @@ domain Page
 
   # Enables page domain notifications.
   command enable
+    parameters
+      # If true, the `Page.fileChooserOpened` event will be emitted regardless of the state set by
+      # `Page.setInterceptFileChooserDialog` command (default: false).
+      experimental optional boolean enableFileChooserOpenedEvent
 
   # The manifest of a webapp, see
   # https://www.w3.org/TR/appmanifest/#dfn-manifest.
```

## Roll protocol to r1422344 — _2025-02-20T04:28:59.000Z_
######  Diff: [`90fcdd6...43b22be`](https://github.com/ChromeDevTools/devtools-protocol/compare/90fcdd6...43b22be)

```diff
@@ browser_protocol.pdl:9751 @@ domain Page
       EmbedderExtensionSentMessageToCachedFrame
       RequestedByWebViewClient
       PostMessageByWebViewClient
+      CacheControlNoStoreDeviceBoundSessionTerminated
 
   # Types of not restored reasons for back-forward cache.
   experimental type BackForwardCacheNotRestoredReasonType extends string
```

## Roll protocol to r1421213 — _2025-02-18T04:29:00.000Z_
######  Diff: [`75e6043...90fcdd6`](https://github.com/ChromeDevTools/devtools-protocol/compare/75e6043...90fcdd6)

```diff
@@ browser_protocol.pdl:801 @@ experimental domain Audits
       WriteErrorTooLongIdField
       WriteErrorUnsupportedType
 
+  type SRIMessageSignatureError extends string
+    enum
+      MissingSignatureHeader
+      MissingSignatureInputHeader
+      InvalidSignatureHeader
+      InvalidSignatureInputHeader
+      SignatureHeaderValueIsNotByteSequence
+      SignatureHeaderValueIsParameterized
+      SignatureHeaderValueIsIncorrectLength
+      SignatureInputHeaderMissingLabel
+      SignatureInputHeaderValueNotInnerList
+      SignatureInputHeaderValueMissingComponents
+      SignatureInputHeaderInvalidComponentType
+      SignatureInputHeaderInvalidComponentName
+      SignatureInputHeaderInvalidHeaderComponentParameter
+      SignatureInputHeaderInvalidDerivedComponentParameter
+      SignatureInputHeaderKeyIdLength
+      SignatureInputHeaderInvalidParameter
+      SignatureInputHeaderMissingRequiredParameters
+      ValidationFailedSignatureExpired
+      ValidationFailedInvalidLength
+      ValidationFailedSignatureMismatch
+
   # Details for issues around "Attribution Reporting API" usage.
   # Explainer: https://github.com/WICG/attribution-reporting-api
   type AttributionReportingIssueDetails extends object
@@ -832,6 +855,11 @@ experimental domain Audits
       SharedDictionaryError sharedDictionaryError
       AffectedRequest request
 
+  type SRIMessageSignatureIssueDetails extends object
+    properties
+      SRIMessageSignatureError error
+      AffectedRequest request
+
   type GenericIssueErrorType extends string
     enum
       FormLabelForNameError
@@ -1076,6 +1104,7 @@ experimental domain Audits
       PropertyRuleIssue
       SharedDictionaryIssue
       SelectElementAccessibilityIssue
+      SRIMessageSignatureIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -1105,6 +1134,7 @@ experimental domain Audits
       optional FederatedAuthUserInfoRequestIssueDetails federatedAuthUserInfoRequestIssueDetails
       optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
       optional SelectElementAccessibilityIssueDetails selectElementAccessibilityIssueDetails
+      optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
```

## Roll protocol to r1420292 — _2025-02-14T04:29:03.000Z_
######  Diff: [`487cc35...75e6043`](https://github.com/ChromeDevTools/devtools-protocol/compare/487cc35...75e6043)

```diff
@@ browser_protocol.pdl:691 @@ experimental domain Audits
       kInlineViolation
       kEvalViolation
       kURLViolation
+      kSRIViolation
       kTrustedTypesSinkViolation
       kTrustedTypesPolicyViolation
       kWasmEvalViolation
@@ -3388,6 +3389,8 @@ domain DOM
         # Get the popover target for a given element. In this case, this given
         # element can only be an HTMLFormControlElement (<input>, <button>).
         PopoverTarget
+        # Get the interest target for a given element.
+        InterestTarget
     returns
       # NodeId of the element matching the queried relation.
       NodeId nodeId
```

## Roll protocol to r1419694 — _2025-02-13T04:29:06.000Z_
######  Diff: [`781a465...487cc35`](https://github.com/ChromeDevTools/devtools-protocol/compare/781a465...487cc35)

```diff
@@ browser_protocol.pdl:12675 @@ experimental domain Preload
       OtherPrerenderedPageActivated
       V8OptimizerDisabled
       PrerenderFailedDuringPrefetch
+      BrowsingDataRemoved
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1419081 — _2025-02-12T04:29:01.000Z_
######  Diff: [`549f720...781a465`](https://github.com/ChromeDevTools/devtools-protocol/compare/549f720...781a465)

```diff
@@ browser_protocol.pdl:986 @@ experimental domain Audits
       string failureMessage
       optional Network.RequestId requestId
 
+  type PartitioningBlobURLInfo extends string
+    enum
+      BlockedCrossPartitionFetching
+      EnforceNoopenerForNavigation
+
+  type PartitioningBlobURLIssueDetails extends object
+    properties
+      # The BlobURL that failed to load.
+      string url
+      # Additional information about the Partitioning Blob URL issue.
+      PartitioningBlobURLInfo partitioningBlobURLInfo
+
   type SelectElementAccessibilityIssueReason extends string
     enum
       DisallowedSelectChild
@@ -1049,6 +1061,7 @@ experimental domain Audits
       CorsIssue
       AttributionReportingIssue
       QuirksModeIssue
+      PartitioningBlobURLIssue
       # Deprecated
       NavigatorUserAgentIssue
       GenericIssue
@@ -1078,6 +1091,7 @@ experimental domain Audits
       optional CorsIssueDetails corsIssueDetails
       optional AttributionReportingIssueDetails attributionReportingIssueDetails
       optional QuirksModeIssueDetails quirksModeIssueDetails
+      optional PartitioningBlobURLIssueDetails partitioningBlobURLIssueDetails
       deprecated optional NavigatorUserAgentIssueDetails navigatorUserAgentIssueDetails
       optional GenericIssueDetails genericIssueDetails
       optional DeprecationIssueDetails deprecationIssueDetails
```

## Roll protocol to r1418467 — _2025-02-11T04:28:54.000Z_
######  Diff: [`b2b5c2c...549f720`](https://github.com/ChromeDevTools/devtools-protocol/compare/b2b5c2c...549f720)

```diff
@@ browser_protocol.pdl:950 @@ experimental domain Audits
       RelyingPartyOriginIsOpaque
       TypeNotMatching
       UiDismissedNoEmbargo
+      CorsError
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
@@ -8362,6 +8363,14 @@ domain Page
       OriginTrialStatus status
       array of OriginTrialTokenWithStatus tokensWithStatus
 
+  # Additional information about the frame document's security origin.
+  experimental type SecurityOriginDetails extends object
+    properties
+      # Indicates whether the frame document's security origin is one
+      # of the local hostnames (e.g. "localhost") or IP addresses (IPv4
+      # 127.0.0.0/8 or IPv6 ::1).
+      boolean isLocalhost
+
   # Information about the Frame on the page.
   type Frame extends object
     properties
@@ -8384,6 +8393,8 @@ domain Page
       experimental string domainAndRegistry
       # Frame document's security origin.
       string securityOrigin
+      # Additional details about the frame document's security origin.
+      experimental optional SecurityOriginDetails securityOriginDetails
       # Frame document's mimeType as determined by the browser.
       string mimeType
       # If the frame failed to load, this contains the URL that could not be loaded. Note that unlike url above, this URL may contain a fragment.
@@ -11283,6 +11294,8 @@ domain Target
       TargetID targetId
       # Binding name, 'cdp' if not specified.
       optional string bindingName
+      # If true, inherits the current root session's permissions (default: false).
+      optional boolean inheritPermissions
 
   # Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
   # one.
```

## Roll protocol to r1415363 — _2025-02-04T04:28:31.000Z_
######  Diff: [`e55a19d...b2b5c2c`](https://github.com/ChromeDevTools/devtools-protocol/compare/e55a19d...b2b5c2c)

```diff
@@ browser_protocol.pdl:1171 @@ experimental domain Extensions
     returns
       # Extension id.
       string id
+  # Uninstalls an unpacked extension (others not supported) from the profile.
+  # Available if the client is connected using the --remote-debugging-pipe flag
+  # and the --enable-unsafe-extension-debugging.
+  command uninstall
+    parameters
+      # Extension id.
+      string id
   # Gets data from extension storage in the given `storageArea`. If `keys` is
   # specified, these are used to filter the result.
   command getStorageItems
```
