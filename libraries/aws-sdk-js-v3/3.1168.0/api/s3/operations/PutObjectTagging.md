# PutObjectTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutObjectTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?tagging`

This operation is not supported for directory buckets.

Sets the supplied tag-set to an object that already exists in a bucket. A tag is a key-value pair.
For more information, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html).

You can associate tags with an object by sending a PUT request against the tagging subresource that
is associated with the object. You can retrieve tags by sending a GET request. For more information, see
[GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html).

For tagging-related restrictions related to characters and encodings, see [Tag
Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html). Note that Amazon S3 limits the maximum number of tags to 10 tags per object.

To use this operation, you must have permission to perform the `s3:PutObjectTagging`
action. By default, the bucket owner has this permission and can grant this permission to others.

To put tags of any other version, use the `versionId` query parameter. You also need
permission for the `s3:PutObjectVersionTagging` action.

`PutObjectTagging` has the following special errors. For more Amazon S3 errors see, [Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).

- `InvalidTag` - The tag provided was not a valid tag. This error can occur if
  the tag did not pass input validation. For more information, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html).
- `MalformedXML` - The XML provided does not match the schema.
- `OperationAborted` - A conflicting conditional action is currently in progress
  against this resource. Please try again.
- `InternalError` - The service was unable to apply the provided tag to the
  object.

The following operations are related to `PutObjectTagging`:

- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)
- [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutObjectTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name containing the object.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Name of the object key.

### `VersionId` — string · sent as query `versionId`

The versionId of the object that the tag-set will be added to.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash for the request body.

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `Tagging` — Tagging · **required** · sent as httpPayload

Container for the `TagSet` and `Tag` elements

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that she or he will be charged for the tagging object
request. Bucket owners need not specify this parameter in their requests.

Values: `requester`

## Output (`PutObjectTaggingOutput`)

### `VersionId` — string · sent as header `x-amz-version-id`

The versionId of the object the tag-set was added to.

## Examples

### To add tags to an existing object

The following example adds tags to an existing object.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg",
  "Tagging": {
    "TagSet": [
      {
        "Key": "Key3",
        "Value": "Value3"
      },
      {
        "Key": "Key4",
        "Value": "Value4"
      }
    ]
  }
}
```

Output:

```json
{
  "VersionId": "null"
}
```
