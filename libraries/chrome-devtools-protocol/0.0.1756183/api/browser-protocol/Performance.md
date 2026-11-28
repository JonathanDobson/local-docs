# Performance domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

4 methods, 1 events, 1 types.

## Methods

### Performance.disable

Disable collecting and reporting metrics.

No parameters.

### Performance.enable

Enable collecting and reporting metrics.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timeDomain` (optional) | string | Time domain to use for collecting and reporting duration metrics. Allowed values: `timeTicks`, `threadTicks` |

### Performance.setTimeDomain

**Experimental** · **Deprecated**

Sets time domain to use for collecting and reporting duration metrics.
Note that this must be called before enabling metrics collection. Calling
this method while metrics collection is enabled returns an error.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timeDomain` | string | Time domain Allowed values: `timeTicks`, `threadTicks` |

### Performance.getMetrics

Retrieve current values of run-time metrics.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `metrics` | array of [Performance.Metric](#type-metric) | Current values for run-time metrics. |

## Events

### Performance.metrics

Current values of the metrics.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `metrics` | array of [Performance.Metric](#type-metric) | Current values of the metrics. |
| `title` | string | Timestamp title. |

## Types

<a id="type-metric"></a>
### Performance.Metric

Run-time execution metric.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Metric name. |
| `value` | number | Metric value. |
