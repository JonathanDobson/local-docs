# RenameObject

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `RenameObjectCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}/{Key+}?renameObject`

Renames an existing object in a directory bucket that uses the S3 Express One Zone storage class.
You can use `RenameObject` by specifying an existing object’s name as the source and the new
name of the object as the destination within the same directory bucket.

`RenameObject` is only supported for objects stored in the S3 Express One Zone storage
class.

To prevent overwriting an object, you can use the `If-None-Match` conditional
header.

- **If-None-Match** - Renames the object only if an object
  with the specified name does not already exist in the directory bucket. If you don't want to
  overwrite an existing object, you can add the `If-None-Match` conditional header with the
  value `‘*’` in the `RenameObject` request. Amazon S3 then returns a `412
  Precondition Failed` error if the object with the specified name already exists. For more
  information, see [RFC 7232](https://datatracker.ietf.org/doc/rfc7232/).

Permissions
:   To grant access to the `RenameObject` operation on a directory bucket, we
    recommend that you use the `CreateSession` operation for session-based authorization.
    Specifically, you grant the `s3express:CreateSession` permission to the directory
    bucket in a bucket policy or an IAM identity-based policy. Then, you make the
    `CreateSession` API call on the directory bucket to obtain a session token. With the
    session token in your request header, you can make API requests to this operation. After the
    session token expires, you make another `CreateSession` API call to generate a new
    session token for use. The Amazon Web Services CLI and SDKs will create and manage your session including
    refreshing the session token automatically to avoid service interruptions when a session expires.
    In your bucket policy, you can specify the `s3express:SessionMode` condition key to
    control who can create a `ReadWrite` or `ReadOnly` session. A
    `ReadWrite` session is required for executing all the Zonal endpoint API operations,
    including `RenameObject`. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html). To learn more about Zonal endpoint API operations, see
    [Authorizing Zonal endpoint API operations with CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-create-session.html) in the *Amazon S3 User
    Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`RenameObjectRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name of the directory bucket containing the object.

You must use virtual-hosted-style requests in the format
`Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not
supported. Directory bucket names must be unique in the chosen Availability Zone. Bucket names must
follow the format `bucket-base-name--zone-id--x-s3`  (for example,
`amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming restrictions, see
[Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

Key name of the object to rename.

### `RenameSource` — string · **required** · sent as header `x-amz-rename-source`

Specifies the source for the rename operation. The value must be URL encoded.

### `DestinationIfMatch` — string · sent as header `If-Match`

Renames the object only if the ETag (entity tag) value provided during the operation matches the
ETag of the object in S3. The `If-Match` header field makes the request method conditional on
ETags. If the ETag values do not match, the operation returns a `412 Precondition Failed`
error.

Expects the ETag value as a string.

### `DestinationIfNoneMatch` — string · sent as header `If-None-Match`

Renames the object only if the destination does not already exist in the specified directory
bucket. If the object does exist when you send a request with `If-None-Match:*`, the S3 API
will return a `412 Precondition Failed` error, preventing an overwrite. The
`If-None-Match` header prevents overwrites of existing data by validating that there's not
an object with the same key name already in your directory bucket.

Expects the `*` character (asterisk).

### `DestinationIfModifiedSince` — timestamp · sent as header `If-Modified-Since`

Renames the object if the destination exists and if it has been modified since the specified
time.

### `DestinationIfUnmodifiedSince` — timestamp · sent as header `If-Unmodified-Since`

Renames the object if it hasn't been modified since the specified time.

### `SourceIfMatch` — string · sent as header `x-amz-rename-source-if-match`

Renames the object if the source exists and if its entity tag (ETag) matches the specified ETag.

### `SourceIfNoneMatch` — string · sent as header `x-amz-rename-source-if-none-match`

Renames the object if the source exists and if its entity tag (ETag) is different than the specified
ETag. If an asterisk (`*`) character is provided, the operation will fail and return a
`412 Precondition Failed` error.

### `SourceIfModifiedSince` — timestamp · sent as header `x-amz-rename-source-if-modified-since`

Renames the object if the source exists and if it has been modified since the specified time.

### `SourceIfUnmodifiedSince` — timestamp · sent as header `x-amz-rename-source-if-unmodified-since`

Renames the object if the source exists and hasn't been modified since the specified time.

### `ClientToken` — string · sent as header `x-amz-client-token`

A unique string with a max of 64 ASCII characters in the ASCII range of 33 - 126.

`RenameObject` supports idempotency using a client token. To make an idempotent API request
using `RenameObject`, specify a client token in the request. You should not reuse the same
client token for other API requests. If you retry a request that completed successfully using the same
client token and the same parameters, the retry succeeds without performing any further actions. If
you retry a successful request using the same client token, but one or more of the parameters are
different, the retry fails and an `IdempotentParameterMismatch` error is returned.

## Output (`RenameObjectOutput`)

_None._

## Errors

- `IdempotencyParameterMismatch` — Parameters on this idempotent request are inconsistent with parameters used in previous request(s).
