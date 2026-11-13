# ListVersionsByFunction

Service: AWS Lambda · SDK for JavaScript v3: `ListVersionsByFunctionCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions/{FunctionName}/versions` · Paginated (token `Marker` → `NextMarker`)

Returns a list of [versions](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) of a Lambda Event Function, with the version-specific configuration of each. Lambda returns up to 50 versions per call.

## Input (`ListVersionsByFunctionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Partial ARN** - `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of versions to return. Note that `ListVersionsByFunction` returns a maximum of 50 items in each response, even if you set the number higher.

## Output (`ListVersionsByFunctionResponse`)

### `NextMarker` — string

The pagination token that's included if more results are available.

### `Versions` — list<FunctionConfiguration>

A list of Lambda function versions.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To list versions of a function

The following example returns a list of versions of a function named my-function

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "Versions": [
    {
      "CodeSha256": "YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=",
      "CodeSize": 5797206,
      "Description": "Process image objects from Amazon S3.",
      "DurableConfig": {
        "ExecutionTimeout": 31622400,
        "RetentionPeriodInDays": 30
      },
      "Environment": {
        "Variables": {
          "BUCKET": "my-bucket-1xpuxmplzrlbh",
          "PREFIX": "inbound"
        }
      },
      "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
      "FunctionName": "my-function",
      "Handler": "index.handler",
      "KMSKeyArn": "arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966",
      "LastModified": "2020-04-10T19:06:32.563+0000",
      "MemorySize": 256,
      "RevisionId": "850ca006-2d98-4ff4-86db-8766e9d32fe9",
      "Role": "arn:aws:iam::123456789012:role/lambda-role",
      "Runtime": "nodejs12.x",
      "Timeout": 15,
      "TracingConfig": {
        "Mode": "Active"
      },
      "Version": "$LATEST"
    },
    {
      "CodeSha256": "YFgDgEKG3ugvF1+pX64gV6tu9qNuIYNUdgJm8nCxsm4=",
      "CodeSize": 5797206,
      "Description": "Process image objects from Amazon S3.",
      "DurableConfig": {
        "ExecutionTimeout": 31622400,
        "RetentionPeriodInDays": 30
      },
      "Environment": {
        "Variables": {
          "BUCKET": "my-bucket-1xpuxmplzrlbh",
          "PREFIX": "inbound"
        }
      },
      "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
      "FunctionName": "my-function",
      "Handler": "index.handler",
      "KMSKeyArn": "arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966",
      "LastModified": "2020-04-10T19:06:32.563+0000",
      "MemorySize": 256,
      "RevisionId": "b75dcd81-xmpl-48a8-a75a-93ba8b5b9727",
      "Role": "arn:aws:iam::123456789012:role/lambda-role",
      "Runtime": "nodejs12.x",
      "Timeout": 5,
      "TracingConfig": {
        "Mode": "Active"
      },
      "Version": "1"
    }
  ]
}
```
