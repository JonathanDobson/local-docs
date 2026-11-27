# Chrome DevTools Protocol changelog — 2026-09

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-09, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1707781 — _2026-09-30T04:45:23.000Z_
######  Diff: [`dc2ddf3...8b7f1d9`](https://github.com/ChromeDevTools/devtools-protocol/compare/dc2ddf3...8b7f1d9)

```diff
@@ browser_protocol.pdl:33 @@ include domains/Extensions.pdl
 include domains/FedCm.pdl
 include domains/Fetch.pdl
 include domains/FileSystem.pdl
+include domains/FindInPage.pdl
 include domains/HeadlessExperimental.pdl
 include domains/IO.pdl
 include domains/IndexedDB.pdl
diff --git a/pdl/domains/FindInPage.pdl b/pdl/domains/FindInPage.pdl
new file mode 100644
index 00000000..ca4aed7e
--- /dev/null
+++ b/pdl/domains/FindInPage.pdl
@@ -0,0 +1,22 @@
+# Copyright 2026 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+
+# This domain provides commands to trigger the "Find in page" feature.
+experimental domain FindInPage
+  # Forwards `query` to the find-in-page facility, starting a new find session.
+  # Where exactly the search starts from is implementation-specific.
+  command findFirst
+    parameters
+      string query
+
+  # Moves to the next match for the query passed to the most recent
+  # findFirst() call.
+  command findNext
+
+  # Moves to the previous match for the query passed to the most recent
+  # findFirst() call.
+  command findPrev
+
+  # Ends the current find session, if any, and clears its highlighting.
+  command stop
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 591234dd..20b5db99 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -152,6 +152,7 @@ domain Page
       private-state-token-redemption
       publickey-credentials-create
       publickey-credentials-get
+      publickey-credentials-remote-client-data-json
       rewriter
       screen-wake-lock
       serial
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 99905a48..ad0d42bf 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -143,7 +143,7 @@ domain Debugger
       optional Location startLocation
       # Location in the source code where scope ends
       optional Location endLocation
-      # True if the scope does not declare any variables or have a runtime context.
+      # True if the scope does not declare any variables.
       # Only present if true.
       # Empty scopes are retained in the scope chain because
       # they can be targeted via `evaluateOnCallFrame` (using `scopeNumber`) or
```

## Roll protocol to r1704951 — _2026-09-26T04:34:54.000Z_
######  Diff: [`1474833...dc2ddf3`](https://github.com/ChromeDevTools/devtools-protocol/compare/1474833...dc2ddf3)

```diff
@@ domains/Emulation.pdl:330 @@ domain Emulation
         # Restores the default viewport meta behavior (disabled on desktop,
         # enabled on mobile).
         default
+      # Text layout mode. Default: `default`. Note: if `mobile` is `true`,
+      # mobile text layout mode (text autosizing) is always enabled.
+      experimental optional enum textLayoutMode
+        # Enables mobile text layout mode (text autosizing / CSS text-size-adjust).
+        mobile
+        # Restores the default text layout mode behavior (disabled on desktop,
+        # enabled on mobile).
+        default
 
   # Start reporting the given posture value to the Device Posture API.
   # This override can also be set in setDeviceMetricsOverride().
```

## Roll protocol to r1704684 — _2026-09-25T10:37:33.000Z_
######  Diff: [`41fafef...1474833`](https://github.com/ChromeDevTools/devtools-protocol/compare/41fafef...1474833)

```diff
@@ domains/Preload.pdl:287 @@ experimental domain Preload
       PreloadingAttemptKey key
       PreloadPipelineId pipelineId
       PreloadingStatus status
+      # The action currently performed by this attempt. This differs from
+      # `key.action` after a prerender-until-script attempt is upgraded in place
+      # to a full prerender.
+      optional SpeculationAction effectiveAction
       optional PrerenderFinalStatus prerenderStatus
       # This is used to give users more information about the name of Mojo interface
       # that is incompatible with prerender and has caused the cancellation of the attempt.
```

