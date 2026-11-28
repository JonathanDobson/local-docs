# Chrome DevTools Protocol changelog — 2026-02

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-02, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1591961 — _2026-02-28T04:43:52.000Z_
######  Diff: [`c217062...58bb362`](https://github.com/ChromeDevTools/devtools-protocol/compare/c217062...58bb362)

```diff
@@ domains/Network.pdl:166 @@ domain Network
       High
       VeryHigh
 
-  # The render blocking behavior of a resource request.
+  # The render-blocking behavior of a resource request.
   experimental type RenderBlockingBehavior extends string
     enum
       Blocking
@@ -1477,7 +1477,7 @@ domain Network
       optional Page.FrameId frameId
       # Whether the request is initiated by a user gesture. Defaults to false.
       optional boolean hasUserGesture
-      # The render blocking behavior of the request.
+      # The render-blocking behavior of the request.
       experimental optional RenderBlockingBehavior renderBlockingBehavior
 
   # Fired when resource loading priority is changed
```

## Roll protocol to r1591319 — _2026-02-27T04:56:42.000Z_
######  Diff: [`d5ffdaf...c217062`](https://github.com/ChromeDevTools/devtools-protocol/compare/d5ffdaf...c217062)

```diff
@@ domains/Emulation.pdl:617 @@ domain Emulation
   experimental command removeScreen
     parameters
       ScreenId screenId
+
+  # Set primary screen. Only supported in headless mode.
+  # Note that this changes the coordinate system origin to the top-left
+  # of the new primary screen, updating the bounds and work areas
+  # of all existing screens accordingly.
+  experimental command setPrimaryScreen
+    parameters
+      ScreenId screenId
```

## Roll protocol to r1590631 — _2026-02-26T05:00:08.000Z_
######  Diff: [`708011c...d5ffdaf`](https://github.com/ChromeDevTools/devtools-protocol/compare/708011c...d5ffdaf)

```diff
@@ domains/Audits.pdl:7 @@ @@ -7,6 +7,7 @@
 # Audits domain allows investigation of page violations and possible improvements.
 experimental domain Audits
   depends on Network
+  depends on Runtime
 
   # Information about a cookie that is affected by an inspector issue.
   type AffectedCookie extends object
@@ -696,6 +697,41 @@ experimental domain Audits
       # Used for messages about activation disabled reason
       optional string disableReason
 
+  # Metadata about the ad script that was on the stack that caused the current
+  # script in the `AdAncestry` to be considered ad related.
+  type AdScriptIdentifier extends object
+    properties
+      # The script's v8 identifier.
+      Runtime.ScriptId scriptId
+      # v8's debugging id for the v8::Context.
+      Runtime.UniqueDebuggerId debuggerId
+      # The script's url (or generated name based on id if inline script).
+      string name
+
+  # Providence about how an ad script was determined to be such. It is an ad
+  # because its url matched a filterlist rule, or because some other ad script
+  # was on the stack when this script was loaded.
+  type AdAncestry extends object
+    properties
+      # The ad-script in the stack when the offending script was loaded. This is
+      # recursive down to the root script that was tagged due to the filterlist
+      # rule.
+      array of AdScriptIdentifier adAncestryChain
+      # The filterlist rule that caused the root (last) script in
+      # `adAncestry` to be ad-tagged.
+      optional string rootScriptFilterlistRule
+
+  # The issue warns about blocked calls to privacy sensitive APIs via the
+  # Selective Permissions Intervention.
+  type SelectivePermissionsInterventionIssueDetails extends object
+    properties
+      # Which API was intervened on.
+      string apiName
+      # Why the ad script using the API is considered an ad.
+      AdAncestry adAncestry
+      # The stack trace at the time of the intervention.
+      optional Runtime.StackTrace stackTrace
+
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
   # information about the kind of issue.
@@ -731,6 +767,7 @@ experimental domain Audits
       UserReidentificationIssue
       PermissionElementIssue
       PerformanceIssue
+      SelectivePermissionsInterventionIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -766,6 +803,7 @@ experimental domain Audits
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
       optional PermissionElementIssueDetails permissionElementIssueDetails
       optional PerformanceIssueDetails performanceIssueDetails
+      optional SelectivePermissionsInterventionIssueDetails selectivePermissionsInterventionIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
diff --git a/pdl/domains/Emulation.pdl b/pdl/domains/Emulation.pdl
index 5491f4cf..8488dffc 100644
--- a/pdl/domains/Emulation.pdl
+++ b/pdl/domains/Emulation.pdl
@@ -297,6 +297,15 @@ domain Emulation
       # to continuous.
       # Deprecated, use Emulation.setDevicePostureOverride.
       experimental deprecated optional DevicePosture devicePosture
+      # Scrollbar type. Default: `default`.
+      experimental optional enum scrollbarType
+        # Emulates scrollbars that float over the content, typically appearing
+        # only when scrolling.
+        overlay
+        # Restores the platform's default scrollbar behavior, which might be
+        # classic (occupying space within the layout) or overlay, depending
+        # on the platform. Note: if `mobile` is `true`, the default scrollbar type is `overlay`.
+        default
 
   # Start reporting the given posture value to the Device Posture API.
   # This override can also be set in setDeviceMetricsOverride().
diff --git a/pdl/domains/Extensions.pdl b/pdl/domains/Extensions.pdl
index d50da280..8b3da102 100644
--- a/pdl/domains/Extensions.pdl
+++ b/pdl/domains/Extensions.pdl
@@ -38,6 +38,28 @@ experimental domain Extensions
     returns
       # Extension id.
       string id
+
+  # Detailed information about an extension.
+  type ExtensionInfo extends object
+    properties
+      # Extension id.
+      string id
+      # Extension name.
+      string name
+      # Extension version.
+      string version
+      # The path from which the extension was loaded.
+      string path
+      # Extension enabled status.
+      boolean enabled
+
+  # Gets a list of all unpacked extensions.
+  # Available if the client is connected using the --remote-debugging-pipe flag
+  # and the --enable-unsafe-extension-debugging flag is set.
+  command getExtensions
+    returns
+      array of ExtensionInfo extensions
+
   # Uninstalls an unpacked extension (others not supported) from the profile.
   # Available if the client is connected using the --remote-debugging-pipe flag
   # and the --enable-unsafe-extension-debugging.
```

