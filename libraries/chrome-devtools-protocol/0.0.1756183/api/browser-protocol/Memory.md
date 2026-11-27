# Memory domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

11 methods, 0 events, 5 types.

## Methods

### Memory.getDOMCounters

Retruns current DOM object counters.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `documents` | integer |  |
| `nodes` | integer |  |
| `jsEventListeners` | integer |  |

### Memory.getDOMCountersForLeakDetection

Retruns DOM object counters after preparing renderer for leak detection.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `counters` | array of [Memory.DOMCounter](#type-domcounter) | DOM object counters. |

### Memory.prepareForLeakDetection

Prepares for leak detection by terminating workers, stopping spellcheckers,
dropping non-essential internal caches, running garbage collections, etc.

No parameters.

### Memory.forciblyPurgeJavaScriptMemory

Simulate OomIntervention by purging V8 memory.

No parameters.

### Memory.setPressureNotificationsSuppressed

Enable/disable suppressing memory pressure notifications in all processes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `suppressed` | boolean | If true, memory pressure notifications will be suppressed. |

### Memory.simulatePressureNotification

Simulate a memory pressure notification in all processes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `level` | [Memory.PressureLevel](#type-pressurelevel) | Memory pressure level of the notification. |

### Memory.startSampling

Start collecting native memory profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `samplingInterval` (optional) | integer | Average number of bytes between samples. |
| `suppressRandomness` (optional) | boolean | Do not randomize intervals between samples. |

### Memory.stopSampling

Stop collecting native memory profile.

No parameters.

### Memory.getAllTimeSamplingProfile

Retrieve native memory allocations profile
collected since renderer process startup.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `profile` | [Memory.SamplingProfile](#type-samplingprofile) |  |

### Memory.getBrowserSamplingProfile

Retrieve native memory allocations profile
collected since browser process startup.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `profile` | [Memory.SamplingProfile](#type-samplingprofile) |  |

### Memory.getSamplingProfile

Retrieve native memory allocations profile collected since last
`startSampling` call.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `profile` | [Memory.SamplingProfile](#type-samplingprofile) |  |

## Types

<a id="type-pressurelevel"></a>
### Memory.PressureLevel

Memory pressure level.

Type: string

Allowed values: `moderate`, `critical`

<a id="type-samplingprofilenode"></a>
### Memory.SamplingProfileNode

Heap profile sample.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `size` | number | Size of the sampled allocation. |
| `total` | number | Total bytes attributed to this sample. |
| `stack` | array of string | Execution stack at the point of allocation. |

<a id="type-samplingprofile"></a>
### Memory.SamplingProfile

Array of heap profile samples.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `samples` | array of [Memory.SamplingProfileNode](#type-samplingprofilenode) |  |
| `modules` | array of [Memory.Module](#type-module) |  |

<a id="type-module"></a>
### Memory.Module

Executable module information

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name of the module. |
| `uuid` | string | UUID of the module. |
| `baseAddress` | string | Base address where the module is loaded into memory. Encoded as a decimal or hexadecimal (0x prefixed) string. |
| `size` | number | Size of the module in bytes. |

<a id="type-domcounter"></a>
### Memory.DOMCounter

DOM object counter data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Object name. Note: object names should be presumed volatile and clients should not expect the returned names to be consistent across runs. |
| `count` | integer | Object count. |
