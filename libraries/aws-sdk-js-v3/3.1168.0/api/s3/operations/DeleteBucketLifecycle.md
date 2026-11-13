# DeleteBucketLifecycle

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketLifecycleCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?lifecycle`

Deletes the lifecycle configuration from the specified bucket. Amazon S3 removes all the lifecycle
configuration rules in the lifecycle subresource associated with the bucket. Your objects never expire,
and Amazon S3 no longer automatically deletes any objects on the basis of rules contained in the deleted
lifecycle configuration.

Permissions
:   - **General purpose bucket permissions** - By default, all Amazon S3
      resources are private, including buckets, objects, and related subresources (for example,
      lifecycle configuration and website configuration). Only the resource owner (that is, the
      Amazon Web Services account that created it) can access the resource. The resource owner can optionally
      grant access permissions to others by writing an access policy. For this operation, a user
      must have the `s3:PutLifecycleConfiguration` permission.

      For more information about permissions, see [Managing Access Permissions to Your
      Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

    - **Directory bucket permissions** - You must have the
      `s3express:PutLifecycleConfiguration` permission in an IAM identity-based policy
      to use this operation. Cross-account access to this API operation isn't supported. The
      resource owner can optionally grant access permissions to others by creating a role or user
      for them as long as they are within the same account as the owner and resource.

      For more information about directory bucket policies and permissions, see [Authorizing Regional endpoint APIs with IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User
      Guide*.

      **Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
      For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
      *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
      *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is
    `s3express-control.region.amazonaws.com`.

For more information about the object expiration, see [Elements to
Describe Lifecycle Actions](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions).

Related actions include:

- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketLifecycleRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name of the lifecycle to delete.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

## Output (`Unit`)

_None._

## Examples

### To delete lifecycle configuration on a bucket.

The following example deletes lifecycle configuration on a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```
