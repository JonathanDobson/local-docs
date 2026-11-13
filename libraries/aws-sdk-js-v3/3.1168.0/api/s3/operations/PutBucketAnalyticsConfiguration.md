# PutBucketAnalyticsConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketAnalyticsConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?analytics`

This operation is not supported for directory buckets.

Sets an analytics configuration for the bucket (specified by the analytics configuration ID). You
can have up to 1,000 analytics configurations per bucket.

You can choose to have storage class analysis export analysis reports sent to a comma-separated
values (CSV) flat file. See the `DataExport` request element. Reports are updated daily and
are based on the object filters that you configure. When selecting data export, you specify a
destination bucket and an optional destination prefix where the file is written. You can export the data
to a destination bucket in a different account. However, the destination bucket must be in the same
Region as the bucket that you are making the PUT analytics configuration to. For more information, see
[Amazon S3 Analytics –
Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html).

You must create a bucket policy on the destination bucket where the exported file is written to
grant permissions to Amazon S3 to write objects to the bucket. For an example policy, see [Granting
Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9).

To use this operation, you must have permissions to perform the
`s3:PutAnalyticsConfiguration` action. The bucket owner has this permission by default. The
bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3
Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

`PutBucketAnalyticsConfiguration` has the following special errors:

- - *HTTP Error: HTTP 400 Bad Request*
  - *Code: InvalidArgument*
  - *Cause: Invalid argument.*
- - *HTTP Error: HTTP 400 Bad Request*
  - *Code: TooManyConfigurations*
  - *Cause: You are attempting to create a new configuration but have already reached
    the 1,000-configuration limit.*
- - *HTTP Error: HTTP 403 Forbidden*
  - *Code: AccessDenied*
  - *Cause: You are not the owner of the specified bucket, or you do not have the
    s3:PutAnalyticsConfiguration bucket permission to set the configuration on the
    bucket.*

The following operations are related to `PutBucketAnalyticsConfiguration`:

- [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html)
- [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html)
- [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketAnalyticsConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket to which an analytics configuration is stored.

### `Id` — string · **required** · sent as query `id`

The ID that identifies the analytics configuration.

### `AnalyticsConfiguration` — AnalyticsConfiguration · **required** · sent as httpPayload

The configuration and any analyses for the analytics filter.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._
