# Chrome DevTools Protocol changelog — 2026-04

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-04, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1621552 — _2026-04-28T05:34:17.000Z_
######  Diff: [`e0946be...470fb6a`](https://github.com/ChromeDevTools/devtools-protocol/compare/e0946be...470fb6a)

```diff
@@ domains/DOM.pdl:44 @@ domain DOM
       after
       expand-icon
       picker-icon
-      interest-hint
+      interest-button
       marker
       backdrop
       column
```

## Roll protocol to r1619965 — _2026-04-24T05:20:53.000Z_
######  Diff: [`5d8fd1a...e0946be`](https://github.com/ChromeDevTools/devtools-protocol/compare/5d8fd1a...e0946be)

```diff
@@ domains/Extensions.pdl:15 @@ experimental domain Extensions
       managed
 
   # Runs an extension default action.
-  # Available if the client is connected using the --remote-debugging-pipe
-  # flag and the --enable-unsafe-extension-debugging flag is set.
   command triggerAction
     parameters
       # Extension id.
@@ -26,9 +24,7 @@ experimental domain Extensions
 
   # Installs an unpacked extension from the filesystem similar to
   # --load-extension CLI flags. Returns extension ID once the extension
-  # has been installed. Available if the client is connected using the
-  # --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging
-  # flag is set.
+  # has been installed.
   command loadUnpacked
     parameters
       # Absolute file path.
@@ -54,15 +50,11 @@ experimental domain Extensions
       boolean enabled
 
   # Gets a list of all unpacked extensions.
-  # Available if the client is connected using the --remote-debugging-pipe flag
-  # and the --enable-unsafe-extension-debugging flag is set.
   command getExtensions
     returns
       array of ExtensionInfo extensions
 
   # Uninstalls an unpacked extension (others not supported) from the profile.
-  # Available if the client is connected using the --remote-debugging-pipe flag
-  # and the --enable-unsafe-extension-debugging.
   command uninstall
     parameters
       # Extension id.
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index 4b3836a4..463107ab 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -15,6 +15,8 @@ experimental domain WebMCP
     properties
       # A hint indicating that the tool does not modify any state.
       optional boolean readOnly
+      # A hint indicating that the tool output may contain untrusted content, ex: UGC, 3rd party data.
+      optional boolean untrustedContent
       # If the declarative tool was declared with the autosubmit attribute.
       optional boolean autosubmit
```

## Roll protocol to r1618660 — _2026-04-22T05:15:00.000Z_
######  Diff: [`eed2b1b...5d8fd1a`](https://github.com/ChromeDevTools/devtools-protocol/compare/eed2b1b...5d8fd1a)

```diff
@@ domains/Page.pdl:1618 @@ domain Page
       EmbedderExtensionMessaging
       EmbedderExtensionMessagingForOpenPort
       EmbedderExtensionSentMessageToCachedFrame
+      EmbedderExtensionFrame
       RequestedByWebViewClient
       PostMessageByWebViewClient
       CacheControlNoStoreDeviceBoundSessionTerminated
```

## Roll protocol to r1617982 — _2026-04-21T05:16:43.000Z_
######  Diff: [`4d08372...eed2b1b`](https://github.com/ChromeDevTools/devtools-protocol/compare/4d08372...eed2b1b)

```diff
@@ domains/WebMCP.pdl:76 @@ experimental domain WebMCP
       # Array of tools that were added.
       array of Tool tools
 
+  # Definition of a tool that was removed.
+  type RemovedTool extends object
+    properties
+      # Tool name.
+      string name
+      # Frame identifier associated with the tool registration.
+      Page.FrameId frameId
+
   # Event fired when tools are removed.
   event toolsRemoved
     parameters
       # Array of tools that were removed.
-      array of Tool tools
+      array of RemovedTool tools
 
   # Event fired when a tool invocation starts.
   event toolInvoked
```

## Roll protocol to r1617013 — _2026-04-18T05:05:32.000Z_
######  Diff: [`ae00315...4d08372`](https://github.com/ChromeDevTools/devtools-protocol/compare/ae00315...4d08372)

```diff
@@ domains/Target.pdl:21 @@ domain Target
       string url
       # Whether the target has an attached client.
       boolean attached
+      # Id of the parent target, if any. For example, "iframe" target may have a "page" parent.
+      optional TargetID parentId
       # Opener target Id
       optional TargetID openerId
       # Whether the target has access to the originating window.
```

## Roll protocol to r1616338 — _2026-04-17T05:17:05.000Z_
######  Diff: [`d852d0c...ae00315`](https://github.com/ChromeDevTools/devtools-protocol/compare/d852d0c...ae00315)

