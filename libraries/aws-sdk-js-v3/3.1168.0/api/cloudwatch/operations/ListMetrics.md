# ListMetrics

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListMetricsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

List the specified metrics. You can use the returned metrics with [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) to get statistical data.

Up to 500 results are returned for any one call. To retrieve additional results,
use the returned token with subsequent calls.

After you create a metric, allow up to 15 minutes for the metric to appear. To see
metric statistics sooner, use [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

If you are using CloudWatch cross-account observability, you can use this
operation in a monitoring account and view metrics from the linked source accounts. For
more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

`ListMetrics` doesn't return information about metrics if those metrics
haven't reported data in the past two weeks. To retrieve those metrics, use [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

## Input (`ListMetricsInput`)

### `Namespace` — string

The metric namespace to filter against. Only the namespace that matches exactly
will be returned.

### `MetricName` — string

The name of the metric to filter against. Only the metrics with names that match
exactly will be returned.

### `Dimensions` — list<DimensionFilter>

The dimensions to filter against. Only the dimension with names that match exactly
will be returned. If you specify one dimension name and a metric has that dimension and
also other dimensions, it will be returned.

### `NextToken` — string

The token returned by a previous call to indicate that there is more data
available.

### `RecentlyActive` — RecentlyActive (enum)

To filter the results to show only metrics that have had data points published in the
past three hours, specify this parameter with a value of `PT3H`. This is the
only valid value for this parameter.

The results that are returned are an approximation of the value you specify. There is
a low probability that the returned results include metrics with last published data as
much as 50 minutes more than the specified time interval.

Values: `PT3H`

### `IncludeLinkedAccounts` — boolean

If you are using this operation in a monitoring account, specify `true` to
include metrics from source accounts in the returned data.

The default is `false`.

### `OwningAccount` — string

When you use this operation in a monitoring account, use this field to return metrics
only from one source account. To do so, specify that source account ID in this field,
and also specify `true` for `IncludeLinkedAccounts`.

## Output (`ListMetricsOutput`)

### `Metrics` — list<Metric>

The metrics that match your request.

### `NextToken` — string

The token that marks the start of the next batch of returned results.

### `OwningAccounts` — list<string>

If you are using this operation in a monitoring account, this array contains the
account IDs of the source accounts where the metrics in the returned data are
from.

This field is a 1:1 mapping between each metric that is returned and the ID of the
owning account.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
