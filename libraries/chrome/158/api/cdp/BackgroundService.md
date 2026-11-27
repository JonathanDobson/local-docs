# BackgroundService domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Defines events for background web platform features.

Methods are called as `BackgroundService.<command>` and events arrive as `BackgroundService.<event>`.

## Commands

### BackgroundService.startObserving

Enables event updates for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [ServiceName](#type-servicename) |  |

### BackgroundService.stopObserving

Disables event updates for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [ServiceName](#type-servicename) |  |

### BackgroundService.setRecording

Set the recording state for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `shouldRecord` | boolean |  |
| `service` | [ServiceName](#type-servicename) |  |

### BackgroundService.clearEvents

Clears all stored data for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [ServiceName](#type-servicename) |  |

## Events

### BackgroundService.recordingStateChanged

Called when the recording state for the service has been updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isRecording` | boolean |  |
| `service` | [ServiceName](#type-servicename) |  |

### BackgroundService.backgroundServiceEventReceived

Called with all existing backgroundServiceEvents when enabled, and all new events afterwards if enabled and recording.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `backgroundServiceEvent` | [BackgroundServiceEvent](#type-backgroundserviceevent) |  |

## Types

<a id="type-servicename"></a>
### BackgroundService.ServiceName

Type: string

The Background Service that will be associated with the commands/events. Every Background Service operates independently, but they share the same API.

Allowed values: `backgroundFetch`, `backgroundSync`, `pushMessaging`, `notifications`, `paymentHandler`, `periodicBackgroundSync`

<a id="type-eventmetadata"></a>
### BackgroundService.EventMetadata

Type: object

A key-value pair for additional event information to pass along.

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | string |  |
| `value` | string |  |

<a id="type-backgroundserviceevent"></a>
### BackgroundService.BackgroundServiceEvent

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Timestamp of the event (in seconds). |
| `origin` | string | The origin this event belongs to. |
| `serviceWorkerRegistrationId` | [ServiceWorker.RegistrationID](ServiceWorker.md#type-registrationid) | The Service Worker ID that initiated the event. |
| `service` | [ServiceName](#type-servicename) | The Background Service this event belongs to. |
| `eventName` | string | A description of the event. |
| `instanceId` | string | An identifier that groups related events together. |
| `eventMetadata` | array of [EventMetadata](#type-eventmetadata) | A list of event-specific information. |
| `storageKey` | string | Storage key this event belongs to. |

