# FedCm domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain allows interacting with the FedCM dialog.

7 methods, 2 events, 5 types.

## Methods

### FedCm.enable

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disableRejectionDelay` (optional) | boolean | Allows callers to disable the promise rejection delay that would normally happen, if this is unimportant to what's being tested. (step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in) |

### FedCm.disable

No parameters.

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
| `dialogButton` | [FedCm.DialogButton](#type-dialogbutton) |  |

### FedCm.openUrl

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `accountIndex` | integer |  |
| `accountUrlType` | [FedCm.AccountUrlType](#type-accounturltype) |  |

### FedCm.dismissDialog

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `triggerCooldown` (optional) | boolean |  |

### FedCm.resetCooldown

Resets the cooldown time, if any, to allow the next FedCM call to show
a dialog even if one was recently dismissed by the user.

No parameters.

## Events

### FedCm.dialogShown

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |
| `dialogType` | [FedCm.DialogType](#type-dialogtype) |  |
| `accounts` | array of [FedCm.Account](#type-account) |  |
| `title` | string | These exist primarily so that the caller can verify the RP context was used appropriately. |
| `subtitle` (optional) | string |  |

### FedCm.dialogClosed

Triggered when a dialog is closed, either by user action, JS abort,
or a command below.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `dialogId` | string |  |

## Types

<a id="type-loginstate"></a>
### FedCm.LoginState

Whether this is a sign-up or sign-in action for this account, i.e.
whether this account has ever been used to sign in to this RP before.

Type: string

Allowed values: `SignIn`, `SignUp`

<a id="type-dialogtype"></a>
### FedCm.DialogType

The types of FedCM dialogs.

Type: string

Allowed values: `AccountChooser`, `AutoReauthn`, `ConfirmIdpLogin`, `Error`

<a id="type-dialogbutton"></a>
### FedCm.DialogButton

The buttons on the FedCM dialog.

Type: string

Allowed values: `ConfirmIdpLoginContinue`, `ErrorGotIt`, `ErrorMoreDetails`

<a id="type-accounturltype"></a>
### FedCm.AccountUrlType

The URLs that each account has

Type: string

Allowed values: `TermsOfService`, `PrivacyPolicy`

<a id="type-account"></a>
### FedCm.Account

Corresponds to IdentityRequestAccount

Type: object

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
| `loginState` | [FedCm.LoginState](#type-loginstate) |  |
| `termsOfServiceUrl` (optional) | string | These two are only set if the loginState is signUp |
| `privacyPolicyUrl` (optional) | string |  |
