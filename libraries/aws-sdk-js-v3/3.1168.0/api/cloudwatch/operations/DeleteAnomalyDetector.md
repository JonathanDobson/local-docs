# DeleteAnomalyDetector

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteAnomalyDetectorCommand` from `@aws-sdk/client-cloudwatch`

Deletes the specified anomaly detection model from your account. For more information
about how to delete an anomaly detection model, see [Deleting an anomaly detection model](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html#Delete_Anomaly_Detection_Model) in the *CloudWatch User
Guide*.

## Input (`DeleteAnomalyDetectorInput`)

### `AnomalyDetectorId` — string

Specifies the unique identifier of the anomaly detector to delete. If you specify
this parameter, you do not need to specify a metric to identify the detector.

### `Namespace` — string · **deprecated**

The namespace associated with the anomaly detection model to delete.

### `MetricName` — string · **deprecated**

The metric name associated with the anomaly detection model to delete.

### `Dimensions` — list<Dimension> · **deprecated**

The metric dimensions associated with the anomaly detection model to delete.

### `Stat` — string · **deprecated**

The statistic associated with the anomaly detection model to delete.

### `SingleMetricAnomalyDetector` — SingleMetricAnomalyDetector

A single metric anomaly detector to be deleted.

When using `SingleMetricAnomalyDetector`, you cannot include the following
parameters in the same operation:

- `Dimensions`,
- `MetricName`
- `Namespace`
- `Stat`
- the `MetricMathAnomalyDetector` parameters of
  `DeleteAnomalyDetectorInput`

Instead, specify the single metric anomaly detector attributes as part of the
`SingleMetricAnomalyDetector` property.

### `MetricMathAnomalyDetector` — MetricMathAnomalyDetector

The metric math anomaly detector to be deleted.

When using `MetricMathAnomalyDetector`, you cannot include following
parameters in the same operation:

- `Dimensions`,
- `MetricName`
- `Namespace`
- `Stat`
- the `SingleMetricAnomalyDetector` parameters of
  `DeleteAnomalyDetectorInput`

Instead, specify the metric math anomaly detector attributes as part of the
`MetricMathAnomalyDetector` property.

## Output (`DeleteAnomalyDetectorOutput`)

_None._

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterCombinationException` — Parameters were used together that cannot be used together.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
- `ResourceNotFoundException` — The named resource does not exist.