## Roll protocol to r1589152 — _2026-02-24T05:03:10.000Z_
######  Diff: [`6b927c9...708011c`](https://github.com/ChromeDevTools/devtools-protocol/compare/6b927c9...708011c)

```diff
@@ domains/Emulation.pdl:525 @@ domain Emulation
   experimental type DisabledImageType extends string
     enum
       avif
+      jxl
       webp
 
   experimental command setDisabledImageTypes
```

## Roll protocol to r1588380 — _2026-02-22T04:58:30.000Z_
######  Diff: [`e3b75f4...6b927c9`](https://github.com/ChromeDevTools/devtools-protocol/compare/e3b75f4...6b927c9)

```diff
@@ domains/DOM.pdl:183 @@ domain DOM
       experimental optional boolean isScrollable
       experimental optional boolean affectedByStartingStyles
       experimental optional array of StyleSheetId adoptedStyleSheets
+      experimental optional boolean isAdRelated
 
   # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
   type DetachedElementInfo extends object
@@ -912,6 +913,14 @@ domain DOM
       # If the node is scrollable.
       boolean isScrollable
 
+  # Fired when a node's ad related state changes.
+  experimental event adRelatedStateUpdated
+    parameters
+      # The id of the node.
+      DOM.NodeId nodeId
+      # If the node is ad related.
+      boolean isAdRelated
+
   # Fired when a node's starting styles changes.
   experimental event affectedByStartingStylesFlagUpdated
     parameters
```

## Roll protocol to r1588251 — _2026-02-21T04:50:25.000Z_
######  Diff: [`d03fc9b...e3b75f4`](https://github.com/ChromeDevTools/devtools-protocol/compare/d03fc9b...e3b75f4)

```diff
@@ domains/Network.pdl:2184 @@ domain Network
       FailedToUnwrapKey
       SessionDeletedDuringRefresh
 
+  # Details about a failed device bound session network request.
+  experimental type DeviceBoundSessionFailedRequest extends object
+    properties
+      # The failed request URL.
+      string requestUrl
+      # The net error of the response if it was not OK.
+      optional string netError
+      # The response code if the net error was OK and the response code was not
+      # 200.
+      optional integer responseError
+      # The body of the response if the net error was OK, the response code was
+      # not 200, and the response body was not empty.
+      optional string responseErrorBody
+
   # Session event details specific to creation.
   experimental type CreationEventDetails extends object
     properties
@@ -2192,6 +2206,9 @@ domain Network
       # The session if there was a newly created session. This is populated for
       # all successful creation events.
       optional DeviceBoundSession newSession
+      # Details about a failed device bound session network request if there was
+      # one.
+      optional DeviceBoundSessionFailedRequest failedRequest
 
   # Session event details specific to refresh.
   experimental type RefreshEventDetails extends object
@@ -2212,6 +2229,9 @@ domain Network
       optional DeviceBoundSession newSession
       # See comments on `net::device_bound_sessions::RefreshEventResult::was_fully_proactive_refresh`.
       boolean wasFullyProactiveRefresh
+      # Details about a failed device bound session network request if there was
+      # one.
+      optional DeviceBoundSessionFailedRequest failedRequest
 
   # Session event details specific to termination.
   experimental type TerminationEventDetails extends object
```

