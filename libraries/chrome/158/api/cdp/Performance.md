# Performance domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `Performance.<command>` and events arrive as `Performance.<event>`.

## Commands

### Performance.disable

Disable collecting and reporting metrics.

### Performance.enable

Enable collecting and reporting metrics.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timeDomain` (optional) | enum: `timeTicks`, `threadTicks` | Time domain to use for collecting and reporting duration metrics. |

### Performance.setTimeDomain *(experimental)* *(deprecated)*

Sets time domain to use for collecting and reporting duration metrics. Note that this must be called before enabling metrics collection. Calling this method while metrics collection is enabled returns an error.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timeDomain` | enum: `timeTicks`, `threadTicks` | Time domain |

### Performance.getMetrics

Retrieve current values of run-time metrics.

**Returns**

| Name | Type | Description |
|---|---|---|
| `metrics` | array of [Metric](#type-metric) | Current values for run-time metrics. |

## Events

### Performance.metrics

Current values of the metrics.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `metrics` | array of [Metric](#type-metric) | Current values of the metrics. |
| `title` | string | Timestamp title. |

## Types

<a id="type-metric"></a>
### Performance.Metric

Type: object

Run-time execution metric.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Metric name. |
| `value` | number | Metric value. |

