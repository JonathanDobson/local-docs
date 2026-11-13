# DeleteObjects

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteObjectsCommand` from `@aws-sdk/client-s3` · HTTP: `POST /{Bucket}?delete`

This operation enables you to delete multiple objects from a bucket using a single HTTP request. If
you know the object keys that you want to delete, then this operation provides a suitable alternative to
sending individual delete requests, reducing per-request overhead.

The request can contain a list of up to 1,000 keys that you want to delete. In the XML, you provide
the object key names, and optionally, version IDs if you want to delete a specific version of the object
from a versioning-enabled bucket. For each key, Amazon S3 performs a delete operation and returns the result
of that delete, success or failure, in the response. If the object specified in the request isn't found,
Amazon S3 confirms the deletion by returning the result as deleted.

- **Directory buckets** -
  S3 Versioning isn't enabled and supported for directory buckets.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
  *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
  *Amazon S3 User Guide*.

The operation supports two modes for the response: verbose and quiet. By default, the operation uses
verbose mode in which the response includes the result of deletion of each key in your request. In quiet
mode the response includes only keys where the delete operation encountered an error. For a successful
deletion in a quiet mode, the operation does not return any information about the delete in the response
body.

When performing this action on an MFA Delete enabled bucket, that attempts to delete any versioned
objects, you must include an MFA token. If you do not provide one, the entire request will fail, even if
there are non-versioned objects you are trying to delete. If you provide an invalid token, whether there
are versioned keys in the request or not, the entire Multi-Object Delete request will fail. For
information about MFA Delete, see [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete) in the
*Amazon S3 User Guide*.

**Directory buckets** - MFA delete is not supported by directory buckets.

Permissions
:   - **General purpose bucket permissions** - The following
      permissions are required in your policies when your `DeleteObjects` request
      includes specific headers.

      - **`s3:DeleteObject`** - To delete an
        object from a bucket, you must always specify the `s3:DeleteObject`
        permission.
      - **`s3:DeleteObjectVersion`** - To delete a specific version of an object from a versioning-enabled
        bucket, you must specify the `s3:DeleteObjectVersion` permission.

        If the `s3:DeleteObject` or `s3:DeleteObjectVersion` permissions are explicitly
        denied in your bucket policy, attempts to delete any unversioned objects
        result in a `403 Access Denied` error.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

Content-MD5 request header
:   - **General purpose bucket** - The Content-MD5 request header
      is required for all Multi-Object Delete requests. Amazon S3 uses the header value to ensure that
      your request body has not been altered in transit.
    - **Directory bucket** - The Content-MD5 request header
      or a additional checksum request header (including `x-amz-checksum-crc32`,
      `x-amz-checksum-crc32c`, `x-amz-checksum-sha1`, or
      `x-amz-checksum-sha256`) is required for all Multi-Object Delete requests.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following operations are related to `DeleteObjects`:

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`DeleteObjectsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name containing the objects to delete.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Delete` — Delete · **required** · sent as httpPayload

Container for the request.

### `MFA` — string · sent as header `x-amz-mfa`

The concatenation of the authentication device's serial number, a space, and the value that is
displayed on your authentication device. Required to permanently delete a versioned object if versioning
is configured with MFA delete enabled.

When performing the `DeleteObjects` operation on an MFA delete enabled bucket, which
attempts to delete the specified versioned objects, you must include an MFA token. If you don't provide
an MFA token, the entire request will fail, even if there are non-versioned objects that you are trying
to delete. If you provide an invalid token, whether there are versioned object keys in the request or
not, the entire Multi-Object Delete request will fail. For information about MFA Delete, see  [MFA
Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `BypassGovernanceRetention` — boolean · sent as header `x-amz-bypass-governance-retention`

Specifies whether you want to delete this object even if it has a Governance-type Object Lock in
place. To use this header, you must have the `s3:BypassGovernanceRetention`
permission.

This functionality is not supported for directory buckets.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum-algorithm` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`.

For the `x-amz-checksum-algorithm` header, replace `algorithm` with the supported algorithm from the following list:

- `CRC32`
- `CRC32C`
- `CRC64NVME`
- `MD5`
- `SHA1`
- `SHA256`
- `SHA512`
- `XXHASH3`
- `XXHASH64`
- `XXHASH128`

For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If the individual checksum value you provide through `x-amz-checksum-algorithm` doesn't match the checksum algorithm you set through `x-amz-sdk-checksum-algorithm`, Amazon S3 fails the request with a `BadDigest` error.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

## Output (`DeleteObjectsOutput`)

### `Deleted` — list<DeletedObject>

Container element for a successful delete. It identifies the object that was successfully
deleted.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `Errors` — list<Error>

Container for a failed delete action that describes the object that Amazon S3 attempted to delete and the
error it encountered.

## Examples

### To delete multiple object versions from a versioned bucket

The following example deletes objects from a bucket. The request specifies object versions. S3 deletes specific object versions and returns the key and versions of deleted objects in the response.

Input:

```json
{
  "Bucket": "examplebucket",
  "Delete": {
    "Objects": [
      {
        "Key": "HappyFace.jpg",
        "VersionId": "2LWg7lQLnY41.maGB5Z6SWW.dcq0vx7b"
      },
      {
        "Key": "HappyFace.jpg",
        "VersionId": "yoz3HB.ZhCS_tKVEmIOr7qYyyAaZSKVd"
      }
    ],
    "Quiet": false
  }
}
```

Output:

```json
{
  "Deleted": [
    {
      "VersionId": "yoz3HB.ZhCS_tKVEmIOr7qYyyAaZSKVd",
      "Key": "HappyFace.jpg"
    },
    {
      "VersionId": "2LWg7lQLnY41.maGB5Z6SWW.dcq0vx7b",
      "Key": "HappyFace.jpg"
    }
  ]
}
```

### To delete multiple objects from a versioned bucket

The following example deletes objects from a bucket. The bucket is versioned, and the request does not specify the object version to delete. In this case, all versions remain in the bucket and S3 adds a delete marker.

Input:

```json
{
  "Bucket": "examplebucket",
  "Delete": {
    "Objects": [
      {
        "Key": "objectkey1"
      },
      {
        "Key": "objectkey2"
      }
    ],
    "Quiet": false
  }
}
```

Output:

```json
{
  "Deleted": [
    {
      "DeleteMarkerVersionId": "A._w1z6EFiCF5uhtQMDal9JDkID9tQ7F",
      "Key": "objectkey1",
      "DeleteMarker": true
    },
    {
      "DeleteMarkerVersionId": "iOd_ORxhkKe_e8G8_oSGxt2PjsCZKlkt",
      "Key": "objectkey2",
      "DeleteMarker": true
    }
  ]
}
```
