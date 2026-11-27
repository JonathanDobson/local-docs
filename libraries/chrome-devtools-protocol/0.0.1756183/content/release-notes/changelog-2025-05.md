# Chrome DevTools Protocol changelog — 2025-05

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-05, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1467305 — _2025-05-30T04:31:28.000Z_
######  Diff: [`8aaa683...c9a1a5d`](https://github.com/ChromeDevTools/devtools-protocol/compare/8aaa683...c9a1a5d)

```diff
@@ browser_protocol.pdl:3006 @@ domain DOM
       view-transition
       view-transition-group
       view-transition-image-pair
+      view-transition-group-children
       view-transition-old
       view-transition-new
       placeholder
```

## Roll protocol to r1466870 — _2025-05-29T04:34:46.000Z_
######  Diff: [`dc7b911...8aaa683`](https://github.com/ChromeDevTools/devtools-protocol/compare/dc7b911...8aaa683)

```diff
@@ browser_protocol.pdl:10838 @@ experimental domain Storage
       # Whether or not to set an entry for a key if that key is already present.
       # Present only for SharedStorageAccessMethod: set.
       optional boolean ignoreIfPresent
-      # If the method is called on a shared storage worklet, or as part of
-      # a shared storage worklet script, it will have a number for the
-      # associated worklet, denoting the (0-indexed) order of the worklet's
+      # A number denoting the (0-based) order of the worklet's
       # creation relative to all other shared storage worklets created by
       # documents using the current storage partition.
-      # Present only for SharedStorageAccessMethods: addModule, createWorklet,
-      # run, selectURL, and any other SharedStorageAccessMethod when the
-      # SharedStorageAccessScope is sharedStorageWorklet.
-      # TODO(crbug.com/401011862): Pass this only for addModule & createWorklet.
+      # Present only for SharedStorageAccessMethods: addModule, createWorklet.
       optional integer workletOrdinal
       # Hex representation of the DevTools token used as the TargetID for the
       # associated shared storage worklet.
@@ -12036,7 +12031,7 @@ domain Tracing
 
   type TraceConfig extends object
     properties
-      # Controls how the trace buffer stores data.
+      # Controls how the trace buffer stores data. The default is `recordUntilFull`.
       experimental optional enum recordMode
         recordUntilFull
         recordContinuously
```

## Roll protocol to r1465725 — _2025-05-27T04:31:56.000Z_
######  Diff: [`44a7afb...dc7b911`](https://github.com/ChromeDevTools/devtools-protocol/compare/44a7afb...dc7b911)

```diff
@@ browser_protocol.pdl:1634 @@ domain Browser
         inProgress
         completed
         canceled
+      # If download is "completed", provides the path of the downloaded file.
+      # Depending on the platform, it is not guaranteed to be set, nor the file
+      # is guaranteed to exist.
+      experimental optional string filePath
 
   # Close browser gracefully.
   command close
@@ -3008,6 +3012,7 @@ domain DOM
       file-selector-button
       details-content
       picker
+      permission-icon
 
   # Shadow root type.
   type ShadowRootType extends string
```

## Roll protocol to r1464554 — _2025-05-23T04:31:06.000Z_
######  Diff: [`e267f46...44a7afb`](https://github.com/ChromeDevTools/devtools-protocol/compare/e267f46...44a7afb)

```diff
@@ browser_protocol.pdl:3513 @@ domain DOM
         PopoverTarget
         # Get the interest target for a given element.
         InterestTarget
+        # Get the commandfor target for a given element. In this case, this given
+        # element can only be an HTMLButtonElement.
+        CommandFor
     returns
       # NodeId of the element matching the queried relation.
       NodeId nodeId
```

## Roll protocol to r1463868 — _2025-05-22T04:31:25.000Z_
######  Diff: [`13ce94b...e267f46`](https://github.com/ChromeDevTools/devtools-protocol/compare/13ce94b...e267f46)

