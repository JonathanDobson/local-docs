# GetBucketVersioning

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketVersioningCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?versioning`

This operation is not supported for directory buckets.

Returns the versioning state of a bucket.

To retrieve the versioning state of a bucket, you must be the bucket owner.

This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete
status is `enabled`, the bucket owner must use an authentication device to change the
versioning state of the bucket.

The following operations are related to `GetBucketVersioning`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketVersioningRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the versioning information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketVersioningOutput`)

### `Status` — BucketVersioningStatus (enum)

The versioning state of the bucket.

Values: `Enabled`, `Suspended`

### `MFADelete` — MFADeleteStatus (enum)

Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only
returned if the bucket has been configured with MFA delete. If the bucket has never been so configured,
this element is not returned.

Values: `Enabled`, `Disabled`

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
  "Status": "Enabled",
  "MFADelete": "Disabled"
}
```
