# DescribeSecret

Service: AWS Secrets Manager · SDK for JavaScript v3: `DescribeSecretCommand` from `@aws-sdk/client-secrets-manager`

Retrieves the details of a secret. It does not include the encrypted secret value.
Secrets Manager only returns fields that have a value in the response.

The `VersionIdsToStages` field in the response includes every version ID
that has a staging label attached, even if that version doesn't contain a secret
value. In contrast, `ListSecretVersionIds` only returns versions that
contain a secret value. To check whether a secret version contains a value, call
GetSecretValue.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:DescribeSecret`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`DescribeSecretRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

## Output (`DescribeSecretResponse`)

### `ARN` — string

The ARN of the secret.

### `Name` — string

The name of the secret.

### `Type` — string

The exact string that identifies the partner that holds the external secret. For more
information, see [Using Secrets Manager managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html).

### `Description` — string

The description of the secret.

### `KmsKeyId` — string

The key ID or alias ARN of the KMS key that Secrets Manager uses to encrypt the secret value.
If the secret is encrypted with the Amazon Web Services managed key
`aws/secretsmanager`, this field is omitted. Secrets created using the
console use an KMS key ID.

### `RotationEnabled` — boolean · default `null`

Specifies whether automatic rotation is turned on for this secret. If the secret has
never been configured for rotation, Secrets Manager returns null.

To turn on rotation, use RotateSecret. To turn off rotation, use
CancelRotateSecret.

### `RotationLambdaARN` — string

The ARN of the Lambda function that Secrets Manager invokes to rotate the secret.

### `RotationRules` — RotationRulesType

The rotation schedule and Lambda function for this secret. If the secret previously had
rotation turned on, but it is now turned off, this field shows the previous rotation
schedule and rotation function. If the secret never had rotation turned on, this field
is omitted.

### `ExternalSecretRotationMetadata` — list<ExternalSecretRotationMetadataItem>

The metadata needed to successfully rotate a managed external secret. A list of key
value pairs in JSON format specified by the partner. For more information about the
required information, see [Managed external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

### `ExternalSecretRotationRoleArn` — string

The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held
by a third-party partner. For more information, see [Security and
permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html).

### `LastRotatedDate` — timestamp

The last date and time that Secrets Manager rotated the secret. If the secret isn't configured
for rotation or rotation has been disabled, Secrets Manager returns null.

### `LastChangedDate` — timestamp

The last date and time that this secret was modified in any way.

### `LastAccessedDate` — timestamp

The date that the secret was last accessed in the Region. This field is omitted if the
secret has never been retrieved in the Region.

### `DeletedDate` — timestamp

The date the secret is scheduled for deletion. If it is not scheduled for deletion,
this field is omitted. When you delete a secret, Secrets Manager requires a recovery window of at
least 7 days before deleting the secret. Some time after the deleted date, Secrets Manager deletes
the secret, including all of its versions.

If a secret is scheduled for deletion, then its details, including the encrypted
secret value, is not accessible. To cancel a scheduled deletion and restore access to
the secret, use RestoreSecret.

### `NextRotationDate` — timestamp

The next rotation is scheduled to occur on or before this date. If the secret isn't
configured for rotation or rotation has been disabled, Secrets Manager returns null. If rotation
fails, Secrets Manager retries the entire rotation process multiple times. If rotation
is unsuccessful, this date may be in the past.

This date represents the latest date that rotation will occur, but it is not an
approximate rotation date. In some cases, for example if you turn off automatic rotation
and then turn it back on, the next rotation may occur much sooner than this date.

### `Tags` — list<Tag>

The list of tags attached to the secret. To add tags to a secret, use TagResource. To remove tags, use UntagResource.

### `VersionIdsToStages` — map<string, list<string>>

A list of the versions of the secret that have staging labels attached. Versions that
don't have staging labels are considered deprecated and Secrets Manager can delete them.

Secrets Manager uses staging labels to indicate the status of a secret version during rotation.
The three staging labels for rotation are:

- `AWSCURRENT`, which indicates the current version of the
  secret.
- `AWSPENDING`, which indicates the version of the secret that
  contains new secret information that will become the next current version when
  rotation finishes.

  During rotation, Secrets Manager creates an `AWSPENDING` version ID before
  creating the new secret version. To check if a secret version exists, call GetSecretValue.
- `AWSPREVIOUS`, which indicates the previous current version of the
  secret. You can use this as the *last known good*
  version.

For more information about rotation and staging labels, see [How rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).

### `OwningService` — string

The ID of the service that created this secret. For more information, see [Secrets managed by
other Amazon Web Services services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

### `CreatedDate` — timestamp

The date the secret was created.

### `PrimaryRegion` — string

The Region the secret is in. If a secret is replicated to other Regions, the replicas
are listed in `ReplicationStatus`.

### `ReplicationStatus` — list<ReplicationStatusType>

A list of the replicas of this secret and their status:

- `Failed`, which indicates that the replica was not created.
- `InProgress`, which indicates that Secrets Manager is in the process of
  creating the replica.
- `InSync`, which indicates that the replica was created.

### `CrossAccountPrimary` — CrossAccountPrimaryType

Information about the primary secret in the other Amazon Web Services account that this
cross-account replica secret replicates from, including the primary secret ARN and the
replication status. This field is omitted if the secret is not a cross-account
replica.

### `CrossAccountReplicas` — list<CrossAccountReplicaEntry>

A list of this secret's cross-account replica secrets and their replication status, if
this secret is the primary for cross-account replication. This field is omitted if the
secret has no cross-account replicas.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.
