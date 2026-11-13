# GetBucketEncryption

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketEncryptionCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?encryption`

Returns the default encryption configuration for an Amazon S3 bucket. By default, all buckets have a
default encryption configuration that uses server-side encryption with Amazon S3 managed keys (SSE-S3). This operation also returns the [BucketKeyEnabled](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled) and [BlockedEncryptionTypes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html#AmazonS3-Type-ServerSideEncryptionRule-BlockedEncryptionTypes) statuses.

- **General purpose buckets** - For information about the bucket
  default encryption feature, see [Amazon S3 Bucket Default Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the
  *Amazon S3 User Guide*.
- **Directory buckets** -
  For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS. For information about the default encryption configuration in
  directory buckets, see [Setting default server-side
  encryption behavior for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html).

Permissions
:   - **General purpose bucket permissions** - The
      `s3:GetEncryptionConfiguration` permission is required in a policy. The bucket
      owner has this permission by default. The bucket owner can grant this permission to others.
      For more information about permissions, see [Permissions Related to Bucket Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your
      Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).
    - **Directory bucket permissions** - To grant access to
      this API operation, you must have the `s3express:GetEncryptionConfiguration`
      permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the Amazon Web Services account that owns the resource.
      For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

The following operations are related to `GetBucketEncryption`:

- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
- [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketEncryptionRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket from which the server-side encryption configuration is retrieved.

**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code
`501 Not Implemented`.

## Output (`GetBucketEncryptionOutput`)

### `ServerSideEncryptionConfiguration` — ServerSideEncryptionConfiguration · sent as httpPayload

Specifies the default server-side-encryption configuration.
