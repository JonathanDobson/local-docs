# AssociateDatasetKmsKey

Service: Amazon CloudWatch · SDK for JavaScript v3: `AssociateDatasetKmsKeyCommand` from `@aws-sdk/client-cloudwatch`

Associates an Amazon Web Services Key Management Service (Amazon Web Services KMS)
customer managed key with the specified dataset. After this operation completes, all
data published to the dataset is encrypted at rest using the specified KMS key.
Callers must have `kms:Decrypt` permission on the key to read the
encrypted data.

Only the `default` dataset is supported. The `default` dataset
is implicit for every account in every Region — you do not need to create it before
calling this operation.

You can call `AssociateDatasetKmsKey` on a dataset that is already
associated with a KMS key to replace the existing key with a different one. The
caller must have `kms:Decrypt` permission on both the current key and
the new key.

If the currently associated key has been deleted, is scheduled for deletion,
is pending import, is unavailable, or has been disabled, Amazon CloudWatch
does not require `kms:Decrypt` permission on the current key and
the rotation proceeds. If the key was only disabled, consider re-enabling it
instead of rotating, because re-enabling allows Amazon CloudWatch to
resume decrypting your existing metric data encrypted with that key.

The KMS key that you specify must meet all of the following requirements:

- It must be a symmetric encryption KMS key (key spec
  `SYMMETRIC_DEFAULT`, key usage `ENCRYPT_DECRYPT`).
  Asymmetric keys, HMAC keys, and key material types other than
  `SYMMETRIC_DEFAULT` are not supported.
- It must be enabled and not pending deletion.
- Its key policy must grant the CloudWatch service principal
  (`cloudwatch.amazonaws.com`) these permissions:
  `kms:DescribeKey`, `kms:GenerateDataKey`,
  `kms:Encrypt`, `kms:Decrypt`, and
  `kms:ReEncrypt*`. Amazon CloudWatch requires these permissions
  to manage the data on your behalf.
- The calling principal must have `kms:Decrypt` permission on the
  key.
- It must be specified as a fully qualified key ARN. Key IDs, aliases, and
  alias ARNs are not accepted.
- It must be in the same Amazon Web Services Region as the dataset.

Before completing the association, Amazon CloudWatch validates the key by
performing a series of dry-run KMS operations. Service-principal checks run first to
verify that the key policy grants the required access to Amazon CloudWatch. These
checks include `kms:DescribeKey`, `kms:GenerateDataKey`,
`kms:Encrypt`, `kms:Decrypt`, and `kms:ReEncrypt*`.
After those succeed, a `kms:Decrypt` dry-run is run with the caller's
credentials to verify that the calling principal can use the new key. When you are
replacing an existing key, the caller's `kms:Decrypt` dry-run is also run
on the current key.

If any of these checks on the new key fails, the operation fails and the existing
key association (if any) remains unchanged. Common failure causes include the new key
being disabled, the key policy not granting the required permissions to
Amazon CloudWatch, or the caller lacking `kms:Decrypt` permission on
the new key.

For more information about using customer managed keys with Amazon CloudWatch,
see [Encryption at rest
with customer managed keys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cmk-encryption.html) in the *Amazon CloudWatch User
Guide*.

## Input (`AssociateDatasetKmsKeyInput`)

### `DatasetIdentifier` — string · **required**

Specifies the identifier of the dataset that you want to associate the KMS key
with. For the `default` dataset, you can specify either
`default` or the full dataset Amazon Resource Name (ARN) in the format
`arn:aws:cloudwatch:Region:account-id:dataset/default`.

### `KmsKeyArn` — string · **required**

Specifies the Amazon Resource Name (ARN) of the customer managed KMS key to
associate with the dataset. The key must be a symmetric encryption KMS key
(`SYMMETRIC_DEFAULT`) in the same Amazon Web Services Region as the
dataset.

The ARN must be in the format
`arn:aws:kms:Region:account-id:key/key-id`.
Key IDs, aliases, and alias ARNs are not accepted.

For more information about KMS key ARNs, see [Key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in
the *Amazon Web Services Key Management Service Developer
Guide*.

## Output (`AssociateDatasetKmsKeyOutput`)

_None._

## Errors

- `ConflictException` — This operation attempted to create a resource that already exists.
- `KmsAccessDeniedException` — The operation was denied because either the calling principal lacks the required Amazon Web Services Key Management Service (Amazon Web Services KMS) permission on the key, or the key policy does not…
- `KmsKeyDisabledException` — The specified Amazon Web Services Key Management Service (Amazon Web Services KMS) key is disabled or pending deletion.
- `KmsKeyNotFoundException` — The specified Amazon Web Services Key Management Service (Amazon Web Services KMS) key could not be found.
- `ResourceNotFoundException` — The named resource does not exist.
