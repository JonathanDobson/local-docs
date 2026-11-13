# PutBucketAcl

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketAclCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?acl`

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025,
the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following Amazon Web Services Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

This operation is not supported for directory buckets.

Sets the permissions on an existing bucket using access control lists (ACL). For more information,
see [Using ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html). To
set the ACL of a bucket, you must have the `WRITE_ACP` permission.

You can use one of the following two ways to set a bucket's permissions:

- Specify the ACL in the request body
- Specify permissions using request headers

You cannot specify access permission using both the body and the request headers.

Depending on your application needs, you may choose to set the ACL on a bucket using either the
request body or the headers. For example, if you have an existing application that updates a bucket ACL
using the request body, then you can continue to use that approach.

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled
and no longer affect permissions. You must use policies to grant access to your bucket and the objects
in it. Requests to set ACLs or update ACLs fail and return the
`AccessControlListNotSupported` error code. Requests to read ACLs are still supported.
For more information, see [Controlling object ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in
the *Amazon S3 User Guide*.

Permissions
:   You can set access permissions by using one of the following methods:

    - Specify a canned ACL with the `x-amz-acl` request header. Amazon S3 supports a set
      of predefined ACLs, known as *canned ACLs*. Each canned ACL has a
      predefined set of grantees and permissions. Specify the canned ACL name as the value of
      `x-amz-acl`. If you use this header, you cannot use other access control-specific
      headers in your request. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL).
    - Specify access permissions explicitly with the `x-amz-grant-read`,
      `x-amz-grant-read-acp`, `x-amz-grant-write-acp`, and
      `x-amz-grant-full-control` headers. When using these headers, you specify
      explicit access permissions and grantees (Amazon Web Services accounts or Amazon S3 groups) who will receive the
      permission. If you use these ACL-specific headers, you cannot use the `x-amz-acl`
      header to set a canned ACL. These parameters map to the set of permissions that Amazon S3 supports
      in an ACL. For more information, see [Access Control List (ACL)
      Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html).

      You specify each grantee as a type=value pair, where the type is one of the
      following:

      - `id` – if the value specified is the canonical user ID of an
        Amazon Web Services account
      - `uri` – if you are granting permissions to a predefined group
      - `emailAddress` – if the value specified is the email address of an
        Amazon Web Services account

        Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions:

        - US East (N. Virginia)
        - US West (N. California)
        - US West (Oregon)
        - Asia Pacific (Singapore)
        - Asia Pacific (Sydney)
        - Asia Pacific (Tokyo)
        - Europe (Ireland)
        - South America (São Paulo)

        For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the Amazon Web Services General Reference.

      For example, the following `x-amz-grant-write` header grants create, overwrite,
      and delete objects permission to LogDelivery group predefined by Amazon S3 and two Amazon Web Services accounts
      identified by their email addresses.

      `x-amz-grant-write: uri="http://acs.amazonaws.com/groups/s3/LogDelivery",
      id="111122223333", id="555566667777"`

    You can use either a canned ACL or specify access permissions explicitly. You cannot do
    both.

Grantee Values
:   You can specify the person (grantee) to whom you're assigning access rights (using request
    elements) in the following ways. For examples of how to specify these grantee values in JSON
    format, see the Amazon Web Services CLI example in  [Enabling Amazon S3 server
    access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html) in the *Amazon S3 User Guide*.

    - By the person's ID:

      `<>ID<><>GranteesEmail<>`

      DisplayName is optional and ignored in the request
    - By URI:

      `<>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<>`
    - By Email address:

      `<>Grantees@email.com<>&`

      The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl
      request, appears as the CanonicalUser.

      Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions:

      - US East (N. Virginia)
      - US West (N. California)
      - US West (Oregon)
      - Asia Pacific (Singapore)
      - Asia Pacific (Sydney)
      - Asia Pacific (Tokyo)
      - Europe (Ireland)
      - South America (São Paulo)

      For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the Amazon Web Services General Reference.

The following operations are related to `PutBucketAcl`:

- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
- [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketAclRequest`)

### `ACL` — BucketCannedACL (enum) · sent as header `x-amz-acl`

The canned ACL to apply to the bucket.

Values: `private`, `public-read`, `public-read-write`, `authenticated-read`

### `AccessControlPolicy` — AccessControlPolicy · sent as httpPayload

Contains the elements that set the ACL permissions for an object per grantee.

### `Bucket` — string · **required** · sent as httpLabel

The bucket to which to apply the ACL.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the data. This header must be used as a
message integrity check to verify that the request body was not corrupted in transit. For more
information, go to [RFC 1864.](http://www.ietf.org/rfc/rfc1864.txt)

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `GrantFullControl` — string · sent as header `x-amz-grant-full-control`

Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

### `GrantRead` — string · sent as header `x-amz-grant-read`

Allows grantee to list the objects in the bucket.

### `GrantReadACP` — string · sent as header `x-amz-grant-read-acp`

Allows grantee to read the bucket ACL.

### `GrantWrite` — string · sent as header `x-amz-grant-write`

Allows grantee to create new objects in the bucket.

For the bucket and object owners of existing objects, also allows deletions and overwrites of those
objects.

### `GrantWriteACP` — string · sent as header `x-amz-grant-write-acp`

Allows grantee to write the ACL for the applicable bucket.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Put bucket acl

The following example replaces existing ACL on a bucket. The ACL grants the bucket owner (specified using the owner ID) and write permission to the LogDelivery group. Because this is a replace operation, you must specify all the grants in your request. To incrementally add or remove ACL grants, you might use the console.

Input:

```json
{
  "Bucket": "examplebucket",
  "GrantFullControl": "id=examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484",
  "GrantWrite": "uri=http://acs.amazonaws.com/groups/s3/LogDelivery"
}
```