## Roll protocol to r1704034 — _2026-09-24T04:37:35.000Z_
######  Diff: [`95987cc...692abe8`](https://github.com/ChromeDevTools/devtools-protocol/compare/95987cc...692abe8)

```diff
@@ domains/Page.pdl:388 @@ domain Page
       number scrollOffsetY
       # Frame swap timestamp.
       optional Network.TimeSinceEpoch timestamp
+      # Frame swap timestamp as monotonic time.
+      optional Network.MonotonicTime monotonicTimestamp
 
   # Javascript dialog type.
   type DialogType extends string
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index 444d06eb..91f2641e 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -58,6 +58,14 @@ experimental domain Storage
       # Base64-encoded serialized token.
       string token
 
+  # Configuration for a Private Verification Tokens issuer.
+  experimental type PrivateVerificationTokensIssuerConfig extends object
+    properties
+      # Origin of the token issuer.
+      string issuerOrigin
+      # Origins authorized to redeem tokens from this issuer.
+      array of string redeemerOrigins
+
 
 
   type StorageBucketsDurability extends string
@@ -234,6 +242,12 @@ experimental domain Storage
     returns
       array of PrivateVerificationToken tokens
 
+  # Returns the configured Private Verification Tokens issuers and their redeemer
+  # origins.
+  experimental command getPrivateVerificationTokensIssuerConfigs
+    returns
+      array of PrivateVerificationTokensIssuerConfig configs
+
   # Removes all Private Verification Tokens issued by the provided issuerOrigin.
   experimental command clearPrivateVerificationTokens
     parameters
```

## Roll protocol to r1702366 — _2026-09-22T04:36:06.000Z_
######  Diff: [`1cab90f...95987cc`](https://github.com/ChromeDevTools/devtools-protocol/compare/1cab90f...95987cc)

```diff
@@ domains/Audits.pdl:36 @@ experimental domain Audits
       ExcludeSameSiteLax
       ExcludeSameSiteStrict
       ExcludeDomainNonASCII
-      ExcludeThirdPartyCookieBlockedInFirstPartySet
       ExcludeThirdPartyPhaseout
       ExcludePortMismatch
       ExcludeSchemeMismatch
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 571bd165..0161e058 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -630,9 +630,6 @@ domain Network
       UserPreferences
       # The cookie was blocked due to third-party cookie phaseout.
       ThirdPartyPhaseout
-      # The cookie was blocked by third-party cookie blocking between sites in
-      # the same First-Party Set.
-      ThirdPartyBlockedInFirstPartySet
       # The syntax of the Set-Cookie header of the response was invalid.
       SyntaxError
       # The scheme of the connection is not allowed to store cookies.
@@ -699,9 +696,6 @@ domain Network
       UserPreferences
       # The cookie was blocked due to third-party cookie phaseout.
       ThirdPartyPhaseout
-      # The cookie was blocked by third-party cookie blocking between sites in
-      # the same First-Party Set.
-      ThirdPartyBlockedInFirstPartySet
       # An unknown error was encountered when trying to send this cookie.
       UnknownError
       # The cookie had the "SameSite=Strict" attribute but came from a response
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index 7702942c..444d06eb 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -321,19 +321,3 @@ experimental domain Storage
 
   # Private Verification Tokens have been stored or deleted.
   experimental event privateVerificationTokensUpdated
-
-  # A single Related Website Set object.
-  experimental type RelatedWebsiteSet extends object
-    properties
-      # The primary site of this set, along with the ccTLDs if there is any.
-      array of string primarySites
-      # The associated sites of this set, along with the ccTLDs if there is any.
-      array of string associatedSites
-      # The service sites of this set, along with the ccTLDs if there is any.
-      array of string serviceSites
-
-  # Returns the effective Related Website Sets in use by this profile for the browser
-  # session. The effective Related Website Sets will not change during a browser session.
-  experimental command getRelatedWebsiteSets
-    returns
-      array of RelatedWebsiteSet sets
```

