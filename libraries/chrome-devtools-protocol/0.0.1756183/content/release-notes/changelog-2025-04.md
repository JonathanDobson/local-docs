# Chrome DevTools Protocol changelog — 2025-04

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-04, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1453708 — _2025-04-30T04:30:29.000Z_
######  Diff: [`3d50984...4fe3878`](https://github.com/ChromeDevTools/devtools-protocol/compare/3d50984...4fe3878)

```diff
@@ browser_protocol.pdl:1079 @@ experimental domain Audits
       # The value of the property rule property that failed to parse
       optional string propertyValue
 
+  type UserReidentificationIssueType extends string
+    enum
+      BlockedFrameNavigation
+      BlockedSubresource
+
+  # This issue warns about uses of APIs that may be considered misuse to
+  # re-identify users.
+  type UserReidentificationIssueDetails extends object
+    properties
+      UserReidentificationIssueType type
+      # Applies to BlockedFrameNavigation and BlockedSubresource issue types.
+      optional AffectedRequest request
+
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
   # information about the kind of issue.
@@ -1109,6 +1122,7 @@ experimental domain Audits
       SharedDictionaryIssue
       SelectElementAccessibilityIssue
       SRIMessageSignatureIssue
+      UserReidentificationIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -1139,6 +1153,7 @@ experimental domain Audits
       optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
       optional SelectElementAccessibilityIssueDetails selectElementAccessibilityIssueDetails
       optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
+      optional UserReidentificationIssueDetails userReidentificationIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
```

## Roll protocol to r1453071 — _2025-04-29T04:30:14.000Z_
######  Diff: [`63aa321...3d50984`](https://github.com/ChromeDevTools/devtools-protocol/compare/63aa321...3d50984)

```diff
@@ browser_protocol.pdl:8455 @@ domain Page
 
   # All Permissions Policy features. This enum should match the one defined
   # in services/network/public/cpp/permissions_policy/permissions_policy_features.json5.
+  # LINT.IfChange(PermissionsPolicyFeature)
   experimental type PermissionsPolicyFeature extends string
     enum
       accelerometer
@@ -8521,6 +8522,7 @@ domain Page
       keyboard-map
       language-detector
       local-fonts
+      local-network-access
       magnetometer
       media-playback-while-not-visible
       microphone
@@ -8534,6 +8536,7 @@ domain Page
       private-state-token-redemption
       publickey-credentials-create
       publickey-credentials-get
+      record-ad-auction-events
       rewriter
       run-ad-auction
       screen-wake-lock
@@ -8558,6 +8561,7 @@ domain Page
       window-management
       writer
       xr-spatial-tracking
+  # LINT.ThenChange(//services/network/public/cpp/permissions_policy/permissions_policy_features.json5:PermissionsPolicy)
 
   # Reason for a permissions policy feature to be disabled.
   experimental type PermissionsPolicyBlockReason extends string
@@ -13351,6 +13355,21 @@ experimental domain BluetoothEmulation
       connection
       discovery
 
+  # Indicates the various types of characteristic write.
+  type CharacteristicWriteType extends string
+    enum
+      write-default-deprecated
+      write-with-response
+      write-without-response
+
+  # Indicates the various types of characteristic operation.
+  type CharacteristicOperationType extends string
+    enum
+      read
+      write
+      subscribe-to-notifications
+      unsubscribe-from-notifications
+
   # Stores the manufacturer data
   type ManufacturerData extends object
     properties
@@ -13435,6 +13454,18 @@ experimental domain BluetoothEmulation
       GATTOperationType type
       integer code
 
+  # Simulates the response from the characteristic with |characteristicId| for a
+  # characteristic operation of |type|. The |code| value follows the Error
+  # Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
+  # The |data| is expected to exist when simulating a successful read operation
+  # response.
+  command simulateCharacteristicOperationResponse
+    parameters
+      string characteristicId
+      CharacteristicOperationType type
+      integer code
+      optional binary data
+
   # Adds a service with |serviceUuid| to the peripheral with |address|.
   command addService
     parameters
@@ -13487,3 +13518,13 @@ experimental domain BluetoothEmulation
     parameters
       string address
       GATTOperationType type
+
+  # Event for when a characteristic operation of |type| to the characteristic
+  # respresented by |characteristicId| happened. |data| and |writeType| is
+  # expected to exist when |type| is write.
+  event characteristicOperationReceived
+    parameters
+      string characteristicId
+      CharacteristicOperationType type
+      optional binary data
+      optional CharacteristicWriteType writeType
```

