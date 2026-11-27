# Chrome DevTools Protocol changelog — 2026-05

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-05, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1638949 — _2026-05-30T05:38:26.000Z_
######  Diff: [`2f5c261...0efa44f`](https://github.com/ChromeDevTools/devtools-protocol/compare/2f5c261...0efa44f)

```diff
@@ browser_protocol.pdl:9 @@ version
   minor 3
 
 include domains/Accessibility.pdl
+include domains/Ads.pdl
 include domains/Animation.pdl
 include domains/Audits.pdl
 include domains/Autofill.pdl
diff --git a/pdl/domains/Ads.pdl b/pdl/domains/Ads.pdl
new file mode 100644
index 00000000..d15b209d
--- /dev/null
+++ b/pdl/domains/Ads.pdl
@@ -0,0 +1,33 @@
+# Copyright 2026 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+
+# A domain for ad-related metrics and data.
+experimental domain Ads
+  depends on Network
+  depends on Page
+  depends on Runtime
+
+  # Ad metrics for a page.
+  type AdMetrics extends object
+    properties
+      # The viewport ad density by area, represented as a percentage (an integer
+      # between 0 and 100).
+      integer viewportAdDensityByArea
+      # The time-weighted average of the viewport ad density by area, measured
+      # across the duration of the page.
+      number averageViewportAdDensityByArea
+      # The number of ads currently visible within the viewport.
+      integer viewportAdCount
+      # The time-weighted average of the viewport ad count, measured across the
+      # duration of the page.
+      number averageViewportAdCount
+      # The total ad CPU usage, in milliseconds.
+      number totalAdCpuTime
+      # The total ad network bytes.
+      number totalAdNetworkBytes
+
+  # Retrieves ad metrics for the current page.
+  command getAdMetrics
+    returns
+      AdMetrics metrics
diff --git a/pdl/domains/Audits.pdl b/pdl/domains/Audits.pdl
index 14148cd8..548281f0 100644
--- a/pdl/domains/Audits.pdl
+++ b/pdl/domains/Audits.pdl
@@ -592,6 +592,17 @@ experimental domain Audits
       WellKnownMissingAccountsEndpoint
       UserLoggedOut
       WellKnownAccountsEndpointCrossOrigin
+      AccountsHttpNotFound
+      AccountsNoResponse
+      AccountsInvalidResponse
+      AccountsInvalidContentType
+      AccountsEmptyList
+      EmailVerificationWellKnownHttpNotFound
+      EmailVerificationWellKnownNoResponse
+      EmailVerificationWellKnownInvalidResponse
+      EmailVerificationWellKnownInvalidContentType
+      JwksHttpNotFound
+      JwksInvalidResponse
 
   # This issue tracks client hints related issues. It's used to deprecate old
   # features, encourage the use of new ones, and provide general guidance.
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index 5efa7d88..40ba279d 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -258,6 +258,7 @@ experimental domain Preload
       # The prefetch finished successfully but was never used.
       PrefetchSuccessfulButNotUsed
       PrefetchNotUsedProbeFailed
+      PrefetchCancelledOnUserNavigation
 
   # Fired when a prefetch attempt is updated.
   event prefetchStatusUpdated
```

## Roll protocol to r1638241 — _2026-05-29T05:50:04.000Z_
######  Diff: [`c2ef27f...2f5c261`](https://github.com/ChromeDevTools/devtools-protocol/compare/c2ef27f...2f5c261)

```diff
@@ domains/Target.pdl:349 @@ domain Target
       # This can be the page or tab target ID.
       TargetID targetId
       # The id of the panel we want DevTools to open initially. Currently
-      # supported panels are elements, console, network, sources, resources
-      # and performance.
+      # supported panels are elements, console, network, sources, resources,
+      # timeline, chrome-recorder, heap-profiler, lighthouse, and security.
       optional string panelId
     returns
       # The targetId of DevTools page target.
```

## Roll protocol to r1637485 — _2026-05-28T05:49:23.000Z_
######  Diff: [`7919a58...c2ef27f`](https://github.com/ChromeDevTools/devtools-protocol/compare/7919a58...c2ef27f)

```diff
@@ domains/Network.pdl:2228 @@ domain Network
       InvalidFederatedSessionProviderFailedToRestoreKey
       FailedToUnwrapKey
       SessionDeletedDuringRefresh
+      CrossOriginRegistrationSiteNotIncluded
 
   # Details about a failed device bound session network request.
   experimental type DeviceBoundSessionFailedRequest extends object
```

## Roll protocol to r1636713 — _2026-05-27T05:50:56.000Z_
######  Diff: [`b6b27f6...7919a58`](https://github.com/ChromeDevTools/devtools-protocol/compare/b6b27f6...7919a58)