## Roll protocol to r1701330 — _2026-09-19T04:33:58.000Z_
######  Diff: [`a3ab2d1...1cab90f`](https://github.com/ChromeDevTools/devtools-protocol/compare/a3ab2d1...1cab90f)

```diff
@@ domains/WebMCP.pdl:19 @@ experimental domain WebMCP
       optional boolean untrustedContent
       # A hint indicating that executing the tool will result in consequential actions, ex: booking a flight, transferring money.
       optional boolean consequential
+      # If true, indicates that the tool is intended for debugging and developer tooling rather than end-user interactions.
+      optional boolean debugging
       # If the declarative tool was declared with the autosubmit attribute.
       optional boolean autosubmit
```

## Roll protocol to r1700460 — _2026-09-18T04:38:05.000Z_
######  Diff: [`bab8418...a3ab2d1`](https://github.com/ChromeDevTools/devtools-protocol/compare/bab8418...a3ab2d1)

```diff
@@ domains/Overlay.pdl:116 @@ experimental domain Overlay
       aaa
       apca
 
+  # Configuration for Inset-Modified Containing Block (IMCB) and CSS Anchor Positioning highlight.
+  type ImcbHighlightConfig extends object
+    properties
+      # Border color for the Inset-Modified Containing Block (default: transparent).
+      optional DOM.RGBA imcbBorderColor
+      # Background fill color for the Inset-Modified Containing Block (default: transparent).
+      optional DOM.RGBA imcbBackgroundColor
+      # Fill color for the inset modifiers area (difference between CB and IMCB).
+      optional DOM.RGBA insetsBackgroundColor
+      # Hatch color for the inset modifiers area.
+      optional DOM.RGBA insetsHatchColor
+      # Border color for the referenced target anchor element(s) (when element is anchor-positioned).
+      optional DOM.RGBA anchorBorderColor
+      # Background fill color for the referenced target anchor element(s) (when element is anchor-positioned).
+      optional DOM.RGBA anchorBackgroundColor
+      # Whether to render the 3x3 position-area grid lines when position-area is used.
+      optional boolean showPositionAreaGrid
+      # Line color for the 3x3 position-area grid lines.
+      optional DOM.RGBA positionAreaGridLineColor
+      # Fill color for the active region within the position-area grid.
+      optional DOM.RGBA positionAreaActiveRegionColor
+
   # Configuration data for the highlighting of page elements.
   type HighlightConfig extends object
     properties
@@ -157,6 +179,8 @@ experimental domain Overlay
       optional ContrastAlgorithm contrastAlgorithm
       # The container query container highlight configuration (default: all transparent).
       optional ContainerQueryContainerHighlightConfig containerQueryContainerHighlightConfig
+      # The IMCB highlight configuration (default: all transparent).
+      optional ImcbHighlightConfig imcbHighlightConfig
 
   type ColorFormat extends string
     enum
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index a2d197c5..c8c374af 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -804,7 +804,18 @@ domain Page
     returns
       optional binary primaryIcon
 
-  # Returns the unique (PWA) app id.
+  type SubApp extends object
+    properties
+      # Display name of the sub-app.
+      string name
+      # Scope of the sub-app.
+      string scope
+      # Manifest id of the sub-app.
+      string manifestId
+      # Start URL of the sub-app.
+      string startUrl
+
+  # Returns the unique (PWA) app id, along with IWA bundle ID and parent app info.
   # Only returns values if the feature flag 'WebAppEnableManifestId' is enabled
   experimental command getAppId
     returns
@@ -812,6 +823,20 @@ domain Page
       optional string appId
       # Recommendation for manifest's id attribute to match current id computed from start_url
       optional string recommendedId
+      # The bundle ID for an Isolated Web App (IWA)
+      optional string bundleId
+      # The name of the parent app if this app is a Sub-App
+      optional string parentAppName
+
+  # Returns the list of installed child Sub-Apps for the inspected parent app.
+  experimental command getSubApps
+    returns
+      array of SubApp subApps
+
+  # Returns the list of sibling Sub-Apps sharing the same parent app if the inspected context is a Sub-App.
+  experimental command getSiblingSubApps
+    returns
+      array of SubApp subApps
 
   experimental command getAdScriptAncestry
     parameters
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index c741899e..7702942c 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -40,6 +40,25 @@ experimental domain Storage
       string issuerOrigin
       number count
 
+  # Details of a stored Private Verification Token.
+  experimental type PrivateVerificationToken extends object
+    properties
+      # Unique identifier of the token in the database.
+      string id
+      # Origin of the token issuer.
+      string issuerOrigin
+      # Public key ID used to issue the token.
+      integer keyId
+      # Expiration timestamp in seconds since the epoch.
+      Network.TimeSinceEpoch expiration
+      # Token creation timestamp in seconds since the epoch.
+      Network.TimeSinceEpoch creationTime
+      # Token protocol version.
+      integer version
+      # Base64-encoded serialized token.
+      string token
+
+
 
   type StorageBucketsDurability extends string
     enum
@@ -209,6 +228,27 @@ experimental domain Storage
       # True if any tokens were deleted, false otherwise.
       boolean didDeleteTokens
 
+  # Returns all stored Private Verification Tokens for the current browsing
+  # context.
+  experimental command getPrivateVerificationTokens
+    returns
+      array of PrivateVerificationToken tokens
+
+  # Removes all Private Verification Tokens issued by the provided issuerOrigin.
+  experimental command clearPrivateVerificationTokens
+    parameters
+      string issuerOrigin
+
+  # Removes a specific Private Verification Token by its ID.
+  experimental command deletePrivateVerificationToken
+    parameters
+      string tokenId
+
+  # Set tracking for Private Verification Tokens.
+  experimental command setPrivateVerificationTokensTracking
+    parameters
+      boolean enable
+
   # Set tracking for a storage key's buckets.
   experimental command setStorageBucketTracking
     parameters
@@ -279,6 +319,9 @@ experimental domain Storage
     parameters
       string bucketId
 
+  # Private Verification Tokens have been stored or deleted.
+  experimental event privateVerificationTokensUpdated
+
   # A single Related Website Set object.
   experimental type RelatedWebsiteSet extends object
     properties
```