## Roll protocol to r1452169 — _2025-04-26T04:29:56.000Z_
######  Diff: [`22067e8...63aa321`](https://github.com/ChromeDevTools/devtools-protocol/compare/22067e8...63aa321)

```diff
@@ js_protocol.pdl:649 @@ domain Debugger
       Runtime.ExecutionContextId executionContextId
       # Content hash of the script, SHA-256.
       string hash
-      # For Wasm modules, the content of the `build_id` custom section.
+      # For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment.
       string buildId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object executionContextAuxData
@@ -690,7 +690,7 @@ domain Debugger
       Runtime.ExecutionContextId executionContextId
       # Content hash of the script, SHA-256.
       string hash
-      # For Wasm modules, the content of the `build_id` custom section.
+      # For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment.
       string buildId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object executionContextAuxData
```

## Roll protocol to r1451615 — _2025-04-25T04:30:43.000Z_
######  Diff: [`376b7a3...22067e8`](https://github.com/ChromeDevTools/devtools-protocol/compare/376b7a3...22067e8)

```diff
@@ browser_protocol.pdl:9186 @@ domain Page
       # Recommendation for manifest's id attribute to match current id computed from start_url
       optional string recommendedId
 
-  experimental command getAdScriptId
+  experimental command getAdScriptAncestryIds
     parameters
       FrameId frameId
     returns
-      # Identifies the bottom-most script which caused the frame to be labelled
-      # as an ad. Only sent if frame is labelled as an ad and id is available.
-      optional AdScriptId adScriptId
+      # The ancestry chain of ad script identifiers leading to this frame's
+      # creation, ordered from the most immediate script (in the frame creation
+      # stack) to more distant ancestors (that created the immediately preceding
+      # script). Only sent if frame is labelled as an ad and ids are available.
+      array of AdScriptId adScriptAncestryIds
 
   # Returns present frame tree structure.
   command getFrameTree
@@ -9804,6 +9806,8 @@ domain Page
   # closed.
   event javascriptDialogClosed
     parameters
+      # Frame id.
+      experimental FrameId frameId
       # Whether dialog was confirmed.
       boolean result
       # User input in case of prompt.
@@ -9815,6 +9819,8 @@ domain Page
     parameters
       # Frame url.
       string url
+      # Frame id.
+      experimental FrameId frameId
       # Message that will be displayed by the dialog.
       string message
       # Dialog type.
```

## Roll protocol to r1450379 — _2025-04-23T04:30:35.000Z_
######  Diff: [`ecbd284...376b7a3`](https://github.com/ChromeDevTools/devtools-protocol/compare/ecbd284...376b7a3)

