# Chrome DevTools Protocol changelog — 2026-03

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-03, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1604597 — _2026-03-25T05:02:28.000Z_
######  Diff: [`94a770f...1abe750`](https://github.com/ChromeDevTools/devtools-protocol/compare/94a770f...1abe750)

```diff
@@ browser_protocol.pdl:18 @@ include domains/Browser.pdl
 include domains/CSS.pdl
 include domains/CacheStorage.pdl
 include domains/Cast.pdl
+include domains/CrashReportContext.pdl
 include domains/DOM.pdl
 include domains/DOMDebugger.pdl
 include domains/DOMSnapshot.pdl
diff --git a/pdl/domains/CrashReportContext.pdl b/pdl/domains/CrashReportContext.pdl
new file mode 100644
index 00000000..27b3702f
--- /dev/null
+++ b/pdl/domains/CrashReportContext.pdl
@@ -0,0 +1,20 @@
+# Copyright 2026 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+
+# This domain exposes the current state of the CrashReportContext API.
+experimental domain CrashReportContext
+  depends on Page
+
+  # Key-value pair in CrashReportContext.
+  type CrashReportContextEntry extends object
+    properties
+      string key
+      string value
+      # The ID of the frame where the key-value pair was set.
+      Page.FrameId frameId
+
+  # Returns all entries in the CrashReportContext across all frames in the page.
+  command getEntries
+    returns
+      array of CrashReportContextEntry entries
```

## Roll protocol to r1603894 — _2026-03-24T05:02:01.000Z_
######  Diff: [`169ca38...94a770f`](https://github.com/ChromeDevTools/devtools-protocol/compare/169ca38...94a770f)

```diff
@@ domains/WebMCP.pdl:11 @@ experimental domain WebMCP
 
   # Tool annotations
   type Annotation extends object
+
     properties
       # A hint indicating that the tool does not modify any state.
       optional boolean readOnly
       # If the declarative tool was declared with the autosubmit attribute.
       optional boolean autosubmit
 
+  # Represents the status of a tool invocation.
+  type InvocationStatus extends string
+    enum
+      Success
+      Canceled
+      Error
+
   # Definition of a tool that can be invoked.
   type Tool extends object
     properties
@@ -51,3 +59,30 @@ experimental domain WebMCP
     parameters
       # Array of tools that were removed.
       array of Tool tools
+
+  # Event fired when a tool invocation starts.
+  event toolInvoked
+    parameters
+      # Name of the tool to invoke.
+      string toolName
+      # Frame id
+      Page.FrameId frameId
+      # Invocation identifier.
+      string invocationId
+      # The input parameters used for the invocation.
+      string input
+
+  # Event fired when a tool invocation completes or fails.
+  event toolResponded
+    parameters
+      # Invocation identifier.
+      string invocationId
+      # Status of the invocation.
+      InvocationStatus status
+      # Output or error delivered as delivered to the agent. Missing if `status` is anything other than Success.
+      optional object output
+      # Error text for protocol users.
+      optional string errorText
+      # The exception object, if the javascript tool threw an error>
+      optional Runtime.RemoteObject exception
+
```

## Roll protocol to r1602427 — _2026-03-20T04:57:27.000Z_
######  Diff: [`7a16bec...169ca38`](https://github.com/ChromeDevTools/devtools-protocol/compare/7a16bec...169ca38)

