# CheckpointDurableExecution

Service: AWS Lambda · SDK for JavaScript v3: `CheckpointDurableExecutionCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2025-12-01/durable-executions/{DurableExecutionArn}/checkpoint`

Saves the progress of a [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.

Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.

## Input (`CheckpointDurableExecutionRequest`)

### `DurableExecutionArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the durable execution.

### `CheckpointToken` — string · **required**

A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.

### `Updates` — list<OperationUpdate>

An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.

### `ClientToken` — string

An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.

## Output (`CheckpointDurableExecutionResponse`)

### `CheckpointToken` — string

A new checkpoint token to use for the next checkpoint operation. This token replaces the one provided in the request and must be used for subsequent checkpoints to maintain proper ordering.

### `NewExecutionState` — CheckpointUpdatedExecutionState · **required**

Updated execution state information that includes any changes that occurred since the last checkpoint, such as completed callbacks or expired timers. This allows the SDK to update its internal state during replay.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
