# Chrome DevTools Protocol changelog — 2025-08

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-08, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1508733 — _2025-08-30T04:30:36.000Z_
######  Diff: [`f87879c...ede3fcf`](https://github.com/ChromeDevTools/devtools-protocol/compare/f87879c...ede3fcf)

```diff
@@ domains/Browser.pdl:103 @@ domain Browser
       closeTabSearch
       openGlic
 
-  # Set permission settings for given origin.
+  # Set permission settings for given requesting and embedding origins.
   experimental command setPermission
     parameters
       # Descriptor of permission to override.
       PermissionDescriptor permission
       # Setting of the permission.
       PermissionSetting setting
-      # Origin the permission applies to, all origins if not specified.
+      # Requesting origin the permission applies to, all origins if not specified.
       optional string origin
+      # Embedding origin the permission applies to. It is ignored unless the requesting origin is
+      # present and valid. If the requesting origin is provided but the embedding origin isn't, the
+      # requesting origin is used as the embedding origin.
+      optional string embeddingOrigin
       # Context to override. When omitted, default browser context is used.
       optional BrowserContextID browserContextId
```

## Roll protocol to r1507524 — _2025-08-28T04:31:32.000Z_
######  Diff: [`8952758...f87879c`](https://github.com/ChromeDevTools/devtools-protocol/compare/8952758...f87879c)

```diff
@@ domains/Network.pdl:1107 @@ domain Network
       optional integer maxPostDataSize
       # Whether DirectSocket chunk send/receive events should be reported.
       experimental optional boolean reportDirectSocketTraffic
+      # Enable storing response bodies outside of renderer, so that these survive
+      # a cross-process navigation. Requires maxTotalBufferSize to be set.
+      # Currently defaults to false.
+      experimental optional boolean enableDurableMessages
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
```

## Roll protocol to r1505444 — _2025-08-23T04:31:11.000Z_
######  Diff: [`11bcaf8...8952758`](https://github.com/ChromeDevTools/devtools-protocol/compare/11bcaf8...8952758)

```diff
@@ domains/CSS.pdl:239 @@ experimental domain CSS
       # Computed style property value.
       string value
 
+  experimental type ComputedStyleExtraFields extends object
+    properties
+      # Returns whether or not this node is being rendered with base appearance,
+      # which happens when it has its appearance property set to base/base-select
+      # or it is in the subtree of an element being rendered with base appearance.
+      boolean isAppearanceBase
+
   # CSS style representation.
   type CSSStyle extends object
     properties
@@ -674,6 +681,9 @@ experimental domain CSS
     returns
       # Computed style for the specified DOM node.
       array of CSSComputedStyleProperty computedStyle
+      # A list of non-standard "extra fields" which blink stores alongside each
+      # computed style.
+      experimental ComputedStyleExtraFields extraFields
 
   # Resolve the specified values in the context of the provided element.
   # For example, a value of '1em' is evaluated according to the computed
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 8958da96..a8fd0f2c 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -1107,10 +1107,6 @@ domain Network
       optional integer maxPostDataSize
       # Whether DirectSocket chunk send/receive events should be reported.
       experimental optional boolean reportDirectSocketTraffic
-      # Enable storing response bodies outside of renderer, so that these survive
-      # a cross-process navigation. Requires maxTotalBufferSize to be set.
-      # Currently defaults to false.
-      experimental optional boolean enableDurableMessages
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
```

## Roll protocol to r1504847 — _2025-08-22T04:32:04.000Z_
######  Diff: [`65c042d...11bcaf8`](https://github.com/ChromeDevTools/devtools-protocol/compare/65c042d...11bcaf8)

