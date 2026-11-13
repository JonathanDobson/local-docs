# GetFunctionCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetFunctionCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2020-06-30/functions/{FunctionName}/code-signing-config`

Returns the code signing configuration for the specified function.

## Input (`GetFunctionCodeSigningConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Output (`GetFunctionCodeSigningConfigResponse`)

### `CodeSigningConfigArn` — string · **required**

The The Amazon Resource Name (ARN) of the code signing configuration.

### `FunctionName` — string · **required**

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Errors

- `CodeSigningConfigNotFoundException` — The specified code signing configuration does not exist.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
