# HeadObject

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `HeadObjectCommand` from `@aws-sdk/client-s3` · HTTP: `HEAD /{Bucket}/{Key+}`

The `HEAD` operation retrieves metadata from an object without returning the object
itself. This operation is useful if you're interested only in an object's metadata.

A `HEAD` request has the same options as a `GET` operation on an object. The
response is identical to the `GET` response except that there is no response body. Because
of this, if the `HEAD` request generates an error, it returns a generic code, such as
`400 Bad Request`, `403 Forbidden`, `404 Not Found`, `405
Method Not Allowed`, `412 Precondition Failed`, or `304 Not Modified`.
It's not possible to retrieve the exact exception of these error codes.

Request headers are limited to 8 KB in size. For more information, see [Common Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html).

Permissions
:   - **General purpose bucket permissions** - To use
      `HEAD`, you must have the `s3:GetObject` permission. You need the
      relevant read object (or version) permission for this operation. For more information, see
      [Actions, resources,
      and condition keys for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html) in the *Amazon S3 User Guide*. For more
      information about the permissions to S3 API operations by S3 resource types, see [Required permissions for
      Amazon S3 API operations](/AmazonS3/latest/userguide/using-with-s3-policy-actions.html) in the *Amazon S3 User Guide*.

      If the object you request doesn't exist, the error that Amazon S3 returns depends on whether
      you also have the `s3:ListBucket` permission.

      - If you have the `s3:ListBucket` permission on the bucket, Amazon S3 returns an
        HTTP status code `404 Not Found` error.
      - If you don’t have the `s3:ListBucket` permission, Amazon S3 returns an HTTP
        status code `403 Forbidden` error.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

      If you enable `x-amz-checksum-mode` in the request and the object is encrypted
      with Amazon Web Services Key Management Service (Amazon Web Services KMS), you must also have the
      `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM
      identity-based policies and KMS key policies for the KMS key to retrieve the checksum of
      the object.

Encryption
:   Encryption request headers, like `x-amz-server-side-encryption`, should not be
    sent for `HEAD` requests if your object uses server-side encryption with Key Management Service
    (KMS) keys (SSE-KMS), dual-layer server-side encryption with Amazon Web Services KMS keys (DSSE-KMS), or
    server-side encryption with Amazon S3 managed encryption keys (SSE-S3). The
    `x-amz-server-side-encryption` header is used when you `PUT` an object
    to S3 and want to specify the encryption method. If you include this header in a
    `HEAD` request for an object that uses these types of keys, you’ll get an HTTP
    `400 Bad Request` error. It's because the encryption method can't be changed when
    you retrieve the object.

    If you encrypt an object by using server-side encryption with customer-provided encryption
    keys (SSE-C) when you store the object in Amazon S3, then when you retrieve the metadata from the
    object, you must use the following headers to provide the encryption key for the server to be able
    to retrieve the object's metadata. The headers are:

    - `x-amz-server-side-encryption-customer-algorithm`
    - `x-amz-server-side-encryption-customer-key`
    - `x-amz-server-side-encryption-customer-key-MD5`

    For more information about SSE-C, see [Server-Side Encryption (Using
    Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide*.

    **Directory bucket**  -
    For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS. SSE-C isn't supported. For more
    information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide*.

Versioning
:   - If the current version of the object is a delete marker, Amazon S3 behaves as if the object was
      deleted and includes `x-amz-delete-marker: true` in the response.
    - If the specified version is a delete marker, the response returns a `405 Method Not
      Allowed` error and the `Last-Modified: timestamp` response header.

    - **Directory buckets** -
      Delete marker is not supported for directory buckets.
    - **Directory buckets** -
      S3 Versioning isn't enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets. You can only specify `null` to the
      `versionId` query parameter in the request.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

    For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
    *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
    *Amazon S3 User Guide*.

The following actions are related to `HeadObject`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`HeadObjectRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket that contains the object.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `IfMatch` — string · sent as header `If-Match`

Return the object only if its entity tag (ETag) is the same as the one specified; otherwise, return
a 412 (precondition failed) error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the
request as follows:

- `If-Match` condition evaluates to `true`, and;
- `If-Unmodified-Since` condition evaluates to `false`;

Then Amazon S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232).

### `IfModifiedSince` — timestamp · sent as header `If-Modified-Since`

Return the object only if it has been modified since the specified time; otherwise, return a 304
(not modified) error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in
the request as follows:

- `If-None-Match` condition evaluates to `false`, and;
- `If-Modified-Since` condition evaluates to `true`;

Then Amazon S3 returns the `304 Not Modified` response code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232).

### `IfNoneMatch` — string · sent as header `If-None-Match`

Return the object only if its entity tag (ETag) is different from the one specified; otherwise,
return a 304 (not modified) error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in
the request as follows:

- `If-None-Match` condition evaluates to `false`, and;
- `If-Modified-Since` condition evaluates to `true`;

Then Amazon S3 returns the `304 Not Modified` response code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232).

### `IfUnmodifiedSince` — timestamp · sent as header `If-Unmodified-Since`

Return the object only if it has not been modified since the specified time; otherwise, return a 412
(precondition failed) error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the
request as follows:

- `If-Match` condition evaluates to `true`, and;
- `If-Unmodified-Since` condition evaluates to `false`;

Then Amazon S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232).

### `Key` — string · **required** · sent as httpLabel

The object key.

### `Range` — string · sent as header `Range`

HeadObject returns only the metadata for an object. If the Range is satisfiable, only the
`ContentLength` is affected in the response. If the Range is not satisfiable, S3 returns a
`416 - Requested Range Not Satisfiable` error.

### `ResponseCacheControl` — string · sent as query `response-cache-control`

Sets the `Cache-Control` header of the response.

### `ResponseContentDisposition` — string · sent as query `response-content-disposition`

Sets the `Content-Disposition` header of the response.

### `ResponseContentEncoding` — string · sent as query `response-content-encoding`

Sets the `Content-Encoding` header of the response.

### `ResponseContentLanguage` — string · sent as query `response-content-language`

Sets the `Content-Language` header of the response.

### `ResponseContentType` — string · sent as query `response-content-type`

Sets the `Content-Type` header of the response.

### `ResponseExpires` — timestamp · sent as query `response-expires`

Sets the `Expires` header of the response.

### `VersionId` — string · sent as query `versionId`

Version ID used to reference a specific version of the object.

For directory buckets in this API operation, only the `null` value of the version ID is supported.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

Specifies the algorithm to use when encrypting the object (for example, AES256).

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

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `PartNumber` — integer · sent as query `partNumber`

Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively
performs a 'ranged' HEAD request for the part specified. Useful querying about the size of the part and
the number of parts in this object.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `ChecksumMode` — ChecksumMode (enum) · sent as header `x-amz-checksum-mode`

To retrieve the checksum, this parameter must be enabled.

**General purpose buckets** -
If you enable checksum mode and the object is uploaded with a [checksum](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html) and encrypted with
an Key Management Service (KMS) key, you must have permission to use the `kms:Decrypt` action to
retrieve the checksum.

**Directory buckets** - If you enable `ChecksumMode`
and the object is encrypted with Amazon Web Services Key Management Service (Amazon Web Services KMS), you must also have the
`kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based
policies and KMS key policies for the KMS key to retrieve the checksum of the object.

Values: `ENABLED`

## Output (`HeadObjectOutput`)

### `DeleteMarker` — boolean · sent as header `x-amz-delete-marker`

Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this
response header does not appear in the response.

This functionality is not supported for directory buckets.

### `AcceptRanges` — string · sent as header `accept-ranges`

Indicates that a range of bytes was specified.

### `Expiration` — string · sent as header `x-amz-expiration`

If the object expiration is configured (see [`PutBucketLifecycleConfiguration`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)), the response includes this header. It
includes the `expiry-date` and `rule-id` key-value pairs providing object
expiration information. The value of the `rule-id` is URL-encoded.

Object expiration information is not returned in directory buckets and this header returns the
value "`NotImplemented`" in all responses for directory buckets.

### `Restore` — string · sent as header `x-amz-restore`

If the object is an archived object (an object whose storage class is GLACIER), the response
includes this header if either the archive restoration is in progress (see [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) or an archive copy is already
restored.

If an archive copy is already restored, the header value indicates when Amazon S3 is scheduled to delete
the object copy. For example:

`x-amz-restore: ongoing-request="false", expiry-date="Fri, 21 Dec 2012 00:00:00
GMT"`

