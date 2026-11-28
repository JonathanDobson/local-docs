# Chrome DevTools Protocol changelog — 2026-06

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-06, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1654583 — _2026-06-30T05:49:23.000Z_
######  Diff: [`3c5658b...5b82e41`](https://github.com/ChromeDevTools/devtools-protocol/compare/3c5658b...5b82e41)

```diff
@@ domains/Audits.pdl:743 @@ experimental domain Audits
       FontSizeTooSmall
       FontSizeTooLarge
       InvalidSizeValue
+      NonSecureContext
+      MissingTransientUserActivation
 
   # This issue warns about improper usage of the <permission> element.
   type PermissionElementIssueDetails extends object
```

## Roll protocol to r1652909 — _2026-06-26T05:49:04.000Z_
######  Diff: [`ebe045b...888fb74`](https://github.com/ChromeDevTools/devtools-protocol/compare/ebe045b...888fb74)

```diff
@@ domains/Ads.pdl:8 @@ experimental domain Ads
   depends on Page
   depends on Runtime
 
+  # Ad frame data.
+  type AdFrameData extends object
+    properties
+      # The DevTools frame token.
+      Page.FrameId frameId
+      # The initial origin of the frame. To minimize the payload size, this is
+      # only sent once per frame.
+      optional string initialOrigin
+      # The network bytes of the frame.
+      number networkBytes
+      # The CPU time of the frame, in milliseconds.
+      number cpuTime
+
   # Ad metrics for a page.
   type AdMetrics extends object
     properties
@@ -26,6 +39,10 @@ experimental domain Ads
       number totalAdCpuTime
       # The total ad network bytes.
       number totalAdNetworkBytes
+      # The list of ad frames that have been updated since the last event.
+      array of AdFrameData updateAdFrames
+      # The list of ad frame IDs that have been removed since the last event.
+      array of Page.FrameId removeAdFrames
 
   # Retrieves ad metrics for the current page.
   command getAdMetrics
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 40e65bca..76ea8ee3 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -76,8 +76,10 @@ domain DOM
       file-selector-button
       details-content
       picker
+      select-listbox
       permission-icon
       overscroll-area-parent
+      overscroll-backdrop
       skeleton
 
   # Shadow root type.
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index ecde9ae4..414867f5 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -640,6 +640,13 @@ domain Page
       # Whether or not universal access should be granted to the isolated world. This is a powerful
       # option, use with caution.
       optional boolean grantUniveralAccess
+      # An optional content security policy to set for the isolated world.
+      # If omitted, any existing CSP for the world will be cleared.
+      # Note that clearing or updating the CSP does not immediately affect the active
+      # context in the same document because LocalDOMWindow caches the
+      # ContentSecurityPolicy object. The change takes effect on subsequent
+      # navigations when a new window context is created.
+      optional string contentSecurityPolicy
     returns
       # Execution context of the isolated world.
       Runtime.ExecutionContextId executionContextId
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index 1783c582..222ac760 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -173,13 +173,11 @@ domain Target
       # present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or
       # `background: false`. The life-time of the tab is limited to the life-time of the session.
       experimental optional boolean hidden
-      # If specified, the option is used to determine if the new target should
-      # be focused or not. By default, the focus behavior depends on the
-      # value of the background field. For example, background=false and focus=false
-      # will result in the target tab being opened but the browser window remain
-      # unchanged (if it was in the background, it will remain in the background)
-      # and background=false with focus=undefined will result in the window being focused.
-      # Using background: true and focus: true is not supported and will result in an error.
+      # If specified, determines whether the new target should be focused.
+      # By default, the focus behavior depends on the `background` parameter:
+      # - If `background` is false (default) and `focus` is omitted, the new target is focused and the browser window is brought to the foreground.
+      # - If `background` is false and `focus` is false, the target is opened but the browser window's focus remains unchanged (e.g., if the window was in the background, it stays there).
+      # - If `background` is true, setting `focus` to true is not supported and will result in an error.
       experimental optional boolean focus
     returns
       # The id of the page opened.
diff --git a/pdl/domains/Tracing.pdl b/pdl/domains/Tracing.pdl
index 5103577e..d070f3a9 100644
--- a/pdl/domains/Tracing.pdl
+++ b/pdl/domains/Tracing.pdl
@@ -130,6 +130,17 @@ domain Tracing
       experimental optional binary perfettoConfig
       # Backend type (defaults to `auto`)
       experimental optional TracingBackend tracingBackend
+      # Maximum width and height (in pixels) of each captured screenshot.
+      # Only used when the `disabled-by-default-devtools.screenshot` category is
+      # enabled. Defaults to 500. The combined memory footprint of screenshots
+      # (`screenshotMaxSize` * `screenshotMaxSize` * 4 * `screenshotMaxCount`)
+      # is clamped to the existing per-session budget.
+      experimental optional integer screenshotMaxSize
+      # Maximum number of screenshots captured during a single tracing session.
+      # Only used when the `disabled-by-default-devtools.screenshot` category is
+      # enabled. Defaults to 450. Clamped together with `screenshotMaxSize` to
+      # stay within the per-session screenshot memory budget.
+      experimental optional integer screenshotMaxCount
 
   experimental event bufferUsage
     parameters
```

