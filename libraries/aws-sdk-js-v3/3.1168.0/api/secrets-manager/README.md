# AWS Secrets Manager — API reference

API version `2017-10-17` · protocol awsJson1_1 · SDK for JavaScript v3 client `@aws-sdk/client-secrets-manager`

Amazon Web Services Secrets Manager

Amazon Web Services Secrets Manager provides a service to enable you to store, manage, and retrieve, secrets.

This guide provides descriptions of the Secrets Manager API. For more information about using this
service, see the [Amazon Web Services Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/introduction.html).

**API Version**

This version of the Secrets Manager API Reference documents the Secrets Manager API version 2017-10-17.

For a list of endpoints, see [Amazon Web Services Secrets Manager
endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/asm_access.html#endpoints).

**Support and Feedback for Amazon Web Services Secrets Manager**

We welcome your feedback. Send your comments to [awssecretsmanager-feedback@amazon.com](mailto:awssecretsmanager-feedback@amazon.com), or post your feedback and questions in the [Amazon Web Services Secrets Manager Discussion Forum](http://forums.aws.amazon.com/forum.jspa?forumID=296). For more
information about the Amazon Web Services Discussion Forums, see [Forums
Help](http://forums.aws.amazon.com/help.jspa).

**Logging API Requests**

Amazon Web Services Secrets Manager supports Amazon Web Services CloudTrail, a service that records Amazon Web Services API calls for your Amazon Web Services
account and delivers log files to an Amazon S3 bucket. By using information that's collected
by Amazon Web Services CloudTrail, you can determine the requests successfully made to Secrets Manager, who made the
request, when it was made, and so on. For more about Amazon Web Services Secrets Manager and support for Amazon Web Services
CloudTrail, see [Logging
Amazon Web Services Secrets Manager Events with Amazon Web Services CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html#monitoring_cloudtrail) in the *Amazon Web Services Secrets Manager User Guide*.
To learn more about CloudTrail, including enabling it and find your log files, see the [Amazon Web Services CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html).

## Operations (26)

- [`AssociateCrossAccountReplica`](operations/AssociateCrossAccountReplica.md) — Links a primary secret in your account to a replica secret in a different Amazon Web Services account and starts replication to this replica.
- [`BatchGetSecretValue`](operations/BatchGetSecretValue.md) — Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary` for up to 20 secrets.
- [`CancelRotateSecret`](operations/CancelRotateSecret.md) — Turns off automatic rotation, and if a rotation is currently in progress, cancels the rotation.
- [`CreateSecret`](operations/CreateSecret.md) — Creates a new secret.
- [`DeleteResourcePolicy`](operations/DeleteResourcePolicy.md) — Deletes the resource-based permission policy attached to the secret.
- [`DeleteSecret`](operations/DeleteSecret.md) — Deletes a secret and all of its versions.
- [`DescribeSecret`](operations/DescribeSecret.md) — Retrieves the details of a secret.
- [`DisassociateCrossAccountReplica`](operations/DisassociateCrossAccountReplica.md) — Removes the link between a primary secret in your account and a cross-account replica secret, and stops replication to the replica secret.
- [`GetRandomPassword`](operations/GetRandomPassword.md) — Generates a random password.
- [`GetResourcePolicy`](operations/GetResourcePolicy.md) — Retrieves the JSON text of the resource-based policy document attached to the secret.
- [`GetSecretValue`](operations/GetSecretValue.md) — Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary` from the specified version of a secret, whichever contains content.
- [`ListResourcePolicies`](operations/ListResourcePolicies.md) — Lists the resource-based policies attached to a secret.
- [`ListSecretVersionIds`](operations/ListSecretVersionIds.md) — Lists the versions of a secret.
- [`ListSecrets`](operations/ListSecrets.md) — Lists the secrets that are stored by Secrets Manager in the Amazon Web Services account, not including secrets that are marked for deletion.
- [`PutResourcePolicy`](operations/PutResourcePolicy.md) — Attaches a resource-based permission policy to a secret.
- [`PutSecretValue`](operations/PutSecretValue.md) — Creates a new version of your secret by creating a new encrypted value and attaching it to the secret.
- [`RemoveRegionsFromReplication`](operations/RemoveRegionsFromReplication.md) — For a secret that is replicated to other Regions, deletes the secret replicas from the Regions you specify.
- [`ReplicateSecretToRegions`](operations/ReplicateSecretToRegions.md) — Replicates the secret to a new Regions.
- [`RestoreSecret`](operations/RestoreSecret.md) — Cancels the scheduled deletion of a secret by removing the `DeletedDate` time stamp.
- [`RotateSecret`](operations/RotateSecret.md) — Configures and starts the asynchronous process of rotating the secret.
- [`StopReplicationToReplica`](operations/StopReplicationToReplica.md) — Removes the link between a replica secret and its primary secret, and stops replication to the replica.
- [`TagResource`](operations/TagResource.md) — Attaches tags to a secret.
- [`UntagResource`](operations/UntagResource.md) — Removes specific tags from a secret.
- [`UpdateSecret`](operations/UpdateSecret.md) — Modifies the details of a secret, including metadata and the secret value.
- [`UpdateSecretVersionStage`](operations/UpdateSecretVersionStage.md) — Modifies the staging labels attached to a version of a secret.
- [`ValidateResourcePolicy`](operations/ValidateResourcePolicy.md) — Validates that a resource policy does not grant a wide range of principals access to your secret.
