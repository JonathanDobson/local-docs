# DeleteBucketCors

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteBucketCorsCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}?cors`

This operation is not supported for directory buckets.

Deletes the `cors` configuration information set for the bucket.

To use this operation, you must have permission to perform the `s3:PutBucketCORS` action.
The bucket owner has this permission by default and can grant this permission to others.

For information about `cors`, see [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the
*Amazon S3 User Guide*.

**Related Resources**

- [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html)
- [RESTOPTIONSobject](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTOPTIONSobject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteBucketCorsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

Specifies the bucket whose `cors` configuration is being deleted.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### To delete cors configuration on a bucket.

The following example deletes CORS configuration on a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```
