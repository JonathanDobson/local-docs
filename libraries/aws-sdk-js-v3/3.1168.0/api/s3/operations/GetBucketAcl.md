# GetBucketAcl

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketAclCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?acl`

This operation is not supported for directory buckets.

This implementation of the `GET` action uses the `acl` subresource to return
the access control list (ACL) of a bucket. To use `GET` to return the ACL of the bucket, you
must have the `READ_ACP` access to the bucket. If `READ_ACP` permission is granted
to the anonymous user, you can return the ACL of the bucket without using an authorization
header.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, requests to read
ACLs are still supported and return the `bucket-owner-full-control` ACL with the owner
being the account that created the bucket. For more information, see  [Controlling object ownership and
disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

The following operations are related to `GetBucketAcl`:

- [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)

## Input (`GetBucketAclRequest`)

### `Bucket` — string · **required** · sent as httpLabel

Specifies the S3 bucket whose ACL is being requested.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketAclOutput`)

### `Owner` — Owner

Container for the bucket owner's ID.

### `Grants` — list<Grant>

A list of grants.
