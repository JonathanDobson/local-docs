# DigitalCredentials domain *(experimental)*

Copyright 2026 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain allows interacting with the Digital Credentials API for automation.

Methods are called as `DigitalCredentials.<command>` and events arrive as `DigitalCredentials.<event>`.

## Commands

### DigitalCredentials.setVirtualWalletBehavior

Sets the behavior of the virtual wallet for digital credential requests issued from this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `action` | [VirtualWalletAction](#type-virtualwalletaction) | The action of the virtual wallet. |
| `protocol` (optional) | string | The protocol identifier (e.g. "openid4vp"). Required when \|action\| is "respond", forbidden otherwise. |
| `response` (optional) | object | The response data object returned by the wallet. Required when \|action\| is "respond", forbidden otherwise. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame to scope the virtual wallet behavior to. |

## Types

<a id="type-virtualwalletaction"></a>
### DigitalCredentials.VirtualWalletAction

Type: string

The type of virtual wallet action.

Allowed values: `respond`, `decline`, `wait`, `clear`

