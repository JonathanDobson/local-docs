# Chrome DevTools Protocol changelog — 2024-08

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-08, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1349043 — _2024-08-30T04:28:39.000Z_
######  Diff: [`487d94d...c79610f`](https://github.com/ChromeDevTools/devtools-protocol/compare/487d94d...c79610f)

```diff
@@ browser_protocol.pdl:10668 @@ experimental domain Storage
       array of AttributionReportingAggregatableDebugReportingData debugData
       optional string aggregationCoordinatorOrigin
 
+  experimental type AttributionScopesData extends object
+    properties
+      array of string values
+      # number instead of integer because not all uint32 can be represented by
+      # int
+      number limit
+      number maxEventStates
+
   experimental type AttributionReportingSourceRegistration extends object
     properties
       Network.TimeSinceEpoch time
@@ -10688,6 +10696,7 @@ experimental domain Storage
       AttributionReportingTriggerDataMatching triggerDataMatching
       SignedInt64AsBase10 destinationLimitPriority
       AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
+      optional AttributionScopesData scopesData
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
@@ -10764,6 +10773,7 @@ experimental domain Storage
       AttributionReportingSourceRegistrationTimeConfig sourceRegistrationTimeConfig
       optional string triggerContextId
       AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
+      array of string scopes
 
   experimental type AttributionReportingEventLevelResult extends string
     enum
@@ -12415,7 +12425,6 @@ experimental domain Preload
       PrefetchFailedMIMENotSupported
       PrefetchFailedNetError
       PrefetchFailedNon2XX
-      PrefetchFailedPerPageLimitExceeded
       PrefetchEvictedAfterCandidateRemoved
       PrefetchEvictedForNewerPrefetch
       PrefetchHeldback
```

## Roll protocol to r1348440 — _2024-08-29T04:28:12.000Z_
######  Diff: [`81f12ac...487d94d`](https://github.com/ChromeDevTools/devtools-protocol/compare/81f12ac...487d94d)

```diff
@@ browser_protocol.pdl:9220 @@ domain Page
         # A new frame target will be created (see Target.attachedToTarget).
         swap
 
+  # Fired before frame subtree is detached. Emitted before any frame of the
+  # subtree is actually detached.
+  experimental event frameSubtreeWillBeDetached
+    parameters
+      # Id of the frame that is the root of the subtree that will be detached.
+      FrameId frameId
+
   # The type of a frameNavigated event.
   experimental type NavigationType extends string
     enum
```

## Roll protocol to r1347815 — _2024-08-28T04:28:21.000Z_
######  Diff: [`ad08fca...81f12ac`](https://github.com/ChromeDevTools/devtools-protocol/compare/ad08fca...81f12ac)

```diff
@@ browser_protocol.pdl:10696 @@ experimental domain Storage
       destinationBothLimitsReached
       reportingOriginsPerSiteLimitReached
       exceedsMaxChannelCapacity
+      exceedsMaxScopesChannelCapacity
       exceedsMaxTriggerStateCardinality
+      exceedsMaxEventStatesLimit
       destinationPerDayReportingLimitReached
 
   experimental event attributionReportingSourceRegistered
```

## Roll protocol to r1347151 — _2024-08-27T04:29:22.000Z_
######  Diff: [`09ae3f7...ad08fca`](https://github.com/ChromeDevTools/devtools-protocol/compare/09ae3f7...ad08fca)

