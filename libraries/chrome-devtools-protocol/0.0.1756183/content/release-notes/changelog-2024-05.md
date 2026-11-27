# Chrome DevTools Protocol changelog — 2024-05

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-05, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1308459 — _2024-05-31T04:27:42.000Z_
######  Diff: [`24b69f0...24f369f`](https://github.com/ChromeDevTools/devtools-protocol/compare/24b69f0...24f369f)

```diff
@@ browser_protocol.pdl:7093 @@ domain Network
         FailedPrecondition
         ResourceExhausted
         AlreadyExists
-        Unavailable
+        ResourceLimited
         Unauthorized
         BadResponse
         InternalError
```

## Roll protocol to r1306150 — _2024-05-26T04:28:00.000Z_
######  Diff: [`bbd2600...24b69f0`](https://github.com/ChromeDevTools/devtools-protocol/compare/bbd2600...24b69f0)

```diff
@@ browser_protocol.pdl:3337 @@ domain DOM
       # Descendant nodes with container queries against the given container.
       array of NodeId nodeIds
 
+  # Returns the target anchor element of the given anchor query according to
+  # https://www.w3.org/TR/css-anchor-position-1/#target.
+  experimental command getAnchorElement
+    parameters
+      # Id of the positioned element from which to find the anchor.
+      NodeId nodeId
+      # An optional anchor specifier, as defined in
+      # https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier.
+      # If not provided, it will return the implicit anchor element for
+      # the given positioned element.
+      optional string anchorSpecifier
+    returns
+      # The anchor element of the given anchor query.
+      NodeId nodeId
+
   # Fired when `Element`'s attribute is modified.
   event attributeModified
     parameters
```

## Roll protocol to r1305504 — _2024-05-24T04:27:22.000Z_
######  Diff: [`799ae7e...bbd2600`](https://github.com/ChromeDevTools/devtools-protocol/compare/799ae7e...bbd2600)

```diff
@@ browser_protocol.pdl:12401 @@ experimental domain PWA
     returns
       # ID of the tab target created as a result.
       Target.TargetID targetId
+
+  # Opens one or more local files from an installed web app identified by its
+  # manifestId. The web app needs to have file handlers registered to process
+  # the files. The API returns one or more tabs / web contents' based
+  # Target.TargetIDs which can be used to attach to via Target.attachToTarget or
+  # similar APIs.
+  # If some files in the parameters cannot be handled by the web app, they will
+  # be ignored. If none of the files can be handled, this API returns an error.
+  # If no files provided as the parameter, this API also returns an error.
+  #
+  # According to the definition of the file handlers in the manifest file, one
+  # Target.TargetID may represent a tab handling one or more files. The order of
+  # the returned Target.TargetIDs is also not guaranteed.
+  #
+  # TODO(crbug.com/339454034): Check the existences of the input files.
+  command launchFilesInApp
+    parameters
+      string manifestId
+      array of string files
+    returns
+      # IDs of the tab targets created as the result.
+      array of Target.TargetID targetIds
```

## Roll protocol to r1304863 — _2024-05-23T04:26:40.000Z_
######  Diff: [`7c5d5b6...799ae7e`](https://github.com/ChromeDevTools/devtools-protocol/compare/7c5d5b6...799ae7e)

```diff
@@ browser_protocol.pdl:851 @@ experimental domain Audits
       array of string allowedSites
       number optOutPercentage
       boolean isOptOutTopLevel
+      CookieOperation operation
 
   type ClientHintIssueReason extends string
     enum
@@ -5589,6 +5590,10 @@ domain Network
       experimental number workerFetchStart
       # Settled fetch event respondWith promise.
       experimental number workerRespondWithSettled
+      # Started ServiceWorker static routing source evaluation.
+      experimental optional number workerRouterEvaluationStart
+      # Started cache lookup when the source was evaluated to `cache`.
+      experimental optional number workerCacheLookupStart
       # Started sending request.
       number sendStart
       # Finished sending request.
@@ -5874,6 +5879,8 @@ domain Network
       # The router source of the matched rule. If there is a matched rule, this
       # field will be set, otherwise no value will be set.
       optional ServiceWorkerRouterSource matchedSourceType
+      # The actual router source used.
+      optional ServiceWorkerRouterSource actualSourceType
 
   # HTTP response data.
   type Response extends object
```

