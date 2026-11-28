# Chrome DevTools Protocol changelog — 2025-12

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-12, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1560991 — _2025-12-19T04:33:52.000Z_
######  Diff: [`ead0e84...2b34c65`](https://github.com/ChromeDevTools/devtools-protocol/compare/ead0e84...2b34c65)

```diff
@@ domains/Network.pdl:166 @@ domain Network
       High
       VeryHigh
 
+  # The render blocking behavior of a resource request.
+  experimental type RenderBlockingBehavior extends string
+    enum
+      Blocking
+      InBodyParserBlocking
+      NonBlocking
+      NonBlockingDynamic
+      PotentiallyBlocking
+
   # Post data entry for HTTP request
   type PostDataEntry extends object
     properties
@@ -1498,6 +1507,8 @@ domain Network
       optional Page.FrameId frameId
       # Whether the request is initiated by a user gesture. Defaults to false.
       optional boolean hasUserGesture
+      # The render blocking behavior of the request.
+      experimental optional RenderBlockingBehavior renderBlockingBehavior
 
   # Fired when resource loading priority is changed
   experimental event resourceChangedPriority
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index bd96c7cc..987851bc 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -164,7 +164,9 @@ domain Page
       language-detector
       language-model
       local-fonts
+      local-network
       local-network-access
+      loopback-network
       magnetometer
       manual-text
       media-playback-while-not-visible
diff --git a/pdl/domains/Tracing.pdl b/pdl/domains/Tracing.pdl
index 44fc3f39..5103577e 100644
--- a/pdl/domains/Tracing.pdl
+++ b/pdl/domains/Tracing.pdl
@@ -78,6 +78,12 @@ domain Tracing
       # A list of supported tracing categories.
       array of string categories
 
+  # Return a descriptor for all available tracing categories.
+  experimental command getTrackEventDescriptor
+    returns
+      # Base64-encoded serialized perfetto.protos.TrackEventDescriptor protobuf message.
+      binary descriptor
+
   # Record a clock sync marker in the trace.
   experimental command recordClockSyncMarker
     parameters
```

## Roll protocol to r1559729 — _2025-12-17T04:33:54.000Z_
######  Diff: [`d90a8a2...ead0e84`](https://github.com/ChromeDevTools/devtools-protocol/compare/d90a8a2...ead0e84)

```diff
@@ domains/Network.pdl:1145 @@ domain Network
       experimental optional boolean reportDirectSocketTraffic
       # Enable storing response bodies outside of renderer, so that these survive
       # a cross-process navigation. Requires maxTotalBufferSize to be set.
-      # Currently defaults to false.
+      # Currently defaults to false. This field is being deprecated in favor of the dedicated
+      # configureDurableMessages command, due to the possibility of deadlocks when awaiting
+      # Network.enable before issuing Runtime.runIfWaitingForDebugger.
       experimental optional boolean enableDurableMessages
 
+  # Configures storing response bodies outside of renderer, so that these survive
+  # a cross-process navigation.
+  # If maxTotalBufferSize is not set, durable messages are disabled.
+  experimental command configureDurableMessages
+    parameters
+      # Buffer size in bytes to use when preserving network payloads (XHRs, etc).
+      optional integer maxTotalBufferSize
+      # Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
+      optional integer maxResourceBufferSize
+
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
   # Deprecated. Use Storage.getCookies instead.
```

## Roll protocol to r1558402 — _2025-12-13T04:32:36.000Z_
######  Diff: [`ab59de7...d90a8a2`](https://github.com/ChromeDevTools/devtools-protocol/compare/ab59de7...d90a8a2)

```diff
@@ domains/Browser.pdl:49 @@ domain Browser
       idleDetection
       keyboardLock
       localFonts
+      localNetwork
       localNetworkAccess
+      loopbackNetwork
       midi
       midiSysex
       nfc
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index d61ab3ca..8d8ead63 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -132,6 +132,8 @@ domain Target
     returns
       # An array of browser context ids.
       array of Browser.BrowserContextID browserContextIds
+      # The id of the default browser context if available.
+      experimental optional Browser.BrowserContextID defaultBrowserContextId
 
   # Creates a new page.
   command createTarget
```

## Roll protocol to r1557841 — _2025-12-12T04:33:57.000Z_
######  Diff: [`6a7ac7d...ab59de7`](https://github.com/ChromeDevTools/devtools-protocol/compare/6a7ac7d...ab59de7)

```diff
@@ domains/Audits.pdl:412 @@ experimental domain Audits
       FormInputHasWrongButWellIntendedAutocompleteValueError
       ResponseWasBlockedByORB
       NavigationEntryMarkedSkippable
+      AutofillAndManualTextPolicyControlledFeaturesInfo
+      AutofillPolicyControlledFeatureInfo
+      ManualTextPolicyControlledFeatureInfo
 
   # Depending on the concrete errorType, different properties are set.
   type GenericIssueDetails extends object
```

## Roll protocol to r1555890 — _2025-12-09T04:33:09.000Z_
######  Diff: [`47b9187...6a7ac7d`](https://github.com/ChromeDevTools/devtools-protocol/compare/47b9187...6a7ac7d)

```diff
@@ domains/DOM.pdl:76 @@ domain DOM
       picker
       permission-icon
       overscroll-area-parent
-      overscroll-client-area
 
   # Shadow root type.
   type ShadowRootType extends string
```
