# CreateBucketMetadataConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `CreateBucketMetadataConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `POST /{Bucket}?metadataConfiguration`

Creates an S3 Metadata V2 metadata configuration for a general purpose bucket. For more information, see
[Accelerating
data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have the following permissions. For more information, see
    [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    If you want to encrypt your metadata tables with server-side encryption with Key Management Service
    (KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more
    information, see [Setting up permissions for configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html) in the
    *Amazon S3 User Guide*.

    If you also want to integrate your table bucket with Amazon Web Services analytics services so that you can
    query your metadata table, you need additional permissions. For more information, see  [Integrating
    Amazon S3 Tables with Amazon Web Services analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) in the
    *Amazon S3 User Guide*.

    To query your metadata tables, you need additional permissions. For more information, see
    [Permissions for querying metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-query-permissions.html) in the *Amazon S3 User Guide*.

    - `s3:CreateBucketMetadataTableConfiguration`

      The IAM policy action name is the same for the V1 and V2 API operations.
    - `s3tables:CreateTableBucket`
    - `s3tables:CreateNamespace`
    - `s3tables:GetTable`
    - `s3tables:CreateTable`
    - `s3tables:PutTablePolicy`
    - `s3tables:PutTableBucketPolicy`
    - `s3tables:PutTableEncryption`
    - `kms:DescribeKey`
    - `iam:PassRole` - required if you include an
      `AnnotationTableConfiguration` with an IAM role.

The following operations are related to `CreateBucketMetadataConfiguration`:

- [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)
- [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)
- [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)
- [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)
- [UpdateBucketMetadataAnnotationTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html)

If you include an `AnnotationTableConfiguration` with an IAM role, the role must
have a trust policy that allows the Amazon S3 metadata service to assume it, and a permissions policy
that grants the actions needed to read annotations from your bucket. The following examples show
a trust policy and a permissions policy that you can adapt for your bucket and account.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`CreateBucketMetadataConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The general purpose bucket that you want to create the metadata configuration for.

### `ContentMD5` — string · sent as header `Content-MD5`

The `Content-MD5` header for the metadata configuration.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

The checksum algorithm to use with your metadata configuration.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `MetadataConfiguration` — MetadataConfiguration · **required** · sent as httpPayload

The contents of your metadata configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The expected owner of the general purpose bucket that corresponds to your metadata configuration.

## Output (`Unit`)

_None._
