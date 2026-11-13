# PutRuntimeManagementConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutRuntimeManagementConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2021-07-20/functions/{FunctionName}/runtime-management-config`

Sets the runtime management configuration for a function's version. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Input (`PutRuntimeManagementConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version of the function. This can be `$LATEST` or a published version number. If no value is specified, the configuration for the `$LATEST` version is returned.

### `UpdateRuntimeOn` — UpdateRuntimeOn (enum) · **required**

Specify the runtime update mode.

- **Auto (default)** - Automatically update to the most recent and secure runtime version using a [Two-phase runtime version rollout](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase). This is the best choice for most customers to ensure they always benefit from runtime updates.
- **Function update** - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.
- **Manual** - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see [Roll back a runtime version](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback).

Values: `Auto`, `Manual`, `FunctionUpdate`

### `RuntimeVersionArn` — string

The ARN of the runtime version you want the function to use.

This is only required if you're using the **Manual** runtime update mode.

## Output (`PutRuntimeManagementConfigResponse`)

### `UpdateRuntimeOn` — UpdateRuntimeOn (enum) · **required**

The runtime update mode.

Values: `Auto`, `Manual`, `FunctionUpdate`

### `FunctionArn` — string · **required**

The ARN of the function

### `RuntimeVersionArn` — string

The ARN of the runtime the function is configured to use. If the runtime update mode is **manual**, the ARN is returned, otherwise `null` is returned.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
