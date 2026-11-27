# Chrome DevTools Protocol changelog — 2024-11

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-11, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1389614 — _2024-11-29T04:30:26.000Z_
######  Diff: [`c2bdeee...33ab53c`](https://github.com/ChromeDevTools/devtools-protocol/compare/c2bdeee...33ab53c)

```diff
@@ browser_protocol.pdl:654 @@ experimental domain Audits
       CorpNotSameOriginAfterDefaultedToSameOriginByDip
       CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip
       CorpNotSameSite
+      SRIMessageSignatureMismatch
 
   # Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
   # code. Currently only used for COEP/COOP, but may be extended to include
@@ -5991,6 +5992,7 @@ domain Network
       corp-not-same-origin-after-defaulted-to-same-origin-by-dip
       corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip
       corp-not-same-site
+      sri-message-signature-mismatch
 
   # The reason why request was blocked.
   type CorsError extends string
```

## Roll protocol to r1388031 — _2024-11-26T04:30:08.000Z_
######  Diff: [`1538d6c...e3771a8`](https://github.com/ChromeDevTools/devtools-protocol/compare/1538d6c...e3771a8)

```diff
@@ browser_protocol.pdl:1393 @@ domain Browser
 
   experimental type PermissionType extends string
     enum
-      accessibilityEvents
+      ar
       audioCapture
-      backgroundSync
+      automaticFullscreen
       backgroundFetch
+      backgroundSync
+      cameraPanTiltZoom
       capturedSurfaceControl
       clipboardReadWrite
       clipboardSanitizedWrite
       displayCapture
       durableStorage
-      flash
       geolocation
+      handTracking
       idleDetection
+      keyboardLock
       localFonts
       midi
       midiSysex
@@ -1412,16 +1415,19 @@ domain Browser
       notifications
       paymentHandler
       periodicBackgroundSync
+      pointerLock
       protectedMediaIdentifier
       sensors
-      storageAccess
+      smartCard
       speakerSelection
+      storageAccess
       topLevelStorageAccess
       videoCapture
-      videoCapturePanTiltZoom
+      vr
       wakeLockScreen
       wakeLockSystem
       webAppInstallation
+      webPrinting
       windowManagement
 
   experimental type PermissionSetting extends string
```

## Roll protocol to r1387316 — _2024-11-24T04:29:22.000Z_
######  Diff: [`a49a587...1538d6c`](https://github.com/ChromeDevTools/devtools-protocol/compare/a49a587...1538d6c)

```diff
@@ browser_protocol.pdl:2733 @@ domain DOM
     enum
       first-line
       first-letter
-      check
+      checkmark
       before
       after
       select-arrow
```

## Roll protocol to r1387216 — _2024-11-23T04:29:30.000Z_
######  Diff: [`4183867...a49a587`](https://github.com/ChromeDevTools/devtools-protocol/compare/4183867...a49a587)

```diff
@@ browser_protocol.pdl:2749 @@ domain DOM
       first-line-inherited
       scroll-marker
       scroll-marker-group
-      scroll-next-button
-      scroll-prev-button
+      scroll-button
       scrollbar
       scrollbar-thumb
       scrollbar-button
```

## Roll protocol to r1386619 — _2024-11-22T04:29:55.000Z_
######  Diff: [`78587ee...4183867`](https://github.com/ChromeDevTools/devtools-protocol/compare/78587ee...4183867)

```diff
@@ browser_protocol.pdl:543 @@ experimental domain Audits
       SetCookie
       ReadCookie
 
+  # Represents the category of insight that a cookie issue falls under.
+  type InsightType extends string
+    enum
+      # Cookie domain has an entry in third-party cookie migration readiness
+      # list:
+      # https://github.com/privacysandbox/privacy-sandbox-dev-support/blob/main/3pc-migration-readiness.md
+      GitHubResource
+      # Cookie is exempted due to a grace period:
+      # https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
+      GracePeriod
+      # Cookie is exempted due a heuristics-based exemptiuon:
+      # https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/heuristics-based-exception
+      Heuristics
+
+  # Information about the suggested solution to a cookie issue.
+  type CookieIssueInsight extends object
+    properties
+      InsightType type
+      # Link to table entry in third-party cookie migration readiness list.
+      optional string tableEntryUrl
+
   # This information is currently necessary, as the front-end has a difficult
   # time finding a specific cookie. With this, we can convey specific error
   # information without the cookie.
@@ -562,6 +583,8 @@ experimental domain Audits
       optional string siteForCookies
       optional string cookieUrl
       optional AffectedRequest request
+      # The recommended solution to the issue.
+      optional CookieIssueInsight insight
 
   type MixedContentResolutionStatus extends string
     enum
```