```diff
@@ domains/Audits.pdl:316 @@ experimental domain Audits
       WriteErrorNonSecureContext
       WriteErrorNonStringIdField
       WriteErrorNonStringInMatchDestList
+      WriteErrorInvalidMatchDestList
       WriteErrorNonStringMatchField
       WriteErrorNonTokenTypeField
       WriteErrorRequestAborted
@@ -560,6 +561,38 @@ experimental domain Audits
       InvalidAccountsResponse
       NoReturningUserFromFetchedAccounts
 
+  type EmailVerificationRequestIssueDetails extends object
+    properties
+      EmailVerificationRequestIssueReason emailVerificationRequestIssueReason
+
+  # Represents the failure reason when an email verification request fails.
+  # Should be updated alongside EmailVerificationRequestResult in
+  # third_party/blink/public/mojom/devtools/inspector_issue.mojom.
+  type EmailVerificationRequestIssueReason extends string
+    enum
+      InvalidEmail
+      DnsFetchFailed
+      DnsInvalidRecord
+      WellKnownHttpNotFound
+      WellKnownNoResponse
+      WellKnownInvalidResponse
+      WellKnownListEmpty
+      WellKnownInvalidContentType
+      WellKnownMissingIssuanceEndpoint
+      WellKnownIssuanceEndpointCrossOrigin
+      WellKnownUnsupportedSigningAlgorithm
+      TokenHttpNotFound
+      TokenNoResponse
+      TokenInvalidResponse
+      TokenInvalidContentType
+      TokenMalformedSdJwt
+      TokenInvalidSdJwt
+      KeyBindingSigningFailed
+      RpOriginIsOpaque
+      WellKnownMissingAccountsEndpoint
+      UserLoggedOut
+      WellKnownAccountsEndpointCrossOrigin
+
   # This issue tracks client hints related issues. It's used to deprecate old
   # features, encourage the use of new ones, and provide general guidance.
   type ClientHintIssueDetails extends object
@@ -743,6 +776,7 @@ experimental domain Audits
       PermissionElementIssue
       PerformanceIssue
       SelectivePermissionsInterventionIssue
+      EmailVerificationRequestIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -778,6 +812,7 @@ experimental domain Audits
       optional PermissionElementIssueDetails permissionElementIssueDetails
       optional PerformanceIssueDetails performanceIssueDetails
       optional SelectivePermissionsInterventionIssueDetails selectivePermissionsInterventionIssueDetails
+      optional EmailVerificationRequestIssueDetails emailVerificationRequestIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
```

## Roll protocol to r1635485 — _2026-05-24T05:45:30.000Z_
######  Diff: [`e47d08c...b6b27f6`](https://github.com/ChromeDevTools/devtools-protocol/compare/e47d08c...b6b27f6)

```diff
@@ domains/Emulation.pdl:436 @@ domain Emulation
       PressureSource source
       optional PressureMetadata metadata
 
-  # TODO: OBSOLETE: To remove when setPressureDataOverride is merged.
   # Provides a given pressure state that will be processed and eventually be
   # delivered to PressureObserver users. |source| must have been previously
   # overridden by setPressureSourceOverrideEnabled.
@@ -445,15 +444,6 @@ domain Emulation
       PressureSource source
       PressureState state
 
-  # Provides a given pressure data set that will be processed and eventually be
-  # delivered to PressureObserver users. |source| must have been previously
-  # overridden by setPressureSourceOverrideEnabled.
-  experimental command setPressureDataOverride
-    parameters
-      PressureSource source
-      PressureState state
-      optional number ownContributionEstimate
-
   # Overrides the Idle state.
   command setIdleOverride
     parameters
```

## Roll protocol to r1634055 — _2026-05-21T05:48:46.000Z_
######  Diff: [`357026f...e47d08c`](https://github.com/ChromeDevTools/devtools-protocol/compare/357026f...e47d08c)

```diff
@@ domains/Target.pdl:36 @@ domain Target
       # Provides additional details for specific target types. For example, for
       # the type of "page", this may be set to "prerender".
       experimental optional string subtype
+      # Embedder-specific target metadata. This is only set for targets of
+      # type "tab".
+      experimental optional object embedderData
 
   # A filter used by target query/discovery/auto-attach operations.
   experimental type FilterEntry extends object
```

## Roll protocol to r1629771 — _2026-05-13T05:38:01.000Z_
######  Diff: [`f223775...bbfe84d`](https://github.com/ChromeDevTools/devtools-protocol/compare/f223775...bbfe84d)

