# Chrome DevTools Protocol changelog — 2025-03

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-03, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1439962 — _2025-03-30T04:30:16.000Z_
######  Diff: [`c1a57ab...fc91db8`](https://github.com/ChromeDevTools/devtools-protocol/compare/c1a57ab...fc91db8)

```diff
@@ browser_protocol.pdl:13266 @@ experimental domain BluetoothEmulation
       integer rssi
       ScanRecord scanRecord
 
+  # Describes the properties of a characteristic. This follows Bluetooth Core
+  # Specification BT 4.2 Vol 3 Part G 3.3.1. Characteristic Properties.
+  type CharacteristicProperties extends object
+    properties
+      optional boolean broadcast
+      optional boolean read
+      optional boolean writeWithoutResponse
+      optional boolean write
+      optional boolean notify
+      optional boolean indicate
+      optional boolean authenticatedSignedWrites
+      optional boolean extendedProperties
+
   # Enable the BluetoothEmulation domain.
   command enable
     parameters
@@ -13307,20 +13320,41 @@ experimental domain BluetoothEmulation
       GATTOperationType type
       integer code
 
-  # Adds a service with |uuid| to the peripheral with |address|.
+  # Adds a service with |serviceUuid| to the peripheral with |address|.
   command addService
     parameters
       string address
       string serviceUuid
     returns
       # An identifier that uniquely represents this service.
-      string id
+      string serviceId
 
-  # Removes the service respresented by |id| from the peripheral with |address|.
+  # Removes the service respresented by |serviceId| from the peripheral with
+  # |address|.
   command removeService
     parameters
       string address
-      string id
+      string serviceId
+
+  # Adds a characteristic with |characteristicUuid| and |properties| to the
+  # service represented by |serviceId| in the peripheral with |address|.
+  command addCharacteristic
+    parameters
+      string address
+      string serviceId
+      string characteristicUuid
+      CharacteristicProperties properties
+    returns
+      # An identifier that uniquely represents this characteristic.
+      string characteristicId
+
+  # Removes the characteristic respresented by |characteristicId| from the
+  # service respresented by |serviceId| in the peripheral with |address|.
+  command removeCharacteristic
+    parameters
+      string address
+      string serviceId
+      string characteristicId
 
   # Event for when a GATT operation of |type| to the peripheral with |address|
   # happened.
```

## Roll protocol to r1439209 — _2025-03-28T04:30:28.000Z_
######  Diff: [`028dc50...c1a57ab`](https://github.com/ChromeDevTools/devtools-protocol/compare/028dc50...c1a57ab)

```diff
@@ browser_protocol.pdl:823 @@ experimental domain Audits
       ValidationFailedSignatureExpired
       ValidationFailedInvalidLength
       ValidationFailedSignatureMismatch
+      ValidationFailedIntegrityMismatch
 
   # Details for issues around "Attribution Reporting API" usage.
   # Explainer: https://github.com/WICG/attribution-reporting-api
@@ -859,6 +860,7 @@ experimental domain Audits
     properties
       SRIMessageSignatureError error
       string signatureBase
+      array of string integrityAssertions
       AffectedRequest request
 
   type GenericIssueErrorType extends string
@@ -6640,6 +6642,8 @@ domain Network
       PortMismatch
       # The cookie's source scheme value does not match the request origin's scheme.
       SchemeMismatch
+      # Unpartitioned cookie access from an anonymous context was blocked.
+      AnonymousContext
 
   # Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.
   experimental type CookieExemptionReason extends string
@@ -13303,6 +13307,21 @@ experimental domain BluetoothEmulation
       GATTOperationType type
       integer code
 
+  # Adds a service with |uuid| to the peripheral with |address|.
+  command addService
+    parameters
+      string address
+      string serviceUuid
+    returns
+      # An identifier that uniquely represents this service.
+      string id
+
+  # Removes the service respresented by |id| from the peripheral with |address|.
+  command removeService
+    parameters
+      string address
+      string id
+
   # Event for when a GATT operation of |type| to the peripheral with |address|
   # happened.
   event gattOperationReceived
```

## Roll protocol to r1438564 — _2025-03-27T04:30:05.000Z_
######  Diff: [`432dff0...028dc50`](https://github.com/ChromeDevTools/devtools-protocol/compare/432dff0...028dc50)

