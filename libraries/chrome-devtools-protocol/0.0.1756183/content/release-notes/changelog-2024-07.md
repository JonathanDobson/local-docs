# Chrome DevTools Protocol changelog — 2024-07

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-07, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1335233 — _2024-07-31T04:25:01.000Z_
######  Diff: [`a313e79...62fe5c9`](https://github.com/ChromeDevTools/devtools-protocol/compare/a313e79...62fe5c9)

```diff
@@ browser_protocol.pdl:1102 @@ experimental domain Audits
     parameters
       InspectorIssue issue
 
-# Defines commands and events for browser extensions. Available if the client
-# is connected using the --remote-debugging-pipe flag and
-# the --enable-unsafe-extension-debugging flag is set.
+# Defines commands and events for browser extensions.
 experimental domain Extensions
+  # Storage areas.
+  type StorageArea extends string
+    enum
+      session
+      local
+      sync
+      managed
   # Installs an unpacked extension from the filesystem similar to
   # --load-extension CLI flags. Returns extension ID once the extension
-  # has been installed.
+  # has been installed. Available if the client is connected using the
+  # --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging
+  # flag is set.
   command loadUnpacked
     parameters
       # Absolute file path.
@@ -1116,6 +1123,18 @@ experimental domain Extensions
     returns
       # Extension id.
       string id
+  # Gets data from extension storage in the given `area`. If `keys` is
+  # specified, these are used to filter the result.
+  command getStorageItems
+    parameters
+      # ID of extension.
+      string id
+      # StorageArea to retrieve data from.
+      StorageArea storageArea
+      # Keys to retrieve.
+      optional array of string keys
+    returns
+      object data
 
 # Defines commands and events for Autofill.
 experimental domain Autofill
@@ -7964,6 +7983,7 @@ domain Page
   experimental type PermissionsPolicyFeature extends string
     enum
       accelerometer
+      all-screens-capture
       ambient-light-sensor
       attribution-reporting
       autoplay
@@ -12285,6 +12305,7 @@ experimental domain Preload
       AllPrerenderingCanceled
       WindowClosed
       SlowNetwork
+      OtherPrerenderedPageActivated
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1334619 — _2024-07-30T04:27:32.000Z_
######  Diff: [`20344f9...a313e79`](https://github.com/ChromeDevTools/devtools-protocol/compare/20344f9...a313e79)

```diff
@@ browser_protocol.pdl:12284 @@ experimental domain Preload
       JavaScriptInterfaceRemoved
       AllPrerenderingCanceled
       WindowClosed
+      SlowNetwork
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1333880 — _2024-07-27T04:27:46.000Z_
######  Diff: [`5c9857d...20344f9`](https://github.com/ChromeDevTools/devtools-protocol/compare/5c9857d...20344f9)

```diff
@@ browser_protocol.pdl:8020 @@ domain Page
       keyboard-map
       local-fonts
       magnetometer
+      media-playback-while-not-visible
       microphone
       midi
       otp-credentials
```

## Roll protocol to r1330662 — _2024-07-20T04:28:07.000Z_
######  Diff: [`2d19a4e...5c9857d`](https://github.com/ChromeDevTools/devtools-protocol/compare/2d19a4e...5c9857d)

```diff
@@ browser_protocol.pdl:4185 @@ domain Emulation
       optional SensorReadingXYZ xyz
       optional SensorReadingQuaternion quaternion
 
+  experimental type PressureSource extends string
+    enum
+      cpu
+
+  experimental type PressureState extends string
+    enum
+      nominal
+      fair
+      serious
+      critical
+
+  experimental type PressureMetadata extends object
+    properties
+      optional boolean available
+
   # Tells whether emulation is supported.
   deprecated command canEmulate
     returns
@@ -4354,6 +4369,24 @@ domain Emulation
       SensorType type
       SensorReading reading
 
+  # Overrides a pressure source of a given type, as used by the Compute
+  # Pressure API, so that updates to PressureObserver.observe() are provided
+  # via setPressureStateOverride instead of being retrieved from
+  # platform-provided telemetry data.
+  experimental command setPressureSourceOverrideEnabled
+    parameters
+      boolean enabled
+      PressureSource source
+      optional PressureMetadata metadata
+
+  # Provides a given pressure state that will be processed and eventually be
+  # delivered to PressureObserver users. |source| must have been previously
+  # overridden by setPressureSourceOverrideEnabled.
+  experimental command setPressureStateOverride
+    parameters
+      PressureSource source
+      PressureState state
+
   # Overrides the Idle state.
   command setIdleOverride
     parameters
```

