# GetFunctionScalingConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetFunctionScalingConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-11-30/functions/{FunctionName}/function-scaling-config`

Retrieves the scaling configuration for a Lambda Managed Instances function.

## Input (`GetFunctionScalingConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

### `Qualifier` — string · **required** · sent as query `Qualifier`

Specify a version or alias to get the scaling configuration for a published version of the function.

## Output (`GetFunctionScalingConfigResponse`)

### `FunctionArn` — string

The Amazon Resource Name (ARN) of the function.

### `AppliedFunctionScalingConfig` — FunctionScalingConfig

The scaling configuration that is currently applied to the function. This represents the actual scaling settings in effect.

### `RequestedFunctionScalingConfig` — FunctionScalingConfig

The scaling configuration that was requested for the function.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
