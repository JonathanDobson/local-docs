# ListDirectoryBuckets

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListDirectoryBucketsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /?x-id=ListDirectoryBuckets` · Paginated (token `ContinuationToken` → `ContinuationToken`)

Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request. For
more information about directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the
*Amazon S3 User Guide*.

**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   You must have the `s3express:ListAllMyDirectoryBuckets` permission in
    an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the Amazon Web Services account that owns the resource.
    For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is
    `s3express-control.region.amazonaws.com`.

The `BucketRegion` response element is not part of the
`ListDirectoryBuckets` Response Syntax.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListDirectoryBucketsRequest`)

### `ContinuationToken` — string · sent as query `continuation-token`

`ContinuationToken` indicates to Amazon S3 that the list is being continued on buckets in this
account with a token. `ContinuationToken` is obfuscated and is not a real bucket name. You
can use this `ContinuationToken` for the pagination of the list results.

### `MaxDirectoryBuckets` — integer · sent as query `max-directory-buckets`

Maximum number of buckets to be returned in response. When the number is more than the count of
buckets that are owned by an Amazon Web Services account, return all the buckets in response.

## Output (`ListDirectoryBucketsOutput`)

### `Buckets` — list<Bucket>

The list of buckets owned by the requester.

### `ContinuationToken` — string

If `ContinuationToken` was sent with the request, it is included in the response. You can
use the returned `ContinuationToken` for pagination of the list response.