```diff
@@ domains/DOM.pdl:13 @@ @@ -13,6 +13,7 @@
 # corresponding document elements as their child nodes.
 domain DOM
   depends on Runtime
+  depends on Network
 
   # Unique DOM node identifier.
   type NodeId extends integer
@@ -184,7 +185,7 @@ domain DOM
       experimental optional boolean isScrollable
       experimental optional boolean affectedByStartingStyles
       experimental optional array of StyleSheetId adoptedStyleSheets
-      experimental optional boolean isAdRelated
+      experimental optional Network.AdProvenance adProvenance
 
   # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
   type DetachedElementInfo extends object
@@ -919,8 +920,8 @@ domain DOM
     parameters
       # The id of the node.
       DOM.NodeId nodeId
-      # If the node is ad related.
-      boolean isAdRelated
+      # The provenance of the ad related node, if it is ad related.
+      optional Network.AdProvenance adProvenance
 
   # Fired when a node's starting styles changes.
   experimental event affectedByStartingStylesFlagUpdated
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 504edfe8..a03d977b 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -1825,6 +1825,19 @@ domain Network
       # `ancestryChain` to be tagged as an ad.
       optional string rootScriptFilterlistRule
 
+  # Represents the provenance of an ad resource or element. Only one of
+  # `filterlistRule` or `adScriptAncestry` can be set. If `filterlistRule`
+  # is provided, the resource URL directly matches a filter list rule. If
+  # `adScriptAncestry` is provided, an ad script initiated the resource fetch or
+  # appended the element to the DOM. If neither is provided, the entity is
+  # known to be an ad, but provenance tracking information is unavailable.
+  experimental type AdProvenance extends object
+    properties
+      # The filterlist rule that matched, if any.
+      optional string filterlistRule
+      # The script ancestry that created the ad, if any.
+      optional AdAncestry adScriptAncestry
+
   # Fired when additional information about a requestWillBeSent event is available from the
   # network stack. Not every requestWillBeSent event will have an additional
   # requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
```

## Roll protocol to r1601756 — _2026-03-19T05:02:00.000Z_
######  Diff: [`e653604...7a16bec`](https://github.com/ChromeDevTools/devtools-protocol/compare/e653604...7a16bec)

```diff
@@ domains/CSS.pdl:602 @@ experimental domain CSS
       array of CSSFunctionParameter parameters
       # Function body.
       array of CSSFunctionNode children
+      # The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule.
+      experimental optional DOM.BackendNodeId originTreeScopeNodeId
 
   # CSS keyframe rule representation.
   type CSSKeyframeRule extends object
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index e42956a9..79b8cfce 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -41,6 +41,7 @@ domain DOM
       checkmark
       before
       after
+      expand-icon
       picker-icon
       interest-hint
       marker
diff --git a/pdl/domains/WebAuthn.pdl b/pdl/domains/WebAuthn.pdl
index 0ef007ce..0b3700ef 100644
--- a/pdl/domains/WebAuthn.pdl
+++ b/pdl/domains/WebAuthn.pdl
@@ -20,6 +20,7 @@ experimental domain WebAuthn
     enum
       ctap2_0
       ctap2_1
+      ctap2_2
 
   type AuthenticatorTransport extends string
     enum
@@ -57,6 +58,14 @@ experimental domain WebAuthn
       # https://w3c.github.io/webauthn/#prf-extension
       # Defaults to false.
       optional boolean hasPrf
+      # If set to true, the authenticator will support the hmac-secret extension.
+      # https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-hmac-secret-extension
+      # Defaults to false.
+      optional boolean hasHmacSecret
+      # If set to true, the authenticator will support the hmac-secret-mc extension.
+      # https://fidoalliance.org/specs/fido-v2.2-rd-20241003/fido-client-to-authenticator-protocol-v2.2-rd-20241003.html#sctn-hmac-secret-make-cred-extension
+      # Defaults to false.
+      optional boolean hasHmacSecretMc
       # If set to true, tests of user presence will succeed immediately.
       # Otherwise, they will not be resolved. Defaults to true.
       optional boolean automaticPresenceSimulation
```

## Roll protocol to r1601035 — _2026-03-18T05:02:54.000Z_
######  Diff: [`0c3ac05...e653604`](https://github.com/ChromeDevTools/devtools-protocol/compare/0c3ac05...e653604)

