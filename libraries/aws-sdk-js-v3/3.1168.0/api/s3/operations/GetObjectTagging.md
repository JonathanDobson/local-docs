# GetObjectTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetObjectTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?tagging`

This operation is not supported for directory buckets.

Returns the tag-set of an object. You send the GET request against the tagging subresource
associated with the object.

To use this operation, you must have permission to perform the `s3:GetObjectTagging`
action. By default, the GET action returns information about current version of an object. For a
versioned bucket, you can have multiple versions of an object in your bucket. To retrieve tags of any
other version, use the versionId query parameter. You also need permission for the
`s3:GetObjectVersionTagging` action.

By default, the bucket owner has this permission and can grant this permission to others.

For information about the Amazon S3 object tagging feature, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html).

The following actions are related to `GetObjectTagging`:

- [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
- [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetObjectTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name containing the object for which to get the tagging information.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Object key for which to get the tagging information.

### `VersionId` — string · sent as query `versionId`

The versionId of the object for which to get the tagging information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Output (`GetObjectTaggingOutput`)

### `VersionId` — string · sent as header `x-amz-version-id`

The versionId of the object for which you got the tagging information.

### `TagSet` — list<Tag> · **required**

Contains the tag set.

## Examples

### To retrieve tag set of a specific object version

The following example retrieves tag set of an object. The request specifies object version.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "exampleobject",
  "VersionId": "ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI"
}
```

Output:

```json
{
  "VersionId": "ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI",
  "TagSet": [
    {
      "Value": "Value1",
      "Key": "Key1"
    }
  ]
}
```

### To retrieve tag set of an object

The following example retrieves tag set of an object.

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
  "VersionId": "null",
  "TagSet": [
    {
      "Value": "Value4",
      "Key": "Key4"
    },
    {
      "Value": "Value3",
      "Key": "Key3"
    }
  ]
}
```
