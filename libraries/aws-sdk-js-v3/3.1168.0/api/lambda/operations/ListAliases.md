# ListAliases

Service: AWS Lambda · SDK for JavaScript v3: `ListAliasesCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions/{FunctionName}/aliases` · Paginated

Returns a list of [aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) for a Lambda Event Function.

## Input (`ListAliasesRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `FunctionVersion` — string · sent as query `FunctionVersion`

Specify a function version to only list aliases that invoke that version.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

Limit the number of aliases returned.

## Output (`ListAliasesResponse`)

### `NextMarker` — string

The pagination token that's included if more results are available.

### `Aliases` — list<AliasConfiguration>

A list of aliases.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To list a function's aliases

The following example returns a list of aliases for a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "Aliases": [
    {
      "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:BETA",
      "Description": "Production environment BLUE.",
      "FunctionVersion": "2",
      "Name": "BLUE",
      "RevisionId": "a410117f-xmpl-494e-8035-7e204bb7933b",
      "RoutingConfig": {
        "AdditionalVersionWeights": {
          "1": 0.7
        }
      }
    },
    {
      "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE",
      "Description": "Production environment GREEN.",
      "FunctionVersion": "1",
      "Name": "GREEN",
      "RevisionId": "21d40116-xmpl-40ba-9360-3ea284da1bb5"
    }
  ]
}
```
