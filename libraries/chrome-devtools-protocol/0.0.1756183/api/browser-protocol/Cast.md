# Cast domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

A domain for interacting with Cast, Presentation API, and Remote Playback API
functionalities.

6 methods, 2 events, 1 types.

## Methods

### Cast.enable

Starts observing for sinks that can be used for tab mirroring, and if set,
sinks compatible with |presentationUrl| as well. When sinks are found, a
|sinksUpdated| event is fired.
Also starts observing for issue messages. When an issue is added or removed,
an |issueUpdated| event is fired.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `presentationUrl` (optional) | string |  |

### Cast.disable

Stops observing for sinks and issues.

No parameters.

### Cast.setSinkToUse

Sets a sink to be used when the web page requests the browser to choose a
sink via Presentation API, Remote Playback API, or Cast SDK.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sinkName` | string |  |

### Cast.startDesktopMirroring

Starts mirroring the desktop to the sink.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sinkName` | string |  |

### Cast.startTabMirroring

Starts mirroring the tab to the sink.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sinkName` | string |  |

### Cast.stopCasting

Stops the active Cast session on the sink.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sinkName` | string |  |

## Events

### Cast.sinksUpdated

This is fired whenever the list of available sinks changes. A sink is a
device or a software surface that you can cast to.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `sinks` | array of [Cast.Sink](#type-sink) |  |

### Cast.issueUpdated

This is fired whenever the outstanding issue/error message changes.
|issueMessage| is empty if there is no issue.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `issueMessage` | string |  |

## Types

<a id="type-sink"></a>
### Cast.Sink

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `id` | string |  |
| `session` (optional) | string | Text describing the current session. Present only if there is an active session on the sink. |
