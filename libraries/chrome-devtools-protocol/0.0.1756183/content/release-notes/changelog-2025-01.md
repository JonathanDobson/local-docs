# Chrome DevTools Protocol changelog — 2025-01

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-01, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1413902 — _2025-01-31T04:28:29.000Z_
######  Diff: [`2fef0e4...e55a19d`](https://github.com/ChromeDevTools/devtools-protocol/compare/2fef0e4...e55a19d)

```diff
@@ browser_protocol.pdl:2253 @@ experimental domain CSS
     parameters
       # Identifier of the frame where "via-inspector" stylesheet should be created.
       Page.FrameId frameId
+      # If true, creates a new stylesheet for every call. If false,
+      # returns a stylesheet previously created by a call with force=false
+      # for the frame's document if it exists or creates a new stylesheet
+      # (default: false).
+      optional boolean force
     returns
       # Identifier of the created "via-inspector" stylesheet.
       StyleSheetId styleSheetId
```

## Roll protocol to r1413303 — _2025-01-30T04:28:44.000Z_
######  Diff: [`c026fa6...2fef0e4`](https://github.com/ChromeDevTools/devtools-protocol/compare/c026fa6...2fef0e4)

```diff
@@ browser_protocol.pdl:9396 @@ domain Page
 
   experimental event frameResized
 
+  # Fired when a navigation starts. This event is fired for both
+  # renderer-initiated and browser-initiated navigations. For renderer-initiated
+  # navigations, the event is fired after `frameRequestedNavigation`.
+  # Navigation may still be cancelled after the event is issued. Multiple events
+  # can be fired for a single navigation, for example, when a same-document
+  # navigation becomes a cross-document navigation (such as in the case of a
+  # frameset).
+  experimental event frameStartedNavigating
+    parameters
+      # ID of the frame that is being navigated.
+      FrameId frameId
+      # The URL the navigation started with. The final URL can be different.
+      string url
+      # Loader identifier. Even though it is present in case of same-document
+      # navigation, the previously committed loaderId would not change unless
+      # the navigation changes from a same-document to a cross-document
+      # navigation.
+      Network.LoaderId loaderId
+      enum navigationType
+        reload
+        reloadBypassingCache
+        restore
+        restoreWithPost
+        historySameDocument
+        historyDifferentDocument
+        sameDocument
+        differentDocument
+
   # Fired when a renderer-initiated navigation is requested.
   # Navigation may still be cancelled after the event is issued.
   experimental event frameRequestedNavigation
```

## Roll protocol to r1412693 — _2025-01-29T04:28:28.000Z_
######  Diff: [`2fe675d...c026fa6`](https://github.com/ChromeDevTools/devtools-protocol/compare/2fe675d...c026fa6)

```diff
@@ js_protocol.pdl:564 @@ domain Debugger
       experimental optional array of LocationRange skipList
 
   # Fired when breakpoint is resolved to an actual script and location.
-  event breakpointResolved
+  # Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.
+  deprecated event breakpointResolved
     parameters
       # Breakpoint unique identifier.
       BreakpointId breakpointId
@@ -622,6 +623,13 @@ domain Debugger
       # URL of the external symbol source.
       optional string externalURL
 
+  type ResolvedBreakpoint extends object
+    properties
+      # Breakpoint unique identifier.
+      BreakpointId breakpointId
+      # Actual breakpoint location.
+      Location location
+
   # Fired when virtual machine fails to parse the script.
   event scriptFailedToParse
     parameters
@@ -706,6 +714,10 @@ domain Debugger
       experimental optional array of Debugger.DebugSymbols debugSymbols
       # The name the embedder supplied for this script.
       experimental optional string embedderName
+      # The list of set breakpoints in this script if calls to `setBreakpointByUrl`
+      # matches this script's URL or hash. Clients that use this list can ignore the
+      # `breakpointResolved` event. They are equivalent.
+      experimental optional array of ResolvedBreakpoint resolvedBreakpoints
 
 experimental domain HeapProfiler
   depends on Runtime
@@ -1560,10 +1572,14 @@ domain Runtime
   # It is the total usage of the corresponding isolate not scoped to a particular Runtime.
   experimental command getHeapUsage
     returns
-      # Used heap size in bytes.
+      # Used JavaScript heap size in bytes.
       number usedSize
-      # Allocated heap size in bytes.
+      # Allocated JavaScript heap size in bytes.
       number totalSize
+      # Used size in bytes in the embedder's garbage-collected heap.
+      number embedderHeapUsedSize
+      # Size in bytes of backing storage for array buffers and external strings.
+      number backingStorageSize
 
   # Returns properties of a given object. Object group of the result is inherited from the target
   # object.
```

