# StopDurableExecution

Service: AWS Lambda · SDK for JavaScript v3: `StopDurableExecutionCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2025-12-01/durable-executions/{DurableExecutionArn}/stop`

Stops a running [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html). The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.

## Input (`StopDurableExecutionRequest`)

### `DurableExecutionArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the durable execution.

### `Error` — ErrorObject · sent as httpPayload

Optional error details explaining why the execution is being stopped. The combined size of all error fields is limited to 1 MB.

## Output (`StopDurableExecutionResponse`)

### `StopTimestamp` — timestamp · **required**

The timestamp when the execution was stopped (ISO 8601 format).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
