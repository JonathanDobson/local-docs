# StopReplicationToReplica

Service: AWS Secrets Manager · SDK for JavaScript v3: `StopReplicationToReplicaCommand` from `@aws-sdk/client-secrets-manager`

Removes the link between a replica secret and its primary secret, and stops
replication to the replica. You call this operation from the replica account or Region.
Depending on the type of replica, the behavior is:

- **Cross-Region replica**: promotes the replica to
  a standalone primary secret in the replica Region.
- **Cross-account replica**: promotes the replica
  in your account to a standalone secret and stops replication from its primary
  secret in the other account. Secrets Manager updates the primary secret's replication status
  to `Detached` for this replica.

To stop cross-account replication from the primary account instead, use DisassociateCrossAccountReplica.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:StopReplicationToReplica`. For cross-account
replica secrets, you must also have `secretsmanager:DeleteResourcePolicy`
permissions. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`StopReplicationToReplicaRequest`)

### `SecretId` — string · **required**

The ARN or name of the replica secret.

For a cross-region replica, the replica ARN is the same as the original primary secret
ARN except that the Region is changed to the replica Region. For a cross-account
replica, this is the ARN or name of the replica secret in your account.

## Output (`StopReplicationToReplicaResponse`)

### `ARN` — string

The ARN of the promoted secret. For a cross-region replica, this ARN is the same as the
original primary secret's ARN except that the Region is changed. For a cross-account
replica, this is the ARN of the promoted secret in your account.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To stop cross-account replication from the replica account

The following example, called from the replica account, unlinks a cross-account replica secret from its primary secret in another account and stops replication. The secret remains in the replica account as a standalone secret.

Input:

```json
{
  "SecretId": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3"
}
```
