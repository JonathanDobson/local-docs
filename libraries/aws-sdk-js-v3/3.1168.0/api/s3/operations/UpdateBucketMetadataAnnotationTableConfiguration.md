# UpdateBucketMetadataAnnotationTableConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `UpdateBucketMetadataAnnotationTableConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?metadataAnnotationTable`

Updates the annotation table configuration for an Amazon S3 bucket's metadata configuration. Use this
operation to enable or disable the annotation table, or to update its associated IAM role.

An annotation table is a queryable Iceberg table that contains records of all annotations
attached to objects in the bucket. To use this operation, the bucket must have an existing Amazon S3
Metadata configuration.

To use this operation, you must have the
`s3:UpdateBucketMetadataAnnotationTableConfiguration` permission. If you are specifying
or changing the IAM role, you must also have `iam:PassRole` permission for the role.

The IAM role must have a trust policy that allows the Amazon S3 metadata service to assume it, and a
permissions policy that grants the actions needed to read annotations from your bucket. The
following examples show a trust policy and a permissions policy that you can adapt for your bucket
and account.

The following operations are related to
`UpdateBucketMetadataAnnotationTableConfiguration`:

- [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)
- [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)

## Input (`UpdateBucketMetadataAnnotationTableConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket whose annotation table configuration to update.

### `ContentMD5` — string · sent as header `Content-MD5`

Base64-encoded MD5 digest of the message body.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Checksum algorithm for the request payload.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `AnnotationTableConfiguration` — AnnotationTableConfigurationUpdates · **required** · sent as httpPayload

The annotation table configuration updates to apply.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner.

## Output (`Unit`)

_None._
