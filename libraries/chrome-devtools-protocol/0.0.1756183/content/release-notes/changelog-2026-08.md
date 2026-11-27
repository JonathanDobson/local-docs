# Chrome DevTools Protocol changelog — 2026-08

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-08, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1687809 — _2026-08-28T07:01:23.000Z_
######  Diff: [`0fb57f9...ea39a11`](https://github.com/ChromeDevTools/devtools-protocol/compare/0fb57f9...ea39a11)

```diff
@@ domains/WebAuthn.pdl:106 @@ experimental domain WebAuthn
       # If -1, the credential won't have an associated signature counter, and
       # every assertion operation will report a value of 0.
       # See https://w3c.github.io/webauthn/#signature-counter
-      integer signCount
+      number signCount
       # The large blob associated with the credential.
       # See https://w3c.github.io/webauthn/#sctn-large-blob-extension
       optional binary largeBlob
@@ -233,7 +233,7 @@ experimental domain WebAuthn
       # If -1, the signature counter is removed from the credential, and every
       # assertion operation will report a value of 0.
       # See https://w3c.github.io/webauthn/#signature-counter
-      optional integer signCount
+      optional number signCount
 
   # Triggered when a credential is added to an authenticator.
   event credentialAdded
```

## Roll protocol to r1686980 — _2026-08-27T06:39:03.000Z_
######  Diff: [`5ee78b3...0fb57f9`](https://github.com/ChromeDevTools/devtools-protocol/compare/5ee78b3...0fb57f9)

```diff
@@ domains/Browser.pdl:225 @@ domain Browser
       # Commandline parameters
       array of string arguments
 
+  # Adds or updates a mock camera in the shared video capture device list for
+  # test automation. The mock camera is not scoped to a particular page or
+  # frame and is removed when the DevTools session that created it disconnects.
+  experimental command addMockCamera
+    parameters
+      # Required non-empty identifier for the mock camera. This is mapped to an
+      # internal virtual-device identifier and is not the MediaDeviceInfo.deviceId
+      # exposed to the page.
+      string deviceId
+
   # Chrome histogram bucket.
   experimental type Bucket extends object
     properties
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 0961300c..a2d197c5 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -127,6 +127,7 @@ domain Page
       gamepad
       geolocation
       gyroscope
+      haptics
       hid
       identity-credentials-get
       idle-detection
```

## Roll protocol to r1684464 — _2026-08-22T04:37:33.000Z_
######  Diff: [`a12defa...5ee78b3`](https://github.com/ChromeDevTools/devtools-protocol/compare/a12defa...5ee78b3)

