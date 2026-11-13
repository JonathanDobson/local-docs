# PutFunctionScalingConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutFunctionScalingConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2025-11-30/functions/{FunctionName}/function-scaling-config`

Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.

## Input (`PutFunctionScalingConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

### `Qualifier` — string · **required** · sent as query `Qualifier`

Specify a version or alias to set the scaling configuration for a published version of the function.

### `FunctionScalingConfig` — FunctionScalingConfig

The scaling configuration to apply to the function, including minimum and maximum execution environment limits.

## Output (`PutFunctionScalingConfigResponse`)

### `FunctionState` — State (enum)

The current state of the function after applying the scaling configuration.

Values: `Pending`, `Active`, `Inactive`, `Failed`, `Deactivating`, `Deactivated`, `ActiveNonInvocable`, `Deleting`

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
