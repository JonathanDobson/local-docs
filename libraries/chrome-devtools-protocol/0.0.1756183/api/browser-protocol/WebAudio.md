# WebAudio domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain allows inspection of Web Audio API.
https://webaudio.github.io/web-audio-api/

3 methods, 13 events, 13 types.

## Methods

### WebAudio.enable

Enables the WebAudio domain and starts sending context lifetime events.

No parameters.

### WebAudio.disable

Disables the WebAudio domain.

No parameters.

### WebAudio.getRealtimeData

Fetch the realtime data from the registered contexts.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `realtimeData` | [WebAudio.ContextRealtimeData](#type-contextrealtimedata) |  |

## Events

### WebAudio.contextCreated

Notifies that a new BaseAudioContext has been created.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [WebAudio.BaseAudioContext](#type-baseaudiocontext) |  |

### WebAudio.contextWillBeDestroyed

Notifies that an existing BaseAudioContext will be destroyed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

### WebAudio.contextChanged

Notifies that existing BaseAudioContext has changed some properties (id stays the same)..

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [WebAudio.BaseAudioContext](#type-baseaudiocontext) |  |

### WebAudio.audioListenerCreated

Notifies that the construction of an AudioListener has finished.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `listener` | [WebAudio.AudioListener](#type-audiolistener) |  |

### WebAudio.audioListenerWillBeDestroyed

Notifies that a new AudioListener has been created.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `listenerId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

### WebAudio.audioNodeCreated

Notifies that a new AudioNode has been created.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `node` | [WebAudio.AudioNode](#type-audionode) |  |

### WebAudio.audioNodeWillBeDestroyed

Notifies that an existing AudioNode has been destroyed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

### WebAudio.audioParamCreated

Notifies that a new AudioParam has been created.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `param` | [WebAudio.AudioParam](#type-audioparam) |  |

### WebAudio.audioParamWillBeDestroyed

Notifies that an existing AudioParam has been destroyed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `paramId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

### WebAudio.nodesConnected

Notifies that two AudioNodes are connected.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |
| `destinationInputIndex` (optional) | number |  |

### WebAudio.nodesDisconnected

Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |
| `destinationInputIndex` (optional) | number |  |

### WebAudio.nodeParamConnected

Notifies that an AudioNode is connected to an AudioParam.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |

### WebAudio.nodeParamDisconnected

Notifies that an AudioNode is disconnected to an AudioParam.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |

## Types

<a id="type-graphobjectid"></a>
### WebAudio.GraphObjectId

An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API

Type: string

<a id="type-contexttype"></a>
### WebAudio.ContextType

Enum of BaseAudioContext types

Type: string

Allowed values: `realtime`, `offline`

<a id="type-contextstate"></a>
### WebAudio.ContextState

Enum of AudioContextState from the spec

Type: string

Allowed values: `suspended`, `running`, `closed`, `interrupted`

<a id="type-nodetype"></a>
### WebAudio.NodeType

Enum of AudioNode types

Type: string

<a id="type-channelcountmode"></a>
### WebAudio.ChannelCountMode

Enum of AudioNode::ChannelCountMode from the spec

Type: string

Allowed values: `clamped-max`, `explicit`, `max`

<a id="type-channelinterpretation"></a>
### WebAudio.ChannelInterpretation

Enum of AudioNode::ChannelInterpretation from the spec

Type: string

Allowed values: `discrete`, `speakers`

<a id="type-paramtype"></a>
### WebAudio.ParamType

Enum of AudioParam types

Type: string

<a id="type-automationrate"></a>
### WebAudio.AutomationRate

Enum of AudioParam::AutomationRate from the spec

Type: string

Allowed values: `a-rate`, `k-rate`

<a id="type-contextrealtimedata"></a>
### WebAudio.ContextRealtimeData

Fields in AudioContext that change in real-time.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `currentTime` | number | The current context time in second in BaseAudioContext. |
| `renderCapacity` | number | The time spent on rendering graph divided by render quantum duration, and multiplied by 100. 100 means the audio renderer reached the full capacity and glitch may occur. |
| `callbackIntervalMean` | number | A running mean of callback interval. |
| `callbackIntervalVariance` | number | A running variance of callback interval. |

<a id="type-baseaudiocontext"></a>
### WebAudio.BaseAudioContext

Protocol object for BaseAudioContext

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `contextType` | [WebAudio.ContextType](#type-contexttype) |  |
| `contextState` | [WebAudio.ContextState](#type-contextstate) |  |
| `realtimeData` (optional) | [WebAudio.ContextRealtimeData](#type-contextrealtimedata) |  |
| `callbackBufferSize` | number | Platform-dependent callback buffer size. |
| `maxOutputChannelCount` | number | Number of output channels supported by audio hardware in use. |
| `sampleRate` | number | Context sample rate. |
| `renderQuantumSize` | number |  |

<a id="type-audiolistener"></a>
### WebAudio.AudioListener

Protocol object for AudioListener

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `listenerId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |

<a id="type-audionode"></a>
### WebAudio.AudioNode

Protocol object for AudioNode

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `nodeType` | [WebAudio.NodeType](#type-nodetype) |  |
| `numberOfInputs` | number |  |
| `numberOfOutputs` | number |  |
| `channelCount` | number |  |
| `channelCountMode` | [WebAudio.ChannelCountMode](#type-channelcountmode) |  |
| `channelInterpretation` | [WebAudio.ChannelInterpretation](#type-channelinterpretation) |  |

<a id="type-audioparam"></a>
### WebAudio.AudioParam

Protocol object for AudioParam

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `paramId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [WebAudio.GraphObjectId](#type-graphobjectid) |  |
| `paramType` | [WebAudio.ParamType](#type-paramtype) |  |
| `rate` | [WebAudio.AutomationRate](#type-automationrate) |  |
| `defaultValue` | number |  |
| `minValue` | number |  |
| `maxValue` | number |  |
