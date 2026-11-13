# PutMetricStream

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutMetricStreamCommand` from `@aws-sdk/client-cloudwatch`

Creates or updates a metric stream. Metric streams can automatically stream CloudWatch
metrics to Amazon Web Services destinations, including Amazon S3, and to many third-party
solutions.

For more information, see  [Using
Metric Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html).

To create a metric stream, you must be signed in to an account that has the
`iam:PassRole` permission and either the
`CloudWatchFullAccess` policy or the
`cloudwatch:PutMetricStream` permission.

When you create or update a metric stream, you choose one of the following:

- Stream metrics from all metric namespaces in the account.
- Stream metrics from all metric namespaces in the account, except for the
  namespaces that you list in `ExcludeFilters`.
- Stream metrics from only the metric namespaces that you list in
  `IncludeFilters`.

By default, a metric stream always sends the `MAX`, `MIN`,
`SUM`, and `SAMPLECOUNT` statistics for each metric that is
streamed. You can use the `StatisticsConfigurations` parameter to have the
metric stream send additional statistics in the stream. Streaming additional statistics
incurs additional costs. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

When you use `PutMetricStream` to create a new metric stream, the stream is
created in the `running` state. If you use it to update an existing stream,
the state of the stream is not changed.

If you are using CloudWatch cross-account observability and you create a metric
stream in a monitoring account, you can choose whether to include metrics from source
accounts in the stream. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

## Input (`PutMetricStreamInput`)

### `Name` — string · **required**

If you are creating a new metric stream, this is the name for the new stream. The name
must be different than the names of other metric streams in this account and
Region.

If you are updating a metric stream, specify the name of that stream here.

Valid characters are A-Z, a-z, 0-9, "-" and "\_".

### `IncludeFilters` — list<MetricStreamFilter>

If you specify this parameter, the stream sends only the metrics from the metric
namespaces that you specify here.

You cannot include `IncludeFilters` and `ExcludeFilters` in the
same operation.

### `ExcludeFilters` — list<MetricStreamFilter>

If you specify this parameter, the stream sends metrics from all metric namespaces
except for the namespaces that you specify here.

You cannot include `ExcludeFilters` and `IncludeFilters` in the
same operation.

### `FirehoseArn` — string · **required**

The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric
stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be
in the same account as the metric stream.

### `RoleArn` — string · **required**

The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data
Firehose resources. This IAM role must already exist and must be in the same account as
the metric stream. This IAM role must include the following permissions:

- firehose:PutRecord
- firehose:PutRecordBatch

### `OutputFormat` — MetricStreamOutputFormat (enum) · **required**

The output format for the stream. Valid values are `json`,
`opentelemetry1.0`, and `opentelemetry0.7`. For more
information about metric stream output formats, see [Metric streams output formats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html).

Values: `json`, `opentelemetry0.7`, `opentelemetry1.0`

### `Tags` — list<Tag>

A list of key-value pairs to associate with the metric stream. You can associate as
many as 50 tags with a metric stream.

Tags can help you organize and categorize your resources. You can also use them to
scope user permissions by granting a user permission to access or change only resources
with certain tag values.

You can use this parameter only when you are creating a new metric stream. If you are
using this operation to update an existing metric stream, any tags you specify in this
parameter are ignored. To change the tags of an existing metric stream, use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html).

### `StatisticsConfigurations` — list<MetricStreamStatisticsConfiguration>

By default, a metric stream always sends the `MAX`, `MIN`,
`SUM`, and `SAMPLECOUNT` statistics for each metric that is
streamed. You can use this parameter to have the metric stream also send additional
statistics in the stream. This array can have up to 100 members.

For each entry in this array, you specify one or more metrics and the list of
additional statistics to stream for those metrics. The additional statistics that you
can stream depend on the stream's `OutputFormat`. If the
`OutputFormat` is `json`, you can stream any additional
statistic that is supported by CloudWatch, listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). If the `OutputFormat`
is `opentelemetry1.0` or `opentelemetry0.7`, you can stream
percentile statistics such as p95, p99.9, and so on.

### `IncludeLinkedAccountsMetrics` — boolean

If you are creating a metric stream in a monitoring account, specify `true`
to include metrics from source accounts in the metric stream.

## Output (`PutMetricStreamOutput`)

### `Arn` — string

The ARN of the metric stream.

## Errors

- `ConcurrentModificationException` — More than one process tried to modify a resource at the same time.
- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterCombinationException` — Parameters were used together that cannot be used together.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