## Roll protocol to r1304228 — _2024-05-22T04:27:23.000Z_
######  Diff: [`fa8a8ed...7c5d5b6`](https://github.com/ChromeDevTools/devtools-protocol/compare/fa8a8ed...7c5d5b6)

```diff
@@ browser_protocol.pdl:911 @@ experimental domain Audits
       NotSignedInWithIdp
       MissingTransientUserActivation
       ReplacedByButtonMode
+      RelyingPartyOriginIsOpaque
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
```

## Roll protocol to r1302984 — _2024-05-18T04:26:58.000Z_
######  Diff: [`82ed3df...fa8a8ed`](https://github.com/ChromeDevTools/devtools-protocol/compare/82ed3df...fa8a8ed)

```diff
@@ browser_protocol.pdl:8710 @@ domain Page
       # If set, the script will be injected into all frames of the inspected page after reload.
       # Argument will be ignored if reloading dataURL origin.
       optional string scriptToEvaluateOnLoad
+      # If set, an error will be thrown if the target page's main frame's
+      # loader id does not match the provided id. This prevents accidentally
+      # reloading an unintended target in case there's a racing navigation.
+      experimental optional Network.LoaderId loaderId
 
   # Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
   experimental deprecated command removeScriptToEvaluateOnLoad
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index ee14676c..8dad9c98 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -1297,10 +1297,6 @@ domain Runtime
   # Id of an execution context.
   type ExecutionContextId extends integer
 
-  # Id of an execution context that is unique across processes
-  # (unlike ExecutionContextId).
-  type ExecutionContextUniqueId extends string
-
   # Description of an isolated world.
   type ExecutionContextDescription extends object
     properties
@@ -1314,7 +1310,7 @@ domain Runtime
       # A system-unique execution context identifier. Unlike the id, this is unique across
       # multiple processes, so can be reliably used to identify specific context while backend
       # performs a cross-process navigation.
-      experimental ExecutionContextUniqueId uniqueId
+      experimental string uniqueId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object auxData
 
@@ -1675,8 +1671,7 @@ domain Runtime
       # If specified, the binding would only be exposed to the specified
       # execution context. If omitted and `executionContextName` is not set,
       # the binding is exposed to all execution contexts of the target.
-      # This parameter is mutually exclusive with `executionContextName`
-      # and `executionContextUniqueId`.
+      # This parameter is mutually exclusive with `executionContextName`.
       # Deprecated in favor of `executionContextName` due to an unclear use case
       # and bugs in implementation (crbug.com/1169639). `executionContextId` will be
       # removed in the future.
@@ -1685,12 +1680,8 @@ domain Runtime
       # matching name, even for contexts created after the binding is added.
       # See also `ExecutionContext.name` and `worldName` parameter to
       # `Page.addScriptToEvaluateOnNewDocument`.
-      # This parameter is mutually exclusive with `executionContextId`
-      # and `executionContextUniqueId`.
+      # This parameter is mutually exclusive with `executionContextId`.
       optional string executionContextName
-      # This parameter is mutually exclusive with `executionContextId`
-      # and `executionContextName`.
-      experimental optional ExecutionContextUniqueId executionContextUniqueId
 
   # This method does not remove binding function from global object but
   # unsubscribes current runtime agent from Runtime.bindingCalled notifications.
@@ -1717,7 +1708,6 @@ domain Runtime
       string payload
       # Identifier of the context where the call was made.
       ExecutionContextId executionContextId
-      experimental ExecutionContextUniqueId executionContextUniqueId
 
   # Issued when console API was called.
   event consoleAPICalled
@@ -1746,7 +1736,6 @@ domain Runtime
       array of RemoteObject args
       # Identifier of the context where the call was made.
       ExecutionContextId executionContextId
-      experimental ExecutionContextUniqueId executionContextUniqueId
       # Call timestamp.
       Timestamp timestamp
       # Stack trace captured when the call was made. The async stack chain is automatically reported for
@@ -1785,7 +1774,7 @@ domain Runtime
       # Id of the destroyed context
       deprecated ExecutionContextId executionContextId
       # Unique Id of the destroyed context
-      experimental ExecutionContextUniqueId executionContextUniqueId
+      experimental string executionContextUniqueId
 
   # Issued when all executionContexts were cleared in browser
   event executionContextsCleared
```

