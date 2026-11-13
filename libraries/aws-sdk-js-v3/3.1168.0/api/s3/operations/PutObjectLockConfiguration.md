# PutObjectLockConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutObjectLockConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?object-lock`

This operation is not supported for directory buckets.

Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock
configuration will be applied by default to every new object placed in the specified bucket. For more
information, see [Locking
Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

- The `DefaultRetention` settings require both a mode and a period.
- The `DefaultRetention` period can be either `Days` or `Years`
  but you must select one. You cannot specify `Days` and `Years` at the same
  time.
- You can enable Object Lock for new or existing buckets. For more information, see [Configuring
  Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-configure.html).

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutObjectLockConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket whose Object Lock configuration you want to create or replace.

### `ObjectLockConfiguration` — ObjectLockConfiguration · sent as httpPayload

The Object Lock configuration that you want to apply to the specified bucket.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `Token` — string · sent as header `x-amz-bucket-object-lock-token`

A token to allow Object Lock to be enabled for an existing bucket.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash for the request body.

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

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`PutObjectLockConfigurationOutput`)

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`
