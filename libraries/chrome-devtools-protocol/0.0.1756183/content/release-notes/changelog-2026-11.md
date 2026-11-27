# Chrome DevTools Protocol changelog — 2026-11

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-11, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1756183 — _2026-11-27T04:30:09.000Z_
######  Diff: [`2711fe1...56496a4`](https://github.com/ChromeDevTools/devtools-protocol/compare/2711fe1...56496a4)

```diff
@@ domains/Browser.pdl:224 @@ domain Browser
       # Commandline parameters
       array of string arguments
 
-  # Adds or updates a mock camera in the shared video capture device list for
+  # Adds a mock camera in the shared video capture device list for
   # test automation. The mock camera is not scoped to a particular page or
   # frame and is removed when the DevTools session that created it disconnects.
+  # Returns success after the video capture service confirms registration.
+  # Does not wait for device-list updates or devicechange events in pages.
+  # Registration failures are reported as errors.
   experimental command addMockCamera
     parameters
       # Required non-empty identifier for the mock camera within the current
       # DevTools session. Different sessions can use the same identifier
       # without replacing each other's cameras. This is not the
       # MediaDeviceInfo.deviceId exposed to the page.
+      # An identifier that is already registered or being registered in this
+      # session is rejected. The existing camera or registration attempt is
+      # left unchanged, including any active streams.
       string deviceId
 
   # Chrome histogram bucket.
```

## Roll protocol to r1755318 — _2026-11-26T04:29:19.000Z_
######  Diff: [`856c4ed...2711fe1`](https://github.com/ChromeDevTools/devtools-protocol/compare/856c4ed...2711fe1)

```diff
@@ domains/Network.pdl:220 @@ domain Network
       experimental optional boolean isSameSite
       # True when the resource request is ad-related.
       experimental optional boolean isAdRelated
+      # The provenance of an ad resource request, if it is ad-related and
+      # provenance is available.
+      experimental optional AdProvenance adProvenance
 
   # Details of a signed certificate timestamp (SCT).
   type SignedCertificateTimestamp extends object
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index bcd5a4d5..efbac6fe 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -194,6 +194,7 @@ experimental domain Preload
       CrossDocumentRestart
       PrefetchFailedCrossOriginSubframe
       UnexpectedMainFrameNavigation
+      AudioOutput
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1754134 — _2026-11-25T04:30:01.000Z_
######  Diff: [`4593138...856c4ed`](https://github.com/ChromeDevTools/devtools-protocol/compare/4593138...856c4ed)

```diff
@@ domains/Audits.pdl:780 @@ experimental domain Audits
       # Frame containing the image.
       Page.FrameId frameId
 
+  # Details for issues about a page that declares viewport-fit=cover, receives
+  # a non-zero top safe-area inset (e.g. a device cutout or system status bar),
+  # but does not consume env(safe-area-inset-top) anywhere in its CSS while
+  # having DOM content likely to be occluded by that inset.
+  type ViewportFitCoverMissingSafeAreaInsetTopIssueDetails extends object
+    properties
+      # The frame that triggered the issue.
+      Page.FrameId frameId
+
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
   # information about the kind of issue.
@@ -817,6 +826,7 @@ experimental domain Audits
       EmailVerificationRequestIssue
       LazyLoadImageIssue
       WebInstallIssue
+      ViewportFitCoverMissingSafeAreaInsetTopIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -854,6 +864,7 @@ experimental domain Audits
       optional EmailVerificationRequestIssueDetails emailVerificationRequestIssueDetails
       optional LazyLoadImageIssueDetails lazyLoadImageIssueDetails
       optional WebInstallIssueDetails webInstallIssueDetails
+      optional ViewportFitCoverMissingSafeAreaInsetTopIssueDetails viewportFitCoverMissingSafeAreaInsetTopIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
```

## Roll protocol to r1752859 — _2026-11-24T04:34:30.000Z_
######  Diff: [`62afb85...4593138`](https://github.com/ChromeDevTools/devtools-protocol/compare/62afb85...4593138)

```diff
@@ domains/Emulation.pdl:258 @@ domain Emulation
     parameters
       SafeAreaInsets insets
 
