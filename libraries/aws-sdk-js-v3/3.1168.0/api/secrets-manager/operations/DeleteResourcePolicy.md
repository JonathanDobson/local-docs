# DeleteResourcePolicy

Service: AWS Secrets Manager · SDK for JavaScript v3: `DeleteResourcePolicyCommand` from `@aws-sdk/client-secrets-manager`

Deletes the resource-based permission policy attached to the secret. To attach a
policy to a secret, use PutResourcePolicy.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:DeleteResourcePolicy`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`DeleteResourcePolicyRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to delete the attached resource-based policy for.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `PolicyName` — string

The name of the resource policy to delete. If you don't specify this field, Secrets Manager uses
`default`. You can only delete the `default` policy; if you
specify any other name, the operation returns an
`InvalidParameterException`.

## Output (`DeleteResourcePolicyResponse`)

### `ARN` — string

The ARN of the secret that the resource-based policy was deleted for.

### `Name` — string

The name of the secret that the resource-based policy was deleted for.

### `PolicyName` — string

The name of the deleted resource policy. If you didn't specify `PolicyName` in the
request, this is `default`.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To delete the resource-based policy attached to a secret

The following example shows how to delete the resource-based policy that is attached to a secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "PolicyName": "default"
}
```