```diff
@@ domains/Media.pdl:66 @@ experimental domain Media
       # Extra data attached to an error, such as an HRESULT, Video Codec, etc.
       object data
 
+  type Player extends object
+    properties
+      PlayerId playerId
+      optional DOM.BackendNodeId domNodeId
+
   # This can be called multiple times, and can be used to set / override /
   # remove player properties. A null propValue indicates removal.
   event playerPropertiesChanged
@@ -93,11 +98,11 @@ experimental domain Media
       array of PlayerError errors
 
   # Called whenever a player is created, or when a new agent joins and receives
-  # a list of active players. If an agent is restored, it will receive the full
-  # list of player ids and all events again.
-  event playersCreated
+  # a list of active players. If an agent is restored, it will receive one
+  # event for each active player.
+  event playerCreated
     parameters
-      array of PlayerId players
+      Player player
 
   # Enables the Media domain
   command enable
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index fca59cc7..8958da96 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -296,6 +296,25 @@ domain Network
       corp-not-same-site
       sri-message-signature-mismatch
 
+  # Sets Controls for IP Proxy of requests.
+  # Page reload is required before the new behavior will be observed.
+  experimental type IpProxyStatus extends string
+    enum
+      Available
+      FeatureNotEnabled
+      MaskedDomainListNotEnabled
+      MaskedDomainListNotPopulated
+      AuthTokensUnavailable
+      Unavailable
+      BypassedByDevTools
+
+  # Returns enum representing if IP Proxy of requests is available
+  # or reason it is not active.
+  experimental command getIPProtectionProxyStatus
+    returns
+      # Whether IP proxy is available
+      IpProxyStatus status
+
   # The reason why request was blocked.
   type CorsError extends string
     enum
@@ -1088,6 +1107,10 @@ domain Network
       optional integer maxPostDataSize
       # Whether DirectSocket chunk send/receive events should be reported.
       experimental optional boolean reportDirectSocketTraffic
+      # Enable storing response bodies outside of renderer, so that these survive
+      # a cross-process navigation. Requires maxTotalBufferSize to be set.
+      # Currently defaults to false.
+      experimental optional boolean enableDurableMessages
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
```

## Roll protocol to r1503754 — _2025-08-20T04:32:27.000Z_
######  Diff: [`d3d8ab5...65c042d`](https://github.com/ChromeDevTools/devtools-protocol/compare/d3d8ab5...65c042d)

```diff
@@ domains/Network.pdl:1088 @@ domain Network
       optional integer maxPostDataSize
       # Whether DirectSocket chunk send/receive events should be reported.
       experimental optional boolean reportDirectSocketTraffic
-      # Enable storing response bodies outside of renderer, so that these survive
-      # a cross-process navigation. Requires maxTotalBufferSize to be set.
-      # Currently defaults to false.
-      experimental optional boolean enableDurableMessages
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
```

## Roll protocol to r1503134 — _2025-08-19T04:31:54.000Z_
######  Diff: [`7bf9db8...d3d8ab5`](https://github.com/ChromeDevTools/devtools-protocol/compare/7bf9db8...d3d8ab5)

```diff
@@ domains/Network.pdl:1088 @@ domain Network
       optional integer maxPostDataSize
       # Whether DirectSocket chunk send/receive events should be reported.
       experimental optional boolean reportDirectSocketTraffic
+      # Enable storing response bodies outside of renderer, so that these survive
+      # a cross-process navigation. Requires maxTotalBufferSize to be set.
+      # Currently defaults to false.
+      experimental optional boolean enableDurableMessages
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
```

## Roll protocol to r1501779 — _2025-08-15T04:33:26.000Z_
######  Diff: [`ae77133...ce40d37`](https://github.com/ChromeDevTools/devtools-protocol/compare/ae77133...ce40d37)

```diff
@@ domains/Target.pdl:27 @@ domain Target
       experimental boolean canAccessOpener
       # Frame id of originating window (is only set if target has an opener).
       experimental optional Page.FrameId openerFrameId
+      # Id of the parent frame, only present for the "iframe" targets.
+      experimental optional Page.FrameId parentFrameId
       experimental optional Browser.BrowserContextID browserContextId
       # Provides additional details for specific target types. For example, for
       # the type of "page", this may be set to "prerender".
```

## Roll protocol to r1501221 — _2025-08-14T06:10:27.000Z_
######  Diff: [`ec909f9...073b3ab`](https://github.com/ChromeDevTools/devtools-protocol/compare/ec909f9...073b3ab)

