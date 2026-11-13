# PutBucketInventoryConfiguration

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketInventoryConfigurationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?inventory`

This implementation of the `PUT` action adds an S3 Inventory configuration (identified by
the inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket.

Amazon S3 inventory generates inventories of the objects in the bucket on a daily or weekly basis, and
the results are published to a flat file. The bucket that is inventoried is called the
*source* bucket, and the bucket where the inventory flat file is stored is called
the *destination* bucket. The *destination* bucket must be in the
same Amazon Web Services Region as the *source* bucket.

When you configure an inventory for a *source* bucket, you specify the
*destination* bucket where you want the inventory to be stored, and whether to
generate the inventory daily or weekly. You can also configure what object metadata to include and
whether to inventory all object versions or only current versions. For more information, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) in the
Amazon S3 User Guide.

You must create a bucket policy on the *destination* bucket to grant
permissions to Amazon S3 to write objects to the bucket in the defined location. For an example policy, see
 [Granting
Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9).

**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have permission to perform the
    `s3:PutInventoryConfiguration` action. The bucket owner has this permission by
    default and can grant this permission to others.

    The `s3:PutInventoryConfiguration` permission allows a user to create an [S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)
    report that includes all object metadata fields available and to specify the destination bucket to
    store the inventory. A user with read access to objects in the destination bucket can also access
    all object metadata fields that are available in the inventory report.

    - **General purpose bucket permissions** - The
      `s3:PutInventoryConfiguration` permission is required in a policy. For more information
      about general purpose buckets permissions, see [Using Bucket Policies and User
      Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to
      this API operation, you must have the `s3express:PutInventoryConfiguration` permission in
      an IAM identity-based policy instead of a bucket policy.
      For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

    To restrict access to an inventory report, see [Restricting access to an Amazon S3 Inventory report](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-s3-inventory) in the
    *Amazon S3 User Guide*. For more information about the metadata fields available
    in S3 Inventory, see [Amazon S3 Inventory
    lists](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html#storage-inventory-contents) in the *Amazon S3 User Guide*. For more information about
    permissions, see [Permissions related to bucket subresource operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Identity and access management in
    Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

`PutBucketInventoryConfiguration` has the following special errors:

HTTP 400 Bad Request Error
:   *Code:* InvalidArgument

    *Cause:* Invalid Argument

HTTP 400 Bad Request Error
:   *Code:* TooManyConfigurations

    *Cause:* You are attempting to create a new configuration but have already
    reached the 1,000-configuration limit.

HTTP 403 Forbidden Error
:   *Cause:* You are not the owner of the specified bucket, or you do not have
    the `s3:PutInventoryConfiguration` bucket permission to set the configuration on the
    bucket.

The following operations are related to `PutBucketInventoryConfiguration`:

- [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
- [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
- [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketInventoryConfigurationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket where the inventory configuration will be stored.

**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

### `Id` — string · **required** · sent as query `id`

The ID used to identify the inventory configuration.

### `InventoryConfiguration` — InventoryConfiguration · **required** · sent as httpPayload

Specifies the inventory configuration.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code
`501 Not Implemented`.

## Output (`Unit`)

_None._