```diff
@@ domains/ServiceWorker.pdl:32 @@ experimental domain ServiceWorker
       activated
       redundant
 
+  # Mostly corresponds to `RouterCondition` in ServiceWorker spec
+  # (https://www.w3.org/TR/service-workers/#dictdef-routercondition) while this
+  # currently lacks support for the nested conditions ("or" and "not").
+  # TODO(crbug.com/540469610): Support recursive conditions.
+  type ServiceWorkerRouterCondition extends object
+    properties
+      # Plain text, or JSON serialization of URLPatternInit or URLPattern
+      optional string urlPattern
+      optional string requestMethod
+      optional string requestMode
+      optional string requestDestination
+      optional ServiceWorkerVersionRunningStatus runningStatus
+
+  type ServiceWorkerRouterSourceType extends string
+    enum
+      # https://www.w3.org/TR/service-workers/#enumdef-routersourceenum
+      cache
+      fetchEvent
+      network
+      raceNetworkAndFetchHandler
+      raceNetworkAndCache
+      # Tag for https://www.w3.org/TR/service-workers/#dictdef-routersourcedict
+      sourceDict
+
+  # https://www.w3.org/TR/service-workers/#dictdef-routersourcedict
+  type ServiceWorkerRouterSourceDict extends object
+    properties
+      string cacheName
+
+  # Corresponds to `RouterSource` in the spec while the representation is different as follows.
+  # (https://www.w3.org/TR/service-workers/#typedefdef-routersource)
+  # - `RouterSourceEnum`: `type` equals `cache`, `sourceDict` is null.
+  # - `RouterSourceDict`: `type` equals `sourceDict`, `sourceDict` has valid value.
+  type ServiceWorkerRouterSource extends object
+    properties
+      ServiceWorkerRouterSourceType type
+      # Non-empty iff `type` equals "sourceDict".
+      optional ServiceWorkerRouterSourceDict sourceDict
+
+  type ServiceWorkerRouterRule extends object
+    properties
+      ServiceWorkerRouterCondition condition
+      ServiceWorkerRouterSource source
+      # Rule ID assigned by the browser. Unique within each ServiceWorkerVersion.
+      integer id
+
   # ServiceWorker version.
   type ServiceWorkerVersion extends object
     properties
@@ -47,7 +93,11 @@ experimental domain ServiceWorker
       optional number scriptResponseTime
       optional array of Target.TargetID controlledClients
       optional Target.TargetID targetId
+      # Migration to `typedRouterRules` is in progress. The browser sends either
+      # `routerRules` or `typedRouterRules`.
+      # TODO(crbug.com/540469610): Remove `routerRules` after the migration.
       optional string routerRules
+      optional array of ServiceWorkerRouterRule typedRouterRules
 
   # ServiceWorker error message.
   type ServiceWorkerErrorMessage extends object
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index addcbb35..c741899e 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -21,7 +21,6 @@ experimental domain Storage
       websql
       service_workers
       cache_storage
-      shared_storage
       storage_buckets
       all
       other
@@ -42,147 +41,6 @@ experimental domain Storage
       number count
 
 
-  # Enum of shared storage access scopes.
-  type SharedStorageAccessScope extends string
-    enum
-      window
-      sharedStorageWorklet
-      header
-
-  # Enum of shared storage access methods.
-  type SharedStorageAccessMethod extends string
-    enum
-      addModule
-      createWorklet
-      selectURL
-      run
-      batchUpdate
-      set
-      append
-      delete
-      clear
-      get
-      keys
-      values
-      entries
-      length
-      remainingBudget
-
-  # Struct for a single key-value pair in an origin's shared storage.
-  type SharedStorageEntry extends object
-    properties
-      string key
-      string value
-
-  # Details for an origin's shared storage.
-  type SharedStorageMetadata extends object
-    properties
-      # Time when the origin's shared storage was last created.
-      Network.TimeSinceEpoch creationTime
-      # Number of key-value pairs stored in origin's shared storage.
-      integer length
-      # Current amount of bits of entropy remaining in the navigation budget.
-      number remainingBudget
-      # Total number of bytes stored as key-value pairs in origin's shared
-      # storage.
-      integer bytesUsed
-
-  # Represents a dictionary object passed in as privateAggregationConfig to
-  # run or selectURL.
-  type SharedStoragePrivateAggregationConfig extends object
-    properties
-      # The chosen aggregation service deployment.
-      optional string aggregationCoordinatorOrigin
-      # The context ID provided.
-      optional string contextId
-      # Configures the maximum size allowed for filtering IDs.
-      integer filteringIdMaxBytes
-      # The limit on the number of contributions in the final report.
-      optional integer maxContributions
-
-  # Pair of reporting metadata details for a candidate URL for `selectURL()`.
-  type SharedStorageReportingMetadata extends object
-    properties
-      string eventType
-      string reportingUrl
-
-  # Bundles a candidate URL with its reporting metadata.
-  type SharedStorageUrlWithMetadata extends object
-    properties
-      # Spec of candidate URL.
-      string url
-      # Any associated reporting metadata.
-      array of SharedStorageReportingMetadata reportingMetadata
-
-  # Bundles the parameters for shared storage access events whose
-  # presence/absence can vary according to SharedStorageAccessType.
-  type SharedStorageAccessParams extends object
-    properties
-      # Spec of the module script URL.
-      # Present only for SharedStorageAccessMethods: addModule and
-      # createWorklet.
-      optional string scriptSourceUrl
-      # String denoting "context-origin", "script-origin", or a custom
-      # origin to be used as the worklet's data origin.
-      # Present only for SharedStorageAccessMethod: createWorklet.
-      optional string dataOrigin
-      # Name of the registered operation to be run.
-      # Present only for SharedStorageAccessMethods: run and selectURL.
-      optional string operationName
-      # ID of the operation call.
-      # Present only for SharedStorageAccessMethods: run and selectURL.
-      optional string operationId
-      # Whether or not to keep the worket alive for future run or selectURL
-      # calls.
-      # Present only for SharedStorageAccessMethods: run and selectURL.
-      optional boolean keepAlive
-      # Configures the private aggregation options.
-      # Present only for SharedStorageAccessMethods: run and selectURL.
-      optional SharedStoragePrivateAggregationConfig privateAggregationConfig
-      # The operation's serialized data in bytes (converted to a string).
-      # Present only for SharedStorageAccessMethods: run and selectURL.
-      # TODO(crbug.com/401011862): Consider updating this parameter to binary.
-      optional string serializedData
-      # Array of candidate URLs' specs, along with any associated metadata.
-      # Present only for SharedStorageAccessMethod: selectURL.
-      optional array of SharedStorageUrlWithMetadata urlsWithMetadata
-      # Spec of the URN:UUID generated for a selectURL call.
-      # Present only for SharedStorageAccessMethod: selectURL.
-      optional string urnUuid
-      # Key for a specific entry in an origin's shared storage.
-      # Present only for SharedStorageAccessMethods: set, append, delete, and
-      # get.
-      optional string key
-      # Value for a specific entry in an origin's shared storage.
-      # Present only for SharedStorageAccessMethods: set and append.
-      optional string value
-      # Whether or not to set an entry for a key if that key is already present.
-      # Present only for SharedStorageAccessMethod: set.
-      optional boolean ignoreIfPresent
-      # A number denoting the (0-based) order of the worklet's
-      # creation relative to all other shared storage worklets created by
-      # documents using the current storage partition.
-      # Present only for SharedStorageAccessMethods: addModule, createWorklet.
-      optional integer workletOrdinal
-      # Hex representation of the DevTools token used as the TargetID for the
-      # associated shared storage worklet.
-      # Present only for SharedStorageAccessMethods: addModule, createWorklet,
-      # run, selectURL, and any other SharedStorageAccessMethod when the
-      # SharedStorageAccessScope is sharedStorageWorklet.
-      optional Target.TargetID workletTargetId
-      # Name of the lock to be acquired, if present.
-      # Optionally present only for SharedStorageAccessMethods: batchUpdate,
-      # set, append, delete, and clear.
-      optional string withLock
-      # If the method has been called as part of a batchUpdate, then this
-      # number identifies the batch to which it belongs.
-      # Optionally present only for SharedStorageAccessMethods:
-      # batchUpdate (required), set, append, delete, and clear.
-      optional string batchUpdateId
-      # Number of modifier methods sent in batch.
-      # Present only for SharedStorageAccessMethod: batchUpdate.
-      optional integer batchSize
-
   type StorageBucketsDurability extends string
     enum
       relaxed
@@ -351,51 +209,6 @@ experimental domain Storage
       # True if any tokens were deleted, false otherwise.
       boolean didDeleteTokens
 
-  # Gets metadata for an origin's shared storage.
-  experimental command getSharedStorageMetadata
-    parameters
-      string ownerOrigin
-    returns
-      SharedStorageMetadata metadata
-
-  # Gets the entries in an given origin's shared storage.
-  experimental command getSharedStorageEntries
-    parameters
-      string ownerOrigin
-    returns
-      array of SharedStorageEntry entries
-
-  # Sets entry with `key` and `value` for a given origin's shared storage.
-  experimental command setSharedStorageEntry
-    parameters
-      string ownerOrigin
-      string key
-      string value
-      # If `ignoreIfPresent` is included and true, then only sets the entry if
-      # `key` doesn't already exist.
-      optional boolean ignoreIfPresent
-
-  # Deletes entry for `key` (if it exists) for a given origin's shared storage.
-  experimental command deleteSharedStorageEntry
-    parameters
-      string ownerOrigin
-      string key
-
-  # Clears all entries for a given origin's shared storage.
-  experimental command clearSharedStorageEntries
-    parameters
-      string ownerOrigin
-
-  # Resets the budget for `ownerOrigin` by clearing all budget withdrawals.
-  experimental command resetSharedStorageBudget
-    parameters
-      string ownerOrigin
-
-  # Enables/disables issuing of sharedStorageAccessed events.
-  experimental command setSharedStorageTracking
-    parameters
-      boolean enable
-
   # Set tracking for a storage key's buckets.
   experimental command setStorageBucketTracking
     parameters
@@ -458,47 +271,6 @@ experimental domain Storage
       # Storage bucket to update.
       string bucketId
 
-  # Shared storage was accessed by the associated page.
-  # The following parameters are included in all events.
-  event sharedStorageAccessed
-    parameters
-      # Time of the access.
-      Network.TimeSinceEpoch accessTime
-      # Enum value indicating the access scope.
-      SharedStorageAccessScope scope
-      # Enum value indicating the Shared Storage API method invoked.
-      SharedStorageAccessMethod method
-      # DevTools Frame Token for the primary frame tree's root.
-      Page.FrameId mainFrameId
-      # Serialization of the origin owning the Shared Storage data.
-      string ownerOrigin
-      # Serialization of the site owning the Shared Storage data.
-      string ownerSite
-      # The sub-parameters wrapped by `params` are all optional and their
-      # presence/absence depends on `type`.
-      SharedStorageAccessParams params
-
-  # A shared storage run or selectURL operation finished its execution.
-  # The following parameters are included in all events.
-  event sharedStorageWorkletOperationExecutionFinished
-    parameters
-      # Time that the operation finished.
-      Network.TimeSinceEpoch finishedTime
-      # Time, in microseconds, from start of shared storage JS API call until
-      # end of operation execution in the worklet.
-      integer executionTime
-      # Enum value indicating the Shared Storage API method invoked.
-      SharedStorageAccessMethod method
-      # ID of the operation call.
-      string operationId
-      # Hex representation of the DevTools token used as the TargetID for the
-      # associated shared storage worklet.
-      Target.TargetID workletTargetId
-      # DevTools Frame Token for the primary frame tree's root.
-      Page.FrameId mainFrameId
-      # Serialization of the origin owning the Shared Storage data.
-      string ownerOrigin
-
   event storageBucketCreatedOrUpdated
     parameters
       StorageBucketInfo bucketInfo
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index 463107ab..13490686 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -17,6 +17,8 @@ experimental domain WebMCP
       optional boolean readOnly
       # A hint indicating that the tool output may contain untrusted content, ex: UGC, 3rd party data.
       optional boolean untrustedContent
+      # A hint indicating that executing the tool will result in consequential actions, ex: booking a flight, transferring money.
+      optional boolean consequential
       # If the declarative tool was declared with the autosubmit attribute.
       optional boolean autosubmit
```