-  # Overrides virtual keyboard geometry in CSS pixels, relative to the top-level viewport. The
-  # provided rect is used for navigator.virtualKeyboard.boundingRect, geometrychange events, and
-  # env(keyboard-inset-*) values on the inspected frame. The override applies independently of
-  # navigator.virtualKeyboard.overlaysContent so clients can preview overlay geometry without
-  # mutating page state. Values are rounded to the nearest CSS pixel. Omitting the rect clears the
-  # override.
-  experimental command setVirtualKeyboardGeometryOverride
-    parameters
-      optional DOM.Rect keyboardRect
-
   # Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
   # window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
   # query results).
```

## Roll protocol to r1751165 — _2026-11-21T04:32:13.000Z_
######  Diff: [`cc9d57b...62afb85`](https://github.com/ChromeDevTools/devtools-protocol/compare/cc9d57b...62afb85)

```diff
@@ domains/Network.pdl:32 @@ domain Network
       CSPViolationReport
       Preflight
       FedCM
+      EmailVerification
       Other
 
   # Unique loader identifier.
@@ -546,6 +547,7 @@ domain Network
         SignedExchange
         preflight
         FedCM
+        EmailVerification
         other
       # Initiator JavaScript stack trace, set for Script only.
       # Requires the Debugger domain to be enabled.
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 3da7a899..0a25270e 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1022,6 +1022,11 @@ domain Page
       # loader id does not match the provided id. This prevents accidentally
       # reloading an unintended target in case there's a racing navigation.
       experimental optional Network.LoaderId loaderId
+      # If true and the page has POST data, the browser shows the form
+      # resubmission dialog before the reload. The command returns after the
+      # user responds to the dialog. If the user cancels the dialog, the
+      # command returns an error. The default value is false.
+      experimental optional boolean checkForRepost
 
   # Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
   experimental deprecated command removeScriptToEvaluateOnLoad
```

## Roll protocol to r1750115 — _2026-11-20T04:34:12.000Z_
######  Diff: [`d21ec9f...cc9d57b`](https://github.com/ChromeDevTools/devtools-protocol/compare/d21ec9f...cc9d57b)

```diff
@@ domains/Audits.pdl:637 @@ experimental domain Audits
       InteractiveContentOptionChild
       InteractiveContentLegendChild
       InteractiveContentSummaryDescendant
+      AnchorMenuDescendant
+      InteractiveContentMenuDescendant
+      TextMenuDescendant
 
-  # This issue warns about errors in the select or summary element content model.
+  # This issue warns about errors in the select, summary, or menu element content model.
   type ElementAccessibilityIssueDetails extends object
     properties
       DOM.BackendNodeId nodeId
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index da77927f..e3ebfd2f 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -2105,6 +2105,7 @@ domain Network
       AttestationCertificationError
       AttestationSigningError
       FederatedRegistrationRedirected
+      CrossSiteRefreshSessionConfig
   # LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult)
 
   # Details about a failed device bound session network request.
```

## Roll protocol to r1748923 — _2026-11-19T04:31:18.000Z_
######  Diff: [`95a78c6...d21ec9f`](https://github.com/ChromeDevTools/devtools-protocol/compare/95a78c6...d21ec9f)

```diff
@@ domains/Target.pdl:34 @@ domain Target
       experimental optional Page.FrameId parentFrameId
       experimental optional Browser.BrowserContextID browserContextId
       # Provides additional details for specific target types. For example, for
-      # the type of "page", this may be set to "prerender".
+      # the type of "page", this may be set to "prerender", and for "tab", this
+      # may be set to "unloaded". An unloaded tab has a history entry, but no
+      # document for it: for example, after the tab was discarded, after
+      # session restore without load, or after the renderer crashed. The tab
+      # stays unloaded until a new document commits. A new tab that has not
+      # navigated is not unloaded. Target.targetInfoChanged reports changes of
+      # this value for tabs.
       experimental optional string subtype
       # Embedder-specific target metadata. This is only set for targets of
       # type "tab".
```

## Roll protocol to r1747637 — _2026-11-18T04:30:15.000Z_
######  Diff: [`65346a3...95a78c6`](https://github.com/ChromeDevTools/devtools-protocol/compare/65346a3...95a78c6)

```diff
@@ js_protocol.pdl:1068 @@ domain Runtime
     properties
       enum serialization
         # Whether the result should be deep-serialized. The result is put into
