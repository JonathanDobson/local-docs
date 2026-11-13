# AssociateCrossAccountReplica

Service: AWS Secrets Manager · SDK for JavaScript v3: `AssociateCrossAccountReplicaCommand` from `@aws-sdk/client-secrets-manager`

Links a primary secret in your account to a replica secret in a different Amazon Web Services
account and starts replication to this replica. The replica secret must already exist in the
other Amazon Web Services account. Create the replica with CreateSecret and set its
`CrossAccountPrimaryARN` field set to this primary secret's ARN.
When you call AssociateCrossAccountReplica, Secrets Manager calls
AcceptCrossAccountReplication on the replica secret on your behalf.

The primary and replica secrets must be in the same Amazon Web Services Region and partition, and
you must call this operation from the account that owns the primary secret. A primary
secret can have at most one cross-account replica. This operation is idempotent, so
you can call it again for the same replica to repair replication. If the association fails,
Secrets Manager does not modify either the primary or replica secret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:AssociateCrossAccountReplica`,
`secretsmanager:GetSecretValue` on the primary secret, and
`secretsmanager:AcceptCrossAccountReplication` on the replica secret. You
must also have `kms:Decrypt` permission for the Key Management Service
(KMS) key that encrypts the primary secret, and
`kms:Encrypt` permission for the Amazon Web Services KMS key that encrypts the replica
secret. If you supply `ReplicationRoleARN`, you also need
`iam:PassRole` for that role. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`AssociateCrossAccountReplicaRequest`)

### `SecretId` — string · **required**

The ARN or name of the primary secret in your account to replicate.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `CrossAccountReplicaARN` — string · **required**

The ARN of the replica secret in the other Amazon Web Services account. The replica secret must be
in the same Region and partition as the primary secret. Additionally, the replica account owner
must have created the replica secret as a cross-account replica of the primary secret.
For more information see CreateSecret.

### `ReplicaRestriction` — ReplicaRestrictionType (enum)

Whether the replica account must belong to the same Amazon Web Services organization as the primary
account:

- `SameOrg`, which requires the replica account to be in the same
  organization as the primary account. This is the default.
- `NoRestriction`, which allows the replica account to be in any
  organization.

Values: `SameOrg`, `NoRestriction`

### `ReplicationRoleARN` — string

The ARN of an IAM role in the primary account that Secrets Manager assumes to perform
replication. If you don't include this field, Secrets Manager replicates using the credentials
of caller who updates the primary secret. For more information, see [Cross-account replication permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cross-account-replicate-permissions.html).

## Output (`AssociateCrossAccountReplicaResponse`)

### `ARN` — string

The ARN of the primary secret.

### `CrossAccountReplicaARN` — string

The ARN of the replica secret in the other account.

### `ReplicationStatus` — StatusType (enum)

The status of replication to the replica secret. Possible values:

- `InSync`, which indicates that replication to the replica completed
  successfully and the replica is up to date.
- `Failed`, which indicates that replication to the replica did not
  succeed.
- `InProgress`, which indicates that Secrets Manager is replicating to the
  replica.
- `Pending`, which indicates that replication has not yet started.
- `Detached`, which indicates that primary secret is no longer linked to
  the replica secret.

Values: `InSync`, `Failed`, `InProgress`, `Pending`, `Detached`

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `LimitExceededException` — The request failed because it would exceed one of the Secrets Manager quotas.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To replicate a secret to another account

The following example links a primary secret to a replica secret in another AWS account and starts replication. The replica secret was previously created in the other account using CreateSecret with the CrossAccountPrimaryARN set to this primary secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3",
  "ReplicationStatus": "InProgress"
}
```
