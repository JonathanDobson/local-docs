# GetBucketPolicyStatus

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketPolicyStatusCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?policyStatus`

This operation is not supported for directory buckets.

Retrieves the policy status for an Amazon S3 bucket, indicating whether the bucket is public. In order to
use this operation, you must have the `s3:GetBucketPolicyStatus` permission. For more
information about Amazon S3 permissions, see [Specifying Permissions in a
Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

For more information about when Amazon S3 considers a bucket public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status).

The following operations are related to `GetBucketPolicyStatus`:

- [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html)
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketPolicyStatusRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose policy status you want to retrieve.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketPolicyStatusOutput`)

### `PolicyStatus` — PolicyStatus · sent as httpPayload

The policy status for the specified bucket.
