# GetObjectLockConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetObjectLockConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?object-lock`

This operation is not supported for directory buckets.

Gets the Object Lock configuration for a bucket. The rule specified in the Object Lock configuration
will be applied by default to every new object placed in the specified bucket. For more information, see
[Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

The following action is related to `GetObjectLockConfiguration`:

- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetObjectLockConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket whose Object Lock configuration you want to retrieve.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetObjectLockConfigurationOutput`)

### `ObjectLockConfiguration` — ObjectLockConfiguration · sent as httpPayload

The specified bucket's Object Lock configuration.