## Roll protocol to r1683682 — _2026-08-21T04:41:18.000Z_
######  Diff: [`022aac9...a12defa`](https://github.com/ChromeDevTools/devtools-protocol/compare/022aac9...a12defa)

```diff
@@ domains/Ads.pdl:48 @@ experimental domain Ads
   command getAdMetrics
     returns
       AdMetrics metrics
+
+  # An ad script.
+  # Note: when the script is a transitive ad script, we only fill in the
+  # immediate ancestor script in the provenance's adScriptAncestry field (as its
+  # first entry), rather than filling in the full ancestry. This saves work for
+  # the backend, and the frontend can reconstruct the full ancestry if
+  # necessary.
+  type AdScript extends object
+    properties
+      # The script ID.
+      Runtime.ScriptId scriptId
+      # The ad provenance.
+      Network.AdProvenance provenance
+
+  # Retrieves ad scripts for the current page. To minimize payload size, this
+  # only returns the newly tracked ad scripts since the last call to
+  # getAdScripts (i.e., the delta).
+  command getAdScripts
+    returns
+      array of AdScript newScripts
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index c00edefc..228ed6c8 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -1701,6 +1701,9 @@ domain Network
       # The filterlist rule that matched, if any.
       optional string filterlistRule
       # The script ancestry that created the ad, if any.
+      # Note: depending on the context, this may represent the full ancestry up
+      # to the root script, or it may contain only one script representing the
+      # immediate ancestor.
       optional AdAncestry adScriptAncestry
 
   # Fired when additional information about a requestWillBeSent event is available from the
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 80cd13ea..0961300c 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1170,8 +1170,16 @@ domain Page
       optional integer maxWidth
       # Maximum screenshot height.
       optional integer maxHeight
-      # Send every n-th frame.
+      # Send every n-th frame. Must be a positive integer.
       optional integer everyNthFrame
+      # Maximum number of frames sent until screencastFrameAck is required.
+      # Defaults to 3. Must be a positive integer.
+      optional integer maxFramesInFlight
+      # By default, after screencastFrameAck arrives, the next produced frame is sent.
+      # Passing this flag enables storing the last produced frame in memory, which is
+      # immediately sent upon screencastFrameAck. This way, overall performance is
+      # traded for a better latency.
+      optional boolean sendLastFrame
 
   # Starts screencast video recording.
   experimental command startScreenRecording
```

