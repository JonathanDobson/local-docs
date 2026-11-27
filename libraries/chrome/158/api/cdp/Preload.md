# Preload domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `Preload.<command>` and events arrive as `Preload.<event>`.

## Commands

### Preload.enable

### Preload.disable

## Events

### Preload.ruleSetUpdated

Upsert. Currently, it is only emitted when a rule set added.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ruleSet` | [RuleSet](#type-ruleset) |  |

### Preload.ruleSetRemoved

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [RuleSetId](#type-rulesetid) |  |

### Preload.preloadEnabledStateUpdated

Fired when a preload enabled state is updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disabledByPreference` | boolean |  |
| `disabledByDataSaver` | boolean |  |
| `disabledByBatterySaver` | boolean |  |
| `disabledByHoldbackPrefetchSpeculationRules` | boolean |  |
| `disabledByHoldbackPrerenderSpeculationRules` | boolean |  |

### Preload.prefetchStatusUpdated

Fired when a prefetch attempt is updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `key` | [PreloadingAttemptKey](#type-preloadingattemptkey) |  |
| `pipelineId` | [PreloadPipelineId](#type-preloadpipelineid) |  |
| `initiatingFrameId` | [Page.FrameId](Page.md#type-frameid) | The frame id of the frame initiating prefetch. |
| `prefetchUrl` | string |  |
| `status` | [PreloadingStatus](#type-preloadingstatus) |  |
| `prefetchStatus` | [PrefetchStatus](#type-prefetchstatus) |  |
| `requestId` | [Network.RequestId](Network.md#type-requestid) |  |

### Preload.prerenderStatusUpdated

Fired when a prerender attempt is updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `key` | [PreloadingAttemptKey](#type-preloadingattemptkey) |  |
| `pipelineId` | [PreloadPipelineId](#type-preloadpipelineid) |  |
| `status` | [PreloadingStatus](#type-preloadingstatus) |  |
| `effectiveAction` (optional) | [SpeculationAction](#type-speculationaction) | The action currently performed by this attempt. This differs from `key.action` after a prerender-until-script attempt is upgraded in place to a full prerender. |
| `prerenderStatus` (optional) | [PrerenderFinalStatus](#type-prerenderfinalstatus) |  |
| `disallowedMojoInterface` (optional) | string | This is used to give users more information about the name of Mojo interface that is incompatible with prerender and has caused the cancellation of the attempt. |
| `mismatchedHeaders` (optional) | array of [PrerenderMismatchedHeaders](#type-prerendermismatchedheaders) |  |

### Preload.preloadingAttemptSourcesUpdated

Send a list of sources for all preloading attempts in a document.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) |  |
| `preloadingAttemptSources` | array of [PreloadingAttemptSource](#type-preloadingattemptsource) |  |

## Types

<a id="type-rulesetid"></a>
### Preload.RuleSetId

Type: string

Unique id

<a id="type-ruleset"></a>
### Preload.RuleSet

Type: object

Corresponds to SpeculationRuleSet

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [RuleSetId](#type-rulesetid) |  |
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) | Identifies a document which the rule set is associated with. |
| `sourceText` | string | Source text of JSON representing the rule set. If it comes from `<script>` tag, it is the textContent of the node. Note that it is a JSON for valid case.  See also: - https://wicg.github.io/nav-speculation/speculation-rules.html - https://github.com/WICG/nav-speculation/blob/main/triggers.md |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | A speculation rule set is either added through an inline `<script>` tag or through an external resource via the 'Speculation-Rules' HTTP header. For the first case, we include the BackendNodeId of the relevant `<script>` tag. For the second case, we include the external URL where the rule set was loaded from, and also RequestId if Network domain is enabled.  See also: - https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-script - https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-header |
| `url` (optional) | string |  |
| `requestId` (optional) | [Network.RequestId](Network.md#type-requestid) |  |
| `errorType` (optional) | [RuleSetErrorType](#type-ruleseterrortype) | Error information `errorMessage` is null iff `errorType` is null. |
| `errorMessage` (optional) *(deprecated)* | string | TODO(https://crbug.com/1425354): Replace this property with structured error. |
| `tag` (optional) | string | For more details, see: https://github.com/WICG/nav-speculation/blob/main/speculation-rules-tags.md |

<a id="type-ruleseterrortype"></a>
### Preload.RuleSetErrorType

Type: string

Allowed values: `SourceIsNotJsonObject`, `InvalidRulesSkipped`, `InvalidRulesetLevelTag`

<a id="type-speculationaction"></a>
### Preload.SpeculationAction

Type: string

The type of preloading attempted. It corresponds to mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it isn't being used by clients).

Allowed values: `Prefetch`, `Prerender`, `PrerenderUntilScript`

<a id="type-speculationtargethint"></a>
### Preload.SpeculationTargetHint

Type: string

Corresponds to mojom::SpeculationTargetHint. See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints

Allowed values: `Blank`, `Self`

<a id="type-preloadingattemptkey"></a>
### Preload.PreloadingAttemptKey

Type: object

A key that identifies a preloading attempt.  The url used is the url specified by the trigger (i.e. the initial URL), and not the final url that is navigated to. For example, prerendering allows same-origin main frame navigations during the attempt, but the attempt is still keyed with the initial URL.

**Properties**

| Name | Type | Description |
|---|---|---|
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) |  |
| `action` | [SpeculationAction](#type-speculationaction) |  |
| `url` | string |  |
| `formSubmission` (optional) | boolean |  |
| `targetHint` (optional) | [SpeculationTargetHint](#type-speculationtargethint) |  |

<a id="type-preloadingattemptsource"></a>
### Preload.PreloadingAttemptSource

Type: object

Lists sources for a preloading attempt, specifically the ids of rule sets that had a speculation rule that triggered the attempt, and the BackendNodeIds of <a href> or <area href> elements that triggered the attempt (in the case of attempts triggered by a document rule). It is possible for multiple rule sets and links to trigger a single attempt.

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | [PreloadingAttemptKey](#type-preloadingattemptkey) |  |
| `ruleSetIds` | array of [RuleSetId](#type-rulesetid) |  |
| `nodeIds` | array of [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |

<a id="type-preloadpipelineid"></a>
### Preload.PreloadPipelineId

Type: string

Chrome manages different types of preloads together using a concept of preloading pipeline. For example, if a site uses a SpeculationRules for prerender, Chrome first starts a prefetch and then upgrades it to prerender.  CDP events for them are emitted separately but they share `PreloadPipelineId`.

<a id="type-prerenderfinalstatus"></a>
### Preload.PrerenderFinalStatus

Type: string

List of FinalStatus reasons for Prerender2.

Allowed values: `Activated`, `Destroyed`, `LowEndDevice`, `InvalidSchemeRedirect`, `InvalidSchemeNavigation`, `NavigationRequestBlockedByCsp`, `MojoBinderPolicy`, `RendererProcessCrashed`, `RendererProcessKilled`, `Download`, `TriggerDestroyed`, `NavigationNotCommitted`, `NavigationBadHttpStatus`, `ClientCertRequested`, `NavigationRequestNetworkError`, `CancelAllHostsForTesting`, `DidFailLoad`, `Stop`, `SslCertificateError`, `LoginAuthRequested`, `UaChangeRequiresReload`, `BlockedByClient`, `AudioOutputDeviceRequested`, `MixedContent`, `TriggerBackgrounded`, `MemoryLimitExceeded`, `DataSaverEnabled`, `TriggerUrlHasEffectiveUrl`, `ActivatedBeforeStarted`, `InactivePageRestriction`, `StartFailed`, `TimeoutBackgrounded`, `CrossSiteRedirectInInitialNavigation`, `CrossSiteNavigationInInitialNavigation`, `SameSiteCrossOriginRedirectNotOptInInInitialNavigation`, `SameSiteCrossOriginNavigationNotOptInInInitialNavigation`, `ActivationNavigationParameterMismatch`, `ActivatedInBackground`, `EmbedderHostDisallowed`, `ActivationNavigationDestroyedBeforeSuccess`, `TabClosedByUserGesture`, `TabClosedWithoutUserGesture`, `PrimaryMainFrameRendererProcessCrashed`, `PrimaryMainFrameRendererProcessKilled`, `ActivationFramePolicyNotCompatible`, `PreloadingDisabled`, `BatterySaverEnabled`, `ActivatedDuringMainFrameNavigation`, `PreloadingUnsupportedByWebContents`, `CrossSiteRedirectInMainFrameNavigation`, `CrossSiteNavigationInMainFrameNavigation`, `SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation`, `SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation`, `MemoryPressureOnTrigger`, `MemoryPressureAfterTriggered`, `PrerenderingDisabledByDevTools`, `SpeculationRuleRemoved`, `ActivatedWithAuxiliaryBrowsingContexts`, `MaxNumOfRunningEagerPrerendersExceeded`, `MaxNumOfRunningNonEagerPrerendersExceeded`, `MaxNumOfRunningEmbedderPrerendersExceeded`, `PrerenderingUrlHasEffectiveUrl`, `RedirectedPrerenderingUrlHasEffectiveUrl`, `ActivationUrlHasEffectiveUrl`, `JavaScriptInterfaceAdded`, `JavaScriptInterfaceRemoved`, `AllPrerenderingCanceled`, `WindowClosed`, `SlowNetwork`, `OtherPrerenderedPageActivated`, `V8OptimizerDisabled`, `PrerenderFailedDuringPrefetch`, `BrowsingDataRemoved`, `PrerenderHostReused`, `FormSubmitWhenPrerendering`, `CrossDocumentRestart`, `PrefetchFailedCrossOriginSubframe`

<a id="type-preloadingstatus"></a>
### Preload.PreloadingStatus

Type: string

Preloading status values, see also PreloadingTriggeringOutcome. This status is shared by prefetchStatusUpdated and prerenderStatusUpdated.

Allowed values: `Pending`, `Running`, `Ready`, `Success`, `Failure`, `NotSupported`

<a id="type-prefetchstatus"></a>
### Preload.PrefetchStatus

Type: string

TODO(https://crbug.com/1384419): revisit the list of PrefetchStatus and filter out the ones that aren't necessary to the developers.

Allowed values: `PrefetchAllowed`, `PrefetchFailedIneligibleRedirect`, `PrefetchFailedInvalidRedirect`, `PrefetchFailedMIMENotSupported`, `PrefetchFailedNetError`, `PrefetchFailedNon2XX`, `PrefetchEvictedAfterBrowsingDataRemoved`, `PrefetchEvictedAfterCandidateRemoved`, `PrefetchEvictedForNewerPrefetch`, `PrefetchHeldback`, `PrefetchIneligibleRetryAfter`, `PrefetchIsPrivacyDecoy`, `PrefetchIsStale`, `PrefetchNotEligibleBlockedByConnectionAllowlist`, `PrefetchNotEligibleBrowserContextOffTheRecord`, `PrefetchNotEligibleCrossOrigin`, `PrefetchNotEligibleDataSaverEnabled`, `PrefetchNotEligibleExistingProxy`, `PrefetchNotEligibleHostIsNonUnique`, `PrefetchNotEligibleNonDefaultStoragePartition`, `PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy`, `PrefetchNotEligibleSchemeIsNotHttps`, `PrefetchNotEligibleUserHasCookies`, `PrefetchNotEligibleUserHasServiceWorker`, `PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler`, `PrefetchNotEligibleRedirectFromServiceWorker`, `PrefetchNotEligibleRedirectToServiceWorker`, `PrefetchNotEligibleBatterySaverEnabled`, `PrefetchNotEligiblePreloadingDisabled`, `PrefetchNotFinishedInTime`, `PrefetchNotStarted`, `PrefetchNotUsedCookiesChanged`, `PrefetchProxyNotAvailable`, `PrefetchResponseUsed`, `PrefetchSuccessfulButNotUsed`, `PrefetchNotUsedProbeFailed`, `PrefetchCancelledOnUserNavigation`

<a id="type-prerendermismatchedheaders"></a>
### Preload.PrerenderMismatchedHeaders

Type: object

Information of headers to be displayed when the header mismatch occurred.

**Properties**

| Name | Type | Description |
|---|---|---|
| `headerName` | string |  |
| `initialValue` (optional) | string |  |
| `activationValue` (optional) | string |  |

