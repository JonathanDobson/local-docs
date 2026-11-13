# UpdateSecret

Service: AWS Secrets Manager · SDK for JavaScript v3: `UpdateSecretCommand` from `@aws-sdk/client-secrets-manager`

Modifies the details of a secret, including metadata and the secret value. To change
the secret value, you can also use PutSecretValue.

To change the rotation configuration of a secret, use RotateSecret
instead.

To change a secret so that it is managed by another service, you need to recreate the
secret in that service. See [Secrets Manager secrets
managed by other Amazon Web Services services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

We recommend you avoid calling `UpdateSecret` at a sustained rate of more
than once every 10 minutes. When you call `UpdateSecret` to update the secret
value, Secrets Manager creates a new version of the secret. Secrets Manager removes outdated versions when
there are more than 100, but it does not remove versions created less than 24 hours ago.
If you update the secret value more than once every 10 minutes, you create more versions
than Secrets Manager removes, and you will reach the quota for secret versions.

If you include `SecretString` or `SecretBinary` to create a new
secret version, Secrets Manager automatically moves the staging label `AWSCURRENT` to
the new version. Then it attaches the label `AWSPREVIOUS` to the version that
`AWSCURRENT` was removed from.

If you call this operation with a `ClientRequestToken` that matches an
existing version's `VersionId`, the operation results in an error. You can't
modify an existing version, you can only create a new version. To remove a version,
remove all staging labels from it. See UpdateSecretVersionStage.

Secrets Manager generates a CloudTrail log entry when you call this action.
Do not include sensitive information in request parameters except
`SecretBinary` or `SecretString` because it might be logged.
For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:UpdateSecret`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html). If you use a
customer managed key, you must also have `kms:GenerateDataKey`,
`kms:Encrypt`, and `kms:Decrypt` permissions on the key. If
you change the KMS key and you don't have `kms:Encrypt` permission to the new
key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more
information, see  [Secret encryption
and decryption](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to [Mitigate the risks of using command-line tools to store Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html).

## Input (`UpdateSecretRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `ClientRequestToken` — string

If you include `SecretString` or `SecretBinary`, then Secrets Manager
creates a new version for the secret, and this parameter specifies the unique identifier
for the new version.

If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.

If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.

This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.

### `Description` — string

The description of the secret.

### `KmsKeyId` — string

The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt new
secret versions as well as any existing versions with the staging labels
`AWSCURRENT`, `AWSPENDING`, or `AWSPREVIOUS`. If
you don't have `kms:Encrypt` permission to the new key, Secrets Manager does not
re-encrypt existing secret versions with the new key. For more information about
versions and staging labels, see [Concepts:
Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version).

A key alias is always prefixed by `alias/`, for example
`alias/aws/secretsmanager`. For more information, see [About
aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).

If you set this to an empty string, Secrets Manager uses the Amazon Web Services managed key
`aws/secretsmanager`. If this key doesn't already exist in your account,
then Secrets Manager creates it for you automatically. All users and roles in the Amazon Web Services account
automatically have access to use `aws/secretsmanager`. Creating
`aws/secretsmanager` can result in a one-time significant delay in
returning the result.

You can only use the Amazon Web Services managed key
`aws/secretsmanager` if you call this operation using credentials from
the same Amazon Web Services account that owns the secret. If the secret is in a different
account, then you must use a customer managed key and provide the ARN of that
KMS key in this field. The user making the call must have
permissions to both the secret and the KMS key in their respective
accounts.

### `SecretBinary` — blob

The binary data to encrypt and store in the new version of the secret. We recommend
that you store your binary data in a file and then pass the contents of the file as a
parameter.

Either `SecretBinary` or `SecretString` must have a value, but
not both.

You can't access this parameter in the Secrets Manager console.

Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.

### `SecretString` — string

The text data to encrypt and store in the new version of the secret. We recommend you
use a JSON structure of key/value pairs for your secret value.

Either `SecretBinary` or `SecretString` must have a value, but
not both.

Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.

### `Type` — string

The exact string that identifies the third-party partner that holds the external
secret. For more information, see [Managed external secret
partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

## Output (`UpdateSecretResponse`)

### `ARN` — string

The ARN of the secret that was updated.

### `Name` — string

The name of the secret that was updated.

### `VersionId` — string

If Secrets Manager created a new version of the secret during this operation, then
`VersionId` contains the unique identifier of the new version.

## Errors

- `DecryptionFailure` — Secrets Manager can't decrypt the protected secret text using the provided KMS key.
- `EncryptionFailure` — Secrets Manager can't encrypt the protected secret text using the provided KMS key.
- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `LimitExceededException` — The request failed because it would exceed one of the Secrets Manager quotas.
- `MalformedPolicyDocumentException` — The resource policy has syntax errors.
- `PreconditionNotMetException` — The request failed because you did not complete all the prerequisite steps.
- `ResourceExistsException` — A resource with the ID you requested already exists.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To create a new version of the encrypted secret value

The following example shows how to create a new version of the secret by updating the SecretString field. Alternatively, you can use the put-secret-value operation.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "SecretString": "{JSON STRING WITH CREDENTIALS}"
}
```

Output:

```json
{
  "ARN": "aws:arn:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE"
}
```

### To update the description of a secret

The following example shows how to modify the description of a secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "Description": "This is a new description for the secret.",
  "ClientRequestToken": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret"
}
```

### To update the KMS key associated with a secret

This example shows how to update the KMS customer managed key (CMK) used to encrypt the secret value. The KMS CMK must be in the same region as the secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret"
}
```
