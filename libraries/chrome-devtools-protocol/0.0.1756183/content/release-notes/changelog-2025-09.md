# Chrome DevTools Protocol changelog — 2025-09

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-09, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1521046 — _2025-09-26T04:31:48.000Z_
######  Diff: [`e3b838c...f6820b4`](https://github.com/ChromeDevTools/devtools-protocol/compare/e3b838c...f6820b4)

```diff
@@ domains/CSS.pdl:165 @@ experimental domain CSS
       StyleSheetOrigin origin
       # Associated style declaration.
       CSSStyle style
+      # The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule.
+      experimental optional DOM.BackendNodeId originTreeScopeNodeId
       # Media list array (for rules involving media queries). The array enumerates media queries
       # starting with the innermost one, going outwards.
       optional array of CSSMedia media
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index 5c4e1302..973259c0 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -239,12 +239,21 @@ experimental domain Storage
       StorageBucketsDurability durability
 
   # Returns a storage key given a frame id.
-  command getStorageKeyForFrame
+  # Deprecated. Please use Storage.getStorageKey instead.
+  deprecated command getStorageKeyForFrame
     parameters
       Page.FrameId frameId
     returns
       SerializedStorageKey storageKey
 
+  # Returns storage key for the given frame. If no frame ID is provided,
+  # the storage key of the target executing this command is returned.
+  experimental command getStorageKey
+    parameters
+      optional Page.FrameId frameId
+    returns
+      SerializedStorageKey storageKey
+
   # Clears storage for origin.
   command clearDataForOrigin
     parameters
```

## Roll protocol to r1519099 — _2025-09-23T04:31:20.000Z_
######  Diff: [`78aae66...e3b838c`](https://github.com/ChromeDevTools/devtools-protocol/compare/78aae66...e3b838c)

```diff
@@ domains/Page.pdl:1768 @@ domain Page
   experimental command setPrerenderingAllowed
     parameters
       boolean isAllowed
-
-  # Enable/disable prewarming triggers manually.
-  #
-  # This command manages DSE Prewarming triggers. While a client is connected,
-  # prewarming triggers are disabled by default. This command can change this
-  # default behavior to allow the triggers, or to disallow them again.
-  # See https://chromestatus.com/feature/6266608741908480 for more details on
-  # the DSE Prewarming feature.
-  experimental command setPrewarmingAllowed
-    parameters
-      boolean isAllowed
```

## Roll protocol to r1518305 — _2025-09-20T04:30:57.000Z_
######  Diff: [`418ab00...78aae66`](https://github.com/ChromeDevTools/devtools-protocol/compare/418ab00...78aae66)

```diff
@@ domains/Network.pdl:1087 @@ domain Network
   # Disables network tracking, prevents network events from being sent to the client.
   command disable
 
-  # Activates emulation of network conditions.
-  command emulateNetworkConditions
+  experimental type NetworkConditions extends object
+    properties
+      # Only matching requests will be affected by these conditions. Patterns use the URLPattern constructor string
+      # syntax (https://urlpattern.spec.whatwg.org/). If the pattern is empty, all requests are matched (including p2p
+      # connections).
+      string urlPattern
+      # Minimum latency from request sent to response headers received (ms).
+      number latency
+      # Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
+      number downloadThroughput
+      # Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
+      number uploadThroughput
+      # Connection type if known.
+      optional ConnectionType connectionType
+      # WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets.
+      optional number packetLoss
+      # WebRTC packet queue length (packet). 0 removes any queue length limitations.
+      optional integer packetQueueLength
+      # WebRTC packetReordering feature.
+      optional boolean packetReordering
+
+  # Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
+  # and overrideNetworkState commands, which can be used together to the same effect.
+  deprecated command emulateNetworkConditions
     parameters
       # True to emulate internet disconnection.
       boolean offline
@@ -1107,6 +1129,34 @@ domain Network
       # WebRTC packetReordering feature.
       experimental optional boolean packetReordering
 
+  # Activates emulation of network conditions for individual requests using URL match patterns.
+  experimental command emulateNetworkConditionsByRule
+    parameters
+      # True to emulate internet disconnection.
+      boolean offline
+      # Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global
+      # conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are
+      # also applied for throttling of p2p connections.
+      array of NetworkConditions matchedNetworkConditions
+    returns
+      # An id for each entry in matchedNetworkConditions. The id will be included in the requestWillBeSentExtraInfo for
+      # requests affected by a rule.
+      array of string ruleIds
+
+  # Override the state of navigator.onLine and navigator.connection.
+  experimental command overrideNetworkState
+    parameters
+      # True to emulate internet disconnection.
+      boolean offline
+      # Minimum latency from request sent to response headers received (ms).
+      number latency
+      # Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
+      number downloadThroughput
+      # Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
+      number uploadThroughput
+      # Connection type if known.
+      optional ConnectionType connectionType
+
   # Enables network tracking, network events will now be delivered to the client.
   command enable
     parameters
@@ -1776,6 +1826,9 @@ domain Network
       optional ClientSecurityState clientSecurityState
       # Whether the site has partitioned cookies stored in a partition different than the current one.
       optional boolean siteHasCookieInOtherPartition
+      # The network conditions id if this request was affected by network conditions configured via
+      # emulateNetworkConditionsByRule.
+      optional string appliedNetworkConditionsId
 
   # Fired when additional information about a responseReceived event is available from the network
   # stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
```

