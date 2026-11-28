# Chrome DevTools Protocol changelog — 2026-07

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-07, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1670834 — _2026-07-30T05:25:53.000Z_
######  Diff: [`6fe72ec...6f1723f`](https://github.com/ChromeDevTools/devtools-protocol/compare/6fe72ec...6f1723f)

```diff
@@ domains/Network.pdl:2258 @@ domain Network
   experimental type RefreshEventDetails extends object
     properties
       # The result of a refresh.
+      # LINT.IfChange(DeviceBoundSessionRefreshResult)
       enum refreshResult
         Refreshed
         InitializedService
@@ -2267,6 +2268,8 @@ domain Network
         SigningQuotaExceeded
         RefreshedAsWaiter
         TransientSigningError
+        InScopeRefreshNotYetNeeded
+      # LINT.ThenChange(//net/device_bound_sessions/refresh_result.h:DeviceBoundSessionRefreshResult,//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionRefreshResult)
       # If there was a fetch attempt, the result of that.
       optional DeviceBoundSessionFetchResult fetchResult
       # The session display if there was a newly created session. This is populated
```

## Roll protocol to r1669207 — _2026-07-28T05:33:24.000Z_
######  Diff: [`a9544e3...6fe72ec`](https://github.com/ChromeDevTools/devtools-protocol/compare/a9544e3...6fe72ec)

```diff
@@ domains/WebAuthn.pdl:98 @@ experimental domain WebAuthn
       # An opaque byte sequence with a maximum size of 64 bytes mapping the
       # credential to a specific user.
       optional binary userHandle
-      # Signature counter. This is incremented by one for each successful
-      # assertion.
+      # Signature counter. Must be equal to or greater than -1.
+      # If -1, the credential won't have an associated signature counter, and
+      # every assertion operation will report a value of 0.
       # See https://w3c.github.io/webauthn/#signature-counter
-      integer signCount
+      optional integer signCount
       # The large blob associated with the credential.
       # See https://w3c.github.io/webauthn/#sctn-large-blob-extension
       optional binary largeBlob
@@ -224,6 +225,11 @@ experimental domain WebAuthn
       optional boolean backupState
       optional integer activeCmtgKeyIndex
       optional boolean generateCmtgKeyOnNextOperation
+      # Must be equal to or greater than -1.
+      # If -1, the signature counter is removed from the credential, and every
+      # assertion operation will report a value of 0.
+      # See https://w3c.github.io/webauthn/#signature-counter
+      optional integer signCount
 
   # Triggered when a credential is added to an authenticator.
   event credentialAdded
```

## Roll protocol to r1666840 — _2026-07-23T05:37:45.000Z_
######  Diff: [`8ff84ba...a9544e3`](https://github.com/ChromeDevTools/devtools-protocol/compare/8ff84ba...a9544e3)

```diff
@@ domains/WebAuthn.pdl:222 @@ experimental domain WebAuthn
       binary credentialId
       optional boolean backupEligibility
       optional boolean backupState
+      optional integer activeCmtgKeyIndex
+      optional boolean generateCmtgKeyOnNextOperation
 
   # Triggered when a credential is added to an authenticator.
   event credentialAdded
```

## Roll protocol to r1666022 — _2026-07-22T05:31:07.000Z_
######  Diff: [`3bd8f01...8ff84ba`](https://github.com/ChromeDevTools/devtools-protocol/compare/3bd8f01...8ff84ba)