```diff
@@ browser_protocol.pdl:10656 @@ experimental domain Storage
       # storage.
       integer bytesUsed
 
+  # Represents a dictionary object passed in as privateAggregationConfig to
+  # run or selectURL.
+  type SharedStoragePrivateAggregationConfig extends object
+    properties
+      # The chosen aggregation service deployment.
+      optional string aggregationCoordinatorOrigin
+      # The context ID provided.
+      optional string contextId
+      # Configures the maximum size allowed for filtering IDs.
+      integer filteringIdMaxBytes
+      # The limit on the number of contributions in the final report.
+      optional integer maxContributions
+
   # Pair of reporting metadata details for a candidate URL for `selectURL()`.
   type SharedStorageReportingMetadata extends object
     properties
@@ -10675,44 +10688,61 @@ experimental domain Storage
   type SharedStorageAccessParams extends object
     properties
       # Spec of the module script URL.
-      # Present only for SharedStorageAccessType.documentAddModule.
+      # Present only for SharedStorageAccessMethods: addModule and
+      # createWorklet.
       optional string scriptSourceUrl
+      # String denoting "context-origin", "script-origin", or a custom
+      # origin to be used as the worklet's data origin.
+      # Present only for SharedStorageAccessMethod: createWorklet.
+      optional string dataOrigin
       # Name of the registered operation to be run.
-      # Present only for SharedStorageAccessType.documentRun and
-      # SharedStorageAccessType.documentSelectURL.
+      # Present only for SharedStorageAccessMethods: run and selectURL.
       optional string operationName
+      # Whether or not to keep the worket alive for future run or selectURL
+      # calls.
+      # Present only for SharedStorageAccessMethods: run and selectURL.
+      optional boolean keepAlive
+      # Configures the private aggregation options.
+      # Present only for SharedStorageAccessMethods: run and selectURL.
+      optional SharedStoragePrivateAggregationConfig privateAggregationConfig
       # The operation's serialized data in bytes (converted to a string).
-      # Present only for SharedStorageAccessType.documentRun and
-      # SharedStorageAccessType.documentSelectURL.
+      # Present only for SharedStorageAccessMethods: run and selectURL.
+      # TODO(crbug.com/401011862): Consider updating this parameter to binary.
       optional string serializedData
       # Array of candidate URLs' specs, along with any associated metadata.
-      # Present only for SharedStorageAccessType.documentSelectURL.
+      # Present only for SharedStorageAccessMethod: selectURL.
       optional array of SharedStorageUrlWithMetadata urlsWithMetadata
+      # Spec of the URN:UUID generated for a selectURL call.
+      # Present only for SharedStorageAccessMethod: selectURL.
+      optional string urnUuid
       # Key for a specific entry in an origin's shared storage.
-      # Present only for SharedStorageAccessType.documentSet,
-      # SharedStorageAccessType.documentAppend,
-      # SharedStorageAccessType.documentDelete,
-      # SharedStorageAccessType.workletSet,
-      # SharedStorageAccessType.workletAppend,
-      # SharedStorageAccessType.workletDelete,
-      # SharedStorageAccessType.workletGet,
-      # SharedStorageAccessType.headerSet,
-      # SharedStorageAccessType.headerAppend, and
-      # SharedStorageAccessType.headerDelete.
+      # Present only for SharedStorageAccessMethods: set, append, delete, and
+      # get.
       optional string key
       # Value for a specific entry in an origin's shared storage.
-      # Present only for SharedStorageAccessType.documentSet,
-      # SharedStorageAccessType.documentAppend,
-      # SharedStorageAccessType.workletSet,
-      # SharedStorageAccessType.workletAppend,
-      # SharedStorageAccessType.headerSet, and
-      # SharedStorageAccessType.headerAppend.
+      # Present only for SharedStorageAccessMethods: set and append.
       optional string value
       # Whether or not to set an entry for a key if that key is already present.
-      # Present only for SharedStorageAccessType.documentSet,
-      # SharedStorageAccessType.workletSet, and
-      # SharedStorageAccessType.headerSet.
+      # Present only for SharedStorageAccessMethod: set.
       optional boolean ignoreIfPresent
+      # If the method is called on a worklet, or as part of
+      # a worklet script, it will have an ID for the associated worklet.
+      # Present only for SharedStorageAccessMethods: addModule, createWorklet,
+      # run, selectURL, and any other SharedStorageAccessMethod when the
+      # SharedStorageAccessScope is worklet.
+      optional string workletId
+      # Name of the lock to be acquired, if present.
+      # Optionally present only for SharedStorageAccessMethods: batchUpdate,
+      # set, append, delete, and clear.
+      optional string withLock
+      # If the method has been called as part of a batchUpdate, then this
+      # number identifies the batch to which it belongs.
+      # Optionally present only for SharedStorageAccessMethods:
+      # batchUpdate (required), set, append, delete, and clear.
+      optional string batchUpdateId
+      # Number of modifier methods sent in batch.
+      # Present only for SharedStorageAccessMethod: batchUpdate.
+      optional integer batchSize
 
   type StorageBucketsDurability extends string
     enum
@@ -11193,6 +11223,8 @@ experimental domain Storage
       optional AttributionScopesData scopesData
       integer maxEventLevelReports
       array of AttributionReportingNamedBudgetDef namedBudgets
+      boolean debugReporting
+      number eventLevelEpsilon
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
```

## Roll protocol to r1449749 — _2025-04-22T04:30:50.000Z_
######  Diff: [`d4fc663...ecbd284`](https://github.com/ChromeDevTools/devtools-protocol/compare/d4fc663...ecbd284)

