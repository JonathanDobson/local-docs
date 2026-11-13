# ListBucketAnalyticsConfigurations

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListBucketAnalyticsConfigurationsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?analytics&x-id=ListBucketAnalyticsConfigurations`

This operation is not supported for directory buckets.

Lists the analytics configurations for the bucket. You can have up to 1,000 analytics configurations
per bucket.

This action supports list pagination and does not return more than 100 configurations at a time. You
should always check the `IsTruncated` element in the response. If there are no more
configurations to list, `IsTruncated` is set to false. If there are more configurations to
list, `IsTruncated` is set to true, and there will be a value in
`NextContinuationToken`. You use the `NextContinuationToken` value to continue
the pagination of the list by passing the value in continuation-token in the request to `GET`
the next page.

To use this operation, you must have permissions to perform the
`s3:GetAnalyticsConfiguration` action. The bucket owner has this permission by default. The
bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3
Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

For information about Amazon S3 analytics feature, see [Amazon S3 Analytics – Storage Class
Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html).

The following operations are related to `ListBucketAnalyticsConfigurations`:

- [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html)
- [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html)
- [PutBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListBucketAnalyticsConfigurationsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket from which analytics configurations are retrieved.

### `ContinuationToken` — string · sent as query `continuation-token`

The `ContinuationToken` that represents a placeholder from where this request should
begin.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`ListBucketAnalyticsConfigurationsOutput`)

### `IsTruncated` — boolean

Indicates whether the returned list of analytics configurations is complete. A value of true
indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent
request.

### `ContinuationToken` — string

The marker that is used as a starting point for this analytics configuration list response. This
value is present if it was sent in the request.

### `NextContinuationToken` — string

`NextContinuationToken` is sent when `isTruncated` is true, which indicates
that there are more analytics configurations to list. The next request must include this
`NextContinuationToken`. The token is obfuscated and is not a usable value.

### `AnalyticsConfigurationList` — list<AnalyticsConfiguration>

The list of analytics configurations for a bucket.
