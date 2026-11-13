# CompleteMultipartUpload

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `CompleteMultipartUploadCommand` from `@aws-sdk/client-s3` · HTTP: `POST /{Bucket}/{Key+}`

Completes a multipart upload by assembling previously uploaded parts.

You first initiate the multipart upload and then upload all parts using the [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) operation or the
[UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)
operation. After successfully uploading all relevant parts of an upload, you call this
`CompleteMultipartUpload` operation to complete the upload. Upon receiving this request,
Amazon S3 concatenates all the parts in ascending order by part number to create a new object. In the
CompleteMultipartUpload request, you must provide the parts list and ensure that the parts list is
complete. The CompleteMultipartUpload API operation concatenates the parts that you provide in the list.
For each part in the list, you must provide the `PartNumber` value and the `ETag`
value that are returned after that part was uploaded.

The processing of a CompleteMultipartUpload request could take several minutes to finalize. After
Amazon S3 begins processing the request, it sends an HTTP response header that specifies a `200
OK` response. While processing is in progress, Amazon S3 periodically sends white space characters to
keep the connection from timing out. A request could fail after the initial `200 OK` response
has been sent. This means that a `200 OK` response can contain either a success or an error.
The error response might be embedded in the `200 OK` response. If you call this API operation
directly, make sure to design your application to parse the contents of the response and handle it
appropriately. If you use Amazon Web Services SDKs, SDKs handle this condition. The SDKs detect the embedded error and
apply error handling per your configuration settings (including automatically retrying the request as
appropriate). If the condition persists, the SDKs throw an exception (or, for the SDKs that don't use
exceptions, they return an error).

