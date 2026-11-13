# DeleteObjectTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteObjectTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}/{Key+}?tagging`

This operation is not supported for directory buckets.

Removes the entire tag set from the specified object. For more information about managing object
tags, see  [Object
Tagging](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html).

To use this operation, you must have permission to perform the `s3:DeleteObjectTagging`
action.

To delete tags of a specific object version, add the `versionId` query parameter in the
request. You will need permission for the `s3:DeleteObjectVersionTagging` action.

The following operations are related to `DeleteObjectTagging`:

- [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)
- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteObjectTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name containing the objects from which to remove the tags.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

The key that identifies the object in the bucket from which to remove all tags.

### `VersionId` — string · sent as query `versionId`

The versionId of the object that the tag-set will be removed from.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`DeleteObjectTaggingOutput`)

### `VersionId` — string · sent as header `x-amz-version-id`

The versionId of the object the tag-set was removed from.

## Examples

### To remove tag set from an object

The following example removes tag set associated with the specified object. If the bucket is versioning enabled, the operation removes tag set from the latest object version.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg"
}
```

Output:

```json
{
  "VersionId": "null"
}
```

### To remove tag set from an object version

The following example removes tag set associated with the specified object version. The request specifies both the object key and object version.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg",
  "VersionId": "ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI"
}
```

Output:

```json
{
  "VersionId": "ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI"
}
```
