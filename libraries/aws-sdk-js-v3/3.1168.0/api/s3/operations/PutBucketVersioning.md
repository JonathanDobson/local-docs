# PutBucketVersioning

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketVersioningCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?versioning`

This operation is not supported for directory buckets.

When you enable versioning on a bucket for the first time, it might take a short amount of time
for the change to be fully propagated. While this change is propagating, you might encounter
intermittent `HTTP 404 NoSuchKey` errors for requests to objects created or updated after
enabling versioning. We recommend that you wait for 15 minutes after enabling versioning before
issuing write operations (`PUT` or `DELETE`) on objects in the bucket.

Sets the versioning state of an existing bucket.

You can set the versioning state with one of the following values:

**Enabled**—Enables versioning for the objects in the bucket. All
objects added to the bucket receive a unique version ID.

**Suspended**—Disables versioning for the objects in the bucket. All
objects added to the bucket receive the version ID null.

If the versioning state has never been set on a bucket, it has no versioning state; a [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) request does not return a versioning state value.

In order to enable MFA Delete, you must be the bucket owner. If you are the bucket owner and want to
enable MFA Delete in the bucket versioning configuration, you must include the `x-amz-mfa
request` header and the `Status` and the `MfaDelete` request elements in a
request to set the versioning state of the bucket.

If you have an object expiration lifecycle configuration in your non-versioned bucket and you want
to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent
expiration policy. The noncurrent expiration lifecycle configuration will manage the deletes of the
noncurrent object versions in the version-enabled bucket. (A version-enabled bucket maintains one
current and zero or more noncurrent object versions.) For more information, see [Lifecycle and
Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-and-other-bucket-config).

The following operations are related to `PutBucketVersioning`:

- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
- [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketVersioningRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name.

### `ContentMD5` — string · sent as header `Content-MD5`

>The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
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

### `MFA` — string · sent as header `x-amz-mfa`

The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device. The serial number is the number that uniquely identifies the MFA device. For physical MFA devices, this is the unique serial number that's provided with the device. For virtual MFA devices, the serial number is the device ARN. For more information, see [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) and [Configuring MFA delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html) in the *Amazon Simple Storage Service User Guide*.

### `VersioningConfiguration` — VersioningConfiguration · **required** · sent as httpPayload

Container for setting the versioning state.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set versioning configuration on a bucket

The following example sets versioning configuration on bucket. The configuration enables versioning on the bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "VersioningConfiguration": {
    "MFADelete": "Disabled",
    "Status": "Enabled"
  }
}
```
