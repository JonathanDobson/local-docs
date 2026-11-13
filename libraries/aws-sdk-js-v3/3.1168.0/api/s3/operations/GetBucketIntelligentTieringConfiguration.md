# GetBucketIntelligentTieringConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketIntelligentTieringConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?intelligent-tiering&x-id=GetBucketIntelligentTieringConfiguration`

This operation is not supported for directory buckets.

Gets the S3 Intelligent-Tiering configuration from the specified bucket.

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective storage access tier, without performance impact or operational overhead. S3 Intelligent-Tiering delivers automatic cost savings in three low latency and high throughput access tiers. To get the lowest storage cost on data that can be accessed in minutes to hours, you can choose to activate additional archiving capabilities.

The S3 Intelligent-Tiering storage class is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. If the size of an object is less than 128 KB, it is not monitored and not eligible for auto-tiering. Smaller objects can be stored, but they are always charged at the Frequent Access tier rates in the S3 Intelligent-Tiering storage class.

For more information, see [Storage class for automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

Operations related to `GetBucketIntelligentTieringConfiguration` include:

- [DeleteBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html)
- [PutBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)
- [ListBucketIntelligentTieringConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketIntelligentTieringConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.

### `Id` — string · **required** · sent as query `id`

The ID used to identify the S3 Intelligent-Tiering configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketIntelligentTieringConfigurationOutput`)

### `IntelligentTieringConfiguration` — IntelligentTieringConfiguration · sent as httpPayload

Container for S3 Intelligent-Tiering configuration.
