# StopMetricStreams

Service: Amazon CloudWatch · SDK for JavaScript v3: `StopMetricStreamsCommand` from `@aws-sdk/client-cloudwatch`

Stops the streaming of metrics for one or more of your metric streams.

## Input (`StopMetricStreamsInput`)

### `Names` — list<string> · **required**

The array of the names of metric streams to stop streaming.

This is an "all or nothing" operation. If you do not have permission to access all of
the metric streams that you list here, then none of the streams that you list in the
operation will stop streaming.

## Output (`StopMetricStreamsOutput`)

_None._

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