If the object restoration is in progress, the header returns the value
`ongoing-request="true"`.

For more information about archiving objects, see [Transitioning Objects: General Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-transition-general-considerations).

This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

### `ArchiveStatus` — ArchiveStatus (enum) · sent as header `x-amz-archive-status`

The archive state of the head object.

This functionality is not supported for directory buckets.

Values: `ARCHIVE_ACCESS`, `DEEP_ARCHIVE_ACCESS`

### `LastModified` — timestamp · sent as header `Last-Modified`

Date and time when the object was last modified.

### `ContentLength` — long · sent as header `Content-Length`

Size of the body in bytes.

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

The Base64 encoded, 512-bit `SHA512` digest of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

The Base64 encoded, 128-bit `MD5` digest of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

The Base64 encoded, 64-bit `XXHASH64` checksum of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

The Base64 encoded, 64-bit `XXHASH3` checksum of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

The Base64 encoded, 128-bit `XXHASH128` checksum of the object. For more information, see
[Checking
object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumType` — ChecksumType (enum) · sent as header `x-amz-checksum-type`

The checksum type, which determines how part-level checksums are combined to create an object-level
checksum for multipart objects. You can use this header response to verify that the checksum type that
is received is the same checksum type that was specified in `CreateMultipartUpload` request.
For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

Values: `COMPOSITE`, `FULL_OBJECT`

### `ETag` — string · sent as header `ETag`

An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a
resource found at a URL.

### `MissingMeta` — integer · sent as header `x-amz-missing-meta`

This is set to the number of metadata entries not returned in `x-amz-meta` headers. This
can happen if you create metadata using an API like SOAP that supports more flexible metadata than the
REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP
headers.

This functionality is not supported for directory buckets.

### `VersionId` — string · sent as header `x-amz-version-id`

Version ID of the object.

This functionality is not supported for directory buckets.

### `CacheControl` — string · sent as header `Cache-Control`

Specifies caching behavior along the request/reply chain.

### `ContentDisposition` — string · sent as header `Content-Disposition`

Specifies presentational information for the object.

### `ContentEncoding` — string · sent as header `Content-Encoding`

Indicates what content encodings have been applied to the object and thus what decoding mechanisms
must be applied to obtain the media-type referenced by the Content-Type header field.

### `ContentLanguage` — string · sent as header `Content-Language`

The language the content is in.

### `ContentType` — string · sent as header `Content-Type`

A standard MIME type describing the format of the object data.

### `ContentRange` — string · sent as header `Content-Range`

The portion of the object returned in the response for a `GET` request.

### `Expires` — string · sent as header `Expires`

The date and time at which the object is no longer cacheable.

### `WebsiteRedirectLocation` — string · sent as header `x-amz-website-redirect-location`

If the bucket is configured as a website, redirects requests for this object to another object in
the same bucket or to an external URL. Amazon S3 stores the value of this header in the object
metadata.

This functionality is not supported for directory buckets.

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
encryption option is `aws:fsx`.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `Metadata` — map<string, string>

A map of metadata to store with the object in S3.

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

### `BucketKeyEnabled` — boolean · sent as header `x-amz-server-side-encryption-bucket-key-enabled`

Indicates whether the object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS)
keys (SSE-KMS).

### `StorageClass` — StorageClass (enum) · sent as header `x-amz-storage-class`

Provides storage class information of the object. Amazon S3 returns this header for all objects except
for S3 Standard storage class objects.

For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html).

**Directory buckets**  -
Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ReplicationStatus` — ReplicationStatus (enum) · sent as header `x-amz-replication-status`

Amazon S3 can return this header if your request involves a bucket that is either a source or a
destination in a replication rule.

In replication, you have a source bucket on which you configure replication and destination bucket
or buckets where Amazon S3 stores object replicas. When you request an object (`GetObject`) or
object metadata (`HeadObject`) from these buckets, Amazon S3 will return the
`x-amz-replication-status` header in the response as follows:

- **If requesting an object from the source bucket**, Amazon S3 will
  return the `x-amz-replication-status` header if the object in your request is eligible
  for replication.

  For example, suppose that in your replication configuration, you specify object prefix
  `TaxDocs` requesting Amazon S3 to replicate objects with key prefix `TaxDocs`.
  Any objects you upload with this key name prefix, for example `TaxDocs/document1.pdf`,
  are eligible for replication. For any object request with this key name prefix, Amazon S3 will return the
  `x-amz-replication-status` header with value PENDING, COMPLETED or FAILED indicating
  object replication status.
- **If requesting an object from a destination bucket**, Amazon S3 will
  return the `x-amz-replication-status` header with value REPLICA if the object in your
  request is a replica that Amazon S3 created and there is no replica modification replication in
  progress.
- **When replicating objects to multiple destination buckets**, the
  `x-amz-replication-status` header acts differently. The header of the source object
  will only return a value of COMPLETED when replication is successful to all destinations. The header
  will remain at value PENDING until replication has completed for all destinations. If one or more
  destinations fails replication the header will return FAILED.

For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).