```diff
@@ browser_protocol.pdl:10554 @@ experimental domain Storage
       bidderTrustedSignals
       sellerTrustedSignals
 
-  # Enum of shared storage access types.
-  type SharedStorageAccessType extends string
-    enum
-      documentAddModule
-      documentSelectURL
-      documentRun
-      documentSet
-      documentAppend
-      documentDelete
-      documentClear
-      documentGet
-      workletSet
-      workletAppend
-      workletDelete
-      workletClear
-      workletGet
-      workletKeys
-      workletEntries
-      workletLength
-      workletRemainingBudget
-      headerSet
-      headerAppend
-      headerDelete
-      headerClear
+  # Enum of shared storage access scopes.
+  type SharedStorageAccessScope extends string
+    enum
+      window
+      sharedStorageWorklet
+      protectedAudienceWorklet
+      header
+
+  # Enum of shared storage access methods.
+  type SharedStorageAccessMethod extends string
+    enum
+      addModule
+      createWorklet
+      selectURL
+      run
+      batchUpdate
+      set
+      append
+      delete
+      clear
+      get
+      keys
+      values
+      entries
+      length
+      remainingBudget
 
   # Struct for a single key-value pair in an origin's shared storage.
   type SharedStorageEntry extends object
@@ -10993,12 +10995,16 @@ experimental domain Storage
     parameters
       # Time of the access.
       Network.TimeSinceEpoch accessTime
+      # Enum value indicating the access scope.
+      SharedStorageAccessScope scope
       # Enum value indicating the Shared Storage API method invoked.
-      SharedStorageAccessType type
+      SharedStorageAccessMethod method
       # DevTools Frame Token for the primary frame tree's root.
       Page.FrameId mainFrameId
-      # Serialized origin for the context that invoked the Shared Storage API.
+      # Serialization of the origin owning the Shared Storage data.
       string ownerOrigin
+      # Serialization of the site owning the Shared Storage data.
+      string ownerSite
       # The sub-parameters wrapped by `params` are all optional and their
       # presence/absence depends on `type`.
       SharedStorageAccessParams params
```

## Roll protocol to r1436416 — _2025-03-22T04:29:26.000Z_
######  Diff: [`cf78806...432dff0`](https://github.com/ChromeDevTools/devtools-protocol/compare/cf78806...432dff0)

```diff
@@ browser_protocol.pdl:8464 @@ domain Page
       interest-cohort
       join-ad-interest-group
       keyboard-map
+      language-detector
       local-fonts
       magnetometer
       media-playback-while-not-visible
@@ -8478,6 +8479,7 @@ domain Page
       private-state-token-redemption
       publickey-credentials-create
       publickey-credentials-get
+      rewriter
       run-ad-auction
       screen-wake-lock
       serial
@@ -8488,7 +8490,9 @@ domain Page
       speaker-selection
       storage-access
       sub-apps
+      summarizer
       sync-xhr
+      translator
       unload
       usb
       usb-unrestricted
@@ -8497,6 +8501,7 @@ domain Page
       web-printing
       web-share
       window-management
+      writer
       xr-spatial-tracking
 
   # Reason for a permissions policy feature to be disabled.
@@ -13215,6 +13220,12 @@ experimental domain BluetoothEmulation
       powered-off
       powered-on
 
+  # Indicates the various types of GATT event.
+  type GATTOperationType extends string
+    enum
+      connection
+      discovery
+
   # Stores the manufacturer data
   type ManufacturerData extends object
     properties
@@ -13276,3 +13287,19 @@ experimental domain BluetoothEmulation
   command simulateAdvertisement
     parameters
       ScanEntry entry
+
+  # Simulates the response code from the peripheral with |address| for a
+  # GATT operation of |type|. The |code| value follows the HCI Error Codes from
+  # Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.
+  command simulateGATTOperationResponse
+    parameters
+      string address
+      GATTOperationType type
+      integer code
+
+  # Event for when a GATT operation of |type| to the peripheral with |address|
+  # happened.
+  event gattOperationReceived
+    parameters
+      string address
+      GATTOperationType type
```

