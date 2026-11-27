# Audits domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Audits domain allows investigation of page violations and possible improvements.

Depends on: [Network](Network.md), [Runtime](Runtime.md)

4 methods, 1 events, 70 types.

## Methods

### Audits.getEncodedResponse

Returns the response body and size if it were re-encoded with the specified settings. Only
applies to images.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](Network.md#type-requestid) | Identifier of the network request to get content for. |
| `encoding` | string | The encoding to use. Allowed values: `webp`, `jpeg`, `png` |
| `quality` (optional) | number | The quality of the encoding (0-1). (defaults to 1) |
| `sizeOnly` (optional) | boolean | Whether to only return the size information (defaults to false). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `body` (optional) | string | The encoded body as a base64 string. Omitted if sizeOnly is true. (Encoded as a base64 string when passed over JSON) |
| `originalSize` | integer | Size before re-encoding. |
| `encodedSize` | integer | Size after re-encoding. |

### Audits.disable

Disables issues domain, prevents further issues from being reported to the client.

No parameters.

### Audits.enable

Enables issues domain, sends the issues collected so far to the client by means of the
`issueAdded` event.

No parameters.

### Audits.checkFormsIssues

Runs the form issues check for the target page. Found issues are reported
using Audits.issueAdded event.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `formIssues` | array of [Audits.GenericIssueDetails](#type-genericissuedetails) |  |

## Events

### Audits.issueAdded

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `issue` | [Audits.InspectorIssue](#type-inspectorissue) |  |

## Types

<a id="type-affectedcookie"></a>
### Audits.AffectedCookie

Information about a cookie that is affected by an inspector issue.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The following three properties uniquely identify a cookie |
| `path` | string |  |
| `domain` | string |  |

<a id="type-affectedrequest"></a>
### Audits.AffectedRequest

Information about a request that is affected by an inspector issue.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestId` (optional) | [Network.RequestId](Network.md#type-requestid) | The unique request id. |
| `url` | string |  |

<a id="type-affectedframe"></a>
### Audits.AffectedFrame

Information about the frame affected by an inspector issue.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) |  |

<a id="type-cookieexclusionreason"></a>
### Audits.CookieExclusionReason

Type: string

Allowed values: `ExcludeSameSiteUnspecifiedTreatedAsLax`, `ExcludeSameSiteNoneInsecure`, `ExcludeSameSiteLax`, `ExcludeSameSiteStrict`, `ExcludeDomainNonASCII`, `ExcludeThirdPartyPhaseout`, `ExcludePortMismatch`, `ExcludeSchemeMismatch`

<a id="type-cookiewarningreason"></a>
### Audits.CookieWarningReason

Type: string

Allowed values: `WarnSameSiteUnspecifiedCrossSiteContext`, `WarnSameSiteNoneInsecure`, `WarnSameSiteUnspecifiedLaxAllowUnsafe`, `WarnSameSiteStrictLaxDowngradeStrict`, `WarnSameSiteStrictCrossDowngradeStrict`, `WarnSameSiteStrictCrossDowngradeLax`, `WarnSameSiteLaxCrossDowngradeStrict`, `WarnSameSiteLaxCrossDowngradeLax`, `WarnAttributeValueExceedsMaxSize`, `WarnDomainNonASCII`, `WarnThirdPartyPhaseout`, `WarnCrossSiteRedirectDowngradeChangesInclusion`, `WarnDeprecationTrialMetadata`, `WarnThirdPartyCookieHeuristic`

<a id="type-cookieoperation"></a>
### Audits.CookieOperation

Type: string

Allowed values: `SetCookie`, `ReadCookie`

<a id="type-insighttype"></a>
### Audits.InsightType

Represents the category of insight that a cookie issue falls under.

Type: string

Allowed values: `GitHubResource`, `GracePeriod`, `Heuristics`

<a id="type-cookieissueinsight"></a>
### Audits.CookieIssueInsight

Information about the suggested solution to a cookie issue.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [Audits.InsightType](#type-insighttype) |  |
| `tableEntryUrl` (optional) | string | Link to table entry in third-party cookie migration readiness list. |

<a id="type-cookieissuedetails"></a>
### Audits.CookieIssueDetails

This information is currently necessary, as the front-end has a difficult
time finding a specific cookie. With this, we can convey specific error
information without the cookie.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `cookie` (optional) | [Audits.AffectedCookie](#type-affectedcookie) | If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line is syntactically or semantically malformed in a way that no valid cookie could be created. |
| `rawCookieLine` (optional) | string |  |
| `cookieWarningReasons` | array of [Audits.CookieWarningReason](#type-cookiewarningreason) |  |
| `cookieExclusionReasons` | array of [Audits.CookieExclusionReason](#type-cookieexclusionreason) |  |
| `operation` | [Audits.CookieOperation](#type-cookieoperation) | Optionally identifies the site-for-cookies and the cookie url, which may be used by the front-end as additional context. |
| `siteForCookies` (optional) | string |  |
| `cookieUrl` (optional) | string |  |
| `request` (optional) | [Audits.AffectedRequest](#type-affectedrequest) |  |
| `insight` (optional) | [Audits.CookieIssueInsight](#type-cookieissueinsight) | The recommended solution to the issue. |

<a id="type-performanceissuetype"></a>
### Audits.PerformanceIssueType

Type: string

Allowed values: `DocumentCookie`

<a id="type-performanceissuedetails"></a>
### Audits.PerformanceIssueDetails

Details for a performance issue.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `performanceIssueType` | [Audits.PerformanceIssueType](#type-performanceissuetype) |  |
| `sourceCodeLocation` (optional) | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |

<a id="type-mixedcontentresolutionstatus"></a>
### Audits.MixedContentResolutionStatus

Type: string

Allowed values: `MixedContentBlocked`, `MixedContentAutomaticallyUpgraded`, `MixedContentWarning`

<a id="type-mixedcontentresourcetype"></a>
### Audits.MixedContentResourceType

Type: string

Allowed values: `Audio`, `Beacon`, `CSPReport`, `Download`, `EventSource`, `Favicon`, `Font`, `Form`, `Frame`, `Image`, `Import`, `JSON`, `Manifest`, `Ping`, `PluginData`, `PluginResource`, `Prefetch`, `Resource`, `Script`, `ServiceWorker`, `SharedWorker`, `SpeculationRules`, `Stylesheet`, `Track`, `Video`, `Worker`, `XMLHttpRequest`, `XSLT`

<a id="type-mixedcontentissuedetails"></a>
### Audits.MixedContentIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `resourceType` (optional) | [Audits.MixedContentResourceType](#type-mixedcontentresourcetype) | The type of resource causing the mixed content issue (css, js, iframe, form,...). Marked as optional because it is mapped to from blink::mojom::RequestContextType, which will be replaced by network::mojom::RequestDestination |
| `resolutionStatus` | [Audits.MixedContentResolutionStatus](#type-mixedcontentresolutionstatus) | The way the mixed content issue is being resolved. |
| `insecureURL` | string | The unsafe http url causing the mixed content issue. |
| `mainResourceURL` | string | The url responsible for the call to an unsafe url. |
| `request` (optional) | [Audits.AffectedRequest](#type-affectedrequest) | The mixed content request. Does not always exist (e.g. for unsafe form submission urls). |
| `frame` (optional) | [Audits.AffectedFrame](#type-affectedframe) | Optional because not every mixed content issue is necessarily linked to a frame. |

<a id="type-blockedbyresponsereason"></a>
### Audits.BlockedByResponseReason

Enum indicating the reason a response has been blocked. These reasons are
refinements of the net error BLOCKED_BY_RESPONSE.

Type: string

Allowed values: `CoepFrameResourceNeedsCoepHeader`, `CoopSandboxedIFrameCannotNavigateToCoopPage`, `CorpNotSameOrigin`, `CorpNotSameOriginAfterDefaultedToSameOriginByCoep`, `CorpNotSameOriginAfterDefaultedToSameOriginByDip`, `CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip`, `CorpNotSameSite`, `SRIMessageSignatureMismatch`

<a id="type-blockedbyresponseissuedetails"></a>
### Audits.BlockedByResponseIssueDetails

Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
code. Currently only used for COEP/COOP, but may be extended to include
some CSP errors in the future.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |
| `parentFrame` (optional) | [Audits.AffectedFrame](#type-affectedframe) |  |
| `blockedFrame` (optional) | [Audits.AffectedFrame](#type-affectedframe) |  |
| `reason` | [Audits.BlockedByResponseReason](#type-blockedbyresponsereason) |  |

<a id="type-heavyadresolutionstatus"></a>
### Audits.HeavyAdResolutionStatus

Type: string

Allowed values: `HeavyAdBlocked`, `HeavyAdWarning`

<a id="type-heavyadreason"></a>
### Audits.HeavyAdReason

Type: string

Allowed values: `NetworkTotalLimit`, `CpuTotalLimit`, `CpuPeakLimit`

<a id="type-heavyadissuedetails"></a>
### Audits.HeavyAdIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `resolution` | [Audits.HeavyAdResolutionStatus](#type-heavyadresolutionstatus) | The resolution status, either blocking the content or warning. |
| `reason` | [Audits.HeavyAdReason](#type-heavyadreason) | The reason the ad was blocked, total network or cpu or peak cpu. |
| `frame` | [Audits.AffectedFrame](#type-affectedframe) | The frame that was blocked. |

<a id="type-contentsecuritypolicyviolationtype"></a>
### Audits.ContentSecurityPolicyViolationType

Type: string

Allowed values: `kInlineViolation`, `kEvalViolation`, `kURLViolation`, `kSRIViolation`, `kTrustedTypesSinkViolation`, `kTrustedTypesPolicyViolation`, `kWasmEvalViolation`

<a id="type-sourcecodelocation"></a>
### Audits.SourceCodeLocation

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` (optional) | [Runtime.ScriptId](Runtime.md#type-scriptid) |  |
| `url` | string |  |
| `lineNumber` | integer |  |
| `columnNumber` | integer |  |

<a id="type-contentsecuritypolicyissuedetails"></a>
### Audits.ContentSecurityPolicyIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `blockedURL` (optional) | string | The url not included in allowed sources. |
| `violatedDirective` | string | Specific directive that is violated, causing the CSP issue. |
| `isReportOnly` | boolean |  |
| `contentSecurityPolicyViolationType` | [Audits.ContentSecurityPolicyViolationType](#type-contentsecuritypolicyviolationtype) |  |
| `frameAncestor` (optional) | [Audits.AffectedFrame](#type-affectedframe) |  |
| `sourceCodeLocation` (optional) | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |
| `violatingNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |

<a id="type-sharedarraybufferissuetype"></a>
### Audits.SharedArrayBufferIssueType

Type: string

Allowed values: `TransferIssue`, `CreationIssue`

<a id="type-sharedarraybufferissuedetails"></a>
### Audits.SharedArrayBufferIssueDetails

Details for a issue arising from an SAB being instantiated in, or
transferred to a context that is not cross-origin isolated.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sourceCodeLocation` | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |
| `isWarning` | boolean |  |
| `type` | [Audits.SharedArrayBufferIssueType](#type-sharedarraybufferissuetype) |  |

<a id="type-corsissuedetails"></a>
### Audits.CorsIssueDetails

Details for a CORS related issue, e.g. a warning or error related to
CORS RFC1918 enforcement.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `corsErrorStatus` | [Network.CorsErrorStatus](Network.md#type-corserrorstatus) |  |
| `isWarning` | boolean |  |
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |
| `location` (optional) | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |
| `initiatorOrigin` (optional) | string |  |
| `resourceIPAddressSpace` (optional) | [Network.IPAddressSpace](Network.md#type-ipaddressspace) |  |
| `clientSecurityState` (optional) | [Network.ClientSecurityState](Network.md#type-clientsecuritystate) |  |

<a id="type-shareddictionaryerror"></a>
### Audits.SharedDictionaryError

Type: string

Allowed values: `UseErrorCrossOriginNoCorsRequest`, `UseErrorDictionaryLoadFailure`, `UseErrorMatchingDictionaryNotUsed`, `UseErrorUnexpectedContentDictionaryHeader`, `WriteErrorCossOriginNoCorsRequest`, `WriteErrorDisallowedBySettings`, `WriteErrorExpiredResponse`, `WriteErrorFeatureDisabled`, `WriteErrorInsufficientResources`, `WriteErrorInvalidMatchField`, `WriteErrorInvalidStructuredHeader`, `WriteErrorInvalidTTLField`, `WriteErrorNavigationRequest`, `WriteErrorNoMatchField`, `WriteErrorNonIntegerTTLField`, `WriteErrorNonListMatchDestField`, `WriteErrorNonSecureContext`, `WriteErrorNonStringIdField`, `WriteErrorNonStringInMatchDestList`, `WriteErrorInvalidMatchDestList`, `WriteErrorNonStringMatchField`, `WriteErrorNonTokenTypeField`, `WriteErrorRequestAborted`, `WriteErrorShuttingDown`, `WriteErrorTooLongIdField`, `WriteErrorUnsupportedType`

<a id="type-srimessagesignatureerror"></a>
### Audits.SRIMessageSignatureError

Type: string

Allowed values: `MissingSignatureHeader`, `MissingSignatureInputHeader`, `InvalidSignatureHeader`, `InvalidSignatureInputHeader`, `SignatureHeaderValueIsNotByteSequence`, `SignatureHeaderValueIsParameterized`, `SignatureHeaderValueIsIncorrectLength`, `SignatureInputHeaderMissingLabel`, `SignatureInputHeaderValueNotInnerList`, `SignatureInputHeaderValueMissingComponents`, `SignatureInputHeaderInvalidComponentType`, `SignatureInputHeaderInvalidComponentName`, `SignatureInputHeaderInvalidHeaderComponentParameter`, `SignatureInputHeaderInvalidDerivedComponentParameter`, `SignatureInputHeaderKeyIdLength`, `SignatureInputHeaderInvalidParameter`, `SignatureInputHeaderMissingRequiredParameters`, `ValidationFailedSignatureExpired`, `ValidationFailedInvalidLength`, `ValidationFailedSignatureMismatch`, `ValidationFailedIntegrityMismatch`, `SignatureBaseUnknownDerivedComponent`, `SignatureBaseMissingHeader`, `SignatureBaseInvalidUnencodedDigest`, `SignatureBaseUnsupportedComponent`

<a id="type-unencodeddigesterror"></a>
### Audits.UnencodedDigestError

Type: string

Allowed values: `MalformedDictionary`, `UnknownAlgorithm`, `IncorrectDigestType`, `IncorrectDigestLength`

<a id="type-connectionallowlisterror"></a>
### Audits.ConnectionAllowlistError

Type: string

Allowed values: `InvalidHeader`, `MoreThanOneList`, `ItemNotInnerList`, `InvalidAllowlistItemType`, `ReportingEndpointNotToken`, `InvalidUrlPattern`, `IFrameAttributeLoosensEmbeddingRequirement`, `InvalidAllowConnectionAllowlistFrom`, `EmbeddingRequirementNotSatisfied`

<a id="type-quirksmodeissuedetails"></a>
### Audits.QuirksModeIssueDetails

Details for issues about documents in Quirks Mode
or Limited Quirks Mode that affects page layouting.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `isLimitedQuirksMode` | boolean | If false, it means the document's mode is "quirks" instead of "limited-quirks". |
| `documentNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |
| `url` | string |  |
| `frameId` | [Page.FrameId](Page.md#type-frameid) |  |
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) |  |

<a id="type-navigatoruseragentissuedetails"></a>
### Audits.NavigatorUserAgentIssueDetails

**Deprecated**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string |  |
| `location` (optional) | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |

<a id="type-shareddictionaryissuedetails"></a>
### Audits.SharedDictionaryIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sharedDictionaryError` | [Audits.SharedDictionaryError](#type-shareddictionaryerror) |  |
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |

<a id="type-srimessagesignatureissuedetails"></a>
### Audits.SRIMessageSignatureIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `error` | [Audits.SRIMessageSignatureError](#type-srimessagesignatureerror) |  |
| `signatureBase` | string |  |
| `integrityAssertions` | array of string |  |
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |

<a id="type-unencodeddigestissuedetails"></a>
### Audits.UnencodedDigestIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `error` | [Audits.UnencodedDigestError](#type-unencodeddigesterror) |  |
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |

<a id="type-connectionallowlistissuedetails"></a>
### Audits.ConnectionAllowlistIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `error` | [Audits.ConnectionAllowlistError](#type-connectionallowlisterror) |  |
| `request` | [Audits.AffectedRequest](#type-affectedrequest) |  |

<a id="type-genericissueerrortype"></a>
### Audits.GenericIssueErrorType

Type: string

Allowed values: `FormLabelForNameError`, `FormDuplicateIdForInputError`, `FormInputWithNoLabelError`, `FormAutocompleteAttributeEmptyError`, `FormEmptyIdAndNameAttributesForInputError`, `FormAriaLabelledByToNonExistingIdError`, `FormInputAssignedAutocompleteValueToIdOrNameAttributeError`, `FormLabelHasNeitherForNorNestedInputError`, `FormLabelForMatchesNonExistingIdError`, `FormInputHasWrongButWellIntendedAutocompleteValueError`, `ResponseWasBlockedByORB`, `NavigationEntryMarkedSkippable`, `BackUINavigationWouldSkipAd`, `AutofillAndManualTextPolicyControlledFeaturesInfo`, `AutofillPolicyControlledFeatureInfo`, `ManualTextPolicyControlledFeatureInfo`, `FormModelContextParameterMissingTitleAndDescription`, `FormModelContextMissingToolName`, `FormModelContextMissingToolDescription`, `FormModelContextRequiredParameterMissingName`, `FormModelContextParameterMissingName`, `GeolocationPromptWithoutUserGesture`

<a id="type-genericissuedetails"></a>
### Audits.GenericIssueDetails

Depending on the concrete errorType, different properties are set.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `errorType` | [Audits.GenericIssueErrorType](#type-genericissueerrortype) | Issues with the same errorType are aggregated in the frontend. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) |  |
| `violatingNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |
| `violatingNodeAttribute` (optional) | string |  |
| `request` (optional) | [Audits.AffectedRequest](#type-affectedrequest) |  |

<a id="type-deprecationissuedetails"></a>
### Audits.DeprecationIssueDetails

This issue tracks information needed to print a deprecation message.
https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `affectedFrame` (optional) | [Audits.AffectedFrame](#type-affectedframe) |  |
| `sourceCodeLocation` | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |
| `type` | string | One of the deprecation names from third_party/blink/renderer/core/frame/deprecation/deprecation.json5 |

<a id="type-bouncetrackingissuedetails"></a>
### Audits.BounceTrackingIssueDetails

This issue warns about sites in the redirect chain of a finished navigation
that may be flagged as trackers and have their state cleared if they don't
receive a user interaction. Note that in this context 'site' means eTLD+1.
For example, if the URL `https://example.test:80/bounce` was in the
redirect chain, the site reported would be `example.test`.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `trackingSites` | array of string |  |

<a id="type-cookiedeprecationmetadataissuedetails"></a>
### Audits.CookieDeprecationMetadataIssueDetails

This issue warns about third-party sites that are accessing cookies on the
current page, and have been permitted due to having a global metadata grant.
Note that in this context 'site' means eTLD+1. For example, if the URL
`https://example.test:80/web_page` was accessing cookies, the site reported
would be `example.test`.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `allowedSites` | array of string |  |
| `optOutPercentage` | number |  |
| `isOptOutTopLevel` | boolean |  |
| `operation` | [Audits.CookieOperation](#type-cookieoperation) |  |

<a id="type-clienthintissuereason"></a>
### Audits.ClientHintIssueReason

Type: string

Allowed values: `MetaTagAllowListInvalidOrigin`, `MetaTagModifiedHTML`

<a id="type-federatedauthrequestissuedetails"></a>
### Audits.FederatedAuthRequestIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `federatedAuthRequestIssueReason` | [Audits.FederatedAuthRequestIssueReason](#type-federatedauthrequestissuereason) |  |

<a id="type-federatedauthrequestissuereason"></a>
### Audits.FederatedAuthRequestIssueReason

Represents the failure reason when a federated authentication reason fails.
Should be updated alongside RequestIdTokenStatus in
third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
all cases except for success.

Type: string

Allowed values: `ShouldEmbargo`, `TooManyRequests`, `WellKnownHttpNotFound`, `WellKnownNoResponse`, `WellKnownBlockedByConnectionAllowlist`, `WellKnownInvalidResponse`, `WellKnownListEmpty`, `WellKnownInvalidContentType`, `ConfigNotInWellKnown`, `WellKnownTooBig`, `ConfigHttpNotFound`, `ConfigNoResponse`, `ConfigBlockedByConnectionAllowlist`, `ConfigInvalidResponse`, `ConfigInvalidContentType`, `IdpNotPotentiallyTrustworthy`, `DisabledInSettings`, `DisabledInFlags`, `ErrorFetchingSignin`, `InvalidSigninResponse`, `AccountsHttpNotFound`, `AccountsNoResponse`, `AccountsBlockedByConnectionAllowlist`, `AccountsInvalidResponse`, `AccountsListEmpty`, `AccountsInvalidContentType`, `IdTokenHttpNotFound`, `IdTokenNoResponse`, `IdTokenBlockedByConnectionAllowlist`, `IdTokenInvalidResponse`, `IdTokenIdpErrorResponse`, `IdTokenCrossSiteIdpErrorResponse`, `IdTokenInvalidRequest`, `IdTokenInvalidContentType`, `ErrorIdToken`, `Canceled`, `RpPageNotVisible`, `SilentMediationFailure`, `NotSignedInWithIdp`, `MissingTransientUserActivation`, `ReplacedByActiveMode`, `RelyingPartyOriginIsOpaque`, `TypeNotMatching`, `UiDismissedNoEmbargo`, `CorsError`, `SuppressedBySegmentationPlatform`, `PopupBlockedByConnectionAllowlist`

<a id="type-federatedauthuserinforequestissuedetails"></a>
### Audits.FederatedAuthUserInfoRequestIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `federatedAuthUserInfoRequestIssueReason` | [Audits.FederatedAuthUserInfoRequestIssueReason](#type-federatedauthuserinforequestissuereason) |  |

<a id="type-federatedauthuserinforequestissuereason"></a>
### Audits.FederatedAuthUserInfoRequestIssueReason

Represents the failure reason when a getUserInfo() call fails.
Should be updated alongside FederatedAuthUserInfoRequestResult in
third_party/blink/public/mojom/devtools/inspector_issue.mojom.

Type: string

Allowed values: `NotSameOrigin`, `NotIframe`, `NotPotentiallyTrustworthy`, `NoApiPermission`, `NotSignedInWithIdp`, `NoAccountSharingPermission`, `InvalidConfigOrWellKnown`, `InvalidAccountsResponse`, `NoReturningUserFromFetchedAccounts`

<a id="type-emailverificationrequestissuedetails"></a>
### Audits.EmailVerificationRequestIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `emailVerificationRequestIssueReason` | [Audits.EmailVerificationRequestIssueReason](#type-emailverificationrequestissuereason) |  |

<a id="type-emailverificationrequestissuereason"></a>
### Audits.EmailVerificationRequestIssueReason

Represents the failure reason when an email verification request fails.
Should be updated alongside EmailVerificationRequestResult in
third_party/blink/public/mojom/devtools/inspector_issue.mojom.

Type: string

Allowed values: `InvalidEmail`, `DnsFetchFailed`, `DnsInvalidRecord`, `WellKnownHttpNotFound`, `WellKnownNoResponse`, `WellKnownInvalidResponse`, `WellKnownListEmpty`, `WellKnownInvalidContentType`, `WellKnownMissingIssuanceEndpoint`, `WellKnownIssuanceEndpointCrossOrigin`, `WellKnownUnsupportedSigningAlgorithm`, `TokenHttpNotFound`, `TokenNoResponse`, `TokenInvalidResponse`, `TokenInvalidContentType`, `TokenMalformedSdJwt`, `TokenInvalidSdJwt`, `KeyBindingSigningFailed`, `RpOriginIsOpaque`, `WellKnownMissingAccountsEndpoint`, `UserLoggedOut`, `WellKnownAccountsEndpointCrossOrigin`, `AccountsHttpNotFound`, `AccountsNoResponse`, `AccountsInvalidResponse`, `AccountsInvalidContentType`, `AccountsEmptyList`, `EmailVerificationWellKnownHttpNotFound`, `EmailVerificationWellKnownNoResponse`, `EmailVerificationWellKnownInvalidResponse`, `EmailVerificationWellKnownInvalidContentType`, `JwksHttpNotFound`, `JwksInvalidResponse`, `TokenVerificationSdJwtUnsupportedHeaderAlg`, `TokenVerificationSdJwtInvalidTyp`, `TokenVerificationSdJwtMissingIss`, `TokenVerificationSdJwtMissingIat`, `TokenVerificationSdJwtMissingCnf`, `TokenVerificationSdJwtMissingEmail`, `TokenVerificationSdJwtInvalidIssuedAt`, `TokenVerificationSdJwtInvalidIssuer`, `TokenVerificationSdJwtJwksMissingKeys`, `TokenVerificationSdJwtSignatureFailed`, `TokenVerificationSdJwtInvalidEmailVerified`, `TokenVerificationSdJwtInvalidEmail`, `TokenVerificationSdJwtInvalidHolderKey`, `TokenVerificationKbInvalidTyp`, `TokenVerificationKbMissingAud`, `TokenVerificationKbMissingNonce`, `TokenVerificationKbMissingIat`, `TokenVerificationKbMissingSdHash`, `TokenVerificationKbInvalidIssuedAt`, `TokenVerificationKbInvalidAudience`, `TokenVerificationKbInvalidNonce`, `TokenVerificationKbInvalidSdHash`, `TokenVerificationKbMissingCnf`, `TokenVerificationKbSignatureFailed`, `CrossOriginIframeNotSupported`

<a id="type-clienthintissuedetails"></a>
### Audits.ClientHintIssueDetails

This issue tracks client hints related issues. It's used to deprecate old
features, encourage the use of new ones, and provide general guidance.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sourceCodeLocation` | [Audits.SourceCodeLocation](#type-sourcecodelocation) |  |
| `clientHintIssueReason` | [Audits.ClientHintIssueReason](#type-clienthintissuereason) |  |

<a id="type-failedrequestinfo"></a>
### Audits.FailedRequestInfo

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The URL that failed to load. |
| `failureMessage` | string | The failure message for the failed request. |
| `requestId` (optional) | [Network.RequestId](Network.md#type-requestid) |  |

<a id="type-partitioningbloburlinfo"></a>
### Audits.PartitioningBlobURLInfo

Type: string

Allowed values: `BlockedCrossPartitionFetching`, `EnforceNoopenerForNavigation`

<a id="type-partitioningbloburlissuedetails"></a>
### Audits.PartitioningBlobURLIssueDetails

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The BlobURL that failed to load. |
| `partitioningBlobURLInfo` | [Audits.PartitioningBlobURLInfo](#type-partitioningbloburlinfo) | Additional information about the Partitioning Blob URL issue. |

<a id="type-elementaccessibilityissuereason"></a>
### Audits.ElementAccessibilityIssueReason

Type: string

Allowed values: `DisallowedSelectChild`, `DisallowedOptGroupChild`, `NonPhrasingContentOptionChild`, `InteractiveContentOptionChild`, `InteractiveContentLegendChild`, `InteractiveContentSummaryDescendant`, `AnchorMenuDescendant`, `InteractiveContentMenuDescendant`, `TextMenuDescendant`

<a id="type-elementaccessibilityissuedetails"></a>
### Audits.ElementAccessibilityIssueDetails

This issue warns about errors in the select, summary, or menu element content model.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |
| `elementAccessibilityIssueReason` | [Audits.ElementAccessibilityIssueReason](#type-elementaccessibilityissuereason) |  |
| `hasDisallowedAttributes` | boolean |  |

<a id="type-stylesheetloadingissuereason"></a>
### Audits.StyleSheetLoadingIssueReason

Type: string

Allowed values: `LateImportRule`, `RequestFailed`

<a id="type-stylesheetloadingissuedetails"></a>
### Audits.StylesheetLoadingIssueDetails

This issue warns when a referenced stylesheet couldn't be loaded.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sourceCodeLocation` | [Audits.SourceCodeLocation](#type-sourcecodelocation) | Source code position that referenced the failing stylesheet. |
| `styleSheetLoadingIssueReason` | [Audits.StyleSheetLoadingIssueReason](#type-stylesheetloadingissuereason) | Reason why the stylesheet couldn't be loaded. |
| `failedRequestInfo` (optional) | [Audits.FailedRequestInfo](#type-failedrequestinfo) | Contains additional info when the failure was due to a request. |

<a id="type-propertyruleissuereason"></a>
### Audits.PropertyRuleIssueReason

Type: string

Allowed values: `InvalidSyntax`, `InvalidInitialValue`, `InvalidInherits`, `InvalidName`

<a id="type-propertyruleissuedetails"></a>
### Audits.PropertyRuleIssueDetails

This issue warns about errors in property rules that lead to property
registrations being ignored.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sourceCodeLocation` | [Audits.SourceCodeLocation](#type-sourcecodelocation) | Source code position of the property rule. |
| `propertyRuleIssueReason` | [Audits.PropertyRuleIssueReason](#type-propertyruleissuereason) | Reason why the property rule was discarded. |
| `propertyValue` (optional) | string | The value of the property rule property that failed to parse |

<a id="type-userreidentificationissuetype"></a>
### Audits.UserReidentificationIssueType

Type: string

Allowed values: `BlockedFrameNavigation`, `BlockedSubresource`, `NoisedCanvasReadback`

<a id="type-userreidentificationissuedetails"></a>
### Audits.UserReidentificationIssueDetails

This issue warns about uses of APIs that may be considered misuse to
re-identify users.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [Audits.UserReidentificationIssueType](#type-userreidentificationissuetype) |  |
| `request` (optional) | [Audits.AffectedRequest](#type-affectedrequest) | Applies to BlockedFrameNavigation and BlockedSubresource issue types. |
| `sourceCodeLocation` (optional) | [Audits.SourceCodeLocation](#type-sourcecodelocation) | Applies to NoisedCanvasReadback issue type. |

<a id="type-permissionelementissuetype"></a>
### Audits.PermissionElementIssueType

Type: string

Allowed values: `InvalidType`, `FencedFrameDisallowed`, `CspFrameAncestorsMissing`, `PermissionsPolicyBlocked`, `PaddingRightUnsupported`, `PaddingBottomUnsupported`, `InsetBoxShadowUnsupported`, `RequestInProgress`, `UntrustedEvent`, `RegistrationFailed`, `TypeNotSupported`, `InvalidTypeActivation`, `SecurityChecksFailed`, `ActivationDisabled`, `GeolocationDeprecated`, `InvalidDisplayStyle`, `NonOpaqueColor`, `LowContrast`, `FontSizeTooSmall`, `FontSizeTooLarge`, `InvalidSizeValue`, `NonSecureContext`, `MissingTransientUserActivation`

<a id="type-permissionelementissuedetails"></a>
### Audits.PermissionElementIssueDetails

This issue warns about improper usage of the <permission> element.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `issueType` | [Audits.PermissionElementIssueType](#type-permissionelementissuetype) |  |
| `type` (optional) | string | The value of the type attribute. |
| `nodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The node ID of the <permission> element. |
| `isWarning` (optional) | boolean | True if the issue is a warning, false if it is an error. |
| `permissionName` (optional) | string | Fields for message construction: Used for messages that reference a specific permission name |
| `occluderNodeInfo` (optional) | string | Used for messages about occlusion |
| `occluderParentNodeInfo` (optional) | string | Used for messages about occluder's parent |
| `disableReason` (optional) | string | Used for messages about activation disabled reason |

<a id="type-webinstallissuereason"></a>
### Audits.WebInstallIssueReason

Type: string

Allowed values: `ManifestParsingOrNetworkError`, `StartUrlInvalid`, `ManifestMissingNameOrShortName`, `ManifestMissingId`, `NoManifest`

<a id="type-webinstallissuedetails"></a>
### Audits.WebInstallIssueDetails

This issue reports a failure involving a web app manifest used by a Web
Install operation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `manifestUrl` (optional) | string |  |
| `reason` | [Audits.WebInstallIssueReason](#type-webinstallissuereason) |  |

<a id="type-selectivepermissionsinterventionissuedetails"></a>
### Audits.SelectivePermissionsInterventionIssueDetails

The issue warns about blocked calls to privacy sensitive APIs via the
Selective Permissions Intervention.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `apiName` | string | Which API was intervened on. |
| `adAncestry` | [Network.AdAncestry](Network.md#type-adancestry) | Why the ad script using the API is considered an ad. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | The stack trace at the time of the intervention. |

<a id="type-lazyloadimageissuedetails"></a>
### Audits.LazyLoadImageIssueDetails

Details for issues about lazy-loaded images without explicit dimensions.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | DOM node of the problematic HTMLImageElement. |
| `url` | string | URL or src attribute of the image. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame containing the image. |

<a id="type-viewportfitcovermissingsafeareainsettopissuedetails"></a>
### Audits.ViewportFitCoverMissingSafeAreaInsetTopIssueDetails

Details for issues about a page that declares viewport-fit=cover, receives
a non-zero top safe-area inset (e.g. a device cutout or system status bar),
but does not consume env(safe-area-inset-top) anywhere in its CSS while
having DOM content likely to be occluded by that inset.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The frame that triggered the issue. |

<a id="type-inspectorissuecode"></a>
### Audits.InspectorIssueCode

A unique identifier for the type of issue. Each type may use one of the
optional fields in InspectorIssueDetails to convey more specific
information about the kind of issue.

Type: string

Allowed values: `CookieIssue`, `MixedContentIssue`, `BlockedByResponseIssue`, `HeavyAdIssue`, `ContentSecurityPolicyIssue`, `SharedArrayBufferIssue`, `CorsIssue`, `QuirksModeIssue`, `PartitioningBlobURLIssue`, `NavigatorUserAgentIssue`, `GenericIssue`, `DeprecationIssue`, `ClientHintIssue`, `FederatedAuthRequestIssue`, `BounceTrackingIssue`, `CookieDeprecationMetadataIssue`, `StylesheetLoadingIssue`, `FederatedAuthUserInfoRequestIssue`, `PropertyRuleIssue`, `SharedDictionaryIssue`, `ElementAccessibilityIssue`, `SRIMessageSignatureIssue`, `UnencodedDigestIssue`, `ConnectionAllowlistIssue`, `UserReidentificationIssue`, `PermissionElementIssue`, `PerformanceIssue`, `SelectivePermissionsInterventionIssue`, `EmailVerificationRequestIssue`, `LazyLoadImageIssue`, `WebInstallIssue`, `ViewportFitCoverMissingSafeAreaInsetTopIssue`

<a id="type-inspectorissuedetails"></a>
### Audits.InspectorIssueDetails

This struct holds a list of optional fields with additional information
specific to the kind of issue. When adding a new issue code, please also
add a new optional field to this type.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `cookieIssueDetails` (optional) | [Audits.CookieIssueDetails](#type-cookieissuedetails) |  |
| `mixedContentIssueDetails` (optional) | [Audits.MixedContentIssueDetails](#type-mixedcontentissuedetails) |  |
| `blockedByResponseIssueDetails` (optional) | [Audits.BlockedByResponseIssueDetails](#type-blockedbyresponseissuedetails) |  |
| `heavyAdIssueDetails` (optional) | [Audits.HeavyAdIssueDetails](#type-heavyadissuedetails) |  |
| `contentSecurityPolicyIssueDetails` (optional) | [Audits.ContentSecurityPolicyIssueDetails](#type-contentsecuritypolicyissuedetails) |  |
| `sharedArrayBufferIssueDetails` (optional) | [Audits.SharedArrayBufferIssueDetails](#type-sharedarraybufferissuedetails) |  |
| `corsIssueDetails` (optional) | [Audits.CorsIssueDetails](#type-corsissuedetails) |  |
| `quirksModeIssueDetails` (optional) | [Audits.QuirksModeIssueDetails](#type-quirksmodeissuedetails) |  |
| `partitioningBlobURLIssueDetails` (optional) | [Audits.PartitioningBlobURLIssueDetails](#type-partitioningbloburlissuedetails) |  |
| `navigatorUserAgentIssueDetails` (optional) | [Audits.NavigatorUserAgentIssueDetails](#type-navigatoruseragentissuedetails) | **Deprecated** |
| `genericIssueDetails` (optional) | [Audits.GenericIssueDetails](#type-genericissuedetails) |  |
| `deprecationIssueDetails` (optional) | [Audits.DeprecationIssueDetails](#type-deprecationissuedetails) |  |
| `clientHintIssueDetails` (optional) | [Audits.ClientHintIssueDetails](#type-clienthintissuedetails) |  |
| `federatedAuthRequestIssueDetails` (optional) | [Audits.FederatedAuthRequestIssueDetails](#type-federatedauthrequestissuedetails) |  |
| `bounceTrackingIssueDetails` (optional) | [Audits.BounceTrackingIssueDetails](#type-bouncetrackingissuedetails) |  |
| `cookieDeprecationMetadataIssueDetails` (optional) | [Audits.CookieDeprecationMetadataIssueDetails](#type-cookiedeprecationmetadataissuedetails) |  |
| `stylesheetLoadingIssueDetails` (optional) | [Audits.StylesheetLoadingIssueDetails](#type-stylesheetloadingissuedetails) |  |
| `propertyRuleIssueDetails` (optional) | [Audits.PropertyRuleIssueDetails](#type-propertyruleissuedetails) |  |
| `federatedAuthUserInfoRequestIssueDetails` (optional) | [Audits.FederatedAuthUserInfoRequestIssueDetails](#type-federatedauthuserinforequestissuedetails) |  |
| `sharedDictionaryIssueDetails` (optional) | [Audits.SharedDictionaryIssueDetails](#type-shareddictionaryissuedetails) |  |
| `elementAccessibilityIssueDetails` (optional) | [Audits.ElementAccessibilityIssueDetails](#type-elementaccessibilityissuedetails) |  |
| `sriMessageSignatureIssueDetails` (optional) | [Audits.SRIMessageSignatureIssueDetails](#type-srimessagesignatureissuedetails) |  |
| `unencodedDigestIssueDetails` (optional) | [Audits.UnencodedDigestIssueDetails](#type-unencodeddigestissuedetails) |  |
| `connectionAllowlistIssueDetails` (optional) | [Audits.ConnectionAllowlistIssueDetails](#type-connectionallowlistissuedetails) |  |
| `userReidentificationIssueDetails` (optional) | [Audits.UserReidentificationIssueDetails](#type-userreidentificationissuedetails) |  |
| `permissionElementIssueDetails` (optional) | [Audits.PermissionElementIssueDetails](#type-permissionelementissuedetails) |  |
| `performanceIssueDetails` (optional) | [Audits.PerformanceIssueDetails](#type-performanceissuedetails) |  |
| `selectivePermissionsInterventionIssueDetails` (optional) | [Audits.SelectivePermissionsInterventionIssueDetails](#type-selectivepermissionsinterventionissuedetails) |  |
| `emailVerificationRequestIssueDetails` (optional) | [Audits.EmailVerificationRequestIssueDetails](#type-emailverificationrequestissuedetails) |  |
| `lazyLoadImageIssueDetails` (optional) | [Audits.LazyLoadImageIssueDetails](#type-lazyloadimageissuedetails) |  |
| `webInstallIssueDetails` (optional) | [Audits.WebInstallIssueDetails](#type-webinstallissuedetails) |  |
| `viewportFitCoverMissingSafeAreaInsetTopIssueDetails` (optional) | [Audits.ViewportFitCoverMissingSafeAreaInsetTopIssueDetails](#type-viewportfitcovermissingsafeareainsettopissuedetails) |  |

<a id="type-issueid"></a>
### Audits.IssueId

A unique id for a DevTools inspector issue. Allows other entities (e.g.
exceptions, CDP message, console messages, etc.) to reference an issue.

Type: string

<a id="type-inspectorissue"></a>
### Audits.InspectorIssue

An inspector issue reported from the back-end.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `code` | [Audits.InspectorIssueCode](#type-inspectorissuecode) |  |
| `details` | [Audits.InspectorIssueDetails](#type-inspectorissuedetails) |  |
| `issueId` (optional) | [Audits.IssueId](#type-issueid) | A unique id for this issue. May be omitted if no other entity (e.g. exception, CDP message, etc.) is referencing this issue. |
