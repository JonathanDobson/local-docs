# Chrome DevTools Protocol changelog — 2025-07

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-07, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1493946 — _2025-07-30T04:34:37.000Z_
######  Diff: [`868b942...7de76fa`](https://github.com/ChromeDevTools/devtools-protocol/compare/868b942...7de76fa)

```diff
@@ browser_protocol.pdl:2134 @@ experimental domain CSS
       optional DOM.LogicalAxes logicalAxes
       # true if the query contains scroll-state() queries.
       optional boolean queriesScrollState
+      # true if the query contains anchored() queries.
+      optional boolean queriesAnchored
 
   # CSS Supports at-rule descriptor.
   experimental type CSSSupports extends object
@@ -3717,9 +3719,9 @@ domain DOM
 
   # Returns the query container of the given node based on container query
   # conditions: containerName, physical and logical axes, and whether it queries
-  # scroll-state. If no axes are provided and queriesScrollState is false, the
-  # style container is returned, which is the direct parent or the closest
-  # element with a matching container-name.
+  # scroll-state or anchored elements. If no axes are provided and
+  # queriesScrollState is false, the style container is returned, which is the
+  # direct parent or the closest element with a matching container-name.
   experimental command getContainerForNode
     parameters
       NodeId nodeId
@@ -3727,6 +3729,7 @@ domain DOM
       optional PhysicalAxes physicalAxes
       optional LogicalAxes logicalAxes
       optional boolean queriesScrollState
+      optional boolean queriesAnchored
     returns
       # The container node for the given node, or null if not found.
       optional NodeId nodeId
@@ -13245,6 +13248,7 @@ experimental domain Preload
       V8OptimizerDisabled
       PrerenderFailedDuringPrefetch
       BrowsingDataRemoved
+      PrerenderHostReused
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1491235 — _2025-07-24T04:34:08.000Z_
######  Diff: [`87144ce...41692aa`](https://github.com/ChromeDevTools/devtools-protocol/compare/87144ce...41692aa)

```diff
@@ browser_protocol.pdl:6362 @@ domain Network
       # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
       PrivateNetworkAccessPermissionDenied
       # Request was a local network request and is denied by user permission.
-      # https://github.com/explainers-by-googlers/local-network-access
+      # https://wicg.github.io/local-network-access/
       LocalNetworkAccessPermissionDenied
 
   type CorsErrorStatus extends object
```

## Roll protocol to r1490591 — _2025-07-23T04:34:18.000Z_
######  Diff: [`4819069...87144ce`](https://github.com/ChromeDevTools/devtools-protocol/compare/4819069...87144ce)

```diff
@@ browser_protocol.pdl:6508 @@ domain Network
       Security.SecurityState securityState
       # Security details for the request.
       optional SecurityDetails securityDetails
+      # Indicates whether the request was sent through IP Protection proxies. If
+      # set to true, the request used the IP Protection privacy feature.
+      experimental optional boolean isIpProtectionUsed
 
   # WebSocket request data.
   type WebSocketRequest extends object
```

## Roll protocol to r1488636 — _2025-07-18T04:33:56.000Z_
######  Diff: [`1103fe1...4819069`](https://github.com/ChromeDevTools/devtools-protocol/compare/1103fe1...4819069)

```diff
@@ browser_protocol.pdl:7711 @@ domain Network
   experimental type IPAddressSpace extends string
     enum
       Loopback
-      Private
+      Local
       Public
       Unknown
 
@@ -13103,6 +13103,7 @@ experimental domain Preload
     enum
       SourceIsNotJsonObject
       InvalidRulesSkipped
+      InvalidRulesetLevelTag
 
   # The type of preloading attempted. It corresponds to
   # mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it
```

## Roll protocol to r1488040 — _2025-07-17T04:33:47.000Z_
######  Diff: [`15a4967...1103fe1`](https://github.com/ChromeDevTools/devtools-protocol/compare/15a4967...1103fe1)

```diff
@@ browser_protocol.pdl:2559 @@ experimental domain CSS
       # A list of CSS at-function rules referenced by styles of this node.
       experimental optional array of CSSFunctionRule cssFunctionRules
 
+  # Returns the values of the default UA-defined environment variables used in env()
+  experimental command getEnvironmentVariables
+    returns
+      object environmentVariables
+
   # Returns all media queries parsed by the rendering engine.
   command getMediaQueries
     returns