```diff
@@ browser_protocol.pdl:743 @@ experimental domain Audits
       NoRegisterTriggerHeader
       NoRegisterOsSourceHeader
       NoRegisterOsTriggerHeader
+      NavigationRegistrationUniqueScopeAlreadySet
 
   type SharedDictionaryError extends string
     enum
@@ -5523,12 +5524,21 @@ experimental domain Memory
       moderate
       critical
 
+  # Retruns current DOM object counters.
   command getDOMCounters
     returns
       integer documents
       integer nodes
       integer jsEventListeners
 
+  # Retruns DOM object counters after preparing renderer for leak detection.
+  command getDOMCountersForLeakDetection
+    returns
+      # DOM object counters.
+      array of DOMCounter counters
+
+  # Prepares for leak detection by terminating workers, stopping spellcheckers,
+  # dropping non-essential internal caches, running garbage collections, etc.
   command prepareForLeakDetection
 
   # Simulate OomIntervention by purging V8 memory.
@@ -5604,6 +5614,15 @@ experimental domain Memory
       # Size of the module in bytes.
       number size
 
+  # DOM object counter data.
+  type DOMCounter extends object
+    properties
+      # Object name. Note: object names should be presumed volatile and clients should not expect
+      # the returned names to be consistent across runs.
+      string name
+      # Object count.
+      integer count
+
 # Network domain allows tracking network activities of the page. It exposes information about http,
 # file, data and other requests and responses, their headers, bodies, timing, etc.
 domain Network
@@ -6341,6 +6360,8 @@ domain Network
       TPCDMetadata
       # The cookie should have been blocked by 3PCD but is exempted by Deprecation Trial mitigation.
       TPCDDeprecationTrial
+      # The cookie should have been blocked by 3PCD but is exempted by Top-level Deprecation Trial mitigation.
+      TopLevelTPCDDeprecationTrial
       # The cookie should have been blocked by 3PCD but is exempted by heuristics mitigation.
       TPCDHeuristics
       # The cookie should have been blocked by 3PCD but is exempted by Enterprise Policy.
```

## Roll protocol to r1346313 — _2024-08-24T04:27:30.000Z_
######  Diff: [`08dfe29...09ae3f7`](https://github.com/ChromeDevTools/devtools-protocol/compare/08dfe29...09ae3f7)

```diff
@@ browser_protocol.pdl:1392 @@ domain Browser
       videoCapturePanTiltZoom
       wakeLockScreen
       wakeLockSystem
+      webAppInstallation
       windowManagement
 
   experimental type PermissionSetting extends string
@@ -8098,6 +8099,7 @@ domain Page
       usb
       usb-unrestricted
       vertical-scroll
+      web-app-installation
       web-printing
       web-share
       window-management
```

## Roll protocol to r1345247 — _2024-08-22T04:27:41.000Z_
######  Diff: [`084b75c...08dfe29`](https://github.com/ChromeDevTools/devtools-protocol/compare/084b75c...08dfe29)

```diff
@@ browser_protocol.pdl:8077 @@ domain Page
       otp-credentials
       payment
       picture-in-picture
+      popins
       private-aggregation
       private-state-token-issuance
       private-state-token-redemption
@@ -9453,6 +9454,7 @@ domain Page
       ContentWebUSB
       ContentMediaSessionService
       ContentScreenReader
+      ContentDiscarded
 
       # See components/back_forward_cache/back_forward_cache_disable.h for explanations.
       EmbedderPopupBlockerTabHelper
```

## Roll protocol to r1344581 — _2024-08-21T04:28:14.000Z_
######  Diff: [`be47cf8...084b75c`](https://github.com/ChromeDevTools/devtools-protocol/compare/be47cf8...084b75c)

```diff
@@ browser_protocol.pdl:9453 @@ domain Page
       ContentWebUSB
       ContentMediaSessionService
       ContentScreenReader
-      ContentDiscarded
 
       # See components/back_forward_cache/back_forward_cache_disable.h for explanations.
       EmbedderPopupBlockerTabHelper
```

## Roll protocol to r1343927 — _2024-08-20T04:30:10.000Z_
######  Diff: [`24fc3ac...be47cf8`](https://github.com/ChromeDevTools/devtools-protocol/compare/24fc3ac...be47cf8)

```diff
@@ browser_protocol.pdl:9453 @@ domain Page
       ContentWebUSB
       ContentMediaSessionService
       ContentScreenReader
+      ContentDiscarded
 
       # See components/back_forward_cache/back_forward_cache_disable.h for explanations.
       EmbedderPopupBlockerTabHelper
```

## Roll protocol to r1342118 — _2024-08-15T04:27:44.000Z_
######  Diff: [`2a921f6...24fc3ac`](https://github.com/ChromeDevTools/devtools-protocol/compare/2a921f6...24fc3ac)

