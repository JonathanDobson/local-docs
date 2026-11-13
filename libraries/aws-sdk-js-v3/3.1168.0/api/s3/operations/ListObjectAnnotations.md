# ListObjectAnnotations

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListObjectAnnotationsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?annotation&x-id=ListObjectAnnotations` · Paginated (token `ContinuationToken` → `NextContinuationToken`)

Lists the annotations attached to an Amazon S3 object. Results are paginated, with a maximum of
1,000 annotations per object. Use the `AnnotationPrefix` parameter to filter the
results by name prefix.

To use this operation, you must have the `s3:ListObjectAnnotations` permission.

Annotations are not supported by the following features: S3 Inventory Reports,
API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and
S3 Express One Zone (directory buckets).

The following operations are related to `ListObjectAnnotations`:

- [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)
- [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)
- [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)

## Input (`ListObjectAnnotationsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket that contains the object.

### `Key` — string · **required** · sent as httpLabel

The object key.

### `VersionId` — string · sent as query `versionId`

The version ID of the object.

### `MaxAnnotationResults` — integer · sent as query `max-annotation-results`

The maximum number of annotations to return in the response. Maximum is 1,000.

### `AnnotationPrefix` — string · sent as query `annotation-prefix`

Filter results to annotations whose name begins with the specified prefix.

### `ContinuationToken` — string · sent as query `continuation-token`

Continuation token returned by a previous request to retrieve the next page.

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

## Output (`ListObjectAnnotationsOutput`)

### `Annotations` — list<AnnotationEntry>

The list of annotations attached to the object.

### `Bucket` — string

The bucket name.

### `Key` — string

The object key.

### `ObjectVersionId` — string · sent as header `x-amz-object-version-id`

The version ID of the object.

### `AnnotationPrefix` — string

The prefix used to filter the response.

### `MaxAnnotationResults` — integer

The maximum number of annotations returned in the response.

### `AnnotationCount` — integer

The number of annotations returned.

### `ContinuationToken` — string

The continuation token used in this request.

### `NextContinuationToken` — string

The continuation token to use to retrieve the next page of results.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `InvalidPrefix` — The annotation prefix you provided is invalid.
- `NoSuchBucket` — The specified bucket does not exist.
- `NoSuchKey` — The specified key does not exist.
