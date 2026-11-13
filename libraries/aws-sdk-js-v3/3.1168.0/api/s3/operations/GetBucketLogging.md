# GetBucketLogging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketLoggingCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?logging`

This operation is not supported for directory buckets.

Returns the logging status of a bucket and the permissions users have to view and modify that
status.

The following operations are related to `GetBucketLogging`:

- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [PutBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketLoggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name for which to get the logging information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketLoggingOutput`)

### `LoggingEnabled` — LoggingEnabled

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a
bucket. For more information, see [PUT Bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html) in the
*Amazon S3 API Reference*.
