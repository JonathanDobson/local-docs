# Profiler domain

Depends on: [Runtime](Runtime.md), [Debugger](Debugger.md)

Methods are called as `Profiler.<command>` and events arrive as `Profiler.<event>`.

## Commands

### Profiler.disable

### Profiler.enable

### Profiler.getBestEffortCoverage

Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [ScriptCoverage](#type-scriptcoverage) | Coverage data for the current isolate. |

### Profiler.setSamplingInterval

Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `interval` | integer | New sampling interval in microseconds. |

### Profiler.start

### Profiler.startPreciseCoverage

Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callCount` (optional) | boolean | Collect accurate call counts beyond simple 'covered' or 'not covered'. |
| `detailed` (optional) | boolean | Collect block-based coverage. |
| `allowTriggeredUpdates` (optional) | boolean | Allow the backend to send updates on its own initiative |

**Returns**

| Name | Type | Description |
|---|---|---|
| `timestamp` | number | Monotonically increasing time (in seconds) when the coverage update was taken in the backend. |

### Profiler.stop

**Returns**

| Name | Type | Description |
|---|---|---|
| `profile` | [Profile](#type-profile) | Recorded profile. |

### Profiler.stopPreciseCoverage

Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code.

### Profiler.takePreciseCoverage

Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [ScriptCoverage](#type-scriptcoverage) | Coverage data for the current isolate. |
| `timestamp` | number | Monotonically increasing time (in seconds) when the coverage update was taken in the backend. |

## Events

### Profiler.consoleProfileFinished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string |  |
| `location` | [Debugger.Location](Debugger.md#type-location) | Location of console.profileEnd(). |
| `profile` | [Profile](#type-profile) |  |
| `title` (optional) | string | Profile title passed as an argument to console.profile(). |

### Profiler.consoleProfileStarted

Sent when new profile recording is started using console.profile() call.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string |  |
| `location` | [Debugger.Location](Debugger.md#type-location) | Location of console.profile(). |
| `title` (optional) | string | Profile title passed as an argument to console.profile(). |

### Profiler.preciseCoverageDeltaUpdate *(experimental)*

Reports coverage delta since the last poll (either from an event like this, or from `takePreciseCoverage` for the current isolate. May only be sent if precise code coverage has been started. This event can be trigged by the embedder to, for example, trigger collection of coverage data immediately at a certain point in time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timestamp` | number | Monotonically increasing time (in seconds) when the coverage update was taken in the backend. |
| `occasion` | string | Identifier for distinguishing coverage events. |
| `result` | array of [ScriptCoverage](#type-scriptcoverage) | Coverage data for the current isolate. |

## Types

<a id="type-profilenode"></a>
### Profiler.ProfileNode

Type: object

Profile node. Holds callsite information, execution statistics and child nodes.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | integer | Unique id of the node. |
| `callFrame` | [Runtime.CallFrame](Runtime.md#type-callframe) | Function location. |
| `hitCount` (optional) | integer | Number of samples where this node was on top of the call stack. |
| `children` (optional) | array of integer | Child node ids. |
| `deoptReason` (optional) | string | The reason of being not optimized. The function may be deoptimized or marked as don't optimize. |
| `positionTicks` (optional) | array of [PositionTickInfo](#type-positiontickinfo) | An array of source position ticks. |

<a id="type-profile"></a>
### Profiler.Profile

Type: object

Profile.

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [ProfileNode](#type-profilenode) | The list of profile nodes. First item is the root node. |
| `startTime` | number | Profiling start timestamp in microseconds. |
| `endTime` | number | Profiling end timestamp in microseconds. |
| `samples` (optional) | array of integer | Ids of samples top nodes. |
| `timeDeltas` (optional) | array of integer | Time intervals between adjacent samples in microseconds. The first delta is relative to the profile startTime. |

<a id="type-positiontickinfo"></a>
### Profiler.PositionTickInfo

Type: object

Specifies a number of samples attributed to a certain source position.

**Properties**

| Name | Type | Description |
|---|---|---|
| `line` | integer | Source line number (1-based). |
| `ticks` | integer | Number of samples attributed to the source line. |

<a id="type-coveragerange"></a>
### Profiler.CoverageRange

Type: object

Coverage data for a source range.

**Properties**

| Name | Type | Description |
|---|---|---|
| `startOffset` | integer | JavaScript script source offset for the range start. |
| `endOffset` | integer | JavaScript script source offset for the range end. |
| `count` | integer | Collected execution count of the source range. |

<a id="type-functioncoverage"></a>
### Profiler.FunctionCoverage

Type: object

Coverage data for a JavaScript function.

**Properties**

| Name | Type | Description |
|---|---|---|
| `functionName` | string | JavaScript function name. |
| `ranges` | array of [CoverageRange](#type-coveragerange) | Source ranges inside the function with coverage data. |
| `isBlockCoverage` | boolean | Whether coverage data for this function has block granularity. |

<a id="type-scriptcoverage"></a>
### Profiler.ScriptCoverage

Type: object

Coverage data for a JavaScript script.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | JavaScript script id. |
| `url` | string | JavaScript script name or url. |
| `functions` | array of [FunctionCoverage](#type-functioncoverage) | Functions contained in the script that has coverage data. |

