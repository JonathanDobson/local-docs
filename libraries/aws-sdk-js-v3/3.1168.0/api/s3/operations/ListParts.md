# ListParts

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListPartsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?x-id=ListParts` · Paginated (token `PartNumberMarker` → `NextPartNumberMarker`)

Lists the parts that have been uploaded for a specific multipart upload.

To use this operation, you must provide the `upload ID` in the request. You obtain this
uploadID by sending the initiate multipart upload request through [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html).

The `ListParts` request returns a maximum of 1,000 uploaded parts. The limit of 1,000
parts is also the default value. You can restrict the number of parts in a response by specifying the
`max-parts` request parameter. If your multipart upload consists of more than 1,000 parts,
the response returns an `IsTruncated` field with the value of `true`, and a
`NextPartNumberMarker` element. To list remaining uploaded parts, in subsequent
`ListParts` requests, include the `part-number-marker` query string parameter
and set its value to the `NextPartNumberMarker` field value from the previous
response.

For more information on multipart uploads, see [Uploading Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) in
the *Amazon S3 User Guide*.

**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   - **General purpose bucket permissions** - For information
      about permissions required to use the multipart upload API, see [Multipart Upload and Permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html) in
      the *Amazon S3 User Guide*.

      If the upload was created using server-side encryption with Key Management Service (KMS) keys
      (SSE-KMS) or dual-layer server-side encryption with Amazon Web Services KMS keys (DSSE-KMS), you must have
      permission to the `kms:Decrypt` action for the `ListParts` request to
      succeed.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following operations are related to `ListParts`:

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListPartsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket to which the parts are being uploaded.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Object key for which the multipart upload was initiated.

### `MaxParts` — integer · sent as query `max-parts`

Sets the maximum number of parts to return.

### `PartNumberMarker` — string · sent as query `part-number-marker`

Specifies the part after which listing should begin. Only parts with higher part numbers will be
listed.

### `UploadId` — string · **required** · sent as query `uploadId`

Upload ID identifying the multipart upload whose parts are being listed.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created
using a checksum algorithm. For more information,
see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

### `SSECustomerKey` — string · sent as header `x-amz-server-side-encryption-customer-key`

The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm.
For more information, see
[Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

### `SSECustomerKeyMD5` — string · sent as header `x-amz-server-side-encryption-customer-key-MD5`

The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum
algorithm. For more information,
see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

## Output (`ListPartsOutput`)

### `AbortDate` — timestamp · sent as header `x-amz-abort-date`

If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads
and the prefix in the lifecycle rule matches the object name in the request, then the response includes
this header indicating when the initiated multipart upload will become eligible for abort operation. For
more information, see [Aborting
Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config).

The response will also include the `x-amz-abort-rule-id` header that will provide the ID
of the lifecycle configuration rule that defines this action.

This functionality is not supported for directory buckets.

### `AbortRuleId` — string · sent as header `x-amz-abort-rule-id`

This header is returned along with the `x-amz-abort-date` header. It identifies
applicable lifecycle configuration rule that defines the action to abort incomplete multipart
uploads.

This functionality is not supported for directory buckets.

### `Bucket` — string

The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or
access point alias if used.

### `Key` — string

Object key for which the multipart upload was initiated.

### `UploadId` — string

Upload ID identifying the multipart upload whose parts are being listed.

### `PartNumberMarker` — string

Specifies the part after which listing should begin. Only parts with higher part numbers will be
listed.

### `NextPartNumberMarker` — string

When a list is truncated, this element specifies the last part in the list, as well as the value to
use for the `part-number-marker` request parameter in a subsequent request.

### `MaxParts` — integer

Maximum number of parts that were allowed in the response.

### `IsTruncated` — boolean

Indicates whether the returned list of parts is truncated. A true value indicates that the list was
truncated. A list can be truncated if the number of parts exceeds the limit returned in the MaxParts
element.

### `Parts` — list<Part>

Container for elements related to a particular part. A response can contain zero or more
`Part` elements.

### `Initiator` — Initiator

Container element that identifies who initiated the multipart upload. If the initiator is an
Amazon Web Services account, this element provides the same information as the `Owner` element. If the
initiator is an IAM User, this element provides the user ARN.

### `Owner` — Owner

Container element that identifies the object owner, after the object is created. If multipart upload
is initiated by an IAM user, this element provides the parent account ID.

**Directory buckets** - The bucket owner is returned as the
object owner for all the parts.

### `StorageClass` — StorageClass (enum)

The class of storage used to store the uploaded object.

**Directory buckets** -
Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum)

The algorithm that was used to create a checksum of the object.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ChecksumType` — ChecksumType (enum)

The checksum type, which determines how part-level checksums are combined to create an object-level
checksum for multipart objects. You can use this header response to verify that the checksum type that
is received is the same checksum type that was specified in `CreateMultipartUpload` request.
For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

Values: `COMPOSITE`, `FULL_OBJECT`

## Examples

### To list parts of a multipart upload.

The following example lists parts uploaded for a specific multipart upload.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "bigobject",
  "UploadId": "example7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--"
}
```

Output:

```json
{
  "Owner": {
    "DisplayName": "owner-display-name",
    "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
  },
  "Initiator": {
    "DisplayName": "owner-display-name",
    "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
  },
  "Parts": [
    {
      "LastModified": "2016-12-16T00:11:42.000Z",
      "PartNumber": 1,
      "ETag": "\"d8c2eafd90c266e19ab9dcacc479f8af\"",
      "Size": 26246026
    },
    {
      "LastModified": "2016-12-16T00:15:01.000Z",
      "PartNumber": 2,
      "ETag": "\"d8c2eafd90c266e19ab9dcacc479f8af\"",
      "Size": 26246026
    }
  ],
  "StorageClass": "STANDARD"
}
```
