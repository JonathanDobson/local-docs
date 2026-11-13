# PutObject

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutObjectCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?x-id=PutObject`

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025,
the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following Amazon Web Services Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

Adds an object to a bucket.

- Amazon S3 never adds partial objects; if you receive a success response, Amazon S3 added the entire
  object to the bucket. You cannot use `PutObject` to only update a single piece of
  metadata for an existing object. You must put the entire object with updated metadata if you want
  to update some values.
- If your bucket uses the bucket owner enforced setting for Object Ownership, ACLs are disabled
  and no longer affect permissions. All objects written to the bucket by any account will be owned
  by the bucket owner.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
  *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
  *Amazon S3 User Guide*.

Amazon S3 is a distributed system. If it receives multiple write requests for the same object
simultaneously, it overwrites all but the last object written. However, Amazon S3 provides features that can
modify this behavior:

- **S3 Object Lock** - To prevent objects from being deleted
  or overwritten, you can use [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in the *Amazon S3 User Guide*.

  This functionality is not supported for directory buckets.
- **If-None-Match** - Uploads the object only if the object
  key name does not already exist in the specified bucket. Otherwise, Amazon S3 returns a `412
  Precondition Failed` error. If a conflicting operation occurs during the upload, S3 returns
  a `409 ConditionalRequestConflict` response. On a 409 failure, retry the upload.

  Expects the \* character (asterisk).

  For more information, see [Add preconditions to S3 operations with
  conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the *Amazon S3 User Guide* or [RFC 7232](https://datatracker.ietf.org/doc/rfc7232/).

  This functionality is not supported for S3 on Outposts.
- **S3 Versioning** - When you enable versioning for a bucket,
  if Amazon S3 receives multiple write requests for the same object simultaneously, it stores all versions
  of the objects. For each write request that is made to the same object, Amazon S3 automatically generates
  a unique version ID of that object being stored in Amazon S3. You can retrieve, replace, or delete any
  version of the object. For more information about versioning, see [Adding Objects to
  Versioning-Enabled Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/AddingObjectstoVersioningEnabledBuckets.html) in the *Amazon S3 User Guide*. For information
  about returning the versioning state of a bucket, see [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html).

  This functionality is not supported for directory buckets.

Permissions
:   - **General purpose bucket permissions** - The following
      permissions are required in your policies when your `PutObject` request includes
      specific headers.

      - **`s3:PutObject`** - To successfully
        complete the `PutObject` request, you must always have the
        `s3:PutObject` permission on a bucket to add an object to it.
      - **`s3:PutObjectAcl`** - To successfully change the objects ACL of your `PutObject`
        request, you must have the `s3:PutObjectAcl`.
      - **`s3:PutObjectTagging`** - To successfully set the tag-set with your `PutObject`
        request, you must have the `s3:PutObjectTagging`.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

      If the object is encrypted with SSE-KMS, you must also have the
      `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM
      identity-based policies and KMS key policies for the KMS key.

Data integrity with Content-MD5
:   - **General purpose bucket** - To ensure that data is not
      corrupted traversing the network, use the `Content-MD5` header. When you use this
      header, Amazon S3 checks the object against the provided MD5 value and, if they do not match, Amazon S3
      returns an error. Alternatively, when the object's ETag is its MD5 digest, you can calculate
      the MD5 while putting the object to Amazon S3 and compare the returned ETag to the calculated MD5
      value.
    - **Directory bucket** -
      This functionality is not supported for directory buckets.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

Errors
:   - You might receive an `InvalidRequest` error for several reasons. Depending on the reason for the error, you might receive one of the following messages:

      - Cannot specify both a write offset value and user-defined object metadata for existing
        objects.
      - Checksum Type mismatch occurred, expected checksum Type: sha1, actual checksum Type:
        crc32c.
      - Request body cannot be empty when 'write offset' is specified.

For more information about related Amazon S3 APIs, see the following:

- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutObjectRequest`)

### `ACL` — ObjectCannedACL (enum) · sent as header `x-amz-acl`

The canned ACL to apply to the object. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL) in the
*Amazon S3 User Guide*.

When adding a new object, you can use headers to grant ACL-based permissions to individual
Amazon Web Services accounts or to predefined groups defined by Amazon S3. These permissions are then added to the ACL on
the object. By default, all objects are private. Only the owner has full access control. For more
information, see [Access Control
List (ACL) Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html) and [Managing ACLs Using the REST API](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-using-rest-api.html) in the
*Amazon S3 User Guide*.

If the bucket that you're uploading objects to uses the bucket owner enforced setting for S3 Object
Ownership, ACLs are disabled and no longer affect permissions. Buckets that use this setting only accept
PUT requests that don't specify an ACL or PUT requests that specify bucket owner full control ACLs, such
as the `bucket-owner-full-control` canned ACL or an equivalent form of this ACL expressed in
the XML format. PUT requests that contain other ACLs (for example, custom grants to certain
Amazon Web Services accounts) fail and return a `400` error with the error code
`AccessControlListNotSupported`. For more information, see  [Controlling ownership of objects and
disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

Values: `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, `bucket-owner-full-control`

### `Body` — blob · sent as httpPayload · default `""`

Object data.

### `Bucket` — string · **required** · sent as httpLabel

The bucket name to which the PUT action was initiated.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `CacheControl` — string · sent as header `Cache-Control`

Can be used to specify caching behavior along the request/reply chain. For more information, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

### `ContentDisposition` — string · sent as header `Content-Disposition`

Specifies presentational information for the object. For more information, see <https://www.rfc-editor.org/rfc/rfc6266#section-4>.

### `ContentEncoding` — string · sent as header `Content-Encoding`

Specifies what content encodings have been applied to the object and thus what decoding mechanisms
must be applied to obtain the media-type referenced by the Content-Type header field. For more
information, see <https://www.rfc-editor.org/rfc/rfc9110.html#field.content-encoding>.

### `ContentLanguage` — string · sent as header `Content-Language`

The language the content is in.

### `ContentLength` — long · sent as header `Content-Length`

Size of the body in bytes. This parameter is useful when the size of the body cannot be determined
automatically. For more information, see <https://www.rfc-editor.org/rfc/rfc9110.html#name-content-length>.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the message (without the headers) according to
RFC 1864. This header can be used as a message integrity check to verify that the data is the same data
that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an
end-to-end integrity check. For more information about REST request authentication, see [REST
Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html).

The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is required for
any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more
information, see [Uploading objects
to an Object Lock enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object)  in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

### `ContentType` — string · sent as header `Content-Type`

A standard MIME type describing the format of the contents. For more information, see <https://www.rfc-editor.org/rfc/rfc9110.html#name-content-type>.

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

The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is required for
any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more
information, see [Uploading objects
to an Object Lock enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object)  in the *Amazon S3 User Guide*.