## Roll protocol to r1327118 — _2024-07-13T04:27:09.000Z_
######  Diff: [`7c6f8b3...2d19a4e`](https://github.com/ChromeDevTools/devtools-protocol/compare/7c6f8b3...2d19a4e)

```diff
@@ browser_protocol.pdl:10523 @@ experimental domain Storage
       exact
       modulus
 
+  experimental type AttributionReportingAggregatableDebugReportingData extends object
+    properties
+      UnsignedInt128AsBase16 keyPiece
+      # number instead of integer because not all uint32 can be represented by
+      # int
+      number value
+      array of string types
+
+  experimental type AttributionReportingAggregatableDebugReportingConfig extends object
+    properties
+      # number instead of integer because not all uint32 can be represented by
+      # int, only present for source registrations
+      optional number budget
+      UnsignedInt128AsBase16 keyPiece
+      array of AttributionReportingAggregatableDebugReportingData debugData
+      optional string aggregationCoordinatorOrigin
+
   experimental type AttributionReportingSourceRegistration extends object
     properties
       Network.TimeSinceEpoch time
@@ -10542,6 +10559,7 @@ experimental domain Storage
       optional UnsignedInt64AsBase10 debugKey
       AttributionReportingTriggerDataMatching triggerDataMatching
       SignedInt64AsBase10 destinationLimitPriority
+      AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
@@ -10615,6 +10633,7 @@ experimental domain Storage
       optional string aggregationCoordinatorOrigin
       AttributionReportingSourceRegistrationTimeConfig sourceRegistrationTimeConfig
       optional string triggerContextId
+      AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
 
   experimental type AttributionReportingEventLevelResult extends string
     enum
```

## Roll protocol to r1326544 — _2024-07-12T04:27:03.000Z_
######  Diff: [`09a23aa...7c6f8b3`](https://github.com/ChromeDevTools/devtools-protocol/compare/09a23aa...7c6f8b3)

```diff
@@ browser_protocol.pdl:10541 @@ experimental domain Storage
       array of AttributionReportingAggregationKeysEntry aggregationKeys
       optional UnsignedInt64AsBase10 debugKey
       AttributionReportingTriggerDataMatching triggerDataMatching
+      SignedInt64AsBase10 destinationLimitPriority
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
```

## Roll protocol to r1325906 — _2024-07-11T04:28:25.000Z_
######  Diff: [`8297006...09a23aa`](https://github.com/ChromeDevTools/devtools-protocol/compare/8297006...09a23aa)

```diff
@@ browser_protocol.pdl:2208 @@ experimental domain CSS
       deprecated optional array of CSSPositionFallbackRule cssPositionFallbackRules
       # A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property.
       optional array of CSSPositionTryRule cssPositionTryRules
+      # Index of the active fallback in the applied position-try-fallback property,
+      # will not be set if there is no active position-try fallback.
+      optional integer activePositionFallbackIndex
       # A list of CSS at-property rules matching this node.
       optional array of CSSPropertyRule cssPropertyRules
       # A list of CSS property registrations matching this node.
@@ -7215,6 +7218,7 @@ domain Network
       UnsafeNone
       SameOriginPlusCoep
       RestrictPropertiesPlusCoep
+      NoopenerAllowPopups
 
   experimental type CrossOriginOpenerPolicyStatus extends object
     properties
```

## Roll protocol to r1325288 — _2024-07-10T04:27:56.000Z_
######  Diff: [`5c95bcf...8297006`](https://github.com/ChromeDevTools/devtools-protocol/compare/5c95bcf...8297006)