-        # `deepSerializedValue` and `ObjectId` is provided.
+        # `deepSerializedValue`; `objectId` is provided for objects and symbols.
+        # `value` and `unserializableValue` are not set.
         deep
         # Whether the result is expected to be a JSON object which should be sent by value.
         # The result is put either into `value` or into `unserializableValue`. Synonym of
@@ -1170,9 +1171,10 @@ domain Runtime
       # Object class (constructor) name. Specified for `object` type values only.
       optional string className
       # Remote object value in case of primitive values or JSON values (if it was requested).
+      # Not set in `deep` serialization mode, see `deepSerializedValue`.
       optional any value
       # Primitive value which can not be JSON-stringified does not have `value`, but gets this
-      # property.
+      # property. Not set in `deep` serialization mode, see `deepSerializedValue`.
       optional UnserializableValue unserializableValue
       # String representation of the object.
       optional string description
```

## Roll protocol to r1746437 — _2026-11-17T04:34:05.000Z_
######  Diff: [`dd55cb6...65346a3`](https://github.com/ChromeDevTools/devtools-protocol/compare/dd55cb6...65346a3)

```diff
@@ domains/Preload.pdl:193 @@ experimental domain Preload
       FormSubmitWhenPrerendering
       CrossDocumentRestart
       PrefetchFailedCrossOriginSubframe
+      UnexpectedMainFrameNavigation
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1744848 — _2026-11-14T04:32:42.000Z_
######  Diff: [`c092aa9...dd55cb6`](https://github.com/ChromeDevTools/devtools-protocol/compare/c092aa9...dd55cb6)

```diff
@@ domains/BluetoothEmulation.pdl:200 @@ experimental domain BluetoothEmulation
     parameters
       string address
 
+  # Simulates the ATT MTU exchange procedure from Bluetooth Core Specification
+  # Vol 3 Part F 3.4.2 establishing |mtu| for the connection to the peripheral
+  # with |address|.
+  command simulateGATTMtuChange
+    parameters
+      string address
+      integer mtu
+
   # Event for when a GATT operation of |type| to the peripheral with |address|
   # happened.
   event gattOperationReceived
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 5862a6bb..90e37017 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -79,7 +79,6 @@ domain DOM
       select-listbox
       permission-icon
       overscroll-area-parent
-      overscroll-backdrop
       skeleton
 
   # Shadow root type.
```

## Roll protocol to r1743766 — _2026-11-13T04:33:08.000Z_
######  Diff: [`d961d96...c092aa9`](https://github.com/ChromeDevTools/devtools-protocol/compare/d961d96...c092aa9)

```diff
@@ js_protocol.pdl:246 @@ domain Debugger
       # List of the possible breakpoint locations.
       array of BreakLocation locations
 
+  # Returns the current scope chain of the given call frame. Unlike the scope chain reported
+  # with the `paused` event, it reflects changes made to variables since then (e.g. via
+  # `evaluateOnCallFrame` or `setVariableValue`).
+  experimental command getScopeChain
+    parameters
+      # Call frame identifier to get the scope chain for.
+      CallFrameId callFrameId
+    returns
+      # Scope chain for the call frame.
+      array of Scope scopeChain
+
   # Returns source for the script with given id.
   command getScriptSource
     parameters
```

## Roll protocol to r1742540 — _2026-11-12T04:30:22.000Z_
######  Diff: [`f574964...d961d96`](https://github.com/ChromeDevTools/devtools-protocol/compare/f574964...d961d96)

```diff
@@ domains/Browser.pdl:337 @@ domain Browser
     parameters
       BrowserCommandId commandId
 
-  # Allows a site to use privacy sandbox features that require enrollment
-  # without the site actually being enrolled. Only supported on page targets.
-  command addPrivacySandboxEnrollmentOverride
-    parameters
-      string url
-
   # Gets the current globally-applied privacy control status
   # See https://www.w3.org/TR/gpc/#get-global-privacy-control
   experimental command getGlobalPrivacyControl
```

## Roll protocol to r1740066 — _2026-11-10T04:34:49.000Z_
######  Diff: [`b0d96c6...f574964`](https://github.com/ChromeDevTools/devtools-protocol/compare/b0d96c6...f574964)

