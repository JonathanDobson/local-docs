# GetBucketTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?tagging`

This operation is not supported for directory buckets.

Returns the tag set associated with the general purpose bucket.

To use this operation, you must have permission to perform the `s3:GetBucketTagging`
action. By default, the bucket owner has this permission and can grant this permission to others.

`GetBucketTagging` has the following special error:

- Error code: `NoSuchTagSet`

  - Description: There is no tag set associated with the bucket.

The following operations are related to `GetBucketTagging`:

- [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html)
- [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the tagging information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketTaggingOutput`)

### `TagSet` — list<Tag> · **required**

Contains the tag set.

## Examples

### To get tag set associated with a bucket

The following example returns tag set associated with a bucket

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "TagSet": [
    {
      "Value": "value1",
      "Key": "key1"
    },
    {
      "Value": "value2",
      "Key": "key2"
    }
  ]
}
```
