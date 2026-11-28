# WebAuthn domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain allows configuring virtual authenticators to test the WebAuthn API.

Methods are called as `WebAuthn.<command>` and events arrive as `WebAuthn.<event>`.

## Commands

### WebAuthn.enable

Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enableUI` (optional) | boolean | Whether to enable the WebAuthn user interface. Enabling the UI is recommended for debugging and demo purposes, as it is closer to the real experience. Disabling the UI is recommended for automated testing. Supported at the embedder's discretion if UI is available. Defaults to false. |

### WebAuthn.disable

Disable the WebAuthn domain.

### WebAuthn.addVirtualAuthenticator

Creates and adds a virtual authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `options` | [VirtualAuthenticatorOptions](#type-virtualauthenticatoroptions) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |

### WebAuthn.setResponseOverrideBits

Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `isBogusSignature` (optional) | boolean | If isBogusSignature is set, overrides the signature in the authenticator response to be zero. Defaults to false. |
| `isBadUV` (optional) | boolean | If isBadUV is set, overrides the UV bit in the flags in the authenticator response to be zero. Defaults to false. |
| `isBadUP` (optional) | boolean | If isBadUP is set, overrides the UP bit in the flags in the authenticator response to be zero. Defaults to false. |

### WebAuthn.removeVirtualAuthenticator

Removes the given authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |

### WebAuthn.addCredential

Adds the credential to the specified authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credential` | [Credential](#type-credential) |  |

### WebAuthn.getCredential

Returns a single credential stored in the given virtual authenticator that matches the credential ID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credentialId` | binary |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `credential` | [Credential](#type-credential) |  |

### WebAuthn.getCredentials

Returns all the credentials stored in the given virtual authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `credentials` | array of [Credential](#type-credential) |  |

### WebAuthn.removeCredential

Removes a credential from the authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credentialId` | binary |  |

### WebAuthn.clearCredentials

Clears all the credentials from the specified device.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |

### WebAuthn.setUserVerified

Sets whether User Verification succeeds or fails for an authenticator. The default is true.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `isUserVerified` | boolean |  |

### WebAuthn.setAutomaticPresenceSimulation

Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator. The default is true.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `enabled` | boolean |  |

### WebAuthn.setCredentialProperties

Allows setting credential properties. https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credentialId` | binary |  |
| `backupEligibility` (optional) | boolean |  |
| `backupState` (optional) | boolean |  |
| `activeCmtgKeyIndex` (optional) | integer |  |
| `generateCmtgKeyOnNextOperation` (optional) | boolean |  |
| `signCount` (optional) | number | Must be equal to or greater than -1. If -1, the signature counter is removed from the credential, and every assertion operation will report a value of 0. See https://w3c.github.io/webauthn/#signature-counter |

## Events

### WebAuthn.credentialAdded

Triggered when a credential is added to an authenticator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credential` | [Credential](#type-credential) |  |

### WebAuthn.credentialDeleted

Triggered when a credential is deleted, e.g. through PublicKeyCredential.signalUnknownCredential().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credentialId` | binary |  |

### WebAuthn.credentialUpdated

Triggered when a credential is updated, e.g. through PublicKeyCredential.signalCurrentUserDetails().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credential` | [Credential](#type-credential) |  |

### WebAuthn.credentialAsserted

Triggered when a credential is used in a webauthn assertion.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `authenticatorId` | [AuthenticatorId](#type-authenticatorid) |  |
| `credential` | [Credential](#type-credential) |  |

## Types

<a id="type-authenticatorid"></a>
### WebAuthn.AuthenticatorId

Type: string

<a id="type-authenticatorprotocol"></a>
### WebAuthn.AuthenticatorProtocol

Type: string

Allowed values: `u2f`, `ctap2`

<a id="type-ctap2version"></a>
### WebAuthn.Ctap2Version

Type: string

Allowed values: `ctap2_0`, `ctap2_1`, `ctap2_2`

<a id="type-authenticatortransport"></a>
### WebAuthn.AuthenticatorTransport

Type: string

LINT.IfChange(AuthenticatorTransport)

Allowed values: `usb`, `nfc`, `ble`, `cable`, `hybrid`, `smart-card`, `internal`

<a id="type-virtualauthenticatoroptions"></a>
### WebAuthn.VirtualAuthenticatorOptions

Type: object

LINT.ThenChange(//content/browser/devtools/protocol/webauthn_handler.cc:ConvertToFidoTransportProtocol)

**Properties**

| Name | Type | Description |
|---|---|---|
| `protocol` | [AuthenticatorProtocol](#type-authenticatorprotocol) |  |
| `ctap2Version` (optional) | [Ctap2Version](#type-ctap2version) | Defaults to ctap2_0. Ignored if \|protocol\| == u2f. |
| `transport` | [AuthenticatorTransport](#type-authenticatortransport) |  |
| `hasResidentKey` (optional) | boolean | Defaults to false. |
| `hasUserVerification` (optional) | boolean | Defaults to false. |
| `hasLargeBlob` (optional) | boolean | If set to true, the authenticator will support the largeBlob extension. https://w3c.github.io/webauthn#largeBlob Defaults to false. |
| `hasCredBlob` (optional) | boolean | If set to true, the authenticator will support the credBlob extension. https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension Defaults to false. |
| `hasMinPinLength` (optional) | boolean | If set to true, the authenticator will support the minPinLength extension. https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extension Defaults to false. |
| `hasPrf` (optional) | boolean | If set to true, the authenticator will support the prf extension. https://w3c.github.io/webauthn/#prf-extension Defaults to false. |
| `hasHmacSecret` (optional) | boolean | If set to true, the authenticator will support the hmac-secret extension. https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-hmac-secret-extension Defaults to false. |
| `hasHmacSecretMc` (optional) | boolean | If set to true, the authenticator will support the hmac-secret-mc extension. https://fidoalliance.org/specs/fido-v2.2-rd-20241003/fido-client-to-authenticator-protocol-v2.2-rd-20241003.html#sctn-hmac-secret-make-cred-extension Defaults to false. |
| `hasCmtgKey` (optional) | boolean | If set to true, the authenticator will support the cmtgKey (Credential Manager Trust Group Key) extension. https://github.com/w3c/webauthn/pull/2377 Defaults to false. |
| `automaticPresenceSimulation` (optional) | boolean | If set to true, tests of user presence will succeed immediately. Otherwise, they will not be resolved. Defaults to true. |
| `isUserVerified` (optional) | boolean | Sets whether User Verification succeeds or fails for an authenticator. Defaults to false. |
| `defaultBackupEligibility` (optional) | boolean | Credentials created by this authenticator will have the backup eligibility (BE) flag set to this value. Defaults to false. https://w3c.github.io/webauthn/#sctn-credential-backup |
| `defaultBackupState` (optional) | boolean | Credentials created by this authenticator will have the backup state (BS) flag set to this value. Defaults to false. https://w3c.github.io/webauthn/#sctn-credential-backup |

<a id="type-credential"></a>
### WebAuthn.Credential

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `credentialId` | binary |  |
| `isResidentCredential` | boolean |  |
| `rpId` (optional) | string | Relying Party ID the credential is scoped to. Must be set when adding a credential. |
| `privateKey` | binary | The ECDSA P-256 private key in PKCS#8 format. |
| `userHandle` (optional) | binary | An opaque byte sequence with a maximum size of 64 bytes mapping the credential to a specific user. |
| `signCount` | number | Signature counter. Must be equal to or greater than -1. If -1, the credential won't have an associated signature counter, and every assertion operation will report a value of 0. See https://w3c.github.io/webauthn/#signature-counter |
| `largeBlob` (optional) | binary | The large blob associated with the credential. See https://w3c.github.io/webauthn/#sctn-large-blob-extension |
| `backupEligibility` (optional) | boolean | Assertions returned by this credential will have the backup eligibility (BE) flag set to this value. Defaults to the authenticator's defaultBackupEligibility value. |
| `backupState` (optional) | boolean | Assertions returned by this credential will have the backup state (BS) flag set to this value. Defaults to the authenticator's defaultBackupState value. |
| `userName` (optional) | string | The credential's user.name property. Equivalent to empty if not set. https://w3c.github.io/webauthn/#dom-publickeycredentialentity-name |
| `userDisplayName` (optional) | string | The credential's user.displayName property. Equivalent to empty if not set. https://w3c.github.io/webauthn/#dom-publickeycredentialuserentity-displayname |
| `cmtgKeys` (optional) | array of binary | The CMTG keys associated with the credential. |
| `activeCmtgKeyIndex` (optional) | integer | The 0-based index of the active key in cmtgKeys. |
| `generateCmtgKeyOnNextOperation` (optional) | boolean | If true, the authenticator will generate a new CMTG key on the next operation. |

