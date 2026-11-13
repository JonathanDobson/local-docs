# GetDurableExecution

Service: AWS Lambda · SDK for JavaScript v3: `GetDurableExecutionCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-12-01/durable-executions/{DurableExecutionArn}`

Retrieves detailed information about a specific [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.

## Input (`GetDurableExecutionRequest`)

### `DurableExecutionArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the durable execution.

### `IncludeExecutionData` — boolean · sent as query `IncludeExecutionData` · default `true`

Specifies whether to include execution data such as input payload, result, and error information in the response. Set to `false` for a more compact response that includes only execution metadata. The default value is set to `true`.

## Output (`GetDurableExecutionResponse`)

### `DurableExecutionArn` — string · **required**

The Amazon Resource Name (ARN) of the durable execution.

### `DurableExecutionName` — string · **required**

The name of the durable execution. This is either the name you provided when invoking the function, or a system-generated unique identifier if no name was provided.

### `FunctionArn` — string · **required**

The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.

### `InputPayload` — string

The JSON input payload that you provided when you started the durable execution. Asynchronous invocations support up to 1 MB, and synchronous invocations support up to 6 MB.

### `Result` — string

The JSON result returned by the durable execution if it completed successfully. This field is only present when the execution status is `SUCCEEDED`. Asynchronous invocations support up to 1 MB, and synchronous invocations support up to 6 MB.

### `Error` — ErrorObject

Error information if the durable execution failed. This field is only present when the execution status is `FAILED`, `TIMED_OUT`, or `STOPPED`. The combined size of all error fields is limited to 1 MB.

### `StartTimestamp` — timestamp · **required**

The date and time when the durable execution started, in Unix timestamp format.

### `Status` — ExecutionStatus (enum) · **required**

The current status of the durable execution. Valid values are `RUNNING`, `SUCCEEDED`, `FAILED`, `TIMED_OUT`, and `STOPPED`.

Values: `RUNNING`, `SUCCEEDED`, `FAILED`, `TIMED_OUT`, `STOPPED`

### `EndTimestamp` — timestamp

The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the execution has completed (status is `SUCCEEDED`, `FAILED`, `TIMED_OUT`, or `STOPPED`).

### `Version` — string

The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the execution use the same function version.

### `TraceHeader` — TraceHeader

The trace headers associated with the durable execution.

### `ExecutionDataIncluded` — boolean

Indicates whether execution data is included in this response. Returns `false` when `IncludeExecutionData` is set to `false` in the request.

### `DurableConfig` — DurableConfig

Configuration settings for the durable execution, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
