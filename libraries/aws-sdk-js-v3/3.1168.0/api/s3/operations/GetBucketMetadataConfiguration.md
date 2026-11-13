# GetBucketMetadataConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketMetadataConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?metadataConfiguration`

Retrieves the S3 Metadata configuration for a general purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2
metadata configurations. However, if you try to use the V1
`GetBucketMetadataTableConfiguration` API operation with V2 configurations, you
will receive an HTTP `405 Method Not Allowed` error.

Permissions
:   To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration`
    permission. For more information, see [Setting up permissions for
    configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the *Amazon S3 User Guide*.

    The IAM policy action name is the same for the V1 and V2 API operations.

The following operations are related to `GetBucketMetadataConfiguration`:

- [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
- [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
- [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)
- [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketMetadataConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that corresponds to the metadata configuration that you want to
retrieve.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected owner of the general purpose bucket that you want to retrieve the metadata table
configuration for.

## Output (`GetBucketMetadataConfigurationOutput`)

### `GetBucketMetadataConfigurationResult` — GetBucketMetadataConfigurationResult · sent as httpPayload

The metadata configuration for the general purpose bucket.
