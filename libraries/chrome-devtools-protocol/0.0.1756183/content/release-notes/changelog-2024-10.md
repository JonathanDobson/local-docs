# Chrome DevTools Protocol changelog — 2024-10

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-10, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1376096 — _2024-10-31T04:30:05.000Z_
######  Diff: [`6866f7c...2354f74`](https://github.com/ChromeDevTools/devtools-protocol/compare/6866f7c...2354f74)

```diff
@@ browser_protocol.pdl:11720 @@ experimental domain WebAudio
       suspended
       running
       closed
+      interrupted
 
   # Enum of AudioNode types
   type NodeType extends string
```

## Roll protocol to r1375038 — _2024-10-29T04:29:43.000Z_
######  Diff: [`b213dca...6866f7c`](https://github.com/ChromeDevTools/devtools-protocol/compare/b213dca...6866f7c)

```diff
@@ browser_protocol.pdl:10715 @@ experimental domain Storage
       SignedInt64AsBase10 destinationLimitPriority
       AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
       optional AttributionScopesData scopesData
+      integer maxEventLevelReports
 
   experimental type AttributionReportingSourceRegistrationResult extends string
     enum
```

## Roll protocol to r1373723 — _2024-10-25T04:30:25.000Z_
######  Diff: [`60273fe...b213dca`](https://github.com/ChromeDevTools/devtools-protocol/compare/60273fe...b213dca)

```diff
@@ browser_protocol.pdl:8095 @@ domain Page
       encrypted-media
       execution-while-out-of-viewport
       execution-while-not-rendered
-      fenced-frame-unpartitioned-data
+      fenced-unpartitioned-storage-read
       focus-without-user-activation
       fullscreen
       frobulate
```

## Roll protocol to r1371839 — _2024-10-22T04:29:59.000Z_
######  Diff: [`91bd3ba...60273fe`](https://github.com/ChromeDevTools/devtools-protocol/compare/91bd3ba...60273fe)

```diff
@@ browser_protocol.pdl:2677 @@ domain DOM
     enum
       first-line
       first-letter
+      check
       before
       after
       marker
@@ -8094,6 +8095,7 @@ domain Page
       encrypted-media
       execution-while-out-of-viewport
       execution-while-not-rendered
+      fenced-frame-unpartitioned-data
       focus-without-user-activation
       fullscreen
       frobulate
```

## Roll protocol to r1368592 — _2024-10-15T04:29:39.000Z_
######  Diff: [`1526dda...91bd3ba`](https://github.com/ChromeDevTools/devtools-protocol/compare/1526dda...91bd3ba)

```diff
@@ browser_protocol.pdl:2709 @@ domain DOM
       placeholder
       file-selector-button
       details-content
-      select-fallback-button
-      select-fallback-button-text
       picker
 
   # Shadow root type.
@@ -9520,6 +9518,7 @@ domain Page
       EmbedderExtensionMessagingForOpenPort
       EmbedderExtensionSentMessageToCachedFrame
       RequestedByWebViewClient
+      PostMessageByWebViewClient
 
   # Types of not restored reasons for back-forward cache.
   experimental type BackForwardCacheNotRestoredReasonType extends string
```

## Roll protocol to r1367902 — _2024-10-12T04:29:12.000Z_
######  Diff: [`770b664...1526dda`](https://github.com/ChromeDevTools/devtools-protocol/compare/770b664...1526dda)

```diff
@@ browser_protocol.pdl:12431 @@ experimental domain Preload
       SlowNetwork
       OtherPrerenderedPageActivated
       V8OptimizerDisabled
+      PrerenderFailedDuringPrefetch
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1366620 — _2024-10-10T04:29:17.000Z_
######  Diff: [`c2f5637...770b664`](https://github.com/ChromeDevTools/devtools-protocol/compare/c2f5637...770b664)

```diff
@@ browser_protocol.pdl:918 @@ experimental domain Audits
       ThirdPartyCookiesBlocked
       NotSignedInWithIdp
       MissingTransientUserActivation
-      ReplacedByButtonMode
+      ReplacedByActiveMode
       InvalidFieldsSpecified
       RelyingPartyOriginIsOpaque
       TypeNotMatching
```

## Roll protocol to r1363470 — _2024-10-03T04:29:46.000Z_
######  Diff: [`ce00a1b...c2f5637`](https://github.com/ChromeDevTools/devtools-protocol/compare/ce00a1b...c2f5637)

```diff
@@ browser_protocol.pdl:11993 @@ experimental domain WebAuthn
       # flag set to this value. Defaults to the authenticator's
       # defaultBackupState value.
       optional boolean backupState
+      # The credential's user.name property. Equivalent to empty if not set.
+      # https://w3c.github.io/webauthn/#dom-publickeycredentialentity-name
+      optional string userName
+      # The credential's user.displayName property. Equivalent to empty if
+      # not set.
+      # https://w3c.github.io/webauthn/#dom-publickeycredentialuserentity-displayname
+      optional string userDisplayName
 
   # Enable the WebAuthn domain and start intercepting credential storage and
   # retrieval with a virtual authenticator.
@@ -12096,6 +12103,20 @@ experimental domain WebAuthn
       AuthenticatorId authenticatorId
       Credential credential
 
+  # Triggered when a credential is deleted, e.g. through
+  # PublicKeyCredential.signalUnknownCredential().
+  event credentialDeleted
+    parameters
+      AuthenticatorId authenticatorId
+      binary credentialId
+
+  # Triggered when a credential is updated, e.g. through
+  # PublicKeyCredential.signalCurrentUserDetails().
+  event credentialUpdated
+    parameters
+      AuthenticatorId authenticatorId
+      Credential credential
+
   # Triggered when a credential is used in a webauthn assertion.
   event credentialAsserted
     parameters
@@ -12409,6 +12430,7 @@ experimental domain Preload
       WindowClosed
       SlowNetwork
       OtherPrerenderedPageActivated
+      V8OptimizerDisabled
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
```

## Roll protocol to r1362837 — _2024-10-02T04:29:26.000Z_
######  Diff: [`5ce3c3b...ce00a1b`](https://github.com/ChromeDevTools/devtools-protocol/compare/5ce3c3b...ce00a1b)

```diff
@@ js_protocol.pdl:369 @@ domain Debugger
       # call stacks (default).
       integer maxDepth
 
+  # Replace previous blackbox execution contexts with passed ones. Forces backend to skip
+  # stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by
+  # performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
+  experimental command setBlackboxExecutionContexts
+    parameters
+      # Array of execution context unique ids for the debugger to ignore.
+      array of string uniqueIds
+
   # Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
   # scripts with url matching one of the patterns. VM will try to leave blackboxed script by
   # performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
@@ -376,6 +384,8 @@ domain Debugger
     parameters
       # Array of regexps that will be used to check script url for blackbox state.
       array of string patterns
+      # If true, also ignore scripts with no source url.
+      optional boolean skipAnonymous
 
   # Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
   # scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
```