```diff
@@ domains/Audits.pdl:429 @@ experimental domain Audits
       AutofillPolicyControlledFeatureInfo
       ManualTextPolicyControlledFeatureInfo
       FormModelContextParameterMissingTitleAndDescription
+      FormModelContextMissingToolName
+      FormModelContextMissingToolDescription
+      FormModelContextRequiredParameterMissingName
+      FormModelContextParameterMissingName
 
   # Depending on the concrete errorType, different properties are set.
   type GenericIssueDetails extends object
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index d687c478..f7ecb3a5 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -64,6 +64,12 @@ experimental domain WebMCP
       # Unique identifier for this invocation. Response is sent before tool events.
       string invocationId
 
+  # Cancels a pending tool invocation.
+  command cancelInvocation
+    parameters
+      # Invocation identifier to cancel.
+      string invocationId
+
   # Event fired when new tools are added.
   event toolsAdded
     parameters
```

## Roll protocol to r1615727 — _2026-04-16T10:28:34.000Z_
######  Diff: [`bb00b98...d852d0c`](https://github.com/ChromeDevTools/devtools-protocol/compare/bb00b98...d852d0c)

```diff
@@ domains/Network.pdl:2260 @@ domain Network
       # The result of a refresh.
       enum refreshResult
         Refreshed
+        RefreshedAsWaiter
         InitializedService
         Unreachable
         ServerError
@@ -2290,6 +2291,7 @@ domain Network
         ServerRequested
         InvalidSessionParams
         RefreshFatalError
+        DevTools
 
   # Session event details specific to challenges.
   experimental type ChallengeEventDetails extends object
@@ -2334,6 +2336,11 @@ domain Network
       # Whether to enable or disable events.
       boolean enable
 
+  # Deletes a device bound session.
+  experimental command deleteDeviceBoundSession
+    parameters
+      DeviceBoundSessionKey key
+
   # Fetches the schemeful site for a specific origin.
   experimental command fetchSchemefulSite
     parameters
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index e8380799..1f943c6e 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -27,7 +27,8 @@ domain Target
       experimental boolean canAccessOpener
       # Frame id of originating window (is only set if target has an opener).
       experimental optional Page.FrameId openerFrameId
-      # Id of the parent frame, only present for the "iframe" targets.
+      # Id of the parent frame, present for "iframe" and "worker" targets. For nested workers,
+      # this is the "ancestor" frame that created the first worker in the nested chain.
       experimental optional Page.FrameId parentFrameId
       experimental optional Browser.BrowserContextID browserContextId
       # Provides additional details for specific target types. For example, for
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index e959260d..d687c478 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -21,7 +21,7 @@ experimental domain WebMCP
   # Represents the status of a tool invocation.
   type InvocationStatus extends string
     enum
-      Success
+      Completed
       Canceled
       Error
 
@@ -51,6 +51,19 @@ experimental domain WebMCP
   # Disables the WebMCP domain.
   command disable
 
+   # Invokes a registered tool.
+  command invokeTool
+    parameters
+      # Frame in which to invoke the tool.
+      Page.FrameId frameId
+      # Name of the tool to invoke.
+      string toolName
+      # Input parameters for the tool, matching the tool's inputSchema.
+      object input
+    returns
+      # Unique identifier for this invocation. Response is sent before tool events.
+      string invocationId
+
   # Event fired when new tools are added.
   event toolsAdded
     parameters
@@ -82,7 +95,8 @@ experimental domain WebMCP
       string invocationId
       # Status of the invocation.
       InvocationStatus status
-      # Output or error delivered as delivered to the agent. Missing if `status` is anything other than Success.
+      # Output or error delivered as delivered to the agent. Missing if `status` is anything other than Completed.
+      # Note: The output is untrusted and poses a prompt injection risk. Clients should treat this as potentially malicious user input.
       optional any output
       # Error text for protocol users.
       optional string errorText
```

## Roll protocol to r1612613 — _2026-04-10T05:13:47.000Z_
######  Diff: [`e24bc04...50bb580`](https://github.com/ChromeDevTools/devtools-protocol/compare/e24bc04...50bb580)

