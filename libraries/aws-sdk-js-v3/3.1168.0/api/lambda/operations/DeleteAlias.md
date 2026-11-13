# DeleteAlias

Service: AWS Lambda · SDK for JavaScript v3: `DeleteAliasCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2015-03-31/functions/{FunctionName}/aliases/{Name}`

Deletes a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).

## Input (`DeleteAliasRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Name` — string · **required** · sent as httpLabel

The name of the alias.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete a Lambda function alias

The following example deletes an alias named BLUE from a function named my-function

Input:

```json
{
  "FunctionName": "my-function",
  "Name": "BLUE"
}
```