```diff
@@ browser_protocol.pdl:11165 @@ experimental domain Storage
       number limit
       number maxEventStates
 
+  experimental type AttributionReportingNamedBudgetDef extends object
+    properties
+      string name
+      integer budget
+
   experimental type AttributionReportingSourceRegistration extends object
     properties
       Network.TimeSinceEpoch time
@@ -11187,6 +11192,7 @@ experimental domain Storage
       AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
       optional AttributionScopesData scopesData
       integer maxEventLevelReports
+      array of AttributionReportingNamedBudgetDef namedBudgets
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
@@ -11249,6 +11255,11 @@ experimental domain Storage
       optional UnsignedInt64AsBase10 dedupKey
       AttributionReportingFilterPair filters
 
+  experimental type AttributionReportingNamedBudgetCandidate extends object
+    properties
+      optional string name
+      AttributionReportingFilterPair filters
+
   experimental type AttributionReportingTriggerRegistration extends object
     properties
       AttributionReportingFilterPair filters
@@ -11264,6 +11275,7 @@ experimental domain Storage
       optional string triggerContextId
       AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
       array of string scopes
+      array of AttributionReportingNamedBudgetCandidate namedBudgets
 
   experimental type AttributionReportingEventLevelResult extends string
     enum
```

## Roll protocol to r1449119 — _2025-04-19T04:29:57.000Z_
######  Diff: [`a38625f...d4fc663`](https://github.com/ChromeDevTools/devtools-protocol/compare/a38625f...d4fc663)

```diff
@@ browser_protocol.pdl:4854 @@ domain Emulation
       # Whether the override should be enabled.
       boolean enabled
 
+  # Allows overriding the difference between the small and large viewport sizes, which determine the
+  # value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.
+  experimental command setSmallViewportHeightDifferenceOverride
+    parameters
+      # This will cause an element of size 100svh to be `difference` pixels smaller than an element
+      # of size 100lvh.
+      integer difference
+
 # This domain provides experimental commands only supported in headless mode.
 experimental domain HeadlessExperimental
   depends on Page
@@ -9977,7 +9985,8 @@ domain Page
       RequestedByWebViewClient
       PostMessageByWebViewClient
       CacheControlNoStoreDeviceBoundSessionTerminated
-      CacheLimitPruned
+      CacheLimitPrunedOnModerateMemoryPressure
+      CacheLimitPrunedOnCriticalMemoryPressure
 
   # Types of not restored reasons for back-forward cache.
   experimental type BackForwardCacheNotRestoredReasonType extends string
```

## Roll protocol to r1448144 — _2025-04-17T04:30:33.000Z_
######  Diff: [`82e761e...a38625f`](https://github.com/ChromeDevTools/devtools-protocol/compare/82e761e...a38625f)

```diff
@@ browser_protocol.pdl:11333 @@ experimental domain Storage
       # party URL, only the first-party URL is returned in the array.
       array of string matchedUrls
 
+  command setProtectedAudienceKAnonymity
+    parameters
+      string owner
+      string name
+      array of binary hashes
+
 # The SystemInfo domain defines methods and events for querying low-level system information.
 experimental domain SystemInfo
```

## Roll protocol to r1447524 — _2025-04-16T04:30:24.000Z_
######  Diff: [`4526a56...82e761e`](https://github.com/ChromeDevTools/devtools-protocol/compare/4526a56...82e761e)

```diff
@@ browser_protocol.pdl:7512 @@ domain Network
       RequestId identifier
       MonotonicTime timestamp
 
+  # Fired when data is sent to tcp direct socket stream.
+  experimental event directTCPSocketChunkSent
+    parameters
+      RequestId identifier
+      binary data
+      MonotonicTime timestamp
+
+  # Fired when data is received from tcp direct socket stream.
+  experimental event directTCPSocketChunkReceived
+    parameters
+      RequestId identifier
+      binary data
+      MonotonicTime timestamp
+
+  # Fired when there is an error
+  # when writing to tcp direct socket stream.
+  # For example, if user writes illegal type like string
+  # instead of ArrayBuffer or ArrayBufferView.
+  # There's no reporting for reading, because
+  # we cannot know errors on the other side.
+  experimental event directTCPSocketChunkError
+    parameters
+      RequestId identifier
+      string errorMessage
+      MonotonicTime timestamp
+
   experimental type PrivateNetworkRequestPolicy extends string
     enum
       Allow
```

