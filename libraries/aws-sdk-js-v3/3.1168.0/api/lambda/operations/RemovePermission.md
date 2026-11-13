# RemovePermission

Service: AWS Lambda · SDK for JavaScript v3: `RemovePermissionCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2015-03-31/functions/{FunctionName}/policy/{StatementId}`

Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of GetPolicy.

## Input (`RemovePermissionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `StatementId` — string · **required** · sent as httpLabel

Statement ID of the permission to remove.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version or alias to remove permissions from a published version of the function.

### `RevisionId` — string · sent as query `RevisionId`

Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `PublicPolicyException` — The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To remove a Lambda function's permissions

The following example removes a permissions statement named xaccount from the PROD alias of a function named my-function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "PROD",
  "StatementId": "xaccount"
}
```