## Roll protocol to r1651496 — _2026-06-24T05:48:07.000Z_
######  Diff: [`42c3c57...ebe045b`](https://github.com/ChromeDevTools/devtools-protocol/compare/42c3c57...ebe045b)

```diff
@@ domains/Audits.pdl:604 @@ experimental domain Audits
       JwksHttpNotFound
       JwksInvalidResponse
       TokenVerificationSdJwtUnsupportedHeaderAlg
+      TokenVerificationSdJwtInvalidTyp
       TokenVerificationSdJwtMissingIss
       TokenVerificationSdJwtMissingIat
       TokenVerificationSdJwtMissingCnf
diff --git a/pdl/domains/Overlay.pdl b/pdl/domains/Overlay.pdl
index 8ef51bbb..33144933 100644
--- a/pdl/domains/Overlay.pdl
+++ b/pdl/domains/Overlay.pdl
@@ -208,6 +208,36 @@ experimental domain Overlay
       # The content box highlight outline color (default: transparent).
       optional DOM.RGBA outlineColor
 
+  # Supported display cutout shapes.
+  type DisplayCutoutShape extends string
+    enum
+      pill
+      notch
+      circle
+      rectangle
+
+  # Configuration for a display cutout.
+  type DisplayCutoutConfig extends object
+    properties
+      # A rectangle representing the cutout bounds.
+      DOM.Rect rect
+      # Shape used to draw the cutout.
+      DisplayCutoutShape shape
+      # Border radius for rounded cutout shapes.
+      optional integer borderRadius
+      # Upper shoulder radius for notch cutout shapes.
+      optional integer upperRadius
+      # Lower transition radius for notch cutout shapes.
+      optional integer lowerRadius
+      # Center x coordinate for circle cutout shapes.
+      optional integer cx
+      # Center y coordinate for circle cutout shapes.
+      optional integer cy
+      # Radius for circle cutout shapes.
+      optional integer radius
+      # The cutout fill color (default: black).
+      optional DOM.RGBA contentColor
+
   # Configuration for Window Controls Overlay
   type WindowControlsOverlayConfig extends object
     properties
@@ -476,6 +506,12 @@ experimental domain Overlay
       # hinge data, null means hideHinge
       optional HingeConfig hingeConfig
 
+  # Add a display cutout overlay.
+  command setShowDisplayCutout
+    parameters
+      # display cutout data, null means hide display cutout
+      optional DisplayCutoutConfig displayCutoutConfig
+
   # Show elements in isolation mode with overlays.
   command setShowIsolatedElements
     parameters
```

## Roll protocol to r1648812 — _2026-06-18T06:03:26.000Z_
######  Diff: [`fc77610...42c3c57`](https://github.com/ChromeDevTools/devtools-protocol/compare/fc77610...42c3c57)

```diff
@@ domains/Network.pdl:738 @@ domain Network
       None
       # The cookie should have been blocked by 3PCD but is exempted by explicit user setting.
       UserSetting
-      # The cookie should have been blocked by 3PCD but is exempted by metadata mitigation.
-      TPCDMetadata
-      # The cookie should have been blocked by 3PCD but is exempted by Deprecation Trial mitigation.
-      TPCDDeprecationTrial
-      # The cookie should have been blocked by 3PCD but is exempted by Top-level Deprecation Trial mitigation.
-      TopLevelTPCDDeprecationTrial
-      # The cookie should have been blocked by 3PCD but is exempted by heuristics mitigation.
-      TPCDHeuristics
       # The cookie should have been blocked by 3PCD but is exempted by Enterprise Policy.
       EnterprisePolicy
       # The cookie should have been blocked by 3PCD but is exempted by Storage Access API.
```

## Roll protocol to r1648091 — _2026-06-17T06:06:09.000Z_
######  Diff: [`8ac781c...fc77610`](https://github.com/ChromeDevTools/devtools-protocol/compare/8ac781c...fc77610)

```diff
@@ domains/CSS.pdl:82 @@ experimental domain CSS
       # Specificity of the selector.
       experimental optional Specificity specificity
 
+  # Contribution of an individual simple selector to specificity.
+  experimental type SpecificityComponent extends object
+    properties
+      # The simple selector text that contributes to specificity.
+      string text
+      # The a component contribution.
+      integer a
+      # The b component contribution.
+      integer b
+      # The c component contribution.
+      integer c
+
   # Specificity:
   # https://drafts.csswg.org/selectors/#specificity-rules
   experimental type Specificity extends object
@@ -93,6 +105,8 @@ experimental domain CSS
       integer b
       # The c component, which represents the number of type selectors and pseudo-elements.
       integer c
+      # Per-simple-selector contributions used to explain this specificity.
+      experimental optional array of SpecificityComponent components
 
   # Selector list data.
   type SelectorList extends object
```

