# HeapProfiler domain

Chrome DevTools Protocol, JavaScript / V8 inspector protocol (protocol 1.3).

**Experimental**

Depends on: [Runtime](Runtime.md)

12 methods, 5 events, 4 types.

## Methods

### HeapProfiler.addInspectedHeapObject

Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `heapObjectId` | [HeapProfiler.HeapSnapshotObjectId](#type-heapsnapshotobjectid) | Heap snapshot object id to be accessible by means of $x command line API. |

### HeapProfiler.collectGarbage

No parameters.

### HeapProfiler.disable

No parameters.

### HeapProfiler.enable

No parameters.

### HeapProfiler.getHeapObjectId

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | Identifier of the object to get heap object id for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `heapSnapshotObjectId` | [HeapProfiler.HeapSnapshotObjectId](#type-heapsnapshotobjectid) | Id of the heap snapshot object corresponding to the passed remote object id. |

### HeapProfiler.getObjectByHeapObjectId

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [HeapProfiler.HeapSnapshotObjectId](#type-heapsnapshotobjectid) |  |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Evaluation result. |

### HeapProfiler.getSamplingProfile

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `profile` | [HeapProfiler.SamplingHeapProfile](#type-samplingheapprofile) | Return the sampling profile being collected. |

### HeapProfiler.startSampling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `samplingInterval` (optional) | number | Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes. |
| `stackDepth` (optional) | number | Maximum stack depth. The default value is 128. |
| `includeObjectsCollectedByMajorGC` (optional) | boolean | By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by major GC, which will show which functions cause large temporary memory usage or long GC pauses. |
| `includeObjectsCollectedByMinorGC` (optional) | boolean | By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by minor GC, which is useful when tuning a latency-sensitive application for minimal GC activity. |

### HeapProfiler.startTrackingHeapObjects

**Parameters**

| Name | Type | Description |
|---|---|---|
| `trackAllocations` (optional) | boolean |  |

### HeapProfiler.stopSampling

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `profile` | [HeapProfiler.SamplingHeapProfile](#type-samplingheapprofile) | Recorded sampling heap profile. |

### HeapProfiler.stopTrackingHeapObjects

**Parameters**

| Name | Type | Description |
|---|---|---|
| `reportProgress` (optional) | boolean | If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped. |
| `treatGlobalObjectsAsRoots` (optional) | boolean | **Deprecated** Deprecated in favor of `exposeInternals`. |
| `captureNumericValue` (optional) | boolean | If true, numerical values are included in the snapshot |
| `exposeInternals` (optional) | boolean | **Experimental** If true, exposes internals of the snapshot. |

### HeapProfiler.takeHeapSnapshot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `reportProgress` (optional) | boolean | If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken. |
| `treatGlobalObjectsAsRoots` (optional) | boolean | **Deprecated** If true, a raw snapshot without artificial roots will be generated. Deprecated in favor of `exposeInternals`. |
| `captureNumericValue` (optional) | boolean | If true, numerical values are included in the snapshot |
| `exposeInternals` (optional) | boolean | **Experimental** If true, exposes internals of the snapshot. |

## Events

### HeapProfiler.addHeapSnapshotChunk

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `chunk` | string |  |

### HeapProfiler.heapStatsUpdate

If heap objects tracking has been started then backend may send update for one or more fragments

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `statsUpdate` | array of integer | An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment. |

### HeapProfiler.lastSeenObjectId

If heap objects tracking has been started then backend regularly sends a current value for last
seen object id and corresponding timestamp. If the were changes in the heap since last event
then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `lastSeenObjectId` | integer |  |
| `timestamp` | number |  |

### HeapProfiler.reportHeapSnapshotProgress

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `done` | integer |  |
| `total` | integer |  |
| `finished` (optional) | boolean |  |

### HeapProfiler.resetProfiles

## Types

<a id="type-heapsnapshotobjectid"></a>
### HeapProfiler.HeapSnapshotObjectId

Heap snapshot object id.

Type: string

<a id="type-samplingheapprofilenode"></a>
### HeapProfiler.SamplingHeapProfileNode

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `callFrame` | [Runtime.CallFrame](Runtime.md#type-callframe) | Function location. |
| `selfSize` | number | Allocations size in bytes for the node excluding children. |
| `id` | integer | Node id. Ids are unique across all profiles collected between startSampling and stopSampling. |
| `children` | array of [HeapProfiler.SamplingHeapProfileNode](#type-samplingheapprofilenode) | Child nodes. |

<a id="type-samplingheapprofilesample"></a>
### HeapProfiler.SamplingHeapProfileSample

A single sample from a sampling profile.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `size` | number | Allocation size in bytes attributed to the sample. |
| `nodeId` | integer | Id of the corresponding profile tree node. |
| `ordinal` | number | Time-ordered sample ordinal number. It is unique across all profiles retrieved between startSampling and stopSampling. |

<a id="type-samplingheapprofile"></a>
### HeapProfiler.SamplingHeapProfile

Sampling profile.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `head` | [HeapProfiler.SamplingHeapProfileNode](#type-samplingheapprofilenode) |  |
| `samples` | array of [HeapProfiler.SamplingHeapProfileSample](#type-samplingheapprofilesample) |  |
