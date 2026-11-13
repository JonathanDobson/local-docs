# Amazon Simple Storage Service — API reference

API version `2006-03-01` · protocol restXml · SDK for JavaScript v3 client `@aws-sdk/client-s3`

For information about using the Amazon S3 API—including authentication, signing requests, code examples, and error handling—see the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/Welcome.html).

Welcome to the *Amazon S3 API Reference*. This guide explains the Amazon Simple Storage Service (Amazon S3)
application programming interface (API).

Welcome to the *Amazon S3 API Reference*. This guide explains the Amazon Simple Storage Service (Amazon S3)
application programming interface (API).

You can use any toolkit that supports HTTP to use the REST API. You can even use a browser
to fetch objects, as long as they are anonymously readable.

The REST API uses the standard HTTP headers and status codes, so that standard browsers and toolkits work as expected. In some areas, we have added functionality to HTTP (for example, we added headers to support access control). In these cases, we have done our best to add the new functionality in a way that matched the style of standard HTTP usage.

The current version of the Amazon S3 API is `2006-03-01`.

Amazon S3 supports the REST API.

Support for SOAP over HTTP is deprecated, but it is still available over HTTPS.
However, new Amazon S3 features will not be supported for SOAP. We recommend that
you use either this REST API or the Amazon Web Services SDKs.

## Operations (112)