## Roll protocol to r1446921 — _2025-04-15T04:30:37.000Z_
######  Diff: [`dae4579...4526a56`](https://github.com/ChromeDevTools/devtools-protocol/compare/dae4579...4526a56)

```diff
@@ browser_protocol.pdl:4676 @@ domain Emulation
         protanopia
         tritanopia
 
-  # Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
-  # unavailable.
+  # Overrides the Geolocation Position or Error. Omitting latitude, longitude or
+  # accuracy emulates position unavailable.
   command setGeolocationOverride
     parameters
       # Mock latitude
@@ -4686,6 +4686,14 @@ domain Emulation
       optional number longitude
       # Mock accuracy
       optional number accuracy
+      # Mock altitude
+      optional number altitude
+      # Mock altitudeAccuracy
+      optional number altitudeAccuracy
+      # Mock heading
+      optional number heading
+      # Mock speed
+      optional number speed
 
   experimental command getOverriddenSensorInformation
     parameters
```

## Roll protocol to r1445099 — _2025-04-10T04:30:17.000Z_
######  Diff: [`a4ea2da...dae4579`](https://github.com/ChromeDevTools/devtools-protocol/compare/a4ea2da...dae4579)

```diff
@@ browser_protocol.pdl:1537 @@ domain Browser
     enum
       openTabSearch
       closeTabSearch
+      openGlic
 
   # Set permission settings for given origin.
   experimental command setPermission
@@ -6333,6 +6334,7 @@ domain Network
       cache
       fetch-event
       race-network-and-fetch-handler
+      race-network-and-cache
 
   experimental type ServiceWorkerRouterInfo extends object
     properties
```

## Roll protocol to r1443917 — _2025-04-08T04:30:16.000Z_
######  Diff: [`cbcb4a1...a4ea2da`](https://github.com/ChromeDevTools/devtools-protocol/compare/cbcb4a1...a4ea2da)

```diff
@@ browser_protocol.pdl:8453 @@ domain Page
       cross-origin-isolated
       deferred-fetch
       deferred-fetch-minimal
+      device-attributes
       digital-credentials-get
       direct-sockets
       direct-sockets-private
@@ -11642,11 +11643,14 @@ domain Target
       # Deprecated.
       deprecated optional TargetID targetId
 
-  # Controls whether to automatically attach to new targets which are considered to be related to
-  # this one. When turned on, attaches to all existing related targets as well. When turned off,
+  # Controls whether to automatically attach to new targets which are considered
+  # to be directly related to this one (for example, iframes or workers).
+  # When turned on, attaches to all existing related targets as well. When turned off,
   # automatically detaches from all currently attached targets.
   # This also clears all targets added by `autoAttachRelated` from the list of targets to watch
   # for creation of related targets.
+  # You might want to call this recursively for auto-attached targets to attach
+  # to all available targets.
   command setAutoAttach
     parameters
       # Whether to auto-attach to related targets.
```

## Roll protocol to r1443047 — _2025-04-05T04:29:44.000Z_
######  Diff: [`280d28f...cbcb4a1`](https://github.com/ChromeDevTools/devtools-protocol/compare/280d28f...cbcb4a1)