```diff
@@ browser_protocol.pdl:54 @@ include domains/Target.pdl
 include domains/Tethering.pdl
 include domains/Tracing.pdl
 include domains/WebAudio.pdl
-include domains/WebAuthn.pdl
\ No newline at end of file
+include domains/WebAuthn.pdl
diff --git a/pdl/domains/Emulation.pdl b/pdl/domains/Emulation.pdl
index 861b76ed..13daa510 100644
--- a/pdl/domains/Emulation.pdl
+++ b/pdl/domains/Emulation.pdl
@@ -160,6 +160,56 @@ domain Emulation
     properties
       optional boolean available
 
+  experimental type WorkAreaInsets extends object
+    properties
+      # Work area top inset in pixels. Default is 0;
+      optional integer top
+      # Work area left inset in pixels. Default is 0;
+      optional integer left
+      # Work area bottom inset in pixels. Default is 0;
+      optional integer bottom
+      # Work area right inset in pixels. Default is 0;
+      optional integer right
+
+  experimental type ScreenId extends string
+
+  # Screen information similar to the one returned by window.getScreenDetails() method,
+  # see https://w3c.github.io/window-management/#screendetailed.
+  experimental type ScreenInfo extends object
+    properties
+      # Offset of the left edge of the screen.
+      integer left
+      # Offset of the top edge of the screen.
+      integer top
+      # Width of the screen.
+      integer width
+      # Height of the screen.
+      integer height
+      # Offset of the left edge of the available screen area.
+      integer availLeft
+      # Offset of the top edge of the available screen area.
+      integer availTop
+      # Width of the available screen area.
+      integer availWidth
+      # Height of the available screen area.
+      integer availHeight
+      # Specifies the screen's device pixel ratio.
+      number devicePixelRatio
+      # Specifies the screen's orientation.
+      ScreenOrientation orientation
+      # Specifies the screen's color depth in bits.
+      integer colorDepth
+      # Indicates whether the device has multiple screens.
+      boolean isExtended
+      # Indicates whether the screen is internal to the device or external, attached to the device.
+      boolean isInternal
+      # Indicates whether the screen is set as the the operating system primary screen.
+      boolean isPrimary
+      # Specifies the descriptive label for the screen.
+      string label
+      # Specifies the unique identifier of the screen.
+      ScreenId id
+
   # Tells whether emulation is supported.
   deprecated command canEmulate
     returns
@@ -520,3 +570,39 @@ domain Emulation
       # This will cause an element of size 100svh to be `difference` pixels smaller than an element
       # of size 100lvh.
       integer difference
+
+  # Returns device's screen configuration.
+  experimental command getScreenInfos
+    returns
+      array of ScreenInfo screenInfos
+
+  # Add a new screen to the device. Only supported in headless mode.
+  experimental command addScreen
+    parameters
+      # Offset of the left edge of the screen in pixels.
+      integer left
+      # Offset of the top edge of the screen in pixels.
+      integer top
+      # The width of the screen in pixels.
+      integer width
+      # The height of the screen in pixels.
+      integer height
+      # Specifies the screen's work area. Default is entire screen.
+      optional WorkAreaInsets workAreaInsets
+      # Specifies the screen's device pixel ratio. Default is 1.
+      optional number devicePixelRatio
+      # Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0.
+      optional integer rotation
+      # Specifies the screen's color depth in bits. Default is 24.
+      optional integer colorDepth
+      # Specifies the descriptive label for the screen. Default is none.
+      optional string label
+      # Indicates whether the screen is internal to the device or external, attached to the device. Default is false.
+      optional boolean isInternal
+    returns
+      ScreenInfo screenInfo
+
+  # Remove screen from the device. Only supported in headless mode.
+  experimental command removeScreen
+    parameters
+      ScreenId screenId
```

## ci: generate after split (#330) — _2025-08-13T10:53:00.000Z_
######  Diff: [`1e97f0a...1c3e94f`](https://github.com/ChromeDevTools/devtools-protocol/compare/1e97f0a...1c3e94f)