- [`AbortMultipartUpload`](operations/AbortMultipartUpload.md) — This operation aborts a multipart upload.
- [`CompleteMultipartUpload`](operations/CompleteMultipartUpload.md) — Completes a multipart upload by assembling previously uploaded parts.
- [`CopyObject`](operations/CopyObject.md) — Creates a copy of an object that is already stored in Amazon S3.
- [`CreateBucket`](operations/CreateBucket.md) — This action creates an Amazon S3 bucket.
- [`CreateBucketMetadataConfiguration`](operations/CreateBucketMetadataConfiguration.md) — Creates an S3 Metadata V2 metadata configuration for a general purpose bucket.
- [`CreateBucketMetadataTableConfiguration`](operations/CreateBucketMetadataTableConfiguration.md) — We recommend that you create your S3 Metadata configurations by using the V2 [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.…
- [`CreateMultipartUpload`](operations/CreateMultipartUpload.md) — End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs).
- [`CreateSession`](operations/CreateSession.md) — Creates a session that establishes temporary security credentials to support fast authentication and authorization for the Zonal endpoint API operations on directory buckets.
- [`DeleteBucket`](operations/DeleteBucket.md) — Deletes the S3 bucket.
- [`DeleteBucketAnalyticsConfiguration`](operations/DeleteBucketAnalyticsConfiguration.md) — This operation is not supported for directory buckets.
- [`DeleteBucketCors`](operations/DeleteBucketCors.md) — This operation is not supported for directory buckets.
- [`DeleteBucketEncryption`](operations/DeleteBucketEncryption.md) — This implementation of the DELETE action resets the default encryption for the bucket as server-side encryption with Amazon S3 managed keys (SSE-S3).
- [`DeleteBucketIntelligentTieringConfiguration`](operations/DeleteBucketIntelligentTieringConfiguration.md) — This operation is not supported for directory buckets.
- [`DeleteBucketInventoryConfiguration`](operations/DeleteBucketInventoryConfiguration.md) — Deletes an S3 Inventory configuration (identified by the inventory ID) from the bucket.
- [`DeleteBucketLifecycle`](operations/DeleteBucketLifecycle.md) — Deletes the lifecycle configuration from the specified bucket.
- [`DeleteBucketMetadataConfiguration`](operations/DeleteBucketMetadataConfiguration.md) — Deletes an S3 Metadata configuration from a general purpose bucket.
- [`DeleteBucketMetadataTableConfiguration`](operations/DeleteBucketMetadataTableConfiguration.md) — We recommend that you delete your S3 Metadata configurations by using the V2 [DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConf…
- [`DeleteBucketMetricsConfiguration`](operations/DeleteBucketMetricsConfiguration.md) — Deletes a metrics configuration for the Amazon CloudWatch request metrics (specified by the metrics configuration ID) from the bucket.
- [`DeleteBucketOwnershipControls`](operations/DeleteBucketOwnershipControls.md) — This operation is not supported for directory buckets.
- [`DeleteBucketPolicy`](operations/DeleteBucketPolicy.md) — Deletes the policy of a specified bucket.
- [`DeleteBucketReplication`](operations/DeleteBucketReplication.md) — This operation is not supported for directory buckets.
- [`DeleteBucketTagging`](operations/DeleteBucketTagging.md) — This operation is not supported for directory buckets.
- [`DeleteBucketWebsite`](operations/DeleteBucketWebsite.md) — This operation is not supported for directory buckets.
- [`DeleteObject`](operations/DeleteObject.md) — Removes an object from a bucket.
- [`DeleteObjectAnnotation`](operations/DeleteObjectAnnotation.md) — Deletes a specific annotation from an Amazon S3 object.
- [`DeleteObjectTagging`](operations/DeleteObjectTagging.md) — This operation is not supported for directory buckets.
- [`DeleteObjects`](operations/DeleteObjects.md) — This operation enables you to delete multiple objects from a bucket using a single HTTP request.
- [`DeletePublicAccessBlock`](operations/DeletePublicAccessBlock.md) — This operation is not supported for directory buckets.
- [`GetBucketAbac`](operations/GetBucketAbac.md) — Returns the attribute-based access control (ABAC) property of the general purpose bucket.
- [`GetBucketAccelerateConfiguration`](operations/GetBucketAccelerateConfiguration.md) — This operation is not supported for directory buckets.
- [`GetBucketAcl`](operations/GetBucketAcl.md) — This operation is not supported for directory buckets.
- [`GetBucketAnalyticsConfiguration`](operations/GetBucketAnalyticsConfiguration.md) — This operation is not supported for directory buckets.
- [`GetBucketCors`](operations/GetBucketCors.md) — This operation is not supported for directory buckets.
- [`GetBucketEncryption`](operations/GetBucketEncryption.md) — Returns the default encryption configuration for an Amazon S3 bucket.
- [`GetBucketIntelligentTieringConfiguration`](operations/GetBucketIntelligentTieringConfiguration.md) — This operation is not supported for directory buckets.
- [`GetBucketInventoryConfiguration`](operations/GetBucketInventoryConfiguration.md) — Returns an S3 Inventory configuration (identified by the inventory configuration ID) from the bucket.
- [`GetBucketLifecycleConfiguration`](operations/GetBucketLifecycleConfiguration.md) — Returns the lifecycle configuration information set on the bucket.
- [`GetBucketLocation`](operations/GetBucketLocation.md) — Using the `GetBucketLocation` operation is no longer a best practice.
- [`GetBucketLogging`](operations/GetBucketLogging.md) — This operation is not supported for directory buckets.
- [`GetBucketMetadataConfiguration`](operations/GetBucketMetadataConfiguration.md) — Retrieves the S3 Metadata configuration for a general purpose bucket.
- [`GetBucketMetadataTableConfiguration`](operations/GetBucketMetadataTableConfiguration.md) — We recommend that you retrieve your S3 Metadata configurations by using the V2 [GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfigur…
- [`GetBucketMetricsConfiguration`](operations/GetBucketMetricsConfiguration.md) — Gets a metrics configuration (specified by the metrics configuration ID) from the bucket.
- [`GetBucketNotificationConfiguration`](operations/GetBucketNotificationConfiguration.md) — This operation is not supported for directory buckets.
- [`GetBucketOwnershipControls`](operations/GetBucketOwnershipControls.md) — This operation is not supported for directory buckets.
- [`GetBucketPolicy`](operations/GetBucketPolicy.md) — Returns the policy of a specified bucket.
- [`GetBucketPolicyStatus`](operations/GetBucketPolicyStatus.md) — This operation is not supported for directory buckets.
- [`GetBucketReplication`](operations/GetBucketReplication.md) — This operation is not supported for directory buckets.
- [`GetBucketRequestPayment`](operations/GetBucketRequestPayment.md) — This operation is not supported for directory buckets.
- [`GetBucketTagging`](operations/GetBucketTagging.md) — This operation is not supported for directory buckets.
- [`GetBucketVersioning`](operations/GetBucketVersioning.md) — This operation is not supported for directory buckets.
- [`GetBucketWebsite`](operations/GetBucketWebsite.md) — This operation is not supported for directory buckets.
- [`GetObject`](operations/GetObject.md) — Retrieves an object from Amazon S3.
- [`GetObjectAcl`](operations/GetObjectAcl.md) — This operation is not supported for directory buckets.
- [`GetObjectAnnotation`](operations/GetObjectAnnotation.md) — Retrieves an annotation from an Amazon S3 object.
- [`GetObjectAttributes`](operations/GetObjectAttributes.md) — Retrieves all of the metadata from an object without returning the object itself.
- [`GetObjectLegalHold`](operations/GetObjectLegalHold.md) — This operation is not supported for directory buckets.
- [`GetObjectLockConfiguration`](operations/GetObjectLockConfiguration.md) — This operation is not supported for directory buckets.
- [`GetObjectRetention`](operations/GetObjectRetention.md) — This operation is not supported for directory buckets.
- [`GetObjectTagging`](operations/GetObjectTagging.md) — This operation is not supported for directory buckets.
- [`GetObjectTorrent`](operations/GetObjectTorrent.md) — This operation is not supported for directory buckets.
- [`GetPublicAccessBlock`](operations/GetPublicAccessBlock.md) — This operation is not supported for directory buckets.
- [`HeadBucket`](operations/HeadBucket.md) — You can use this operation to determine if a bucket exists and if you have permission to access it.
- [`HeadObject`](operations/HeadObject.md) — The `HEAD` operation retrieves metadata from an object without returning the object itself.
- [`ListBucketAnalyticsConfigurations`](operations/ListBucketAnalyticsConfigurations.md) — This operation is not supported for directory buckets.
- [`ListBucketIntelligentTieringConfigurations`](operations/ListBucketIntelligentTieringConfigurations.md) — This operation is not supported for directory buckets.
- [`ListBucketInventoryConfigurations`](operations/ListBucketInventoryConfigurations.md) — Returns a list of S3 Inventory configurations for the bucket.
- [`ListBucketMetricsConfigurations`](operations/ListBucketMetricsConfigurations.md) — Lists the metrics configurations for the bucket.
- [`ListBuckets`](operations/ListBuckets.md) — This operation is not supported for directory buckets.
- [`ListDirectoryBuckets`](operations/ListDirectoryBuckets.md) — Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request.
- [`ListMultipartUploads`](operations/ListMultipartUploads.md) — This operation lists in-progress multipart uploads in a bucket.
- [`ListObjectAnnotations`](operations/ListObjectAnnotations.md) — Lists the annotations attached to an Amazon S3 object.
- [`ListObjectVersions`](operations/ListObjectVersions.md) — This operation is not supported for directory buckets.
- [`ListObjects`](operations/ListObjects.md) — This operation is not supported for directory buckets.
- [`ListObjectsV2`](operations/ListObjectsV2.md) — Returns some or all (up to 1,000) of the objects in a bucket with each request.
- [`ListParts`](operations/ListParts.md) — Lists the parts that have been uploaded for a specific multipart upload.
- [`PutBucketAbac`](operations/PutBucketAbac.md) — Sets the attribute-based access control (ABAC) property of the general purpose bucket.
- [`PutBucketAccelerateConfiguration`](operations/PutBucketAccelerateConfiguration.md) — This operation is not supported for directory buckets.
- [`PutBucketAcl`](operations/PutBucketAcl.md) — End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs).
- [`PutBucketAnalyticsConfiguration`](operations/PutBucketAnalyticsConfiguration.md) — This operation is not supported for directory buckets.
- [`PutBucketCors`](operations/PutBucketCors.md) — This operation is not supported for directory buckets.
- [`PutBucketEncryption`](operations/PutBucketEncryption.md) — This operation configures default encryption and Amazon S3 Bucket Keys for an existing bucket.
- [`PutBucketIntelligentTieringConfiguration`](operations/PutBucketIntelligentTieringConfiguration.md) — This operation is not supported for directory buckets.
- [`PutBucketInventoryConfiguration`](operations/PutBucketInventoryConfiguration.md) — This implementation of the `PUT` action adds an S3 Inventory configuration (identified by the inventory ID) to the bucket.
- [`PutBucketLifecycleConfiguration`](operations/PutBucketLifecycleConfiguration.md) — Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration.
- [`PutBucketLogging`](operations/PutBucketLogging.md) — End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs).
- [`PutBucketMetricsConfiguration`](operations/PutBucketMetricsConfiguration.md) — Sets a metrics configuration (specified by the metrics configuration ID) for the bucket.
- [`PutBucketNotificationConfiguration`](operations/PutBucketNotificationConfiguration.md) — This operation is not supported for directory buckets.
- [`PutBucketOwnershipControls`](operations/PutBucketOwnershipControls.md) — This operation is not supported for directory buckets.
- [`PutBucketPolicy`](operations/PutBucketPolicy.md) — Applies an Amazon S3 bucket policy to an Amazon S3 bucket.
- [`PutBucketReplication`](operations/PutBucketReplication.md) — This operation is not supported for directory buckets.
- [`PutBucketRequestPayment`](operations/PutBucketRequestPayment.md) — This operation is not supported for directory buckets.
- [`PutBucketTagging`](operations/PutBucketTagging.md) — This operation is not supported for directory buckets.
- [`PutBucketVersioning`](operations/PutBucketVersioning.md) — This operation is not supported for directory buckets.
- [`PutBucketWebsite`](operations/PutBucketWebsite.md) — This operation is not supported for directory buckets.
- [`PutObject`](operations/PutObject.md) — End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs).
- [`PutObjectAcl`](operations/PutObjectAcl.md) — End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs).
- [`PutObjectAnnotation`](operations/PutObjectAnnotation.md) — Attaches an annotation to an Amazon S3 object.
- [`PutObjectLegalHold`](operations/PutObjectLegalHold.md) — This operation is not supported for directory buckets.
- [`PutObjectLockConfiguration`](operations/PutObjectLockConfiguration.md) — This operation is not supported for directory buckets.
- [`PutObjectRetention`](operations/PutObjectRetention.md) — This operation is not supported for directory buckets.
- [`PutObjectTagging`](operations/PutObjectTagging.md) — This operation is not supported for directory buckets.
- [`PutPublicAccessBlock`](operations/PutPublicAccessBlock.md) — This operation is not supported for directory buckets.
- [`RenameObject`](operations/RenameObject.md) — Renames an existing object in a directory bucket that uses the S3 Express One Zone storage class.
- [`RestoreObject`](operations/RestoreObject.md) — This operation is not supported for directory buckets.
- [`SelectObjectContent`](operations/SelectObjectContent.md) — This operation is not supported for directory buckets.
- [`UpdateBucketMetadataAnnotationTableConfiguration`](operations/UpdateBucketMetadataAnnotationTableConfiguration.md) — Updates the annotation table configuration for an Amazon S3 bucket's metadata configuration.
- [`UpdateBucketMetadataInventoryTableConfiguration`](operations/UpdateBucketMetadataInventoryTableConfiguration.md) — Enables or disables a live inventory table for an S3 Metadata configuration on a general purpose bucket.
- [`UpdateBucketMetadataJournalTableConfiguration`](operations/UpdateBucketMetadataJournalTableConfiguration.md) — Enables or disables journal table record expiration for an S3 Metadata configuration on a general purpose bucket.
- [`UpdateObjectEncryption`](operations/UpdateObjectEncryption.md) — This operation is not supported for directory buckets or Amazon S3 on Outposts buckets.
- [`UploadPart`](operations/UploadPart.md) — Uploads a part in a multipart upload.
- [`UploadPartCopy`](operations/UploadPartCopy.md) — Uploads a part by copying data from an existing object as data source.
- [`WriteGetObjectResponse`](operations/WriteGetObjectResponse.md) — This operation is not supported for directory buckets.