## Roll protocol to r1698617 — _2026-09-16T04:38:22.000Z_
######  Diff: [`acf4480...bab8418`](https://github.com/ChromeDevTools/devtools-protocol/compare/acf4480...bab8418)

```diff
@@ domains/Animation.pdl:143 @@ experimental domain Animation
     parameters
       # List of animation ids to seek.
       array of string animations
-      # Set the current time of each animation.
-      number currentTime
+      # Set each animation to the same time.
+      optional number currentTime
+      # Set each animation to a different time. If set, should have the same
+      # length as animations. Exactly one of currentTime or currentTimes should
+      # be set.
+      optional array of number currentTimes
 
   # Sets the paused state of a set of animations.
   command setPaused
```

## Roll protocol to r1697629 — _2026-09-14T23:38:30.000Z_
######  Diff: [`f395a59...acf4480`](https://github.com/ChromeDevTools/devtools-protocol/compare/f395a59...acf4480)

```diff
@@ domains/DOM.pdl:845 @@ domain DOM
       # If true, opens and holds interest. If false, releases forced interest.
       boolean enable
 
+  # Sets a spelling or grammar error marker on the given range of text.
+  # See https://github.com/Igalia/explainers/blob/main/force-spelling-grammar-markers/README.md
+  # Note: exactly one between nodeId, backendNodeId and objectId should be passed
+  # to identify the node.
+  experimental command setTextMarker
+    parameters
+      # Identifier of the node.
+      optional NodeId nodeId
+      # Identifier of the backend node.
+      optional BackendNodeId backendNodeId
+      # JavaScript object id of the node wrapper.
+      optional Runtime.RemoteObjectId objectId
+      # The type of marker to set on the given range of text.
+      enum type
+        # A spelling error marker, rendered as ::spelling-error
+        spelling
+        # A grammar error marker, rendered as ::grammar-error
+        grammar
+      # Start offset into the element's rendered text in UTF-16 code units.
+      # For a text control, an offset into the control's value.
+      # Offsets count text in DOM order and do not enter shadow trees.
+      # To mark text inside a shadow tree, pass the element inside the shadow tree.
+      integer start
+      # End offset (exclusive) in the same units and space as start.
+      integer end
+
+  # Clears the spelling and grammar error text markers overlapping the ranges
+  # set by setTextMarker in this session. These markers are also removed when
+  # the DOM domain is disabled or the session ends.
+  experimental command clearTextMarkers
+
   # Fired when `Element`'s attribute is modified.
   event attributeModified
     parameters
```

