# GetBucketRequestPayment

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketRequestPaymentCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?requestPayment`

This operation is not supported for directory buckets.

Returns the request payment configuration of a bucket. To use this version of the operation, you
must be the bucket owner. For more information, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html).

The following operations are related to `GetBucketRequestPayment`:

- [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketRequestPaymentRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the payment request configuration

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketRequestPaymentOutput`)

### `Payer` — Payer (enum)

Specifies who pays for the download and request fees.

Values: `Requester`, `BucketOwner`

## Examples

### To get bucket versioning configuration

The following example retrieves bucket versioning configuration.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "Payer": "BucketOwner"
}
```
