# DeletePublicAccessBlock

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeletePublicAccessBlockCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?publicAccessBlock`

This operation is not supported for directory buckets.

Removes the `PublicAccessBlock` configuration for an Amazon S3 bucket. This
operation removes the bucket-level configuration only. The effective public access behavior
will still be governed by account-level settings (which may inherit from organization-level
policies). To use this operation, you must have the `s3:PutBucketPublicAccessBlock`
permission. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access
Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

The following operations are related to `DeletePublicAccessBlock`:

- [Using
  Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html)
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
- [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeletePublicAccessBlockRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The Amazon S3 bucket whose `PublicAccessBlock` configuration you want to delete.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._
