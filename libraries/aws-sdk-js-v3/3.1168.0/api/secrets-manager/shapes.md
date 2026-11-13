# AWS Secrets Manager — data types

Structures, unions and enums used by the operations (operation inputs and outputs are on the operation pages).

## APIErrorType (structure)

The error Secrets Manager encountered while retrieving an individual secret as part of BatchGetSecretValue.

### `SecretId` — string

The ARN or name of the secret.

### `ErrorCode` — string

The error Secrets Manager encountered while retrieving an individual secret as part of BatchGetSecretValue, for example
`ResourceNotFoundException`,`InvalidParameterException`,
`InvalidRequestException`, `DecryptionFailure`, or
`AccessDeniedException`.

### `Message` — string

A message describing the error.

## CrossAccountPrimaryType (structure)

Contains information about the primary secret that a cross-account replica secret
replicates from, including its ARN and replication status. This information is only
available for cross-account replica secrets.

### `PrimarySecretARN` — string

The ARN of the primary secret replicating into this replica secret.

### `ReplicationStatus` — StatusType (enum)

The status of replication from the primary secret to this replica. The status can be:

- `InSync`: Replication to the replica secret is complete.
- `Failed`: Replication to the replica secret was unable to be completed.
- `InProgress`: Replication to the replica secret has started but is not complete.
- `Pending`: Replication has not yet started for the replica secret.
- `Detached`: Replication to the replica secret was stopped by the primary.

Values: `InSync`, `Failed`, `InProgress`, `Pending`, `Detached`

### `StatusMessage` — string

A message that describes the replication status, if Secrets Manager has more information to
provide.

## CrossAccountReplicaEntry (structure)

Information about a cross-account replica secret. This information is only
available for cross-account primary secrets.

### `ReplicaSecretARN` — string

The ARN of the replica secret.

### `ReplicationRoleARN` — string

The ARN of the IAM role that Secrets Manager assumes to replicate to this replica, if one was
specified when the replica was associated.

### `ReplicationStatus` — StatusType (enum)

The status of replication from this primary secret. The status can be:

- `InSync`: Replication from the primary secret is complete.
- `Failed`: Replication from the primary secret was unable to be completed.
- `InProgress`: Replication from the primary secret has started but is not complete.
- `Detached`: Replication from the primary secret was stopped by the replica.

Values: `InSync`, `Failed`, `InProgress`, `Pending`, `Detached`

### `StatusMessage` — string

A message that describes the replication status, if Secrets Manager has more information to
provide.

## ExternalSecretRotationMetadataItem (structure)

