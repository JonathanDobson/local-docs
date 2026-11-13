# UpdateAlias

Service: AWS Lambda · SDK for JavaScript v3: `UpdateAliasCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2015-03-31/functions/{FunctionName}/aliases/{Name}`

Updates the configuration of a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).

## Input (`UpdateAliasRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Name` — string · **required** · sent as httpLabel

The name of the alias.

### `FunctionVersion` — string

The function version that the alias invokes.

### `Description` — string

A description of the alias.

### `RoutingConfig` — AliasRoutingConfiguration

The [routing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing) of the alias.

### `RevisionId` — string

Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.

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
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To update a function alias

The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.

Input:

```json
{
  "FunctionName": "my-function",
  "FunctionVersion": "2",
  "Name": "BLUE",
  "RoutingConfig": {
    "AdditionalVersionWeights": {
      "1": 0.7
    }
  }
}
```

Output:

```json
{
  "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:BLUE",
  "Description": "Production environment BLUE.",
  "FunctionVersion": "2",
  "Name": "BLUE",
  "RevisionId": "594f41fb-xmpl-4c20-95c7-6ca5f2a92c93",
  "RoutingConfig": {
    "AdditionalVersionWeights": {
      "1": 0.7
    }
  }
}
```