This functionality is not supported for directory buckets.

Values: `COMPLETE`, `PENDING`, `FAILED`, `REPLICA`, `COMPLETED`

### `PartsCount` — integer · sent as header `x-amz-mp-parts-count`

The count of parts this object has. This value is only returned if you specify
`partNumber` in your request and the object was uploaded as a multipart upload.

### `TagCount` — integer · sent as header `x-amz-tagging-count`

The number of tags, if any, on the object, when you have the relevant permission to read object
tags.

You can use [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) to retrieve the tag set associated with an object.

This functionality is not supported for directory buckets.

### `ObjectLockMode` — ObjectLockMode (enum) · sent as header `x-amz-object-lock-mode`

The Object Lock mode, if any, that's in effect for this object. This header is only returned if the
requester has the `s3:GetObjectRetention` permission. For more information about S3 Object
Lock, see [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

This functionality is not supported for directory buckets.

Values: `GOVERNANCE`, `COMPLIANCE`

### `ObjectLockRetainUntilDate` — timestamp · sent as header `x-amz-object-lock-retain-until-date`

The date and time when the Object Lock retention period expires. This header is only returned if the
requester has the `s3:GetObjectRetention` permission.

This functionality is not supported for directory buckets.

### `ObjectLockLegalHoldStatus` — ObjectLockLegalHoldStatus (enum) · sent as header `x-amz-object-lock-legal-hold`

Specifies whether a legal hold is in effect for this object. This header is only returned if the
requester has the `s3:GetObjectLegalHold` permission. This header is not returned if the
specified version of this object has never had a legal hold applied. For more information about S3
Object Lock, see [Object
Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

This functionality is not supported for directory buckets.

Values: `ON`, `OFF`

### `ObjectLockEventHold` — ObjectLockEventHold (enum) · sent as header `x-amz-object-lock-event-hold`

The event hold status for this object. This header is only returned if the requester has the
`s3:GetObjectRetention` permission.

This functionality is not supported for directory buckets.

Values: `ON`, `OFF`

### `ObjectLockEventHoldDurationDays` — integer · sent as header `x-amz-object-lock-event-hold-duration-days`

The event hold duration in days for this object. Only returned when the event hold is
enabled.

This functionality is not supported for directory buckets.

### `ObjectLockEventHoldDurationYears` — integer · sent as header `x-amz-object-lock-event-hold-duration-years`

The event hold duration in years for this object. Only returned when the event hold is
enabled.

This functionality is not supported for directory buckets.

## Errors

- `NotFound` — The specified content does not exist.

## Examples

### To retrieve metadata of an object without returning the object itself

The following example retrieves an object metadata.

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
  "AcceptRanges": "bytes",
  "ContentType": "image/jpeg",
  "LastModified": "2016-12-15T01:19:41.000Z",
  "ContentLength": 3191,
  "VersionId": "null",
  "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
  "Metadata": {}
}
```
