# GetDurableExecutionState

Service: AWS Lambda · SDK for JavaScript v3: `GetDurableExecutionStateCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-12-01/durable-executions/{DurableExecutionArn}/state` · Paginated (token `Marker` → `NextMarker`)

Retrieves the current execution state required for the replay process during [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.

The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.

## Input (`GetDurableExecutionStateRequest`)

### `DurableExecutionArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the durable execution.

### `CheckpointToken` — string · **required** · sent as query `CheckpointToken`

A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.

### `Marker` — string · sent as query `Marker`

If `NextMarker` was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.

### `MaxItems` — integer · sent as query `MaxItems` · default `0`

The maximum number of operations to return per call. You can use `Marker` to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.

## Output (`GetDurableExecutionStateResponse`)

### `Operations` — list<Operation> · **required**

An array of operations that represent the current state of the durable execution. Operations are ordered by their start sequence number in ascending order and include information needed for replay processing.

### `NextMarker` — string

If present, indicates that more operations are available. Use this value as the `Marker` parameter in a subsequent request to retrieve the next page of results.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