## Roll protocol to r1410712 — _2025-01-24T04:28:44.000Z_
######  Diff: [`0e9f04b...2fe675d`](https://github.com/ChromeDevTools/devtools-protocol/compare/0e9f04b...2fe675d)

```diff
@@ browser_protocol.pdl:6495 @@ domain Network
       TopLevelStorageAccess
       # The cookie should have been blocked by 3PCD but is exempted by the first-party URL scheme.
       Scheme
+      # The cookie was included due to the 'allow-same-site-none-cookies' value being set in the sandboxing policy.
+      SameSiteNoneCookiesInSandbox
 
   # A cookie which was not stored from a response with the corresponding reason.
   experimental type BlockedSetCookieWithReason extends object
```

## Roll protocol to r1409451 — _2025-01-22T04:28:58.000Z_
######  Diff: [`2ecbfaf...0e9f04b`](https://github.com/ChromeDevTools/devtools-protocol/compare/2ecbfaf...0e9f04b)

```diff
@@ browser_protocol.pdl:10985 @@ experimental domain Storage
     returns
       array of RelatedWebsiteSet sets
 
+  # Returns the list of URLs from a page and its embedded resources that match
+  # existing grace period URL pattern rules.
+  # https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
+  experimental command getAffectedUrlsForThirdPartyCookieMetadata
+    parameters
+      # The URL of the page currently being visited.
+      string firstPartyUrl
+      # The list of embedded resource URLs from the page.
+      array of string thirdPartyUrls
+
+    returns
+      # Array of matching URLs. If there is a primary pattern match for the first-
+      # party URL, only the first-party URL is returned in the array.
+      array of string matchedUrls
+
 # The SystemInfo domain defines methods and events for querying low-level system information.
 experimental domain SystemInfo
```

## Roll protocol to r1406504 — _2025-01-15T04:28:35.000Z_
######  Diff: [`713993e...2ecbfaf`](https://github.com/ChromeDevTools/devtools-protocol/compare/713993e...2ecbfaf)

```diff
@@ browser_protocol.pdl:11174 @@ domain Target
       string host
       integer port
 
+  # The state of the target window.
+  experimental type WindowState extends string
+    enum
+      normal
+      minimized
+      maximized
+      fullscreen
+
   # Activates (focuses) the target.
   command activateTarget
     parameters
@@ -11255,6 +11263,9 @@ domain Target
       optional integer width
       # Frame height in DIP (requires newWindow to be true or headless shell).
       optional integer height
+      # Frame window state (requires newWindow to be true or headless shell).
+      # Default is normal.
+      optional WindowState windowState
       # The browser context to create the page in.
       experimental optional Browser.BrowserContextID browserContextId
       # Whether BeginFrames for this target will be controlled via DevTools (headless shell only,
```

## Roll protocol to r1404580 — _2025-01-10T04:29:07.000Z_
######  Diff: [`e2b4f4f...713993e`](https://github.com/ChromeDevTools/devtools-protocol/compare/e2b4f4f...713993e)

```diff
@@ browser_protocol.pdl:949 @@ experimental domain Audits
       InvalidFieldsSpecified
       RelyingPartyOriginIsOpaque
       TypeNotMatching
+      UiDismissedNoEmbargo
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
@@ -4217,56 +4218,6 @@ experimental domain DOMStorage
     parameters
       StorageId storageId
 
-experimental domain Database
-
-  # Unique identifier of Database object.
-  type DatabaseId extends string
-
-  # Database object.
-  type Database extends object
-    properties
-      # Database ID.
-      DatabaseId id
-      # Database domain.
-      string domain
-      # Database name.
-      string name
-      # Database version.
-      string version
-
-  # Database error.
-  type Error extends object
-    properties
-      # Error message.
-      string message
-      # Error code.
-      integer code
-
-  # Disables database tracking, prevents database events from being sent to the client.
-  command disable
-
-  # Enables database tracking, database events will now be delivered to the client.
-  command enable
-
-  command executeSQL
-    parameters
-      DatabaseId databaseId
-      string query
-    returns
-      optional array of string columnNames
-      optional array of any values
-      optional Error sqlError
-
-  command getDatabaseTableNames
-    parameters
-      DatabaseId databaseId
-    returns
-      array of string tableNames
-
-  event addDatabase
-    parameters
-      Database database
-
 experimental domain DeviceOrientation
 
   # Clears the overridden Device Orientation.
@@ -8246,6 +8197,7 @@ domain Page
       ch-ua
       ch-ua-arch
       ch-ua-bitness
+      ch-ua-high-entropy-values
       ch-ua-platform
       ch-ua-model
       ch-ua-mobile
```

