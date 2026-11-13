# PutBucketRequestPayment

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketRequestPaymentCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?requestPayment`

This operation is not supported for directory buckets.

Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads
from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person
requesting the download will be charged for the download. For more information, see [Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html).

The following operations are related to `PutBucketRequestPayment`:

- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [GetBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketRequestPaymentRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
message integrity check to verify that the request body was not corrupted in transit. For more
information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt).

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `RequestPaymentConfiguration` — RequestPaymentConfiguration · **required** · sent as httpPayload

Container for Payer.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set request payment configuration on a bucket.

The following example sets request payment configuration on a bucket so that person requesting the download is charged.

Input:

```json
{
  "Bucket": "examplebucket",
  "RequestPaymentConfiguration": {
    "Payer": "Requester"
  }
}
```
