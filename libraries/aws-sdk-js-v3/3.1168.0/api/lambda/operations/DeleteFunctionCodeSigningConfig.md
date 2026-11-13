# DeleteFunctionCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `DeleteFunctionCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2020-06-30/functions/{FunctionName}/code-signing-config`

Removes the code signing configuration from the function.

## Input (`DeleteFunctionCodeSigningConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Output (`Unit`)

_None._

## Errors

- `CodeSigningConfigNotFoundException` — The specified code signing configuration does not exist.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