## Roll protocol to r1302401 — _2024-05-17T04:26:51.000Z_
######  Diff: [`f8def09...82ed3df`](https://github.com/ChromeDevTools/devtools-protocol/compare/f8def09...82ed3df)

```diff
@@ browser_protocol.pdl:849 @@ experimental domain Audits
   type CookieDeprecationMetadataIssueDetails extends object
     properties
       array of string allowedSites
+      number optOutPercentage
+      boolean isOptOutTopLevel
 
   type ClientHintIssueReason extends string
     enum
```

## Roll protocol to r1301748 — _2024-05-16T04:24:35.000Z_
######  Diff: [`e200d9e...f8def09`](https://github.com/ChromeDevTools/devtools-protocol/compare/e200d9e...f8def09)

```diff
@@ browser_protocol.pdl:6183 @@ domain Network
       TopLevelStorageAccess
       # The cookie should have been blocked by 3PCD but is exempted by CORS opt-in.
       CorsOptIn
+      # The cookie should have been blocked by 3PCD but is exempted by the first-party URL scheme.
+      Scheme
 
   # A cookie which was not stored from a response with the corresponding reason.
   experimental type BlockedSetCookieWithReason extends object
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 8dad9c98..ee14676c 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -1297,6 +1297,10 @@ domain Runtime
   # Id of an execution context.
   type ExecutionContextId extends integer
 
+  # Id of an execution context that is unique across processes
+  # (unlike ExecutionContextId).
+  type ExecutionContextUniqueId extends string
+
   # Description of an isolated world.
   type ExecutionContextDescription extends object
     properties
@@ -1310,7 +1314,7 @@ domain Runtime
       # A system-unique execution context identifier. Unlike the id, this is unique across
       # multiple processes, so can be reliably used to identify specific context while backend
       # performs a cross-process navigation.
-      experimental string uniqueId
+      experimental ExecutionContextUniqueId uniqueId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object auxData
 
@@ -1671,7 +1675,8 @@ domain Runtime
       # If specified, the binding would only be exposed to the specified
       # execution context. If omitted and `executionContextName` is not set,
       # the binding is exposed to all execution contexts of the target.
-      # This parameter is mutually exclusive with `executionContextName`.
+      # This parameter is mutually exclusive with `executionContextName`
+      # and `executionContextUniqueId`.
       # Deprecated in favor of `executionContextName` due to an unclear use case
       # and bugs in implementation (crbug.com/1169639). `executionContextId` will be
       # removed in the future.
@@ -1680,8 +1685,12 @@ domain Runtime
       # matching name, even for contexts created after the binding is added.
       # See also `ExecutionContext.name` and `worldName` parameter to
       # `Page.addScriptToEvaluateOnNewDocument`.
-      # This parameter is mutually exclusive with `executionContextId`.
+      # This parameter is mutually exclusive with `executionContextId`
+      # and `executionContextUniqueId`.
       optional string executionContextName
+      # This parameter is mutually exclusive with `executionContextId`
+      # and `executionContextName`.
+      experimental optional ExecutionContextUniqueId executionContextUniqueId
 
   # This method does not remove binding function from global object but
   # unsubscribes current runtime agent from Runtime.bindingCalled notifications.
@@ -1708,6 +1717,7 @@ domain Runtime
       string payload
       # Identifier of the context where the call was made.
       ExecutionContextId executionContextId
+      experimental ExecutionContextUniqueId executionContextUniqueId
 
   # Issued when console API was called.
   event consoleAPICalled
@@ -1736,6 +1746,7 @@ domain Runtime
       array of RemoteObject args
       # Identifier of the context where the call was made.
       ExecutionContextId executionContextId
+      experimental ExecutionContextUniqueId executionContextUniqueId
       # Call timestamp.
       Timestamp timestamp
       # Stack trace captured when the call was made. The async stack chain is automatically reported for
@@ -1774,7 +1785,7 @@ domain Runtime
       # Id of the destroyed context
       deprecated ExecutionContextId executionContextId
       # Unique Id of the destroyed context
-      experimental string executionContextUniqueId
+      experimental ExecutionContextUniqueId executionContextUniqueId
 
   # Issued when all executionContexts were cleared in browser
   event executionContextsCleared
```

