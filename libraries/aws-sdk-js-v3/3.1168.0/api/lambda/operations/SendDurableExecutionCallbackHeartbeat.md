# SendDurableExecutionCallbackHeartbeat

Service: AWS Lambda · SDK for JavaScript v3: `SendDurableExecutionCallbackHeartbeatCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2025-12-01/durable-execution-callbacks/{CallbackId}/heartbeat`

Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.

## Input (`SendDurableExecutionCallbackHeartbeatRequest`)

### `CallbackId` — string · **required** · sent as httpLabel

The unique identifier for the callback operation.

## Output (`SendDurableExecutionCallbackHeartbeatResponse`)

_None._

## Errors

- `CallbackTimeoutException` — The callback ID token has either expired or the callback associated with the token has already been closed.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
