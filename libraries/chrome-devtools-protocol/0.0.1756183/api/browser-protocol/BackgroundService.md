# BackgroundService domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Defines events for background web platform features.

4 methods, 2 events, 3 types.

## Methods

### BackgroundService.startObserving

Enables event updates for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [BackgroundService.ServiceName](#type-servicename) |  |

### BackgroundService.stopObserving

Disables event updates for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [BackgroundService.ServiceName](#type-servicename) |  |

### BackgroundService.setRecording

Set the recording state for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `shouldRecord` | boolean |  |
| `service` | [BackgroundService.ServiceName](#type-servicename) |  |

### BackgroundService.clearEvents

Clears all stored data for the service.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `service` | [BackgroundService.ServiceName](#type-servicename) |  |

## Events

### BackgroundService.recordingStateChanged

Called when the recording state for the service has been updated.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `isRecording` | boolean |  |
| `service` | [BackgroundService.ServiceName](#type-servicename) |  |

### BackgroundService.backgroundServiceEventReceived

Called with all existing backgroundServiceEvents when enabled, and all new
events afterwards if enabled and recording.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `backgroundServiceEvent` | [BackgroundService.BackgroundServiceEvent](#type-backgroundserviceevent) |  |

## Types

<a id="type-servicename"></a>
### BackgroundService.ServiceName

The Background Service that will be associated with the commands/events.
Every Background Service operates independently, but they share the same
API.

Type: string

Allowed values: `backgroundFetch`, `backgroundSync`, `pushMessaging`, `notifications`, `paymentHandler`, `periodicBackgroundSync`

<a id="type-eventmetadata"></a>
### BackgroundService.EventMetadata

A key-value pair for additional event information to pass along.

Type: object

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
| `service` | [BackgroundService.ServiceName](#type-servicename) | The Background Service this event belongs to. |
| `eventName` | string | A description of the event. |
| `instanceId` | string | An identifier that groups related events together. |
| `eventMetadata` | array of [BackgroundService.EventMetadata](#type-eventmetadata) | A list of event-specific information. |
| `storageKey` | string | Storage key this event belongs to. |
