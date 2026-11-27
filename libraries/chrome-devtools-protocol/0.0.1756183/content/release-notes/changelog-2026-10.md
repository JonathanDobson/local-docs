# Chrome DevTools Protocol changelog — 2026-10

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-10, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1732152 — _2026-10-31T04:39:53.000Z_
######  Diff: [`a45ae55...92be9c2`](https://github.com/ChromeDevTools/devtools-protocol/compare/a45ae55...92be9c2)

```diff
@@ domains/Page.pdl:1227 @@ domain Page
       optional integer maxHeight
       # Maximum frame rate in frames per second.
       optional integer frameRate
+      # The area to record. Defaults to `target`.
+      experimental optional enum captureArea
+        # Records only the target page.
+        target
+        # Records the browser window that shows the target, like window
+        # capture with getDisplayMedia(). If the target is a docked DevTools
+        # window, the window shows DevTools and the inspected page. Only
+        # available to trusted clients and to embedders that support it.
+        browserWindow
     returns
       # A handle of the stream that holds resulting screencast data.
       experimental IO.StreamHandle stream
```

## Roll protocol to r1727723 — _2026-10-27T04:43:32.000Z_
######  Diff: [`7245ec5...ebca906`](https://github.com/ChromeDevTools/devtools-protocol/compare/7245ec5...ebca906)

```diff
@@ domains/Preload.pdl:192 @@ experimental domain Preload
       PrerenderHostReused
       FormSubmitWhenPrerendering
       CrossDocumentRestart
+      PrefetchFailedCrossOriginSubframe
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1724436 — _2026-10-22T04:44:00.000Z_
######  Diff: [`71ba93d...7245ec5`](https://github.com/ChromeDevTools/devtools-protocol/compare/71ba93d...7245ec5)

```diff
@@ domains/Network.pdl:2104 @@ domain Network
       PreProvisionedKeyNotFound
       AttestationCertificationError
       AttestationSigningError
+      FederatedRegistrationRedirected
   # LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult)
 
   # Details about a failed device bound session network request.
```

## Roll protocol to r1723477 — _2026-10-21T04:41:19.000Z_
######  Diff: [`95b1af6...71ba93d`](https://github.com/ChromeDevTools/devtools-protocol/compare/95b1af6...71ba93d)

```diff
@@ domains/Network.pdl:1569 @@ domain Network
   experimental event directUDPSocketJoinedMulticastGroup
     parameters
       RequestId identifier
+      # Multicast group address.
       string IPAddress
+      # Source address of a source-specific multicast (SSM) membership. Absent
+      # for any-source multicast (ASM) memberships.
+      optional string sourceAddress
 
   experimental event directUDPSocketLeftMulticastGroup
     parameters
       RequestId identifier
+      # Multicast group address.
       string IPAddress
+      # Source address of a source-specific multicast (SSM) membership. Absent
+      # for any-source multicast (ASM) memberships.
+      optional string sourceAddress
 
 
   # Fired upon direct_socket.UDPSocket creation.
```

## Roll protocol to r1721602 — _2026-10-19T04:39:23.000Z_
######  Diff: [`a07da3c...95b1af6`](https://github.com/ChromeDevTools/devtools-protocol/compare/a07da3c...95b1af6)

```diff
@@ domains/Autofill.pdl:86 @@ experimental domain Autofill
 
   # Trigger autofill on a form identified by the fieldId.
   # If the field and related form cannot be autofilled, returns an error.
+  # Returns once the values have been applied to the form fields.
   command trigger
     parameters
       # Identifies a field that serves as an anchor for autofill.
```

## Roll protocol to r1721318 — _2026-10-17T04:40:04.000Z_
######  Diff: [`e908551...a07da3c`](https://github.com/ChromeDevTools/devtools-protocol/compare/e908551...a07da3c)

```diff
@@ domains/Browser.pdl:230 @@ domain Browser
   # frame and is removed when the DevTools session that created it disconnects.
   experimental command addMockCamera
     parameters
-      # Required non-empty identifier for the mock camera. This is mapped to an
-      # internal virtual-device identifier and is not the MediaDeviceInfo.deviceId
-      # exposed to the page.
+      # Required non-empty identifier for the mock camera within the current
+      # DevTools session. Different sessions can use the same identifier
+      # without replacing each other's cameras. This is not the
+      # MediaDeviceInfo.deviceId exposed to the page.
       string deviceId
 
   # Chrome histogram bucket.
```

## Roll protocol to r1720385 — _2026-10-16T04:43:16.000Z_
######  Diff: [`dfad770...e908551`](https://github.com/ChromeDevTools/devtools-protocol/compare/dfad770...e908551)

```diff
@@ domains/Network.pdl:2139 @@ domain Network
         RefreshedAsWaiter
         TransientSigningError
         InScopeRefreshNotYetNeeded
+        Canceled
       # LINT.ThenChange(//net/device_bound_sessions/refresh_result.h:DeviceBoundSessionRefreshResult,//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionRefreshResult)
       # If there was a fetch attempt, the result of that.
       optional DeviceBoundSessionFetchResult fetchResult
```

## Roll protocol to r1718299 — _2026-10-14T04:41:00.000Z_
######  Diff: [`52f4748...dfad770`](https://github.com/ChromeDevTools/devtools-protocol/compare/52f4748...dfad770)

```diff
@@ domains/Page.pdl:164 @@ domain Page
       sync-xhr
       tools
       translator