```diff
@@ domains/Audits.pdl:688 @@ experimental domain Audits
       # Used for messages about activation disabled reason
       optional string disableReason
 
-  # Metadata about the ad script that was on the stack that caused the current
-  # script in the `AdAncestry` to be considered ad related.
-  type AdScriptIdentifier extends object
-    properties
-      # The script's v8 identifier.
-      Runtime.ScriptId scriptId
-      # v8's debugging id for the v8::Context.
-      Runtime.UniqueDebuggerId debuggerId
-      # The script's url (or generated name based on id if inline script).
-      string name
-
-  # Providence about how an ad script was determined to be such. It is an ad
-  # because its url matched a filterlist rule, or because some other ad script
-  # was on the stack when this script was loaded.
-  type AdAncestry extends object
-    properties
-      # The ad-script in the stack when the offending script was loaded. This is
-      # recursive down to the root script that was tagged due to the filterlist
-      # rule.
-      array of AdScriptIdentifier adAncestryChain
-      # The filterlist rule that caused the root (last) script in
-      # `adAncestry` to be ad-tagged.
-      optional string rootScriptFilterlistRule
-
   # The issue warns about blocked calls to privacy sensitive APIs via the
   # Selective Permissions Intervention.
   type SelectivePermissionsInterventionIssueDetails extends object
@@ -719,7 +695,7 @@ experimental domain Audits
       # Which API was intervened on.
       string apiName
       # Why the ad script using the API is considered an ad.
-      AdAncestry adAncestry
+      Network.AdAncestry adAncestry
       # The stack trace at the time of the intervention.
       optional Runtime.StackTrace stackTrace
 
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index de36ac7c..504edfe8 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -1799,6 +1799,32 @@ domain Network
       IPAddressSpace initiatorIPAddressSpace
       LocalNetworkAccessRequestPolicy localNetworkAccessRequestPolicy
 
+  # Identifies the script on the stack that caused a resource or element to be
+  # labeled as an ad. For resources, this indicates the context that triggered
+  # the fetch. For elements, this indicates the context that caused the element
+  # to be appended to the DOM.
+  experimental type AdScriptIdentifier extends object
+    properties
+      # The script's V8 identifier.
+      Runtime.ScriptId scriptId
+      # V8's debugging ID for the v8::Context.
+      Runtime.UniqueDebuggerId debuggerId
+      # The script's url (or generated name based on id if inline script).
+      string name
+
+  # Encapsulates the script ancestry and the root script filter list rule that
+  # caused the resource or element to be labeled as an ad.
+  experimental type AdAncestry extends object
+    properties
+      # A chain of `AdScriptIdentifier`s representing the ancestry of an ad
+      # script that led to the creation of a resource or element. The chain is
+      # ordered from the script itself (lowest level) up to its root ancestor
+      # that was flagged by a filter list.
+      array of AdScriptIdentifier ancestryChain
+      # The filter list rule that caused the root (last) script in
+      # `ancestryChain` to be tagged as an ad.
+      optional string rootScriptFilterlistRule
+
   # Fired when additional information about a requestWillBeSent event is available from the
   # network stack. Not every requestWillBeSent event will have an additional
   # requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 76d6ed49..12734a90 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -36,31 +36,6 @@ domain Page
       AdFrameType adFrameType
       optional array of AdFrameExplanation explanations
 
-  # Identifies the script which caused a script or frame to be labelled as an
-  # ad.
-  experimental type AdScriptId extends object
-    properties
-      # Script Id of the script which caused a script or frame to be labelled as
-      # an ad.
-      Runtime.ScriptId scriptId
-      # Id of scriptId's debugger.
-      Runtime.UniqueDebuggerId debuggerId
-
-  # Encapsulates the script ancestry and the root script filterlist rule that
-  # caused the frame to be labelled as an ad. Only created when `ancestryChain`
-  # is not empty.
-  experimental type AdScriptAncestry extends object
-    properties
-      # A chain of `AdScriptId`s representing the ancestry of an ad script that
-      # led to the creation of a frame. The chain is ordered from the script
-      # itself (lower level) up to its root ancestor that was flagged by
-      # filterlist.
-      array of AdScriptId ancestryChain
-      # The filterlist rule that caused the root (last) script in
-      # `ancestryChain` to be ad-tagged. Only populated if the rule is
-      # available.
-      optional string rootScriptFilterlistRule
-
   # Indicates whether the frame is a secure context and why it is the case.
   experimental type SecureContextType extends string
     enum
@@ -843,7 +818,7 @@ domain Page
       # chain is ordered from the most immediate script (in the frame creation
       # stack) to more distant ancestors (that created the immediately preceding
       # script). Only sent if frame is labelled as an ad and ids are available.
-      optional AdScriptAncestry adScriptAncestry
+      optional Network.AdAncestry adScriptAncestry
 
   # Returns present frame tree structure.
   command getFrameTree
diff --git a/pdl/domains/SmartCardEmulation.pdl b/pdl/domains/SmartCardEmulation.pdl
new file mode 100644
index 00000000..3daf2503
--- /dev/null
+++ b/pdl/domains/SmartCardEmulation.pdl
@@ -0,0 +1,405 @@
+# Copyright 2025 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+#
+# Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp
+# This domain allows to emulate smart card readers and cards,
+# bypassing the need for physical hardware.
+
+experimental domain SmartCardEmulation
+
+  # Indicates the PC/SC error code.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__ErrorCodes.html
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/secauthn/authentication-return-values
+  type ResultCode extends string
+    enum
+      success
+      removed-card
+      reset-card
+      unpowered-card
+      unresponsive-card
+      unsupported-card
+      reader-unavailable
+      sharing-violation
+      not-transacted
+      no-smartcard
+      proto-mismatch
+      system-cancelled
+      not-ready
+      cancelled
+      insufficient-buffer
+      invalid-handle
+      invalid-parameter
+      invalid-value
+      no-memory
+      timeout
+      unknown-reader
+      unsupported-feature
+      no-readers-available
+      service-stopped
+      no-service
+      comm-error
+      internal-error
+      server-too-busy
+      unexpected
+      shutdown
+
+      # Maps to SCARD_E_UNKNOWN_CARD.
+      # TODO(crbug.com/472114998): Rename Mojo's kUnknownError to kUnknownCard to match.
+      unknown-card
+
+      # Error code that is not mapped in this enum.
+      unknown
+
+  # Maps to the |SCARD_SHARE_*| values.
+  type ShareMode extends string
+    enum
+      shared
+      exclusive
+      direct
+
+  # Indicates what the reader should do with the card.
+  type Disposition extends string
+    enum
+      leave-card
+      reset-card
+      unpower-card
+      eject-card
+
+  # Maps to |SCARD_*| connection state values.
+  type ConnectionState extends string
+    enum
+      absent
+      present
+      swallowed
+      powered
+      negotiable
+      specific
+
+  # Maps to the |SCARD_STATE_*| flags.
+  type ReaderStateFlags extends object
+    properties
+      optional boolean unaware
+      optional boolean ignore
+      optional boolean changed
+      optional boolean unknown
+      optional boolean unavailable
+      optional boolean empty
+      optional boolean present
+      optional boolean exclusive
+      optional boolean inuse
+      optional boolean mute
+      optional boolean unpowered
+
+  # Maps to the |SCARD_PROTOCOL_*| flags.
+  type ProtocolSet extends object
+    properties
+      optional boolean t0
+      optional boolean t1
+      optional boolean raw
+
+  # Maps to the |SCARD_PROTOCOL_*| values.
+  type Protocol extends string
+    enum
+      t0
+      t1
+      raw
+
+  type ReaderStateIn extends object
+    properties
+      string reader
+      ReaderStateFlags currentState
+      integer currentInsertionCount
+
+  type ReaderStateOut extends object
+    properties
+      string reader
+      ReaderStateFlags eventState
+      integer eventCount
+      binary atr
+
+  # Enables the |SmartCardEmulation| domain.
+  command enable
+
+  # Disables the |SmartCardEmulation| domain.
+  command disable
+
+  # Reports the successful result of a |SCardEstablishContext| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext
+  command reportEstablishContextResult
+    parameters
+      string requestId
+      integer contextId
+
+  # Reports the successful result of a |SCardReleaseContext| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext
+  command reportReleaseContextResult
+    parameters
+      string requestId
+
+  # Reports the successful result of a |SCardListReaders| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa
+  command reportListReadersResult
+    parameters
+      string requestId
+      array of string readers
+
+  # Reports the successful result of a |SCardGetStatusChange| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea
+  command reportGetStatusChangeResult
+    parameters
+      string requestId
+      array of ReaderStateOut readerStates
+
+  # Reports the result of a |SCardBeginTransaction| call.
+  # On success, this creates a new transaction object.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction
+  command reportBeginTransactionResult
+    parameters
+      string requestId
+      integer handle
+
+  # Reports the successful result of a call that returns only a result code.
+  # Used for: |SCardCancel|, |SCardDisconnect|, |SCardSetAttrib|, |SCardEndTransaction|.
+  #
+  # This maps to:
+  # 1. SCardCancel
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel
+  #
+  # 2. SCardDisconnect
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect
+  #
+  # 3. SCardSetAttrib
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib
+  #
+  # 4. SCardEndTransaction
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction
+  command reportPlainResult
+    parameters
+      string requestId
+
+  # Reports the successful result of a |SCardConnect| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta
+  command reportConnectResult
+    parameters
+      string requestId
+      integer handle
+      optional Protocol activeProtocol
+
+  # Reports the successful result of a call that sends back data on success.
+  # Used for |SCardTransmit|, |SCardControl|, and |SCardGetAttrib|.
+  #
+  # This maps to:
+  # 1. SCardTransmit
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit
+  #
+  # 2. SCardControl
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol
+  #
+  # 3. SCardGetAttrib
+  #    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602
+  #    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib
+  command reportDataResult
+    parameters
+      string requestId
+      binary data
+
+  # Reports the successful result of a |SCardStatus| call.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa
+  command reportStatusResult
+    parameters
+      string requestId
+      string readerName
+      ConnectionState state
+      binary atr
+      optional Protocol protocol
+
+  # Reports an error result for the given request.
+  command reportError
+    parameters
+      string requestId
+      ResultCode resultCode
+
+  # Fired when |SCardEstablishContext| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext
+  event establishContextRequested
+    parameters
+      string requestId
+
+  # Fired when |SCardReleaseContext| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext
+  event releaseContextRequested
+    parameters
+      string requestId
+      integer contextId
+
+  # Fired when |SCardListReaders| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa
+  event listReadersRequested
+    parameters
+      string requestId
+      integer contextId
+
+  # Fired when |SCardGetStatusChange| is called. Timeout is specified in milliseconds.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea
+  event getStatusChangeRequested
+    parameters
+      string requestId
+      integer contextId
+      array of ReaderStateIn readerStates
+
+      # in milliseconds, if absent, it means "infinite"
+      optional integer timeout
+
+  # Fired when |SCardCancel| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel
+  event cancelRequested
+    parameters
+      string requestId
+      integer contextId
+
+  # Fired when |SCardConnect| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta
+  event connectRequested
+    parameters
+      string requestId
+      integer contextId
+      string reader
+      ShareMode shareMode
+      ProtocolSet preferredProtocols
+
+  # Fired when |SCardDisconnect| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect
+  event disconnectRequested
+    parameters
+      string requestId
+      integer handle
+      Disposition disposition
+
+  # Fired when |SCardTransmit| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit
+  event transmitRequested
+    parameters
+      string requestId
+      integer handle
+      binary data
+      optional Protocol protocol
+
+  # Fired when |SCardControl| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol
+  event controlRequested
+    parameters
+      string requestId
+      integer handle
+      integer controlCode
+      binary data
+
+  # Fired when |SCardGetAttrib| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib
+  event getAttribRequested
+    parameters
+      string requestId
+      integer handle
+      integer attribId
+
+  # Fired when |SCardSetAttrib| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib
+  event setAttribRequested
+    parameters
+      string requestId
+      integer handle
+      integer attribId
+      binary data
+
+  # Fired when |SCardStatus| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa
+  event statusRequested
+    parameters
+      string requestId
+      integer handle
+
+  # Fired when |SCardBeginTransaction| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction
+  event beginTransactionRequested
+    parameters
+      string requestId
+      integer handle
+
+  # Fired when |SCardEndTransaction| is called.
+  #
+  # This maps to:
+  # PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b
+  # Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction
+  event endTransactionRequested
+    parameters
+      string requestId
+      integer handle
+      Disposition disposition
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
new file mode 100644
index 00000000..2ddf07ff
--- /dev/null
+++ b/pdl/domains/WebMCP.pdl
@@ -0,0 +1,53 @@
+# Copyright 2026 The Chromium Authors
+# Use of this source code is governed by a BSD-style license that can be
+# found in the LICENSE file.
+#
+# Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp
+
+experimental domain WebMCP
+  depends on Runtime
+  depends on Page
+  depends on DOM
+
+  # Tool annotations
+  type Annotation extends object
+    properties
+      # A hint indicating that the tool does not modify any state.
+      optional boolean readOnly
+      # If the declarative tool was declared with the autosubmit attribute.
+      optional boolean autosubmit
+
+  # Definition of a tool that can be invoked.
+  type Tool extends object
+    properties
+      # Tool name.
+      string name
+      # Tool description.
+      string description
+      # Schema for the tool's input parameters.
+      optional object inputSchema
+      # Optional annotations for the tool.
+      optional Annotation annotations
+      # Frame identifier associated with the tool registration.
+      Page.FrameId frameId
+      # Optional node ID for declarative tools.
+      optional DOM.BackendNodeId backendNodeId
+      # The stack trace at the time of the registration.
+      optional Runtime.StackTrace stackTrace
+
+
+  # Enables the WebMCP domain, allowing events to be sent. Enabling the domain will trigger a toolsAdded event for
+  # all currently registered tools.
+  command enable
+
+  # Event fired when new tools are added.
+  event toolsAdded
+    parameters
+      # Array of tools that were added.
+      array of Tool tools
+
+  # Event fired when tools are removed.
+  event toolsRemoved
+    parameters
+      # Array of tools that were removed.
+      array of Tool tools
```

