# DeleteMetricStream

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteMetricStreamCommand` from `@aws-sdk/client-cloudwatch`

Permanently deletes the metric stream that you specify.

## Input (`DeleteMetricStreamInput`)

### `Name` — string · **required**

The name of the metric stream to delete.

## Output (`DeleteMetricStreamOutput`)

_None._

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
