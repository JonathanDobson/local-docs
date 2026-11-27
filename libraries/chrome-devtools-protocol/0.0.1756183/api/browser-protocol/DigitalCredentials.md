# DigitalCredentials domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain allows interacting with the Digital Credentials API for automation.

1 methods, 0 events, 1 types.

## Methods

### DigitalCredentials.setVirtualWalletBehavior

Sets the behavior of the virtual wallet for digital credential requests
issued from this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `action` | [DigitalCredentials.VirtualWalletAction](#type-virtualwalletaction) | The action of the virtual wallet. |
| `protocol` (optional) | string | The protocol identifier (e.g. "openid4vp"). Required when \|action\| is "respond", forbidden otherwise. |
| `response` (optional) | object | The response data object returned by the wallet. Required when \|action\| is "respond", forbidden otherwise. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame to scope the virtual wallet behavior to. |

## Types

<a id="type-virtualwalletaction"></a>
### DigitalCredentials.VirtualWalletAction

The type of virtual wallet action.

Type: string

Allowed values: `respond`, `decline`, `wait`, `clear`
