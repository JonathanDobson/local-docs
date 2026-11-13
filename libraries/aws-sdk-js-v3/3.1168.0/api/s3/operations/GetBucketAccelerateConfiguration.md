# GetBucketAccelerateConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketAccelerateConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?accelerate`

This operation is not supported for directory buckets.

This implementation of the GET action uses the `accelerate` subresource to return the
Transfer Acceleration state of a bucket, which is either `Enabled` or `Suspended`.
Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers
to and from Amazon S3.

To use this operation, you must have permission to perform the
`s3:GetAccelerateConfiguration` action. The bucket owner has this permission by default.
The bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to your Amazon S3
Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide*.

You set the Transfer Acceleration state of an existing bucket to `Enabled` or
`Suspended` by using the [PutBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html) operation.

A GET `accelerate` request does not return a state value for a bucket that has no
transfer acceleration state. A bucket has no Transfer Acceleration state if a state has never been set
on the bucket.

For more information about transfer acceleration, see [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) in the
Amazon S3 User Guide.

The following operations are related to `GetBucketAccelerateConfiguration`:

- [PutBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketAccelerateConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which the accelerate configuration is retrieved.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Output (`GetBucketAccelerateConfigurationOutput`)

### `Status` — BucketAccelerateStatus (enum)

The accelerate configuration of the bucket.

Values: `Enabled`, `Suspended`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`