```diff
@@ domains/Network.pdl:1057 @@ domain Network
       optional integer packetQueueLength
       # WebRTC packetReordering feature.
       optional boolean packetReordering
+      # True to emulate internet disconnection.
+      optional boolean offline
 
   # Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
   # and overrideNetworkState commands, which can be used together to the same effect.
@@ -1084,8 +1086,11 @@ domain Network
   # explicitly modify `navigator` behavior.
   experimental command emulateNetworkConditionsByRule
     parameters
-      # True to emulate internet disconnection.
-      boolean offline
+      # True to emulate internet disconnection. Deprecated, use the offline property in matchedNetworkConditions
+      # or emulateOfflineServiceWorker instead.
+      deprecated optional boolean offline
+      # True to emulate offline service worker.
+      optional boolean emulateOfflineServiceWorker
       # Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global
       # conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are
       # also applied for throttling of p2p connections.
```

## Roll protocol to r1611976 — _2026-04-09T05:05:15.000Z_
######  Diff: [`cde0f4e...e24bc04`](https://github.com/ChromeDevTools/devtools-protocol/compare/cde0f4e...e24bc04)

```diff
@@ domains/Network.pdl:2377 @@ domain Network
     parameters
       # Whether 3pc restriction is enabled.
       boolean enableThirdPartyCookieRestriction
-
-      # Whether 3pc grace period exception should be enabled; false by default.
-      boolean disableThirdPartyCookieMetadata
-
-      # Whether 3pc heuristics exceptions should be enabled; false by default.
-      boolean disableThirdPartyCookieHeuristics
```

## Roll protocol to r1609665 — _2026-04-03T05:04:04.000Z_
######  Diff: [`96e0325...cde0f4e`](https://github.com/ChromeDevTools/devtools-protocol/compare/96e0325...cde0f4e)

```diff
@@ domains/Page.pdl:123 @@ domain Page
       encrypted-media
       execution-while-out-of-viewport
       execution-while-not-rendered
-      fenced-unpartitioned-storage-read
       focus-without-user-activation
       fullscreen
       frobulate
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index f2550f78..100e94d7 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -622,21 +622,6 @@ experimental domain Storage
     returns
       array of RelatedWebsiteSet sets
 
-  # Returns the list of URLs from a page and its embedded resources that match
-  # existing grace period URL pattern rules.
-  # https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
-  experimental command getAffectedUrlsForThirdPartyCookieMetadata
-    parameters
-      # The URL of the page currently being visited.
-      string firstPartyUrl
-      # The list of embedded resource URLs from the page.
-      array of string thirdPartyUrls
-
-    returns
-      # Array of matching URLs. If there is a primary pattern match for the first-
-      # party URL, only the first-party URL is returned in the array.
-      array of string matchedUrls
-
   command setProtectedAudienceKAnonymity
     parameters
       string owner
```

## Roll protocol to r1608973 — _2026-04-02T05:06:03.000Z_
######  Diff: [`1abe750...96e0325`](https://github.com/ChromeDevTools/devtools-protocol/compare/1abe750...96e0325)

