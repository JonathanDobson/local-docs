# ReplicateSecretToRegions

Service: AWS Secrets Manager · SDK for JavaScript v3: `ReplicateSecretToRegionsCommand` from `@aws-sdk/client-secrets-manager`

Replicates the secret to a new Regions. See [Multi-Region secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:ReplicateSecretToRegions`. If the primary
secret is encrypted with a KMS key other than `aws/secretsmanager`, you also
need `kms:Decrypt` permission to the key. To encrypt the replicated secret
with a KMS key other than `aws/secretsmanager`, you need
`kms:GenerateDataKey` and `kms:Encrypt` to the key.
For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`ReplicateSecretToRegionsRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to replicate.

### `AddReplicaRegions` — list<ReplicaRegionType> · **required**

A list of Regions in which to replicate the secret.

### `ForceOverwriteReplicaSecret` — boolean · default `false`

Specifies whether to overwrite a secret with the same name in the destination Region.
By default, secrets aren't overwritten.

## Output (`ReplicateSecretToRegionsResponse`)

### `ARN` — string

The ARN of the primary secret.

### `ReplicationStatus` — list<ReplicationStatusType>

The status of replication.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### Example

The following example replicates a secret to eu-west-3. The replica is encrypted with the AWS managed key aws/secretsmanager.

Input:

```json
{
  "SecretId": "MyTestSecret",
  "AddReplicaRegions": [
    {
      "Region": "eu-west-3"
    }
  ],
  "ForceOverwriteReplicaSecret": true
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-1a2b3c",
  "ReplicationStatus": [
    {
      "Region": "eu-west-3",
      "KmsKeyId": "alias/aws/secretsmanager",
      "Status": "InProgress"
    }
  ]
}
```