For directory buckets, when you use Amazon Web Services SDKs, `CRC32` is the default checksum algorithm that's used for performance.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
This header specifies the Base64 encoded, 32-bit `CRC32` checksum of the object. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the
*Amazon S3 User Guide*.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
This header specifies the Base64 encoded, 32-bit `CRC32C` checksum of the object. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the
*Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME`
checksum of the object. The `CRC64NVME` checksum is always a full object checksum. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
This header specifies the Base64 encoded, 160-bit `SHA1` digest of the object. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the
*Amazon S3 User Guide*.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
This header specifies the Base64 encoded, 256-bit `SHA256` digest of the object. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the
*Amazon S3 User Guide*.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 512-bit `SHA512`
digest of the object. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 128-bit `MD5`
digest of the object. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `XXHASH64`
checksum of the object. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `XXHASH3`
checksum of the object. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 128-bit `XXHASH128`
checksum of the object. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `Expires` — string · sent as header `Expires`

The date and time at which the object is no longer cacheable. For more information, see <https://www.rfc-editor.org/rfc/rfc7234#section-5.3>.

### `IfMatch` — string · sent as header `If-Match`

Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches
the ETag of the object in S3. If the ETag values do not match, the operation returns a `412
Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409
ConditionalRequestConflict` response. On a 409 failure you should fetch the object's ETag and
retry the upload.

Expects the ETag value as a string.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232), or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the
*Amazon S3 User Guide*.

### `IfNoneMatch` — string · sent as header `If-None-Match`

Uploads the object only if the object key name does not already exist in the bucket specified.
Otherwise, Amazon S3 returns a `412 Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409
ConditionalRequestConflict` response. On a 409 failure you should retry the upload.

Expects the '\*' (asterisk) character.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232), or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the
*Amazon S3 User Guide*.

### `GrantFullControl` — string · sent as header `x-amz-grant-full-control`

Gives the grantee READ, READ\_ACP, and WRITE\_ACP permissions on the object.

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

### `GrantRead` — string · sent as header `x-amz-grant-read`

Allows grantee to read the object data and its metadata.

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

### `GrantReadACP` — string · sent as header `x-amz-grant-read-acp`

Allows grantee to read the object ACL.

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

### `GrantWriteACP` — string · sent as header `x-amz-grant-write-acp`

Allows grantee to write the ACL for the applicable object.

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

### `Key` — string · **required** · sent as httpLabel

Object key for which the PUT action was initiated.

### `WriteOffsetBytes` — long · sent as header `x-amz-write-offset-bytes`

Specifies the offset for appending data to existing objects in bytes. The offset must be equal to
the size of the existing object being appended to. If no object exists, setting this header to 0 will
create a new object.

This functionality is only supported for objects in the Amazon S3 Express One Zone storage class in
directory buckets.

### `Metadata` — map<string, string>

A map of metadata to store with the object in S3.

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm that was used when you store this object in Amazon S3 or
Amazon FSx.

- **General purpose buckets**  - You have four mutually exclusive
  options to protect data using server-side encryption in Amazon S3, depending on how you choose to manage
  the encryption keys. Specifically, the encryption key options are Amazon S3 managed keys (SSE-S3),
  Amazon Web Services KMS keys (SSE-KMS or DSSE-KMS), and customer-provided keys (SSE-C). Amazon S3 encrypts data with
  server-side encryption by using Amazon S3 managed keys (SSE-S3) by default. You can optionally tell Amazon S3
  to encrypt data at rest by using server-side encryption with other key options. For more
  information, see [Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in
  the *Amazon S3 User Guide*.
- **Directory buckets**  -
  For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with KMS keys (SSE-KMS) (`aws:kms`). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your
  `CreateSession` requests or `PUT` object requests. Then, new objects
  are automatically encrypted with the desired encryption settings. For more
  information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide*. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with KMS for new object uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html).

  In the Zonal endpoint API calls (except [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) and [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)) using the REST API, the encryption request headers must match the encryption settings that are specified in the `CreateSession` request.
  You can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) that are specified in the `CreateSession` request.
  You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and
  Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket.

  When you use the CLI or the Amazon Web Services SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the Amazon Web Services SDKs use the bucket's default encryption configuration for the
  `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request.
  So in the Zonal endpoint API calls (except [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) and [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)),
  the encryption request headers must match the default encryption configuration of the directory bucket.
- **S3 access points for Amazon FSx**  - When accessing data stored in
  Amazon FSx file systems using S3 access points, the only valid server side encryption option is
  `aws:fsx`. All Amazon FSx file systems have encryption configured by default and are
  encrypted at rest. Data is automatically encrypted before being written to the file system, and
  automatically decrypted as it is read. These processes are handled transparently by Amazon FSx.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `StorageClass` — StorageClass (enum) · sent as header `x-amz-storage-class`

By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. The STANDARD
storage class provides high durability and high availability. Depending on performance needs, you can
specify a different Storage Class. For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) in the
*Amazon S3 User Guide*.

- Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in
  Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in
  Dedicated Local Zones.
- Amazon S3 on Outposts only uses the OUTPOSTS Storage Class.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `WebsiteRedirectLocation` — string · sent as header `x-amz-website-redirect-location`

If the bucket is configured as a website, redirects requests for this object to another object in
the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For
information about object metadata, see [Object Key and Metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html) in the *Amazon S3
User Guide*.

In the following example, the request header sets the redirect to an object (anotherPage.html) in
the same bucket:

`x-amz-website-redirect-location: /anotherPage.html`

In the following example, the request header sets the object redirect to another website:

`x-amz-website-redirect-location: http://www.example.com/`