```diff
@@ browser_protocol.pdl:10800 @@ experimental domain Storage
       # Name of the registered operation to be run.
       # Present only for SharedStorageAccessMethods: run and selectURL.
       optional string operationName
+      # ID of the operation call.
+      # Present only for SharedStorageAccessMethods: run and selectURL.
+      optional string operationId
       # Whether or not to keep the worket alive for future run or selectURL
       # calls.
       # Present only for SharedStorageAccessMethods: run and selectURL.
@@ -10827,12 +10830,22 @@ experimental domain Storage
       # Whether or not to set an entry for a key if that key is already present.
       # Present only for SharedStorageAccessMethod: set.
       optional boolean ignoreIfPresent
-      # If the method is called on a worklet, or as part of
-      # a worklet script, it will have an ID for the associated worklet.
+      # If the method is called on a shared storage worklet, or as part of
+      # a shared storage worklet script, it will have a number for the
+      # associated worklet, denoting the (0-indexed) order of the worklet's
+      # creation relative to all other shared storage worklets created by
+      # documents using the current storage partition.
+      # Present only for SharedStorageAccessMethods: addModule, createWorklet,
+      # run, selectURL, and any other SharedStorageAccessMethod when the
+      # SharedStorageAccessScope is sharedStorageWorklet.
+      # TODO(crbug.com/401011862): Pass this only for addModule & createWorklet.
+      optional integer workletOrdinal
+      # Hex representation of the DevTools token used as the TargetID for the
+      # associated shared storage worklet.
       # Present only for SharedStorageAccessMethods: addModule, createWorklet,
       # run, selectURL, and any other SharedStorageAccessMethod when the
-      # SharedStorageAccessScope is worklet.
-      optional string workletId
+      # SharedStorageAccessScope is sharedStorageWorklet.
+      optional Target.TargetID workletTargetId
       # Name of the lock to be acquired, if present.
       # Optionally present only for SharedStorageAccessMethods: batchUpdate,
       # set, append, delete, and clear.
@@ -11197,6 +11210,27 @@ experimental domain Storage
       # presence/absence depends on `type`.
       SharedStorageAccessParams params
 
+  # A shared storage run or selectURL operation finished its execution.
+  # The following parameters are included in all events.
+  event sharedStorageWorkletOperationExecutionFinished
+    parameters
+      # Time that the operation finished.
+      Network.TimeSinceEpoch finishedTime
+      # Time, in microseconds, from start of shared storage JS API call until
+      # end of operation execution in the worklet.
+      integer executionTime
+      # Enum value indicating the Shared Storage API method invoked.
+      SharedStorageAccessMethod method
+      # ID of the operation call.
+      string operationId
+      # Hex representation of the DevTools token used as the TargetID for the
+      # associated shared storage worklet.
+      Target.TargetID workletTargetId
+      # DevTools Frame Token for the primary frame tree's root.
+      Page.FrameId mainFrameId
+      # Serialization of the origin owning the Shared Storage data.
+      string ownerOrigin
+
   event storageBucketCreatedOrUpdated
     parameters
       StorageBucketInfo bucketInfo
```

## Roll protocol to r1462568 — _2025-05-20T04:31:10.000Z_
######  Diff: [`7193d4d...13ce94b`](https://github.com/ChromeDevTools/devtools-protocol/compare/7193d4d...13ce94b)

```diff
@@ browser_protocol.pdl:13667 @@ experimental domain BluetoothEmulation
   event descriptorOperationReceived
     parameters
       string descriptorId
-      CharacteristicOperationType type
+      DescriptorOperationType type
       optional binary data
```

## Roll protocol to r1461159 — _2025-05-16T04:31:23.000Z_
######  Diff: [`3716d55...6474ac4`](https://github.com/ChromeDevTools/devtools-protocol/compare/3716d55...6474ac4)

```diff
@@ browser_protocol.pdl:4744 @@ domain Emulation
       PressureSource source
       optional PressureMetadata metadata
 
+  # TODO: OBSOLETE: To remove when setPressureDataOverride is merged.
   # Provides a given pressure state that will be processed and eventually be
   # delivered to PressureObserver users. |source| must have been previously
   # overridden by setPressureSourceOverrideEnabled.
@@ -4752,6 +4753,15 @@ domain Emulation
       PressureSource source
       PressureState state
 
+  # Provides a given pressure data set that will be processed and eventually be
+  # delivered to PressureObserver users. |source| must have been previously
+  # overridden by setPressureSourceOverrideEnabled.
+  experimental command setPressureDataOverride
+    parameters
+      PressureSource source
+      PressureState state
+      optional number ownContributionEstimate
+
   # Overrides the Idle state.
   command setIdleOverride
     parameters
@@ -13050,7 +13060,6 @@ experimental domain Preload
       InvalidSchemeRedirect
       InvalidSchemeNavigation
       NavigationRequestBlockedByCsp
-      MainFrameNavigation
       MojoBinderPolicy
       RendererProcessCrashed
       RendererProcessKilled
```