The metadata needed to successfully rotate a managed external secret. A list of key
value pairs in JSON format specified by the partner. For more information, see [Managed
external secret partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

### `Key` — string

The key that identifies the item.

### `Value` — string

The value of the specified item.

## Filter (structure)

Allows you to add filters when you use the search function in Secrets Manager. For more
information, see [Find secrets in
Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html).

### `Key` — FilterNameStringType (enum)

The following are keys you can use:

- **description**: Prefix match, not
  case-sensitive.
- **name**: Prefix match, case-sensitive.
- **tag-key**: Prefix match, case-sensitive.
- **tag-value**: Prefix match,
  case-sensitive.
- **primary-region**: Prefix match,
  case-sensitive.
- **owning-service**: Prefix match,
  case-sensitive.
- **all**: Breaks the filter value string into
  words and then searches all attributes for matches. Not case-sensitive.

Values: `description`, `name`, `tag-key`, `tag-value`, `primary-region`, `owning-service`, `all`

### `Values` — list<string>

The keyword to filter for.

You can prefix your search value with an exclamation mark (`!`) in order to
perform negation filters.

## FilterNameStringType (enum)

Values: `description`, `name`, `tag-key`, `tag-value`, `primary-region`, `owning-service`, `all`

## ReplicaRegionType (structure)

A custom type that specifies a `Region` and the `KmsKeyId` for a
replica secret.

### `Region` — string

A Region code. For a list of Region codes, see [Name and code of
Regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).

### `KmsKeyId` — string

The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include
this field, Secrets Manager uses `aws/secretsmanager`.

## ReplicaRestrictionType (enum)

Values: `SameOrg`, `NoRestriction`

## ReplicationStatusType (structure)

A replication object consisting of a `RegionReplicationStatus` object and
includes a Region, KMSKeyId, status, and status message.

### `Region` — string

The Region where replication occurs.

### `KmsKeyId` — string

Can be an `ARN`, `Key ID`, or `Alias`.

### `Status` — StatusType (enum)

The status can be `InProgress`, `Failed`, or
`InSync`.

Values: `InSync`, `Failed`, `InProgress`, `Pending`, `Detached`

### `StatusMessage` — string

Status message such as "*Secret with this name already exists in this
region*".

### `LastAccessedDate` — timestamp

The date that the secret was last accessed in the Region. This field is omitted if the
secret has never been retrieved in the Region.

## ResourcePolicySummary (structure)

A structure that contains details about a resource policy attached to a secret. It does
not contain the contents of the resource policy. To view the contents of the policy, use
[GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html) .

### `PolicyName` — string

The name of the resource policy.

## RotationRulesType (structure)

A structure that defines the rotation configuration for the secret.

### `AutomaticallyAfterDays` — long

The number of days between rotations of the secret. You can use this value to check
that your secret meets your compliance guidelines for how often secrets must be rotated.
If you use this field to set the rotation schedule, Secrets Manager calculates the next rotation
date based on the previous rotation. Manually updating the secret value by calling
`PutSecretValue` or `UpdateSecret` is considered a valid
rotation.

In `DescribeSecret` and `ListSecrets`, this value is calculated
from the rotation schedule after every successful rotation. In
`RotateSecret`, you can set the rotation schedule in
`RotationRules` with `AutomaticallyAfterDays` or
`ScheduleExpression`, but not both. To set a rotation schedule in hours,
use `ScheduleExpression`.

### `Duration` — string

The length of the rotation window in hours, for example `3h` for a three
hour window. Secrets Manager rotates your secret at any time during this window. The window must
not extend into the next rotation window or the next UTC day. The window starts
according to the `ScheduleExpression`. If you don't specify a
`Duration`, for a `ScheduleExpression` in hours, the window
automatically closes after one hour. For a `ScheduleExpression` in days, the
window automatically closes at the end of the UTC day. For more information, including
examples, see [Schedule
expressions in Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the *Secrets Manager Users
Guide*.

### `ScheduleExpression` — string

A `cron()` or `rate()` expression that defines the schedule for
rotating your secret. Secrets Manager rotation schedules use UTC time zone. Secrets Manager rotates your
secret any time during a rotation window.

Secrets Manager `rate()` expressions represent the interval in hours or days that you
want to rotate your secret, for example `rate(12 hours)` or `rate(10
days)`. You can rotate a secret as often as every four hours. If you use a
`rate()` expression, the rotation window starts at midnight. For a rate
in hours, the default rotation window closes after one hour. For a rate in days, the
default rotation window closes at the end of the day. You can set the
`Duration` to change the rotation window. The rotation window must not
extend into the next UTC day or into the next rotation window.

You can use a `cron()` expression to create a rotation schedule that is
more detailed than a rotation interval. For more information, including examples, see
[Schedule
expressions in Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the *Secrets Manager Users Guide*.
For a cron expression that represents a schedule in hours, the default rotation window
closes after one hour. For a cron expression that represents a schedule in days, the
default rotation window closes at the end of the day. You can set the
`Duration` to change the rotation window. The rotation window must not
extend into the next UTC day or into the next rotation window.

## SecretListEntry (structure)

A structure that contains the details about a secret. It does not include the
encrypted `SecretString` and `SecretBinary` values. To get those
values, use [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) .

### `ARN` — string

The Amazon Resource Name (ARN) of the secret.

### `Name` — string

The friendly name of the secret.

### `Type` — string

The exact string that identifies the third-party partner that holds the external
secret. For more information, see [Managed external secret
partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

### `Description` — string

The user-provided description of the secret.

### `KmsKeyId` — string

The ARN of the KMS key that Secrets Manager uses to encrypt the secret value. If the secret is
encrypted with the Amazon Web Services managed key `aws/secretsmanager`, this
field is omitted.

### `RotationEnabled` — boolean · default `null`

Indicates whether automatic, scheduled rotation is enabled for this secret.

### `RotationLambdaARN` — string

The ARN of an Amazon Web Services Lambda function invoked by Secrets Manager to rotate and expire the secret
either automatically per the schedule or manually by a call to [`RotateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html).

### `RotationRules` — RotationRulesType

A structure that defines the rotation configuration for the secret.

### `ExternalSecretRotationMetadata` — list<ExternalSecretRotationMetadataItem>

The metadata needed to successfully rotate a managed external secret. A list of key
value pairs in JSON format specified by the partner. For more information about the
required information, see [Managed external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

### `ExternalSecretRotationRoleArn` — string

The role that Secrets Manager assumes to call APIs required to perform the rotation. For more
information about the required information, see [Managed
external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

### `LastRotatedDate` — timestamp

The most recent date and time that the Secrets Manager rotation process was
successfully completed. This value is null if the secret hasn't ever rotated.

### `LastChangedDate` — timestamp

The last date and time that this secret was modified in any way.

### `LastAccessedDate` — timestamp

The date that the secret was last accessed in the Region. This field is omitted if the
secret has never been retrieved in the Region.

### `DeletedDate` — timestamp

The date and time the deletion of the secret occurred. Not present on active secrets.
The secret can be recovered until the number of days in the recovery window has passed,
as specified in the `RecoveryWindowInDays` parameter of the [`DeleteSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html) operation.

### `NextRotationDate` — timestamp

The next rotation is scheduled to occur on or before this date. If the secret isn't
configured for rotation or rotation has been disabled, Secrets Manager returns null.

### `Tags` — list<Tag>

The list of user-defined tags associated with the secret. To add tags to a secret, use
[`TagResource`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html). To remove tags, use [`UntagResource`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html).

### `SecretVersionsToStages` — map<string, list<string>>

A list of all of the currently assigned `SecretVersionStage` staging labels
and the `SecretVersionId` attached to each one. Staging labels are used to
keep track of the different versions during the rotation process.

A version that does not have any `SecretVersionStage` is considered
deprecated and subject to deletion. Such versions are not included in this
list.

### `OwningService` — string

Returns the name of the service that created the secret.

### `CreatedDate` — timestamp

The date and time when a secret was created.

### `PrimaryRegion` — string

The Region where Secrets Manager originated the secret.

## SecretValueEntry (structure)

A structure that contains the secret value and other details for a secret.

### `ARN` — string

The Amazon Resource Name (ARN) of the secret.

### `Name` — string

The friendly name of the secret.

### `VersionId` — string

The unique version identifier of this version of the secret.

### `SecretBinary` — blob

The decrypted secret value, if the secret value was originally provided as binary data
in the form of a byte array. The parameter represents the binary data as a [base64-encoded](https://tools.ietf.org/html/rfc4648#section-4)
string.

### `SecretString` — string

The decrypted secret value, if the secret value was originally provided as a string or
through the Secrets Manager console.

### `VersionStages` — list<string>

A list of all of the staging labels currently attached to this version of the
secret.

### `CreatedDate` — timestamp

The date the secret was created.

## SecretVersionsListEntry (structure)

A structure that contains information about one version of a secret.

### `VersionId` — string

The unique version identifier of this version of the secret.

### `VersionStages` — list<string>

An array of staging labels that are currently associated with this version of the
secret.

### `LastAccessedDate` — timestamp

The date that this version of the secret was last accessed. Note that the resolution
of this field is at the date level and does not include the time.

### `CreatedDate` — timestamp

The date and time this version of the secret was created.

### `KmsKeyIds` — list<string>

The KMS keys used to encrypt the secret version.

## SortByType (enum)

Values: `created-date`, `last-accessed-date`, `last-changed-date`, `name`

## SortOrderType (enum)

Values: `asc`, `desc`

## StatusType (enum)

Values: `InSync`, `Failed`, `InProgress`, `Pending`, `Detached`

## Tag (structure)

A structure that contains information about a tag.

### `Key` — string

The key identifier, or name, of the tag.

### `Value` — string

The string value associated with the key of the tag.

## ValidationErrorsEntry (structure)

Displays errors that occurred during validation of the resource policy.

### `CheckName` — string

Checks the name of the policy.

### `ErrorMessage` — string

Displays error messages if validation encounters problems during validation of the
resource policy.
