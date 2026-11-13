# GetBucketNotificationConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketNotificationConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?notification`

This operation is not supported for directory buckets.

Returns the notification configuration of a bucket.

If notifications are not enabled on the bucket, the action returns an empty
`NotificationConfiguration` element.

By default, you must be the bucket owner to read the notification configuration of a bucket.
However, the bucket owner can use a bucket policy to grant permission to other users to read this
configuration with the `s3:GetBucketNotification` permission.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

For more information about setting and reading the notification configuration on a bucket, see
[Setting Up Notification
of Bucket Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html). For more information about bucket policies, see [Using Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).

The following action is related to `GetBucketNotification`:

- [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketNotificationConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the notification configuration.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`NotificationConfiguration`)

### `TopicConfigurations` — list<TopicConfiguration>

The topic to which notifications are sent and the events for which notifications are
generated.

### `QueueConfigurations` — list<QueueConfiguration>

The Amazon Simple Queue Service queues to publish messages to and the events for which to publish
messages.

### `LambdaFunctionConfigurations` — list<LambdaFunctionConfiguration>

Describes the Lambda functions to invoke and the events for which to invoke them.

### `EventBridgeConfiguration` — EventBridgeConfiguration

Enables delivery of events to Amazon EventBridge.
