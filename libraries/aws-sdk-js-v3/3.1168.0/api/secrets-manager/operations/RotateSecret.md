# RotateSecret

Service: AWS Secrets Manager · SDK for JavaScript v3: `RotateSecretCommand` from `@aws-sdk/client-secrets-manager`

Configures and starts the asynchronous process of rotating the secret. For information
about rotation, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
in the *Secrets Manager User Guide*. If you include the configuration
parameters, the operation sets the values for the secret and then immediately starts a
rotation. If you don't include the configuration parameters, the operation starts a
rotation with the values already stored in the secret.

When rotation is successful, the `AWSPENDING` staging label might be
attached to the same version as the `AWSCURRENT` version, or it might not be
attached to any version. If the `AWSPENDING` staging label is present but not
attached to the same version as `AWSCURRENT`, then any later invocation of
`RotateSecret` assumes that a previous rotation request is still in
progress and returns an error. When rotation is unsuccessful, the
`AWSPENDING` staging label might be attached to an empty secret version.
For more information, see [Troubleshoot
rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_rotation.html) in the *Secrets Manager User Guide*.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:RotateSecret`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html). You also
need `lambda:InvokeFunction` permissions on the rotation function. For more
information, see  [Permissions for rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-required-permissions-function.html).

## Input (`RotateSecretRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to rotate.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `ClientRequestToken` — string

A unique identifier for the new version of the secret. You only need to specify this
value if you implement your own retry logic and you want to ensure that Secrets Manager doesn't
attempt to create a secret version twice.

If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.

If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.

This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.

### `RotationLambdaARN` — string

For secrets that use a Lambda rotation function to rotate, the ARN of the Lambda
rotation function.

For secrets that use *managed rotation*, omit this field. For more
information, see [Managed
rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html) in the *Secrets Manager User Guide*.

### `RotationRules` — RotationRulesType

A structure that defines the rotation configuration for this secret.

When changing an existing rotation schedule and setting
`RotateImmediately` to `false`:

- If using `AutomaticallyAfterDays` or a
  `ScheduleExpression` with `rate()`, the previously
  scheduled rotation might still occur.
- To prevent unintended rotations, use a `ScheduleExpression`
  with `cron()` for granular control over rotation windows.

### `ExternalSecretRotationMetadata` — list<ExternalSecretRotationMetadataItem>

The metadata needed to successfully rotate a managed external secret. A list of key
value pairs in JSON format specified by the partner. For more information about the
required information, see [Using Secrets Manager managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html)

### `ExternalSecretRotationRoleArn` — string

The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held
by a third-party partner. For more information, see [Security and
permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html).

### `RotateImmediately` — boolean · default `null`

Specifies whether to rotate the secret immediately or wait until the next scheduled
rotation window. The rotation schedule is defined in RotateSecretRequest$RotationRules.

The default for `RotateImmediately` is `true`. If you don't
specify this value, Secrets Manager rotates the secret immediately.

If you set `RotateImmediately` to `false`, Secrets Manager tests
the rotation configuration by running the [`testSecret` step](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html) of the Lambda rotation function. This test
creates an `AWSPENDING` version of the secret and then removes it.

When changing an existing rotation schedule and setting `RotateImmediately`
to `false`:

- If using `AutomaticallyAfterDays` or a
  `ScheduleExpression` with `rate()`, the previously
  scheduled rotation might still occur.
- To prevent unintended rotations, use a `ScheduleExpression` with
  `cron()` for granular control over rotation windows.

Rotation is an asynchronous process. For more information, see [How rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).

## Output (`RotateSecretResponse`)

### `ARN` — string

The ARN of the secret.

### `Name` — string

The name of the secret.

### `VersionId` — string

The ID of the new version of the secret.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To configure rotation for a secret

The following example configures rotation for a secret using a cron expression. The first rotation happens immediately after the changes are stored in the secret. The rotation schedule is the first and 15th day of every month. The rotation window begins at 4:00 PM UTC and ends at 6:00 PM.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda",
  "RotationRules": {
    "ScheduleExpression": "cron(0 16 1,15 * ? *)",
    "Duration": "2h"
  }
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

### To request an immediate rotation for a secret

The following example requests an immediate invocation of the secret's Lambda rotation function. It assumes that the specified secret already has rotation configured. The rotation function runs asynchronously in the background.

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
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```
