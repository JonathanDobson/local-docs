# PutFunctionCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutFunctionCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2020-06-30/functions/{FunctionName}/code-signing-config`

Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function.

## Input (`PutFunctionCodeSigningConfigRequest`)

### `CodeSigningConfigArn` — string · **required**

The The Amazon Resource Name (ARN) of the code signing configuration.

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Output (`PutFunctionCodeSigningConfigResponse`)

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
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
