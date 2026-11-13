# HeadBucket

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `HeadBucketCommand` from `@aws-sdk/client-s3` · HTTP: `HEAD /{Bucket}`

You can use this operation to determine if a bucket exists and if you have permission to access it.
The action returns a `200 OK` HTTP status code if the bucket exists and you have
permission to access it. You can make a `HeadBucket` call on any bucket name to any
Region in the partition, and regardless of the permissions on the bucket, you will receive a
response header with the correct bucket location so that you can then make a proper, signed request
to the appropriate Regional endpoint.

If the bucket doesn't exist or you don't have permission to access it, the `HEAD`
request returns a generic `400 Bad Request`, `403 Forbidden`, or
`404 Not Found` HTTP status code. A message body isn't included, so you can't determine
the exception beyond these HTTP response codes.

Authentication and authorization
:   **General purpose buckets** - Request to public buckets that
    grant the s3:ListBucket permission publicly do not need to be signed. All other
    `HeadBucket` requests must be authenticated and signed by using IAM credentials
    (access key ID and secret access key for the IAM identities). All headers with the
    `x-amz-` prefix, including `x-amz-copy-source`, must be signed. For more
    information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html).

    **Directory buckets** - You must use IAM credentials to
    authenticate and authorize your access to the `HeadBucket` API operation, instead of
    using the temporary security credentials through the `CreateSession` API
    operation.

    Amazon Web Services CLI or SDKs handles authentication and authorization on your behalf.

Permissions
:   - **General purpose bucket permissions** - To use this
      operation, you must have permissions to perform the `s3:ListBucket` action. The
      bucket owner has this permission by default and can grant this permission to others. For more
      information about permissions, see [Managing access permissions to your
      Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - You must have the
      **`s3express:CreateSession`** permission in the
      `Action` element of a policy. If no session mode is specified, the session will be
      created with the maximum allowable privilege, attempting `ReadWrite` first,
      then `ReadOnly` if `ReadWrite` is not permitted. If you want to explicitly
      restrict the access to be read-only, you can set the `s3express:SessionMode` condition key to
      `ReadOnly` on the bucket.

      For more information about example bucket policies, see [Example
      bucket policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) and [Amazon Web Services
      Identity and Access Management (IAM) identity-based policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-identity-policies.html) in the
      *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

    You must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
    *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
    *Amazon S3 User Guide*.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`HeadBucketRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

**Object Lambda access points** - When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`HeadBucketOutput`)

### `BucketArn` — string · sent as header `x-amz-bucket-arn`

The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all
of Amazon Web Services.

This parameter is only supported for S3 directory buckets. For more information, see [Using tags with
directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).

### `BucketLocationType` — LocationType (enum) · sent as header `x-amz-bucket-location-type`

The type of location where the bucket is created.

This functionality is only supported by directory buckets.

Values: `AvailabilityZone`, `LocalZone`

### `BucketLocationName` — string · sent as header `x-amz-bucket-location-name`

The name of the location where the bucket will be created.

For directory buckets, the Zone ID of the Availability Zone or the Local Zone where the bucket is created. An example
Zone ID value for an Availability Zone is `usw2-az1`.

This functionality is only supported by directory buckets.

### `BucketRegion` — string · sent as header `x-amz-bucket-region`

The Region that the bucket is located.

### `AccessPointAlias` — boolean · sent as header `x-amz-access-point-alias`

Indicates whether the bucket name used in the request is an access point alias.

For directory buckets, the value of this field is `false`.

## Errors

- `NotFound` — The specified content does not exist.

## Examples

### To determine if bucket exists

This operation checks to see if a bucket exists.

Input:

```json
{
  "Bucket": "acl1"
}
```