+      unbounded-element
       unload
       usb
       usb-unrestricted
```

## Roll protocol to r1717327 — _2026-10-13T04:49:47.000Z_
######  Diff: [`c3ed21b...52f4748`](https://github.com/ChromeDevTools/devtools-protocol/compare/c3ed21b...52f4748)

```diff
@@ domains/IO.pdl:36 @@ domain IO
       boolean eof
 
   # Return UUID of Blob object specified by a remote object id.
-  command resolveBlob
+  deprecated command resolveBlob
     parameters
       # Object id of a Blob object wrapper.
       Runtime.RemoteObjectId objectId
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index c708fa82..9a00bbe6 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1827,3 +1827,10 @@ domain Page
       # The format is defined by the `AnnotatedPageContent` message in
       # components/optimization_guide/proto/features/common_quality_data.proto
       binary content
+
+  # Configures input visualization on the page.
+  experimental command setInputVisualization
+    parameters
+      # Whether to enable click visualization.
+      optional boolean clicks
+
```

## Roll protocol to r1716261 — _2026-10-10T04:40:11.000Z_
######  Diff: [`8033bef...c3ed21b`](https://github.com/ChromeDevTools/devtools-protocol/compare/8033bef...c3ed21b)

```diff
@@ domains/Network.pdl:1300 @@ domain Network
       MonotonicTime timestamp
       # Total number of bytes received for this request.
       number encodedDataLength
+      # Size of the response body before removing content encodings.
+      # Includes cached bodies, but excludes headers and transfer framing.
+      experimental optional number encodedBodyLength
 
   # Fired if request ended up loading from cache.
   event requestServedFromCache
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 9c77ce72..c708fa82 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -156,10 +156,6 @@ domain Page
       rewriter
       screen-wake-lock
       serial
-      # Deprecated.
-      shared-storage
-      # Deprecated.
-      shared-storage-select-url
       smart-card
       speaker-selection
       storage-access
```

## Roll protocol to r1714151 — _2026-10-08T04:46:24.000Z_
######  Diff: [`d209a9a...8033bef`](https://github.com/ChromeDevTools/devtools-protocol/compare/d209a9a...8033bef)

```diff
@@ domains/Audits.pdl:406 @@ experimental domain Audits
       FormModelContextMissingToolDescription
       FormModelContextRequiredParameterMissingName
       FormModelContextParameterMissingName
+      GeolocationPromptWithoutUserGesture
 
   # Depending on the concrete errorType, different properties are set.
   type GenericIssueDetails extends object
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 20b5db99..9c77ce72 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -852,6 +852,16 @@ domain Page
       # script). Only sent if frame is labelled as an ad and ids are available.
       optional Network.AdAncestry adScriptAncestry
 
+  # Returns the words that the frame's document added to its spell check custom
+  # dictionary with `document.spellCheckCustomDictionary.addWords()`, sorted.
+  # Page script cannot read the dictionary back; this lets developers inspect
+  # it.
+  experimental command getSpellCheckCustomDictionary
+    parameters
+      FrameId frameId
+    returns
+      array of string words
+
   # Returns present frame tree structure.
   command getFrameTree
     returns
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 53096d45..7f1e0829 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -569,6 +569,10 @@ domain Debugger
     parameters
       # The skipList specifies location ranges that should be skipped on step over.
       experimental optional array of LocationRange skipList
+      # Functions whose source range lies within one of the enterRanges are
+      # entered as if by stepInto, even when they are called (directly or
+      # indirectly) from a call that is stepped over.
+      experimental optional array of LocationRange enterRanges
 
   # Fired when breakpoint is resolved to an actual script and location.
   # Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.
```

## Roll protocol to r1710668 — _2026-10-03T04:42:40.000Z_
######  Diff: [`3e46e43...d209a9a`](https://github.com/ChromeDevTools/devtools-protocol/compare/3e46e43...d209a9a)

```diff
@@ domains/CSS.pdl:712 @@ experimental domain CSS
       # Boolean indicating if this is on or off.
       boolean forced
 
+  # Forces a position-try option for the given node.
+  command forcePositionTryOption
+    parameters
+      # The element id for which to force the position-try option.
+      DOM.NodeId nodeId
+      # The 1-based index of the position-try fallback option, 0 for base position (no fallback),
+      # or omitted to clear the forced state.
+      optional integer index
+
   command getBackgroundColors
     parameters
       # Id of the node to get background colors for.
```

## Roll protocol to r1709723 — _2026-10-02T04:43:00.000Z_
######  Diff: [`8b7f1d9...3e46e43`](https://github.com/ChromeDevTools/devtools-protocol/compare/8b7f1d9...3e46e43)

```diff
@@ js_protocol.pdl:143 @@ domain Debugger
       optional Location startLocation
       # Location in the source code where scope ends
       optional Location endLocation
-      # True if the scope does not declare any variables.
-      # Only present if true.
+      # Present if the scope has no variable values to show. Absent means that
+      # the scope declares at least one variable with an available value.
       # Empty scopes are retained in the scope chain because
       # they can be targeted via `evaluateOnCallFrame` (using `scopeNumber`) or
       # matched against scopes in source maps.
-      experimental optional boolean empty
+      experimental optional enum emptyReason
+        # The scope does not declare any variables.
+        no-variables
+        # The scope declares variables, but none of their values are available
+        # (e.g. because they were optimized out or are in their TDZ).
+        all-unavailable
 
   # Search match for resource.
   type SearchMatch extends object
```