## Roll protocol to r1433962 — _2025-03-18T04:29:59.000Z_
######  Diff: [`b9e45c3...cf78806`](https://github.com/ChromeDevTools/devtools-protocol/compare/b9e45c3...cf78806)

```diff
@@ browser_protocol.pdl:858 @@ experimental domain Audits
   type SRIMessageSignatureIssueDetails extends object
     properties
       SRIMessageSignatureError error
+      string signatureBase
       AffectedRequest request
 
   type GenericIssueErrorType extends string
@@ -4594,7 +4595,8 @@ domain Emulation
       experimental optional Page.Viewport viewport
       # If set, the display feature of a multi-segment screen. If not set, multi-segment support
       # is turned-off.
-      experimental optional DisplayFeature displayFeature
+      # Deprecated, use Emulation.setDisplayFeaturesOverride.
+      experimental deprecated optional DisplayFeature displayFeature
       # If set, the posture of a foldable device. If not set the posture is set
       # to continuous.
       # Deprecated, use Emulation.setDevicePostureOverride.
@@ -4612,6 +4614,18 @@ domain Emulation
   # Does nothing if no override is set.
   experimental command clearDevicePostureOverride
 
+  # Start using the given display features to pupulate the Viewport Segments API.
+  # This override can also be set in setDeviceMetricsOverride().
+  experimental command setDisplayFeaturesOverride
+    parameters
+      array of DisplayFeature features
+
+  # Clears the display features override set with either setDeviceMetricsOverride()
+  # or setDisplayFeaturesOverride() and starts using display features from the
+  # platform again.
+  # Does nothing if no override is set.
+  experimental command clearDisplayFeaturesOverride
+
   experimental command setScrollbarsHidden
     parameters
       # Whether scrollbars should be always hidden.
@@ -12903,6 +12917,7 @@ experimental domain Preload
       PrefetchFailedMIMENotSupported
       PrefetchFailedNetError
       PrefetchFailedNon2XX
+      PrefetchEvictedAfterBrowsingDataRemoved
       PrefetchEvictedAfterCandidateRemoved
       PrefetchEvictedForNewerPrefetch
       PrefetchHeldback
```

## Roll protocol to r1432532 — _2025-03-14T04:29:36.000Z_
######  Diff: [`8d0eb7b...b9e45c3`](https://github.com/ChromeDevTools/devtools-protocol/compare/8d0eb7b...b9e45c3)

```diff
@@ browser_protocol.pdl:9911 @@ domain Page
       RequestedByWebViewClient
       PostMessageByWebViewClient
       CacheControlNoStoreDeviceBoundSessionTerminated
+      CacheLimitPruned
 
   # Types of not restored reasons for back-forward cache.
   experimental type BackForwardCacheNotRestoredReasonType extends string
```

## Roll protocol to r1431913 — _2025-03-13T04:30:01.000Z_
######  Diff: [`e968b49...8d0eb7b`](https://github.com/ChromeDevTools/devtools-protocol/compare/e968b49...8d0eb7b)

```diff
@@ browser_protocol.pdl:1481 @@ domain Browser
       idleDetection
       keyboardLock
       localFonts
+      localNetworkAccess
       midi
       midiSysex
       nfc
@@ -1740,6 +1741,25 @@ domain Browser
     parameters
       string url
 
+  experimental type PrivacySandboxAPI extends string
+    enum
+      BiddingAndAuctionServices
+      TrustedKeyValue
+
+  # Configures encryption keys used with a given privacy sandbox API to talk
+  # to a trusted coordinator.  Since this is intended for test automation only,
+  # coordinatorOrigin must be a .test domain. No existing coordinator
+  # configuration for the origin may exist.
+  command addPrivacySandboxCoordinatorKeyConfig
+    parameters
+      PrivacySandboxAPI api
+      string coordinatorOrigin
+      string keyConfig
+      # BrowserContext to perform the action in. When omitted, default browser
+      # context is used.
+      optional BrowserContextID browserContextId
+
+
 # This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
 # have an associated `id` used in subsequent operations on the related object. Each object type has
 # a specific `id` structure, and those are not interchangeable between objects of different kinds.
@@ -7466,6 +7486,7 @@ domain Network
       PreflightBlock
       PreflightWarn
       PermissionBlock
+      PermissionWarn
 
   experimental type IPAddressSpace extends string
     enum
```

