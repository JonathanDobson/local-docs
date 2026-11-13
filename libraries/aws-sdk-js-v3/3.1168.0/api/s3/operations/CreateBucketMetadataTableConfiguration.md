# CreateBucketMetadataTableConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `CreateBucketMetadataTableConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `POST /{Bucket}?metadataTable`

We recommend that you create your S3 Metadata configurations by using the V2
[CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) API operation. We no longer recommend using the V1
`CreateBucketMetadataTableConfiguration` API operation.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

Creates a V1 S3 Metadata configuration for a general purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have the following permissions. For more information, see
    [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    If you want to encrypt your metadata tables with server-side encryption with Key Management Service
    (KMS) keys (SSE-KMS), you need additional permissions. For more
    information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    If you also want to integrate your table bucket with Amazon Web Services analytics services so that you can
    query your metadata table, you need additional permissions. For more information, see  [Integrating
    Amazon S3 Tables with Amazon Web Services analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) in the
    *Amazon S3 User Guide*.

    - `s3:CreateBucketMetadataTableConfiguration`
    - `s3tables:CreateNamespace`
    - `s3tables:GetTable`
    - `s3tables:CreateTable`
    - `s3tables:PutTablePolicy`

The following operations are related to `CreateBucketMetadataTableConfiguration`:

- [DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html)
- [GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`CreateBucketMetadataTableConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that you want to create the metadata table configuration for.

### `ContentMD5` — string · sent as header `Content-MD5`

The `Content-MD5` header for the metadata table configuration.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

The checksum algorithm to use with your metadata table configuration.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `MetadataTableConfiguration` — MetadataTableConfiguration · **required** · sent as httpPayload

The contents of your metadata table configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected owner of the general purpose bucket that corresponds to your metadata table configuration.

## Output (`Unit`)

_None._
