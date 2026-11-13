# GetPolicy

Service: AWS Lambda · SDK for JavaScript v3: `GetPolicyCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions/{FunctionName}/policy`

Returns the [resource-based IAM policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) for a function, version, or alias.

## Input (`GetPolicyRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version or alias to get the policy for that resource.

## Output (`GetPolicyResponse`)

### `Policy` — string

The resource-based policy.

### `RevisionId` — string

A unique identifier for the current revision of the policy.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To retrieve a Lambda function policy

The following example returns the resource-based policy for version 1 of a Lambda function named my-function.

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
  "Policy": "{\"Version\":\"2012-10-17\",\"Id\":\"default\",\"Statement\":[{\"Sid\":\"xaccount\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:root\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-2:123456789012:function:my-function:1\"}]}",
  "RevisionId": "4843f2f6-7c59-4fda-b484-afd0bc0e22b8"
}
```
