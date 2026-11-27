# WebAudio domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain allows inspection of Web Audio API. https://webaudio.github.io/web-audio-api/

Methods are called as `WebAudio.<command>` and events arrive as `WebAudio.<event>`.

## Commands

### WebAudio.enable

Enables the WebAudio domain and starts sending context lifetime events.

### WebAudio.disable

Disables the WebAudio domain.

### WebAudio.getRealtimeData

Fetch the realtime data from the registered contexts.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `realtimeData` | [ContextRealtimeData](#type-contextrealtimedata) |  |

## Events

### WebAudio.contextCreated

Notifies that a new BaseAudioContext has been created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [BaseAudioContext](#type-baseaudiocontext) |  |

### WebAudio.contextWillBeDestroyed

Notifies that an existing BaseAudioContext will be destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |

### WebAudio.contextChanged

Notifies that existing BaseAudioContext has changed some properties (id stays the same)..

**Parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [BaseAudioContext](#type-baseaudiocontext) |  |

### WebAudio.audioListenerCreated

Notifies that the construction of an AudioListener has finished.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `listener` | [AudioListener](#type-audiolistener) |  |

### WebAudio.audioListenerWillBeDestroyed

Notifies that a new AudioListener has been created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `listenerId` | [GraphObjectId](#type-graphobjectid) |  |

### WebAudio.audioNodeCreated

Notifies that a new AudioNode has been created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `node` | [AudioNode](#type-audionode) |  |

### WebAudio.audioNodeWillBeDestroyed

Notifies that an existing AudioNode has been destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [GraphObjectId](#type-graphobjectid) |  |

### WebAudio.audioParamCreated

Notifies that a new AudioParam has been created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `param` | [AudioParam](#type-audioparam) |  |

### WebAudio.audioParamWillBeDestroyed

Notifies that an existing AudioParam has been destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [GraphObjectId](#type-graphobjectid) |  |
| `paramId` | [GraphObjectId](#type-graphobjectid) |  |

### WebAudio.nodesConnected

Notifies that two AudioNodes are connected.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |
| `destinationInputIndex` (optional) | number |  |

### WebAudio.nodesDisconnected

Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |
| `destinationInputIndex` (optional) | number |  |

### WebAudio.nodeParamConnected

Notifies that an AudioNode is connected to an AudioParam.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |

### WebAudio.nodeParamDisconnected

Notifies that an AudioNode is disconnected to an AudioParam.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceId` | [GraphObjectId](#type-graphobjectid) |  |
| `destinationId` | [GraphObjectId](#type-graphobjectid) |  |
| `sourceOutputIndex` (optional) | number |  |

## Types

<a id="type-graphobjectid"></a>
### WebAudio.GraphObjectId

Type: string

An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API

<a id="type-contexttype"></a>
### WebAudio.ContextType

Type: string

Enum of BaseAudioContext types

Allowed values: `realtime`, `offline`

<a id="type-contextstate"></a>
### WebAudio.ContextState

Type: string

Enum of AudioContextState from the spec

Allowed values: `suspended`, `running`, `closed`, `interrupted`

<a id="type-nodetype"></a>
### WebAudio.NodeType

Type: string

Enum of AudioNode types

<a id="type-channelcountmode"></a>
### WebAudio.ChannelCountMode

Type: string

Enum of AudioNode::ChannelCountMode from the spec

Allowed values: `clamped-max`, `explicit`, `max`

<a id="type-channelinterpretation"></a>
### WebAudio.ChannelInterpretation

Type: string

Enum of AudioNode::ChannelInterpretation from the spec

Allowed values: `discrete`, `speakers`

<a id="type-paramtype"></a>
### WebAudio.ParamType

Type: string

Enum of AudioParam types

<a id="type-automationrate"></a>
### WebAudio.AutomationRate

Type: string

Enum of AudioParam::AutomationRate from the spec

Allowed values: `a-rate`, `k-rate`

<a id="type-contextrealtimedata"></a>
### WebAudio.ContextRealtimeData

Type: object

Fields in AudioContext that change in real-time.

**Properties**

| Name | Type | Description |
|---|---|---|
| `currentTime` | number | The current context time in second in BaseAudioContext. |
| `renderCapacity` | number | The time spent on rendering graph divided by render quantum duration, and multiplied by 100. 100 means the audio renderer reached the full capacity and glitch may occur. |
| `callbackIntervalMean` | number | A running mean of callback interval. |
| `callbackIntervalVariance` | number | A running variance of callback interval. |

<a id="type-baseaudiocontext"></a>
### WebAudio.BaseAudioContext

Type: object

Protocol object for BaseAudioContext

**Properties**

| Name | Type | Description |
|---|---|---|
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `contextType` | [ContextType](#type-contexttype) |  |
| `contextState` | [ContextState](#type-contextstate) |  |
| `realtimeData` (optional) | [ContextRealtimeData](#type-contextrealtimedata) |  |
| `callbackBufferSize` | number | Platform-dependent callback buffer size. |
| `maxOutputChannelCount` | number | Number of output channels supported by audio hardware in use. |
| `sampleRate` | number | Context sample rate. |
| `renderQuantumSize` | number |  |

<a id="type-audiolistener"></a>
### WebAudio.AudioListener

Type: object

Protocol object for AudioListener

**Properties**

| Name | Type | Description |
|---|---|---|
| `listenerId` | [GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |

<a id="type-audionode"></a>
### WebAudio.AudioNode

Type: object

Protocol object for AudioNode

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `nodeType` | [NodeType](#type-nodetype) |  |
| `numberOfInputs` | number |  |
| `numberOfOutputs` | number |  |
| `channelCount` | number |  |
| `channelCountMode` | [ChannelCountMode](#type-channelcountmode) |  |
| `channelInterpretation` | [ChannelInterpretation](#type-channelinterpretation) |  |

<a id="type-audioparam"></a>
### WebAudio.AudioParam

Type: object

Protocol object for AudioParam

**Properties**

| Name | Type | Description |
|---|---|---|
| `paramId` | [GraphObjectId](#type-graphobjectid) |  |
| `nodeId` | [GraphObjectId](#type-graphobjectid) |  |
| `contextId` | [GraphObjectId](#type-graphobjectid) |  |
| `paramType` | [ParamType](#type-paramtype) |  |
| `rate` | [AutomationRate](#type-automationrate) |  |
| `defaultValue` | number |  |
| `minValue` | number |  |
| `maxValue` | number |  |

