# ListMetricStreams

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListMetricStreamsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Returns a list of metric streams in this account.

## Input (`ListMetricStreamsInput`)

### `NextToken` — string

Include this value, if it was returned by the previous call, to get the next set of
metric streams.

### `MaxResults` — integer

The maximum number of results to return in one operation.

## Output (`ListMetricStreamsOutput`)

### `NextToken` — string

The token that marks the start of the next batch of returned results. You can use
this token in a subsequent operation to get the next batch of results.

### `Entries` — list<MetricStreamEntry>

The array of metric stream information.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidNextToken` — The next token specified is invalid.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
