# Tracing domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

Depends on: [IO](IO.md)

6 methods, 3 events, 6 types.

## Methods

### Tracing.end

Stop trace events collection.

No parameters.

### Tracing.getCategories

**Experimental**

Gets supported tracing categories.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `categories` | array of string | A list of supported tracing categories. |

### Tracing.getTrackEventDescriptor

**Experimental**

Return a descriptor for all available tracing categories.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `descriptor` | string | Base64-encoded serialized perfetto.protos.TrackEventDescriptor protobuf message. (Encoded as a base64 string when passed over JSON) |

### Tracing.recordClockSyncMarker

**Experimental**

Record a clock sync marker in the trace.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `syncId` | string | The ID of this clock sync marker |

### Tracing.requestMemoryDump

**Experimental**

Request a global memory dump.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `deterministic` (optional) | boolean | Enables more deterministic results by forcing garbage collection |
| `levelOfDetail` (optional) | [Tracing.MemoryDumpLevelOfDetail](#type-memorydumplevelofdetail) | Specifies level of details in memory dump. Defaults to "detailed". |

**Return object**

| Name | Type | Description |
|---|---|---|
| `dumpGuid` | string | GUID of the resulting global memory dump. |
| `success` | boolean | True iff the global memory dump succeeded. |

### Tracing.start

Start trace events collection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `categories` (optional) | string | **Experimental** · **Deprecated** Category/tag filter |
| `options` (optional) | string | **Experimental** · **Deprecated** Tracing options |
| `bufferUsageReportingInterval` (optional) | number | **Experimental** If set, the agent will issue bufferUsage events at this interval, specified in milliseconds |
| `transferMode` (optional) | string | Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to `ReportEvents`). Allowed values: `ReportEvents`, `ReturnAsStream` |
| `streamFormat` (optional) | [Tracing.StreamFormat](#type-streamformat) | Trace data format to use. This only applies when using `ReturnAsStream` transfer mode (defaults to `json`). |
| `streamCompression` (optional) | [Tracing.StreamCompression](#type-streamcompression) | **Experimental** Compression format to use. This only applies when using `ReturnAsStream` transfer mode (defaults to `none`) |
| `traceConfig` (optional) | [Tracing.TraceConfig](#type-traceconfig) |  |
| `perfettoConfig` (optional) | string | **Experimental** Base64-encoded serialized perfetto.protos.TraceConfig protobuf message When specified, the parameters `categories`, `options`, `traceConfig` are ignored. (Encoded as a base64 string when passed over JSON) |
| `tracingBackend` (optional) | [Tracing.TracingBackend](#type-tracingbackend) | **Experimental** Backend type (defaults to `auto`) |
| `screenshotMaxSize` (optional) | integer | **Experimental** Maximum width and height (in pixels) of each captured screenshot. Only used when the `disabled-by-default-devtools.screenshot` category is enabled. Defaults to 500. The combined memory footprint of screenshots (`screenshotMaxSize` * `screenshotMaxSize` * 4 * `screenshotMaxCount`) is clamped to the existing per-session budget. |
| `screenshotMaxCount` (optional) | integer | **Experimental** Maximum number of screenshots captured during a single tracing session. Only used when the `disabled-by-default-devtools.screenshot` category is enabled. Defaults to 450. Clamped together with `screenshotMaxSize` to stay within the per-session screenshot memory budget. |

## Events

### Tracing.bufferUsage

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `percentFull` (optional) | number | A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size. |
| `eventCount` (optional) | number | An approximate number of events in the trace log. |
| `value` (optional) | number | A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size. |

### Tracing.dataCollected

**Experimental**

Contains a bucket of collected trace events. When tracing is stopped collected events will be
sent as a sequence of dataCollected events followed by tracingComplete event.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `value` | array of object |  |

### Tracing.tracingComplete

Signals that tracing is stopped and there is no trace buffers pending flush, all data were
delivered via dataCollected events.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `dataLossOccurred` | boolean | Indicates whether some trace data is known to have been lost, e.g. because the trace ring buffer wrapped around. |
| `stream` (optional) | [IO.StreamHandle](IO.md#type-streamhandle) | A handle of the stream that holds resulting trace data. |
| `traceFormat` (optional) | [Tracing.StreamFormat](#type-streamformat) | Trace data format of returned stream. |
| `streamCompression` (optional) | [Tracing.StreamCompression](#type-streamcompression) | Compression format of returned stream. |

## Types

<a id="type-memorydumpconfig"></a>
### Tracing.MemoryDumpConfig

**Experimental**

Configuration for memory dump. Used only when "memory-infra" category is enabled.

Type: object

<a id="type-traceconfig"></a>
### Tracing.TraceConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `recordMode` (optional) | string | **Experimental** Controls how the trace buffer stores data. The default is `recordUntilFull`. Allowed values: `recordUntilFull`, `recordContinuously`, `recordAsMuchAsPossible`, `echoToConsole` |
| `traceBufferSizeInKb` (optional) | number | **Experimental** Size of the trace buffer in kilobytes. If not specified or zero is passed, a default value of 200 MB would be used. |
| `enableSampling` (optional) | boolean | **Experimental** Turns on JavaScript stack sampling. |
| `enableSystrace` (optional) | boolean | **Experimental** Turns on system tracing. |
| `enableArgumentFilter` (optional) | boolean | **Experimental** Turns on argument filter. |
| `includedCategories` (optional) | array of string | Included category filters. |
| `excludedCategories` (optional) | array of string | Excluded category filters. |
| `syntheticDelays` (optional) | array of string | **Experimental** Configuration to synthesize the delays in tracing. |
| `memoryDumpConfig` (optional) | [Tracing.MemoryDumpConfig](#type-memorydumpconfig) | **Experimental** Configuration for memory dump triggers. Used only when "memory-infra" category is enabled. |

<a id="type-streamformat"></a>
### Tracing.StreamFormat

**Experimental**

Data format of a trace. Can be either the legacy JSON format or the
protocol buffer format. Note that the JSON format will be deprecated soon.

Type: string

Allowed values: `json`, `proto`

<a id="type-streamcompression"></a>
### Tracing.StreamCompression

**Experimental**

Compression type to use for traces returned via streams.

Type: string

Allowed values: `none`, `gzip`

<a id="type-memorydumplevelofdetail"></a>
### Tracing.MemoryDumpLevelOfDetail

**Experimental**

Details exposed when memory request explicitly declared.
Keep consistent with memory_dump_request_args.h and
memory_instrumentation.mojom

Type: string

Allowed values: `background`, `light`, `detailed`

<a id="type-tracingbackend"></a>
### Tracing.TracingBackend

**Experimental**

Backend type to use for tracing. `chrome` uses the Chrome-integrated
tracing service and is supported on all platforms. `system` is only
supported on Chrome OS and uses the Perfetto system tracing service.
`auto` chooses `system` when the perfettoConfig provided to Tracing.start
specifies at least one non-Chrome data source; otherwise uses `chrome`.

Type: string

Allowed values: `auto`, `chrome`, `system`