## Roll protocol to r1596832 — _2026-03-10T04:53:52.000Z_
######  Diff: [`50eddc4...07f7b82`](https://github.com/ChromeDevTools/devtools-protocol/compare/50eddc4...07f7b82)

```diff
@@ browser_protocol.pdl:56 @@ include domains/Tethering.pdl
 include domains/Tracing.pdl
 include domains/WebAudio.pdl
 include domains/WebAuthn.pdl
+include domains/WebMCP.pdl
```

## Roll protocol to r1595872 — _2026-03-07T04:48:07.000Z_
######  Diff: [`374f160...50eddc4`](https://github.com/ChromeDevTools/devtools-protocol/compare/374f160...50eddc4)

```diff
@@ domains/Audits.pdl:258 @@ experimental domain Audits
       boolean isWarning
       SharedArrayBufferIssueType type
 
-  type LowTextContrastIssueDetails extends object
-    properties
-      DOM.BackendNodeId violatingNodeId
-      string violatingNodeSelector
-      number contrastRatio
-      number thresholdAA
-      number thresholdAAA
-      string fontSize
-      string fontWeight
-
   # Details for a CORS related issue, e.g. a warning or error related to
   # CORS RFC1918 enforcement.
   type CorsIssueDetails extends object
@@ -744,7 +734,6 @@ experimental domain Audits
       HeavyAdIssue
       ContentSecurityPolicyIssue
       SharedArrayBufferIssue
-      LowTextContrastIssue
       CorsIssue
       AttributionReportingIssue
       QuirksModeIssue
@@ -781,7 +770,6 @@ experimental domain Audits
       optional HeavyAdIssueDetails heavyAdIssueDetails
       optional ContentSecurityPolicyIssueDetails contentSecurityPolicyIssueDetails
       optional SharedArrayBufferIssueDetails sharedArrayBufferIssueDetails
-      optional LowTextContrastIssueDetails lowTextContrastIssueDetails
       optional CorsIssueDetails corsIssueDetails
       optional AttributionReportingIssueDetails attributionReportingIssueDetails
       optional QuirksModeIssueDetails quirksModeIssueDetails
@@ -849,13 +837,6 @@ experimental domain Audits
   # `issueAdded` event.
   command enable
 
-  # Runs the contrast check for the target page. Found issues are reported
-  # using Audits.issueAdded event.
-  command checkContrast
-    parameters
-      # Whether to report WCAG AAA level issues. Default is false.
-      optional boolean reportAAA
-
   # Runs the form issues check for the target page. Found issues are reported
   # using Audits.issueAdded event.
   command checkFormsIssues
diff --git a/pdl/domains/Page.pdl b/pdl/domains/Page.pdl
index 59b5e038..76d6ed49 100644
--- a/pdl/domains/Page.pdl
+++ b/pdl/domains/Page.pdl
@@ -1537,6 +1537,7 @@ domain Page
       BackForwardCacheDisabledForPrerender
       UserAgentOverrideDiffers
       ForegroundCacheLimit
+      ForwardCacheDisabled
       BrowsingInstanceNotSwapped
       BackForwardCacheDisabledForDelegate
       UnloadHandlerExistsInMainFrame
```