## Roll protocol to r1682007 — _2026-08-19T04:37:26.000Z_
######  Diff: [`0539a3c...022aac9`](https://github.com/ChromeDevTools/devtools-protocol/compare/0539a3c...022aac9)

```diff
@@ domains/Browser.pdl:332 @@ domain Browser
   command addPrivacySandboxEnrollmentOverride
     parameters
       string url
+
+  # Gets the current globally-applied privacy control status
+  # See https://www.w3.org/TR/gpc/#get-global-privacy-control
+  experimental command getGlobalPrivacyControl
+    returns
+      boolean gpc
+
+  # Sets and then gets the current globally-applied privacy control status
+  # See https://www.w3.org/TR/gpc/#set-global-privacy-control
+  experimental command setGlobalPrivacyControl
+    parameters
+      boolean gpc
+    returns
+      boolean gpc
```

## Roll protocol to r1681094 — _2026-08-18T04:35:11.000Z_
######  Diff: [`66fa447...0539a3c`](https://github.com/ChromeDevTools/devtools-protocol/compare/66fa447...0539a3c)

```diff
@@ domains/Emulation.pdl:570 @@ domain Emulation
       # Hardware concurrency to report
       integer hardwareConcurrency
 
+  # Overrides the value of navigator.cpuPerformance
+  experimental command setCPUPerformanceOverride
+    parameters
+      # Override value. Omitting the parameter disables the override.
+      optional enum performanceTier
+        # Tier 0: Unknown
+        unknown
+        # Tier 1: Low
+        low
+        # Tier 2: Mid
+        mid
+        # Tier 3: High
+        high
+        # Tier 4: Ultra
+        ultra
+
   # Allows overriding user agent with the given string.
   # `userAgentMetadata` must be set for Client Hint headers to be sent.
   command setUserAgentOverride
```

