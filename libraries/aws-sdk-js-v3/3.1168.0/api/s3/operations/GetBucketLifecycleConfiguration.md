# GetBucketLifecycleConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketLifecycleConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?lifecycle`

Returns the lifecycle configuration information set on the bucket. For information about lifecycle
configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
prefix, one or more object tags, object size, or any combination of these. Accordingly, this section
describes the latest API, which is compatible with the new functionality. The previous version of the
API supported filtering based only on an object key name prefix, which is supported for general purpose
buckets for backward compatibility. For the related API description, see [GetBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html).

Lifecyle configurations for directory buckets only support expiring objects and cancelling
multipart uploads. Expiring of versioned objects, transitions and tag filters are not
supported.

Permissions
:   - **General purpose bucket permissions** - By default, all Amazon S3
      resources are private, including buckets, objects, and related subresources (for example,
      lifecycle configuration and website configuration). Only the resource owner (that is, the
      Amazon Web Services account that created it) can access the resource. The resource owner can optionally
      grant access permissions to others by writing an access policy. For this operation, a user
      must have the `s3:GetLifecycleConfiguration` permission.

      For more information about permissions, see [Managing Access Permissions to Your
      Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

    - **Directory bucket permissions** - You must have the
      `s3express:GetLifecycleConfiguration` permission in an IAM identity-based policy
      to use this operation. Cross-account access to this API operation isn't supported. The
      resource owner can optionally grant access permissions to others by creating a role or user
      for them as long as they are within the same account as the owner and resource.

      For more information about directory bucket policies and permissions, see [Authorizing Regional endpoint APIs with IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User
      Guide*.

      **Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
      For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
      *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
      *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is
    `s3express-control.region.amazonaws.com`.

`GetBucketLifecycleConfiguration` has the following special error:

- Error code: `NoSuchLifecycleConfiguration`

  - Description: The lifecycle configuration does not exist.
  - HTTP Status Code: 404 Not Found
  - SOAP Fault Code Prefix: Client

The following operations are related to `GetBucketLifecycleConfiguration`:

- [GetBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html)
- [PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html)
- [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketLifecycleConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to get the lifecycle information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

## Output (`GetBucketLifecycleConfigurationOutput`)

### `Rules` — list<LifecycleRule>

Container for a lifecycle rule.

### `TransitionDefaultMinimumObjectSize` — TransitionDefaultMinimumObjectSize (enum) · sent as header `x-amz-transition-default-minimum-object-size`

Indicates which default minimum object size behavior is applied to the lifecycle
configuration.

This parameter applies to general purpose buckets only. It isn't supported for directory bucket
lifecycle configurations.

- `all_storage_classes_128K` - Objects smaller than 128 KB will not transition to
  any storage class by default.
- `varies_by_storage_class` - Objects smaller than 128 KB will transition to Glacier
  Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes
  will prevent transitions smaller than 128 KB.

To customize the minimum object size for any transition you can add a filter that specifies a custom
`ObjectSizeGreaterThan` or `ObjectSizeLessThan` in the body of your transition
rule. Custom filters always take precedence over the default transition behavior.

Values: `varies_by_storage_class`, `all_storage_classes_128K`

## Examples

### To get lifecycle configuration on a bucket

The following example retrieves lifecycle configuration on set on a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "Rules": [
    {
      "Prefix": "TaxDocs",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 365,
          "StorageClass": "STANDARD_IA"
        }
      ],
      "ID": "Rule for TaxDocs/"
    }
  ]
}
```
