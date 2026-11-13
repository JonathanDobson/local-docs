# DeleteObjectAnnotation

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `DeleteObjectAnnotationCommand` from `@aws-sdk/client-s3` · HTTP: `DELETE /{Bucket}/{Key+}?annotation`

Deletes a specific annotation from an Amazon S3 object. Use the `x-amz-object-if-match`
header to perform a conditional delete that only succeeds if the object's ETag matches the
provided value, preventing race conditions during concurrent updates.

Deleting an annotation is permanent. Annotations are not independently versioned, so there is no
delete marker or way to recover a deleted annotation.

To use this operation, you must have the `s3:DeleteObjectAnnotation` permission. If
the object is protected by Object Lock in governance mode, you must also include the
`x-amz-bypass-governance-retention` header.

Annotations are not supported by the following features: S3 Inventory Reports,
API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and
S3 Express One Zone (directory buckets).

The following operations are related to `DeleteObjectAnnotation`:

- [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
- [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
- [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)

## Input (`DeleteObjectAnnotationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket that contains the object.

### `Key` — string · **required** · sent as httpLabel

The object key.

### `AnnotationName` — string · **required** · sent as query `annotationName`

The name of the annotation to delete. Annotation names are UTF-8 encoded and cannot start with
`aws` or `s3` (case-insensitive).

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

The account ID of the expected bucket owner.

### `ObjectIfMatch` — string · sent as header `x-amz-object-if-match`

If specified, the operation only succeeds if the object's ETag matches the provided value.

## Output (`DeleteObjectAnnotationOutput`)

### `ObjectVersionId` — string · sent as header `x-amz-object-version-id`

The version ID of the object that the annotation was deleted from.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `NoSuchBucket` — The specified bucket does not exist.
- `NoSuchKey` — The specified key does not exist.
