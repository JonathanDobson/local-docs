# UpdateBucketMetadataInventoryTableConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `UpdateBucketMetadataInventoryTableConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?metadataInventoryTable`

Enables or disables a live inventory table for an S3 Metadata configuration on a general
purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have the following permissions. For more information, see
    [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    If you want to encrypt your inventory table with server-side encryption with Key Management Service
    (KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more
    information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    - `s3:UpdateBucketMetadataInventoryTableConfiguration`
    - `s3tables:CreateTableBucket`
    - `s3tables:CreateNamespace`
    - `s3tables:GetTable`
    - `s3tables:CreateTable`
    - `s3tables:PutTablePolicy`
    - `s3tables:PutTableEncryption`
    - `kms:DescribeKey`

The following operations are related to `UpdateBucketMetadataInventoryTableConfiguration`:

- [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
- [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
- [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)
- [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`UpdateBucketMetadataInventoryTableConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that corresponds to the metadata configuration that you want to
enable or disable an inventory table for.

### `ContentMD5` — string · sent as header `Content-MD5`

The `Content-MD5` header for the inventory table configuration.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

The checksum algorithm to use with your inventory table configuration.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `InventoryTableConfiguration` — InventoryTableConfigurationUpdates · **required** · sent as httpPayload

The contents of your inventory table configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected owner of the general purpose bucket that corresponds to the metadata table
configuration that you want to enable or disable an inventory table for.

## Output (`Unit`)

_None._
