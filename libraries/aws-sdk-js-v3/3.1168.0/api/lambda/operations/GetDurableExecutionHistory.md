# GetDurableExecutionHistory

Service: AWS Lambda · SDK for JavaScript v3: `GetDurableExecutionHistoryCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-12-01/durable-executions/{DurableExecutionArn}/history` · Paginated (token `Marker` → `NextMarker`)

Retrieves the execution history for a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.

The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.

## Input (`GetDurableExecutionHistoryRequest`)

### `DurableExecutionArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the durable execution.

### `IncludeExecutionData` — boolean · sent as query `IncludeExecutionData`

Specifies whether to include execution data such as step results and callback payloads in the history events. Set to `true` to include data, or `false` to exclude it for a more compact response. The default is `true`.

### `MaxItems` — integer · sent as query `MaxItems` · default `0`

The maximum number of history events to return per call. You can use `Marker` to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.

### `Marker` — string · sent as query `Marker`

If `NextMarker` was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.

### `ReverseOrder` — boolean · sent as query `ReverseOrder`

When set to `true`, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).

## Output (`GetDurableExecutionHistoryResponse`)

### `Events` — list<Event> · **required**

An array of execution history events, ordered chronologically unless `ReverseOrder` is set to `true`. Each event represents a significant occurrence during the execution, such as step completion or callback resolution.

### `NextMarker` — string

If present, indicates that more history events are available. Use this value as the `Marker` parameter in a subsequent request to retrieve the next page of results.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
