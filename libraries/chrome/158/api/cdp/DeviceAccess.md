# DeviceAccess domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `DeviceAccess.<command>` and events arrive as `DeviceAccess.<event>`.

## Commands

### DeviceAccess.enable

Enable events in this domain.

### DeviceAccess.disable

Disable events in this domain.

### DeviceAccess.selectPrompt

Select a device in response to a DeviceAccess.deviceRequestPrompted event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [RequestId](#type-requestid) |  |
| `deviceId` | [DeviceId](#type-deviceid) |  |

### DeviceAccess.cancelPrompt

Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [RequestId](#type-requestid) |  |

## Events

### DeviceAccess.deviceRequestPrompted

A device request opened a user prompt to select a device. Respond with the selectPrompt or cancelPrompt command.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [RequestId](#type-requestid) |  |
| `devices` | array of [PromptDevice](#type-promptdevice) |  |

## Types

<a id="type-requestid"></a>
### DeviceAccess.RequestId

Type: string

Device request id.

<a id="type-deviceid"></a>
### DeviceAccess.DeviceId

Type: string

A device id.

<a id="type-promptdevice"></a>
### DeviceAccess.PromptDevice

Type: object

Device information displayed in a user prompt to select a device.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [DeviceId](#type-deviceid) |  |
| `name` | string | Display name as it appears in a device request user prompt. |

