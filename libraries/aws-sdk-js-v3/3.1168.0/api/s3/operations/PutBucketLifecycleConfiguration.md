# PutBucketLifecycleConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketLifecycleConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?lifecycle`

Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
configuration. Keep in mind that this will overwrite an existing lifecycle configuration, so if you want
to retain any configuration details, they must be included in the new lifecycle configuration. For
information about lifecycle configuration, see [Managing your storage
lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
prefix, one or more object tags, object size, or any combination of these. Accordingly, this section
describes the latest API. The previous version of the API supported filtering based only on an object
key name prefix, which is supported for backward compatibility. For the related API description, see
[PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html).

Rules
:   You specify the lifecycle configuration in your request body. The lifecycle configuration is
    specified as XML consisting of one or more rules. An Amazon S3 Lifecycle configuration can have up to
    1,000 rules. This limit is not adjustable.

    Bucket lifecycle configuration supports specifying a lifecycle rule using an object key name
    prefix, one or more object tags, object size, or any combination of these. Accordingly, this
    section describes the latest API. The previous version of the API supported filtering based only
    on an object key name prefix, which is supported for backward compatibility for general purpose
    buckets. For the related API description, see [PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html).

    Lifecyle configurations for directory buckets only support expiring objects and cancelling
    multipart uploads. Expiring of versioned objects,transitions and tag filters are not
    supported.

    A lifecycle rule consists of the following:

    - A filter identifying a subset of objects to which the rule applies. The filter can be
      based on a key name prefix, object tags, object size, or any combination of these.
    - A status indicating whether the rule is in effect.
    - One or more lifecycle transition and expiration actions that you want Amazon S3 to perform on
      the objects identified by the filter. If the state of your bucket is versioning-enabled or
      versioning-suspended, you can have many versions of the same object (one current version and
      zero or more noncurrent versions). Amazon S3 provides predefined actions that you can specify for
      current and noncurrent object versions.

    For more information, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) and
    [Lifecycle
    Configuration Elements](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html).

Permissions
:   - **General purpose bucket permissions** - By default, all Amazon S3
      resources are private, including buckets, objects, and related subresources (for example,
      lifecycle configuration and website configuration). Only the resource owner (that is, the
      Amazon Web Services account that created it) can access the resource. The resource owner can optionally
      grant access permissions to others by writing an access policy. For this operation, a user
      must have the `s3:PutLifecycleConfiguration` permission.

      You can also explicitly deny permissions. An explicit deny also supersedes any other
      permissions. If you want to block users or accounts from removing or deleting objects from
      your bucket, you must deny them permissions for the following actions:

      - `s3:DeleteObject`
      - `s3:DeleteObjectVersion`
      - `s3:PutLifecycleConfiguration`

        For more information about permissions, see [Managing Access Permissions to
        Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

    - **Directory bucket permissions** - You must have the
      `s3express:PutLifecycleConfiguration` permission in an IAM identity-based policy
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

    The following operations are related to `PutBucketLifecycleConfiguration`:

    - [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
    - [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketLifecycleConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to set the configuration.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum) · sent as header `x-amz-sdk-checksum-algorithm`

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
`x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
parameter.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `LifecycleConfiguration` — BucketLifecycleConfiguration · sent as httpPayload

Container for lifecycle rules. You can add as many as 1,000 rules.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `TransitionDefaultMinimumObjectSize` — TransitionDefaultMinimumObjectSize (enum) · sent as header `x-amz-transition-default-minimum-object-size`

Indicates which default minimum object size behavior is applied to the lifecycle
configuration.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
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

## Output (`PutBucketLifecycleConfigurationOutput`)

### `TransitionDefaultMinimumObjectSize` — TransitionDefaultMinimumObjectSize (enum) · sent as header `x-amz-transition-default-minimum-object-size`

Indicates which default minimum object size behavior is applied to the lifecycle
configuration.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
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

### Put bucket lifecycle

The following example replaces existing lifecycle configuration, if any, on the specified bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "LifecycleConfiguration": {
    "Rules": [
      {
        "Filter": {
          "Prefix": "documents/"
        },
        "Status": "Enabled",
        "Transitions": [
          {
            "Days": 365,
            "StorageClass": "GLACIER"
          }
        ],
        "Expiration": {
          "Days": 3650
        },
        "ID": "TestOnly"
      }
    ]
  }
}
```