```diff
@@ browser_protocol.pdl:1151 @@ experimental domain Extensions
       string id
       # StorageArea to remove data from.
       StorageArea storageArea
+  # Sets `values` in extension storage in the given `storageArea`. The provided `values`
+  # will be merged with existing values in the storage area.
+  command setStorageItems
+    parameters
+      # ID of extension.
+      string id
+      # StorageArea to set data in.
+      StorageArea storageArea
+      # Values to set.
+      object values
 
 # Defines commands and events for Autofill.
 experimental domain Autofill
```

## Roll protocol to r1341448 — _2024-08-14T04:27:41.000Z_
######  Diff: [`175a971...2a921f6`](https://github.com/ChromeDevTools/devtools-protocol/compare/175a971...2a921f6)

```diff
@@ browser_protocol.pdl:1123 @@ experimental domain Extensions
     returns
       # Extension id.
       string id
-  # Gets data from extension storage in the given `area`. If `keys` is
+  # Gets data from extension storage in the given `storageArea`. If `keys` is
   # specified, these are used to filter the result.
   command getStorageItems
     parameters
@@ -1135,6 +1135,22 @@ experimental domain Extensions
       optional array of string keys
     returns
       object data
+  # Removes `keys` from extension storage in the given `storageArea`.
+  command removeStorageItems
+    parameters
+      # ID of extension.
+      string id
+      # StorageArea to remove data from.
+      StorageArea storageArea
+      # Keys to remove.
+      array of string keys
+  # Clears extension storage in the given `storageArea`.
+  command clearStorageItems
+    parameters
+      # ID of extension.
+      string id
+      # StorageArea to remove data from.
+      StorageArea storageArea
 
 # Defines commands and events for Autofill.
 experimental domain Autofill
```

## Roll protocol to r1340018 — _2024-08-10T04:28:25.000Z_
######  Diff: [`2b844ff...175a971`](https://github.com/ChromeDevTools/devtools-protocol/compare/2b844ff...175a971)

```diff
@@ browser_protocol.pdl:9512 @@ domain Page
       FrameId frameId
       # Frame's new url.
       string url
+      # Navigation type
+      enum navigationType
+        # Navigation due to fragment navigation.
+        fragment
+        # Navigation due to history API usage.
+        historyApi
+        # Navigation due to other reasons.
+        other
+
 
   # Compressed image data requested by the `startScreencast`.
   experimental event screencastFrame
```

## Roll protocol to r1339468 — _2024-08-09T04:27:55.000Z_
######  Diff: [`083e9e9...2b844ff`](https://github.com/ChromeDevTools/devtools-protocol/compare/083e9e9...2b844ff)

```diff
@@ browser_protocol.pdl:2780 @@ domain DOM
       optional CompatibilityMode compatibilityMode
       optional BackendNode assignedSlot
 
+  # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
+  type DetachedElementInfo extends object
+    properties
+      Node treeNode
+      array of NodeId retainedNodeIds
+
   # A structure holding an RGBA color.
   type RGBA extends object
     properties
@@ -3290,6 +3296,12 @@ domain DOM
     returns
       string path
 
+  # Returns list of detached nodes
+  experimental command getDetachedDomNodes
+    returns
+      # The list of detached nodes
+      array of DetachedElementInfo detachedNodes
+
   # Enables console to refer to the node with given id via $x (see Command Line API for more details
   # $x functions).
   experimental command setInspectedNode
```

## Roll protocol to r1338866 — _2024-08-08T04:29:00.000Z_
######  Diff: [`d5bb66e...083e9e9`](https://github.com/ChromeDevTools/devtools-protocol/compare/d5bb66e...083e9e9)

```diff
@@ browser_protocol.pdl:2660 @@ domain DOM
       first-line-inherited
       scroll-marker
       scroll-marker-group
+      scroll-next-button
+      scroll-prev-button
       scrollbar
       scrollbar-thumb
       scrollbar-button
```