```diff
@@ domains/Preload.pdl:77 @@ experimental domain Preload
       Network.LoaderId loaderId
       SpeculationAction action
       string url
+      optional boolean formSubmission
       optional SpeculationTargetHint targetHint
 
   # Lists sources for a preloading attempt, specifically the ids of rule sets
@@ -189,6 +190,7 @@ experimental domain Preload
       PrerenderFailedDuringPrefetch
       BrowsingDataRemoved
       PrerenderHostReused
+      FormSubmitWhenPrerendering
 
   # Fired when a preload enabled state is updated.
   event preloadEnabledStateUpdated
diff --git a/pdl/domains/Storage.pdl b/pdl/domains/Storage.pdl
index 973259c0..f2550f78 100644
--- a/pdl/domains/Storage.pdl
+++ b/pdl/domains/Storage.pdl
@@ -606,284 +606,6 @@ experimental domain Storage
     parameters
       string bucketId
 
-  # https://wicg.github.io/attribution-reporting-api/
-  experimental command setAttributionReportingLocalTestingMode
-    parameters
-      # If enabled, noise is suppressed and reports are sent immediately.
-      boolean enabled
-
-  # Enables/disables issuing of Attribution Reporting events.
-  experimental command setAttributionReportingTracking
-    parameters
-      boolean enable
-
-  # Sends all pending Attribution Reports immediately, regardless of their
-  # scheduled report time.
-  experimental command sendPendingAttributionReports
-    returns
-      # The number of reports that were sent.
-      integer numSent
-
-  experimental type AttributionReportingSourceType extends string
-    enum
-      navigation
-      event
-
-  experimental type UnsignedInt64AsBase10 extends string
-  experimental type UnsignedInt128AsBase16 extends string
-  experimental type SignedInt64AsBase10 extends string
-
-  experimental type AttributionReportingFilterDataEntry extends object
-    properties
-      string key
-      array of string values
-
-  experimental type AttributionReportingFilterConfig extends object
-    properties
-      array of AttributionReportingFilterDataEntry filterValues
-      # duration in seconds
-      optional integer lookbackWindow
-
-  experimental type AttributionReportingFilterPair extends object
-    properties
-      array of AttributionReportingFilterConfig filters
-      array of AttributionReportingFilterConfig notFilters
-
-  experimental type AttributionReportingAggregationKeysEntry extends object
-    properties
-      string key
-      UnsignedInt128AsBase16 value
-
-  experimental type AttributionReportingEventReportWindows extends object
-    properties
-      # duration in seconds
-      integer start
-      # duration in seconds
-      array of integer ends
-
-  experimental type AttributionReportingTriggerDataMatching extends string
-    enum
-      exact
-      modulus
-
-  experimental type AttributionReportingAggregatableDebugReportingData extends object
-    properties
-      UnsignedInt128AsBase16 keyPiece
-      # number instead of integer because not all uint32 can be represented by
-      # int
-      number value
-      array of string types
-
-  experimental type AttributionReportingAggregatableDebugReportingConfig extends object
-    properties
-      # number instead of integer because not all uint32 can be represented by
-      # int, only present for source registrations
-      optional number budget
-      UnsignedInt128AsBase16 keyPiece
-      array of AttributionReportingAggregatableDebugReportingData debugData
-      optional string aggregationCoordinatorOrigin
-
-  experimental type AttributionScopesData extends object
-    properties
-      array of string values
-      # number instead of integer because not all uint32 can be represented by
-      # int
-      number limit
-      number maxEventStates
-
-  experimental type AttributionReportingNamedBudgetDef extends object
-    properties
-      string name
-      integer budget
-
-  experimental type AttributionReportingSourceRegistration extends object
-    properties
-      Network.TimeSinceEpoch time
-      # duration in seconds
-      integer expiry
-      # number instead of integer because not all uint32 can be represented by
-      # int
-      array of number triggerData
-      AttributionReportingEventReportWindows eventReportWindows
-      # duration in seconds
-      integer aggregatableReportWindow
-      AttributionReportingSourceType type
-      string sourceOrigin
-      string reportingOrigin
-      array of string destinationSites
-      UnsignedInt64AsBase10 eventId
-      SignedInt64AsBase10 priority
-      array of AttributionReportingFilterDataEntry filterData
-      array of AttributionReportingAggregationKeysEntry aggregationKeys
-      optional UnsignedInt64AsBase10 debugKey
-      AttributionReportingTriggerDataMatching triggerDataMatching
-      SignedInt64AsBase10 destinationLimitPriority
-      AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
-      optional AttributionScopesData scopesData
-      integer maxEventLevelReports
-      array of AttributionReportingNamedBudgetDef namedBudgets
-      boolean debugReporting
-      number eventLevelEpsilon
-
-  experimental type AttributionReportingSourceRegistrationResult extends string
-    enum
-      success
-      internalError
-      insufficientSourceCapacity
-      insufficientUniqueDestinationCapacity
-      excessiveReportingOrigins
-      prohibitedByBrowserPolicy
-      successNoised
-      destinationReportingLimitReached
-      destinationGlobalLimitReached
-      destinationBothLimitsReached
-      reportingOriginsPerSiteLimitReached
-      exceedsMaxChannelCapacity
-      exceedsMaxScopesChannelCapacity
-      exceedsMaxTriggerStateCardinality
-      exceedsMaxEventStatesLimit
-      destinationPerDayReportingLimitReached
-
-  experimental event attributionReportingSourceRegistered
-    parameters
-      AttributionReportingSourceRegistration registration
-      AttributionReportingSourceRegistrationResult result
-
-  experimental type AttributionReportingSourceRegistrationTimeConfig extends string
-    enum
-      include
-      exclude
-
-  experimental type AttributionReportingAggregatableValueDictEntry extends object
-    properties
-      string key
-      # number instead of integer because not all uint32 can be represented by
-      # int
-      number value
-      UnsignedInt64AsBase10 filteringId
-
-
-  experimental type AttributionReportingAggregatableValueEntry extends object
-    properties
-      array of AttributionReportingAggregatableValueDictEntry values
-      AttributionReportingFilterPair filters
-
-  experimental type AttributionReportingEventTriggerData extends object
-    properties
-      UnsignedInt64AsBase10 data
-      SignedInt64AsBase10 priority
-      optional UnsignedInt64AsBase10 dedupKey
-      AttributionReportingFilterPair filters
-
-  experimental type AttributionReportingAggregatableTriggerData extends object
-    properties
-      UnsignedInt128AsBase16 keyPiece
-      array of string sourceKeys
-      AttributionReportingFilterPair filters
-
-  experimental type AttributionReportingAggregatableDedupKey extends object
-    properties
-      optional UnsignedInt64AsBase10 dedupKey
-      AttributionReportingFilterPair filters
-
-  experimental type AttributionReportingNamedBudgetCandidate extends object
-    properties
-      optional string name
-      AttributionReportingFilterPair filters
-
-  experimental type AttributionReportingTriggerRegistration extends object
-    properties
-      AttributionReportingFilterPair filters
-      optional UnsignedInt64AsBase10 debugKey
-      array of AttributionReportingAggregatableDedupKey aggregatableDedupKeys
-      array of AttributionReportingEventTriggerData eventTriggerData
-      array of AttributionReportingAggregatableTriggerData aggregatableTriggerData
-      array of AttributionReportingAggregatableValueEntry aggregatableValues
-      integer aggregatableFilteringIdMaxBytes
-      boolean debugReporting
-      optional string aggregationCoordinatorOrigin
-      AttributionReportingSourceRegistrationTimeConfig sourceRegistrationTimeConfig
-      optional string triggerContextId
-      AttributionReportingAggregatableDebugReportingConfig aggregatableDebugReportingConfig
-      array of string scopes
-      array of AttributionReportingNamedBudgetCandidate namedBudgets
-
-  experimental type AttributionReportingEventLevelResult extends string
-    enum
-      success
-      successDroppedLowerPriority
-      internalError
-      noCapacityForAttributionDestination
-      noMatchingSources
-      deduplicated
-      excessiveAttributions
-      priorityTooLow
-      neverAttributedSource
-      excessiveReportingOrigins
-      noMatchingSourceFilterData
-      prohibitedByBrowserPolicy
-      noMatchingConfigurations
-      excessiveReports
-      falselyAttributedSource
-      reportWindowPassed
-      notRegistered
-      reportWindowNotStarted
-      noMatchingTriggerData
-
-  experimental type AttributionReportingAggregatableResult extends string
-    enum
-      success
-      internalError
-      noCapacityForAttributionDestination
-      noMatchingSources
-      excessiveAttributions
-      excessiveReportingOrigins
-      noHistograms
-      insufficientBudget
-      insufficientNamedBudget
-      noMatchingSourceFilterData
-      notRegistered
-      prohibitedByBrowserPolicy
-      deduplicated
-      reportWindowPassed
-      excessiveReports
-
-  experimental event attributionReportingTriggerRegistered
-    parameters
-      AttributionReportingTriggerRegistration registration
-      AttributionReportingEventLevelResult eventLevel
-      AttributionReportingAggregatableResult aggregatable
-
-  experimental type AttributionReportingReportResult extends string
-    enum
-      # A network request was attempted for the report.
-      sent
-      # No request was attempted because of browser policy.
-      prohibited
-      # No request was attempted because of an error in report assembly,
-      # e.g. the aggregation service was unavailable.
-      failedToAssemble
-      # No request was attempted because the report's expiry passed.
-      expired
-
-  experimental event attributionReportingReportSent
-    parameters
-      string url
-      object body
-      AttributionReportingReportResult result
-      # If result is `sent`, populated with net/HTTP status.
-      optional integer netError
-      optional string netErrorName
-      optional integer httpStatusCode
-
-  experimental event attributionReportingVerboseDebugReportSent
-    parameters
-      string url
-      optional array of object body
-      optional integer netError
-      optional string netErrorName
-      optional integer httpStatusCode
-
   # A single Related Website Set object.
   experimental type RelatedWebsiteSet extends object
     properties
diff --git a/pdl/domains/WebMCP.pdl b/pdl/domains/WebMCP.pdl
index a1696cd2..e959260d 100644
--- a/pdl/domains/WebMCP.pdl
+++ b/pdl/domains/WebMCP.pdl
@@ -48,6 +48,9 @@ experimental domain WebMCP
   # all currently registered tools.
   command enable
 
+  # Disables the WebMCP domain.
+  command disable
+
   # Event fired when new tools are added.
   event toolsAdded
     parameters
@@ -80,7 +83,7 @@ experimental domain WebMCP
       # Status of the invocation.
       InvocationStatus status
       # Output or error delivered as delivered to the agent. Missing if `status` is anything other than Success.
-      optional object output
+      optional any output
       # Error text for protocol users.
       optional string errorText
       # The exception object, if the javascript tool threw an error>
```
