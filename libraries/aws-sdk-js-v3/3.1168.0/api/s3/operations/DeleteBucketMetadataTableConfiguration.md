# DeleteBucketMetadataTableConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketMetadataTableConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?metadataTable`

We recommend that you delete your S3 Metadata configurations by using the V2
[DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html) API operation. We no longer recommend using
the V1 `DeleteBucketMetadataTableConfiguration` API operation.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

Deletes a V1 S3 Metadata configuration from a general purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

You can use the V2 `DeleteBucketMetadataConfiguration` API operation with V1 or V2
metadata table configurations. However, if you try to use the V1
`DeleteBucketMetadataTableConfiguration` API operation with V2 configurations, you
will receive an HTTP `405 Method Not Allowed` error.

Make sure that you update your processes to use the new V2 API operations
(`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`, and
`DeleteBucketMetadataConfiguration`) instead of the V1 API operations.

Permissions
:   To use this operation, you must have the
    `s3:DeleteBucketMetadataTableConfiguration` permission. For more information, see
    [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

The following operations are related to `DeleteBucketMetadataTableConfiguration`:

- [CreateBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html)
- [GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketMetadataTableConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that you want to remove the metadata table configuration from.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected bucket owner of the general purpose bucket that you want to remove the metadata table
configuration from.

## Output (`Unit`)

_None._
