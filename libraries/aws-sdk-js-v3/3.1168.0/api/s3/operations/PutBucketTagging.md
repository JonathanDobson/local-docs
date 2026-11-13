# PutBucketTagging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketTaggingCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?tagging`

This operation is not supported for directory buckets.

Sets the tags for a general purpose bucket if attribute based access control (ABAC) is not enabled for the bucket. When you [enable ABAC for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html), you can no longer use this operation for that bucket and must use the [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) operations instead.

Use tags to organize your Amazon Web Services bill to reflect your own cost structure. To do this, sign up to get
your Amazon Web Services account bill with tag key values included. Then, to see the cost of combined resources,
organize your billing information according to resources with the same tag key values. For example, you
can tag several resources with a specific application name, and then organize your billing information
to see the total cost of that application across several services. For more information, see [Cost Allocation and
Tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) and [Using Cost Allocation in Amazon S3 Bucket Tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html).

When this operation sets the tags for a bucket, it will overwrite any current tags the bucket
already has. You cannot use this operation to add tags to an existing list of tags.

To use this operation, you must have permissions to perform the `s3:PutBucketTagging`
action. The bucket owner has this permission by default and can grant this permission to others. For
more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3
Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

`PutBucketTagging` has the following special errors. For more Amazon S3 errors see, [Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).

- `InvalidTag` - The tag provided was not a valid tag. This error can occur if
  the tag did not pass input validation. For more information, see [Using Cost Allocation in Amazon S3 Bucket
  Tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html).
- `MalformedXML` - The XML provided does not match the schema.
- `OperationAborted` - A conflicting conditional action is currently in progress
  against this resource. Please try again.
- `InternalError` - The service was unable to apply the provided tag to the
  bucket.

The following operations are related to `PutBucketTagging`:

- [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)
- [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketTaggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
message integrity check to verify that the request body was not corrupted in transit. For more
information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt).

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `Tagging` — Tagging · **required** · sent as httpPayload

Container for the `TagSet` and `Tag` elements.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set tags on a bucket

The following example sets tags on a bucket. Any existing tags are replaced.

Input:

```json
{
  "Bucket": "examplebucket",
  "Tagging": {
    "TagSet": [
      {
        "Key": "Key1",
        "Value": "Value1"
      },
      {
        "Key": "Key2",
        "Value": "Value2"
      }
    ]
  }
}
```
