# Chrome DevTools Protocol changelog — 2024-03

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-03, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1280070 — _2024-03-29T04:26:49.000Z_
######  Diff: [`dce7d35...a0b1761`](https://github.com/ChromeDevTools/devtools-protocol/compare/dce7d35...a0b1761)

```diff
@@ browser_protocol.pdl:4159 @@ domain Emulation
       experimental optional DisplayFeature displayFeature
       # If set, the posture of a foldable device. If not set the posture is set
       # to continuous.
-      experimental optional DevicePosture devicePosture
+      # Deprecated, use Emulation.setDevicePostureOverride.
+      experimental deprecated optional DevicePosture devicePosture
+
+  # Start reporting the given posture value to the Device Posture API.
+  # This override can also be set in setDeviceMetricsOverride().
+  experimental command setDevicePostureOverride
+    parameters
+      DevicePosture posture
+
+  # Clears a device posture override set with either setDeviceMetricsOverride()
+  # or setDevicePostureOverride() and starts using posture information from the
+  # platform again.
+  # Does nothing if no override is set.
+  experimental command clearDevicePostureOverride
 
   experimental command setScrollbarsHidden
     parameters
@@ -5817,6 +5830,8 @@ domain Network
       optional boolean fromServiceWorker
       # Specifies that the request was served from the prefetch cache.
       optional boolean fromPrefetchCache
+      # Specifies that the request was served from the prefetch cache.
+      optional boolean fromEarlyHints
       # Information about how Service Worker Static Router was used.
       experimental optional ServiceWorkerRouterInfo serviceWorkerRouterInfo
       # Total number of bytes received for this request so far.
```