## Roll protocol to r1680125 — _2026-08-15T04:37:29.000Z_
######  Diff: [`9af7dce...66fa447`](https://github.com/ChromeDevTools/devtools-protocol/compare/9af7dce...66fa447)

```diff
@@ domains/Page.pdl:131 @@ domain Page
       identity-credentials-get
       idle-detection
       interest-cohort
-      join-ad-interest-group
       keyboard-map
       language-detector
       language-model
@@ -152,9 +151,7 @@ domain Page
       private-state-token-redemption
       publickey-credentials-create
       publickey-credentials-get
-      record-ad-auction-events
       rewriter
-      run-ad-auction
       screen-wake-lock
       serial
       # Deprecated.
```

## Roll protocol to r1679354 — _2026-08-14T05:00:28.000Z_
######  Diff: [`716ccac...9af7dce`](https://github.com/ChromeDevTools/devtools-protocol/compare/716ccac...9af7dce)

```diff
@@ domains/Network.pdl:2094 @@ domain Network
       InvalidPreProvisionedKeyInitiatorMissing
       PreProvisionedKeyAccessNotGranted
       PreProvisionedKeyNotFound
+      AttestationCertificationError
+      AttestationSigningError
   # LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult)
 
   # Details about a failed device bound session network request.
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index b26790f8..761a6f9f 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -236,6 +236,7 @@ experimental domain Preload
       PrefetchIsStale
       PrefetchNotEligibleBlockedByConnectionAllowlist
       PrefetchNotEligibleBrowserContextOffTheRecord
+      PrefetchNotEligibleCrossOrigin
       PrefetchNotEligibleDataSaverEnabled
       PrefetchNotEligibleExistingProxy
       PrefetchNotEligibleHostIsNonUnique
diff --git a/pdl/domains/WebAudio.pdl b/pdl/domains/WebAudio.pdl
index 5df199dd..17d125ee 100644
--- a/pdl/domains/WebAudio.pdl
+++ b/pdl/domains/WebAudio.pdl
@@ -77,6 +77,7 @@ experimental domain WebAudio
       number maxOutputChannelCount
       # Context sample rate.
       number sampleRate
+      number renderQuantumSize
 
 # Protocol object for AudioListener
   type AudioListener extends object
```

## Roll protocol to r1678596 — _2026-08-13T05:03:31.000Z_
######  Diff: [`963b290...716ccac`](https://github.com/ChromeDevTools/devtools-protocol/compare/963b290...716ccac)

```diff
@@ domains/Page.pdl:148 @@ domain Page
       otp-credentials
       payment
       picture-in-picture
-      private-aggregation
       private-state-token-issuance
       private-state-token-redemption
       publickey-credentials-create
```

## Roll protocol to r1677763 — _2026-08-12T05:00:19.000Z_
######  Diff: [`75d6311...963b290`](https://github.com/ChromeDevTools/devtools-protocol/compare/75d6311...963b290)

```diff
@@ domains/Audits.pdl:341 @@ experimental domain Audits
       InvalidAllowlistItemType
       ReportingEndpointNotToken
       InvalidUrlPattern
+      IFrameAttributeLoosensEmbeddingRequirement
+      InvalidAllowConnectionAllowlistFrom
+      EmbeddingRequirementNotSatisfied
 
 # Details for issues about documents in Quirks Mode
 # or Limited Quirks Mode that affects page layouting.
diff --git a/pdl/domains/Emulation.pdl b/pdl/domains/Emulation.pdl
index dfbf0558..bee4a46c 100644
--- a/pdl/domains/Emulation.pdl
+++ b/pdl/domains/Emulation.pdl
@@ -258,6 +258,16 @@ domain Emulation
     parameters
       SafeAreaInsets insets
 
+  # Overrides virtual keyboard geometry in CSS pixels, relative to the top-level viewport. The
+  # provided rect is used for navigator.virtualKeyboard.boundingRect, geometrychange events, and
+  # env(keyboard-inset-*) values on the inspected frame. The override applies independently of
+  # navigator.virtualKeyboard.overlaysContent so clients can preview overlay geometry without
+  # mutating page state. Values are rounded to the nearest CSS pixel. Omitting the rect clears the
+  # override.
+  experimental command setVirtualKeyboardGeometryOverride
+    parameters
+      optional DOM.Rect keyboardRect
+
   # Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
   # window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
   # query results).
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index d3609630..1a4c07ad 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -919,22 +919,6 @@ domain Network
       # Errors occurred while handling the signed exchange.
       optional array of SignedExchangeError errors
 
-  # List of content encodings supported by the backend.
-  experimental type ContentEncoding extends string
-    enum
-      deflate
-      gzip
-      br
-      zstd
-
-  # Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.
-  experimental command setAcceptedEncodings
-    parameters
-      # List of accepted content encodings.
-      array of ContentEncoding encodings
-
-  # Clears accepted encodings set by setAcceptedEncodings
-  experimental command clearAcceptedEncodingsOverride
 
   # Tells whether clearing browser cache is supported.
   deprecated command canClearBrowserCache
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index dcf1ddfb..df727762 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1647,6 +1647,7 @@ domain Page
       EmbedderExtensionMessagingForOpenPort
       EmbedderExtensionSentMessageToCachedFrame
       EmbedderExtensionFrame
+      EmbedderPrivilegedWebContents
       RequestedByWebViewClient
       PostMessageByWebViewClient
       CacheControlNoStoreDeviceBoundSessionTerminated
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 7978923d..498ba7d6 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -487,14 +487,8 @@ domain Debugger
       # New return value.
       Runtime.CallArgument newValue
 
-  # Edits JavaScript source live.
-  #
-  # In general, functions that are currently on the stack can not be edited with
-  # a single exception: If the edited function is the top-most stack frame and
-  # that is the only activation of that function on the stack. In this case
-  # the live edit will be successful and a `Debugger.restartFrame` for the
-  # top-most function is automatically triggered.
-  command setScriptSource
+  # Live edit is no longer supported and this command always fails with a "no longer available" error.
+  deprecated command setScriptSource
     parameters
       # Id of the script to edit.
       Runtime.ScriptId scriptId
```

