# RemoveRegionsFromReplication

Service: AWS Secrets Manager · SDK for JavaScript v3: `RemoveRegionsFromReplicationCommand` from `@aws-sdk/client-secrets-manager`

For a secret that is replicated to other Regions, deletes the secret replicas from the
Regions you specify.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:RemoveRegionsFromReplication`.
For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`RemoveRegionsFromReplicationRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

### `RemoveReplicaRegions` — list<string> · **required**

The Regions of the replicas to remove.

## Output (`RemoveRegionsFromReplicationResponse`)

### `ARN` — string

The ARN of the primary secret.

### `ReplicationStatus` — list<ReplicationStatusType>

The status of replicas for this secret after you remove Regions.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.
