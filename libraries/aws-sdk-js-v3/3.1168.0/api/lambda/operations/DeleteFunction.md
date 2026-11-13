# DeleteFunction

Service: AWS Lambda · SDK for JavaScript v3: `DeleteFunctionCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2015-03-31/functions/{FunctionName}`

Deletes a Lambda Event Function. To delete a specific function version, use the `Qualifier` parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for DeleteAlias.

A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting.

To delete Lambda event source mappings that invoke a function, use DeleteEventSourceMapping. For Amazon Web Services services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.

## Input (`DeleteFunctionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function or version.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:1` (with version).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version to delete. You can't delete a version that an alias references.

## Output (`DeleteFunctionResponse`)

### `StatusCode` — integer · default `0`

The HTTP status code returned by the operation.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete a version of a Lambda function

The following example deletes version 1 of a Lambda function named my-function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "1"
}
```
