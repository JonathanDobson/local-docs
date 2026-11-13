# DisassociateDatasetKmsKey

Service: Amazon CloudWatch · SDK for JavaScript v3: `DisassociateDatasetKmsKeyCommand` from `@aws-sdk/client-cloudwatch`

Removes the customer managed Amazon Web Services Key Management Service
(Amazon Web Services KMS) key association from the specified dataset. After this
operation completes, data that you publish to the dataset is encrypted at rest using
an Amazon Web Services owned key managed by Amazon CloudWatch.

Only the `default` dataset is supported. To call this operation, the
dataset must currently have a customer managed KMS key associated with it. If the
dataset has no associated KMS key, the operation fails with
`ResourceNotFoundException`.

Amazon CloudWatch performs a dry-run `kms:Decrypt` call on the
currently associated key as part of this operation. The caller must have
`kms:Decrypt` permission on the currently associated key. If the key is
accessible but the caller lacks `kms:Decrypt` permission, the operation
fails with `AccessDeniedException`.

If the currently associated key has been deleted, is scheduled for deletion,
is pending import, is unavailable, or has been disabled, Amazon CloudWatch
does not require `kms:Decrypt` permission on that key and the
disassociation proceeds. If the key was only disabled, consider re-enabling it
instead of disassociating, because re-enabling allows Amazon CloudWatch to
resume decrypting your existing metric data.

Disassociating a KMS key from a dataset does not immediately remove the
`kms:Decrypt` requirement on data plane operations. For up to three
hours after disassociation, callers must continue to have
`kms:Decrypt` permission on the previously associated key. Some data
might still be encrypted with that key during this window. After this enforcement
window elapses, the `kms:Decrypt` requirement is lifted.

For more information about using customer managed keys with Amazon CloudWatch,
see [Encryption at rest
with customer managed keys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cmk-encryption.html) in the *Amazon CloudWatch User
Guide*.

## Input (`DisassociateDatasetKmsKeyInput`)

### `DatasetIdentifier` — string · **required**

Specifies the identifier of the dataset from which to remove the KMS key
association. For the `default` dataset, you can specify either
`default` or the full dataset Amazon Resource Name (ARN) in the format
`arn:aws:cloudwatch:Region:account-id:dataset/default`.

## Output (`DisassociateDatasetKmsKeyOutput`)

_None._

## Errors

- `ConflictException` — This operation attempted to create a resource that already exists.
- `ResourceNotFoundException` — The named resource does not exist.
