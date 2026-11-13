# UploadPart

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `UploadPartCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?x-id=UploadPart`

Uploads a part in a multipart upload.

In this operation, you provide new data as a part of an object in your request. However, you have
an option to specify your existing Amazon S3 object as a data source for the part you are uploading. To
upload a part from an existing object, you use the [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) operation.

You must initiate a multipart upload (see [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)) before you can
upload any part. In response to your initiate request, Amazon S3 returns an upload ID, a unique identifier
that you must include in your upload part request.

Part numbers can be any number from 1 to 10,000, inclusive. A part number uniquely identifies a part
and also defines its position within the object being created. If you upload a new part using the same
part number that was used with a previous part, the previously uploaded part is overwritten.

For information about maximum and minimum part sizes and other multipart upload specifications, see
[Multipart upload
limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html) in the *Amazon S3 User Guide*.

After you initiate multipart upload and upload one or more parts, you must either complete or
abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after
you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you
for the parts storage.

For more information on multipart uploads, go to [Multipart Upload Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) in the
*Amazon S3 User Guide* .

**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   - **General purpose bucket permissions** - To perform a
      multipart upload with encryption using an Key Management Service key, the requester must have permission to
      the `kms:Decrypt` and `kms:GenerateDataKey` actions on the key. The
      requester must also have permissions for the `kms:GenerateDataKey` action for the
      `CreateMultipartUpload` API. Then, the requester needs permissions for the
      `kms:Decrypt` action on the `UploadPart` and
      `UploadPartCopy` APIs.

      These permissions are required because Amazon S3 must decrypt and read data from the encrypted
      file parts before it completes the multipart upload. For more information about KMS
      permissions, see [Protecting data using server-side
      encryption with KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon S3 User Guide*. For information
      about the permissions required to use the multipart upload API, see [Multipart upload and
      permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html) and [Multipart upload API and
      permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html#mpuAndPermissions) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

      If the object is encrypted with SSE-KMS, you must also have the
      `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM
      identity-based policies and KMS key policies for the KMS key.

Data integrity
:   **General purpose bucket** - To ensure that data is not corrupted
    traversing the network, specify the `Content-MD5` header in the upload part request.
    Amazon S3 checks the part data against the provided MD5 value. If they do not match, Amazon S3 returns an
    error. If the upload request is signed with Signature Version 4, then Amazon Web Services S3 uses the
    `x-amz-content-sha256` header as a checksum instead of `Content-MD5`. For
    more information see [Authenticating Requests:
    Using the Authorization Header (Amazon Web Services Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html).

    **Directory buckets** - MD5 is not supported by directory buckets. You can use checksum algorithms to check object integrity.

Encryption
:   - **General purpose bucket** - Server-side encryption is for
      data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in its data centers
      and decrypts it when you access it. You have mutually exclusive options to protect data using
      server-side encryption in Amazon S3, depending on how you choose to manage the encryption keys.
      Specifically, the encryption key options are Amazon S3 managed keys (SSE-S3), Amazon Web Services KMS keys
      (SSE-KMS), and Customer-Provided Keys (SSE-C). Amazon S3 encrypts data with server-side encryption
      using Amazon S3 managed keys (SSE-S3) by default. You can optionally tell Amazon S3 to encrypt data at
      rest using server-side encryption with other key options. The option you use depends on
      whether you want to use KMS keys (SSE-KMS) or provide your own encryption key
      (SSE-C).

      Server-side encryption is supported by the S3 Multipart Upload operations. Unless you are
      using a customer-provided encryption key (SSE-C), you don't need to specify the encryption
      parameters in each UploadPart request. Instead, you only need to specify the server-side
      encryption parameters in the initial Initiate Multipart request. For more information, see
      [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html).

      If you have server-side encryption with customer-provided keys (SSE-C) blocked for your general purpose bucket, you will get an HTTP 403 Access Denied error when you specify the SSE-C request headers while writing new data to your bucket. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).

      If you request server-side encryption using a customer-provided encryption key (SSE-C) in
      your initiate multipart upload request, you must provide identical encryption information in
      each part upload using the following request headers.

      - x-amz-server-side-encryption-customer-algorithm
      - x-amz-server-side-encryption-customer-key
      - x-amz-server-side-encryption-customer-key-MD5

      For more information, see [Using Server-Side
      Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in the *Amazon S3 User Guide*.
    - **Directory buckets**  -
      For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with KMS keys (SSE-KMS) (`aws:kms`).

Special errors
:   - Error Code: `NoSuchUpload`

      - Description: The specified multipart upload does not exist. The upload ID might be
        invalid, or the multipart upload might have been aborted or completed.
      - HTTP Status Code: 404 Not Found
      - SOAP Fault Code Prefix: Client

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following operations are related to `UploadPart`:

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`UploadPartRequest`)

### `Body` — blob · sent as httpPayload · default `""`

Object data.

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket to which the multipart upload was initiated.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `ContentLength` — long · sent as header `Content-Length`

Size of the body in bytes. This parameter is useful when the size of the body cannot be determined
automatically.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when using
the command from the CLI. This parameter is required if object lock parameters are specified.

This functionality is not supported for directory buckets.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

This checksum algorithm must be the same for all parts and it match the checksum value supplied in
the `CreateMultipartUpload` request.

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
checksum of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

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
digest of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 128-bit `MD5`
digest of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `XXHASH64`
checksum of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 64-bit `XXHASH3`
checksum of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

This header can be used as a data integrity check to verify that the data received is the same data
that was originally sent. This header specifies the Base64 encoded, 128-bit `XXHASH128`
checksum of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Object key for which the multipart upload was initiated.

### `PartNumber` — integer · **required** · sent as query `partNumber`

Part number of part being uploaded. This is a positive integer between 1 and 10,000.

### `UploadId` — string · **required** · sent as query `uploadId`

Upload ID identifying the multipart upload whose part is being uploaded.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

Specifies the algorithm to use when encrypting the object (for example, AES256).

This functionality is not supported for directory buckets.

### `SSECustomerKey` — string · sent as header `x-amz-server-side-encryption-customer-key`

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is
used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must
be appropriate for use with the algorithm specified in the
`x-amz-server-side-encryption-customer-algorithm header`. This must be the same encryption
key specified in the initiate multipart upload request.

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

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`UploadPartOutput`)

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
encryption option is `aws:fsx`.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `ETag` — string · sent as header `ETag`

Entity tag for the uploaded object.

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

The Base64 encoded, 32-bit `CRC32` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

The Base64 encoded, 160-bit `SHA1` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

The Base64 encoded, 256-bit `SHA256` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

The Base64 encoded, 512-bit `SHA512` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

The Base64 encoded, 128-bit `MD5` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

The Base64 encoded, 64-bit `XXHASH64` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

The Base64 encoded, 64-bit `XXHASH3` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

The Base64 encoded, 128-bit `XXHASH128` checksum of the part. This will only be present if
the checksum was provided in the request. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

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

Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with
Key Management Service (KMS) keys (SSE-KMS).

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### To upload a part

The following example uploads part 1 of a multipart upload. The example specifies a file name for the part data. The Upload ID is same that is returned by the initiate multipart upload.

Input:

```json
{
  "Body": "fileToUpload",
  "Bucket": "examplebucket",
  "Key": "examplelargeobject",
  "PartNumber": 1,
  "UploadId": "xadcOB_7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--"
}
```

Output:

```json
{
  "ETag": "\"d8c2eafd90c266e19ab9dcacc479f8af\""
}
```
