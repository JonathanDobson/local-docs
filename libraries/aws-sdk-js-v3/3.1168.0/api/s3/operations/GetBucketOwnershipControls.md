# GetBucketOwnershipControls

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketOwnershipControlsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?ownershipControls`

This operation is not supported for directory buckets.

Retrieves `OwnershipControls` for an Amazon S3 bucket. To use this operation, you must have
the `s3:GetBucketOwnershipControls` permission. For more information about Amazon S3 permissions,
see [Specifying
permissions in a policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html).

A bucket doesn't have `OwnershipControls` settings in the following cases:

- The bucket was created before the `BucketOwnerEnforced` ownership setting was
  introduced and you've never explicitly applied this value
- You've manually deleted the bucket ownership control value using the
  `DeleteBucketOwnershipControls` API operation.

By default, Amazon S3 sets `OwnershipControls` for all newly created buckets.

For information about Amazon S3 Object Ownership, see [Using Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html).

The following operations are related to `GetBucketOwnershipControls`:

- PutBucketOwnershipControls
- DeleteBucketOwnershipControls

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketOwnershipControlsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose `OwnershipControls` you want to retrieve.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketOwnershipControlsOutput`)

### `OwnershipControls` — OwnershipControls · sent as httpPayload

The `OwnershipControls` (BucketOwnerEnforced, BucketOwnerPreferred, or ObjectWriter)
currently in effect for this Amazon S3 bucket.
