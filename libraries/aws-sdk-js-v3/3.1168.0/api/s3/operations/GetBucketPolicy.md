# GetBucketPolicy

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketPolicyCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?policy`

Returns the policy of a specified bucket.

**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   If you are using an identity other than the root user of the Amazon Web Services account that owns the
    bucket, the calling identity must both have the `GetBucketPolicy` permissions on the
    specified bucket and belong to the bucket owner's account in order to use this operation.

    If you don't have `GetBucketPolicy` permissions, Amazon S3 returns a `403 Access
    Denied` error. If you have the correct permissions, but you're not using an identity that
    belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not Allowed`
    error.

    To ensure that bucket owners don't inadvertently lock themselves out of their own buckets,
    the root principal in a bucket owner's Amazon Web Services account can perform the
    `GetBucketPolicy`, `PutBucketPolicy`, and
    `DeleteBucketPolicy` API actions, even if their bucket policy explicitly denies the
    root principal's access. Bucket owner root principals can only be blocked from performing these
    API actions by VPC endpoint policies and Amazon Web Services Organizations policies.

    - **General purpose bucket permissions** - The
      `s3:GetBucketPolicy` permission is required in a policy. For more information
      about general purpose buckets bucket policies, see [Using Bucket Policies and User
      Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to
      this API operation, you must have the `s3express:GetBucketPolicy` permission in
      an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the Amazon Web Services account that owns the resource.
      For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

Example bucket policies
:   **General purpose buckets example bucket policies** - See [Bucket policy
    examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) in the *Amazon S3 User Guide*.

    **Directory bucket example bucket policies** - See [Example
    bucket policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

The following action is related to `GetBucketPolicy`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketPolicyRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name to get the bucket policy for.

**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

**Access points** - When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

**Object Lambda access points** - When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name.
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned.
For more information about `InvalidAccessPointAliasError`, see [List of
Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList).

Object Lambda access points are not supported by directory buckets.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code
`501 Not Implemented`.

## Output (`GetBucketPolicyOutput`)

### `Policy` — string · sent as httpPayload

The bucket policy as a JSON document.

## Examples

### To get bucket policy

The following example returns bucket policy associated with a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "Policy": "{\"Version\":\"2008-10-17\",&TCX5-2025-waiver;\"Id\":\"LogPolicy\",\"Statement\":[{\"Sid\":\"Enables the log delivery group to publish logs to your bucket \",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"111122223333\"},\"Action\":[\"s3:GetBucketAcl\",\"s3:GetObjectAcl\",\"s3:PutObject\"],\"Resource\":[\"arn:aws:s3:::policytest1/*\",\"arn:aws:s3:::policytest1\"]}]}"
}
```
