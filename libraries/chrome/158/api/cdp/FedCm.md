# FedCm domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain allows interacting with the FedCM dialog.

Methods are called as `FedCm.<command>` and events arrive as `FedCm.<event>`.

## Commands

### FedCm.enable

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disableRejectionDelay` (optional) | boolean | Allows callers to disable the promise rejection delay that would normally happen, if this is unimportant to what's being tested. (step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in) |

### FedCm.disable

### FedCm.selectAccount

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `accountIndex` | integer |  |

### FedCm.clickDialogButton

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `dialogButton` | [DialogButton](#type-dialogbutton) |  |

### FedCm.openUrl

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `accountIndex` | integer |  |
| `accountUrlType` | [AccountUrlType](#type-accounturltype) |  |

### FedCm.dismissDialog

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `triggerCooldown` (optional) | boolean |  |

### FedCm.resetCooldown

Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user.

## Events

### FedCm.dialogShown

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `dialogType` | [DialogType](#type-dialogtype) |  |
| `accounts` | array of [Account](#type-account) |  |
| `title` | string | These exist primarily so that the caller can verify the RP context was used appropriately. |
| `subtitle` (optional) | string |  |

### FedCm.dialogClosed

Triggered when a dialog is closed, either by user action, JS abort, or a command below.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |

## Types

<a id="type-loginstate"></a>
### FedCm.LoginState

Type: string

Whether this is a sign-up or sign-in action for this account, i.e. whether this account has ever been used to sign in to this RP before.

Allowed values: `SignIn`, `SignUp`

<a id="type-dialogtype"></a>
### FedCm.DialogType

Type: string

The types of FedCM dialogs.

Allowed values: `AccountChooser`, `AutoReauthn`, `ConfirmIdpLogin`, `Error`

<a id="type-dialogbutton"></a>
### FedCm.DialogButton

Type: string

The buttons on the FedCM dialog.

Allowed values: `ConfirmIdpLoginContinue`, `ErrorGotIt`, `ErrorMoreDetails`

<a id="type-accounturltype"></a>
### FedCm.AccountUrlType

Type: string

The URLs that each account has

Allowed values: `TermsOfService`, `PrivacyPolicy`

<a id="type-account"></a>
### FedCm.Account

Type: object

Corresponds to IdentityRequestAccount

**Properties**

| Name | Type | Description |
|---|---|---|
| `accountId` | string |  |
| `email` | string |  |
| `name` | string |  |
| `givenName` | string |  |
| `pictureUrl` | string |  |
| `idpConfigUrl` | string |  |
| `idpLoginUrl` | string |  |
| `loginState` | [LoginState](#type-loginstate) |  |
| `termsOfServiceUrl` (optional) | string | These two are only set if the loginState is signUp |
| `privacyPolicyUrl` (optional) | string |  |