@@ -9447,6 +9452,8 @@ domain Page
       optional Network.LoaderId loaderId
       # User friendly error message, present if and only if navigation has failed.
       optional string errorText
+      # Whether the navigation resulted in a download.
+      experimental optional boolean isDownload
 
   # Navigates current page to the given history entry.
   command navigateToHistoryEntry
```

## Roll protocol to r1487398 — _2025-07-16T04:33:49.000Z_
######  Diff: [`9d397ca...15a4967`](https://github.com/ChromeDevTools/devtools-protocol/compare/9d397ca...15a4967)

```diff
@@ browser_protocol.pdl:3751 @@ domain DOM
       # The anchor element of the given anchor query.
       NodeId nodeId
 
+  # When enabling, this API force-opens the popover identified by nodeId
+  # and keeps it open until disabled.
+  experimental command forceShowPopover
+    parameters
+      # Id of the popover HTMLElement
+      NodeId nodeId
+      # If true, opens the popover and keeps it open. If false, closes the
+      # popover if it was previously force-opened.
+      boolean enable
+    returns
+      # List of popovers that were closed in order to respect popover stacking order.
+      array of NodeId nodeIds
+
   # Fired when `Element`'s attribute is modified.
   event attributeModified
     parameters
```

## Roll protocol to r1485358 — _2025-07-11T04:33:31.000Z_
######  Diff: [`f9dda30...9d397ca`](https://github.com/ChromeDevTools/devtools-protocol/compare/f9dda30...9d397ca)

```diff
@@ browser_protocol.pdl:8609 @@ domain Page
       accelerometer
       all-screens-capture
       ambient-light-sensor
+      aria-notify
       attribution-reporting
       autoplay
       bluetooth
```

## Roll protocol to r1484773 — _2025-07-10T04:32:32.000Z_
######  Diff: [`3952063...f9dda30`](https://github.com/ChromeDevTools/devtools-protocol/compare/3952063...f9dda30)

```diff
@@ browser_protocol.pdl:1748 @@ domain Browser
       # with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
       Bounds bounds
 
+  # Set size of the browser contents resizing browser window as necessary.
+  experimental command setContentsSize
+    parameters
+      # Browser window id.
+      WindowID windowId
+      # The window contents width in DIP. Assumes current width if omitted.
+      # Must be specified if 'height' is omitted.
+      optional integer width
+      # The window contents height in DIP. Assumes current height if omitted.
+      # Must be specified if 'width' is omitted.
+      optional integer height
+
   # Set dock tile details, platform-specific.
   experimental command setDockTile
     parameters
```

## Roll protocol to r1483532 — _2025-07-08T04:32:14.000Z_
######  Diff: [`71d5e25...3952063`](https://github.com/ChromeDevTools/devtools-protocol/compare/71d5e25...3952063)

```diff
@@ browser_protocol.pdl:3386 @@ domain DOM
       optional BackendNodeId backendNodeId
       # JavaScript object id of the node wrapper.
       optional Runtime.RemoteObjectId objectId
+      # Include all shadow roots. Equals to false if not specified.
+      experimental optional boolean includeShadowDOM
     returns
       # Outer HTML markup.
       string outerHTML
@@ -4874,6 +4876,13 @@ domain Emulation
       # Image types to disable.
       array of DisabledImageType imageTypes
 
+
+  # Override the value of navigator.connection.saveData
+  experimental command setDataSaverOverride
+    parameters
+      # Override value. Omitting the parameter disables the override.
+      optional boolean dataSaverEnabled
+
   experimental command setHardwareConcurrencyOverride
     parameters
       # Hardware concurrency to report
```

## Roll protocol to r1481382 — _2025-07-02T04:32:10.000Z_
######  Diff: [`097b400...71d5e25`](https://github.com/ChromeDevTools/devtools-protocol/compare/097b400...71d5e25)

```diff
@@ browser_protocol.pdl:8253 @@ experimental domain Overlay
       searchForNode
       searchForUAShadowDOM
       captureAreaScreenshot
-      showDistances
       none
 
   # Disables domain notifications.
@@ -10639,10 +10638,6 @@ experimental domain ServiceWorker
 
   command enable
 
-  command inspectWorker
-    parameters
-      string versionId
-
   command setForceUpdateOnPageLoad
     parameters
       boolean forceUpdateOnPageLoad
```
