# Chrome DevTools Protocol changelog — 2025-06

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-06, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1479623 — _2025-06-27T04:31:59.000Z_
######  Diff: [`bdd3e90...097b400`](https://github.com/ChromeDevTools/devtools-protocol/compare/bdd3e90...097b400)

```diff
@@ browser_protocol.pdl:7671 @@ domain Network
 
   experimental type IPAddressSpace extends string
     enum
-      Local
+      Loopback
       Private
       Public
       Unknown
```

## Roll protocol to r1478340 — _2025-06-25T04:32:05.000Z_
######  Diff: [`3d7bae0...bdd3e90`](https://github.com/ChromeDevTools/devtools-protocol/compare/3d7bae0...bdd3e90)

```diff
@@ browser_protocol.pdl:1031 @@ experimental domain Audits
       # Additional information about the Partitioning Blob URL issue.
       PartitioningBlobURLInfo partitioningBlobURLInfo
 
-  type SelectElementAccessibilityIssueReason extends string
+  type ElementAccessibilityIssueReason extends string
     enum
       DisallowedSelectChild
       DisallowedOptGroupChild
       NonPhrasingContentOptionChild
       InteractiveContentOptionChild
       InteractiveContentLegendChild
+      InteractiveContentSummaryDescendant
 
-  # This issue warns about errors in the select element content model.
-  type SelectElementAccessibilityIssueDetails extends object
+  # This issue warns about errors in the select or summary element content model.
+  type ElementAccessibilityIssueDetails extends object
     properties
       DOM.BackendNodeId nodeId
-      SelectElementAccessibilityIssueReason selectElementAccessibilityIssueReason
+      ElementAccessibilityIssueReason elementAccessibilityIssueReason
       boolean hasDisallowedAttributes
 
   type StyleSheetLoadingIssueReason extends string
@@ -1120,7 +1121,7 @@ experimental domain Audits
       FederatedAuthUserInfoRequestIssue
       PropertyRuleIssue
       SharedDictionaryIssue
-      SelectElementAccessibilityIssue
+      ElementAccessibilityIssue
       SRIMessageSignatureIssue
       UserReidentificationIssue
 
@@ -1151,7 +1152,7 @@ experimental domain Audits
       optional PropertyRuleIssueDetails propertyRuleIssueDetails
       optional FederatedAuthUserInfoRequestIssueDetails federatedAuthUserInfoRequestIssueDetails
       optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
-      optional SelectElementAccessibilityIssueDetails selectElementAccessibilityIssueDetails
+      optional ElementAccessibilityIssueDetails elementAccessibilityIssueDetails
       optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
 
@@ -3517,7 +3518,8 @@ domain DOM
         # Get the popover target for a given element. In this case, this given
         # element can only be an HTMLFormControlElement (<input>, <button>).
         PopoverTarget
-        # Get the interest target for a given element.
+        # Get the interestfor target (the attribute used to be named
+        # `interesttarget`) for for a given element.
         InterestTarget
         # Get the commandfor target for a given element. In this case, this given
         # element can only be an HTMLButtonElement.
@@ -10060,6 +10062,7 @@ domain Page
       BroadcastChannel
       WebXR
       SharedWorker
+      SharedWorkerMessage
       WebLocks
       WebHID
       WebShare
```

## Roll protocol to r1477697 — _2025-06-24T04:32:08.000Z_
######  Diff: [`b6236d7...3d7bae0`](https://github.com/ChromeDevTools/devtools-protocol/compare/b6236d7...3d7bae0)

```diff
@@ browser_protocol.pdl:9720 @@ domain Page
   # Clears seeded compilation cache.
   experimental command clearCompilationCache
 
-  # Enum of possible auto-response for permission / prompt dialogs.
-  experimental type AutoResponseMode extends string
-    enum
-      none
-      autoAccept
-      autoReject
-      autoOptOut
-
   # Sets the Secure Payment Confirmation transaction mode.
   # https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
   experimental command setSPCTransactionMode
     parameters
-      AutoResponseMode mode
+      enum mode
+        none
+        autoAccept
+        autoChooseToAuthAnotherWay
+        autoReject
+        autoOptOut
 
   # Extensions for Custom Handlers API:
   # https://html.spec.whatwg.org/multipage/system-state.html#rph-automation
   experimental command setRPHRegistrationMode
     parameters
-      AutoResponseMode mode
+      enum mode
+        none
+        autoAccept
+        autoReject
 
   # Generates a report for testing.
   experimental command generateTestReport
```

