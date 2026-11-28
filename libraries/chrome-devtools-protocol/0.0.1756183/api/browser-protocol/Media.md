# Media domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain allows detailed inspection of media elements.

2 methods, 5 events, 8 types.

## Methods

### Media.enable

Enables the Media domain

No parameters.

### Media.disable

Disables the Media domain.

No parameters.

## Events

### Media.playerPropertiesChanged

This can be called multiple times, and can be used to set / override /
remove player properties. A null propValue indicates removal.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `playerId` | [Media.PlayerId](#type-playerid) |  |
| `properties` | array of [Media.PlayerProperty](#type-playerproperty) |  |

### Media.playerEventsAdded

Send events as a list, allowing them to be batched on the browser for less
congestion. If batched, events must ALWAYS be in chronological order.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `playerId` | [Media.PlayerId](#type-playerid) |  |
| `events` | array of [Media.PlayerEvent](#type-playerevent) |  |

### Media.playerMessagesLogged

Send a list of any messages that need to be delivered.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `playerId` | [Media.PlayerId](#type-playerid) |  |
| `messages` | array of [Media.PlayerMessage](#type-playermessage) |  |

### Media.playerErrorsRaised

Send a list of any errors that need to be delivered.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `playerId` | [Media.PlayerId](#type-playerid) |  |
| `errors` | array of [Media.PlayerError](#type-playererror) |  |

### Media.playerCreated

Called whenever a player is created, or when a new agent joins and receives
a list of active players. If an agent is restored, it will receive one
event for each active player.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `player` | [Media.Player](#type-player) |  |

## Types

<a id="type-playerid"></a>
### Media.PlayerId

Players will get an ID that is unique within the agent context.

Type: string

<a id="type-timestamp"></a>
### Media.Timestamp

Type: number

<a id="type-playermessage"></a>
### Media.PlayerMessage

Have one type per entry in MediaLogRecord::Type
Corresponds to kMessage

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `level` | string | Keep in sync with MediaLogMessageLevel We are currently keeping the message level 'error' separate from the PlayerError type because right now they represent different things, this one being a DVLOG(ERROR) style log message that gets printed based on what log level is selected in the UI, and the other is a representation of a media::PipelineStatus object. Soon however we're going to be moving away from using PipelineStatus for errors and introducing a new error type which should hopefully let us integrate the error log level into the PlayerError type. Allowed values: `error`, `warning`, `info`, `debug` |
| `message` | string |  |

<a id="type-playerproperty"></a>
### Media.PlayerProperty

Corresponds to kMediaPropertyChange

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `value` | string |  |

<a id="type-playerevent"></a>
### Media.PlayerEvent

Corresponds to kMediaEventTriggered

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Media.Timestamp](#type-timestamp) |  |
| `value` | string |  |

<a id="type-playererrorsourcelocation"></a>
### Media.PlayerErrorSourceLocation

Represents logged source line numbers reported in an error.
NOTE: file and line are from chromium c++ implementation code, not js.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `file` | string |  |
| `line` | integer |  |

<a id="type-playererror"></a>
### Media.PlayerError

Corresponds to kMediaError

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `errorType` | string |  |
| `code` | integer | Code is the numeric enum entry for a specific set of error codes, such as PipelineStatusCodes in media/base/pipeline_status.h |
| `stack` | array of [Media.PlayerErrorSourceLocation](#type-playererrorsourcelocation) | A trace of where this error was caused / where it passed through. |
| `cause` | array of [Media.PlayerError](#type-playererror) | Errors potentially have a root cause error, ie, a DecoderError might be caused by an WindowsError |
| `data` | object | Extra data attached to an error, such as an HRESULT, Video Codec, etc. |

<a id="type-player"></a>
### Media.Player

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `playerId` | [Media.PlayerId](#type-playerid) |  |
| `domNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |
