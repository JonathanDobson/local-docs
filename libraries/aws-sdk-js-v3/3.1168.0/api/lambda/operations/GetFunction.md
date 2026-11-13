# GetFunction

Service: AWS Lambda · SDK for JavaScript v3: `GetFunctionCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions/{FunctionName}`

Returns information about a Lambda Event Function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.

## Input (`GetFunctionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version or alias to get details about a published version of the function.

## Output (`GetFunctionResponse`)

### `Configuration` — FunctionConfiguration

The configuration of the function or version.

### `Code` — FunctionCodeLocation

The deployment package of the function or version.

### `Tags` — map<string, string>

The function's [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html). Lambda returns tag data only if you have explicit allow permissions for [lambda:ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html).

### `TagsError` — TagsError

An object that contains details about an error related to retrieving tags.

### `Concurrency` — Concurrency

The function's [reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a Lambda function

The following example returns code and configuration details for version 1 of a function named my-function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "1"
}
```

Output:

```json
{
  "Code": {
    "Location": "https://awslambda-us-west-2-tasks.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-function-e7d9d1ed-xmpl-4f79-904a-4b87f2681f30?versionId=sH3TQwBOaUy...",
    "RepositoryType": "S3"
  },
  "Configuration": {
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
    "LastUpdateStatus": "Successful",
    "MemorySize": 256,
    "RevisionId": "b75dcd81-xmpl-48a8-a75a-93ba8b5b9727",
    "Role": "arn:aws:iam::123456789012:role/lambda-role",
    "Runtime": "nodejs12.x",
    "State": "Active",
    "Timeout": 15,
    "TracingConfig": {
      "Mode": "Active"
    },
    "Version": "$LATEST"
  },
  "Tags": {
    "DEPARTMENT": "Assets"
  }
}
```