## Roll protocol to r1475386 — _2025-06-18T04:31:55.000Z_
######  Diff: [`f9ae1d4...b6236d7`](https://github.com/ChromeDevTools/devtools-protocol/compare/f9ae1d4...b6236d7)

```diff
@@ browser_protocol.pdl:11541 @@ experimental domain Storage
       optional string netErrorName
       optional integer httpStatusCode
 
+  experimental event attributionReportingVerboseDebugReportSent
+    parameters
+      string url
+      optional array of object body
+      optional integer netError
+      optional string netErrorName
+      optional integer httpStatusCode
+
   # A single Related Website Set object.
   experimental type RelatedWebsiteSet extends object
     properties
@@ -13421,15 +13429,30 @@ experimental domain PWA
       integer badgeCount
       array of FileHandler fileHandlers
 
-  # Installs the given manifest identity, optionally using the given install_url
-  # or IWA bundle location.
+  # Installs the given manifest identity, optionally using the given installUrlOrBundleUrl
+  #
+  # IWA-specific install description:
+  # manifestId corresponds to isolated-app:// + web_package::SignedWebBundleId
+  #
+  # File installation mode:
+  # The installUrlOrBundleUrl can be either file:// or http(s):// pointing
+  # to a signed web bundle (.swbn). In this case SignedWebBundleId must correspond to
+  # The .swbn file's signing key.
+  #
+  # Dev proxy installation mode:
+  # installUrlOrBundleUrl must be http(s):// that serves dev mode IWA.
+  # web_package::SignedWebBundleId must be of type dev proxy.
+  #
+  # The advantage of dev proxy mode is that all changes to IWA
+  # automatically will be reflected in the running app without
+  # reinstallation.
+  #
+  # To generate bundle id for proxy mode:
+  # 1. Generate 32 random bytes.
+  # 2. Add a specific suffix 0x00 at the end.
+  # 3. Encode the entire sequence using Base32 without padding.
   #
-  # TODO(crbug.com/337872319) Support IWA to meet the following specific
-  # requirement.
-  # IWA-specific install description: If the manifest_id is isolated-app://,
-  # install_url_or_bundle_url is required, and can be either an http(s) URL or
-  # file:// URL pointing to a signed web bundle (.swbn). The .swbn file's
-  # signing key must correspond to manifest_id. If Chrome is not in IWA dev
+  # If Chrome is not in IWA dev
   # mode, the installation will fail, regardless of the state of the allowlist.
   command install
     parameters
```

## Roll protocol to r1473885 — _2025-06-14T04:31:36.000Z_
######  Diff: [`048403a...f9ae1d4`](https://github.com/ChromeDevTools/devtools-protocol/compare/048403a...f9ae1d4)

```diff
@@ browser_protocol.pdl:4467 @@ domain Emulation
       pause
       pauseIfNetworkFetchesPending
 
-  # Used to specify User Agent form-factor values. See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors
-  experimental type UserAgentFormFactor extends string
-    enum
-      Desktop
-      Automotive
-      Mobile
-      Tablet
-      XR
-      EInk
-      Watch
-
   # Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints
   experimental type UserAgentBrandVersion extends object
     properties
@@ -4500,7 +4489,9 @@ domain Emulation
       boolean mobile
       optional string bitness
       optional boolean wow64
-      optional array of UserAgentFormFactor formFactors
+      # Used to specify User Agent form-factor values.
+      # See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors
+      optional array of string formFactors
 
   # Used to specify sensor types to emulate.
   # See https://w3c.github.io/sensors/#automation for more information.
```

## Roll protocol to r1473367 — _2025-06-13T04:31:57.000Z_
######  Diff: [`8991629...048403a`](https://github.com/ChromeDevTools/devtools-protocol/compare/8991629...048403a)

```diff
@@ browser_protocol.pdl:6931 @@ domain Network
     properties
       # The outer response of signed HTTP exchange which was received from network.
       Response outerResponse
+      # Whether network response for the signed exchange was accompanied by
+      # extra headers.
+      boolean hasExtraInfo
       # Information about the signed exchange header.
       optional SignedExchangeHeader header
       # Security details for the signed exchange header.
```

## Roll protocol to r1472835 — _2025-06-12T04:31:40.000Z_
######  Diff: [`0d84894...8991629`](https://github.com/ChromeDevTools/devtools-protocol/compare/0d84894...8991629)