```diff
@@ domains/Storage.pdl:21 @@ experimental domain Storage
       websql
       service_workers
       cache_storage
-      interest_groups
       shared_storage
       storage_buckets
       all
diff --git a/pdl/domains/WebAuthn.pdl b/pdl/domains/WebAuthn.pdl
index 0b3700ef..ffa0d262 100644
--- a/pdl/domains/WebAuthn.pdl
+++ b/pdl/domains/WebAuthn.pdl
@@ -66,6 +66,11 @@ experimental domain WebAuthn
       # https://fidoalliance.org/specs/fido-v2.2-rd-20241003/fido-client-to-authenticator-protocol-v2.2-rd-20241003.html#sctn-hmac-secret-make-cred-extension
       # Defaults to false.
       optional boolean hasHmacSecretMc
+      # If set to true, the authenticator will support the cmtgKey (Credential
+      # Manager Trust Group Key) extension.
+      # https://github.com/w3c/webauthn/pull/2377
+      # Defaults to false.
+      optional boolean hasCmtgKey
       # If set to true, tests of user presence will succeed immediately.
       # Otherwise, they will not be resolved. Defaults to true.
       optional boolean automaticPresenceSimulation
@@ -115,6 +120,12 @@ experimental domain WebAuthn
       # not set.
       # https://w3c.github.io/webauthn/#dom-publickeycredentialuserentity-displayname
       optional string userDisplayName
+      # The CMTG keys associated with the credential.
+      optional array of binary cmtgKeys
+      # The 0-based index of the active key in cmtgKeys.
+      optional integer activeCmtgKeyIndex
+      # If true, the authenticator will generate a new CMTG key on the next operation.
+      optional boolean generateCmtgKeyOnNextOperation
 
   # Enable the WebAuthn domain and start intercepting credential storage and
   # retrieval with a virtual authenticator.
```

## Roll protocol to r1663043 — _2026-07-16T05:25:38.000Z_
######  Diff: [`2c7c583...3bd8f01`](https://github.com/ChromeDevTools/devtools-protocol/compare/2c7c583...3bd8f01)

```diff
@@ domains/Audits.pdl:124 @@ experimental domain Audits
 
   type MixedContentResourceType extends string
     enum
-      AttributionSrc
       Audio
       Beacon
       CSPReport
diff --git a/pdl/domains/Browser.pdl b/pdl/domains/Browser.pdl
index 6015a945..b1555691 100644
--- a/pdl/domains/Browser.pdl
+++ b/pdl/domains/Browser.pdl
@@ -332,21 +332,3 @@ domain Browser
   command addPrivacySandboxEnrollmentOverride
     parameters
       string url
-
-  experimental type PrivacySandboxAPI extends string
-    enum
-      BiddingAndAuctionServices
-      TrustedKeyValue
-
-  # Configures encryption keys used with a given privacy sandbox API to talk
-  # to a trusted coordinator.  Since this is intended for test automation only,
-  # coordinatorOrigin must be a .test domain. No existing coordinator
-  # configuration for the origin may exist.
-  command addPrivacySandboxCoordinatorKeyConfig
-    parameters
-      PrivacySandboxAPI api
-      string coordinatorOrigin
-      string keyConfig
-      # BrowserContext to perform the action in. When omitted, default browser
-      # context is used.
-      optional BrowserContextID browserContextId
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index 100e94d7..6018c22a 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -42,45 +42,12 @@ experimental domain Storage
       string issuerOrigin
       number count
 
-  # Protected audience interest group auction identifier.
-  type InterestGroupAuctionId extends string
-
-  # Enum of interest group access types.
-  type InterestGroupAccessType extends string
-    enum
-      join
-      leave
-      update
-      loaded
-      bid
-      win
-      additionalBid
-      additionalBidWin
-      topLevelBid
-      topLevelAdditionalBid
-      clear
-
-  # Enum of auction events.
-  type InterestGroupAuctionEventType extends string
-    enum
-      started
-      configResolved
-
-  # Enum of network fetches auctions can do.
-  type InterestGroupAuctionFetchType extends string
-    enum
-      bidderJs
-      bidderWasm
-      sellerJs
-      bidderTrustedSignals
-      sellerTrustedSignals
 
   # Enum of shared storage access scopes.
   type SharedStorageAccessScope extends string
     enum
       window
       sharedStorageWorklet
-      protectedAudienceWorklet
       header
 
   # Enum of shared storage access methods.
@@ -385,29 +352,6 @@ experimental domain Storage
       # True if any tokens were deleted, false otherwise.
       boolean didDeleteTokens
 
-  # Gets details for a named interest group.
-  experimental command getInterestGroupDetails
-    parameters
-      string ownerOrigin
-      string name
-    returns
-      # This largely corresponds to:
-      # https://wicg.github.io/turtledove/#dictdef-generatebidinterestgroup
-      # but has absolute expirationTime instead of relative lifetimeMs and
-      # also adds joiningOrigin.
-      object details
-
-  # Enables/Disables issuing of interestGroupAccessed events.
-  experimental command setInterestGroupTracking
-    parameters
-      boolean enable
-
-  # Enables/Disables issuing of interestGroupAuctionEventOccurred and
-  # interestGroupAuctionNetworkRequestCreated.
-  experimental command setInterestGroupAuctionTracking
-    parameters
-      boolean enable
-
   # Gets metadata for an origin's shared storage.
   experimental command getSharedStorageMetadata
     parameters
@@ -515,48 +459,6 @@ experimental domain Storage
       # Storage bucket to update.
       string bucketId
 
-  # One of the interest groups was accessed. Note that these events are global
-  # to all targets sharing an interest group store.
-  event interestGroupAccessed
-    parameters
-      Network.TimeSinceEpoch accessTime
-      InterestGroupAccessType type
-      string ownerOrigin
-      string name
-      # For topLevelBid/topLevelAdditionalBid, and when appropriate,
-      # win and additionalBidWin
-      optional string componentSellerOrigin
-      # For bid or somethingBid event, if done locally and not on a server.
-      optional number bid
-      optional string bidCurrency
-      # For non-global events --- links to interestGroupAuctionEvent
-      optional InterestGroupAuctionId uniqueAuctionId
-
-  # An auction involving interest groups is taking place. These events are
-  # target-specific.
-  event interestGroupAuctionEventOccurred
-    parameters
-      Network.TimeSinceEpoch eventTime
-      InterestGroupAuctionEventType type
-      InterestGroupAuctionId uniqueAuctionId
-      # Set for child auctions.
-      optional InterestGroupAuctionId parentAuctionId
-      # Set for started and configResolved
-      optional object auctionConfig
-
-  # Specifies which auctions a particular network fetch may be related to, and
-  # in what role. Note that it is not ordered with respect to
-  # Network.requestWillBeSent (but will happen before loadingFinished
-  # loadingFailed).
-  event interestGroupAuctionNetworkRequestCreated
-    parameters
-      InterestGroupAuctionFetchType type
-      Network.RequestId requestId
-      # This is the set of the auctions using the worklet that issued this
-      # request.  In the case of trusted signals, it's possible that only some of
-      # them actually care about the keys being queried.
-      array of InterestGroupAuctionId auctions
-
   # Shared storage was accessed by the associated page.
   # The following parameters are included in all events.
   event sharedStorageAccessed
@@ -621,9 +523,3 @@ experimental domain Storage
   experimental command getRelatedWebsiteSets
     returns
       array of RelatedWebsiteSet sets
-
-  command setProtectedAudienceKAnonymity
-    parameters
-      string owner
-      string name
-      array of binary hashes
```