## Roll protocol to r1301093 — _2024-05-15T04:27:06.000Z_
######  Diff: [`2ac7f42...e200d9e`](https://github.com/ChromeDevTools/devtools-protocol/compare/2ac7f42...e200d9e)

```diff
@@ browser_protocol.pdl:2633 @@ domain DOM
       highlight
       first-line-inherited
       scroll-marker
-      scroll-markers
+      scroll-marker-group
       scrollbar
       scrollbar-thumb
       scrollbar-button
```

## Roll protocol to r1300426 — _2024-05-14T04:26:18.000Z_
######  Diff: [`404576f...2ac7f42`](https://github.com/ChromeDevTools/devtools-protocol/compare/404576f...2ac7f42)

```diff
@@ browser_protocol.pdl:2626 @@ domain DOM
       marker
       backdrop
       selection
+      search-text
       target-text
       spelling-error
       grammar-error
```

## Roll protocol to r1299070 — _2024-05-10T04:26:27.000Z_
######  Diff: [`fd7b5be...404576f`](https://github.com/ChromeDevTools/devtools-protocol/compare/fd7b5be...404576f)

```diff
@@ browser_protocol.pdl:12127 @@ experimental domain Preload
       ActivationUrlHasEffectiveUrl
       JavaScriptInterfaceAdded
       JavaScriptInterfaceRemoved
+      AllPrerenderingCanceled
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1298513 — _2024-05-09T04:28:16.000Z_
######  Diff: [`2e6353a...fd7b5be`](https://github.com/ChromeDevTools/devtools-protocol/compare/2e6353a...fd7b5be)

```diff
@@ browser_protocol.pdl:12371 @@ experimental domain PWA
   command uninstall
     parameters
       string manifestId
+
+  # Launches the installed web app, or an url in the same web app instead of the
+  # default start url if it is provided. Returns a tab / web contents based
+  # Target.TargetID which can be used to attach to via Target.attachToTarget or
+  # similar APIs.
+  command launch
+    parameters
+      string manifestId
+      optional string url
+    returns
+      # ID of the tab target created as a result.
+      Target.TargetID targetId
```

## Roll protocol to r1297943 — _2024-05-08T04:25:54.000Z_
######  Diff: [`be37be1...2e6353a`](https://github.com/ChromeDevTools/devtools-protocol/compare/be37be1...2e6353a)

```diff
@@ browser_protocol.pdl:12125 @@ experimental domain Preload
       PrerenderingUrlHasEffectiveUrl
       RedirectedPrerenderingUrlHasEffectiveUrl
       ActivationUrlHasEffectiveUrl
+      JavaScriptInterfaceAdded
+      JavaScriptInterfaceRemoved
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1297280 — _2024-05-07T04:27:12.000Z_
######  Diff: [`30f9082...be37be1`](https://github.com/ChromeDevTools/devtools-protocol/compare/30f9082...be37be1)

```diff
@@ browser_protocol.pdl:6459 @@ domain Network
       optional string path
       # If specified, deletes only cookies with the the given name and partitionKey where domain
       # matches provided URL.
-      optional string partitionKey
+      experimental optional string partitionKey
 
   # Disables network tracking, prevents network events from being sent to the client.
   command disable
```

## Roll protocol to r1294763 — _2024-05-01T04:26:34.000Z_
######  Diff: [`b80715b...b717085`](https://github.com/ChromeDevTools/devtools-protocol/compare/b80715b...b717085)

```diff
@@ browser_protocol.pdl:12355 @@ experimental domain PWA
   # requirement.
   # IWA-specific install description: If the manifest_id is isolated-app://,
   # install_url_or_bundle_url is required, and can be either an http(s) URL or
-  # file:// URL pointing to a signed web bundle (.swbn). The .swbn file’s
+  # file:// URL pointing to a signed web bundle (.swbn). The .swbn file's
   # signing key must correspond to manifest_id. If Chrome is not in IWA dev
   # mode, the installation will fail, regardless of the state of the allowlist.
   command install
```
