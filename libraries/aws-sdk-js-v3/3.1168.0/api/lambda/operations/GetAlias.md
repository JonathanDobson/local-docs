# GetAlias

Service: AWS Lambda · SDK for JavaScript v3: `GetAliasCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions/{FunctionName}/aliases/{Name}`

Returns details about a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).

## Input (`GetAliasRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Name` — string · **required** · sent as httpLabel

The name of the alias.

## Output (`AliasConfiguration`)

### `AliasArn` — string

The Amazon Resource Name (ARN) of the alias.

### `Name` — string

The name of the alias.

### `FunctionVersion` — string

The function version that the alias invokes.

### `Description` — string

A description of the alias.

### `RoutingConfig` — AliasRoutingConfiguration

The [routing configuration](https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html) of the alias.

### `RevisionId` — string

A unique identifier that changes when you update the alias.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a Lambda function alias

The following example returns details about an alias named BLUE for a function named my-function

Input:

```json
{
  "FunctionName": "my-function",
  "Name": "BLUE"
}
```

Output:

```json
{
  "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:BLUE",
  "Description": "Production environment BLUE.",
  "FunctionVersion": "3",
  "Name": "BLUE",
  "RevisionId": "594f41fb-xmpl-4c20-95c7-6ca5f2a92c93"
}
```
