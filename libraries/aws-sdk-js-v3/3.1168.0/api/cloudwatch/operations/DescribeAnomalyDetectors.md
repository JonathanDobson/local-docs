# DescribeAnomalyDetectors

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeAnomalyDetectorsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Lists the anomaly detection models that you have created in your account. For single
metric anomaly detectors, you can list all of the models in your account or filter the
results to only the models that are related to a certain namespace, metric name, or
metric dimension. For metric math anomaly detectors, you can list them by adding
`METRIC_MATH` to the `AnomalyDetectorTypes` array. This will
return all metric math anomaly detectors in your account.

## Input (`DescribeAnomalyDetectorsInput`)

### `AnomalyDetectorIds` — list<string>

Specifies the unique identifiers of the anomaly detectors to describe. You can specify
up to 50 identifiers. If you specify this parameter, you cannot also specify the
`Namespace`, `MetricName`, `Dimensions`, or
`AnomalyDetectorTypes` metric filters.

### `NextToken` — string

Use the token returned by the previous operation to request the next page of
results.

### `MaxResults` — integer

The maximum number of results to return in one operation. The maximum value that you
can specify is 100.

To retrieve the remaining results, make another call with the returned
`NextToken` value.

### `Namespace` — string

Limits the results to only the anomaly detection models that are associated with the
specified namespace.

### `MetricName` — string

Limits the results to only the anomaly detection models that are associated with the
specified metric name. If there are multiple metrics with this name in different
namespaces that have anomaly detection models, they're all returned.

### `Dimensions` — list<Dimension>

Limits the results to only the anomaly detection models that are associated with the
specified metric dimensions. If there are multiple metrics that have these dimensions
and have anomaly detection models associated, they're all returned.

### `AnomalyDetectorTypes` — list<AnomalyDetectorType (enum)>

The anomaly detector types to request when using
`DescribeAnomalyDetectorsInput`. If empty, defaults to
`SINGLE_METRIC`.

## Output (`DescribeAnomalyDetectorsOutput`)

### `AnomalyDetectors` — list<AnomalyDetector>

The list of anomaly detection models returned by the operation.

### `NextToken` — string

A token that you can use in a subsequent operation to retrieve the next set of
results.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidNextToken` — The next token specified is invalid.
- `InvalidParameterCombinationException` — Parameters were used together that cannot be used together.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
