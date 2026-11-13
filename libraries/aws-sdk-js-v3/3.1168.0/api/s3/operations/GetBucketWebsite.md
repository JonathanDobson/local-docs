# GetBucketWebsite

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketWebsiteCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?website`

This operation is not supported for directory buckets.

Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a bucket
as website by adding a website configuration. For more information about hosting websites, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

This GET action requires the `S3:GetBucketWebsite` permission. By default, only the
bucket owner can read the bucket website configuration. However, bucket owners can allow other users to
read the website configuration by writing a bucket policy granting them the
`S3:GetBucketWebsite` permission.

The following operations are related to `GetBucketWebsite`:

- [DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html)
- [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketWebsiteRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name for which to get the website configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketWebsiteOutput`)

### `RedirectAllRequestsTo` — RedirectAllRequestsTo

Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

### `IndexDocument` — IndexDocument

The name of the index document for the website (for example `index.html`).

### `ErrorDocument` — ErrorDocument

The object key name of the website error document to use for 4XX class errors.

### `RoutingRules` — list<RoutingRule>

Rules that define when a redirect is applied and the redirect behavior.

## Examples

### To get bucket website configuration

The following example retrieves website configuration of a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "IndexDocument": {
    "Suffix": "index.html"
  },
  "ErrorDocument": {
    "Key": "error.html"
  }
}
```
