# DeleteBucketOwnershipControls

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketOwnershipControlsCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?ownershipControls`

This operation is not supported for directory buckets.

Removes `OwnershipControls` for an Amazon S3 bucket. To use this operation, you must have the
`s3:PutBucketOwnershipControls` permission. For more information about Amazon S3 permissions,
see [Specifying
Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

For information about Amazon S3 Object Ownership, see [Using Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html).

The following operations are related to `DeleteBucketOwnershipControls`:

- GetBucketOwnershipControls
- PutBucketOwnershipControls

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketOwnershipControlsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The Amazon S3 bucket whose `OwnershipControls` you want to delete.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._
