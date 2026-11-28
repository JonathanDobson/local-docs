# Memory domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `Memory.<command>` and events arrive as `Memory.<event>`.

## Commands

### Memory.getDOMCounters

Retruns current DOM object counters.

**Returns**

| Name | Type | Description |
|---|---|---|
| `documents` | integer |  |
| `nodes` | integer |  |
| `jsEventListeners` | integer |  |

### Memory.getDOMCountersForLeakDetection

Retruns DOM object counters after preparing renderer for leak detection.

**Returns**

| Name | Type | Description |
|---|---|---|
| `counters` | array of [DOMCounter](#type-domcounter) | DOM object counters. |

### Memory.prepareForLeakDetection

Prepares for leak detection by terminating workers, stopping spellcheckers, dropping non-essential internal caches, running garbage collections, etc.

### Memory.forciblyPurgeJavaScriptMemory

Simulate OomIntervention by purging V8 memory.

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
| `level` | [PressureLevel](#type-pressurelevel) | Memory pressure level of the notification. |

### Memory.startSampling

Start collecting native memory profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `samplingInterval` (optional) | integer | Average number of bytes between samples. |
| `suppressRandomness` (optional) | boolean | Do not randomize intervals between samples. |

### Memory.stopSampling

Stop collecting native memory profile.

### Memory.getAllTimeSamplingProfile

Retrieve native memory allocations profile collected since renderer process startup.

**Returns**

| Name | Type | Description |
|---|---|---|
| `profile` | [SamplingProfile](#type-samplingprofile) |  |

### Memory.getBrowserSamplingProfile

Retrieve native memory allocations profile collected since browser process startup.

**Returns**

| Name | Type | Description |
|---|---|---|
| `profile` | [SamplingProfile](#type-samplingprofile) |  |

### Memory.getSamplingProfile

Retrieve native memory allocations profile collected since last `startSampling` call.

**Returns**

| Name | Type | Description |
|---|---|---|
| `profile` | [SamplingProfile](#type-samplingprofile) |  |

## Types

<a id="type-pressurelevel"></a>
### Memory.PressureLevel

Type: string

Memory pressure level.

Allowed values: `moderate`, `critical`

<a id="type-samplingprofilenode"></a>
### Memory.SamplingProfileNode

Type: object

Heap profile sample.

**Properties**

| Name | Type | Description |
|---|---|---|
| `size` | number | Size of the sampled allocation. |
| `total` | number | Total bytes attributed to this sample. |
| `stack` | array of string | Execution stack at the point of allocation. |

<a id="type-samplingprofile"></a>
### Memory.SamplingProfile

Type: object

Array of heap profile samples.

**Properties**

| Name | Type | Description |
|---|---|---|
| `samples` | array of [SamplingProfileNode](#type-samplingprofilenode) |  |
| `modules` | array of [Module](#type-module) |  |

<a id="type-module"></a>
### Memory.Module

Type: object

Executable module information

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name of the module. |
| `uuid` | string | UUID of the module. |
| `baseAddress` | string | Base address where the module is loaded into memory. Encoded as a decimal or hexadecimal (0x prefixed) string. |
| `size` | number | Size of the module in bytes. |

<a id="type-domcounter"></a>
### Memory.DOMCounter

Type: object

DOM object counter data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Object name. Note: object names should be presumed volatile and clients should not expect the returned names to be consistent across runs. |
| `count` | integer | Object count. |