## Roll protocol to r1594462 — _2026-03-05T04:56:16.000Z_
######  Diff: [`b888df9...374f160`](https://github.com/ChromeDevTools/devtools-protocol/compare/b888df9...374f160)

```diff
@@ domains/Audits.pdl:438 @@ experimental domain Audits
       AutofillAndManualTextPolicyControlledFeaturesInfo
       AutofillPolicyControlledFeatureInfo
       ManualTextPolicyControlledFeatureInfo
+      FormModelContextParameterMissingTitleAndDescription
 
   # Depending on the concrete errorType, different properties are set.
   type GenericIssueDetails extends object
diff --git a/pdl/domains/CSS.pdl b/pdl/domains/CSS.pdl
index 91437769..1fc28282 100644
--- a/pdl/domains/CSS.pdl
+++ b/pdl/domains/CSS.pdl
@@ -185,6 +185,9 @@ experimental domain CSS
       # @starting-style CSS at-rule array.
       # The array enumerates @starting-style at-rules starting with the innermost one, going outwards.
       experimental optional array of CSSStartingStyle startingStyles
+      # @navigation CSS at-rule array.
+      # The array enumerates @navigation at-rules starting with the innermost one, going outwards.
+      experimental optional array of CSSNavigation navigations
 
   # Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors.
   # This list only contains rule types that are collected during the ancestor rule collection.
@@ -197,6 +200,7 @@ experimental domain CSS
       ScopeRule
       StyleRule
       StartingStyleRule
+      NavigationRule
 
   # CSS coverage information.
   type RuleUsage extends object
@@ -364,6 +368,19 @@ experimental domain CSS
       # Identifier of the stylesheet containing this object (if exists).
       optional DOM.StyleSheetId styleSheetId
 
+  # CSS Navigation at-rule descriptor.
+  experimental type CSSNavigation extends object
+    properties
+      # Navigation rule text.
+      string text
+      # Whether the navigation condition is satisfied.
+      optional boolean active
+      # The associated rule header range in the enclosing stylesheet (if
+      # available).
+      optional SourceRange range
+      # Identifier of the stylesheet containing this object (if exists).
+      optional DOM.StyleSheetId styleSheetId
+
   # CSS Scope at-rule descriptor.
   experimental type CSSScope extends object
     properties
@@ -556,6 +573,8 @@ experimental domain CSS
       optional CSSContainerQuery containerQueries
       # @supports CSS at-rule condition. Only one type of condition should be set.
       optional CSSSupports supports
+      # @navigation condition. Only one type of condition should be set.
+      optional CSSNavigation navigation
       # Block body.
       array of CSSFunctionNode children
       # The condition text.
@@ -924,6 +943,16 @@ experimental domain CSS
       # The resulting CSS Supports rule after modification.
       CSSSupports supports
 
+  # Modifies the expression of a navigation at-rule.
+  experimental command setNavigationText
+    parameters
+      DOM.StyleSheetId styleSheetId
+      SourceRange range
+      string text
+    returns
+      # The resulting CSS Navigation rule after modification.
+      CSSNavigation navigation
+
   # Modifies the expression of a scope at-rule.
   experimental command setScopeText
     parameters
```