## Roll protocol to r1403989 — _2025-01-09T04:29:04.000Z_
######  Diff: [`d212a6d...e2b4f4f`](https://github.com/ChromeDevTools/devtools-protocol/compare/d212a6d...e2b4f4f)

```diff
@@ browser_protocol.pdl:11295 @@ domain Target
     parameters
       # The initial URL the page will be navigated to. An empty string indicates about:blank.
       string url
-      # Frame left origin in DIP (headless chrome only).
+      # Frame left origin in DIP (requires newWindow to be true or headless shell).
       experimental optional integer left
-      # Frame top origin in DIP (headless chrome only).
+      # Frame top origin in DIP (requires newWindow to be true or headless shell).
       experimental optional integer top
-      # Frame width in DIP (headless chrome only).
+      # Frame width in DIP (requires newWindow to be true or headless shell).
       optional integer width
-      # Frame height in DIP (headless chrome only).
+      # Frame height in DIP (requires newWindow to be true or headless shell).
       optional integer height
       # The browser context to create the page in.
       experimental optional Browser.BrowserContextID browserContextId
-      # Whether BeginFrames for this target will be controlled via DevTools (headless chrome only,
+      # Whether BeginFrames for this target will be controlled via DevTools (headless shell only,
       # not supported on MacOS yet, false by default).
       experimental optional boolean enableBeginFrameControl
-      # Whether to create a new Window or Tab (chrome-only, false by default).
+      # Whether to create a new Window or Tab (false by default, not supported by headless shell).
       optional boolean newWindow
-      # Whether to create the target in background or foreground (chrome-only,
-      # false by default).
+      # Whether to create the target in background or foreground (false by default, not supported
+      # by headless shell).
       optional boolean background
       # Whether to create the target of type "tab".
       experimental optional boolean forTab
```

## Roll protocol to r1403386 — _2025-01-08T04:29:00.000Z_
######  Diff: [`7757e29...d212a6d`](https://github.com/ChromeDevTools/devtools-protocol/compare/7757e29...d212a6d)

```diff
@@ browser_protocol.pdl:992 @@ experimental domain Audits
       InteractiveContentOptionChild
       InteractiveContentLegendChild
 
-  # This isue warns about errors in the select element content model.
+  # This issue warns about errors in the select element content model.
   type SelectElementAccessibilityIssueDetails extends object
     properties
       DOM.BackendNodeId nodeId
       SelectElementAccessibilityIssueReason selectElementAccessibilityIssueReason
       boolean hasDisallowedAttributes
 
-
   type StyleSheetLoadingIssueReason extends string
     enum
       LateImportRule
@@ -10261,7 +10260,6 @@ experimental domain Storage
   # Enum of possible storage types.
   type StorageType extends string
     enum
-      appcache
       cookies
       file_systems
       indexeddb
```

## Roll protocol to r1402790 — _2025-01-07T04:28:42.000Z_
######  Diff: [`9d48b99...7757e29`](https://github.com/ChromeDevTools/devtools-protocol/compare/9d48b99...7757e29)

```diff
@@ browser_protocol.pdl:2327 @@ experimental domain CSS
     returns
       array of string results
 
+  experimental command getLonghandProperties
+    parameters
+      string shorthandName
+      string value
+    returns
+      array of CSSProperty longhandProperties
+
   # Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
   # attributes) for a DOM node identified by `nodeId`.
   command getInlineStylesForNode
@@ -7429,6 +7436,7 @@ domain Network
         InternalError
         UnknownError
         FulfilledLocally
+        SiteIssuerLimit
       TrustTokenOperationType type
       RequestId requestId
       # Top level origin. The context in which the operation was attempted.
```

## Roll protocol to r1402036 — _2025-01-04T04:28:29.000Z_
######  Diff: [`1f97d3a...9d48b99`](https://github.com/ChromeDevTools/devtools-protocol/compare/1f97d3a...9d48b99)

```diff
@@ browser_protocol.pdl:7639 @@ domain Network
     returns
       LoadNetworkResourcePageResult resource
 
+  # Sets Controls for third-party cookie access
+  # Page reload is required before the new cookie bahavior will be observed
+  experimental command setCookieControls
+    parameters
+      # Whether 3pc restriction is enabled.
+      boolean enableThirdPartyCookieRestriction
+
+      # Whether 3pc grace period exception should be enabled; false by default.
+      boolean disableThirdPartyCookieMetadata
+
+      # Whether 3pc heuristics exceptions should be enabled; false by default.
+      boolean disableThirdPartyCookieHeuristics
+
 # This domain provides various functionality related to drawing atop the inspected page.
 experimental domain Overlay
   depends on DOM
```