```diff
@@ domains/WebMCP.pdl:66 @@ experimental domain WebMCP
   # Disables the WebMCP domain.
   command disable
 
-   # Invokes a registered tool.
+  # Invokes a registered tool. Exactly one of `toolId` and `toolName` must be specified; the command fails if both or
+  # neither are.
   command invokeTool
     parameters
       # Frame in which to invoke the tool.
       Page.FrameId frameId
-      # Name of the tool to invoke.
-      string toolName
+      # Identifier of the tool to invoke, as reported in `Tool.toolId`. Invokes exactly that tool, and fails if it is no
+      # longer registered, even if a different tool has since been registered under the same name.
+      optional ToolId toolId
+      # Name of the tool to invoke. Deprecated: invokes whichever tool is registered under this name when the command
+      # is handled, which may not be the tool the client observed if the page has since replaced it. Use `toolId`
+      # instead.
+      deprecated optional string toolName
       # Input parameters for the tool, matching the tool's inputSchema.
       object input
     returns
```

## Roll protocol to r1734725 — _2026-11-04T04:37:37.000Z_
######  Diff: [`2e90ef3...b0d96c6`](https://github.com/ChromeDevTools/devtools-protocol/compare/2e90ef3...b0d96c6)

```diff
@@ domains/Page.pdl:153 @@ domain Page
       publickey-credentials-remote-client-data-json
       rewriter
       screen-wake-lock
+      semantic-embedder
       serial
       smart-card
       speaker-selection
```

## Roll protocol to r1733639 — _2026-11-03T05:03:18.000Z_
######  Diff: [`92be9c2...2e90ef3`](https://github.com/ChromeDevTools/devtools-protocol/compare/92be9c2...2e90ef3)

```diff
@@ domains/Browser.pdl:64 @@ domain Browser
       smartCard
       speakerSelection
       storageAccess
-      topLevelStorageAccess
       videoCapture
       vr
       wakeLockScreen
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 2a36c411..b418f0c3 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -77,7 +77,6 @@ domain Page
       autofill
       autoplay
       bluetooth
-      browsing-topics
       camera
       captured-surface-control
       ch-dpr
@@ -131,7 +130,6 @@ domain Page
       hid
       identity-credentials-get
       idle-detection
-      interest-cohort
       keyboard-map
       language-detector
       language-model
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index 48bd8be7..9e163427 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -31,15 +31,24 @@ experimental domain WebMCP
       Canceled
       Error
 
+  # Unique identifier of a registered tool. A new identifier is created every time a tool is registered, so a tool that
+  # is unregistered and then registered again under the same name gets a different identifier. Clients should treat it
+  # as an opaque string.
+  type ToolId extends string
+
   # Definition of a tool that can be invoked.
   type Tool extends object
     properties
+      # Tool identifier.
+      ToolId toolId
       # Tool name.
       string name
       # Tool description.
       string description
       # Schema for the tool's input parameters.
       optional object inputSchema
+      # Schema for the tool's output structure.
+      optional object outputSchema
       # Optional annotations for the tool.
       optional Annotation annotations
       # Frame identifier associated with the tool registration.
@@ -85,6 +94,8 @@ experimental domain WebMCP
   # Definition of a tool that was removed.
   type RemovedTool extends object
     properties
+      # Identifier of the removed tool.
+      ToolId toolId
       # Tool name.
       string name
       # Frame identifier associated with the tool registration.
@@ -99,14 +110,18 @@ experimental domain WebMCP
   # Event fired when a tool invocation starts.
   event toolInvoked
     parameters
-      # Name of the tool to invoke.
-      string toolName
       # Frame id
       Page.FrameId frameId
       # Invocation identifier.
       string invocationId
       # The input parameters used for the invocation.
       string input
+      # Name of the tool to invoke. Missing if the tool was invoked by its identifier, but could not be found (e.g.,
+      # it was already unregistered), so its name could not be recovered.
+      optional string toolName
+      # Identifier of the tool to invoke. Missing if the tool was invoked by name, but could not be found, so its
+      # identifier could not be recovered.
+      optional ToolId toolId
 
   # Event fired when a tool invocation completes or fails.
   event toolResponded
```
