# GetBucketLocation

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketLocationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?location`

Using the `GetBucketLocation` operation is no longer a best practice. To return the
Region that a bucket resides in, we recommend that you use the
[HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
operation instead. For backward compatibility, Amazon S3 continues to support the
`GetBucketLocation` operation.

Returns the Region the bucket resides in. You set the bucket's Region using the
`LocationConstraint` request parameter in a `CreateBucket` request. For more
information, see [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html).

In a bucket's home Region, calls to the `GetBucketLocation` operation are governed
by the bucket's policy. In other Regions, the bucket policy doesn't apply, which means that
cross-account access won't be authorized. However, calls to the `HeadBucket` operation
always return the bucket’s location through an HTTP response header, whether access to the bucket
is authorized or not. Therefore, we recommend using the `HeadBucket` operation for
bucket Region discovery and to avoid using the `GetBucketLocation` operation.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

This operation is not supported for directory buckets.

The following operations are related to `GetBucketLocation`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketLocationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the location.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketLocationOutput`)

### `LocationConstraint` — BucketLocationConstraint (enum)

Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported location
constraints by Region, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

Buckets in Region `us-east-1` have a LocationConstraint of `null`. Buckets
with a LocationConstraint of `EU` reside in `eu-west-1`.

Values: `af-south-1`, `ap-east-1`, `ap-east-2`, `ap-northeast-1`, `ap-northeast-2`, `ap-northeast-3`, `ap-south-1`, `ap-south-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-4`, `ap-southeast-5`, `ap-southeast-6`, `ap-southeast-7`, `ca-central-1`, `ca-west-1`, `cn-north-1`, `cn-northwest-1`, `EU`, `eu-central-1`, `eu-central-2`, `eu-north-1`, `eu-south-1`, `eu-south-2`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `il-central-1`, `me-central-1`, `me-south-1`, `mx-central-1`, `sa-east-1`, `us-east-2`, `us-gov-east-1`, `us-gov-west-1`, `us-west-1`, `us-west-2`

## Examples

### To get bucket location

The following example returns bucket location.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "LocationConstraint": "us-west-2"
}
```
