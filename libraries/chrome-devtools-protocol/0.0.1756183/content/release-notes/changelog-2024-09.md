# Chrome DevTools Protocol changelog — 2024-09

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-09, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1359167 — _2024-09-24T04:29:20.000Z_
######  Diff: [`a615266...5ce3c3b`](https://github.com/ChromeDevTools/devtools-protocol/compare/a615266...5ce3c3b)

```diff
@@ js_protocol.pdl:606 @@ domain Debugger
     properties
       # Type of the debug symbols.
       enum type
-        None
         SourceMap
         EmbeddedDWARF
         ExternalDWARF
@@ -689,8 +688,8 @@ domain Debugger
       experimental optional integer codeOffset
       # The language of the script.
       experimental optional Debugger.ScriptLanguage scriptLanguage
-      # If the scriptLanguage is WebASsembly, the source of debug symbols for the module.
-      experimental optional Debugger.DebugSymbols debugSymbols
+      # If the scriptLanguage is WebAssembly, the source of debug symbols for the module.
+      experimental optional array of Debugger.DebugSymbols debugSymbols
       # The name the embedder supplied for this script.
       experimental optional string embedderName
```

## Roll protocol to r1358005 — _2024-09-20T04:28:44.000Z_
######  Diff: [`e6861d4...a615266`](https://github.com/ChromeDevTools/devtools-protocol/compare/e6861d4...a615266)

```diff
@@ browser_protocol.pdl:8090 @@ domain Page
       deferred-fetch
       digital-credentials-get
       direct-sockets
+      direct-sockets-private
       display-capture
       document-domain
       encrypted-media
```

## Roll protocol to r1356896 — _2024-09-18T04:29:10.000Z_
######  Diff: [`67ed36c...e6861d4`](https://github.com/ChromeDevTools/devtools-protocol/compare/67ed36c...e6861d4)

```diff
@@ browser_protocol.pdl:7925 @@ experimental domain Overlay
       # True for showing hit-test borders
       boolean show
 
-  # Request that backend shows an overlay with web vital metrics.
-  command setShowWebVitals
+  # Deprecated, no longer has any effect.
+  deprecated command setShowWebVitals
     parameters
       boolean show
```

## Roll protocol to r1356270 — _2024-09-17T04:27:33.000Z_
######  Diff: [`ecd57f9...67ed36c`](https://github.com/ChromeDevTools/devtools-protocol/compare/ecd57f9...67ed36c)

```diff
@@ browser_protocol.pdl:532 @@ experimental domain Audits
       WarnDomainNonASCII
       WarnThirdPartyPhaseout
       WarnCrossSiteRedirectDowngradeChangesInclusion
+      WarnDeprecationTrialMetadata
+      WarnThirdPartyCookieHeuristic
 
   type CookieOperation extends string
     enum
@@ -4221,7 +4223,6 @@ domain Emulation
       gyroscope
       linear-acceleration
       magnetometer
-      proximity
       relative-orientation
 
   experimental type SensorMetadata extends object
```

## Roll protocol to r1354347 — _2024-09-12T04:29:25.000Z_
######  Diff: [`5257185...ecd57f9`](https://github.com/ChromeDevTools/devtools-protocol/compare/5257185...ecd57f9)

```diff
@@ browser_protocol.pdl:2679 @@ domain DOM
       after
       marker
       backdrop
+      column
       selection
       search-text
       target-text
```

## Roll protocol to r1352404 — _2024-09-07T04:28:15.000Z_
######  Diff: [`ea79b5d...5257185`](https://github.com/ChromeDevTools/devtools-protocol/compare/ea79b5d...5257185)

```diff
@@ browser_protocol.pdl:6385 @@ domain Network
       StorageAccess
       # The cookie should have been blocked by 3PCD but is exempted by Top-level Storage Access API.
       TopLevelStorageAccess
-      # The cookie should have been blocked by 3PCD but is exempted by CORS opt-in.
-      CorsOptIn
       # The cookie should have been blocked by 3PCD but is exempted by the first-party URL scheme.
       Scheme
```

## Roll protocol to r1351223 — _2024-09-05T04:28:35.000Z_
######  Diff: [`81b9407...ea79b5d`](https://github.com/ChromeDevTools/devtools-protocol/compare/81b9407...ea79b5d)

```diff
@@ browser_protocol.pdl:2703 @@ domain DOM
       view-transition-image-pair
       view-transition-old
       view-transition-new
+      placeholder
+      file-selector-button
+      details-content
+      select-fallback-button
+      select-fallback-button-text
+      picker
 
   # Shadow root type.
   type ShadowRootType extends string
@@ -8079,6 +8085,7 @@ domain Page
       clipboard-read
       clipboard-write
       compute-pressure
+      controlled-frame
       cross-origin-isolated
       deferred-fetch
       digital-credentials-get
```

## Roll protocol to r1349977 — _2024-09-03T04:28:26.000Z_
######  Diff: [`c79610f...81b9407`](https://github.com/ChromeDevTools/devtools-protocol/compare/c79610f...81b9407)

```diff
@@ browser_protocol.pdl:2807 @@ domain DOM
       optional boolean isSVG
       optional CompatibilityMode compatibilityMode
       optional BackendNode assignedSlot
+      experimental optional boolean isScrollable
 
   # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
   type DetachedElementInfo extends object
@@ -3496,6 +3497,14 @@ domain DOM
   # Called when top layer elements are changed.
   experimental event topLayerElementsUpdated
 
+  # Fired when a node's scrollability state changes.
+  experimental event scrollableFlagUpdated
+    parameters
+      # The id of the node.
+      DOM.NodeId nodeId
+      # If the node is scrollable.
+      boolean isScrollable
+
   # Called when a pseudo element is removed from an element.
   experimental event pseudoElementRemoved
     parameters
```