## Roll protocol to r1593706 — _2026-03-04T04:52:43.000Z_
######  Diff: [`58bb362...b888df9`](https://github.com/ChromeDevTools/devtools-protocol/compare/58bb362...b888df9)

```diff
@@ domains/Emulation.pdl:306 @@ domain Emulation
         # classic (occupying space within the layout) or overlay, depending
         # on the platform. Note: if `mobile` is `true`, the default scrollbar type is `overlay`.
         default
+      # If set to true, enables screen orientation lock emulation, which
+      # intercepts screen.orientation.lock() calls from the page and reports
+      # orientation changes via screenOrientationLockChanged events. This is
+      # useful for emulating mobile device orientation lock behavior in
+      # responsive design mode.
+      experimental optional boolean screenOrientationLockEmulation
 
   # Start reporting the given posture value to the Device Posture API.
   # This override can also be set in setDeviceMetricsOverride().
@@ -530,6 +536,16 @@ domain Emulation
   # Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.
   experimental event virtualTimeBudgetExpired
 
+  # Fired when a page calls screen.orientation.lock() or screen.orientation.unlock()
+  # while device emulation is enabled. This allows the DevTools frontend to update the
+  # emulated device orientation accordingly.
+  experimental event screenOrientationLockChanged
+    parameters
+      # Whether the screen orientation is currently locked.
+      boolean locked
+      # The orientation lock type requested by the page. Only set when locked is true.
+      optional ScreenOrientation orientation
+
   # Enum of image types that can be disabled.
   experimental type DisabledImageType extends string
     enum
@@ -613,6 +629,34 @@ domain Emulation
     returns
       ScreenInfo screenInfo
 
+  # Updates specified screen parameters. Only supported in headless mode.
+  experimental command updateScreen
+    parameters
+      # Target screen identifier.
+      ScreenId screenId
+      # Offset of the left edge of the screen in pixels.
+      optional integer left
+      # Offset of the top edge of the screen in pixels.
+      optional integer top
+      # The width of the screen in pixels.
+      optional integer width
+      # The height of the screen in pixels.
+      optional integer height
+      # Specifies the screen's work area.
+      optional WorkAreaInsets workAreaInsets
+      # Specifies the screen's device pixel ratio.
+      optional number devicePixelRatio
+      # Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270.
+      optional integer rotation
+      # Specifies the screen's color depth in bits.
+      optional integer colorDepth
+      # Specifies the descriptive label for the screen.
+      optional string label
+      # Indicates whether the screen is internal to the device or external, attached to the device. Default is false.
+      optional boolean isInternal
+    returns
+      ScreenInfo screenInfo
+
   # Remove screen from the device. Only supported in headless mode.
   experimental command removeScreen
     parameters
```
