# PutBucketOwnershipControls

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketOwnershipControlsCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?ownershipControls`

This operation is not supported for directory buckets.

Creates or modifies `OwnershipControls` for an Amazon S3 bucket. To use this operation, you
must have the `s3:PutBucketOwnershipControls` permission. For more information about Amazon S3
permissions, see [Specifying permissions in a policy](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-with-s3-actions.html).

For information about Amazon S3 Object Ownership, see [Using object ownership](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/about-object-ownership.html).

The following operations are related to `PutBucketOwnershipControls`:

- GetBucketOwnershipControls
- DeleteBucketOwnershipControls

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketOwnershipControlsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose `OwnershipControls` you want to set.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash of the `OwnershipControls` request body.

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `OwnershipControls` — OwnershipControls · **required** · sent as httpPayload

The `OwnershipControls` (BucketOwnerEnforced, BucketOwnerPreferred, or ObjectWriter) that
you want to apply to this Amazon S3 bucket.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use the SDK. This
header will not provide any additional functionality if you don't use the SDK. When you send this
header, there must be a corresponding `x-amz-checksum-algorithm` header
sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

## Output (`Unit`)

_None._