## Roll protocol to r1517051 — _2025-09-18T04:31:09.000Z_
######  Diff: [`86cf20a...418ab00`](https://github.com/ChromeDevTools/devtools-protocol/compare/86cf20a...418ab00)

```diff
@@ domains/Audits.pdl:309 @@ experimental domain Audits
       WriteErrorInsufficientResources
       WriteErrorInvalidMatchField
       WriteErrorInvalidStructuredHeader
+      WriteErrorInvalidTTLField
       WriteErrorNavigationRequest
       WriteErrorNoMatchField
+      WriteErrorNonIntegerTTLField
       WriteErrorNonListMatchDestField
       WriteErrorNonSecureContext
       WriteErrorNonStringIdField
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index c1708696..bc07b8a2 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1768,3 +1768,14 @@ domain Page
   experimental command setPrerenderingAllowed
     parameters
       boolean isAllowed
+
+  # Enable/disable prewarming triggers manually.
+  #
+  # This command manages DSE Prewarming triggers. While a client is connected,
+  # prewarming triggers are disabled by default. This command can change this
+  # default behavior to allow the triggers, or to disallow them again.
+  # See https://chromestatus.com/feature/6266608741908480 for more details on
+  # the DSE Prewarming feature.
+  experimental command setPrewarmingAllowed
+    parameters
+      boolean isAllowed
```

## Roll protocol to r1516431 — _2025-09-17T04:30:57.000Z_
######  Diff: [`0cac6fd...86cf20a`](https://github.com/ChromeDevTools/devtools-protocol/compare/0cac6fd...86cf20a)

```diff
@@ domains/Network.pdl:211 @@ domain Network
       # True if this resource request is considered to be the 'same site' as the
       # request corresponding to the main frame.
       experimental optional boolean isSameSite
+      # True when the resource request is ad-related.
+      experimental optional boolean isAdRelated
 
   # Details of a signed certificate timestamp (SCT).
   type SignedCertificateTimestamp extends object
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 4a386334..bc86332d 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -1142,6 +1142,8 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        # blink's subtypes.
+        trustedtype
       # Object class (constructor) name. Specified for `object` type values only.
       optional string className
       # Remote object value in case of primitive values or JSON values (if it was requested).
@@ -1203,6 +1205,8 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        # blink's subtypes.
+        trustedtype
       # String representation of the object.
       optional string description
       # True iff some of the properties or entries of the original object did not fit.
@@ -1252,6 +1256,8 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        # blink's subtypes.
+        trustedtype
 
   experimental type EntryPreview extends object
     properties
```

## Roll protocol to r1515996 — _2025-09-16T13:32:58.000Z_
######  Diff: [`54189ca...0cac6fd`](https://github.com/ChromeDevTools/devtools-protocol/compare/54189ca...0cac6fd)