## Roll protocol to r1430640 — _2025-03-11T04:29:58.000Z_
######  Diff: [`e1bdcc8...e968b49`](https://github.com/ChromeDevTools/devtools-protocol/compare/e1bdcc8...e968b49)

```diff
@@ browser_protocol.pdl:9527 @@ domain Page
   command setInterceptFileChooserDialog
     parameters
       boolean enabled
+      # If true, cancels the dialog by emitting relevant events (if any)
+      # in addition to not showing it if the interception is enabled
+      # (default: false).
+      experimental optional boolean cancel
 
   event domContentEventFired
     parameters
```

## Roll protocol to r1429850 — _2025-03-08T04:26:13.000Z_
######  Diff: [`5810b85...e1bdcc8`](https://github.com/ChromeDevTools/devtools-protocol/compare/5810b85...e1bdcc8)

```diff
@@ browser_protocol.pdl:7404 @@ domain Network
       # Timestamp.
       MonotonicTime timestamp
 
+  experimental type DirectSocketDnsQueryType extends string
+    enum
+      ipv4
+      ipv6
+
+  experimental type DirectTCPSocketOptions extends object
+    properties
+      # TCP_NODELAY option
+      boolean noDelay
+      # Expected to be unsigned integer.
+      optional number keepAliveDelay
+      # Expected to be unsigned integer.
+      optional number sendBufferSize
+      # Expected to be unsigned integer.
+      optional number receiveBufferSize
+      optional DirectSocketDnsQueryType dnsQueryType
+
+
+  # Fired upon direct_socket.TCPSocket creation.
+  experimental event directTCPSocketCreated
+    parameters
+      RequestId identifier
+      string remoteAddr
+      # Unsigned int 16.
+      integer remotePort
+      DirectTCPSocketOptions options
+      MonotonicTime timestamp
+      optional Initiator initiator
+
+  # Fired when direct_socket.TCPSocket connection is opened.
+  experimental event directTCPSocketOpened
+    parameters
+      RequestId identifier
+      string remoteAddr
+      # Expected to be unsigned integer.
+      integer remotePort
+      MonotonicTime timestamp
+      optional string localAddr
+      # Expected to be unsigned integer.
+      optional integer localPort
+
+  # Fired when direct_socket.TCPSocket is aborted.
+  experimental event directTCPSocketAborted
+    parameters
+      RequestId identifier
+      string errorMessage
+      MonotonicTime timestamp
+
+  # Fired when direct_socket.TCPSocket is closed.
+  experimental event directTCPSocketClosed
+    parameters
+      RequestId identifier
+      MonotonicTime timestamp
+
   experimental type PrivateNetworkRequestPolicy extends string
     enum
       Allow
@@ -9444,7 +9498,7 @@ domain Page
       autoReject
       autoOptOut
 
-# Sets the Secure Payment Confirmation transaction mode.
+  # Sets the Secure Payment Confirmation transaction mode.
   # https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
   experimental command setSPCTransactionMode
     parameters
@@ -12840,6 +12894,9 @@ experimental domain Preload
       PrefetchNotEligibleSchemeIsNotHttps
       PrefetchNotEligibleUserHasCookies
       PrefetchNotEligibleUserHasServiceWorker
+      PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler
+      PrefetchNotEligibleRedirectFromServiceWorker
+      PrefetchNotEligibleRedirectToServiceWorker
       PrefetchNotEligibleBatterySaverEnabled
       PrefetchNotEligiblePreloadingDisabled
       PrefetchNotFinishedInTime
@@ -13149,6 +13206,14 @@ experimental domain BluetoothEmulation
 
   # Enable the BluetoothEmulation domain.
   command enable
+    parameters
+      # State of the simulated central.
+      CentralState state
+      # If the simulated central supports low-energy.
+      boolean leSupported
+
+  # Set the state of the simulated central.
+  command setSimulatedCentralState
     parameters
       # State of the simulated central.
       CentralState state
```

## Roll protocol to r1428127 — _2025-03-05T04:29:34.000Z_
######  Diff: [`c2846c9...5810b85`](https://github.com/ChromeDevTools/devtools-protocol/compare/c2846c9...5810b85)

