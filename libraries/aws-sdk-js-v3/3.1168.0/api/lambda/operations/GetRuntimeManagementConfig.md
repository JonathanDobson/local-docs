# GetRuntimeManagementConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetRuntimeManagementConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2021-07-20/functions/{FunctionName}/runtime-management-config`

Retrieves the runtime management configuration for a function's version. If the runtime update mode is **Manual**, this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is **Auto** or **Function update**, this includes the runtime update mode and `null` is returned for the ARN. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Input (`GetRuntimeManagementConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version of the function. This can be `$LATEST` or a published version number. If no value is specified, the configuration for the `$LATEST` version is returned.

## Output (`GetRuntimeManagementConfigResponse`)

### `UpdateRuntimeOn` — UpdateRuntimeOn (enum)

The current runtime update mode of the function.

Values: `Auto`, `Manual`, `FunctionUpdate`

### `FunctionArn` — string

The Amazon Resource Name (ARN) of your function.

### `RuntimeVersionArn` — string

The ARN of the runtime the function is configured to use. If the runtime update mode is **Manual**, the ARN is returned, otherwise `null` is returned.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