## Roll protocol to r1383960 — _2024-11-16T04:30:17.000Z_
######  Diff: [`0270ad8...78587ee`](https://github.com/ChromeDevTools/devtools-protocol/compare/0270ad8...78587ee)

```diff
@@ browser_protocol.pdl:8130 @@ domain Page
       controlled-frame
       cross-origin-isolated
       deferred-fetch
+      deferred-fetch-minimal
       digital-credentials-get
       direct-sockets
       direct-sockets-private
```

## Roll protocol to r1380148 — _2024-11-08T04:28:53.000Z_
######  Diff: [`0225c22...e098480`](https://github.com/ChromeDevTools/devtools-protocol/compare/0225c22...e098480)

```diff
@@ browser_protocol.pdl:2322 @@ experimental domain CSS
   # Starts tracking the given node for the computed style updates
   # and whenever the computed style is updated for node, it queues
   # a `computedStyleUpdated` event with throttling.
+  # There can only be 1 node tracked for computed style updates
+  # so passing a new node id removes tracking from the previous node.
+  # Pass `undefined` to disable tracking.
   experimental command trackComputedStyleUpdatesForNode
     parameters
       optional DOM.NodeId nodeId
@@ -5704,7 +5707,9 @@ domain Network
   # Unique loader identifier.
   type LoaderId extends string
 
-  # Unique request identifier.
+  # Unique network request identifier.
+  # Note that this does not identify individual HTTP requests that are part of
+  # a network request.
   type RequestId extends string
 
   # Unique intercepted request identifier.
@@ -6218,6 +6223,7 @@ domain Network
         preflight
         other
       # Initiator JavaScript stack trace, set for Script only.
+      # Requires the Debugger domain to be enabled.
       optional Runtime.StackTrace stack
       # Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.
       optional string url
@@ -11503,6 +11509,8 @@ domain Fetch
   depends on Page
 
   # Unique request identifier.
+  # Note that this does not identify individual HTTP requests that are part of
+  # a network request.
   type RequestId extends string
 
   # Stages of the request to handle. Request will intercept before the request is
```

## Roll protocol to r1379457 — _2024-11-07T04:29:07.000Z_
######  Diff: [`652c02c...0225c22`](https://github.com/ChromeDevTools/devtools-protocol/compare/652c02c...0225c22)

```diff
@@ browser_protocol.pdl:6397 @@ domain Network
       # The cookie's name/value pair size exceeded the size limit defined in
       # RFC6265bis.
       NameValuePairExceedsMaxSize
+      # The cookie's source port value does not match the request origin's port.
+      PortMismatch
+      # The cookie's source scheme value does not match the request origin's scheme.
+      SchemeMismatch
 
   # Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.
   experimental type CookieExemptionReason extends string
@@ -9397,7 +9401,8 @@ domain Page
       # Default dialog prompt.
       optional string defaultPrompt
 
-  # Fired for top level page lifecycle events such as navigation, load, paint, etc.
+  # Fired for lifecycle events (navigation, load, paint, etc) in the current
+  # target (including local frames).
   event lifecycleEvent
     parameters
       # Id of the frame.
@@ -10859,6 +10864,7 @@ experimental domain Storage
       excessiveReportingOrigins
       noHistograms
       insufficientBudget
+      insufficientNamedBudget
       noMatchingSourceFilterData
       notRegistered
       prohibitedByBrowserPolicy
```

## Roll protocol to r1378738 — _2024-11-06T04:29:39.000Z_
######  Diff: [`7019b3c...652c02c`](https://github.com/ChromeDevTools/devtools-protocol/compare/7019b3c...652c02c)

