# ListBucketIntelligentTieringConfigurations

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListBucketIntelligentTieringConfigurationsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?intelligent-tiering&x-id=ListBucketIntelligentTieringConfigurations`

This operation is not supported for directory buckets.

Lists the S3 Intelligent-Tiering configuration from the specified bucket.

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective storage access tier, without performance impact or operational overhead. S3 Intelligent-Tiering delivers automatic cost savings in three low latency and high throughput access tiers. To get the lowest storage cost on data that can be accessed in minutes to hours, you can choose to activate additional archiving capabilities.

The S3 Intelligent-Tiering storage class is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. If the size of an object is less than 128 KB, it is not monitored and not eligible for auto-tiering. Smaller objects can be stored, but they are always charged at the Frequent Access tier rates in the S3 Intelligent-Tiering storage class.

For more information, see [Storage class for automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

Operations related to `ListBucketIntelligentTieringConfigurations` include:

- [DeleteBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html)
- [PutBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)
- [GetBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListBucketIntelligentTieringConfigurationsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.

### `ContinuationToken` — string · sent as query `continuation-token`

The `ContinuationToken` that represents a placeholder from where this request should
begin.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`ListBucketIntelligentTieringConfigurationsOutput`)

### `IsTruncated` — boolean

Indicates whether the returned list of analytics configurations is complete. A value of
`true` indicates that the list is not complete and the `NextContinuationToken`
will be provided for a subsequent request.

### `ContinuationToken` — string

The `ContinuationToken` that represents a placeholder from where this request should
begin.

### `NextContinuationToken` — string

The marker used to continue this inventory configuration listing. Use the
`NextContinuationToken` from this response to continue the listing in a subsequent request.
The continuation token is an opaque value that Amazon S3 understands.

### `IntelligentTieringConfigurationList` — list<IntelligentTieringConfiguration>

The list of S3 Intelligent-Tiering configurations for a bucket.
