# Chrome DevTools Protocol changelog — 2025-10

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-10, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1537100 — _2025-10-29T04:32:32.000Z_
######  Diff: [`604a9f6...b8a7fa7`](https://github.com/ChromeDevTools/devtools-protocol/compare/604a9f6...b8a7fa7)

```diff
@@ domains/SystemInfo.pdl:74 @@ experimental domain SystemInfo
       webp
       unknown
 
-  # Describes a supported image decoding profile with its associated minimum and
-  # maximum resolutions and subsampling.
-  type ImageDecodeAcceleratorCapability extends object
-    properties
-      # Image coded, e.g. Jpeg.
-      ImageType imageType
-      # Maximum supported dimensions of the image in pixels.
-      Size maxDimensions
-      # Minimum supported dimensions of the image in pixels.
-      Size minDimensions
-      # Optional array of supported subsampling formats, e.g. 4:2:0, if known.
-      array of SubsamplingFormat subsamplings
-
   # Provides information about the GPU(s) on the system.
   type GPUInfo extends object
     properties
@@ -102,8 +89,6 @@ experimental domain SystemInfo
       array of VideoDecodeAcceleratorCapability videoDecoding
       # Supported accelerated video encoding capabilities.
       array of VideoEncodeAcceleratorCapability videoEncoding
-      # Supported accelerated image decoding capabilities.
-      array of ImageDecodeAcceleratorCapability imageDecoding
 
   # Represents process info.
   type ProcessInfo extends object
```

## Roll protocol to r1534754 — _2025-10-24T04:31:25.000Z_
######  Diff: [`d2b130f...604a9f6`](https://github.com/ChromeDevTools/devtools-protocol/compare/d2b130f...604a9f6)

```diff
@@ domains/Network.pdl:1929 @@ domain Network
   # Fired once security policy has been updated.
   experimental event policyUpdated
 
-  # Fired once when parsing the .wbn file has succeeded.
-  # The event contains the information about the web bundle contents.
-  experimental event subresourceWebBundleMetadataReceived
-    parameters
-      # Request identifier. Used to match this information to another event.
-      RequestId requestId
-      # A list of URLs of resources in the subresource Web Bundle.
-      array of string urls
-
-  # Fired once when parsing the .wbn file has failed.
-  experimental event subresourceWebBundleMetadataError
-    parameters
-      # Request identifier. Used to match this information to another event.
-      RequestId requestId
-      # Error message
-      string errorMessage
-
-  # Fired when handling requests for resources within a .wbn file.
-  # Note: this will only be fired for resources that are requested by the webpage.
-  experimental event subresourceWebBundleInnerResponseParsed
-    parameters
-      # Request identifier of the subresource request
-      RequestId innerRequestId
-      # URL of the subresource resource.
-      string innerRequestURL
-      # Bundle request identifier. Used to match this information to another event.
-      # This made be absent in case when the instrumentation was enabled only
-      # after webbundle was parsed.
-      optional RequestId bundleRequestId
-
-  # Fired when request for resources within a .wbn file failed.
-  experimental event subresourceWebBundleInnerResponseError
-    parameters
-      # Request identifier of the subresource request
-      RequestId innerRequestId
-      # URL of the subresource resource.
-      string innerRequestURL
-      # Error message
-      string errorMessage
-      # Bundle request identifier. Used to match this information to another event.
-      # This made be absent in case when the instrumentation was enabled only
-      # after webbundle was parsed.
-      optional RequestId bundleRequestId
-
   experimental type CrossOriginOpenerPolicyValue extends string
     enum
       SameOrigin
```

## Roll protocol to r1532728 — _2025-10-21T04:31:48.000Z_
######  Diff: [`b7cda17...d2b130f`](https://github.com/ChromeDevTools/devtools-protocol/compare/b7cda17...d2b130f)

```diff
@@ domains/Inspector.pdl:23 @@ experimental domain Inspector
 
   # Fired when debugging target has reloaded after crash
   event targetReloadedAfterCrash
+
+  # Fired on worker targets when main worker script and any imported scripts have been evaluated.
+  experimental event workerScriptLoaded
```

## Roll protocol to r1528500 — _2025-10-11T04:30:26.000Z_
######  Diff: [`7c74e7d...b4246f2`](https://github.com/ChromeDevTools/devtools-protocol/compare/7c74e7d...b4246f2)

```diff
@@ domains/Network.pdl:587 @@ domain Network
         preload
         SignedExchange
         preflight
+        FedCM
         other
       # Initiator JavaScript stack trace, set for Script only.
       # Requires the Debugger domain to be enabled.
```

## Roll protocol to r1527314 — _2025-10-09T04:31:34.000Z_
######  Diff: [`9f2ed89...7c74e7d`](https://github.com/ChromeDevTools/devtools-protocol/compare/9f2ed89...7c74e7d)

```diff
@@ domains/Network.pdl:1267 @@ domain Network
       # List of search matches.
       array of Debugger.SearchMatch result
 
+  experimental type BlockPattern extends object
+    properties
+      # URL pattern to match. Patterns use the URLPattern constructor string syntax
+      # (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: `*://*:*/*.css`.
+      string urlPattern
+      # Whether or not to block the pattern. If false, a matching request will not be blocked even if it matches a later
+      # `BlockPattern`.
+      boolean block
+
   # Blocks URLs from loading.
   experimental command setBlockedURLs
     parameters
