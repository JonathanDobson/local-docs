# Security domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `Security.<command>` and events arrive as `Security.<event>`.

## Commands

### Security.disable

Disables tracking security state changes.

### Security.enable

Enables tracking security state changes.

### Security.setIgnoreCertificateErrors

Enable/disable whether all certificate errors should be ignored.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ignore` | boolean | If true, all certificate errors will be ignored. |

### Security.handleCertificateError *(deprecated)*

Handles a certificate error that fired a certificateError event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventId` | integer | The ID of the event. |
| `action` | [CertificateErrorAction](#type-certificateerroraction) | The action to take on the certificate error. |

### Security.setOverrideCertificateErrors *(deprecated)*

Enable/disable overriding certificate errors. If enabled, all certificate error events need to be handled by the DevTools client and should be answered with `handleCertificateError` commands.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `override` | boolean | If true, certificate errors will be overridden. |

## Events

### Security.certificateError *(deprecated)*

There is a certificate error. If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command. Note: this event does not fire if the certificate error has been allowed internally. Only one client per target should override certificate errors at the same time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventId` | integer | The ID of the event. |
| `errorType` | string | The type of the error. |
| `requestURL` | string | The url that was requested. |

### Security.visibleSecurityStateChanged *(experimental)*

The security state of the page changed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `visibleSecurityState` | [VisibleSecurityState](#type-visiblesecuritystate) | Security state information about the page. |

### Security.securityStateChanged *(deprecated)*

The security state of the page changed. No longer being sent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityState` | [SecurityState](#type-securitystate) | Security state. |
| `schemeIsCryptographic` *(deprecated)* | boolean | True if the page was loaded over cryptographic transport such as HTTPS. |
| `explanations` *(deprecated)* | array of [SecurityStateExplanation](#type-securitystateexplanation) | Previously a list of explanations for the security state. Now always empty. |
| `insecureContentStatus` *(deprecated)* | [InsecureContentStatus](#type-insecurecontentstatus) | Information about insecure content on the page. |
| `summary` (optional) *(deprecated)* | string | Overrides user-visible description of the state. Always omitted. |

## Types

<a id="type-certificateid"></a>
### Security.CertificateId

Type: integer

An internal certificate ID value.

<a id="type-mixedcontenttype"></a>
### Security.MixedContentType

Type: string

A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories

Allowed values: `blockable`, `optionally-blockable`, `none`

<a id="type-securitystate"></a>
### Security.SecurityState

Type: string

The security level of a page or resource.

Allowed values: `unknown`, `neutral`, `insecure`, `secure`, `info`, `insecure-broken`

<a id="type-certificatesecuritystate"></a>
### Security.CertificateSecurityState *(experimental)*

Type: object

Details about the security state of the page certificate.

**Properties**

| Name | Type | Description |
|---|---|---|
| `protocol` | string | Protocol name (e.g. "TLS 1.2" or "QUIC"). |
| `keyExchange` | string | Key Exchange used by the connection, or the empty string if not applicable. |
| `keyExchangeGroup` (optional) | string | (EC)DH group used by the connection, if applicable. |
| `cipher` | string | Cipher name. |
| `mac` (optional) | string | TLS MAC. Note that AEAD ciphers do not have separate MACs. |
| `certificate` | array of string | Page certificate. |
| `subjectName` | string | Certificate subject name. |
| `issuer` | string | Name of the issuing CA. |
| `validFrom` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Certificate valid from date. |
| `validTo` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Certificate valid to (expiration) date |
| `certificateNetworkError` (optional) | string | The highest priority network error code, if the certificate has an error. |
| `certificateHasWeakSignature` | boolean | True if the certificate uses a weak signature algorithm. |
| `certificateHasSha1Signature` | boolean | True if the certificate has a SHA1 signature in the chain. |
| `modernSSL` | boolean | True if modern SSL |
| `obsoleteSslProtocol` | boolean | True if the connection is using an obsolete SSL protocol. |
| `obsoleteSslKeyExchange` | boolean | True if the connection is using an obsolete SSL key exchange. |
| `obsoleteSslCipher` | boolean | True if the connection is using an obsolete SSL cipher. |
| `obsoleteSslSignature` | boolean | True if the connection is using an obsolete SSL signature. |

<a id="type-safetytipstatus"></a>
### Security.SafetyTipStatus *(experimental)*

Type: string

Allowed values: `badReputation`, `lookalike`

<a id="type-safetytipinfo"></a>
### Security.SafetyTipInfo *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `safetyTipStatus` | [SafetyTipStatus](#type-safetytipstatus) | Describes whether the page triggers any safety tips or reputation warnings. Default is unknown. |
| `safeUrl` (optional) | string | The URL the safety tip suggested ("Did you mean?"). Only filled in for lookalike matches. |

<a id="type-visiblesecuritystate"></a>
### Security.VisibleSecurityState *(experimental)*

Type: object

Security state information about the page.

**Properties**

| Name | Type | Description |
|---|---|---|
| `securityState` | [SecurityState](#type-securitystate) | The security level of the page. |
| `certificateSecurityState` (optional) | [CertificateSecurityState](#type-certificatesecuritystate) | Security state details about the page certificate. |
| `safetyTipInfo` (optional) | [SafetyTipInfo](#type-safetytipinfo) | The type of Safety Tip triggered on the page. Note that this field will be set even if the Safety Tip UI was not actually shown. |
| `securityStateIssueIds` | array of string | Array of security state issues ids. |

<a id="type-securitystateexplanation"></a>
### Security.SecurityStateExplanation

Type: object

An explanation of an factor contributing to the security state.

**Properties**

| Name | Type | Description |
|---|---|---|
| `securityState` | [SecurityState](#type-securitystate) | Security state representing the severity of the factor being explained. |
| `title` | string | Title describing the type of factor. |
| `summary` | string | Short phrase describing the type of factor. |
| `description` | string | Full text explanation of the factor. |
| `mixedContentType` | [MixedContentType](#type-mixedcontenttype) | The type of mixed content described by the explanation. |
| `certificate` | array of string | Page certificate. |
| `recommendations` (optional) | array of string | Recommendations to fix any issues. |

<a id="type-insecurecontentstatus"></a>
### Security.InsecureContentStatus *(deprecated)*

Type: object

Information about insecure content on the page.

**Properties**

| Name | Type | Description |
|---|---|---|
| `ranMixedContent` | boolean | Always false. |
| `displayedMixedContent` | boolean | Always false. |
| `containedMixedForm` | boolean | Always false. |
| `ranContentWithCertErrors` | boolean | Always false. |
| `displayedContentWithCertErrors` | boolean | Always false. |
| `ranInsecureContentStyle` | [SecurityState](#type-securitystate) | Always set to unknown. |
| `displayedInsecureContentStyle` | [SecurityState](#type-securitystate) | Always set to unknown. |

<a id="type-certificateerroraction"></a>
### Security.CertificateErrorAction

Type: string

The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request.

Allowed values: `continue`, `cancel`

