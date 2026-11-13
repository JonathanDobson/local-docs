# SendDurableExecutionCallbackSuccess

Service: AWS Lambda · SDK for JavaScript v3: `SendDurableExecutionCallbackSuccessCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2025-12-01/durable-execution-callbacks/{CallbackId}/succeed`

Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation.

## Input (`SendDurableExecutionCallbackSuccessRequest`)

### `CallbackId` — string · **required** · sent as httpLabel

The unique identifier for the callback operation.

### `Result` — blob · sent as httpPayload

The result data from the successful callback operation. Maximum size is 1 MB.

## Output (`SendDurableExecutionCallbackSuccessResponse`)

_None._

## Errors

- `CallbackTimeoutException` — The callback ID token has either expired or the callback associated with the token has already been closed.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