## Roll protocol to r1662358 — _2026-07-15T05:18:52.000Z_
######  Diff: [`0837097...2c7c583`](https://github.com/ChromeDevTools/devtools-protocol/compare/0837097...2c7c583)

```diff
@@ domains/Audits.pdl:270 @@ experimental domain Audits
       optional Network.IPAddressSpace resourceIPAddressSpace
       optional Network.ClientSecurityState clientSecurityState
 
-  type AttributionReportingIssueType extends string
-    enum
-      PermissionPolicyDisabled
-      UntrustworthyReportingOrigin
-      InsecureContext
-      # TODO(apaseltiner): Rename this to InvalidRegisterSourceHeader
-      InvalidHeader
-      InvalidRegisterTriggerHeader
-      SourceAndTriggerHeaders
-      SourceIgnored
-      TriggerIgnored
-      OsSourceIgnored
-      OsTriggerIgnored
-      InvalidRegisterOsSourceHeader
-      InvalidRegisterOsTriggerHeader
-      WebAndOsHeaders
-      NoWebOrOsSupport
-      NavigationRegistrationWithoutTransientUserActivation
-      InvalidInfoHeader
-      NoRegisterSourceHeader
-      NoRegisterTriggerHeader
-      NoRegisterOsSourceHeader
-      NoRegisterOsTriggerHeader
-      NavigationRegistrationUniqueScopeAlreadySet
-
   type SharedDictionaryError extends string
     enum
       UseErrorCrossOriginNoCorsRequest
@@ -368,15 +343,6 @@ experimental domain Audits
       ReportingEndpointNotToken
       InvalidUrlPattern
 
-  # Details for issues around "Attribution Reporting API" usage.
-  # Explainer: https://github.com/WICG/attribution-reporting-api
-  type AttributionReportingIssueDetails extends object
-    properties
-      AttributionReportingIssueType violationType
-      optional AffectedRequest request
-      optional DOM.BackendNodeId violatingNodeId
-      optional string invalidParameter
-
 # Details for issues about documents in Quirks Mode
 # or Limited Quirks Mode that affects page layouting.
   type QuirksModeIssueDetails extends object
@@ -778,6 +744,16 @@ experimental domain Audits
       # The stack trace at the time of the intervention.
       optional Runtime.StackTrace stackTrace
 
+  # Details for issues about lazy-loaded images without explicit dimensions.
+  type LazyLoadImageIssueDetails extends object
+    properties
+      # DOM node of the problematic HTMLImageElement.
+      DOM.BackendNodeId nodeId
+      # URL or src attribute of the image.
+      string url
+      # Frame containing the image.
+      Page.FrameId frameId
+
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
   # information about the kind of issue.
@@ -790,7 +766,6 @@ experimental domain Audits
       ContentSecurityPolicyIssue
       SharedArrayBufferIssue
       CorsIssue
-      AttributionReportingIssue
       QuirksModeIssue
       PartitioningBlobURLIssue
       # Deprecated
@@ -814,6 +789,7 @@ experimental domain Audits
       PerformanceIssue
       SelectivePermissionsInterventionIssue
       EmailVerificationRequestIssue
+      LazyLoadImageIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -827,7 +803,6 @@ experimental domain Audits
       optional ContentSecurityPolicyIssueDetails contentSecurityPolicyIssueDetails
       optional SharedArrayBufferIssueDetails sharedArrayBufferIssueDetails
       optional CorsIssueDetails corsIssueDetails
-      optional AttributionReportingIssueDetails attributionReportingIssueDetails
       optional QuirksModeIssueDetails quirksModeIssueDetails
       optional PartitioningBlobURLIssueDetails partitioningBlobURLIssueDetails
       deprecated optional NavigatorUserAgentIssueDetails navigatorUserAgentIssueDetails
@@ -850,6 +825,7 @@ experimental domain Audits
       optional PerformanceIssueDetails performanceIssueDetails
       optional SelectivePermissionsInterventionIssueDetails selectivePermissionsInterventionIssueDetails
       optional EmailVerificationRequestIssueDetails emailVerificationRequestIssueDetails
+      optional LazyLoadImageIssueDetails lazyLoadImageIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 414867f5..26941081 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -74,7 +74,6 @@ domain Page
       all-screens-capture
       ambient-light-sensor
       aria-notify
-      attribution-reporting
       autofill
       autoplay
       bluetooth
```

