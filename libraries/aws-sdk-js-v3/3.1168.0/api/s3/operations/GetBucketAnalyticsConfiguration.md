# GetBucketAnalyticsConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketAnalyticsConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?analytics&x-id=GetBucketAnalyticsConfiguration`

This operation is not supported for directory buckets.

This implementation of the GET action returns an analytics configuration (identified by the
analytics configuration ID) from the bucket.

To use this operation, you must have permissions to perform the
`s3:GetAnalyticsConfiguration` action. The bucket owner has this permission by default. The
bucket owner can grant this permission to others. For more information about permissions, see  [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3
Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide*.

For information about Amazon S3 analytics feature, see [Amazon S3 Analytics – Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html)
in the *Amazon S3 User Guide*.

The following operations are related to `GetBucketAnalyticsConfiguration`:

- [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html)
- [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html)
- [PutBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketAnalyticsConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket from which an analytics configuration is retrieved.

### `Id` — string · **required** · sent as query `id`

The ID that identifies the analytics configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketAnalyticsConfigurationOutput`)

### `AnalyticsConfiguration` — AnalyticsConfiguration · sent as httpPayload

The configuration and any analyses for the analytics filter.
