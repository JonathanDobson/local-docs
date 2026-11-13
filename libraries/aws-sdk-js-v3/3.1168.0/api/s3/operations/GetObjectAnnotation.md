# GetObjectAnnotation

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetObjectAnnotationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?annotation&x-id=GetObjectAnnotation`

Retrieves an annotation from an Amazon S3 object. To use this operation, you must have the
`s3:GetObjectAnnotation` permission.

If checksum mode is enabled via the `x-amz-checksum-mode` header, Amazon S3
returns the stored checksum in the response headers for client-side validation.

Annotations are not supported by the following features: S3 Inventory Reports,
API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and
S3 Express One Zone (directory buckets).

The following operations are related to `GetObjectAnnotation`:

- [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
- [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)
- [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Input (`GetObjectAnnotationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket that contains the object.

### `Key` — string · **required** · sent as httpLabel

The object key.

### `AnnotationName` — string · **required** · sent as query `annotationName`

The name of the annotation to retrieve.

Length Constraints: Minimum length of 1. Maximum length of 512 bytes.

### `VersionId` — string · sent as query `versionId`

The version ID of the object.

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

### `ChecksumMode` — ChecksumMode (enum) · sent as header `x-amz-checksum-mode`

Set to `ENABLED` to validate the checksum of the annotation payload on retrieval.

Values: `ENABLED`

## Output (`GetObjectAnnotationOutput`)

### `AnnotationPayload` — blob · sent as httpPayload · default `""`

The annotation payload.

### `ObjectVersionId` — string · sent as header `x-amz-object-version-id`

The version ID of the object that the annotation is attached to.

### `LastModified` — timestamp · sent as header `Last-Modified`

The date and time the annotation was last modified.

### `ContentLength` — long · sent as header `Content-Length`

The size of the annotation payload, in bytes.

### `ETag` — string · sent as header `ETag`

The entity tag of the annotation.

### `ChecksumCRC32` — string · sent as header `x-amz-checksum-crc32`

The CRC32 checksum of the annotation payload.

### `ChecksumCRC32C` — string · sent as header `x-amz-checksum-crc32c`

The CRC32C checksum of the annotation payload.

### `ChecksumCRC64NVME` — string · sent as header `x-amz-checksum-crc64nvme`

The CRC64NVME checksum of the annotation payload.

### `ChecksumSHA1` — string · sent as header `x-amz-checksum-sha1`

The SHA1 checksum of the annotation payload.

### `ChecksumSHA256` — string · sent as header `x-amz-checksum-sha256`

The SHA256 checksum of the annotation payload.

### `ChecksumSHA512` — string · sent as header `x-amz-checksum-sha512`

The SHA512 checksum of the annotation payload.

### `ChecksumMD5` — string · sent as header `x-amz-checksum-md5`

The MD5 checksum of the annotation payload.

### `ChecksumXXHASH64` — string · sent as header `x-amz-checksum-xxhash64`

The XXHASH64 checksum of the annotation payload.

### `ChecksumXXHASH3` — string · sent as header `x-amz-checksum-xxhash3`

The XXHASH3 checksum of the annotation payload.

### `ChecksumXXHASH128` — string · sent as header `x-amz-checksum-xxhash128`

The XXHASH128 checksum of the annotation payload.

### `ChecksumType` — ChecksumType (enum) · sent as header `x-amz-checksum-type`

The type of checksum used.

Values: `COMPOSITE`, `FULL_OBJECT`

### `ServerSideEncryption` — ServerSideEncryption (enum) · sent as header `x-amz-server-side-encryption`

The server-side encryption algorithm used.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ReplicationStatus` — ReplicationStatus (enum) · sent as header `x-amz-replication-status`

The replication status of the annotation. Possible values include `PENDING`, `COMPLETED`, `FAILED`, and `REPLICA`.

Values: `COMPLETE`, `PENDING`, `FAILED`, `REPLICA`, `COMPLETED`

## Errors

- `NoSuchAnnotation` — The specified annotation does not exist on this object.
- `NoSuchBucket` — The specified bucket does not exist.
- `NoSuchKey` — The specified key does not exist.
