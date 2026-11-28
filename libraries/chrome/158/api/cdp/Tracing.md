# Tracing domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [IO](IO.md)

Methods are called as `Tracing.<command>` and events arrive as `Tracing.<event>`.

## Commands

### Tracing.end

Stop trace events collection.

### Tracing.getCategories *(experimental)*

Gets supported tracing categories.

**Returns**

| Name | Type | Description |
|---|---|---|
| `categories` | array of string | A list of supported tracing categories. |

### Tracing.getTrackEventDescriptor *(experimental)*

Return a descriptor for all available tracing categories.

**Returns**

| Name | Type | Description |
|---|---|---|
| `descriptor` | binary | Base64-encoded serialized perfetto.protos.TrackEventDescriptor protobuf message. |

### Tracing.recordClockSyncMarker *(experimental)*

Record a clock sync marker in the trace.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `syncId` | string | The ID of this clock sync marker |

### Tracing.requestMemoryDump *(experimental)*

Request a global memory dump.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `deterministic` (optional) | boolean | Enables more deterministic results by forcing garbage collection |
| `levelOfDetail` (optional) | [MemoryDumpLevelOfDetail](#type-memorydumplevelofdetail) | Specifies level of details in memory dump. Defaults to "detailed". |

**Returns**

| Name | Type | Description |
|---|---|---|
| `dumpGuid` | string | GUID of the resulting global memory dump. |
| `success` | boolean | True iff the global memory dump succeeded. |

### Tracing.start

Start trace events collection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `categories` (optional) *(experimental)* *(deprecated)* | string | Category/tag filter |
| `options` (optional) *(experimental)* *(deprecated)* | string | Tracing options |
| `bufferUsageReportingInterval` (optional) *(experimental)* | number | If set, the agent will issue bufferUsage events at this interval, specified in milliseconds |
| `transferMode` (optional) | enum: `ReportEvents`, `ReturnAsStream` | Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to `ReportEvents`). |
| `streamFormat` (optional) | [StreamFormat](#type-streamformat) | Trace data format to use. This only applies when using `ReturnAsStream` transfer mode (defaults to `json`). |
| `streamCompression` (optional) *(experimental)* | [StreamCompression](#type-streamcompression) | Compression format to use. This only applies when using `ReturnAsStream` transfer mode (defaults to `none`) |
| `traceConfig` (optional) | [TraceConfig](#type-traceconfig) |  |
| `perfettoConfig` (optional) *(experimental)* | binary | Base64-encoded serialized perfetto.protos.TraceConfig protobuf message When specified, the parameters `categories`, `options`, `traceConfig` are ignored. |
| `tracingBackend` (optional) *(experimental)* | [TracingBackend](#type-tracingbackend) | Backend type (defaults to `auto`) |
| `screenshotMaxSize` (optional) *(experimental)* | integer | Maximum width and height (in pixels) of each captured screenshot. Only used when the `disabled-by-default-devtools.screenshot` category is enabled. Defaults to 500. The combined memory footprint of screenshots (`screenshotMaxSize` * `screenshotMaxSize` * 4 * `screenshotMaxCount`) is clamped to the existing per-session budget. |
| `screenshotMaxCount` (optional) *(experimental)* | integer | Maximum number of screenshots captured during a single tracing session. Only used when the `disabled-by-default-devtools.screenshot` category is enabled. Defaults to 450. Clamped together with `screenshotMaxSize` to stay within the per-session screenshot memory budget. |

## Events

### Tracing.bufferUsage *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `percentFull` (optional) | number | A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size. |
| `eventCount` (optional) | number | An approximate number of events in the trace log. |
| `value` (optional) | number | A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size. |

### Tracing.dataCollected *(experimental)*

Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `value` | array of object |  |

### Tracing.tracingComplete

Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dataLossOccurred` | boolean | Indicates whether some trace data is known to have been lost, e.g. because the trace ring buffer wrapped around. |
| `stream` (optional) | [IO.StreamHandle](IO.md#type-streamhandle) | A handle of the stream that holds resulting trace data. |
| `traceFormat` (optional) | [StreamFormat](#type-streamformat) | Trace data format of returned stream. |
| `streamCompression` (optional) | [StreamCompression](#type-streamcompression) | Compression format of returned stream. |

## Types

<a id="type-memorydumpconfig"></a>
### Tracing.MemoryDumpConfig *(experimental)*

Type: object

Configuration for memory dump. Used only when "memory-infra" category is enabled.

<a id="type-traceconfig"></a>
### Tracing.TraceConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `recordMode` (optional) *(experimental)* | enum: `recordUntilFull`, `recordContinuously`, `recordAsMuchAsPossible`, `echoToConsole` | Controls how the trace buffer stores data. The default is `recordUntilFull`. |
| `traceBufferSizeInKb` (optional) *(experimental)* | number | Size of the trace buffer in kilobytes. If not specified or zero is passed, a default value of 200 MB would be used. |
| `enableSampling` (optional) *(experimental)* | boolean | Turns on JavaScript stack sampling. |
| `enableSystrace` (optional) *(experimental)* | boolean | Turns on system tracing. |
| `enableArgumentFilter` (optional) *(experimental)* | boolean | Turns on argument filter. |
| `includedCategories` (optional) | array of string | Included category filters. |
| `excludedCategories` (optional) | array of string | Excluded category filters. |
| `syntheticDelays` (optional) *(experimental)* | array of string | Configuration to synthesize the delays in tracing. |
| `memoryDumpConfig` (optional) *(experimental)* | [MemoryDumpConfig](#type-memorydumpconfig) | Configuration for memory dump triggers. Used only when "memory-infra" category is enabled. |

<a id="type-streamformat"></a>
### Tracing.StreamFormat *(experimental)*

Type: string

Data format of a trace. Can be either the legacy JSON format or the protocol buffer format. Note that the JSON format will be deprecated soon.

Allowed values: `json`, `proto`

<a id="type-streamcompression"></a>
### Tracing.StreamCompression *(experimental)*

Type: string

Compression type to use for traces returned via streams.

Allowed values: `none`, `gzip`

<a id="type-memorydumplevelofdetail"></a>
### Tracing.MemoryDumpLevelOfDetail *(experimental)*

Type: string

Details exposed when memory request explicitly declared. Keep consistent with memory_dump_request_args.h and memory_instrumentation.mojom

Allowed values: `background`, `light`, `detailed`

<a id="type-tracingbackend"></a>
### Tracing.TracingBackend *(experimental)*

Type: string

Backend type to use for tracing. `chrome` uses the Chrome-integrated tracing service and is supported on all platforms. `system` is only supported on Chrome OS and uses the Perfetto system tracing service. `auto` chooses `system` when the perfettoConfig provided to Tracing.start specifies at least one non-Chrome data source; otherwise uses `chrome`.

Allowed values: `auto`, `chrome`, `system`

