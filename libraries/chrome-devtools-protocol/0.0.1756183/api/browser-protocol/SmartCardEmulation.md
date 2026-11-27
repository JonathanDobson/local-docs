# SmartCardEmulation domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

12 methods, 14 events, 9 types.

## Methods

### SmartCardEmulation.enable

Enables the |SmartCardEmulation| domain.

No parameters.

### SmartCardEmulation.disable

Disables the |SmartCardEmulation| domain.

No parameters.

### SmartCardEmulation.reportEstablishContextResult

Reports the successful result of a |SCardEstablishContext| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |

### SmartCardEmulation.reportReleaseContextResult

Reports the successful result of a |SCardReleaseContext| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |

### SmartCardEmulation.reportListReadersResult

Reports the successful result of a |SCardListReaders| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `readers` | array of string |  |

### SmartCardEmulation.reportGetStatusChangeResult

Reports the successful result of a |SCardGetStatusChange| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `readerStates` | array of [SmartCardEmulation.ReaderStateOut](#type-readerstateout) |  |

### SmartCardEmulation.reportBeginTransactionResult

Reports the result of a |SCardBeginTransaction| call.
On success, this creates a new transaction object.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |

### SmartCardEmulation.reportPlainResult

Reports the successful result of a call that returns only a result code.
Used for: |SCardCancel|, |SCardDisconnect|, |SCardSetAttrib|, |SCardEndTransaction|.

This maps to:
1. SCardCancel
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel

2. SCardDisconnect
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect

3. SCardSetAttrib
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib

4. SCardEndTransaction
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |

### SmartCardEmulation.reportConnectResult

Reports the successful result of a |SCardConnect| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `activeProtocol` (optional) | [SmartCardEmulation.Protocol](#type-protocol) |  |

### SmartCardEmulation.reportDataResult

Reports the successful result of a call that sends back data on success.
Used for |SCardTransmit|, |SCardControl|, and |SCardGetAttrib|.

This maps to:
1. SCardTransmit
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit

2. SCardControl
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol

3. SCardGetAttrib
   PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602
   Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `data` | string |  |

### SmartCardEmulation.reportStatusResult

Reports the successful result of a |SCardStatus| call.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `readerName` | string |  |
| `state` | [SmartCardEmulation.ConnectionState](#type-connectionstate) |  |
| `atr` | string |  |
| `protocol` (optional) | [SmartCardEmulation.Protocol](#type-protocol) |  |

### SmartCardEmulation.reportError

Reports an error result for the given request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `resultCode` | [SmartCardEmulation.ResultCode](#type-resultcode) |  |

## Events

### SmartCardEmulation.establishContextRequested

Fired when |SCardEstablishContext| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |

### SmartCardEmulation.releaseContextRequested

Fired when |SCardReleaseContext| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |

### SmartCardEmulation.listReadersRequested

Fired when |SCardListReaders| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |

### SmartCardEmulation.getStatusChangeRequested

Fired when |SCardGetStatusChange| is called. Timeout is specified in milliseconds.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |
| `readerStates` | array of [SmartCardEmulation.ReaderStateIn](#type-readerstatein) |  |
| `timeout` (optional) | integer | in milliseconds, if absent, it means "infinite" |

### SmartCardEmulation.cancelRequested

Fired when |SCardCancel| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |

### SmartCardEmulation.connectRequested

Fired when |SCardConnect| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `contextId` | integer |  |
| `reader` | string |  |
| `shareMode` | [SmartCardEmulation.ShareMode](#type-sharemode) |  |
| `preferredProtocols` | [SmartCardEmulation.ProtocolSet](#type-protocolset) |  |

### SmartCardEmulation.disconnectRequested

Fired when |SCardDisconnect| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `disposition` | [SmartCardEmulation.Disposition](#type-disposition) |  |

### SmartCardEmulation.transmitRequested

Fired when |SCardTransmit| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `data` | string |  |
| `protocol` (optional) | [SmartCardEmulation.Protocol](#type-protocol) |  |

### SmartCardEmulation.controlRequested

Fired when |SCardControl| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `controlCode` | integer |  |
| `data` | string |  |

### SmartCardEmulation.getAttribRequested

Fired when |SCardGetAttrib| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `attribId` | integer |  |

### SmartCardEmulation.setAttribRequested

Fired when |SCardSetAttrib| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `attribId` | integer |  |
| `data` | string |  |

### SmartCardEmulation.statusRequested

Fired when |SCardStatus| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |

### SmartCardEmulation.beginTransactionRequested

Fired when |SCardBeginTransaction| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |

### SmartCardEmulation.endTransactionRequested

Fired when |SCardEndTransaction| is called.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b
Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | string |  |
| `handle` | integer |  |
| `disposition` | [SmartCardEmulation.Disposition](#type-disposition) |  |

## Types

<a id="type-resultcode"></a>
### SmartCardEmulation.ResultCode

Indicates the PC/SC error code.

This maps to:
PC/SC Lite: https://pcsclite.apdu.fr/api/group__ErrorCodes.html
Microsoft: https://learn.microsoft.com/en-us/windows/win32/secauthn/authentication-return-values

Type: string

Allowed values: `success`, `removed-card`, `reset-card`, `unpowered-card`, `unresponsive-card`, `unsupported-card`, `reader-unavailable`, `sharing-violation`, `not-transacted`, `no-smartcard`, `proto-mismatch`, `system-cancelled`, `not-ready`, `cancelled`, `insufficient-buffer`, `invalid-handle`, `invalid-parameter`, `invalid-value`, `no-memory`, `timeout`, `unknown-reader`, `unsupported-feature`, `no-readers-available`, `service-stopped`, `no-service`, `comm-error`, `internal-error`, `server-too-busy`, `unexpected`, `shutdown`, `unknown-card`, `unknown`

<a id="type-sharemode"></a>
### SmartCardEmulation.ShareMode

Maps to the |SCARD_SHARE_*| values.

Type: string

Allowed values: `shared`, `exclusive`, `direct`

<a id="type-disposition"></a>
### SmartCardEmulation.Disposition

Indicates what the reader should do with the card.

Type: string

Allowed values: `leave-card`, `reset-card`, `unpower-card`, `eject-card`

<a id="type-connectionstate"></a>
### SmartCardEmulation.ConnectionState

Maps to |SCARD_*| connection state values.

Type: string

Allowed values: `absent`, `present`, `swallowed`, `powered`, `negotiable`, `specific`

<a id="type-readerstateflags"></a>
### SmartCardEmulation.ReaderStateFlags

Maps to the |SCARD_STATE_*| flags.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `unaware` (optional) | boolean |  |
| `ignore` (optional) | boolean |  |
| `changed` (optional) | boolean |  |
| `unknown` (optional) | boolean |  |
| `unavailable` (optional) | boolean |  |
| `empty` (optional) | boolean |  |
| `present` (optional) | boolean |  |
| `exclusive` (optional) | boolean |  |
| `inuse` (optional) | boolean |  |
| `mute` (optional) | boolean |  |
| `unpowered` (optional) | boolean |  |

<a id="type-protocolset"></a>
### SmartCardEmulation.ProtocolSet

Maps to the |SCARD_PROTOCOL_*| flags.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `t0` (optional) | boolean |  |
| `t1` (optional) | boolean |  |
| `raw` (optional) | boolean |  |

<a id="type-protocol"></a>
### SmartCardEmulation.Protocol

Maps to the |SCARD_PROTOCOL_*| values.

Type: string

Allowed values: `t0`, `t1`, `raw`

<a id="type-readerstatein"></a>
### SmartCardEmulation.ReaderStateIn

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `reader` | string |  |
| `currentState` | [SmartCardEmulation.ReaderStateFlags](#type-readerstateflags) |  |
| `currentInsertionCount` | integer |  |

<a id="type-readerstateout"></a>
### SmartCardEmulation.ReaderStateOut

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `reader` | string |  |
| `eventState` | [SmartCardEmulation.ReaderStateFlags](#type-readerstateflags) |  |
| `eventCount` | integer |  |
| `atr` | string |  |