## Roll protocol to r1696802 — _2026-09-12T04:34:27.000Z_
######  Diff: [`9b417d8...f395a59`](https://github.com/ChromeDevTools/devtools-protocol/compare/9b417d8...f395a59)

```diff
@@ domains/Audits.pdl:741 @@ experimental domain Audits
       # Used for messages about activation disabled reason
       optional string disableReason
 
+  type WebInstallIssueReason extends string
+    enum
+      ManifestParsingOrNetworkError
+      StartUrlInvalid
+      ManifestMissingNameOrShortName
+      ManifestMissingId
+      NoManifest
+
+  # This issue reports a failure involving a web app manifest used by a Web
+  # Install operation.
+  type WebInstallIssueDetails extends object
+    properties
+      optional string manifestUrl
+      WebInstallIssueReason reason
+
   # The issue warns about blocked calls to privacy sensitive APIs via the
   # Selective Permissions Intervention.
   type SelectivePermissionsInterventionIssueDetails extends object
@@ -798,6 +813,7 @@ experimental domain Audits
       SelectivePermissionsInterventionIssue
       EmailVerificationRequestIssue
       LazyLoadImageIssue
+      WebInstallIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -834,6 +850,7 @@ experimental domain Audits
       optional SelectivePermissionsInterventionIssueDetails selectivePermissionsInterventionIssueDetails
       optional EmailVerificationRequestIssueDetails emailVerificationRequestIssueDetails
       optional LazyLoadImageIssueDetails lazyLoadImageIssueDetails
+      optional WebInstallIssueDetails webInstallIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 3509822c..39866855 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -827,6 +827,15 @@ domain DOM
       # List of popovers that were closed in order to respect popover stacking order.
       array of NodeId nodeIds
 
+  # Returns candidate nodes that are configured as triggers for the given popover.
+  experimental command getImplicitAnchorCandidates
+    parameters
+      # Id of the popover HTMLElement.
+      NodeId nodeId
+    returns
+      # Candidate elements that can invoke this popover.
+      array of BackendNodeId backendNodeIds
+
   # When enabling, this API forces an element to gain interest in its target,
   # keeping interest active until disabled.
   experimental command forceShowInterest
```

## Roll protocol to r1695952 — _2026-09-11T04:39:58.000Z_
######  Diff: [`bfb674c...9b417d8`](https://github.com/ChromeDevTools/devtools-protocol/compare/bfb674c...9b417d8)

```diff
@@ domains/ServiceWorker.pdl:33 @@ experimental domain ServiceWorker
       redundant
 
   # Mostly corresponds to `RouterCondition` in ServiceWorker spec
-  # (https://www.w3.org/TR/service-workers/#dictdef-routercondition) while this
-  # currently lacks support for the nested conditions ("or" and "not").
-  # TODO(crbug.com/540469610): Support recursive conditions.
+  # (https://www.w3.org/TR/service-workers/#dictdef-routercondition)
   type ServiceWorkerRouterCondition extends object
     properties
       # Plain text, or JSON serialization of URLPatternInit or URLPattern
@@ -44,6 +42,8 @@ experimental domain ServiceWorker
       optional string requestMode
       optional string requestDestination
       optional ServiceWorkerVersionRunningStatus runningStatus
+      optional array of ServiceWorkerRouterCondition or
+      optional ServiceWorkerRouterCondition not
 
   type ServiceWorkerRouterSourceType extends string
     enum
```