## Roll protocol to r1676914 — _2026-08-11T04:53:33.000Z_
######  Diff: [`495a557...75d6311`](https://github.com/ChromeDevTools/devtools-protocol/compare/495a557...75d6311)

```diff
@@ domains/Page.pdl:158 @@ domain Page
       run-ad-auction
       screen-wake-lock
       serial
+      # Deprecated.
       shared-storage
+      # Deprecated.
       shared-storage-select-url
       smart-card
       speaker-selection
diff --git a/pdl/domains/WebAuthn.pdl b/pdl/domains/WebAuthn.pdl
index 9f83b032..5e3e5d3f 100644
--- a/pdl/domains/WebAuthn.pdl
+++ b/pdl/domains/WebAuthn.pdl
@@ -22,6 +22,7 @@ experimental domain WebAuthn
       ctap2_1
       ctap2_2
 
+  # LINT.IfChange(AuthenticatorTransport)
   type AuthenticatorTransport extends string
     enum
       # Cross-Platform authenticator attachments:
@@ -29,8 +30,11 @@ experimental domain WebAuthn
       nfc
       ble
       cable
+      hybrid
+      smart-card
       # Platform authenticator attachment:
       internal
+  # LINT.ThenChange(//content/browser/devtools/protocol/webauthn_handler.cc:ConvertToFidoTransportProtocol)
 
   type VirtualAuthenticatorOptions extends object
     properties
```

## Roll protocol to r1676105 — _2026-08-08T04:42:45.000Z_
######  Diff: [`2d019e7...495a557`](https://github.com/ChromeDevTools/devtools-protocol/compare/2d019e7...495a557)

```diff
@@ domains/Page.pdl:1175 @@ domain Page
       # Send every n-th frame.
       optional integer everyNthFrame
 
+  # Starts screencast video recording.
+  experimental command startScreenRecording
+    parameters
+      optional boolean audio
+      # Maximum frame width in pixels.
+      optional integer maxWidth
+      # Maximum frame height in pixels.
+      optional integer maxHeight
+      # Maximum frame rate in frames per second.
+      optional integer frameRate
+    returns
+      # A handle of the stream that holds resulting screencast data.
+      experimental IO.StreamHandle stream
+
+  # Stops screencast video recording.
+  experimental command stopScreenRecording
+    returns
+      # A handle of the stream that holds resulting screencast data.
+      experimental IO.StreamHandle stream
+
   # Force the page stop all navigations and pending resource fetches.
   command stopLoading
```

## Roll protocol to r1674729 — _2026-08-06T05:29:04.000Z_
######  Diff: [`41535d3...2d019e7`](https://github.com/ChromeDevTools/devtools-protocol/compare/41535d3...2d019e7)

```diff
@@ js_protocol.pdl:212 @@ domain Debugger
       optional boolean throwOnSideEffect
       # Terminate execution after timing out (number of milliseconds).
       experimental optional Runtime.TimeDelta timeout
+      # Specifies the scope number to evaluate the expression in (default: 0, innermost scope).
+      experimental optional integer scopeNumber
     returns
       # Object wrapper for the evaluation result.
       Runtime.RemoteObject result
```

## Roll protocol to r1673900 — _2026-08-05T05:28:38.000Z_
######  Diff: [`7283814...41535d3`](https://github.com/ChromeDevTools/devtools-protocol/compare/7283814...41535d3)

