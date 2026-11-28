# DeviceAccess domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

4 methods, 1 events, 3 types.

## Methods

### DeviceAccess.enable

Enable events in this domain.

No parameters.

### DeviceAccess.disable

Disable events in this domain.

No parameters.

### DeviceAccess.selectPrompt

Select a device in response to a DeviceAccess.deviceRequestPrompted event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [DeviceAccess.RequestId](#type-requestid) |  |
| `deviceId` | [DeviceAccess.DeviceId](#type-deviceid) |  |

### DeviceAccess.cancelPrompt

Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [DeviceAccess.RequestId](#type-requestid) |  |

## Events

### DeviceAccess.deviceRequestPrompted

A device request opened a user prompt to select a device. Respond with the
selectPrompt or cancelPrompt command.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [DeviceAccess.RequestId](#type-requestid) |  |
| `devices` | array of [DeviceAccess.PromptDevice](#type-promptdevice) |  |

## Types

<a id="type-requestid"></a>
### DeviceAccess.RequestId

Device request id.

Type: string

<a id="type-deviceid"></a>
### DeviceAccess.DeviceId

A device id.

Type: string

<a id="type-promptdevice"></a>
### DeviceAccess.PromptDevice

Device information displayed in a user prompt to select a device.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [DeviceAccess.DeviceId](#type-deviceid) |  |
| `name` | string | Display name as it appears in a device request user prompt. |