```diff
@@ domains/Network.pdl:622 @@ domain Network
       # Cookie path.
       string path
       # Cookie expiration date as the number of seconds since the UNIX epoch.
+      # The value is set to -1 if the expiry date is not set.
+      # The value can be null for values that cannot be represented in
+      # JSON (±Inf).
       number expires
       # Cookie size.
       integer size
```

## Roll protocol to r1515189 — _2025-09-13T04:29:50.000Z_
######  Diff: [`0dba65c...262032f`](https://github.com/ChromeDevTools/devtools-protocol/compare/0dba65c...262032f)

```diff
@@ domains/IndexedDB.pdl:159 @@ experimental domain IndexedDB
       string databaseName
       # Object store name.
       string objectStoreName
-      # Index name, empty string for object store data requests.
-      string indexName
+      # Index name. If not specified, it performs an object store data request.
+      optional string indexName
       # Number of records to skip.
       integer skipCount
       # Number of records to fetch.
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index c9c966b6..c1708696 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1577,8 +1577,10 @@ domain Page
       WebXR
       SharedWorker
       SharedWorkerMessage
+      SharedWorkerWithNoActiveClient
       WebLocks
       WebHID
+      WebBluetooth
       WebShare
       RequestedStorageAccessGrant
       WebNfc
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 73da9149..4a386334 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -794,6 +794,8 @@ experimental domain HeapProfiler
       # Average sample interval in bytes. Poisson distribution is used for the intervals. The
       # default value is 32768 bytes.
       optional number samplingInterval
+      # Maximum stack depth. The default value is 128.
+      optional number stackDepth
       # By default, the sampling heap profiler reports only objects which are
       # still alive when the profile is returned via getSamplingProfile or
       # stopSampling, which is useful for determining what functions contribute
```

## Roll protocol to r1514079 — _2025-09-11T04:31:06.000Z_
######  Diff: [`60a842d...0dba65c`](https://github.com/ChromeDevTools/devtools-protocol/compare/60a842d...0dba65c)

```diff
@@ domains/Accessibility.pdl:110 @@ experimental domain Accessibility
   # - from 'live' to 'root': attributes which apply to nodes in live regions
   # - from 'autocomplete' to 'valuetext': attributes which apply to widgets
   # - from 'checked' to 'selected': states which apply to widgets
-  # - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
+  # - from 'activedescendant' to 'owns': relationships between elements other than parent/child/sibling
+  # - from 'activeFullscreenElement' to 'uninteresting': reasons why this noode is hidden
   type AXPropertyName extends string
     enum
       actions
@@ -154,6 +155,25 @@ experimental domain Accessibility
       labelledby
       owns
       url
+      # LINT.IfChange(AXIgnoredReason)
+      activeFullscreenElement
+      activeModalDialog
+      activeAriaModalDialog
+      ariaHiddenElement
+      ariaHiddenSubtree
+      emptyAlt
+      emptyText
+      inertElement
+      inertSubtree
+      labelContainer
+      labelFor
+      notRendered
+      notVisible
+      presentationalRole
+      probablyPresentational
+      inactiveCarouselTabContent
+      uninteresting
+      # LINT.ThenChange(//third_party/blink/renderer/modules/accessibility/ax_enums.cc:AXIgnoredReason)
 
   # A node in the accessibility tree.
   type AXNode extends object
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 5a16c329..71a50b6f 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -177,6 +177,7 @@ domain DOM
       optional CompatibilityMode compatibilityMode
       optional BackendNode assignedSlot
       experimental optional boolean isScrollable
+      experimental optional boolean affectedByStartingStyles
 
   # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
   type DetachedElementInfo extends object
@@ -898,6 +899,14 @@ domain DOM
       # If the node is scrollable.
       boolean isScrollable
 
+  # Fired when a node's starting styles changes.
+  experimental event affectedByStartingStylesFlagUpdated
+    parameters
+      # The id of the node.
+      DOM.NodeId nodeId
+      # If the node has starting styles.
+      boolean affectedByStartingStyles
+
   # Called when a pseudo element is removed from an element.
   experimental event pseudoElementRemoved
     parameters
```

