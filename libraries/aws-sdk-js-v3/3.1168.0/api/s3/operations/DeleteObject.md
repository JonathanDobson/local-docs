# DeleteObject

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteObjectCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}/{Key+}?x-id=DeleteObject`

Removes an object from a bucket. The behavior depends on the bucket's versioning state:

- If bucket versioning is not enabled, the operation permanently deletes the object.
- If bucket versioning is enabled, the operation inserts a delete marker, which becomes the
  current version of the object. To permanently delete an object in a versioned bucket, you must
  include the object’s `versionId` in the request. For more information about
  versioning-enabled buckets, see [Deleting object versions from a
  versioning-enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html).
- If bucket versioning is suspended, the operation removes the object that has a null
  `versionId`, if there is one, and inserts a delete marker that becomes the current
  version of the object. If there isn't an object with a null `versionId`, and all versions
  of the object have a `versionId`, Amazon S3 does not remove the object and only inserts a
  delete marker. To permanently delete an object that has a `versionId`, you must include
  the object’s `versionId` in the request. For more information about versioning-suspended
  buckets, see [Deleting
  objects from versioning-suspended buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectsfromVersioningSuspendedBuckets.html).

- **Directory buckets** - S3 Versioning isn't enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets.
  You can only specify `null` to the `versionId` query parameter in the
  request.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
  *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
  *Amazon S3 User Guide*.

To remove a specific version, you must use the `versionId` query parameter. Using this
query parameter permanently deletes the version. If the object deleted is a delete marker, Amazon S3 sets the
response header `x-amz-delete-marker` to true.

If the object you want to delete is in a bucket where the bucket versioning configuration is MFA
Delete enabled, you must include the `x-amz-mfa` request header in the DELETE
`versionId` request. Requests that include `x-amz-mfa` must use HTTPS. For more
information about MFA Delete, see [Using MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html) in the *Amazon S3 User
Guide*. To see sample requests that use versioning, see [Sample Request](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectDELETE.html#ExampleVersionObjectDelete).

**Directory buckets** - MFA delete is not supported by directory buckets.

You can delete objects by explicitly calling DELETE Object or calling ([PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html)) to enable Amazon S3 to
remove them for you. If you want to block users or accounts from removing or deleting objects from your
bucket, you must deny them the `s3:DeleteObject`, `s3:DeleteObjectVersion`, and
`s3:PutLifeCycleConfiguration` actions.

**Directory buckets** -
S3 Lifecycle is not supported by directory buckets.

Permissions
:   - **General purpose bucket permissions** - The following
      permissions are required in your policies when your `DeleteObjects` request
      includes specific headers.

      - **`s3:DeleteObject`** - To
        delete an object from a bucket, you must always have the
        `s3:DeleteObject` permission.
      - **`s3:DeleteObjectVersion`** - To delete a specific version of an object from a versioning-enabled
        bucket, you must have the `s3:DeleteObjectVersion` permission.

        If the `s3:DeleteObject` or `s3:DeleteObjectVersion` permissions are explicitly
        denied in your bucket policy, attempts to delete any unversioned objects
        result in a `403 Access Denied` error.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following action is related to `DeleteObject`:

- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

The `If-Match` header is supported for both general purpose and directory buckets. `IfMatchLastModifiedTime` and `IfMatchSize` is only supported for directory buckets.

## Input (`DeleteObjectRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name of the bucket containing the object.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Key name of the object to delete.

### `MFA` — string · sent as header `x-amz-mfa`

The concatenation of the authentication device's serial number, a space, and the value that is
displayed on your authentication device. Required to permanently delete a versioned object if versioning
is configured with MFA delete enabled.

This functionality is not supported for directory buckets.

### `VersionId` — string · sent as query `versionId`

Version ID used to reference a specific version of the object.

For directory buckets in this API operation, only the `null` value of the version ID is supported.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `BypassGovernanceRetention` — boolean · sent as header `x-amz-bypass-governance-retention`

Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this
operation. To use this header, you must have the `s3:BypassGovernanceRetention`
permission.

This functionality is not supported for directory buckets.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `IfMatch` — string · sent as header `If-Match`

Deletes the object if the ETag (entity tag) value provided during the delete operation matches the ETag of the object in S3.
If the ETag values do not match, the operation returns a `412 Precondition Failed` error.

Expects the ETag value as a string. `If-Match` does accept a string value of an '\*' (asterisk) character to denote a match of any ETag.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232).

### `IfMatchLastModifiedTime` — timestamp · sent as header `x-amz-if-match-last-modified-time`

If present, the object is deleted only if its modification times matches the provided
`Timestamp`. If the `Timestamp` values do not match, the operation returns a
`412 Precondition Failed` error. If the `Timestamp` matches or if the object
doesn’t exist, the operation returns a `204 Success (No Content)` response.

This functionality is only supported for directory buckets.

### `IfMatchSize` — long · sent as header `x-amz-if-match-size`

If present, the object is deleted only if its size matches the provided size in bytes. If the
`Size` value does not match, the operation returns a `412 Precondition Failed`
error. If the `Size` matches or if the object doesn’t exist, the operation returns a
`204 Success (No Content)` response.

This functionality is only supported for directory buckets.

You can use the `If-Match`, `x-amz-if-match-last-modified-time` and
`x-amz-if-match-size` conditional headers in conjunction with each-other or
individually.

## Output (`DeleteObjectOutput`)

### `DeleteMarker` — boolean · sent as header `x-amz-delete-marker`

Indicates whether the specified object version that was permanently deleted was (true) or was not
(false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not
(false) the current version of the object is a delete marker. To learn more about delete markers, see
[Working with delete
markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).

This functionality is not supported for directory buckets.

### `VersionId` — string · sent as header `x-amz-version-id`

Returns the version ID of the delete marker created as a result of the DELETE operation.

This functionality is not supported for directory buckets.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### To delete an object (from a non-versioned bucket)

The following example deletes an object from a non-versioned bucket.

Input:

```json
{
  "Bucket": "ExampleBucket",
  "Key": "HappyFace.jpg"
}
```

### To delete an object

The following example deletes an object from an S3 bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "objectkey.jpg"
}
```