For more information about website hosting in Amazon S3, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) and [How to Configure Website Page
Redirects](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

Specifies the algorithm to use when encrypting the object (for example, `AES256`).

This functionality is not supported for directory buckets.

### `SSECustomerKey` — string · sent as header `x-amz-server-side-encryption-customer-key`

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is
used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must
be appropriate for use with the algorithm specified in the
`x-amz-server-side-encryption-customer-algorithm` header.

This functionality is not supported for directory buckets.

### `SSECustomerKeyMD5` — string · sent as header `x-amz-server-side-encryption-customer-key-MD5`

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header
for a message integrity check to ensure that the encryption key was transmitted without error.

This functionality is not supported for directory buckets.

### `SSEKMSKeyId` — string · sent as header `x-amz-server-side-encryption-aws-kms-key-id`

Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same
account that's issuing the command, you must use the full Key ARN not the Key ID.

**General purpose buckets** - If you specify `x-amz-server-side-encryption` with `aws:kms` or `aws:kms:dsse`, this header specifies the ID (Key ID, Key ARN, or Key Alias) of the KMS
key to use. If you specify
`x-amz-server-side-encryption:aws:kms` or
`x-amz-server-side-encryption:aws:kms:dsse`, but do not provide `x-amz-server-side-encryption-aws-kms-key-id`, Amazon S3 uses the Amazon Web Services managed key
(`aws/s3`) to protect the data.

**Directory buckets** - To encrypt data using SSE-KMS, it's recommended to specify the
`x-amz-server-side-encryption` header to `aws:kms`. Then, the `x-amz-server-side-encryption-aws-kms-key-id` header implicitly uses
the bucket's default KMS customer managed key ID. If you want to explicitly set the `x-amz-server-side-encryption-aws-kms-key-id` header, it must match the bucket's default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket's lifetime.
The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3`) isn't supported.
Incorrect key specification results in an HTTP `400 Bad Request` error.

### `SSEKMSEncryptionContext` — string · sent as header `x-amz-server-side-encryption-context`

Specifies the Amazon Web Services KMS Encryption Context as an additional encryption context to use for object encryption. The value of
this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.
This value is stored as object metadata and automatically gets passed on
to Amazon Web Services KMS for future `GetObject` operations on
this object.

**General purpose buckets** - This value must be explicitly added during `CopyObject` operations if you want an additional encryption context for your object. For more information, see [Encryption context](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#encryption-context) in the *Amazon S3 User Guide*.

**Directory buckets** - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported.

### `BucketKeyEnabled` — boolean · sent as header `x-amz-server-side-encryption-bucket-key-enabled`

Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with
server-side encryption using Key Management Service (KMS) keys (SSE-KMS).

**General purpose buckets** - Setting this header to
`true` causes Amazon S3 to use an S3 Bucket Key for object encryption with
SSE-KMS. Also, specifying this header with a PUT action doesn't affect bucket-level settings for S3
Bucket Key.

**Directory buckets** - S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html), [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops), or
[the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job). In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `Tagging` — string · sent as header `x-amz-tagging`

The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example,
"Key1=Value1")

This functionality is not supported for directory buckets.

### `ObjectLockMode` — ObjectLockMode (enum) · sent as header `x-amz-object-lock-mode`

The Object Lock mode that you want to apply to this object.

This functionality is not supported for directory buckets.

Values: `GOVERNANCE`, `COMPLIANCE`

### `ObjectLockRetainUntilDate` — timestamp · sent as header `x-amz-object-lock-retain-until-date`

The date and time when you want this object's Object Lock to expire. Must be formatted as a
timestamp parameter.

This functionality is not supported for directory buckets.

### `ObjectLockLegalHoldStatus` — ObjectLockLegalHoldStatus (enum) · sent as header `x-amz-object-lock-legal-hold`

Specifies whether a legal hold will be applied to this object. For more information about S3 Object
Lock, see [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) in
the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `ON`, `OFF`

### `ObjectLockEventHold` — ObjectLockEventHold (enum) · sent as header `x-amz-object-lock-event-hold`

Specifies the event hold status to apply to this object. Set to `ON` to enable or
`OFF` to disable.

This functionality is not supported for directory buckets.

Values: `ON`, `OFF`

### `ObjectLockEventHoldDurationDays` — integer · sent as header `x-amz-object-lock-event-hold-duration-days`

Specifies the event hold duration in days to apply to this object. You cannot specify a
duration in both days and years.

This functionality is not supported for directory buckets.

### `ObjectLockEventHoldDurationYears` — integer · sent as header `x-amz-object-lock-event-hold-duration-years`

Specifies the event hold duration in years to apply to this object. You cannot specify a
duration in both days and years.

This functionality is not supported for directory buckets.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`PutObjectOutput`)

### `Expiration` — string · sent as header `x-amz-expiration`

If the expiration is configured for the object (see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)) in the *Amazon S3 User Guide*, the response
includes this header. It includes the `expiry-date` and `rule-id` key-value pairs
that provide information about object expiration. The value of the `rule-id` is
URL-encoded.

Object expiration information is not returned in directory buckets and this header returns the
value "`NotImplemented`" in all responses for directory buckets.

### `ETag` — string · sent as header `ETag`

Entity tag for the uploaded object.

**General purpose buckets**  - To ensure that data is not corrupted
traversing the network, for objects where the ETag is the MD5 digest of the object, you can calculate
the MD5 while putting an object to Amazon S3 and compare the returned ETag to the calculated MD5
value.

**Directory buckets**  - The ETag for the object in a
directory bucket isn't the MD5 digest of the object.

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This header is present if
the object was uploaded with the `CRC64NVME` checksum algorithm, or if it was uploaded
without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to the uploaded
object). For more information about how checksums are calculated with multipart uploads, see [Checking object
integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

The Base64 encoded, 512-bit `SHA512` digest of the object. This header is present if
the object was uploaded with the `SHA512` checksum algorithm. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

The Base64 encoded, 128-bit `MD5` digest of the object. This header is present if
the object was uploaded with the `MD5` checksum algorithm. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

The Base64 encoded, 64-bit `XXHASH64` checksum of the object. This header is present if
the object was uploaded with the `XXHASH64` checksum algorithm. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

The Base64 encoded, 64-bit `XXHASH3` checksum of the object. This header is present if
the object was uploaded with the `XXHASH3` checksum algorithm. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

The Base64 encoded, 128-bit `XXHASH128` checksum of the object. This header is present if
the object was uploaded with the `XXHASH128` checksum algorithm. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumType` — ChecksumType (enum) · sent as header `x-amz-checksum-type`

This header specifies the checksum type of the object, which determines how part-level checksums are
combined to create an object-level checksum for multipart objects. For `PutObject` uploads,
the checksum type is always `FULL_OBJECT`. You can use this header as a data integrity check
to verify that the checksum type that is received is the same checksum that was specified. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
encryption option is `aws:fsx`.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `VersionId` — string · sent as header `x-amz-version-id`

Version ID of the object.

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the
object being stored. Amazon S3 returns this ID in the response. When you enable versioning for a bucket, if
Amazon S3 receives multiple write requests for the same object simultaneously, it stores all of the objects.
For more information about versioning, see [Adding Objects to
Versioning-Enabled Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/AddingObjectstoVersioningEnabledBuckets.html) in the *Amazon S3 User Guide*. For information about
returning the versioning state of a bucket, see [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html).

This functionality is not supported for directory buckets.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

If server-side encryption with a customer-provided encryption key was requested, the response will
include this header to confirm the encryption algorithm that's used.

This functionality is not supported for directory buckets.

### `SSECustomerKeyMD5` — string · sent as header `x-amz-server-side-encryption-customer-key-MD5`

If server-side encryption with a customer-provided encryption key was requested, the response will
include this header to provide the round-trip message integrity verification of the customer-provided
encryption key.

This functionality is not supported for directory buckets.

### `SSEKMSKeyId` — string · sent as header `x-amz-server-side-encryption-aws-kms-key-id`

If present, indicates the ID of the KMS key that was used for object encryption.

### `SSEKMSEncryptionContext` — string · sent as header `x-amz-server-side-encryption-context`

If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of
this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.
This value is stored as object metadata and automatically gets
passed on to Amazon Web Services KMS for future `GetObject`
operations on this object.

### `BucketKeyEnabled` — boolean · sent as header `x-amz-server-side-encryption-bucket-key-enabled`

Indicates whether the uploaded object uses an S3 Bucket Key for server-side encryption with
Key Management Service (KMS) keys (SSE-KMS).

### `Size` — long · sent as header `x-amz-object-size`

The size of the object in bytes. This value is only be present if you append to an object.

This functionality is only supported for objects in the Amazon S3 Express One Zone storage class in
directory buckets.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `EncryptionTypeMismatch` — The existing object was created with a different encryption type.
- `InvalidRequest` — A parameter or header in your request isn't valid.
- `InvalidWriteOffset` — The write offset value that you specified does not match the current object size.
- `TooManyParts` — You have attempted to add more parts than the maximum of 10000 that are allowed for this object.

## Examples

### To create an object.

The following example creates an object. If the bucket is versioning enabled, S3 returns version ID in response.

Input:

```json
{
  "Body": "filetoupload",
  "Bucket": "examplebucket",
  "Key": "objectkey"
}
```

Output:

```json
{
  "VersionId": "Bvq0EDKxOcXLJXNo_Lkz37eM3R4pfzyQ",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\""
}
```

### To upload an object (specify optional headers)

The following example uploads an object. The request specifies optional request headers to directs S3 to use specific storage class and use server-side encryption.

Input:

```json
{
  "Body": "HappyFace.jpg",
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg",
  "ServerSideEncryption": "AES256",
  "StorageClass": "STANDARD_IA"
}
```

Output:

```json
{
  "VersionId": "CG612hodqujkf8FaaNfp8U..FIhLROcp",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
  "ServerSideEncryption": "AES256"
}
```

### To upload an object

The following example uploads an object to a versioning-enabled bucket. The source file is specified using Windows file syntax. S3 returns VersionId of the newly created object.

Input:

```json
{
  "Body": "HappyFace.jpg",
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg"
}
```

Output:

```json
{
  "VersionId": "tpf3zF08nBplQK1XLOefGskR7mGDwcDk",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\""
}
```

### To upload an object and specify canned ACL.

The following example uploads and object. The request specifies optional canned ACL (access control list) to all READ access to authenticated users. If the bucket is versioning enabled, S3 returns version ID in response.

Input:

```json
{
  "ACL": "authenticated-read",
  "Body": "filetoupload",
  "Bucket": "examplebucket",
  "Key": "exampleobject"
}
```

Output:

```json
{
  "VersionId": "Kirh.unyZwjQ69YxcQLA8z4F5j3kJJKr",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\""
}
```

### To upload an object and specify optional tags

The following example uploads an object. The request specifies optional object tags. The bucket is versioned, therefore S3 returns version ID of the newly created object.

Input:

```json
{
  "Body": "c:\\HappyFace.jpg",
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg",
  "Tagging": "key1=value1&key2=value2"
}
```

Output:

```json
{
  "VersionId": "psM2sYY4.o1501dSx8wMvnkOzSBB.V4a",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\""
}
```

### To upload an object and specify server-side encryption and object tags

The following example uploads an object. The request specifies the optional server-side encryption option. The request also specifies optional object tags. If the bucket is versioning enabled, S3 returns version ID in response.

Input:

```json
{
  "Body": "filetoupload",
  "Bucket": "examplebucket",
  "Key": "exampleobject",
  "ServerSideEncryption": "AES256",
  "Tagging": "key1=value1&key2=value2"
}
```

Output:

```json
{
  "VersionId": "Ri.vC6qVlA4dEnjgRV4ZHsHoFIjqEMNt",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
  "ServerSideEncryption": "AES256"
}
```

### To upload object and specify user-defined metadata

The following example creates an object. The request also specifies optional metadata. If the bucket is versioning enabled, S3 returns version ID in response.

Input:

```json
{
  "Body": "filetoupload",
  "Bucket": "examplebucket",
  "Key": "exampleobject",
  "Metadata": {
    "metadata1": "value1",
    "metadata2": "value2"
  }
}
```

Output:

```json
{
  "VersionId": "pSKidl4pHBiNwukdbcPXAIs.sshFFOc0",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\""
}
```
