# GetFunctionRecursionConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetFunctionRecursionConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2024-08-31/functions/{FunctionName}/recursion-config`

Returns your function's [recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) configuration.

## Input (`GetFunctionRecursionConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name of the function.

## Output (`GetFunctionRecursionConfigResponse`)

### `RecursiveLoop` — RecursiveLoop (enum)

If your function's recursive loop detection configuration is `Allow`, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop.

If your function's recursive loop detection configuration is `Terminate`, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.

By default, Lambda sets your function's configuration to `Terminate`. You can update this configuration using the PutFunctionRecursionConfig action.

Values: `Allow`, `Terminate`

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