```diff
@@ browser_protocol.pdl:13339 @@ experimental domain BluetoothEmulation
       # An identifier that uniquely represents this service.
       string serviceId
 
-  # Removes the service respresented by |serviceId| from the peripheral with
-  # |address|.
+  # Removes the service respresented by |serviceId| from the simulated central.
   command removeService
     parameters
-      string address
       string serviceId
 
   # Adds a characteristic with |characteristicUuid| and |properties| to the
-  # service represented by |serviceId| in the peripheral with |address|.
+  # service represented by |serviceId|.
   command addCharacteristic
     parameters
-      string address
       string serviceId
       string characteristicUuid
       CharacteristicProperties properties
@@ -13359,34 +13356,24 @@ experimental domain BluetoothEmulation
       string characteristicId
 
   # Removes the characteristic respresented by |characteristicId| from the
-  # service respresented by |serviceId| in the peripheral with |address|.
+  # simulated central.
   command removeCharacteristic
     parameters
-      string address
-      string serviceId
       string characteristicId
 
   # Adds a descriptor with |descriptorUuid| to the characteristic respresented
-  # by |characteristicId| in the service represented by |serviceId| of the
-  # peripheral with |address|.
+  # by |characteristicId|.
   command addDescriptor
     parameters
-      string address
-      string serviceId
       string characteristicId
       string descriptorUuid
     returns
       # An identifier that uniquely represents this descriptor.
       string descriptorId
 
-  # Removes the descriptor with |descriptorId| from the characteristic
-  # respresented by |characteristicId| in the service represented by |serviceId|
-  # of the peripheral with |address|.
+  # Removes the descriptor with |descriptorId| from the simulated central.
   command removeDescriptor
     parameters
-      string address
-      string serviceId
-      string characteristicId
       string descriptorId
 
   # Event for when a GATT operation of |type| to the peripheral with |address|
```

## Roll protocol to r1441961 — _2025-04-03T04:31:08.000Z_
######  Diff: [`52a677b...280d28f`](https://github.com/ChromeDevTools/devtools-protocol/compare/52a677b...280d28f)

```diff
@@ browser_protocol.pdl:11591 @@ domain Target
       optional boolean background
       # Whether to create the target of type "tab".
       experimental optional boolean forTab
+      # Whether to create a hidden target. The hidden target is observable via protocol, but not
+      # present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or
+      # `background: false`. The life-time of the tab is limited to the life-time of the session.
+      experimental optional boolean hidden
     returns
       # The id of the page opened.
       TargetID targetId
```

## Roll protocol to r1441344 — _2025-04-02T04:30:43.000Z_
######  Diff: [`fc91db8...52a677b`](https://github.com/ChromeDevTools/devtools-protocol/compare/fc91db8...52a677b)

```diff
@@ browser_protocol.pdl:983 @@ experimental domain Audits
       TypeNotMatching
       UiDismissedNoEmbargo
       CorsError
+      SuppressedBySegmentationPlatform
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
@@ -2436,7 +2437,12 @@ experimental domain CSS
   # For example, a value of '1em' is evaluated according to the computed
   # 'font-size' of the element and a value 'calc(1px + 2px)' will be
   # resolved to '3px'.
-  command resolveValues
+  # If the `propertyName` was specified the `values` are resolved as if
+  # they were property's declaration. If a value cannot be parsed according
+  # to the provided property syntax, the value is parsed using combined
+  # syntax as if null `propertyName` was provided. If the value cannot be
+  # resolved even then, return the provided value without any changes.
+  experimental command resolveValues
     parameters
       # Substitution functions (var()/env()/attr()) and cascade-dependent
       # keywords (revert/revert-layer) do not work.
@@ -2447,9 +2453,9 @@ experimental domain CSS
       optional string propertyName
       # Pseudo element type, only works for pseudo elements that generate
       # elements in the tree, such as ::before and ::after.
-      experimental optional DOM.PseudoType pseudoType
+      optional DOM.PseudoType pseudoType
       # Pseudo element custom ident.
-      experimental optional string pseudoIdentifier
+      optional string pseudoIdentifier
     returns
       array of string results
 
@@ -13356,6 +13362,29 @@ experimental domain BluetoothEmulation
       string serviceId
       string characteristicId
 
+  # Adds a descriptor with |descriptorUuid| to the characteristic respresented
+  # by |characteristicId| in the service represented by |serviceId| of the
+  # peripheral with |address|.
+  command addDescriptor
+    parameters
+      string address
+      string serviceId
+      string characteristicId
+      string descriptorUuid
+    returns
+      # An identifier that uniquely represents this descriptor.
+      string descriptorId
+
+  # Removes the descriptor with |descriptorId| from the characteristic
+  # respresented by |characteristicId| in the service represented by |serviceId|
+  # of the peripheral with |address|.
+  command removeDescriptor
+    parameters
+      string address
+      string serviceId
+      string characteristicId
+      string descriptorId
+
   # Event for when a GATT operation of |type| to the peripheral with |address|
   # happened.
   event gattOperationReceived
```
