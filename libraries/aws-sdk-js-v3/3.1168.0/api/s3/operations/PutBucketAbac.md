# PutBucketAbac

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketAbacCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?abac`

Sets the attribute-based access control (ABAC) property of the general purpose bucket. You must have `s3:PutBucketABAC` permission to perform this action. When you enable ABAC, you can use tags for access control on your buckets. Additionally, when ABAC is enabled, you must use the [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) actions to manage tags on your buckets. You can nolonger use the [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html) and [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html) actions to tag your bucket. For more information, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

## Input (`PutBucketAbacRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the general purpose bucket.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash of the `PutBucketAbac` request body.

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more
information, see  [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The Amazon Web Services account ID of the general purpose bucket's owner.

### `AbacStatus` — AbacStatus · **required** · sent as httpPayload

The ABAC status of the general purpose bucket. When ABAC is enabled for the general purpose bucket, you can use tags to manage access to the general purpose buckets as well as for cost tracking purposes. When ABAC is disabled for the general purpose buckets, you can only use tags for cost tracking purposes. For more information, see [Using tags with S3 general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html).

## Output (`Unit`)

_None._
