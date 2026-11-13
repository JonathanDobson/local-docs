# PutObjectAnnotation

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutObjectAnnotationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?annotation`

Attaches an annotation to an Amazon S3 object. An annotation is a named payload of 1 byte to 1 MiB
that you can associate with a specific object or object version. Each object can have up to 1,000
annotations.

For annotation naming rules and restrictions, see [Annotation naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/annotations-overview.html)
in the *Amazon S3 User Guide*.

Annotations inherit the encryption of their parent object. For objects without server-side
encryption, annotations are encrypted with SSE-S3 (the default for new objects). Objects
encrypted with SSE-C cannot have annotations.

To use this operation, you must have the `s3:PutObjectAnnotation` permission. If the
bucket has Requester Pays enabled, you must include the `x-amz-request-payer` header.

Annotations are not supported by the following features: S3 Inventory Reports,
API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and
S3 Express One Zone (directory buckets).

The following operations are related to `PutObjectAnnotation`:

- [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
- [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)
- [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Input (`PutObjectAnnotationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket that contains the object.

### `Key` — string · **required** · sent as httpLabel

The object key.

### `VersionId` — string · sent as query `versionId`

The version ID of the object to attach the annotation to.

### `AnnotationName` — string · **required** · sent as query `annotationName`

The name of the annotation.

Length Constraints: Minimum length of 1. Maximum length of 512 bytes.

### `AnnotationPayload` — blob · **required** · sent as httpPayload

The annotation payload. Must be between 1 byte and 1 MiB in size, and must be valid UTF-8
encoded text. If the payload contains invalid UTF-8 bytes, the request fails with HTTP 415
(Unsupported Media Type). To store binary data, encode the payload using Base64 before
uploading.

### `ObjectIfMatch` — string · sent as header `x-amz-object-if-match`

If specified, the operation only succeeds if the object's ETag matches the provided value.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

The checksum algorithm to use. Supported values: `CRC32`, `CRC32C`, `CRC64NVME`, `SHA1`, `SHA256`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

Base64-encoded CRC32 checksum of the annotation payload.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

Base64-encoded CRC32C checksum of the annotation payload.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

Base64-encoded CRC64NVME checksum of the annotation payload.

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

Base64-encoded SHA1 checksum of the annotation payload.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

Base64-encoded SHA256 checksum of the annotation payload.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

Base64-encoded SHA512 checksum of the annotation payload.

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

Base64-encoded MD5 checksum of the annotation payload.

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

Base64-encoded XXHASH64 checksum of the annotation payload.

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

Base64-encoded XXHASH3 checksum of the annotation payload.

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

Base64-encoded XXHASH128 checksum of the annotation payload.

### `ContentMD5` — string · sent as header `Content-MD5`

Base64-encoded MD5 digest of the message.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.

## Output (`PutObjectAnnotationOutput`)

### `Key` — string

The object key.

### `AnnotationName` — string

The name of the annotation.

### `ObjectVersionId` — string · sent as header `x-amz-object-version-id`

The version ID of the object that the annotation was attached to.

### `ETag` — string · sent as header `ETag`

The entity tag of the annotation.

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

The CRC32 checksum of the stored annotation.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

The CRC32C checksum of the stored annotation.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

The CRC64NVME checksum of the stored annotation.

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

The SHA1 checksum of the stored annotation.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

The SHA256 checksum of the stored annotation.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

The SHA512 checksum of the stored annotation.

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

The MD5 checksum of the stored annotation.

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

The XXHASH64 checksum of the stored annotation.

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

The XXHASH3 checksum of the stored annotation.

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

The XXHASH128 checksum of the stored annotation.

### `ChecksumType` — ChecksumType (enum) · sent as header `x-amz-checksum-type`

The type of checksum used.

Values: `COMPOSITE`, `FULL_OBJECT`

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used to encrypt the annotation.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `AnnotationLimitExceeded` — The request would exceed the maximum number of annotations allowed per object.
- `AnnotationNameTooLong` — The annotation name exceeds 512 bytes.
- `InvalidAnnotationName` — The annotation name you provided is invalid.
- `InvalidRequest` — A parameter or header in your request isn't valid.
- `NoSuchBucket` — The specified bucket does not exist.
- `NoSuchKey` — The specified key does not exist.
- `UnsupportedMediaType` — The annotation payload is not valid UTF-8 encoded text.