## Roll protocol to r1660672 — _2026-07-11T05:25:49.000Z_
######  Diff: [`f6ba0b1...0837097`](https://github.com/ChromeDevTools/devtools-protocol/compare/f6ba0b1...0837097)

```diff
@@ domains/Network.pdl:2263 @@ domain Network
         InitializedService
         Unreachable
         ServerError
-        RefreshQuotaExceeded
         FatalError
         SigningQuotaExceeded
         RefreshedAsWaiter
```

## Roll protocol to r1658499 — _2026-07-08T05:32:02.000Z_
######  Diff: [`d71b8c6...f6ba0b1`](https://github.com/ChromeDevTools/devtools-protocol/compare/d71b8c6...f6ba0b1)

```diff
@@ domains/Network.pdl:2223 @@ domain Network
       FailedToUnwrapKey
       SessionDeletedDuringRefresh
       CrossOriginRegistrationSiteNotIncluded
+      InvalidPreProvisionedKeyInitiatorMissing
+      PreProvisionedKeyAccessNotGranted
+      PreProvisionedKeyNotFound
   # LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult)
 
   # Details about a failed device bound session network request.
```

## Roll protocol to r1657692 — _2026-07-07T05:51:00.000Z_
######  Diff: [`29e7238...d71b8c6`](https://github.com/ChromeDevTools/devtools-protocol/compare/29e7238...d71b8c6)

