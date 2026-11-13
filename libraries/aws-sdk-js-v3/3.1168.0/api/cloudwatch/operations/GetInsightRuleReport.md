# GetInsightRuleReport

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetInsightRuleReportCommand` from `@aws-sdk/client-cloudwatch`

This operation returns the time series data collected by a Contributor Insights rule.
The data includes the identity and number of contributors to the log group.

You can also optionally return one or more statistics about each data point in the
time series. These statistics can include the following:

- `UniqueContributors` -- the number of unique contributors for each
  data point.
- `MaxContributorValue` -- the value of the top contributor for each
  data point. The identity of the contributor might change for each data point in
  the graph.

  If this rule aggregates by COUNT, the top contributor for each data point is
  the contributor with the most occurrences in that period. If the rule aggregates
  by SUM, the top contributor is the contributor with the highest sum in the log
  field specified by the rule's `Value`, during that period.
- `SampleCount` -- the number of data points matched by the
  rule.
- `Sum` -- the sum of the values from all contributors during the
  time period represented by that data point.
- `Minimum` -- the minimum value from a single observation during the
  time period represented by that data point.
- `Maximum` -- the maximum value from a single observation during the
  time period represented by that data point.
- `Average` -- the average value from all contributors during the
  time period represented by that data point.

## Input (`GetInsightRuleReportInput`)

### `RuleName` — string · **required**

The name of the rule that you want to see data from.

### `StartTime` — timestamp · **required**

The start time of the data to use in the report. When used in a raw HTTP Query API, it
is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example,
`2019-07-01T23:59:59`.

### `EndTime` — timestamp · **required**

The end time of the data to use in the report. When used in a raw HTTP Query API, it
is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example,
`2019-07-01T23:59:59`.

### `Period` — integer · **required**

The period, in seconds, to use for the statistics in the
`InsightRuleMetricDatapoint` results.

### `MaxContributorCount` — integer

The maximum number of contributors to include in the report. The range is 1 to 100. If
you omit this, the default of 10 is used.

### `Metrics` — list<string>

Specifies which metrics to use for aggregation of contributor values for the report.
You can specify one or more of the following metrics:

- `UniqueContributors` -- the number of unique contributors for each
  data point.
- `MaxContributorValue` -- the value of the top contributor for each
  data point. The identity of the contributor might change for each data point in
  the graph.

  If this rule aggregates by COUNT, the top contributor for each data point is
  the contributor with the most occurrences in that period. If the rule aggregates
  by SUM, the top contributor is the contributor with the highest sum in the log
  field specified by the rule's `Value`, during that period.
- `SampleCount` -- the number of data points matched by the
  rule.
- `Sum` -- the sum of the values from all contributors during the
  time period represented by that data point.
- `Minimum` -- the minimum value from a single observation during the
  time period represented by that data point.
- `Maximum` -- the maximum value from a single observation during the
  time period represented by that data point.
- `Average` -- the average value from all contributors during the
  time period represented by that data point.

### `OrderBy` — string

Determines what statistic to use to rank the contributors. Valid values are
`Sum` and `Maximum`.

## Output (`GetInsightRuleReportOutput`)

### `KeyLabels` — list<string>

An array of the strings used as the keys for this rule. The keys are the dimensions
used to classify contributors. If the rule contains more than one key, then each unique
combination of values for the keys is counted as a unique contributor.

### `AggregationStatistic` — string

Specifies whether this rule aggregates contributor data by COUNT or SUM.

### `AggregateValue` — double

The sum of the values from all individual contributors that match the rule.

### `ApproximateUniqueCount` — long

An approximate count of the unique contributors found by this rule in this time
period.

### `Contributors` — list<InsightRuleContributor>

An array of the unique contributors found by this rule in this time period. If the
rule contains multiple keys, each combination of values for the keys counts as a unique
contributor.

### `MetricDatapoints` — list<InsightRuleMetricDatapoint>

A time series of metric data points that matches the time period in the rule
request.

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
- `ResourceNotFoundException` — The named resource does not exist.
