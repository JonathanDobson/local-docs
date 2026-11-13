# PutPublicAccessBlock

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutPublicAccessBlockCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?publicAccessBlock`

This operation is not supported for directory buckets.

Creates or modifies the `PublicAccessBlock` configuration for an Amazon S3 bucket. To use this
operation, you must have the `s3:PutBucketPublicAccessBlock` permission. For more information
about Amazon S3 permissions, see [Specifying Permissions in a
Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

When Amazon S3 evaluates the `PublicAccessBlock` configuration for a bucket or an
object, it checks the `PublicAccessBlock` configuration for both the bucket (or
the bucket that contains the object) and the bucket owner's account. Account-level settings
automatically inherit from organization-level policies when present. If the
`PublicAccessBlock` configurations are different between the bucket and the
account, Amazon S3 uses the most restrictive combination of the bucket-level and account-level
settings.

For more information about when Amazon S3 considers a bucket or an object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status).

The following operations are related to `PutPublicAccessBlock`:

- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)
- [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html)
- [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutPublicAccessBlockRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose `PublicAccessBlock` configuration you want to
set.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash of the `PutPublicAccessBlock` request body.

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `PublicAccessBlockConfiguration` — PublicAccessBlockConfiguration · **required** · sent as httpPayload

The `PublicAccessBlock` configuration that you want to apply to this Amazon S3
bucket. You can enable the configuration options in any combination. For more information
about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._
