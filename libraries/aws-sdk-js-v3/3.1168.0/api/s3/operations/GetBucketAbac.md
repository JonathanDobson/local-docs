# GetBucketAbac

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketAbacCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?abac`

Returns the attribute-based access control (ABAC) property of the general purpose bucket. If ABAC is enabled on your bucket, you can use tags on the bucket for access control. For more information, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

## Input (`GetBucketAbacRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the general purpose bucket.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The Amazon Web Services account ID of the general purpose bucket's owner.

## Output (`GetBucketAbacOutput`)

### `AbacStatus` — AbacStatus · sent as httpPayload

The ABAC status of the general purpose bucket.
