# ListBucketInventoryConfigurations

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListBucketInventoryConfigurationsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?inventory&x-id=ListBucketInventoryConfigurations`

Returns a list of S3 Inventory configurations for the bucket. You can have up to 1,000 inventory
configurations per bucket.

This action supports list pagination and does not return more than 100 configurations at a time.
Always check the `IsTruncated` element in the response. If there are no more configurations
to list, `IsTruncated` is set to false. If there are more configurations to list,
`IsTruncated` is set to true, and there is a value in `NextContinuationToken`.
You use the `NextContinuationToken` value to continue the pagination of the list by passing
the value in continuation-token in the request to `GET` the next page.

**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported.
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   To use this operation, you must have permissions to perform the
    `s3:GetInventoryConfiguration` action. The bucket owner has this permission by default. The
    bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3
    Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

    - **General purpose bucket permissions** - The
      `s3:GetInventoryConfiguration` permission is required in a policy. For more information
      about general purpose buckets permissions, see [Using Bucket Policies and User
      Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) in the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to
      this API operation, you must have the `s3express:GetInventoryConfiguration` permission in
      an IAM identity-based policy instead of a bucket policy.
      For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

For information about the Amazon S3 inventory feature, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html)

The following operations are related to `ListBucketInventoryConfigurations`:

- [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
- [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
- [PutBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListBucketInventoryConfigurationsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket containing the inventory configurations to retrieve.

**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

### `ContinuationToken` — string · sent as query `continuation-token`

The marker used to continue an inventory configuration listing that has been truncated. Use the
`NextContinuationToken` from a previously truncated list response to continue the listing.
The continuation token is an opaque value that Amazon S3 understands.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code
`501 Not Implemented`.

## Output (`ListBucketInventoryConfigurationsOutput`)

### `ContinuationToken` — string

If sent in the request, the marker that is used as a starting point for this inventory configuration
list response.

### `InventoryConfigurationList` — list<InventoryConfiguration>

The list of inventory configurations for a bucket.

### `IsTruncated` — boolean

Tells whether the returned list of inventory configurations is complete. A value of true indicates
that the list is not complete and the NextContinuationToken is provided for a subsequent request.

### `NextContinuationToken` — string

The marker used to continue this inventory configuration listing. Use the
`NextContinuationToken` from this response to continue the listing in a subsequent request.
The continuation token is an opaque value that Amazon S3 understands.