```diff
@@ domains/DigitalCredentials.pdl:26 @@ experimental domain DigitalCredentials
       # The response data object returned by the wallet.
       # Required when |action| is "respond", forbidden otherwise.
       optional object response
+      # The frame to scope the virtual wallet behavior to.
+      optional Page.FrameId frameId
```

## Roll protocol to r1656784 — _2026-07-04T05:37:09.000Z_
######  Diff: [`a0ec9b1...29e7238`](https://github.com/ChromeDevTools/devtools-protocol/compare/a0ec9b1...29e7238)

```diff
@@ domains/DigitalCredentials.pdl:7 @@ @@ -7,7 +7,7 @@
 # This domain allows interacting with the Digital Credentials API for automation.
 experimental domain DigitalCredentials
   # The type of virtual wallet action.
-  type VirtualWalletBehavior extends string
+  type VirtualWalletAction extends string
     enum
       respond
       decline
@@ -18,11 +18,11 @@ experimental domain DigitalCredentials
   # issued from this frame.
   command setVirtualWalletBehavior
     parameters
-      # The behavior of the virtual wallet.
-      VirtualWalletBehavior behavior
-      # The protocol identifier (e.g. "openid4vp"). Required when |behavior| is
+      # The action of the virtual wallet.
+      VirtualWalletAction action
+      # The protocol identifier (e.g. "openid4vp"). Required when |action| is
       # "respond", forbidden otherwise.
       optional string protocol
       # The response data object returned by the wallet.
-      # Required when |behavior| is "respond", forbidden otherwise.
+      # Required when |action| is "respond", forbidden otherwise.
       optional object response
```

## Roll protocol to r1655900 — _2026-07-02T05:43:39.000Z_
######  Diff: [`5b82e41...a0ec9b1`](https://github.com/ChromeDevTools/devtools-protocol/compare/5b82e41...a0ec9b1)

```diff
@@ browser_protocol.pdl:26 @@ include domains/DOMSnapshot.pdl
 include domains/DOMStorage.pdl
 include domains/DeviceAccess.pdl
 include domains/DeviceOrientation.pdl
+include domains/DigitalCredentials.pdl
 include domains/Emulation.pdl
 include domains/EventBreakpoints.pdl
 include domains/Extensions.pdl
diff --git a/pdl/domains/DigitalCredentials.pdl b/pdl/domains/DigitalCredentials.pdl
new file mode 100644
index 00000000..0ace20a0
--- /dev/null
+++ b/pdl/domains/DigitalCredentials.pdl
@@ -0,0 +1,28 @@
+# Copyright 2026 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+#
+# Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp
+
+# This domain allows interacting with the Digital Credentials API for automation.
+experimental domain DigitalCredentials
+  # The type of virtual wallet action.
+  type VirtualWalletBehavior extends string
+    enum
+      respond
+      decline
+      wait
+      clear
+
+  # Sets the behavior of the virtual wallet for digital credential requests
+  # issued from this frame.
+  command setVirtualWalletBehavior
+    parameters
+      # The behavior of the virtual wallet.
+      VirtualWalletBehavior behavior
+      # The protocol identifier (e.g. "openid4vp"). Required when |behavior| is
+      # "respond", forbidden otherwise.
+      optional string protocol
+      # The response data object returned by the wallet.
+      # Required when |behavior| is "respond", forbidden otherwise.
+      optional object response
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 7a54d715..e535e5bf 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -2149,10 +2149,12 @@ domain Network
   experimental type DeviceBoundSessionEventId extends string
 
   # A fetch result for a device bound session creation or refresh.
+  # LINT.IfChange(DeviceBoundSessionFetchResult)
   experimental type DeviceBoundSessionFetchResult extends string
     enum
       Success
-      KeyError
+      SigningKeyGenerationError
+      AttestationKeyGenerationError
       SigningError
       TransientSigningError
       ServerRequestedTermination
@@ -2221,6 +2223,7 @@ domain Network
       FailedToUnwrapKey
       SessionDeletedDuringRefresh
       CrossOriginRegistrationSiteNotIncluded
+  # LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult)
 
   # Details about a failed device bound session network request.
   experimental type DeviceBoundSessionFailedRequest extends object
```
