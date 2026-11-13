# DeleteBucketTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?tagging`

This operation is not supported for directory buckets.

Deletes tags from the general purpose bucket if attribute based access control (ABAC) is not enabled for the bucket. When you [enable ABAC for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html), you can no longer use this operation for that bucket and must use [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) instead.

To use this operation, you must have permission to perform the `s3:PutBucketTagging`
action. By default, the bucket owner has this permission and can grant this permission to others.

The following operations are related to `DeleteBucketTagging`:

- [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)
- [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket that has the tag set to be removed.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### To delete bucket tags

The following example deletes bucket tags.

Input:

```json
{
  "Bucket": "examplebucket"
}
```
