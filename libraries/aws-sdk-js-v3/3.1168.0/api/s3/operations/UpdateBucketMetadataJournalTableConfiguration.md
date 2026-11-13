# UpdateBucketMetadataJournalTableConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `UpdateBucketMetadataJournalTableConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?metadataJournalTable`

Enables or disables journal table record expiration for an S3 Metadata configuration on a general
purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have the `s3:UpdateBucketMetadataJournalTableConfiguration`
    permission. For more information, see [Setting up permissions for
    configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.

The following operations are related to `UpdateBucketMetadataJournalTableConfiguration`:

- [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
- [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
- [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)
- [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`UpdateBucketMetadataJournalTableConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that corresponds to the metadata configuration that you want to
enable or disable journal table record expiration for.

### `ContentMD5` — string · sent as header `Content-MD5`

The `Content-MD5` header for the journal table configuration.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

The checksum algorithm to use with your journal table configuration.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `JournalTableConfiguration` — JournalTableConfigurationUpdates · **required** · sent as httpPayload

The contents of your journal table configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected owner of the general purpose bucket that corresponds to the metadata table
configuration that you want to enable or disable journal table record expiration for.

## Output (`Unit`)

_None._