```diff
@@ domains/Audits.pdl:346 @@ experimental domain Audits
       ValidationFailedInvalidLength
       ValidationFailedSignatureMismatch
       ValidationFailedIntegrityMismatch
+      SignatureBaseUnknownDerivedComponent
+      SignatureBaseMissingHeader
+      SignatureBaseInvalidUnencodedDigest
+      SignatureBaseUnsupportedComponent
 
   type UnencodedDigestError extends string
     enum
diff --git a/pdl/domains/Preload.pdl b/pdl/domains/Preload.pdl
index 411401ea..5efa7d88 100644
--- a/pdl/domains/Preload.pdl
+++ b/pdl/domains/Preload.pdl
@@ -191,6 +191,7 @@ experimental domain Preload
       BrowsingDataRemoved
       PrerenderHostReused
       FormSubmitWhenPrerendering
+      CrossDocumentRestart
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
diff --git a/pdl/domains/SmartCardEmulation.pdl b/pdl/domains/SmartCardEmulation.pdl
index 3daf2503..9d3d96d9 100644
--- a/pdl/domains/SmartCardEmulation.pdl
+++ b/pdl/domains/SmartCardEmulation.pdl
@@ -47,7 +47,6 @@ experimental domain SmartCardEmulation
       shutdown
 
       # Maps to SCARD_E_UNKNOWN_CARD.
-      # TODO(crbug.com/472114998): Rename Mojo's kUnknownError to kUnknownCard to match.
       unknown-card
 
       # Error code that is not mapped in this enum.
```

## Roll protocol to r1628107 — _2026-05-09T05:30:25.000Z_
######  Diff: [`b3d7e08...145f3d6`](https://github.com/ChromeDevTools/devtools-protocol/compare/b3d7e08...145f3d6)

```diff
@@ domains/Audits.pdl:425 @@ experimental domain Audits
       FormInputHasWrongButWellIntendedAutocompleteValueError
       ResponseWasBlockedByORB
       NavigationEntryMarkedSkippable
+      BackUINavigationWouldSkipAd
       AutofillAndManualTextPolicyControlledFeaturesInfo
       AutofillPolicyControlledFeatureInfo
       ManualTextPolicyControlledFeatureInfo
```

## Roll protocol to r1627472 — _2026-05-08T05:18:19.000Z_
######  Diff: [`6e7b094...b3d7e08`](https://github.com/ChromeDevTools/devtools-protocol/compare/6e7b094...b3d7e08)

```diff
@@ domains/CSS.pdl:338 @@ experimental domain CSS
   experimental type CSSContainerQuery extends object
     properties
       # Container query text.
-      string text
+      # Contains the query part without the container name for a single query.
+      # Deprecated in favor of conditionText which contains the full prelude
+      # after @container.
+      deprecated string text
       # The associated rule header range in the enclosing stylesheet (if
       # available).
       optional SourceRange range
@@ -354,6 +357,8 @@ experimental domain CSS
       optional boolean queriesScrollState
       # true if the query contains anchored() queries.
       optional boolean queriesAnchored
+      # CSSContainerRule.conditionText
+      string conditionText
 
   # CSS Supports at-rule descriptor.
   experimental type CSSSupports extends object
@@ -927,7 +932,17 @@ experimental domain CSS
       CSSMedia media
 
   # Modifies the expression of a container query.
-  experimental command setContainerQueryText
+  # Deprecated. Use setContainerQueryConditionText instead.
+  experimental deprecated command setContainerQueryText
+    parameters
+      DOM.StyleSheetId styleSheetId
+      SourceRange range
+      string text
+    returns
+      # The resulting CSS container query rule after modification.
+      CSSContainerQuery containerQuery
+
+  experimental command setContainerQueryConditionText
     parameters
       DOM.StyleSheetId styleSheetId
       SourceRange range
```

## Roll protocol to r1625959 — _2026-05-06T05:34:33.000Z_
######  Diff: [`8feb4e1...6e7b094`](https://github.com/ChromeDevTools/devtools-protocol/compare/8feb4e1...6e7b094)

```diff
@@ domains/CSS.pdl:523 @@ experimental domain CSS
         font-face
         font-feature-values
         font-palette-values
+        counter-style
       # Subsection of font-feature-values, if this is a subsection.
       optional enum subsection
         # LINT.IfChange(FontVariantAlternatesFeatureType)
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index a32732d7..88ee5bcd 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -2162,6 +2162,7 @@ domain Network
       Success
       KeyError
       SigningError
+      TransientSigningError
       ServerRequestedTermination
       InvalidSessionId
       InvalidChallenge
@@ -2260,13 +2261,14 @@ domain Network
       # The result of a refresh.
       enum refreshResult
         Refreshed
-        RefreshedAsWaiter
         InitializedService
         Unreachable
         ServerError
         RefreshQuotaExceeded
         FatalError
         SigningQuotaExceeded
+        RefreshedAsWaiter
+        TransientSigningError
       # If there was a fetch attempt, the result of that.
       optional DeviceBoundSessionFetchResult fetchResult
       # The session display if there was a newly created session. This is populated
```

## Roll protocol to r1624250 — _2026-05-02T05:22:23.000Z_
######  Diff: [`470fb6a...8feb4e1`](https://github.com/ChromeDevTools/devtools-protocol/compare/470fb6a...8feb4e1)

```diff
@@ domains/Page.pdl:168 @@ domain Page
       sub-apps
       summarizer
       sync-xhr
+      tools
       translator
       unload
       usb
```