## Roll protocol to r1460501 — _2025-05-15T04:31:15.000Z_
######  Diff: [`18bb399...3716d55`](https://github.com/ChromeDevTools/devtools-protocol/compare/18bb399...3716d55)

```diff
@@ browser_protocol.pdl:11250 @@ experimental domain Storage
       # duration in seconds
       array of integer ends
 
-  experimental type AttributionReportingTriggerSpec extends object
-    properties
-      # number instead of integer because not all uint32 can be represented by
-      # int
-      array of number triggerData
-      AttributionReportingEventReportWindows eventReportWindows
-
   experimental type AttributionReportingTriggerDataMatching extends string
     enum
       exact
@@ -11297,7 +11290,10 @@ experimental domain Storage
       Network.TimeSinceEpoch time
       # duration in seconds
       integer expiry
-      array of AttributionReportingTriggerSpec triggerSpecs
+      # number instead of integer because not all uint32 can be represented by
+      # int
+      array of number triggerData
+      AttributionReportingEventReportWindows eventReportWindows
       # duration in seconds
       integer aggregatableReportWindow
       AttributionReportingSourceType type
```

## Roll protocol to r1459876 — _2025-05-14T04:31:17.000Z_
######  Diff: [`3a3ebb4...18bb399`](https://github.com/ChromeDevTools/devtools-protocol/compare/3a3ebb4...18bb399)

```diff
@@ browser_protocol.pdl:5971 @@ domain Network
       Ping
       CSPViolationReport
       Preflight
+      FedCM
       Other
 
   # Unique loader identifier.
@@ -8607,6 +8608,7 @@ domain Page
       media-playback-while-not-visible
       microphone
       midi
+      on-device-speech-recognition
       otp-credentials
       payment
       picture-in-picture
```

## Roll protocol to r1457408 — _2025-05-08T04:31:17.000Z_
######  Diff: [`2edae2a...3a3ebb4`](https://github.com/ChromeDevTools/devtools-protocol/compare/2edae2a...3a3ebb4)

```diff
@@ browser_protocol.pdl:7959 @@ domain Network
       LoadNetworkResourcePageResult resource
 
   # Sets Controls for third-party cookie access
-  # Page reload is required before the new cookie bahavior will be observed
+  # Page reload is required before the new cookie behavior will be observed
   experimental command setCookieControls
     parameters
       # Whether 3pc restriction is enabled.
```

## Roll protocol to r1456738 — _2025-05-07T04:30:59.000Z_
######  Diff: [`3d03f3d...2edae2a`](https://github.com/ChromeDevTools/devtools-protocol/compare/3d03f3d...2edae2a)

```diff
@@ browser_protocol.pdl:6223 @@ domain Network
       mixed-content
       origin
       inspector
+      integrity
       subresource-filter
       content-type
       coep-frame-resource-needs-coep-header
```

## Roll protocol to r1456087 — _2025-05-06T04:30:50.000Z_
######  Diff: [`4925775...3d03f3d`](https://github.com/ChromeDevTools/devtools-protocol/compare/4925775...3d03f3d)