```diff
@@ browser_protocol.pdl:2319 @@ experimental domain CSS
     returns
       array of SourceRange ranges
 
+  # Starts tracking the given node for the computed style updates
+  # and whenever the computed style is updated for node, it queues
+  # a `computedStyleUpdated` event with throttling.
+  experimental command trackComputedStyleUpdatesForNode
+    parameters
+      optional DOM.NodeId nodeId
+
   # Starts tracking the given computed styles for updates. The specified array of properties
   # replaces the one previously specified. Pass empty array to disable tracking.
   # Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
@@ -2486,6 +2493,11 @@ experimental domain CSS
       # Identifier of the removed stylesheet.
       StyleSheetId styleSheetId
 
+  experimental event computedStyleUpdated
+    parameters
+      # The node id that has updated computed styles.
+      DOM.NodeId nodeId
+
 experimental domain CacheStorage
   depends on Storage
```

## Roll protocol to r1377232 — _2024-11-02T04:29:34.000Z_
######  Diff: [`b62e175...b1b0036`](https://github.com/ChromeDevTools/devtools-protocol/compare/b62e175...b1b0036)

```diff
@@ browser_protocol.pdl:117 @@ experimental domain Accessibility
   # - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
   type AXPropertyName extends string
     enum
+      actions
       busy
       disabled
       editable
@@ -517,6 +518,8 @@ experimental domain Audits
       ExcludeDomainNonASCII
       ExcludeThirdPartyCookieBlockedInFirstPartySet
       ExcludeThirdPartyPhaseout
+      ExcludePortMismatch
+      ExcludeSchemeMismatch
 
   type CookieWarningReason extends string
     enum
@@ -2695,6 +2698,7 @@ domain DOM
       check
       before
       after
+      select-arrow
       marker
       backdrop
       column
```

## Roll protocol to r1376744 — _2024-11-01T04:29:19.000Z_
######  Diff: [`2354f74...b62e175`](https://github.com/ChromeDevTools/devtools-protocol/compare/2354f74...b62e175)

```diff
@@ browser_protocol.pdl:1798 @@ experimental domain CSS
       experimental optional array of CSSScope scopes
       # The array keeps the types of ancestor CSSRules from the innermost going outwards.
       experimental optional array of CSSRuleType ruleTypes
+      # @starting-style CSS at-rule array.
+      # The array enumerates @starting-style at-rules starting with the innermost one, going outwards.
+      experimental optional array of CSSStartingStyle startingStyles
 
   # Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors.
   # This list only contains rule types that are collected during the ancestor rule collection.
@@ -1809,6 +1812,7 @@ experimental domain CSS
       LayerRule
       ScopeRule
       StyleRule
+      StartingStyleRule
 
   # CSS coverage information.
   type RuleUsage extends object
@@ -1951,6 +1955,8 @@ experimental domain CSS
       optional DOM.PhysicalAxes physicalAxes
       # Optional logical axes queried for the container.
       optional DOM.LogicalAxes logicalAxes
+      # true if the query contains scroll-state() queries.
+      optional boolean queriesScrollState
 
   # CSS Supports at-rule descriptor.
   experimental type CSSSupports extends object
@@ -1987,6 +1993,15 @@ experimental domain CSS
       # Identifier of the stylesheet containing this object (if exists).
       optional StyleSheetId styleSheetId
 
+  # CSS Starting Style at-rule descriptor.
+  experimental type CSSStartingStyle extends object
+    properties
+      # The associated rule header range in the enclosing stylesheet (if
+      # available).
+      optional SourceRange range
+      # Identifier of the stylesheet containing this object (if exists).
+      optional StyleSheetId styleSheetId
+
   # CSS Layer data.
   experimental type CSSLayerData extends object
     properties
@@ -3387,15 +3402,17 @@ domain DOM
       optional NodeId nodeId
 
   # Returns the query container of the given node based on container query
-  # conditions: containerName, physical, and logical axes. If no axes are
-  # provided, the style container is returned, which is the direct parent or the
-  # closest element with a matching container-name.
+  # conditions: containerName, physical and logical axes, and whether it queries
+  # scroll-state. If no axes are provided and queriesScrollState is false, the
+  # style container is returned, which is the direct parent or the closest
+  # element with a matching container-name.
   experimental command getContainerForNode
     parameters
       NodeId nodeId
       optional string containerName
       optional PhysicalAxes physicalAxes
       optional LogicalAxes logicalAxes
+      optional boolean queriesScrollState
     returns
       # The container node for the given node, or null if not found.
       optional NodeId nodeId
```
