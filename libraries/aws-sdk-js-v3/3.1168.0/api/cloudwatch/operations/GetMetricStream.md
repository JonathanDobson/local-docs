# GetMetricStream

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetMetricStreamCommand` from `@aws-sdk/client-cloudwatch`

Returns information about the metric stream that you specify.

## Input (`GetMetricStreamInput`)

### `Name` — string · **required**

The name of the metric stream to retrieve information about.

## Output (`GetMetricStreamOutput`)

### `Arn` — string

The ARN of the metric stream.

### `Name` — string

The name of the metric stream.

### `IncludeFilters` — list<MetricStreamFilter>

If this array of metric namespaces is present, then these namespaces are the only
metric namespaces that are streamed by this metric stream.

### `ExcludeFilters` — list<MetricStreamFilter>

If this array of metric namespaces is present, then these namespaces are the only
metric namespaces that are not streamed by this metric stream. In this case, all other
metric namespaces in the account are streamed by this metric stream.

### `FirehoseArn` — string

The ARN of the Amazon Kinesis Data Firehose delivery stream that is used by this
metric stream.

### `RoleArn` — string

The ARN of the IAM role that is used by this metric stream.

### `State` — string

The state of the metric stream. The possible values are `running` and
`stopped`.

### `CreationDate` — timestamp

The date that the metric stream was created.

### `LastUpdateDate` — timestamp

The date of the most recent update to the metric stream's configuration.

### `OutputFormat` — MetricStreamOutputFormat (enum)

The output format for the stream. Valid values are `json`,
`opentelemetry1.0`, and `opentelemetry0.7`. For more
information about metric stream output formats, see [Metric streams output formats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html).

Values: `json`, `opentelemetry0.7`, `opentelemetry1.0`

### `StatisticsConfigurations` — list<MetricStreamStatisticsConfiguration>

Each entry in this array displays information about one or more metrics that include
additional statistics in the metric stream. For more information about the additional
statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).

### `IncludeLinkedAccountsMetrics` — boolean

If this is `true` and this metric stream is in a monitoring account, then
the stream includes metrics from source accounts that the monitoring account is linked
to.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterCombinationException` — Parameters were used together that cannot be used together.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
- `ResourceNotFoundException` — The named resource does not exist.
