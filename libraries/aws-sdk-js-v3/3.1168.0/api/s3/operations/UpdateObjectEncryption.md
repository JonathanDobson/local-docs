# UpdateObjectEncryption

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `UpdateObjectEncryptionCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?encryption`

This operation is not supported for directory buckets or Amazon S3 on Outposts buckets.

Updates the server-side encryption type of an existing encrypted object in a general purpose bucket.
You can use the `UpdateObjectEncryption` operation to change encrypted objects from
server-side encryption with Amazon S3 managed keys (SSE-S3) to server-side encryption with Key Management Service (KMS)
keys (SSE-KMS), or to apply S3 Bucket Keys. You can also use the `UpdateObjectEncryption` operation
to change the customer-managed KMS key used to encrypt your data so that you can comply with custom
key-rotation standards.

Using the `UpdateObjectEncryption` operation, you can atomically update the server-side
encryption type of an existing object in a general purpose bucket without any data movement. The
`UpdateObjectEncryption` operation uses envelope encryption to re-encrypt the data key used to
encrypt and decrypt your object with your newly specified server-side encryption type. In other words,
when you use the `UpdateObjectEncryption` operation, your data isn't copied, archived
objects in the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes aren't
restored, and objects in the S3 Intelligent-Tiering storage class aren't moved between tiers.
Additionally, the `UpdateObjectEncryption` operation preserves all object metadata
properties, including the storage class, creation date, last modified date, ETag, and checksum
properties. For more information, see
[Updating server-side encryption for existing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/update-sse-encryption.html) in the
*Amazon S3 User Guide*.

By default, all `UpdateObjectEncryption` requests that specify a customer-managed
KMS key are restricted to KMS keys that are owned by the bucket owner's Amazon Web Services account. If you're
using Organizations, you can request the ability to use KMS keys owned by other member
accounts within your organization by contacting Amazon Web Services Support.

Source objects that are unencrypted, or encrypted with either dual-layer server-side encryption
with KMS keys (DSSE-KMS) or server-side encryption with customer-provided keys (SSE-C) aren't
supported by this operation. Additionally, you cannot specify SSE-S3 encryption as the requested
new encryption type `UpdateObjectEncryption` request.

Permissions
:   - To use the `UpdateObjectEncryption` operation, you must have the following
      permissions:

      - `s3:UpdateObjectEncryption`
      - `kms:Encrypt`
      - `kms:Decrypt`
      - `kms:GenerateDataKey`
      - `kms:ReEncrypt*`
    - If you're using Organizations, to use this operation with customer-managed
      KMS keys from other Amazon Web Services accounts within your organization, you must have the
      `organizations:DescribeAccount` permission.

Errors
:   - You might receive an `InvalidRequest` error for several reasons. Depending
      on the reason for the error, you might receive one of the following messages:

      - The `UpdateObjectEncryption` operation doesn't supported unencrypted
        source objects. Only source objects encrypted with SSE-S3 or SSE-KMS are supported.
      - The `UpdateObjectEncryption` operation doesn't support source objects
        with the encryption type DSSE-KMS or SSE-C. Only source objects encrypted with SSE-S3
        or SSE-KMS are supported.
      - The `UpdateObjectEncryption` operation doesn't support updating the
        encryption type to DSSE-KMS or SSE-C. Modify the request to specify SSE-KMS
        for the updated encryption type, and then try again.
      - Requests that modify an object encryption configuration require Amazon Web Services Signature
        Version 4. Modify the request to use Amazon Web Services Signature Version 4, and then try again.
      - Requests that modify an object encryption configuration require a valid new
        encryption type. Valid values are `SSEKMS`. Modify the request to specify
        SSE-KMS for the updated encryption type, and then try again.
      - Requests that modify an object's encryption type to SSE-KMS require an Amazon Web Services KMS key
        Amazon Resource Name (ARN). Modify the request to specify a KMS key ARN, and then
        try again.
      - Requests that modify an object's encryption type to SSE-KMS require a valid
        Amazon Web Services KMS key Amazon Resource Name (ARN). Confirm that you have a correctly formatted
        KMS key ARN in your request, and then try again.
      - The `BucketKeyEnabled` value isn't valid. Valid values are
        `true` or `false`. Modify the request to specify a valid value,
        and then try again.
    - You might receive an `AccessDenied` error for several reasons. Depending on
      the reason for the error, you might receive one of the following messages:

      - The Amazon Web Services KMS key in the request must be owned by the same account as the bucket. Modify
        the request to specify a KMS key from the same account, and then try again.
      - The bucket owner's account was approved to make `UpdateObjectEncryption` requests
        that use any Amazon Web Services KMS key in their organization, but the bucket owner's account isn't part of
        an organization in Organizations. Make sure that the bucket owner's account and the
        specified KMS key belong to the same organization, and then try again.
      - The specified Amazon Web Services KMS key must be from the same organization in Organizations as
        the bucket. Specify a KMS key that belongs to the same organization as the bucket, and then
        try again.
      - The encryption type for the specified object can’t be updated because that object is
        protected by S3 Object Lock. If the object has a governance-mode retention period or a legal
        hold, you must first remove the Object Lock status on the object before you issue your
        `UpdateObjectEncryption` request. You can't use the `UpdateObjectEncryption`
        operation with objects that have an Object Lock compliance mode retention period applied to them.

## Input (`UpdateObjectEncryptionRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the general purpose bucket that contains the specified object key name.

When you use this operation with an access point attached to a general purpose bucket, you
must either provide the alias of the access point in place of the bucket name or you must specify
the access point Amazon Resource Name (ARN). When using the access point ARN, you must direct
requests to the access point hostname. The access point hostname takes the form
`AccessPointName-AccountId.s3-accesspoint.Region.amazonaws.com`.
When using this operation with an access point through the Amazon Web Services SDKs, you provide the access point
ARN in place of the bucket name. For more information about access point ARNs, see
[Referencing access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-naming.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

The key name of the object that you want to update the server-side encryption type for.

### `VersionId` — string · sent as query `versionId`

The version ID of the object that you want to update the server-side encryption type for.

### `ObjectEncryption` — ObjectEncryption · **required** · sent as httpPayload

The updated server-side encryption type for this object. The `UpdateObjectEncryption`
operation supports the SSE-S3 and SSE-KMS encryption types.

Valid Values: `SSES3` | `SSEKMS`

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide doesn't match the
actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden`
(access denied).

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash for the request body. For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the object when you use an Amazon Web Services SDK. This header
doesn't provide any additional functionality if you don't use the SDK. When you send this header,
there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent.
Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html)  in the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

## Output (`UpdateObjectEncryptionResponse`)

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `AccessDenied` — You might receive this error for several reasons.
- `InvalidRequest` — A parameter or header in your request isn't valid.
- `NoSuchKey` — The specified key does not exist.
