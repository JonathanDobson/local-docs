# DeleteFunctionConcurrency

Service: AWS Lambda · SDK for JavaScript v3: `DeleteFunctionConcurrencyCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2017-10-31/functions/{FunctionName}/concurrency`

Removes a concurrent execution limit from a Lambda Event Function.

## Input (`DeleteFunctionConcurrencyRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To remove the reserved concurrent execution limit from a function

The following example deletes the reserved concurrent execution limit from a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```