## Roll protocol to r1587613 — _2026-02-20T04:57:52.000Z_
######  Diff: [`6c86810...d03fc9b`](https://github.com/ChromeDevTools/devtools-protocol/compare/6c86810...d03fc9b)

```diff
@@ domains/Network.pdl:1113 @@ domain Network
   command enable
     parameters
       # Buffer size in bytes to use when preserving network payloads (XHRs, etc).
+      # This is the maximum number of bytes that will be collected by this
+      # DevTools session.
       experimental optional integer maxTotalBufferSize
       # Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
       experimental optional integer maxResourceBufferSize
```

## Roll protocol to r1585077 — _2026-02-14T04:53:53.000Z_
######  Diff: [`b328fc2...6c86810`](https://github.com/ChromeDevTools/devtools-protocol/compare/b328fc2...6c86810)

```diff
@@ domains/Audits.pdl:105 @@ experimental domain Audits
       # The recommended solution to the issue.
       optional CookieIssueInsight insight
 
+  type PerformanceIssueType extends string
+    enum
+      DocumentCookie
+
+  # Details for a performance issue.
+  type PerformanceIssueDetails extends object
+    properties
+      PerformanceIssueType performanceIssueType
+      optional SourceCodeLocation sourceCodeLocation
+
   type MixedContentResolutionStatus extends string
     enum
       MixedContentBlocked
@@ -720,6 +730,7 @@ experimental domain Audits
       ConnectionAllowlistIssue
       UserReidentificationIssue
       PermissionElementIssue
+      PerformanceIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -754,6 +765,7 @@ experimental domain Audits
       optional ConnectionAllowlistIssueDetails connectionAllowlistIssueDetails
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
       optional PermissionElementIssueDetails permissionElementIssueDetails
+      optional PerformanceIssueDetails performanceIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
diff --git a/pdl/domains/Emulation.pdl b/pdl/domains/Emulation.pdl
index 13daa510..d4cff0d7 100644
--- a/pdl/domains/Emulation.pdl
+++ b/pdl/domains/Emulation.pdl
@@ -571,7 +571,8 @@ domain Emulation
       # of size 100lvh.
       integer difference
 
-  # Returns device's screen configuration.
+  # Returns device's screen configuration. In headful mode, the physical screens configuration is returned,
+  # whereas in headless mode, a virtual headless screen configuration is provided instead.
   experimental command getScreenInfos
     returns
       array of ScreenInfo screenInfos
```

## Roll protocol to r1583009 — _2026-02-11T05:03:45.000Z_
######  Diff: [`17024e1...b328fc2`](https://github.com/ChromeDevTools/devtools-protocol/compare/17024e1...b328fc2)

```diff
@@ domains/Audits.pdl:500 @@ experimental domain Audits
       ConfigNoResponse
       ConfigInvalidResponse
       ConfigInvalidContentType
-      ClientMetadataHttpNotFound
-      ClientMetadataNoResponse
-      ClientMetadataInvalidResponse
-      ClientMetadataInvalidContentType
       IdpNotPotentiallyTrustworthy
       DisabledInSettings
       DisabledInFlags
@@ -525,11 +521,9 @@ experimental domain Audits
       Canceled
       RpPageNotVisible
       SilentMediationFailure
-      ThirdPartyCookiesBlocked
       NotSignedInWithIdp
       MissingTransientUserActivation
       ReplacedByActiveMode
-      InvalidFieldsSpecified
       RelyingPartyOriginIsOpaque
       TypeNotMatching
       UiDismissedNoEmbargo
```

## Roll protocol to r1581282 — _2026-02-07T04:51:01.000Z_
######  Diff: [`e8ee850...17024e1`](https://github.com/ChromeDevTools/devtools-protocol/compare/e8ee850...17024e1)

```diff
@@ domains/Network.pdl:339 @@ domain Network
       HeaderDisallowedByPreflightResponse
       RedirectContainsCredentials
       # Request was a private network request initiated by a non-secure context.
-      InsecurePrivateNetwork
+      InsecureLocalNetwork
       # Request carried a target IP address space property that did not match
       # the target resource's address space.
-      InvalidPrivateNetworkAccess
+      InvalidLocalNetworkAccess
       NoCorsRedirectModeNotFollow
       # Request was a local network request and is denied by user permission.
       # https://wicg.github.io/local-network-access/
```

## Roll protocol to r1580600 — _2026-02-06T04:57:42.000Z_
######  Diff: [`92e7a2f...e8ee850`](https://github.com/ChromeDevTools/devtools-protocol/compare/92e7a2f...e8ee850)

