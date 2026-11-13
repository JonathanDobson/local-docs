# PutBucketNotificationConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketNotificationConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?notification`

This operation is not supported for directory buckets.

Enables notifications of specified events for a bucket. For more information about event
notifications, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).

Using this API, you can replace an existing notification configuration. The configuration is an XML
file that defines the event types that you want Amazon S3 to publish and the destination where you want Amazon S3
to publish an event notification when it detects an event of the specified type.

By default, your bucket has no event notifications configured. That is, the notification
configuration will be an empty `NotificationConfiguration`.

This action replaces the existing notification configuration with the configuration you include in
the request body.

After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification Service
(Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the bucket owner
has permission to publish to it by sending a test notification. In the case of Lambda destinations,
Amazon S3 verifies that the Lambda function permissions grant Amazon S3 permission to invoke the function from the
Amazon S3 bucket. For more information, see [Configuring Notifications for Amazon S3
Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).

You can disable notifications by adding the empty NotificationConfiguration element.

For more information about the number of event notification configurations that you can create per
bucket, see [Amazon S3 service
quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3) in *Amazon Web Services General Reference*.

By default, only the bucket owner can configure notifications on a bucket. However, bucket owners
can use a bucket policy to grant permission to other users to set this configuration with the required
`s3:PutBucketNotification` permission.

The PUT notification is an atomic operation. For example, suppose your notification configuration
includes SNS topic, SQS queue, and Lambda function configurations. When you send a PUT request with
this configuration, Amazon S3 sends test messages to your SNS topic. If the message fails, the entire PUT
action will fail, and Amazon S3 will not add the configuration to your bucket.

If the configuration in the request body includes only one `TopicConfiguration`
specifying only the `s3:ReducedRedundancyLostObject` event type, the response will also
include the `x-amz-sns-test-message-id` header containing the message ID of the test
notification sent to the topic.

The following action is related to `PutBucketNotificationConfiguration`:

- [GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketNotificationConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket.

### `NotificationConfiguration` — NotificationConfiguration · **required** · sent as httpPayload

A container for specifying the notification configuration of the bucket. If this element is empty,
notifications are turned off for the bucket.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `SkipDestinationValidation` — boolean · sent as header `x-amz-skip-destination-validation`

Skips validation of Amazon SQS, Amazon SNS, and Lambda destinations.
True or false value.

## Output (`Unit`)

_None._

## Examples

### Set notification configuration for a bucket

The following example sets notification configuration on a bucket to publish the object created events to an SNS topic.

Input:

```json
{
  "Bucket": "examplebucket",
  "NotificationConfiguration": {
    "TopicConfigurations": [
      {
        "TopicArn": "arn:aws:sns:us-west-2:123456789012:s3-notification-topic",
        "Events": [
          "s3:ObjectCreated:*"
        ]
      }
    ]
  }
}
```
