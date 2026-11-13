# PutBucketPolicy

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketPolicyCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?policy`

Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   If you are using an identity other than the root user of the Amazon Web Services account that owns the
    bucket, the calling identity must both have the `PutBucketPolicy` permissions on the
    specified bucket and belong to the bucket owner's account in order to use this operation.

    If you don't have `PutBucketPolicy` permissions, Amazon S3 returns a `403 Access
    Denied` error. If you have the correct permissions, but you're not using an identity that
    belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not Allowed`
    error.

    To ensure that bucket owners don't inadvertently lock themselves out of their own buckets,
    the root principal in a bucket owner's Amazon Web Services account can perform the
    `GetBucketPolicy`, `PutBucketPolicy`, and
    `DeleteBucketPolicy` API actions, even if their bucket policy explicitly denies the
    root principal's access. Bucket owner root principals can only be blocked from performing these
    API actions by VPC endpoint policies and Amazon Web Services Organizations policies.

    - **General purpose bucket permissions** - The
      `s3:PutBucketPolicy` permission is required in a policy. For more information
      about general purpose buckets bucket policies, see [Using Bucket Policies and User
      Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to
      this API operation, you must have the `s3express:PutBucketPolicy` permission in
      an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the Amazon Web Services account that owns the resource.
      For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

Example bucket policies
:   **General purpose buckets example bucket policies** - See [Bucket policy
    examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) in the *Amazon S3 User Guide*.

    **Directory bucket example bucket policies** - See [Example
    bucket policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

The following operations are related to `PutBucketPolicy`:

- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketPolicyRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket.

**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash of the request body.

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

This functionality is not supported for directory buckets.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum-algorithm` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`.

For the `x-amz-checksum-algorithm` header, replace `algorithm` with the supported algorithm from the following list:

- `CRC32`
- `CRC32C`
- `CRC64NVME`
- `MD5`
- `SHA1`
- `SHA256`
- `SHA512`
- `XXHASH3`
- `XXHASH64`
- `XXHASH128`

For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If the individual checksum value you provide through `x-amz-checksum-algorithm` doesn't match the checksum algorithm you set through `x-amz-sdk-checksum-algorithm`, Amazon S3 fails the request with a `BadDigest` error.

For directory buckets, when you use Amazon Web Services SDKs, `CRC32` is the default checksum algorithm that's used for performance.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ConfirmRemoveSelfBucketAccess` — boolean · sent as header `x-amz-confirm-remove-self-bucket-access`

Set this parameter to true to confirm that you want to remove your permissions to change this bucket
policy in the future.

This functionality is not supported for directory buckets.

### `Policy` — string · **required** · sent as httpPayload

The bucket policy as a JSON document.

For directory buckets, the only IAM action supported in the bucket policy is
`s3express:CreateSession`.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code
`501 Not Implemented`.

## Output (`Unit`)

_None._

## Examples

### Set bucket policy

The following example sets a permission policy on a bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "Policy": "{\"Version\": \"2012-10-17\", \"Statement\": [{ \"Sid\": \"id-1\",\"Effect\": \"Allow\",\"Principal\": {\"AWS\": \"arn:aws:iam::123456789012:root\"}, \"Action\": [ \"s3:PutObject\",\"s3:PutObjectAcl\"], \"Resource\": [\"arn:aws:s3:::acl3/*\" ] } ]}"
}
```