-      # URL patterns to block. Patterns use the URLPattern constructor string syntax
-      # (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: `*://*:*/*.css`.
-      optional array of string urlPatterns
+      # Patterns to match in the order in which they are given. These patterns
+      # also take precedence over any wildcard patterns defined in `urls`.
+      optional array of BlockPattern urlPatterns
       # URL patterns to block. Wildcards ('*') are allowed.
       deprecated optional array of string urls
```

## Roll protocol to r1526665 — _2025-10-08T04:31:07.000Z_
######  Diff: [`0d43ecd...9f2ed89`](https://github.com/ChromeDevTools/devtools-protocol/compare/0d43ecd...9f2ed89)

```diff
@@ domains/Network.pdl:1129 @@ domain Network
       # WebRTC packetReordering feature.
       experimental optional boolean packetReordering
 
-  # Activates emulation of network conditions for individual requests using URL match patterns.
+  # Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated
+  # Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to
+  # explicitly modify `navigator` behavior.
   experimental command emulateNetworkConditionsByRule
     parameters
       # True to emulate internet disconnection.
```

## Roll protocol to r1526016 — _2025-10-07T04:31:13.000Z_
######  Diff: [`a73a111...0d43ecd`](https://github.com/ChromeDevTools/devtools-protocol/compare/a73a111...0d43ecd)

```diff
@@ domains/Browser.pdl:103 @@ domain Browser
       closeTabSearch
       openGlic
 
-  # Set permission settings for given requesting and embedding origins.
+  # Set permission settings for given embedding and embedded origins.
   experimental command setPermission
     parameters
       # Descriptor of permission to override.
       PermissionDescriptor permission
       # Setting of the permission.
       PermissionSetting setting
-      # Requesting origin the permission applies to, all origins if not specified.
+      # Embedding origin the permission applies to, all origins if not specified.
       optional string origin
-      # Embedding origin the permission applies to. It is ignored unless the requesting origin is
-      # present and valid. If the requesting origin is provided but the embedding origin isn't, the
-      # requesting origin is used as the embedding origin.
-      optional string embeddingOrigin
+      # Embedded origin the permission applies to. It is ignored unless the embedding origin is
+      # present and valid. If the embedding origin is provided but the embedded origin isn't, the
+      # embedding origin is used as the embedded origin.
+      optional string embeddedOrigin
       # Context to override. When omitted, default browser context is used.
       optional BrowserContextID browserContextId
 
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 03538feb..c2cdeb1b 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -1090,8 +1090,8 @@ domain Network
   experimental type NetworkConditions extends object
     properties
       # Only matching requests will be affected by these conditions. Patterns use the URLPattern constructor string
-      # syntax (https://urlpattern.spec.whatwg.org/). If the pattern is empty, all requests are matched (including p2p
-      # connections).
+      # syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. If the pattern is empty, all requests are
+      # matched (including p2p connections).
       string urlPattern
       # Minimum latency from request sent to response headers received (ms).
       number latency
@@ -1269,7 +1269,7 @@ domain Network
   experimental command setBlockedURLs
     parameters
       # URL patterns to block. Patterns use the URLPattern constructor string syntax
-      # (https://urlpattern.spec.whatwg.org/). Example: `*://*:*/*.css`.
+      # (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: `*://*:*/*.css`.
       optional array of string urlPatterns
       # URL patterns to block. Wildcards ('*') are allowed.
       deprecated optional array of string urls
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index fd3222ab..8e9c8a2e 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -57,6 +57,7 @@ experimental domain Preload
     enum
       Prefetch
       Prerender
+      PrerenderUntilScript
 
   # Corresponds to mojom::SpeculationTargetHint.
   # See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
```

## Roll protocol to r1525085 — _2025-10-03T23:52:47.000Z_
######  Diff: [`34e1e23...a73a111`](https://github.com/ChromeDevTools/devtools-protocol/compare/34e1e23...a73a111)

```diff
@@ domains/Browser.pdl:119 @@ domain Browser
       # Context to override. When omitted, default browser context is used.
       optional BrowserContextID browserContextId
 
-  # Grant specific permissions to the given origin and reject all others.
-  experimental command grantPermissions
+  # Grant specific permissions to the given origin and reject all others. Deprecated. Use
+  # setPermission instead.
+  experimental deprecated command grantPermissions
     parameters
       array of PermissionType permissions
       # Origin the permission applies to, all origins if not specified.
```

## Roll protocol to r1523998 — _2025-10-02T04:30:37.000Z_
######  Diff: [`8570f86...edeffc1`](https://github.com/ChromeDevTools/devtools-protocol/compare/8570f86...edeffc1)

```diff
@@ domains/Network.pdl:1268 @@ domain Network
   # Blocks URLs from loading.
   experimental command setBlockedURLs
     parameters
+      # URL patterns to block. Patterns use the URLPattern constructor string syntax
+      # (https://urlpattern.spec.whatwg.org/). Example: `*://*:*/*.css`.
+      optional array of string urlPatterns
       # URL patterns to block. Wildcards ('*') are allowed.
-      array of string urls
+      deprecated optional array of string urls
 
   # Toggles ignoring of service worker for each request.
   command setBypassServiceWorker
```