```diff
@@ domains/DOM.pdl:827 @@ domain DOM
       # List of popovers that were closed in order to respect popover stacking order.
       array of NodeId nodeIds
 
+  # When enabling, this API forces an element to gain interest in its target,
+  # keeping interest active until disabled.
+  experimental command forceShowInterest
+    parameters
+      # Id of the interest invoker HTMLElement.
+      NodeId nodeId
+      # If true, opens and holds interest. If false, releases forced interest.
+      boolean enable
+
   # Fired when `Element`'s attribute is modified.
   event attributeModified
     parameters
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 26941081..feb1a1a7 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -684,7 +684,6 @@ domain Page
     properties
       string action
       string name
-      optional array of ImageResource icons
       # Mimic a map, name is the key, accepts is the value.
       optional array of FileFilter accepts
       # Won't repeat the enums, using string for easy comparison. Same as the
diff --git a/pdl/domains/WebAuthn.pdl b/pdl/domains/WebAuthn.pdl
index c0b199c7..9f83b032 100644
--- a/pdl/domains/WebAuthn.pdl
+++ b/pdl/domains/WebAuthn.pdl
@@ -102,7 +102,7 @@ experimental domain WebAuthn
       # If -1, the credential won't have an associated signature counter, and
       # every assertion operation will report a value of 0.
       # See https://w3c.github.io/webauthn/#signature-counter
-      optional integer signCount
+      integer signCount
       # The large blob associated with the credential.
       # See https://w3c.github.io/webauthn/#sctn-large-blob-extension
       optional binary largeBlob
```

## Roll protocol to r1672245 — _2026-08-01T05:34:55.000Z_
######  Diff: [`6f1723f...7283814`](https://github.com/ChromeDevTools/devtools-protocol/compare/6f1723f...7283814)