```diff
@@ browser_protocol.pdl:4346 @@ domain Emulation
   depends on Page
   depends on Runtime
 
+  experimental type SafeAreaInsets extends object
+    properties
+      # Overrides safe-area-inset-top.
+      optional integer top
+      # Overrides safe-area-max-inset-top.
+      optional integer topMax
+      # Overrides safe-area-inset-left.
+      optional integer left
+      # Overrides safe-area-max-inset-left.
+      optional integer leftMax
+      # Overrides safe-area-inset-bottom.
+      optional integer bottom
+      # Overrides safe-area-max-inset-bottom.
+      optional integer bottomMax
+      # Overrides safe-area-inset-right.
+      optional integer right
+      # Overrides safe-area-max-inset-right.
+      optional integer rightMax
+
   # Screen orientation.
   type ScreenOrientation extends object
     properties
@@ -4516,6 +4535,12 @@ domain Emulation
       # cleared.
       optional DOM.RGBA color
 
+  # Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
+  # respective variables to be undefined, even if previously overridden.
+  experimental command setSafeAreaInsetsOverride
+    parameters
+      SafeAreaInsets insets
+
   # Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
   # window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
   # query results).
```

## Roll protocol to r1427544 — _2025-03-04T04:29:27.000Z_
######  Diff: [`044de40...c2846c9`](https://github.com/ChromeDevTools/devtools-protocol/compare/044de40...c2846c9)

```diff
@@ browser_protocol.pdl:2252 @@ experimental domain CSS
       # Associated style declaration.
       CSSStyle style
 
+  # CSS function argument representation.
+  type CSSFunctionParameter extends object
+    properties
+      # The parameter name.
+      string name
+      # The parameter type.
+      string type
+
+  # CSS function conditional block representation.
+  type CSSFunctionConditionNode extends object
+    properties
+      # Media query for this conditional block. Only one type of condition should be set.
+      optional CSSMedia media
+      # Container query for this conditional block. Only one type of condition should be set.
+      optional CSSContainerQuery containerQueries
+      # @supports CSS at-rule condition. Only one type of condition should be set.
+      optional CSSSupports supports
+      # Block body.
+      array of CSSFunctionNode children
+      # The condition text.
+      string conditionText
+
+  # Section of the body of a CSS function rule.
+  type CSSFunctionNode extends object
+    properties
+      # A conditional block. If set, style should not be set.
+      optional CSSFunctionConditionNode condition
+      # Values set by this node. If set, condition should not be set.
+      optional CSSStyle style
+
+  # CSS function at-rule representation.
+  type CSSFunctionRule extends object
+    properties
+      # Name of the function.
+      Value name
+      # The css style sheet identifier (absent for user agent stylesheet and user-specified
+      # stylesheet rules) this rule came from.
+      optional StyleSheetId styleSheetId
+      # Parent stylesheet's origin.
+      StyleSheetOrigin origin
+      # List of parameters.
+      array of CSSFunctionParameter parameters
+      # Function body.
+      array of CSSFunctionNode children
+
   # CSS keyframe rule representation.
   type CSSKeyframeRule extends object
     properties
@@ -2449,6 +2494,8 @@ experimental domain CSS
       optional CSSFontPaletteValuesRule cssFontPaletteValuesRule
       # Id of the first parent element that does not have display: contents.
       experimental optional DOM.NodeId parentLayoutNodeId
+      # A list of CSS at-function rules referenced by styles of this node.
+      experimental optional array of CSSFunctionRule cssFunctionRules
 
   # Returns all media queries parsed by the rendering engine.
   command getMediaQueries
@@ -6145,6 +6192,9 @@ domain Network
       # Request was a private network request and is denied by user permission.
       # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
       PrivateNetworkAccessPermissionDenied
+      # Request was a local network request and is denied by user permission.
+      # https://github.com/explainers-by-googlers/local-network-access
+      LocalNetworkAccessPermissionDenied
 
   type CorsErrorStatus extends object
     properties
@@ -7336,6 +7386,7 @@ domain Network
       WarnFromInsecureToMorePrivate
       PreflightBlock
       PreflightWarn
+      PermissionBlock
 
   experimental type IPAddressSpace extends string
     enum
```