```diff
@@ browser_protocol.pdl:803 @@ experimental domain Audits
 
   type GenericIssueErrorType extends string
     enum
-      CrossOriginPortalPostMessageError
       FormLabelForNameError
       FormDuplicateIdForInputError
       FormInputWithNoLabelError
@@ -9331,7 +9330,6 @@ domain Page
       Printing
       WebDatabase
       PictureInPicture
-      Portal
       SpeechRecognizer
       IdleManager
       PaymentManager
@@ -10839,7 +10837,7 @@ domain Target
       experimental optional Page.FrameId openerFrameId
       experimental optional Browser.BrowserContextID browserContextId
       # Provides additional details for specific target types. For example, for
-      # the type of "page", this may be set to "portal" or "prerender".
+      # the type of "page", this may be set to "prerender".
       experimental optional string subtype
 
   # A filter used by target query/discovery/auto-attach operations.
@@ -12227,6 +12225,7 @@ experimental domain Preload
       JavaScriptInterfaceAdded
       JavaScriptInterfaceRemoved
       AllPrerenderingCanceled
+      WindowClosed
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1324661 — _2024-07-09T04:27:20.000Z_
######  Diff: [`f3aca7c...5c95bcf`](https://github.com/ChromeDevTools/devtools-protocol/compare/f3aca7c...5c95bcf)

```diff
@@ browser_protocol.pdl:4560 @@ domain IO
       # UUID of the specified Blob.
       string uuid
 
+experimental domain FileSystem
+  depends on Network
+  depends on Storage
+
+  type File extends object
+    properties
+      string name
+      # Timestamp
+      Network.TimeSinceEpoch lastModified
+      # Size in bytes
+      number size
+      string type
+
+  type Directory extends object
+    properties
+      string name
+      array of string nestedDirectories
+      # Files that are directly nested under this directory.
+      array of File nestedFiles
+
+  type BucketFileSystemLocator extends object
+    properties
+      # Storage key
+      Storage.SerializedStorageKey storageKey
+      # Bucket name. Not passing a `bucketName` will retrieve the default Bucket. (https://developer.mozilla.org/en-US/docs/Web/API/Storage_API#storage_buckets)
+      optional string bucketName
+      # Path to the directory using each path component as an array item.
+      array of string pathComponents
+
+  command getDirectory
+    parameters
+      BucketFileSystemLocator bucketFileSystemLocator
+    returns
+      # Returns the directory object at the path.
+      Directory directory
+
 experimental domain IndexedDB
   depends on Runtime
   depends on Storage
@@ -10537,6 +10573,8 @@ experimental domain Storage
       # number instead of integer because not all uint32 can be represented by
       # int
       number value
+      UnsignedInt64AsBase10 filteringId
+
 
   experimental type AttributionReportingAggregatableValueEntry extends object
     properties
@@ -10569,6 +10607,7 @@ experimental domain Storage
       array of AttributionReportingEventTriggerData eventTriggerData
       array of AttributionReportingAggregatableTriggerData aggregatableTriggerData
       array of AttributionReportingAggregatableValueEntry aggregatableValues
+      integer aggregatableFilteringIdMaxBytes
       boolean debugReporting
       optional string aggregationCoordinatorOrigin
       AttributionReportingSourceRegistrationTimeConfig sourceRegistrationTimeConfig
```

## Roll protocol to r1323829 — _2024-07-06T04:27:22.000Z_
######  Diff: [`e09b046...f3aca7c`](https://github.com/ChromeDevTools/devtools-protocol/compare/e09b046...f3aca7c)

```diff
@@ browser_protocol.pdl:7927 @@ domain Page
       compute-pressure
       cross-origin-isolated
       deferred-fetch
+      digital-credentials-get
       direct-sockets
       display-capture
       document-domain
```

## Roll protocol to r1323532 — _2024-07-05T04:28:00.000Z_
######  Diff: [`f9caf87...e09b046`](https://github.com/ChromeDevTools/devtools-protocol/compare/f9caf87...e09b046)

```diff
@@ browser_protocol.pdl:2207 @@ experimental domain CSS
       optional array of CSSKeyframesRule cssKeyframesRules
       # A list of CSS position fallbacks matching this node.
       deprecated optional array of CSSPositionFallbackRule cssPositionFallbackRules
-      # A list of CSS @position-try rules matching this node, based on the position-try-options property.
+      # A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property.
       optional array of CSSPositionTryRule cssPositionTryRules
       # A list of CSS at-property rules matching this node.
       optional array of CSSPropertyRule cssPropertyRules
```

## Roll protocol to r1323165 — _2024-07-04T04:27:18.000Z_
######  Diff: [`98a6075...f9caf87`](https://github.com/ChromeDevTools/devtools-protocol/compare/98a6075...f9caf87)

```diff
@@ browser_protocol.pdl:2031 @@ experimental domain CSS
       StyleSheetOrigin origin
       # Associated style declaration.
       CSSStyle style
+      boolean active
 
   # CSS keyframes rule representation.
   type CSSKeyframesRule extends object
```