```diff
@@ domains/Audits.pdl:353 @@ experimental domain Audits
       IncorrectDigestType
       IncorrectDigestLength
 
+  type ConnectionAllowlistError extends string
+    enum
+      InvalidHeader
+      MoreThanOneList
+      ItemNotInnerList
+      InvalidAllowlistItemType
+      ReportingEndpointNotToken
+      InvalidUrlPattern
+
   # Details for issues around "Attribution Reporting API" usage.
   # Explainer: https://github.com/WICG/attribution-reporting-api
   type AttributionReportingIssueDetails extends object
@@ -396,6 +405,11 @@ experimental domain Audits
       UnencodedDigestError error
       AffectedRequest request
 
+  type ConnectionAllowlistIssueDetails extends object
+    properties
+      ConnectionAllowlistError error
+      AffectedRequest request
+
   type GenericIssueErrorType extends string
     enum
       FormLabelForNameError
@@ -709,6 +723,7 @@ experimental domain Audits
       ElementAccessibilityIssue
       SRIMessageSignatureIssue
       UnencodedDigestIssue
+      ConnectionAllowlistIssue
       UserReidentificationIssue
       PermissionElementIssue
 
@@ -742,6 +757,7 @@ experimental domain Audits
       optional ElementAccessibilityIssueDetails elementAccessibilityIssueDetails
       optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
       optional UnencodedDigestIssueDetails unencodedDigestIssueDetails
+      optional ConnectionAllowlistIssueDetails connectionAllowlistIssueDetails
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
       optional PermissionElementIssueDetails permissionElementIssueDetails
 
diff --git a/pdl/domains/Overlay.pdl b/pdl/domains/Overlay.pdl
index 689e42d8..8ef51bbb 100644
--- a/pdl/domains/Overlay.pdl
+++ b/pdl/domains/Overlay.pdl
@@ -255,6 +255,13 @@ experimental domain Overlay
       captureAreaScreenshot
       none
 
+  type InspectedElementAnchorConfig extends object
+    properties
+      # Identifier of the node to highlight.
+      optional DOM.NodeId nodeId
+      # Identifier of the backend node to highlight.
+      optional DOM.BackendNodeId backendNodeId
+
   # Disables domain notifications.
   command disable
 
@@ -423,6 +430,11 @@ experimental domain Overlay
       # An array of node identifiers and descriptors for the highlight appearance.
       array of ContainerQueryHighlightConfig containerQueryHighlightConfigs
 
+  command setShowInspectedElementAnchor
+    parameters
+      # Node identifier for which to show an anchor for.
+      InspectedElementAnchorConfig inspectedElementAnchorConfig
+
   # Requests that backend shows paint rectangles
   command setShowPaintRects
     parameters
@@ -494,5 +506,17 @@ experimental domain Overlay
       # Viewport to capture, in device independent pixels (dip).
       Page.Viewport viewport
 
+  # Fired when user asks to show the Inspect panel.
+  event inspectPanelShowRequested
+    parameters
+      # Id of the node to show in the panel.
+      DOM.BackendNodeId backendNodeId
+
+  # Fired when user asks to restore the Inspected Element floating window.
+  event inspectedElementWindowRestored
+    parameters
+      # Id of the node to restore the floating window for.
+      DOM.BackendNodeId backendNodeId
+
   # Fired when user cancels the inspect mode.
   event inspectModeCanceled
```

## Roll protocol to r1579878 — _2026-02-05T04:58:47.000Z_
######  Diff: [`f8bae52...92e7a2f`](https://github.com/ChromeDevTools/devtools-protocol/compare/f8bae52...92e7a2f)

```diff
@@ domains/Page.pdl:1581 @@ domain Page
       SharedWorkerMessage
       SharedWorkerWithNoActiveClient
       WebLocks
+      WebLocksContention
       WebHID
       WebBluetooth
       WebShare
```

## Roll protocol to r1578551 — _2026-02-03T04:57:40.000Z_
######  Diff: [`cd6a169...f8bae52`](https://github.com/ChromeDevTools/devtools-protocol/compare/cd6a169...f8bae52)

```diff
@@ domains/Network.pdl:1769 @@ domain Network
       DirectUDPMessage message
       MonotonicTime timestamp
 
-  experimental type PrivateNetworkRequestPolicy extends string
+  experimental type LocalNetworkAccessRequestPolicy extends string
     enum
       Allow
       BlockFromInsecureToMorePrivate
@@ -1795,7 +1795,7 @@ domain Network
     properties
       boolean initiatorIsSecureContext
       IPAddressSpace initiatorIPAddressSpace
-      PrivateNetworkRequestPolicy privateNetworkRequestPolicy
+      LocalNetworkAccessRequestPolicy localNetworkAccessRequestPolicy
 
   # Fired when additional information about a requestWillBeSent event is available from the
   # network stack. Not every requestWillBeSent event will have an additional
```