## Roll protocol to r1338258 — _2024-08-07T04:28:16.000Z_
######  Diff: [`5b75e95...d5bb66e`](https://github.com/ChromeDevTools/devtools-protocol/compare/5b75e95...d5bb66e)

```diff
@@ browser_protocol.pdl:8369 @@ domain Page
 
   experimental type ClientNavigationReason extends string
     enum
+      anchorClick
       formSubmissionGet
       formSubmissionPost
       httpHeaderRefresh
-      scriptInitiated
+      initialFrameNavigation
       metaTagRefresh
+      other
       pageBlockInterstitial
       reload
-      anchorClick
+      scriptInitiated
 
   experimental type ClientNavigationDisposition extends string
     enum
```

## Roll protocol to r1337664 — _2024-08-06T04:28:23.000Z_
######  Diff: [`7daeda3...5b75e95`](https://github.com/ChromeDevTools/devtools-protocol/compare/7daeda3...5b75e95)

```diff
@@ browser_protocol.pdl:12612 @@ experimental domain PWA
       # supported yet.
       optional boolean linkCapturing
       optional DisplayMode displayMode
+
+# This domain allows configuring virtual Bluetooth devices to test
+# the web-bluetooth API.
+experimental domain BluetoothEmulation
+  # Indicates the various states of Central.
+  type CentralState extends string
+    enum
+      absent
+      powered-off
+      powered-on
+
+  # Stores the manufacturer data
+  type ManufacturerData extends object
+    properties
+      # Company identifier
+      # https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml
+      # https://usb.org/developers
+      integer key
+      # Manufacturer-specific data
+      binary data
+
+  # Stores the byte data of the advertisement packet sent by a Bluetooth device.
+  type ScanRecord extends object
+    properties
+      optional string name
+      optional array of string uuids
+      # Stores the external appearance description of the device.
+      optional integer appearance
+      # Stores the transmission power of a broadcasting device.
+      optional integer txPower
+      # Key is the company identifier and the value is an array of bytes of
+      # manufacturer specific data.
+      optional array of ManufacturerData manufacturerData
+
+  # Stores the advertisement packet information that is sent by a Bluetooth device.
+  type ScanEntry extends object
+    properties
+      string deviceAddress
+      integer rssi
+      ScanRecord scanRecord
+
+  # Enable the BluetoothEmulation domain.
+  command enable
+    parameters
+      # State of the simulated central.
+      CentralState state
+
+  # Disable the BluetoothEmulation domain.
+  command disable
+
+  # Simulates a peripheral with |address|, |name| and |knownServiceUuids|
+  # that has already been connected to the system.
+  command simulatePreconnectedPeripheral
+    parameters
+      string address
+      string name
+      array of ManufacturerData manufacturerData
+      array of string knownServiceUuids
+
+  # Simulates an advertisement packet described in |entry| being received by
+  # the central.
+  command simulateAdvertisement
+    parameters
+      ScanEntry entry
```

## Roll protocol to r1336433 — _2024-08-02T04:28:52.000Z_
######  Diff: [`62fe5c9...7daeda3`](https://github.com/ChromeDevTools/devtools-protocol/compare/62fe5c9...7daeda3)

```diff
@@ browser_protocol.pdl:2030 @@ experimental domain CSS
       # Associated style declaration.
       CSSStyle style
 
-  # CSS position-fallback rule representation.
-  deprecated type CSSPositionFallbackRule extends object
-    properties
-      Value name
-      # List of keyframes.
-      array of CSSTryRule tryRules
-
   # CSS @position-try rule representation.
   type CSSPositionTryRule extends object
     properties
@@ -2223,8 +2216,6 @@ experimental domain CSS
       optional array of InheritedPseudoElementMatches inheritedPseudoElements
       # A list of CSS keyframed animations matching this node.
       optional array of CSSKeyframesRule cssKeyframesRules
-      # A list of CSS position fallbacks matching this node.
-      deprecated optional array of CSSPositionFallbackRule cssPositionFallbackRules
       # A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property.
       optional array of CSSPositionTryRule cssPositionTryRules
       # Index of the active fallback in the applied position-try-fallback property,
```