Note that if `CompleteMultipartUpload` fails, applications should be prepared to retry
any failed requests (including 500 error responses). For more information, see [Amazon S3 Error Best
Practices](https://docs.aws.amazon.com/AmazonS3/latest/dev/ErrorBestPractices.html).

You can't use `Content-Type: application/x-www-form-urlencoded` for the
CompleteMultipartUpload requests. Also, if you don't provide a `Content-Type` header,
`CompleteMultipartUpload` can still return a `200 OK` response.

For more information about multipart uploads, see [Uploading Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) in
the *Amazon S3 User Guide*.

**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   - **General purpose bucket permissions** - For information
      about permissions required to use the multipart upload API, see [Multipart Upload and Permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html) in
      the *Amazon S3 User Guide*.

      If you provide an [additional checksum value](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html) in your `MultipartUpload` requests and the
      object is encrypted with Key Management Service, you must have permission to use the
      `kms:Decrypt` action for the `CompleteMultipartUpload` request to
      succeed.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

      If the object is encrypted with SSE-KMS, you must also have the
      `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM
      identity-based policies and KMS key policies for the KMS key.

Special errors
:   - Error Code: `EntityTooSmall`

      - Description: Your proposed upload is smaller than the minimum allowed object size.
        Each part must be at least 5 MB in size, except the last part.
      - HTTP Status Code: 400 Bad Request
    - Error Code: `InvalidPart`

      - Description: One or more of the specified parts could not be found. The part might not
        have been uploaded, or the specified ETag might not have matched the uploaded part's
        ETag.
      - HTTP Status Code: 400 Bad Request
    - Error Code: `InvalidPartOrder`

      - Description: The list of parts was not in ascending order. The parts list must be
        specified in order by part number.
      - HTTP Status Code: 400 Bad Request
    - Error Code: `NoSuchUpload`

      - Description: The specified multipart upload does not exist. The upload ID might be
        invalid, or the multipart upload might have been aborted or completed.
      - HTTP Status Code: 404 Not Found

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following operations are related to `CompleteMultipartUpload`:

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`CompleteMultipartUploadRequest`)

### `Bucket` — string · **required** · sent as httpLabel

Name of the bucket to which the multipart upload was initiated.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Object key for which the multipart upload was initiated.

### `MultipartUpload` — CompletedMultipartUpload · sent as httpPayload

The container for the multipart upload request information.

### `UploadId` — string · **required** · sent as query `uploadId`

ID for the initiated multipart upload.

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

### `ChecksumType` — ChecksumType (enum) · sent as header `x-amz-checksum-type`

This header specifies the checksum type of the object, which determines how part-level checksums are
combined to create an object-level checksum for multipart objects. You can use this header as a data
integrity check to verify that the checksum type that is received is the same checksum that was
specified. If the checksum type doesn’t match the checksum type that was specified for the object during
the `CreateMultipartUpload` request, it’ll result in a `BadDigest` error. For more
information, see Checking object integrity in the Amazon S3 User Guide.

Values: `COMPOSITE`, `FULL_OBJECT`

### `MpuObjectSize` — long · sent as header `x-amz-mp-object-size`

The expected total object size of the multipart upload request. If there’s a mismatch between the
specified object size value and the actual object size value, it results in an `HTTP 400
InvalidRequest` error.

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

### `IfMatch` — string · sent as header `If-Match`

Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches
the ETag of the object in S3. If the ETag values do not match, the operation returns a `412
Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409
ConditionalRequestConflict` response. On a 409 failure you should fetch the object's ETag,
re-initiate the multipart upload with `CreateMultipartUpload`, and re-upload each
part.

Expects the ETag value as a string.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232), or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the
*Amazon S3 User Guide*.

### `IfNoneMatch` — string · sent as header `If-None-Match`

Uploads the object only if the object key name does not already exist in the bucket specified.
Otherwise, Amazon S3 returns a `412 Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409
ConditionalRequestConflict` response. On a 409 failure you should re-initiate the multipart
upload with `CreateMultipartUpload` and re-upload each part.

Expects the '\*' (asterisk) character.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232), or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the
*Amazon S3 User Guide*.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is required
only when the object was created using a checksum algorithm or if your bucket policy requires the use of
SSE-C. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html#ssec-require-condition-key) in the *Amazon S3 User Guide*.

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

## Output (`CompleteMultipartUploadOutput`)

### `Location` — string

The URI that identifies the newly created object.

### `Bucket` — string

The name of the bucket that contains the newly created object. Does not return the access point ARN or access point
alias if used.

Access points are not supported by directory buckets.

### `Key` — string

The object key of the newly created object.

### `Expiration` — string · sent as header `x-amz-expiration`

If the object expiration is configured, this will contain the expiration date
(`expiry-date`) and rule ID (`rule-id`). The value of `rule-id` is
URL-encoded.

This functionality is not supported for directory buckets.

### `ETag` — string

Entity tag that identifies the newly created object's data. Objects with different object data will
have different entity tags. The entity tag is an opaque string. The entity tag may or may not be an MD5
digest of the object data. If the entity tag is not an MD5 digest of the object data, it will contain
one or more nonhexadecimal characters and/or will consist of less than 32 or more than 32 hexadecimal
digits. For more information about how the entity tag is calculated, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME`
checksum of the object. The `CRC64NVME` checksum is always a full object checksum. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the object. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the object. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the object. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the object. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the object. For more
information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

### `ChecksumType` — ChecksumType (enum)

The checksum type, which determines how part-level checksums are combined to create an object-level
checksum for multipart objects. You can use this header as a data integrity check to verify that the
checksum type that is received is the same checksum type that was specified during the
`CreateMultipartUpload` request. For more information, see [Checking object integrity in the Amazon S3
User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

Values: `COMPOSITE`, `FULL_OBJECT`

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used when storing this object in Amazon S3.

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
encryption option is `aws:fsx`.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `VersionId` — string · sent as header `x-amz-version-id`

Version ID of the newly created object, in case the bucket has versioning turned on.

This functionality is not supported for directory buckets.

### `SSEKMSKeyId` — string · sent as header `x-amz-server-side-encryption-aws-kms-key-id`

If present, indicates the ID of the KMS key that was used for object encryption.

### `BucketKeyEnabled` — boolean · sent as header `x-amz-server-side-encryption-bucket-key-enabled`

Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with
Key Management Service (KMS) keys (SSE-KMS).

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### To complete multipart upload

The following example completes a multipart upload.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "bigobject",
  "MultipartUpload": {
    "Parts": [
      {
        "PartNumber": 1,
        "ETag": "\"d8c2eafd90c266e19ab9dcacc479f8af\""
      },
      {
        "PartNumber": 2,
        "ETag": "\"d8c2eafd90c266e19ab9dcacc479f8af\""
      }
    ]
  },
  "UploadId": "7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--"
}
```

Output:

```json
{
  "ETag": "\"4d9031c7644d8081c2829f4ea23c55f7-2\"",
  "Bucket": "acexamplebucket",
  "Location": "https://examplebucket.s3.<Region>.amazonaws.com/bigobject",
  "Key": "bigobject"
}
```