```diff
@@ domains/Audits.pdl:468 @@ experimental domain Audits
       TooManyRequests
       WellKnownHttpNotFound
       WellKnownNoResponse
+      WellKnownBlockedByConnectionAllowlist
       WellKnownInvalidResponse
       WellKnownListEmpty
       WellKnownInvalidContentType
@@ -475,6 +476,7 @@ experimental domain Audits
       WellKnownTooBig
       ConfigHttpNotFound
       ConfigNoResponse
+      ConfigBlockedByConnectionAllowlist
       ConfigInvalidResponse
       ConfigInvalidContentType
       IdpNotPotentiallyTrustworthy
@@ -484,11 +486,13 @@ experimental domain Audits
       InvalidSigninResponse
       AccountsHttpNotFound
       AccountsNoResponse
+      AccountsBlockedByConnectionAllowlist
       AccountsInvalidResponse
       AccountsListEmpty
       AccountsInvalidContentType
       IdTokenHttpNotFound
       IdTokenNoResponse
+      IdTokenBlockedByConnectionAllowlist
       IdTokenInvalidResponse
       IdTokenIdpErrorResponse
       IdTokenCrossSiteIdpErrorResponse
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 81ab5df7..d3609630 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -42,9 +42,6 @@ domain Network
   # a network request.
   type RequestId extends string
 
-  # Unique intercepted request identifier.
-  type InterceptionId extends string
-
   # Network level fetch failure reason.
   type ErrorReason extends string
     enum
@@ -849,24 +846,6 @@ domain Network
       # ProvideCredentials.
       optional string password
 
-  # Stages of the interception to begin intercepting. Request will intercept before the request is
-  # sent. Response will intercept after the response is received.
-  experimental type InterceptionStage extends string
-    enum
-      Request
-      HeadersReceived
-
-  # Request pattern for interception.
-  experimental type RequestPattern extends object
-    properties
-      # Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed. Escape character is
-      # backslash. Omitting is equivalent to `"*"`.
-      optional string urlPattern
-      # If set, only requests for matching resource types will be intercepted.
-      optional ResourceType resourceType
-      # Stage at which to begin intercepting requests. Default is Request.
-      optional InterceptionStage interceptionStage
-
   # Information about a signed exchange signature.
   # https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
   experimental type SignedExchangeSignature extends object
@@ -981,35 +960,6 @@ domain Network
   # Clears browser cookies.
   command clearBrowserCookies
 
-  # Response to Network.requestIntercepted which either modifies the request to continue with any
-  # modifications, or blocks it, or completes it with the provided response bytes. If a network
-  # fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
-  # event will be sent with the same InterceptionId.
-  # Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.
-  experimental deprecated command continueInterceptedRequest
-    parameters
-      InterceptionId interceptionId
-      # If set this causes the request to fail with the given reason. Passing `Aborted` for requests
-      # marked with `isNavigationRequest` also cancels the navigation. Must not be set in response
-      # to an authChallenge.
-      optional ErrorReason errorReason
-      # If set the requests completes using with the provided base64 encoded raw response, including
-      # HTTP status line and headers etc... Must not be set in response to an authChallenge.
-      optional binary rawResponse
-      # If set the request url will be modified in a way that's not observable by page. Must not be
-      # set in response to an authChallenge.
-      optional string url
-      # If set this allows the request method to be overridden. Must not be set in response to an
-      # authChallenge.
-      optional string method
-      # If set this allows postData to be set. Must not be set in response to an authChallenge.
-      optional string postData
-      # If set this allows the request headers to be changed. Must not be set in response to an
-      # authChallenge.
-      optional Headers headers
-      # Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
-      optional AuthChallengeResponse authChallengeResponse
-
   # Deletes browser cookies with matching name and url or domain/path/partitionKey pair.
   command deleteCookies
     parameters
@@ -1186,27 +1136,6 @@ domain Network
       # True, if content was sent as base64.
       boolean base64Encoded
 
-  # Returns content served for the given currently intercepted request.
-  experimental command getResponseBodyForInterception
-    parameters
-      # Identifier for the intercepted request to get body for.
-      InterceptionId interceptionId
-    returns
-      # Response body.
-      string body
-      # True, if content was sent as base64.
-      boolean base64Encoded
-
-  # Returns a handle to the stream representing the response body. Note that after this command,
-  # the intercepted request can't be continued as is -- you either need to cancel it or to provide
-  # the response body. The stream only supports sequential read, IO.read will fail if the position
-  # is specified.
-  experimental command takeResponseBodyForInterceptionAsStream
-    parameters
-      InterceptionId interceptionId
-    returns
-      IO.StreamHandle stream
-
   # This method sends a new XMLHttpRequest which is identical to the original one. The following
   # parameters should be identical: method, url, async, request body, extra headers, withCredentials
   # attribute, user, password.
@@ -1314,14 +1243,6 @@ domain Network
       # Whether to attach a page script stack for debugging purpose.
       boolean enabled
 
-  # Sets the requests to intercept that match the provided patterns and optionally resource types.
-  # Deprecated, please use Fetch.enable instead.
-  experimental deprecated command setRequestInterception
-    parameters
-      # Requests matching any of these patterns will be forwarded and wait for the corresponding
-      # continueInterceptedRequest call.
-      array of RequestPattern patterns
-
   # Allows overriding user agent with the given string.
   command setUserAgentOverride
     redirect Emulation
@@ -1402,43 +1323,6 @@ domain Network
       # Total number of bytes received for this request.
       number encodedDataLength
 
-  # Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
-  # mocked.
-  # Deprecated, use Fetch.requestPaused instead.
-  experimental deprecated event requestIntercepted
-    parameters
-      # Each request the page makes will have a unique id, however if any redirects are encountered
-      # while processing that fetch, they will be reported with the same id as the original fetch.
-      # Likewise if HTTP authentication is needed then the same fetch id will be used.
-      InterceptionId interceptionId
-      Request request
-      # The id of the frame that initiated the request.
-      Page.FrameId frameId
-      # How the requested resource will be used.
-      ResourceType resourceType
-      # Whether this is a navigation request, which can abort the navigation completely.
-      boolean isNavigationRequest
-      # Set if the request is a navigation that will result in a download.
-      # Only present after response is received from the server (i.e. HeadersReceived stage).
-      optional boolean isDownload
-      # Redirect location, only sent if a redirect was intercepted.
-      optional string redirectUrl
-      # Details of the Authorization Challenge encountered. If this is set then
-      # continueInterceptedRequest must contain an authChallengeResponse.
-      optional AuthChallenge authChallenge
-      # Response error if intercepted at response stage or if redirect occurred while intercepting
-      # request.
-      optional ErrorReason responseErrorReason
-      # Response code if intercepted at response stage or if redirect occurred while intercepting
-      # request or auth retry occurred.
-      optional integer responseStatusCode
-      # Response headers if intercepted at the response stage or if redirect occurred while
-      # intercepting request or auth retry occurred.
-      optional Headers responseHeaders
-      # If the intercepted request had a corresponding requestWillBeSent event fired for it, then
-      # this requestId will be the same as the requestId present in the requestWillBeSent event.
-      optional RequestId requestId
-
   # Fired if request ended up loading from cache.
   event requestServedFromCache
     parameters
@@ -1657,7 +1541,7 @@ domain Network
   experimental event directTCPSocketAborted
     parameters
       RequestId identifier
-      string errorMessage
+      ErrorReason errorMessage
       MonotonicTime timestamp
 
   # Fired when direct_socket.TCPSocket is closed.
@@ -1736,7 +1620,7 @@ domain Network
   experimental event directUDPSocketAborted
     parameters
       RequestId identifier
-      string errorMessage
+      ErrorReason errorMessage
       MonotonicTime timestamp
 
   # Fired when direct_socket.UDPSocket is closed.
```
