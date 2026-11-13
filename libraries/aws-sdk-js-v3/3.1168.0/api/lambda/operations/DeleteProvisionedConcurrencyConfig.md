# DeleteProvisionedConcurrencyConfig

Service: AWS Lambda · SDK for JavaScript v3: `DeleteProvisionedConcurrencyConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2019-09-30/functions/{FunctionName}/provisioned-concurrency`

Deletes the provisioned concurrency configuration for a function.

## Input (`DeleteProvisionedConcurrencyConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · **required** · sent as query `Qualifier`

The version number or alias name.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete a provisioned concurrency configuration

The following example deletes the provisioned concurrency configuration for the GREEN alias of a function named my-function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "GREEN"
}
```
