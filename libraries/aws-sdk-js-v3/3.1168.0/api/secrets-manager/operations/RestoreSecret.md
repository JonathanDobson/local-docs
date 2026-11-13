# RestoreSecret

Service: AWS Secrets Manager · SDK for JavaScript v3: `RestoreSecretCommand` from `@aws-sdk/client-secrets-manager`

Cancels the scheduled deletion of a secret by removing the `DeletedDate`
time stamp. You can access a secret again after it has been restored.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:RestoreSecret`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`RestoreSecretRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to restore.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

## Output (`RestoreSecretResponse`)

### `ARN` — string

The ARN of the secret that was restored.

### `Name` — string

The name of the secret that was restored.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To restore a previously deleted secret

The following example shows how to restore a secret that you previously scheduled for deletion.

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
  "Name": "MyTestDatabaseSecret"
}
```
