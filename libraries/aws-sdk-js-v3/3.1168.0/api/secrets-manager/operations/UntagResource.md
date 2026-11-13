# UntagResource

Service: AWS Secrets Manager · SDK for JavaScript v3: `UntagResourceCommand` from `@aws-sdk/client-secrets-manager`

Removes specific tags from a secret.

This operation is idempotent. If a requested tag is not attached to the secret, no
error is returned and the secret metadata is unchanged.

If you use tags as part of your security strategy, then removing a tag can change
permissions. If successfully completing this operation would result in you losing
your permissions for this secret, then the operation is blocked and returns an
Access Denied error.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:UntagResource`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`UntagResourceRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `TagKeys` — list<string> · **required**

A list of tag key names to remove from the secret. You don't specify the value. Both
the key and its associated value are removed.

This parameter requires a JSON text string argument.

For storing multiple values, we recommend that you use a JSON text
string argument and specify key/value pairs. For more information, see [Specifying parameter values for the Amazon Web Services CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html)
in the Amazon Web Services CLI User Guide.

## Output (`Unit`)

_None._

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To remove tags from a secret

The following example shows how to remove two tags from a secret's metadata. For each, both the tag and the associated value are removed. There is no output from this API. To see the result, use the DescribeSecret operation.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "TagKeys": [
    "FirstTag",
    "SecondTag"
  ]
}
```