## Roll protocol to r1646372 — _2026-06-13T05:51:22.000Z_
######  Diff: [`838337e...1857dd0`](https://github.com/ChromeDevTools/devtools-protocol/compare/838337e...1857dd0)

```diff
@@ domains/Page.pdl:117 @@ domain Page
       digital-credentials-get
       direct-sockets
       direct-sockets-multicast
-      direct-sockets-private
       display-capture
       document-domain
       encrypted-media
```

## Roll protocol to r1643702 — _2026-06-09T05:48:31.000Z_
######  Diff: [`8aa0e0f...838337e`](https://github.com/ChromeDevTools/devtools-protocol/compare/8aa0e0f...838337e)

```diff
@@ domains/DOM.pdl:816 @@ domain DOM
       # If true, opens the popover and keeps it open. If false, closes the
       # popover if it was previously force-opened.
       boolean enable
+      # Optional ID of the element invoking this popover, used to establish the implicit anchor.
+      # If not provided, it will fall back to the first invoker in the document, preferring
+      # elements with a popovertarget attribute over those with a commandfor attribute. Note that
+      # if there are multiple invokers, this is just an estimate.
+      optional BackendNodeId invokerNodeId
     returns
       # List of popovers that were closed in order to respect popover stacking order.
       array of NodeId nodeIds
```

## Roll protocol to r1642743 — _2026-06-06T05:42:10.000Z_
######  Diff: [`5ad5530...8aa0e0f`](https://github.com/ChromeDevTools/devtools-protocol/compare/5ad5530...8aa0e0f)

```diff
@@ domains/Page.pdl:175 @@ domain Page
       usb-unrestricted
       vertical-scroll
       web-app-installation
+      webnn
       web-printing
       web-share
       window-management
```

## Roll protocol to r1640722 — _2026-06-03T06:04:43.000Z_
######  Diff: [`ef4da13...5ad5530`](https://github.com/ChromeDevTools/devtools-protocol/compare/ef4da13...5ad5530)

```diff
@@ domains/DOM.pdl:78 @@ domain DOM
       picker
       permission-icon
       overscroll-area-parent
+      skeleton
 
   # Shadow root type.
   type ShadowRootType extends string
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index 40ba279d..b26790f8 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -234,6 +234,7 @@ experimental domain Preload
       PrefetchIneligibleRetryAfter
       PrefetchIsPrivacyDecoy
       PrefetchIsStale
+      PrefetchNotEligibleBlockedByConnectionAllowlist
       PrefetchNotEligibleBrowserContextOffTheRecord
       PrefetchNotEligibleDataSaverEnabled
       PrefetchNotEligibleExistingProxy
```

## Roll protocol to r1639953 — _2026-06-02T06:00:45.000Z_
######  Diff: [`0efa44f...ef4da13`](https://github.com/ChromeDevTools/devtools-protocol/compare/0efa44f...ef4da13)

```diff
@@ domains/Audits.pdl:603 @@ experimental domain Audits
       EmailVerificationWellKnownInvalidContentType
       JwksHttpNotFound
       JwksInvalidResponse
+      TokenVerificationSdJwtUnsupportedHeaderAlg
+      TokenVerificationSdJwtMissingIss
+      TokenVerificationSdJwtMissingIat
+      TokenVerificationSdJwtMissingCnf
+      TokenVerificationSdJwtMissingEmail
+      TokenVerificationSdJwtInvalidIssuedAt
+      TokenVerificationSdJwtInvalidIssuer
+      TokenVerificationSdJwtJwksMissingKeys
+      TokenVerificationSdJwtSignatureFailed
+      TokenVerificationSdJwtInvalidEmailVerified
+      TokenVerificationSdJwtInvalidEmail
+      TokenVerificationSdJwtInvalidHolderKey
+      TokenVerificationKbInvalidTyp
+      TokenVerificationKbMissingAud
+      TokenVerificationKbMissingNonce
+      TokenVerificationKbMissingIat
+      TokenVerificationKbMissingSdHash
+      TokenVerificationKbInvalidIssuedAt
+      TokenVerificationKbInvalidAudience
+      TokenVerificationKbInvalidNonce
+      TokenVerificationKbInvalidSdHash
+      TokenVerificationKbMissingCnf
+      TokenVerificationKbSignatureFailed
 
   # This issue tracks client hints related issues. It's used to deprecate old
   # features, encourage the use of new ones, and provide general guidance.
```
