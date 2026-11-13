# CreateAlias

Service: AWS Lambda · SDK for JavaScript v3: `CreateAliasCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2015-03-31/functions/{FunctionName}/aliases`

Creates an [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) for a Lambda Event Function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version.

You can also map an alias to split invocation requests between two versions. Use the `RoutingConfig` parameter to specify a second version and the percentage of invocation requests that it receives.

## Input (`CreateAliasRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Name` — string · **required**

The name of the alias.

### `FunctionVersion` — string · **required**

The function version that the alias invokes.

### `Description` — string

A description of the alias.

### `RoutingConfig` — AliasRoutingConfiguration

The [routing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing) of the alias.

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

- `AliasLimitExceededException` — Lambda couldn't create the alias because your Amazon Web Services account has exceeded the maximum number of aliases allowed per Lambda function.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To create an alias for a Lambda function

The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.

Input:

```json
{
  "Description": "alias for live version of function",
  "FunctionName": "my-function",
  "FunctionVersion": "1",
  "Name": "LIVE"
}
```

Output:

```json
{
  "AliasArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:LIVE",
  "Description": "alias for live version of function",
  "FunctionVersion": "1",
  "Name": "LIVE",
  "RevisionId": "873282ed-xmpl-4dc8-a069-d0c647e470c6"
}
```