## Roll protocol to r1512837 — _2025-09-09T04:31:23.000Z_
######  Diff: [`f2eea64...60a842d`](https://github.com/ChromeDevTools/devtools-protocol/compare/f2eea64...60a842d)

```diff
@@ domains/Preload.pdl:40 @@ experimental domain Preload
       optional RuleSetErrorType errorType
       # TODO(https://crbug.com/1425354): Replace this property with structured error.
       deprecated optional string errorMessage
+      # For more details, see:
+      # https://github.com/WICG/nav-speculation/blob/main/speculation-rules-tags.md
+      optional string tag
 
   type RuleSetErrorType extends string
     enum
```

## Roll protocol to r1511308 — _2025-09-05T04:31:05.000Z_
######  Diff: [`bb9208f...f2eea64`](https://github.com/ChromeDevTools/devtools-protocol/compare/bb9208f...f2eea64)

```diff
@@ domains/PWA.pdl:53 @@ experimental domain PWA
   #
   # To generate bundle id for proxy mode:
   # 1. Generate 32 random bytes.
-  # 2. Add a specific suffix 0x00 at the end.
+  # 2. Add a specific suffix at the end following the documentation
+  #    https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix
   # 3. Encode the entire sequence using Base32 without padding.
   #
   # If Chrome is not in IWA dev
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index c713e453..c9c966b6 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -140,6 +140,7 @@ domain Page
       digital-credentials-create
       digital-credentials-get
       direct-sockets
+      direct-sockets-multicast
       direct-sockets-private
       display-capture
       document-domain
```

## Roll protocol to r1510116 — _2025-09-03T09:48:36.000Z_
######  Diff: [`1ad29d6...bb9208f`](https://github.com/ChromeDevTools/devtools-protocol/compare/1ad29d6...bb9208f)

```diff
@@ domains/Autofill.pdl:22 @@ experimental domain Autofill
   type AddressField extends object
     properties
       # address field name, for example GIVEN_NAME.
+      # The full list of supported field names:
+      # https://source.chromium.org/chromium/chromium/src/+/main:components/autofill/core/browser/field_types.cc;l=38
       string name
       # address field value, for example Jon Doe.
       string value
@@ -90,8 +92,10 @@ experimental domain Autofill
       DOM.BackendNodeId fieldId
       # Identifies the frame that field belongs to.
       optional Page.FrameId frameId
-      # Credit card information to fill out the form. Credit card data is not saved.
-      CreditCard card
+      # Credit card information to fill out the form. Credit card data is not saved.  Mutually exclusive with `address`.
+      optional CreditCard card
+      # Address to fill out the form. Address data is not saved. Mutually exclusive with `card`.
+      optional Address address
 
   # Set addresses so that developers can verify their forms implementation.
   command setAddresses
```

## Roll protocol to r1510016 — _2025-09-03T04:31:02.000Z_
######  Diff: [`32c4fdb...1ad29d6`](https://github.com/ChromeDevTools/devtools-protocol/compare/32c4fdb...1ad29d6)

```diff
@@ domains/Network.pdl:315 @@ domain Network
       # Whether IP proxy is available
       IpProxyStatus status
 
+  # Sets bypass IP Protection Proxy boolean.
+  experimental command setIPProtectionProxyBypassEnabled
+    parameters
+      # Whether IP Proxy is being bypassed by devtools; false by default.
+      boolean enabled
+
   # The reason why request was blocked.
   type CorsError extends string
     enum
```

## Roll protocol to r1509355 — _2025-09-02T04:31:52.000Z_
######  Diff: [`ede3fcf...32c4fdb`](https://github.com/ChromeDevTools/devtools-protocol/compare/ede3fcf...32c4fdb)

```diff
@@ domains/Page.pdl:1600 @@ domain Page
       IndexedDBEvent
       Dummy
       JsNetworkRequestReceivedCacheControlNoStoreResource
-      WebRTCSticky
-      WebTransportSticky
-      WebSocketSticky
+      WebRTCUsedWithCCNS
+      WebTransportUsedWithCCNS
+      WebSocketUsedWithCCNS
       SmartCard
       LiveMediaStreamTrack
       UnloadHandler
```
