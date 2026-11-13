# DisassociateCrossAccountReplica

Service: AWS Secrets Manager · SDK for JavaScript v3: `DisassociateCrossAccountReplicaCommand` from `@aws-sdk/client-secrets-manager`

Removes the link between a primary secret in your account and a cross-account replica
secret, and stops replication to the replica secret. Call this operation on the primary secret.
This action removes the replica association created by AssociateCrossAccountReplica.

Disassociating the replica from the primary does not delete the replica secret or
convert the replica secret to a standalone secret. The replica secret remains in the other
account and its replication status changes to `Detached`. Secrets Manager no longer sends updates
from the primary secret to the replica secret after disassociation. To convert a detached
replica into a standalone secret, call
StopReplicationToReplica on the replica secret.

You must disassociate a cross-account replica before you call DeleteSecret for the primary secret. The DeleteSecret
call fails if any replicas are still associated with the primary secret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:DisassociateCrossAccountReplica`.
For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`DisassociateCrossAccountReplicaRequest`)

### `SecretId` — string · **required**

The ARN or name of the primary secret in your account.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `CrossAccountReplicaARN` — string · **required**

The ARN of the cross-account replica secret to unlink from the primary secret.

## Output (`DisassociateCrossAccountReplicaResponse`)

### `ARN` — string

The ARN of the primary secret.

### `CrossAccountReplicaARN` — string

The ARN of the replica secret that was unlinked from the primary secret.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To stop replicating a secret to another account from the primary account

The following example, called from the primary account, removes the link between a primary secret and its cross-account replica and stops replication. The replica secret remains in the other account, now with a replication status of Detached.

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
  "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3"
}
```
