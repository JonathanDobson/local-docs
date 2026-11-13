# GetPublicAccessBlock

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetPublicAccessBlockCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?publicAccessBlock`

This operation is not supported for directory buckets.

Retrieves the `PublicAccessBlock` configuration for an Amazon S3 bucket. This
operation returns the bucket-level configuration only. To understand the effective public
access behavior, you must also consider account-level settings (which may inherit from
organization-level policies). To use this operation, you must have the
`s3:GetBucketPublicAccessBlock` permission. For more information about Amazon S3
permissions, see [Specifying Permissions in a
Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

When Amazon S3 evaluates the `PublicAccessBlock` configuration for a bucket or an
object, it checks the `PublicAccessBlock` configuration for both the bucket (or
the bucket that contains the object) and the bucket owner's account. Account-level settings
automatically inherit from organization-level policies when present. If the
`PublicAccessBlock` settings are different between the bucket and the account,
Amazon S3 uses the most restrictive combination of the bucket-level and account-level
settings.

For more information about when Amazon S3 considers a bucket or an object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status).

The following operations are related to `GetPublicAccessBlock`:

- [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html)
- [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetPublicAccessBlockRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose `PublicAccessBlock` configuration you want to retrieve.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetPublicAccessBlockOutput`)

### `PublicAccessBlockConfiguration` — PublicAccessBlockConfiguration · sent as httpPayload

The `PublicAccessBlock` configuration currently in effect for this Amazon S3 bucket.
