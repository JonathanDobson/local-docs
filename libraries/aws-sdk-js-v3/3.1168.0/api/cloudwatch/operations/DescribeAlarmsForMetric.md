# DescribeAlarmsForMetric

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeAlarmsForMetricCommand` from `@aws-sdk/client-cloudwatch`

Retrieves the alarms for the specified metric. To filter the results, specify a
statistic, period, or unit.

This operation retrieves only standard alarms that are based on the specified
metric. It does not return alarms based on math expressions that use the specified
metric, or composite alarms that use the specified metric.

## Input (`DescribeAlarmsForMetricInput`)

### `MetricName` — string · **required**

The name of the metric.

### `Namespace` — string · **required**

The namespace of the metric.

### `Statistic` — Statistic (enum)

The statistic for the metric, other than percentiles. For percentile statistics,
use `ExtendedStatistics`.

Values: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

### `ExtendedStatistic` — string

The percentile statistic for the metric. Specify a value between p0.0 and
p100.

### `Dimensions` — list<Dimension>

The dimensions associated with the metric. If the metric has any associated
dimensions, you must specify them in order for the call to succeed.

### `Period` — integer

The period, in seconds, over which the statistic is applied.

### `Unit` — StandardUnit (enum)

The unit for the metric.

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

## Output (`DescribeAlarmsForMetricOutput`)

### `MetricAlarms` — list<MetricAlarm>

The information for each alarm with the specified metric.
