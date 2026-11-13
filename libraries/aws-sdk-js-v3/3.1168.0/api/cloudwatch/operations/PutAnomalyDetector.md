# PutAnomalyDetector

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutAnomalyDetectorCommand` from `@aws-sdk/client-cloudwatch`

Creates an anomaly detection model for a CloudWatch metric. You can use the model to
display a band of expected normal values when the metric is graphed.

If you have enabled unified cross-account observability, and this account is a
monitoring account, the metric can be in the same account or a source account. You can
specify the account ID in the object you specify in the
`SingleMetricAnomalyDetector` parameter.

For more information, see [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html).

## Input (`PutAnomalyDetectorInput`)

### `Namespace` — string · **deprecated**

The namespace of the metric to create the anomaly detection model for.

### `MetricName` — string · **deprecated**

The name of the metric to create the anomaly detection model for.

### `Dimensions` — list<Dimension> · **deprecated**

The metric dimensions to create the anomaly detection model for.

### `Stat` — string · **deprecated**

The statistic to use for the metric and the anomaly detection model.

### `Configuration` — AnomalyDetectorConfiguration

The configuration specifies details about how the anomaly detection model is to be
trained, including time ranges to exclude when training and updating the model. You can
specify as many as 10 time ranges.

The configuration can also include the time zone to use for the metric.

### `MetricCharacteristics` — MetricCharacteristics

Use this object to include parameters to provide information about your metric to
CloudWatch to help it build more accurate anomaly detection models.
Currently, it includes the `PeriodicSpikes` parameter.

### `SingleMetricAnomalyDetector` — SingleMetricAnomalyDetector

A single metric anomaly detector to be created.

When using `SingleMetricAnomalyDetector`, you cannot include the following
parameters in the same operation:

- `Dimensions`
- `MetricName`
- `Namespace`
- `Stat`
- the `MetricMathAnomalyDetector` parameters of
  `PutAnomalyDetectorInput`

Instead, specify the single metric anomaly detector attributes as part of the property
`SingleMetricAnomalyDetector`.

### `MetricMathAnomalyDetector` — MetricMathAnomalyDetector

The metric math anomaly detector to be created.

When using `MetricMathAnomalyDetector`, you cannot include the following
parameters in the same operation:

- `Dimensions`
- `MetricName`
- `Namespace`
- `Stat`
- the `SingleMetricAnomalyDetector` parameters of
  `PutAnomalyDetectorInput`

Instead, specify the metric math anomaly detector attributes as part of the property
`MetricMathAnomalyDetector`.

## Output (`PutAnomalyDetectorOutput`)

### `AnomalyDetectorId` — string

The unique identifier of the anomaly detector that you created or updated.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterCombinationException` — Parameters were used together that cannot be used together.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `LimitExceededException` — The operation exceeded one or more limits.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