_Omitted in this docs set: this commit moved the whole protocol from two .pdl files into one file per domain (pdl/domains/*.pdl), so its diff re-adds every definition (about 28,000 lines) without changing the protocol. See the upstream changelog.md for the raw diff._

## Roll protocol to r1498597 — _2025-08-08T04:34:59.000Z_
######  Diff: [`c7b0419...418ad80`](https://github.com/ChromeDevTools/devtools-protocol/compare/c7b0419...418ad80)

```diff
@@ browser_protocol.pdl:2496 @@ experimental domain CSS
   # resolved even then, return the provided value without any changes.
   experimental command resolveValues
     parameters
-      # Substitution functions (var()/env()/attr()) and cascade-dependent
-      # keywords (revert/revert-layer) do not work.
+      # Cascade-dependent keywords (revert/revert-layer) do not work.
       array of string values
       # Id of the node in whose context the expression is evaluated
       DOM.NodeId nodeId
@@ -8690,6 +8689,7 @@ domain Page
       deferred-fetch
       deferred-fetch-minimal
       device-attributes
+      digital-credentials-create
       digital-credentials-get
       direct-sockets
       direct-sockets-private
```

## Roll protocol to r1498010 — _2025-08-07T04:35:01.000Z_
######  Diff: [`71879bd...c7b0419`](https://github.com/ChromeDevTools/devtools-protocol/compare/71879bd...c7b0419)

```diff
@@ browser_protocol.pdl:1096 @@ experimental domain Audits
     enum
       BlockedFrameNavigation
       BlockedSubresource
+      NoisedCanvasReadback
 
   # This issue warns about uses of APIs that may be considered misuse to
   # re-identify users.
@@ -1104,6 +1105,8 @@ experimental domain Audits
       UserReidentificationIssueType type
       # Applies to BlockedFrameNavigation and BlockedSubresource issue types.
       optional AffectedRequest request
+      # Applies to NoisedCanvasReadback issue type.
+      optional SourceCodeLocation sourceCodeLocation
 
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
@@ -3016,6 +3019,7 @@ domain DOM
       before
       after
       picker-icon
+      interest-hint
       marker
       backdrop
       column
```

## Roll protocol to r1495869 — _2025-08-02T04:33:09.000Z_
######  Diff: [`db8c7d5...71879bd`](https://github.com/ChromeDevTools/devtools-protocol/compare/db8c7d5...71879bd)

```diff
@@ browser_protocol.pdl:10296 @@ domain Page
       # Whether or not it was triggered by user gesture.
       boolean userGesture
 
-  # Issued for every compilation cache generated. Is only available
-  # if Page.setGenerateCompilationCache is enabled.
+  # Issued for every compilation cache generated.
   experimental event compilationCacheProduced
     parameters
       string url
@@ -12097,6 +12096,15 @@ domain Target
     parameters
       TargetInfo targetInfo
 
+  # Opens a DevTools window for the target.
+  experimental command openDevTools
+    parameters
+      # This can be the page or tab target ID.
+      TargetID targetId
+    returns
+      # The targetId of DevTools page target.
+      TargetID targetId
+
 # The Tethering domain defines methods and events for browser port binding.
 experimental domain Tethering
```

## Roll protocol to r1495237 — _2025-08-01T04:41:09.000Z_
######  Diff: [`d80b1dd...db8c7d5`](https://github.com/ChromeDevTools/devtools-protocol/compare/d80b1dd...db8c7d5)

```diff
@@ browser_protocol.pdl:825 @@ experimental domain Audits
       ValidationFailedSignatureMismatch
       ValidationFailedIntegrityMismatch
 
+  type UnencodedDigestError extends string
+    enum
+      MalformedDictionary
+      UnknownAlgorithm
+      IncorrectDigestType
+      IncorrectDigestLength
+
   # Details for issues around "Attribution Reporting API" usage.
   # Explainer: https://github.com/WICG/attribution-reporting-api
   type AttributionReportingIssueDetails extends object
@@ -863,6 +870,11 @@ experimental domain Audits
       array of string integrityAssertions
       AffectedRequest request
 
+  type UnencodedDigestIssueDetails extends object
+    properties
+      UnencodedDigestError error
+      AffectedRequest request
+
   type GenericIssueErrorType extends string
     enum
       FormLabelForNameError
@@ -1123,6 +1135,7 @@ experimental domain Audits
       SharedDictionaryIssue
       ElementAccessibilityIssue
       SRIMessageSignatureIssue
+      UnencodedDigestIssue
       UserReidentificationIssue
 
   # This struct holds a list of optional fields with additional information
@@ -1154,6 +1167,7 @@ experimental domain Audits
       optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
       optional ElementAccessibilityIssueDetails elementAccessibilityIssueDetails
       optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
+      optional UnencodedDigestIssueDetails unencodedDigestIssueDetails
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
```
