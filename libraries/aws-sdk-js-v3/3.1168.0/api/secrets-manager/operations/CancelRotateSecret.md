# CancelRotateSecret

Service: AWS Secrets Manager · SDK for JavaScript v3: `CancelRotateSecretCommand` from `@aws-sdk/client-secrets-manager`

Turns off automatic rotation, and if a rotation is currently in progress, cancels the
rotation.

If you cancel a rotation in progress, it can leave the `VersionStage`
labels in an unexpected state. You might need to remove the staging label
`AWSPENDING` from the partially created version. You also need to
determine whether to roll back to the previous version of the secret by moving the
staging label `AWSCURRENT` to the version that has `AWSPENDING`.
To determine which version has a specific staging label, call DescribeSecret. Then use UpdateSecretVersionStage to change staging labels. For more information, see [How rotation
works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).

To turn on automatic rotation again, call RotateSecret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:CancelRotateSecret`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`CancelRotateSecretRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

## Output (`CancelRotateSecretResponse`)

### `ARN` — string

The ARN of the secret.

### `Name` — string

The name of the secret.

### `VersionId` — string

The unique identifier of the version of the secret created during the rotation. This
version might not be complete, and should be evaluated for possible deletion. We
recommend that you remove the `VersionStage` value `AWSPENDING`
from this version so that Secrets Manager can delete it. Failing to clean up a cancelled rotation
can block you from starting future rotations.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To cancel scheduled rotation for a secret

The following example shows how to cancel rotation for a secret. The operation sets the RotationEnabled field to false and cancels all scheduled rotations. To resume scheduled rotations, you must re-enable rotation by calling the rotate-secret operation.

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
  "Name": "Name"
}
```