```diff
@@ browser_protocol.pdl:8653 @@ domain Page
       join-ad-interest-group
       keyboard-map
       language-detector
+      language-model
       local-fonts
       local-network-access
       magnetometer
```

## Roll protocol to r1472211 — _2025-06-11T04:31:52.000Z_
######  Diff: [`00f18fe...0d84894`](https://github.com/ChromeDevTools/devtools-protocol/compare/00f18fe...0d84894)

```diff
@@ browser_protocol.pdl:4467 @@ domain Emulation
       pause
       pauseIfNetworkFetchesPending
 
+  # Used to specify User Agent form-factor values. See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors
+  experimental type UserAgentFormFactor extends string
+    enum
+      Desktop
+      Automotive
+      Mobile
+      Tablet
+      XR
+      EInk
+      Watch
+
   # Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints
   experimental type UserAgentBrandVersion extends object
     properties
@@ -4489,6 +4500,7 @@ domain Emulation
       boolean mobile
       optional string bitness
       optional boolean wow64
+      optional array of UserAgentFormFactor formFactors
 
   # Used to specify sensor types to emulate.
   # See https://w3c.github.io/sensors/#automation for more information.
```

## Roll protocol to r1470888 — _2025-06-07T04:31:13.000Z_
######  Diff: [`2823d32...00f18fe`](https://github.com/ChromeDevTools/devtools-protocol/compare/2823d32...00f18fe)

```diff
@@ browser_protocol.pdl:4700 @@ domain Emulation
         protanopia
         tritanopia
 
+  # Emulates the given OS text scale.
+  command setEmulatedOSTextScale
+    parameters
+      optional number scale
+
   # Overrides the Geolocation Position or Error. Omitting latitude, longitude or
   # accuracy emulates position unavailable.
   command setGeolocationOverride
```

## Roll protocol to r1468520 — _2025-06-03T04:31:40.000Z_
######  Diff: [`c9a1a5d...2823d32`](https://github.com/ChromeDevTools/devtools-protocol/compare/c9a1a5d...2823d32)

```diff
@@ browser_protocol.pdl:8514 @@ domain Page
       AdFrameType adFrameType
       optional array of AdFrameExplanation explanations
 
-  # Identifies the bottom-most script which caused the frame to be labelled
-  # as an ad.
+  # Identifies the script which caused a script or frame to be labelled as an
+  # ad.
   experimental type AdScriptId extends object
     properties
-      # Script Id of the bottom-most script which caused the frame to be labelled
-      # as an ad.
+      # Script Id of the script which caused a script or frame to be labelled as
+      # an ad.
       Runtime.ScriptId scriptId
-      # Id of adScriptId's debugger.
+      # Id of scriptId's debugger.
       Runtime.UniqueDebuggerId debuggerId
 
+  # Encapsulates the script ancestry and the root script filterlist rule that
+  # caused the frame to be labelled as an ad. Only created when `ancestryChain`
+  # is not empty.
+  experimental type AdScriptAncestry extends object
+    properties
+      # A chain of `AdScriptId`s representing the ancestry of an ad script that
+      # led to the creation of a frame. The chain is ordered from the script
+      # itself (lower level) up to its root ancestor that was flagged by
+      # filterlist.
+      array of AdScriptId ancestryChain
+      # The filterlist rule that caused the root (last) script in
+      # `ancestryChain` to be ad-tagged. Only populated if the rule is
+      # available.
+      optional string rootScriptFilterlistRule
+
   # Indicates whether the frame is a secure context and why it is the case.
   experimental type SecureContextType extends string
     enum
@@ -9291,15 +9306,16 @@ domain Page
       # Recommendation for manifest's id attribute to match current id computed from start_url
       optional string recommendedId
 
-  experimental command getAdScriptAncestryIds
+  experimental command getAdScriptAncestry
     parameters
       FrameId frameId
     returns
       # The ancestry chain of ad script identifiers leading to this frame's
-      # creation, ordered from the most immediate script (in the frame creation
+      # creation, along with the root script's filterlist rule. The ancestry
+      # chain is ordered from the most immediate script (in the frame creation
       # stack) to more distant ancestors (that created the immediately preceding
       # script). Only sent if frame is labelled as an ad and ids are available.
-      array of AdScriptId adScriptAncestryIds
+      optional AdScriptAncestry adScriptAncestry
 
   # Returns present frame tree structure.
   command getFrameTree
```