## Roll protocol to r1695166 — _2026-09-10T04:37:44.000Z_
######  Diff: [`7ad4320...bfb674c`](https://github.com/ChromeDevTools/devtools-protocol/compare/7ad4320...bfb674c)

```diff
@@ domains/Network.pdl:2168 @@ domain Network
         InvalidSessionParams
         RefreshFatalError
         DevTools
+        Replaced
 
   # Session event details specific to challenges.
   experimental type ChallengeEventDetails extends object
diff --git a/pdl/js_protocol.pdl b/pdl/js_protocol.pdl
index 62c15239..99905a48 100644
--- a/pdl/js_protocol.pdl
+++ b/pdl/js_protocol.pdl
@@ -1144,6 +1144,7 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        deferredmodule
         # blink's subtypes.
         trustedtype
       # Object class (constructor) name. Specified for `object` type values only.
@@ -1207,6 +1208,7 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        deferredmodule
         # blink's subtypes.
         trustedtype
       # String representation of the object.
@@ -1258,6 +1260,7 @@ domain Runtime
         dataview
         webassemblymemory
         wasmvalue
+        deferredmodule
         # blink's subtypes.
         trustedtype
```

## Roll protocol to r1694333 — _2026-09-09T04:39:12.000Z_
######  Diff: [`751d6d7...7ad4320`](https://github.com/ChromeDevTools/devtools-protocol/compare/751d6d7...7ad4320)

```diff
@@ js_protocol.pdl:143 @@ domain Debugger
       optional Location startLocation
       # Location in the source code where scope ends
       optional Location endLocation
+      # True if the scope does not declare any variables or have a runtime context.
+      # Only present if true.
+      # Empty scopes are retained in the scope chain because
+      # they can be targeted via `evaluateOnCallFrame` (using `scopeNumber`) or
+      # matched against scopes in source maps.
+      experimental optional boolean empty
 
   # Search match for resource.
   type SearchMatch extends object
```

## Roll protocol to r1693794 — _2026-09-08T15:15:54.000Z_
######  Diff: [`9077895...751d6d7`](https://github.com/ChromeDevTools/devtools-protocol/compare/9077895...751d6d7)

```diff
@@ domains/Audits.pdl:513 @@ experimental domain Audits
       UiDismissedNoEmbargo
       CorsError
       SuppressedBySegmentationPlatform
+      PopupBlockedByConnectionAllowlist
 
   type FederatedAuthUserInfoRequestIssueDetails extends object
     properties
```

## Roll protocol to r1692173 — _2026-09-04T04:40:14.000Z_
######  Diff: [`f4f1f32...9077895`](https://github.com/ChromeDevTools/devtools-protocol/compare/f4f1f32...9077895)

```diff
@@ domains/Emulation.pdl:322 @@ domain Emulation
       # useful for emulating mobile device orientation lock behavior in
       # responsive design mode.
       experimental optional boolean screenOrientationLockEmulation
+      # Viewport meta tag behavior. Default: `default`. Note: if `mobile` is `true`,
+      # the viewport meta tag is always enabled.
+      experimental optional enum viewportMeta
+        # Enables viewport meta tag processing.
+        enable
+        # Restores the default viewport meta behavior (disabled on desktop,
+        # enabled on mobile).
+        default
 
   # Start reporting the given posture value to the Device Posture API.
   # This override can also be set in setDeviceMetricsOverride().
```

## Roll protocol to r1691330 — _2026-09-03T05:31:05.000Z_
######  Diff: [`ea39a11...f4f1f32`](https://github.com/ChromeDevTools/devtools-protocol/compare/ea39a11...f4f1f32)

```diff
@@ domains/Audits.pdl:599 @@ experimental domain Audits
       TokenVerificationKbInvalidSdHash
       TokenVerificationKbMissingCnf
       TokenVerificationKbSignatureFailed
+      CrossOriginIframeNotSupported
 
   # This issue tracks client hints related issues. It's used to deprecate old
   # features, encourage the use of new ones, and provide general guidance.
```
