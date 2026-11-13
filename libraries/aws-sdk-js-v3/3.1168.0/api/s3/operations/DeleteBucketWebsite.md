# DeleteBucketWebsite

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketWebsiteCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?website`

This operation is not supported for directory buckets.

This action removes the website configuration for a bucket. Amazon S3 returns a `200 OK`
response upon successfully deleting a website configuration on the specified bucket. You will get a
`200 OK` response if the website configuration you are trying to delete does not exist on
the bucket. Amazon S3 returns a `404` response if the bucket specified in the request does not
exist.

This DELETE action requires the `S3:DeleteBucketWebsite` permission. By default, only the
bucket owner can delete the website configuration attached to a bucket. However, bucket owners can grant
other users permission to delete the website configuration by writing a bucket policy granting them the
`S3:DeleteBucketWebsite` permission.

For more information about hosting websites, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

The following operations are related to `DeleteBucketWebsite`:

- [GetBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html)
- [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketWebsiteRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name for which you want to remove the website configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### To delete bucket website configuration

The following example deletes bucket website configuration.

Input:

```json
{
  "Bucket": "examplebucket"
}
```