```diff
@@ browser_protocol.pdl:7018 @@ domain Network
       experimental optional integer maxResourceBufferSize
       # Longest post body size (in bytes) that would be included in requestWillBeSent notification
       optional integer maxPostDataSize
+      # Whether DirectSocket chunk send/receive events should be reported.
+      experimental optional boolean reportDirectSocketTraffic
 
   # Returns all browser cookies. Depending on the backend support, will return detailed cookie
   # information in the `cookies` field.
@@ -7549,18 +7551,80 @@ domain Network
       binary data
       MonotonicTime timestamp
 
-  # Fired when there is an error
-  # when writing to tcp direct socket stream.
-  # For example, if user writes illegal type like string
-  # instead of ArrayBuffer or ArrayBufferView.
-  # There's no reporting for reading, because
-  # we cannot know errors on the other side.
-  experimental event directTCPSocketChunkError
+  experimental type DirectUDPSocketOptions extends object
+    properties
+      optional string remoteAddr
+      # Unsigned int 16.
+      optional integer remotePort
+
+      optional string localAddr
+      # Unsigned int 16.
+      optional integer localPort
+
+      optional DirectSocketDnsQueryType dnsQueryType
+
+      # Expected to be unsigned integer.
+      optional number sendBufferSize
+      # Expected to be unsigned integer.
+      optional number receiveBufferSize
+
+
+  # Fired upon direct_socket.UDPSocket creation.
+  experimental event directUDPSocketCreated
+    parameters
+      RequestId identifier
+      DirectUDPSocketOptions options
+      MonotonicTime timestamp
+      optional Initiator initiator
+
+  # Fired when direct_socket.UDPSocket connection is opened.
+  experimental event directUDPSocketOpened
+    parameters
+      RequestId identifier
+      string localAddr
+      # Expected to be unsigned integer.
+      integer localPort
+      MonotonicTime timestamp
+      optional string remoteAddr
+      # Expected to be unsigned integer.
+      optional integer remotePort
+
+  # Fired when direct_socket.UDPSocket is aborted.
+  experimental event directUDPSocketAborted
     parameters
       RequestId identifier
       string errorMessage
       MonotonicTime timestamp
 
+  # Fired when direct_socket.UDPSocket is closed.
+  experimental event directUDPSocketClosed
+    parameters
+      RequestId identifier
+      MonotonicTime timestamp
+
+  experimental type DirectUDPMessage extends object
+    properties
+      binary data
+      # Null for connected mode.
+      optional string remoteAddr
+      # Null for connected mode.
+      # Expected to be unsigned integer.
+      optional integer remotePort
+
+  # Fired when message is sent to udp direct socket stream.
+  experimental event directUDPSocketChunkSent
+    parameters
+      RequestId identifier
+      DirectUDPMessage message
+      MonotonicTime timestamp
+
+  # Fired when message is received from udp direct socket stream.
+  experimental event directUDPSocketChunkReceived
+    parameters
+      RequestId identifier
+      DirectUDPMessage message
+      MonotonicTime timestamp
+
   experimental type PrivateNetworkRequestPolicy extends string
     enum
       Allow
```

## Roll protocol to r1454823 — _2025-05-02T04:30:38.000Z_
######  Diff: [`4fe3878...4925775`](https://github.com/ChromeDevTools/devtools-protocol/compare/4fe3878...4925775)

```diff
@@ browser_protocol.pdl:11380 @@ experimental domain Storage
       AttributionReportingEventLevelResult eventLevel
       AttributionReportingAggregatableResult aggregatable
 
+  experimental type AttributionReportingReportResult extends string
+    enum
+      # A network request was attempted for the report.
+      sent
+      # No request was attempted because of browser policy.
+      prohibited
+      # No request was attempted because of an error in report assembly,
+      # e.g. the aggregation service was unavailable.
+      failedToAssemble
+      # No request was attempted because the report's expiry passed.
+      expired
+
+  experimental event attributionReportingReportSent
+    parameters
+      string url
+      object body
+      AttributionReportingReportResult result
+      # If result is `sent`, populated with net/HTTP status.
+      optional integer netError
+      optional string netErrorName
+      optional integer httpStatusCode
+
   # A single Related Website Set object.
   experimental type RelatedWebsiteSet extends object
     properties
@@ -13385,6 +13407,12 @@ experimental domain BluetoothEmulation
       subscribe-to-notifications
       unsubscribe-from-notifications
 
+  # Indicates the various types of descriptor operation.
+  type DescriptorOperationType extends string
+    enum
+      read
+      write
+
   # Stores the manufacturer data
   type ManufacturerData extends object
     properties
@@ -13481,6 +13509,18 @@ experimental domain BluetoothEmulation
       integer code
       optional binary data
 
+  # Simulates the response from the descriptor with |descriptorId| for a
+  # descriptor operation of |type|. The |code| value follows the Error
+  # Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
+  # The |data| is expected to exist when simulating a successful read operation
+  # response.
+  command simulateDescriptorOperationResponse
+    parameters
+      string descriptorId
+      DescriptorOperationType type
+      integer code
+      optional binary data
+
   # Adds a service with |serviceUuid| to the peripheral with |address|.
   command addService
     parameters
@@ -13527,6 +13567,11 @@ experimental domain BluetoothEmulation
     parameters
       string descriptorId
 
+  # Simulates a GATT disconnection from the peripheral with |address|.
+  command simulateGATTDisconnection
+    parameters
+      string address
+
   # Event for when a GATT operation of |type| to the peripheral with |address|
   # happened.
   event gattOperationReceived
@@ -13543,3 +13588,12 @@ experimental domain BluetoothEmulation
       CharacteristicOperationType type
       optional binary data
       optional CharacteristicWriteType writeType
+
+  # Event for when a descriptor operation of |type| to the descriptor
+  # respresented by |descriptorId| happened. |data| is expected to exist when
+  # |type| is write.
+  event descriptorOperationReceived
+    parameters
+      string descriptorId
+      CharacteristicOperationType type
+      optional binary data
```
