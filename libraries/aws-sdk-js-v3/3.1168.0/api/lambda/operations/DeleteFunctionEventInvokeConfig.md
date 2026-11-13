# DeleteFunctionEventInvokeConfig

Service: AWS Lambda · SDK for JavaScript v3: `DeleteFunctionEventInvokeConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2019-09-25/functions/{FunctionName}/event-invoke-config`

Deletes the configuration for asynchronous invocation for a function, version, or alias.

To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig.

## Input (`DeleteFunctionEventInvokeConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** - `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** - `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

A version number or alias name.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete an asynchronous invocation configuration

The following example deletes the asynchronous invocation configuration for the GREEN alias of a function named my-function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "GREEN"
}
```
