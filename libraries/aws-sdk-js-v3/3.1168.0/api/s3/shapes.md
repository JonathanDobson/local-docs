# Amazon Simple Storage Service — data types

Structures, unions and enums used by the operations (operation inputs and outputs are on the operation pages).

## AbacStatus (structure)

The ABAC status of the general purpose bucket. When ABAC is enabled for the general purpose bucket, you can use tags to manage access to the general purpose buckets as well as for cost tracking purposes. When ABAC is disabled for the general purpose buckets, you can only use tags for cost tracking purposes. For more information, see [Using tags with S3 general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html).

### `Status` — BucketAbacStatus (enum)

The ABAC status of the general purpose bucket.

Values: `Enabled`, `Disabled`

## AbortIncompleteMultipartUpload (structure)

Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before
permanently removing all parts of the upload. For more information, see  [Aborting
Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) in the
*Amazon S3 User Guide*.

### `DaysAfterInitiation` — integer

Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.

## AccelerateConfiguration (structure)

Configures the transfer acceleration state for an Amazon S3 bucket. For more information, see [Amazon S3 Transfer
Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) in the *Amazon S3 User Guide*.

### `Status` — BucketAccelerateStatus (enum)

Specifies the transfer acceleration status of the bucket.

Values: `Enabled`, `Suspended`

## AccessControlPolicy (structure)

Contains the elements that set the ACL permissions for an object per grantee.

### `Grants` — list<Grant>

A list of grants.

### `Owner` — Owner

Container for the bucket owner's display name and ID.

## AccessControlTranslation (structure)

A container for information about access control for replicas.

### `Owner` — OwnerOverride (enum) · **required**

Specifies the replica ownership. For default and valid values, see [PUT bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) in the
*Amazon S3 API Reference*.

Values: `Destination`

## AnalyticsAndOperator (structure)

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
operator must have at least two predicates in any combination, and an object must match all of the
predicates for the filter to apply.

### `Prefix` — string

The prefix to use when evaluating an AND predicate: The prefix that an object must have to be
included in the metrics results.

### `Tags` — list<Tag>

The list of tags to use when evaluating an AND predicate.

## AnalyticsConfiguration (structure)

Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.

### `Id` — string · **required**

The ID that identifies the analytics configuration.

### `Filter` — AnalyticsFilter

The filter used to describe a set of objects for analyses. A filter must have exactly one prefix,
one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be
considered in any analysis.

### `StorageClassAnalysis` — StorageClassAnalysis · **required**

Contains data related to access patterns to be collected and made available to analyze the
tradeoffs between different storage classes.

## AnalyticsExportDestination (structure)

Where to publish the analytics results.

### `S3BucketDestination` — AnalyticsS3BucketDestination · **required**

A destination signifying output to an S3 bucket.

## AnalyticsFilter (union)

The filter used to describe a set of objects for analyses. A filter must have exactly one prefix,
one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be
considered in any analysis.

### `Prefix` — string

The prefix to use when evaluating an analytics filter.

### `Tag` — Tag

The tag to use when evaluating an analytics filter.

### `And` — AnalyticsAndOperator

A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The
operator must have at least two predicates.

## AnalyticsS3BucketDestination (structure)

Contains information about where to publish the analytics results.

### `Format` — AnalyticsS3ExportFileFormat (enum) · **required**

Specifies the file format used when exporting data to Amazon S3.

Values: `CSV`

### `BucketAccountId` — string

The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not
validated before exporting data.

Although this value is optional, we strongly recommend that you set it to help prevent problems
if the destination bucket ownership changes.

### `Bucket` — string · **required**

The Amazon Resource Name (ARN) of the bucket to which data is exported.

### `Prefix` — string

The prefix to use when exporting data. The prefix is prepended to all results.

## AnalyticsS3ExportFileFormat (enum)

Values: `CSV`

## AnnotationConfigurationState (enum)

Values: `ENABLED`, `DISABLED`

## AnnotationDirective (enum)

Values: `COPY`, `EXCLUDE`

## AnnotationEntry (structure)

Describes a single annotation attached to an object, including its name, last modified time,
size, ETag, checksum algorithm, and replication status. Returned in the response from
`ListObjectAnnotations`.

### `AnnotationName` — string · **required**

The name of the annotation.

### `LastModified` — timestamp · **required**

The date and time the annotation was last modified.

### `ETag` — string

The entity tag of the annotation.

### `ChecksumAlgorithm` — list<ChecksumAlgorithm (enum)>

The checksum algorithm used for the annotation.

### `Size` — long · **required**

The size of the annotation payload, in bytes.

### `ReplicationStatus` — ReplicationStatus (enum)

The replication status of the annotation.

Values: `COMPLETE`, `PENDING`, `FAILED`, `REPLICA`, `COMPLETED`

## AnnotationTableConfiguration (structure)

Specifies the configuration for the annotation table associated with a bucket's Amazon S3 Metadata
configuration. The annotation table is an Iceberg table that records annotation events for objects
in the bucket.

### `ConfigurationState` — AnnotationConfigurationState (enum) · **required**

The state of the annotation table. Valid values are `ENABLED` and `DISABLED`.

Values: `ENABLED`, `DISABLED`

### `EncryptionConfiguration` — MetadataTableEncryptionConfiguration

The encryption settings for an S3 Metadata journal table or inventory table configuration.

### `Role` — string

The ARN of the IAM role used to manage the annotation table.

## AnnotationTableConfigurationResult (structure)

Contains the current state of the annotation table associated with a bucket's Amazon S3 Metadata
configuration, including its provisioning status and identifiers.

### `ConfigurationState` — AnnotationConfigurationState (enum) · **required**

The current configuration state of the annotation table.

Values: `ENABLED`, `DISABLED`

### `TableStatus` — string

The provisioning status of the annotation table. Possible values: `CREATING`, `BACKFILLING`, `ACTIVE`, `FAILED`.

### `Error` — ErrorDetails

If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2
`CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code and error message.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `TableName` — string

The name of the annotation table.

### `TableArn` — string

The ARN of the annotation table.

### `Role` — string

The ARN of the IAM role associated with the annotation table.

## AnnotationTableConfigurationUpdates (structure)

Specifies updates to apply to the annotation table configuration. Used as the request body for
`UpdateBucketMetadataAnnotationTableConfiguration`.

### `ConfigurationState` — AnnotationConfigurationState (enum) · **required**

The new configuration state to apply.

Values: `ENABLED`, `DISABLED`

### `EncryptionConfiguration` — MetadataTableEncryptionConfiguration

The encryption settings for an S3 Metadata journal table or inventory table configuration.

### `Role` — string

The new IAM role ARN to apply.

## ArchiveStatus (enum)

Values: `ARCHIVE_ACCESS`, `DEEP_ARCHIVE_ACCESS`

## BlockedEncryptionTypes (structure)

A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type. For example, blocking an encryption type will block `PutObject`, `CopyObject`, `PostObject`, multipart upload, and replication requests to the bucket for objects with the specified encryption type. However, you can continue to read and list any pre-existing objects already encrypted with the specified encryption type. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).

This data type is used with the following actions:

- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
- [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)
- [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)

Permissions
:   You must have the `s3:PutEncryptionConfiguration` permission to block or unblock an encryption type for a bucket.

    You must have the `s3:GetEncryptionConfiguration` permission to view a bucket's encryption type.

### `EncryptionType` — list<EncryptionType (enum)>

The object encryption type that you want to block or unblock for an Amazon S3 general purpose bucket.

Currently, this parameter only supports blocking or unblocking server side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).

## Bucket (structure)

In terms of implementation, a Bucket is a resource.

### `Name` — string

The name of the bucket.

### `CreationDate` — timestamp

Date the bucket was created. This date can change when making changes to your bucket, such as
editing its bucket policy.

### `BucketRegion` — string

`BucketRegion` indicates the Amazon Web Services region where the bucket is located. If the request
contains at least one valid parameter, it is included in the response.

### `BucketArn` — string

The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all
of Amazon Web Services.

This parameter is only supported for S3 directory buckets. For more information, see [Using tags with
directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).

## BucketAbacStatus (enum)

Values: `Enabled`, `Disabled`

## BucketAccelerateStatus (enum)

Values: `Enabled`, `Suspended`

## BucketCannedACL (enum)

Values: `private`, `public-read`, `public-read-write`, `authenticated-read`

## BucketInfo (structure)

Specifies the information about the bucket that will be created. For more information about
directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the
*Amazon S3 User Guide*.

This functionality is only supported by directory buckets.

### `DataRedundancy` — DataRedundancy (enum)

The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.

Values: `SingleAvailabilityZone`, `SingleLocalZone`

### `Type` — BucketType (enum)

The type of bucket.

Values: `Directory`

## BucketLifecycleConfiguration (structure)

Specifies the lifecycle configuration for objects in an Amazon S3 bucket. For more information, see
[Object Lifecycle
Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

### `Rules` — list<LifecycleRule> · **required**

A lifecycle rule for individual objects in an Amazon S3 bucket.

## BucketLocationConstraint (enum)

Values: `af-south-1`, `ap-east-1`, `ap-east-2`, `ap-northeast-1`, `ap-northeast-2`, `ap-northeast-3`, `ap-south-1`, `ap-south-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-4`, `ap-southeast-5`, `ap-southeast-6`, `ap-southeast-7`, `ca-central-1`, `ca-west-1`, `cn-north-1`, `cn-northwest-1`, `EU`, `eu-central-1`, `eu-central-2`, `eu-north-1`, `eu-south-1`, `eu-south-2`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `il-central-1`, `me-central-1`, `me-south-1`, `mx-central-1`, `sa-east-1`, `us-east-2`, `us-gov-east-1`, `us-gov-west-1`, `us-west-1`, `us-west-2`

## BucketLoggingStatus (structure)

Container for logging status information.

### `LoggingEnabled` — LoggingEnabled

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a
bucket. For more information, see [PUT Bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html) in the
*Amazon S3 API Reference*.

## BucketLogsPermission (enum)

Values: `FULL_CONTROL`, `READ`, `WRITE`

## BucketNamespace (enum)

Values: `account-regional`, `global`

## BucketType (enum)

Values: `Directory`

## BucketVersioningStatus (enum)

Values: `Enabled`, `Suspended`

## CORSConfiguration (structure)

Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information,
see [Enabling Cross-Origin Resource
Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the *Amazon S3 User Guide*.

### `CORSRules` — list<CORSRule> · **required**

A set of origins and methods (cross-origin access that you want to allow). You can add up to 100
rules to the configuration.

## CORSRule (structure)

Specifies a cross-origin access rule for an Amazon S3 bucket.

### `ID` — string

Unique identifier for the rule. The value cannot be longer than 255 characters.

### `AllowedHeaders` — list<string>

Headers that are specified in the `Access-Control-Request-Headers` header. These headers
are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns
any requested headers that are allowed.

### `AllowedMethods` — list<string> · **required**

An HTTP method that you allow the origin to execute. Valid values are `GET`,
`PUT`, `HEAD`, `POST`, and `DELETE`.

### `AllowedOrigins` — list<string> · **required**

One or more origins you want customers to be able to access the bucket from.

### `ExposeHeaders` — list<string>

One or more headers in the response that you want customers to be able to access from their
applications (for example, from a JavaScript `XMLHttpRequest` object).

### `MaxAgeSeconds` — integer

The time in seconds that your browser is to cache the preflight response for the specified
resource.

## CSVInput (structure)

Describes how an uncompressed comma-separated values (CSV)-formatted input object is
formatted.

### `FileHeaderInfo` — FileHeaderInfo (enum)

Describes the first line of input. Valid values are:

- `NONE`: First line is not a header.
- `IGNORE`: First line is a header, but you can't use the header values to indicate the
  column in an expression. You can use column position (such as \_1, \_2, …) to indicate the column
  (`SELECT s._1 FROM OBJECT s`).
- `Use`: First line is a header, and you can use the header value to identify a column
  in an expression (`SELECT "name" FROM OBJECT`).

Values: `USE`, `IGNORE`, `NONE`

### `Comments` — string

A single character used to indicate that a row should be ignored when the character is present at
the start of that row. You can specify any character to indicate a comment line. The default character
is `#`.

Default: `#`

### `QuoteEscapeCharacter` — string

A single character used for escaping the quotation mark character inside an already escaped value.
For example, the value `""" a , b """` is parsed as `" a , b "`.

### `RecordDelimiter` — string

A single character used to separate individual records in the input. Instead of the default value,
you can specify an arbitrary delimiter.

### `FieldDelimiter` — string

A single character used to separate individual fields in a record. You can specify an arbitrary
delimiter.

### `QuoteCharacter` — string

A single character used for escaping when the field delimiter is part of the value. For example, if
the value is `a, b`, Amazon S3 wraps this field value in quotation marks, as follows: `" a ,
b "`.

Type: String

Default: `"`

Ancestors: `CSV`

### `AllowQuotedRecordDelimiter` — boolean

Specifies that CSV field values may contain quoted record delimiters and such records should be
allowed. Default value is FALSE. Setting this value to TRUE may lower performance.

## CSVOutput (structure)

Describes how uncompressed comma-separated values (CSV)-formatted results are formatted.

### `QuoteFields` — QuoteFields (enum)

Indicates whether to use quotation marks around output fields.

- `ALWAYS`: Always use quotation marks for output fields.
- `ASNEEDED`: Use quotation marks for output fields when needed.

Values: `ALWAYS`, `ASNEEDED`

### `QuoteEscapeCharacter` — string

The single character used for escaping the quote character inside an already escaped value.

### `RecordDelimiter` — string

A single character used to separate individual records in the output. Instead of the default value,
you can specify an arbitrary delimiter.

### `FieldDelimiter` — string

The value used to separate individual fields in a record. You can specify an arbitrary
delimiter.

### `QuoteCharacter` — string

A single character used for escaping when the field delimiter is part of the value. For example, if
the value is `a, b`, Amazon S3 wraps this field value in quotation marks, as follows: `" a ,
b "`.

## Checksum (structure)

Contains all the possible checksum or digest values for an object.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This checksum is present
if the object was uploaded with the `CRC64NVME` checksum algorithm, or if the object was
uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to the
uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the object. This checksum is present
if the object was uploaded with the `SHA512` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the object. This checksum is present
if the object was uploaded with the `MD5` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the object. This checksum is present
if the object was uploaded with the `XXHASH64` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the object. This checksum is present
if the object was uploaded with the `XXHASH3` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the object. This checksum is present
if the object was uploaded with the `XXHASH128` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumType` — ChecksumType (enum)

The checksum type that is used to calculate the object’s checksum value. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

## ChecksumAlgorithm (enum)

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

## ChecksumMode (enum)

Values: `ENABLED`

## ChecksumType (enum)

Values: `COMPOSITE`, `FULL_OBJECT`

## CommonPrefix (structure)

Container for all (if there are any) keys between Prefix and the next occurrence of the string
specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory
specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in
notes/summer/july, the common prefix is notes/summer/.

### `Prefix` — string

Container for the specified common prefix.

## CompletedMultipartUpload (structure)

The container for the completed multipart upload details.

### `Parts` — list<CompletedPart>

Array of CompletedPart data types.

If you do not supply a valid `Part` with your request, the service sends back an HTTP 400
response.

## CompletedPart (structure)

Details of the parts that were uploaded.

### `ETag` — string

Entity tag returned when the part was uploaded.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if the
multipart upload request was created with the `CRC32` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if the
multipart upload request was created with the `CRC32C` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC64NVME` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` checksum of the part. This checksum is present if the
multipart upload request was created with the `SHA1` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` checksum of the part. This checksum is present if
the multipart upload request was created with the `SHA256` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA512` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the part. This checksum is present if
the multipart upload request was created with the `MD5` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH64` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH3` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH128` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `PartNumber` — integer

Part number that identifies the part. This is a positive integer between 1 and 10,000.

- **General purpose buckets** - In
  `CompleteMultipartUpload`, when a additional checksum (including
  `x-amz-checksum-crc32`, `x-amz-checksum-crc32c`,
  `x-amz-checksum-sha1`, or `x-amz-checksum-sha256`) is applied to each
  part, the `PartNumber` must start at 1 and the part numbers must be consecutive.
  Otherwise, Amazon S3 generates an HTTP `400 Bad Request` status code and an
  `InvalidPartOrder` error code.
- **Directory buckets** - In
  `CompleteMultipartUpload`, the `PartNumber` must start at 1 and the part
  numbers must be consecutive.

## CompressionType (enum)

Values: `NONE`, `GZIP`, `BZIP2`

## Condition (structure)

A container for describing a condition that must be met for the specified redirect to apply. For
example, 1. If request is for pages in the `/docs` folder, redirect to the
`/documents` folder. 2. If request results in HTTP error 4xx, redirect request to another
host where you might process the error.

### `HttpErrorCodeReturnedEquals` — string

The HTTP error code when the redirect is applied. In the event of an error, if the error code equals
this value, then the specified redirect is applied. Required when parent element `Condition`
is specified and sibling `KeyPrefixEquals` is not specified. If both are specified, then both
must be true for the redirect to be applied.

### `KeyPrefixEquals` — string

The object key name prefix when the redirect is applied. For example, to redirect requests for
`ExamplePage.html`, the key prefix will be `ExamplePage.html`. To redirect
request for all pages with the prefix `docs/`, the key prefix will be `/docs`,
which identifies all objects in the `docs/` folder. Required when the parent element
`Condition` is specified and sibling `HttpErrorCodeReturnedEquals` is not
specified. If both conditions are specified, both must be true for the redirect to be applied.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

## ContinuationEvent (structure)

## CopyObjectResult (structure)

Container for all response elements.

### `ETag` — string

Returns the ETag of the new object. The ETag reflects only changes to the contents of an object, not
its metadata.

### `LastModified` — timestamp

Creation date of the object.

### `ChecksumType` — ChecksumType (enum)

The checksum type that is used to calculate the object’s checksum value. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This checksum is present
if the object being copied was uploaded with the `CRC64NVME` checksum algorithm, or if the
object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to
the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the object. This checksum is only present
if the object was uploaded with the `SHA512` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the object. This checksum is only present
if the object was uploaded with the `MD5` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the object. This checksum is only present
if the object was uploaded with the `XXHASH64` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the object. This checksum is only present
if the object was uploaded with the `XXHASH3` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the object. This checksum is only present
if the object was uploaded with the `XXHASH128` checksum algorithm. For more information, see
[Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

## CopyPartResult (structure)

Container for all response elements.

### `ETag` — string

Entity tag of the object.

### `LastModified` — timestamp

Date and time at which the object was uploaded.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC32` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC32C` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC64NVME` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA1` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA256` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA512` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the part. This checksum is present if
the multipart upload request was created with the `MD5` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH64` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH3` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH128` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

## CreateBucketConfiguration (structure)

The configuration information for the bucket.

### `LocationConstraint` — BucketLocationConstraint (enum)

Specifies the Region where the bucket will be created. You might choose a Region to optimize
latency, minimize costs, or address regulatory requirements. For example, if you reside in Europe, you
will probably find it advantageous to create buckets in the Europe (Ireland) Region.

If you don't specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1)
by default. Configurations using the value `EU` will create a bucket in
`eu-west-1`.

For a list of the valid values for all of the Amazon Web Services Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

This functionality is not supported for directory buckets.

Values: `af-south-1`, `ap-east-1`, `ap-east-2`, `ap-northeast-1`, `ap-northeast-2`, `ap-northeast-3`, `ap-south-1`, `ap-south-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-4`, `ap-southeast-5`, `ap-southeast-6`, `ap-southeast-7`, `ca-central-1`, `ca-west-1`, `cn-north-1`, `cn-northwest-1`, `EU`, `eu-central-1`, `eu-central-2`, `eu-north-1`, `eu-south-1`, `eu-south-2`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `il-central-1`, `me-central-1`, `me-south-1`, `mx-central-1`, `sa-east-1`, `us-east-2`, `us-gov-east-1`, `us-gov-west-1`, `us-west-1`, `us-west-2`

### `Location` — LocationInfo

Specifies the location where the bucket will be created.

**Directory buckets**  - The location type is Availability Zone or Local Zone. To
use the Local Zone location type, your account must be enabled
for Local Zones. Otherwise, you get an HTTP `403 Forbidden` error with the error code
`AccessDenied`. To learn more,
see [Enable
accounts for Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/opt-in-directory-bucket-lz.html) in the *Amazon S3 User Guide*.

This functionality is only supported by directory buckets.

### `Bucket` — BucketInfo

Specifies the information about the bucket that will be created.

This functionality is only supported by directory buckets.

### `Tags` — list<Tag>

An array of tags that you can apply to the bucket that you're creating. Tags are key-value pairs of metadata used to categorize and organize your buckets, track costs, and control access.

You must have the `s3:TagResource` permission to create a general
purpose bucket with tags or the `s3express:TagResource` permission to create a directory bucket with tags.

When creating buckets with tags, note that tag-based conditions using `aws:ResourceTag` and `s3:BucketTag` condition keys are applicable only after ABAC is enabled on the bucket. To learn more, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

## DataRedundancy (enum)

Values: `SingleAvailabilityZone`, `SingleLocalZone`

## DefaultRetention (structure)

The container element for optionally specifying the default Object Lock retention settings for new
objects placed in the specified bucket.

- The `DefaultRetention` settings require both a mode and a period.
- The `DefaultRetention` period can be either `Days` or `Years`
  but you must select one. You cannot specify `Days` and `Years` at the same
  time.

### `Mode` — ObjectLockRetentionMode (enum)

The default Object Lock retention mode you want to apply to new objects placed in the specified
bucket. Must be used with either `Days` or `Years`.

Values: `GOVERNANCE`, `COMPLIANCE`

### `Days` — integer

The number of days that you want to specify for the default retention period. Must be used with
`Mode`.

### `Years` — integer

The number of years that you want to specify for the default retention period. Must be used with
`Mode`.

### `DefaultEventHold` — EventHoldDuration

The default event hold duration to be applied to new objects placed in the specified bucket. When
configured, new objects will automatically have an event hold enabled with this duration.

## Delete (structure)

Container for the objects to delete.

### `Objects` — list<ObjectIdentifier> · **required**

The object to delete.

**Directory buckets** - For directory buckets, an object
that's composed entirely of whitespace characters is not supported by the `DeleteObjects`
API operation. The request will receive a `400 Bad Request` error and none of the objects
in the request will be deleted.

### `Quiet` — boolean

Element to enable quiet mode for the request. When you add this element, you must set its value to
`true`.

## DeleteMarkerEntry (structure)

Information about the delete marker.

### `Owner` — Owner

The account that created the delete marker.

### `Key` — string

The object key.

### `VersionId` — string

Version ID of an object.

### `IsLatest` — boolean

Specifies whether the object is (true) or is not (false) the latest version of an object.

### `LastModified` — timestamp

Date and time when the object was last modified.

## DeleteMarkerReplication (structure)

Specifies whether Amazon S3 replicates delete markers. If you specify a `Filter` in your
replication configuration, you must also include a `DeleteMarkerReplication` element. If your
`Filter` includes a `Tag` element, the `DeleteMarkerReplication`
`Status` must be set to Disabled, because Amazon S3 does not support replicating delete markers
for tag-based rules. For an example configuration, see [Basic Rule
Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config).

For more information about delete marker replication, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html).

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of
delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations).

### `Status` — DeleteMarkerReplicationStatus (enum)

Indicates whether to replicate delete markers.

Indicates whether to replicate delete markers.

Values: `Enabled`, `Disabled`

## DeleteMarkerReplicationStatus (enum)

Values: `Enabled`, `Disabled`

## DeletedObject (structure)

Information about the deleted object.

### `Key` — string

The name of the deleted object.

### `VersionId` — string

The version ID of the deleted object.

This functionality is not supported for directory buckets.

### `DeleteMarker` — boolean

Indicates whether the specified object version that was permanently deleted was (true) or was not
(false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not
(false) the current version of the object is a delete marker. To learn more about delete markers, see
[Working with delete
markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).

This functionality is not supported for directory buckets.

### `DeleteMarkerVersionId` — string

The version ID of the delete marker created as a result of the DELETE operation. If you delete a
specific object version, the value returned by this header is the version ID of the object version
deleted.

This functionality is not supported for directory buckets.

## Destination (structure)

Specifies information about where to publish analysis or configuration results for an Amazon S3 bucket
and S3 Replication Time Control (S3 RTC).

### `Bucket` — string · **required**

The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.

### `Account` — string

Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change
replica ownership to the Amazon Web Services account that owns the destination bucket by specifying the
`AccessControlTranslation` property, this is the account ID of the destination bucket
owner. For more information, see [Replication Additional Configuration: Changing
the Replica Owner](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html) in the *Amazon S3 User Guide*.

### `StorageClass` — StorageClass (enum)

The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By
default, Amazon S3 uses the storage class of the source object to create the object replica.

For valid values, see the `StorageClass` element of the [PUT Bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) action in the
*Amazon S3 API Reference*.

`FSX_OPENZFS` is not an accepted value when replicating objects.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `AccessControlTranslation` — AccessControlTranslation

Specify this only in a cross-account scenario (where source and destination bucket owners are not
the same), and you want to change replica ownership to the Amazon Web Services account that owns the destination
bucket. If this is not specified in the replication configuration, the replicas are owned by same
Amazon Web Services account that owns the source object.

### `EncryptionConfiguration` — EncryptionConfiguration

A container that provides information about encryption. If `SourceSelectionCriteria` is
specified, you must specify this element.

### `ReplicationTime` — ReplicationTime

A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all
objects and operations on objects must be replicated. Must be specified together with a
`Metrics` block.

### `Metrics` — Metrics

A container specifying replication metrics-related settings enabling replication metrics and
events.

## DestinationResult (structure)

The destination information for the S3 Metadata configuration.

### `TableBucketType` — S3TablesBucketType (enum)

The type of the table bucket where the metadata configuration is stored. The `aws`
value indicates an Amazon Web Services managed table bucket, and the `customer` value indicates a
customer-managed table bucket. V2 metadata configurations are stored in Amazon Web Services managed table
buckets, and V1 metadata configurations are stored in customer-managed table buckets.

Values: `aws`, `customer`

### `TableBucketArn` — string

The Amazon Resource Name (ARN) of the table bucket where the metadata configuration is stored.

### `TableNamespace` — string

The namespace in the table bucket where the metadata tables for a metadata configuration are
stored.

## EncodingType (enum)

Encoding type used by Amazon S3 to encode the [object keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) in the response. Responses are
encoded only in UTF-8. An object key can contain any Unicode character. However, the XML 1.0 parser
can't parse certain characters, such as characters with an ASCII value from 0 to 10. For characters that
aren't supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
response. For more information about characters to avoid in object key names, see [Object key
naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-guidelines).

When using the URL encoding type, non-ASCII characters that are used in an object's key name will
be percent-encoded according to UTF-8 code values. For example, the object
`test_file(3).png` will appear as `test_file%283%29.png`.

Values: `url`

## Encryption (structure)

Contains the type of server-side encryption used.

### `EncryptionType` — ServerSideEncryption (enum) · **required**

The server-side encryption algorithm used when storing job results in Amazon S3 (for example, AES256,
`aws:kms`).

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `KMSKeyId` — string

If the encryption type is `aws:kms`, this optional value specifies the ID of the
symmetric encryption customer managed key to use for encryption of job results. Amazon S3 only supports symmetric
encryption KMS keys. For more information, see [Asymmetric keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the
*Amazon Web Services Key Management Service Developer Guide*.

### `KMSContext` — string

If the encryption type is `aws:kms`, this optional value can be used to specify the
encryption context for the restore results.

## EncryptionConfiguration (structure)

Specifies encryption-related information for an Amazon S3 bucket that is a destination for replicated
objects.

If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key
ARN. If you use a KMS key alias instead, then KMS resolves the key within the requester’s account.
This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and
not the bucket owner.

### `ReplicaKmsKeyID` — string

Specifies the ID (Key ARN or Alias ARN) of the customer managed Amazon Web Services KMS key stored in Amazon Web Services Key
Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3
only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the
*Amazon Web Services Key Management Service Developer Guide*.

## EncryptionType (enum)

Values: `NONE`, `SSE-C`

## EndEvent (structure)

A message that indicates the request is complete and no more messages will be sent. You should not
assume that the request is complete until the client receives an `EndEvent`.

## Error (structure)

For information about using the Amazon S3 API—including error handling—see the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/Welcome.html).

Container for all error elements.

### `Key` — string

The error key.

### `VersionId` — string

The version ID of the error.

This functionality is not supported for directory buckets.

### `Code` — string

The error code is a string that uniquely identifies an error condition. It is meant to be read and
understood by programs that detect and handle errors by type. The following is a list of Amazon S3 error
codes. For more information, see [Error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).

- - *Code:* AccessDenied
  - *Description:* Access Denied
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* AccountProblem
  - *Description:* There is a problem with your Amazon Web Services account that prevents
    the action from completing successfully. Contact Amazon Web Services Support for further assistance.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* AllAccessDisabled
  - *Description:* All access to this Amazon S3 resource has been disabled.
    Contact Amazon Web Services Support for further assistance.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* AmbiguousGrantByEmailAddress
  - *Description:* The email address you provided is associated with more
    than one account.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* AuthorizationHeaderMalformed
  - *Description:* The authorization header you provided is invalid.
  - *HTTP Status Code:* 400 Bad Request
  - *HTTP Status Code:* N/A
- - *Code:* BadDigest
  - *Description:* The Content-MD5 you specified did not match what we
    received.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* BucketAlreadyExists
  - *Description:* The requested bucket name is not available. The bucket
    namespace is shared by all users of the system. Please select a different name and try
    again.
  - *HTTP Status Code:* 409 Conflict
  - *SOAP Fault Code Prefix:* Client
- - *Code:* BucketAlreadyOwnedByYou
  - *Description:* The bucket you tried to create already exists, and you own
    it. Amazon S3 returns this error in all Amazon Web Services Regions except in the North Virginia Region. For legacy
    compatibility, if you re-create an existing bucket that you already own in the North Virginia
    Region, Amazon S3 returns 200 OK and resets the bucket access control lists (ACLs).
  - *Code:* 409 Conflict (in all Regions except the North Virginia Region)
  - *SOAP Fault Code Prefix:* Client
- - *Code:* BucketNotEmpty
  - *Description:* The bucket you tried to delete is not empty.
  - *HTTP Status Code:* 409 Conflict
  - *SOAP Fault Code Prefix:* Client
- - *Code:* CredentialsNotSupported
  - *Description:* This request does not support credentials.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* CrossLocationLoggingProhibited
  - *Description:* Cross-location logging not allowed. Buckets in one
    geographic location cannot log information to a bucket in another location.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* EntityTooSmall
  - *Description:* Your proposed upload is smaller than the minimum allowed
    object size.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* EntityTooLarge
  - *Description:* Your proposed upload exceeds the maximum allowed object
    size.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* ExpiredToken
  - *Description:* The provided token has expired.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* IllegalVersioningConfigurationException
  - *Description:* Indicates that the versioning configuration specified in
    the request is invalid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* IncompleteBody
  - *Description:* You did not provide the number of bytes specified by the
    Content-Length HTTP header
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* IncorrectNumberOfFilesInPostRequest
  - *Description:* POST requires exactly one file upload per request.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InlineDataTooLarge
  - *Description:* Inline data exceeds the maximum allowed size.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InternalError
  - *Description:* We encountered an internal error. Please try again.
  - *HTTP Status Code:* 500 Internal Server Error
  - *SOAP Fault Code Prefix:* Server
- - *Code:* InvalidAccessKeyId
  - *Description:* The Amazon Web Services access key ID you provided does not exist in our
    records.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidAddressingHeader
  - *Description:* You must specify the Anonymous role.
  - *HTTP Status Code:* N/A
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidArgument
  - *Description:* Invalid Argument
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidBucketName
  - *Description:* The specified bucket is not valid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidBucketState
  - *Description:* The request is not valid with the current state of the
    bucket.
  - *HTTP Status Code:* 409 Conflict
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidDigest
  - *Description:* The Content-MD5 you specified is not valid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidEncryptionAlgorithmError
  - *Description:* The encryption request you specified is not valid. The
    valid value is AES256.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidLocationConstraint
  - *Description:* The specified location constraint is not valid. For more
    information about Regions, see [How to Select a Region for Your
    Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro).
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidObjectState
  - *Description:* The action is not valid for the current state of the
    object.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPart
  - *Description:* One or more of the specified parts could not be found. The
    part might not have been uploaded, or the specified entity tag might not have matched the part's
    entity tag.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPartOrder
  - *Description:* The list of parts was not in ascending order. Parts list
    must be specified in order by part number.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPayer
  - *Description:* All access to this object has been disabled. Please
    contact Amazon Web Services Support for further assistance.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPolicyDocument
  - *Description:* The content of the form does not meet the conditions
    specified in the policy document.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRange
  - *Description:* The requested range cannot be satisfied.
  - *HTTP Status Code:* 416 Requested Range Not Satisfiable
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRequest
  - *Description:* Please use `AWS4-HMAC-SHA256`.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* SOAP requests must be made over an HTTPS
    connection.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Acceleration is not supported for buckets
    with non-DNS compliant names.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Acceleration is not supported for buckets
    with periods (.) in their names.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Accelerate endpoint only supports virtual
    style requests.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Accelerate is not configured on this
    bucket.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Accelerate is disabled on this
    bucket.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Acceleration is not supported on this
    bucket. Contact Amazon Web Services Support for more information.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidRequest
  - *Description:* Amazon S3 Transfer Acceleration cannot be enabled on this
    bucket. Contact Amazon Web Services Support for more information.
  - *HTTP Status Code:* 400 Bad Request
  - *Code:* N/A
- - *Code:* InvalidSecurity
  - *Description:* The provided security credentials are not valid.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidSOAPRequest
  - *Description:* The SOAP request body is invalid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidStorageClass
  - *Description:* The storage class you specified is not valid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidTargetBucketForLogging
  - *Description:* The target bucket for logging does not exist, is not owned
    by you, or does not have the appropriate grants for the log-delivery group.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidToken
  - *Description:* The provided token is malformed or otherwise
    invalid.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidURI
  - *Description:* Couldn't parse the specified URI.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* KeyTooLongError
  - *Description:* Your key is too long.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedACLError
  - *Description:* The XML you provided was not well-formed or did not
    validate against our published schema.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedPOSTRequest
  - *Description:* The body of your POST request is not well-formed
    multipart/form-data.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedXML
  - *Description:* This happens when the user sends malformed XML (XML that
    doesn't conform to the published XSD) for the configuration. The error message is, "The XML you
    provided was not well-formed or did not validate against our published schema."
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MaxMessageLengthExceeded
  - *Description:* Your request was too big.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MaxPostPreDataLengthExceededError
  - *Description:* Your POST request fields preceding the upload file were
    too large.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MetadataTooLarge
  - *Description:* Your metadata headers exceed the maximum allowed metadata
    size.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MethodNotAllowed
  - *Description:* The specified method is not allowed against this
    resource.
  - *HTTP Status Code:* 405 Method Not Allowed
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MissingAttachment
  - *Description:* A SOAP attachment was expected, but none were
    found.
  - *HTTP Status Code:* N/A
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MissingContentLength
  - *Description:* You must provide the Content-Length HTTP header.
  - *HTTP Status Code:* 411 Length Required
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MissingRequestBodyError
  - *Description:* This happens when the user sends an empty XML document as
    a request. The error message is, "Request body is empty."
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MissingSecurityElement
  - *Description:* The SOAP 1.1 request is missing a security element.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* MissingSecurityHeader
  - *Description:* Your request is missing a required header.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoLoggingStatusForKey
  - *Description:* There is no such thing as a logging status subresource for
    a key.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchBucket
  - *Description:* The specified bucket does not exist.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchBucketPolicy
  - *Description:* The specified bucket does not have a bucket policy.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchKey
  - *Description:* The specified key does not exist.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchLifecycleConfiguration
  - *Description:* The lifecycle configuration does not exist.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchUpload
  - *Description:* The specified multipart upload does not exist. The upload
    ID might be invalid, or the multipart upload might have been aborted or completed.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchVersion
  - *Description:* Indicates that the version ID specified in the request
    does not match an existing version.
  - *HTTP Status Code:* 404 Not Found
  - *SOAP Fault Code Prefix:* Client
- - *Code:* NotImplemented
  - *Description:* A header you provided implies functionality that is not
    implemented.
  - *HTTP Status Code:* 501 Not Implemented
  - *SOAP Fault Code Prefix:* Server
- - *Code:* NotSignedUp
  - *Description:* Your account is not signed up for the Amazon S3 service. You
    must sign up before you can use Amazon S3. You can sign up at the following URL: [Amazon S3](http://aws.amazon.com/s3)
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* OperationAborted
  - *Description:* A conflicting conditional action is currently in progress
    against this resource. Try again.
  - *HTTP Status Code:* 409 Conflict
  - *SOAP Fault Code Prefix:* Client
- - *Code:* PermanentRedirect
  - *Description:* The bucket you are attempting to access must be addressed
    using the specified endpoint. Send all future requests to this endpoint.
  - *HTTP Status Code:* 301 Moved Permanently
  - *SOAP Fault Code Prefix:* Client
- - *Code:* PreconditionFailed
  - *Description:* At least one of the preconditions you specified did not
    hold.
  - *HTTP Status Code:* 412 Precondition Failed
  - *SOAP Fault Code Prefix:* Client
- - *Code:* Redirect
  - *Description:* Temporary redirect.
  - *HTTP Status Code:* 307 Moved Temporarily
  - *SOAP Fault Code Prefix:* Client
- - *Code:* RestoreAlreadyInProgress
  - *Description:* Object restore is already in progress.
  - *HTTP Status Code:* 409 Conflict
  - *SOAP Fault Code Prefix:* Client
- - *Code:* RequestIsNotMultiPartContent
  - *Description:* Bucket POST must be of the enclosure-type
    multipart/form-data.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTimeout
  - *Description:* Your socket connection to the server was not read from or
    written to within the timeout period.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTimeTooSkewed
  - *Description:* The difference between the request time and the server's
    time is too large.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTorrentOfBucketError
  - *Description:* Requesting the torrent file of a bucket is not
    permitted.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* SignatureDoesNotMatch
  - *Description:* The request signature we calculated does not match the
    signature you provided. Check your Amazon Web Services secret access key and signing method. For more
    information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) and [SOAP Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/SOAPAuthentication.html) for
    details.
  - *HTTP Status Code:* 403 Forbidden
  - *SOAP Fault Code Prefix:* Client
- - *Code:* ServiceUnavailable
  - *Description:* Service is unable to handle request.
  - *HTTP Status Code:* 503 Service Unavailable
  - *SOAP Fault Code Prefix:* Server
- - *Code:* SlowDown
  - *Description:* Reduce your request rate.
  - *HTTP Status Code:* 503 Slow Down
  - *SOAP Fault Code Prefix:* Server
- - *Code:* TemporaryRedirect
  - *Description:* You are being redirected to the bucket while DNS
    updates.
  - *HTTP Status Code:* 307 Moved Temporarily
  - *SOAP Fault Code Prefix:* Client
- - *Code:* TokenRefreshRequired
  - *Description:* The provided token must be refreshed.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* TooManyBuckets
  - *Description:* You have attempted to create more buckets than
    allowed.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* UnexpectedContent
  - *Description:* This request does not support content.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* UnresolvableGrantByEmailAddress
  - *Description:* The email address you provided does not match any account
    on record.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client
- - *Code:* UserKeyMustBeSpecified
  - *Description:* The bucket POST must contain the specified field name. If
    it is specified, check the order of the fields.
  - *HTTP Status Code:* 400 Bad Request
  - *SOAP Fault Code Prefix:* Client

### `Message` — string

The error message contains a generic description of the error condition in English. It is intended
for a human audience. Simple programs display the message directly to the end user if they encounter an
error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive
error handling and proper internationalization are more likely to ignore the error message.

## ErrorDetails (structure)

If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2
`CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code and error message.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `ErrorCode` — string

If the V1 `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code. The possible error codes and error
messages are as follows:

- `AccessDeniedCreatingResources` - You don't have sufficient permissions to create the
  required resources. Make sure that you have `s3tables:CreateNamespace`,
  `s3tables:CreateTable`, `s3tables:GetTable` and
  `s3tables:PutTablePolicy` permissions, and then try again. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `AccessDeniedWritingToTable` - Unable to write to the metadata table because of
  missing resource permissions. To fix the resource policy, Amazon S3 needs to create a new metadata
  table. To create a new metadata table, you must delete the metadata configuration for this bucket,
  and then create a new metadata configuration.
- `DestinationTableNotFound` - The destination table doesn't exist. To create a new
  metadata table, you must delete the metadata configuration for this bucket, and then create a new
  metadata configuration.
- `ServerInternalError` - An internal error has occurred. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `TableAlreadyExists` - The table that you specified already exists in the table
  bucket's namespace. Specify a different table name. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `TableBucketNotFound` - The table bucket that you specified doesn't exist in this
  Amazon Web Services Region and account. Create or choose a different table bucket. To create a new metadata table,
  you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.

If the V2 `CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code. The possible error codes and error
messages are as follows:

- `AccessDeniedCreatingResources` - You don't have sufficient permissions to create
  the required resources. Make sure that you have `s3tables:CreateTableBucket`,
  `s3tables:CreateNamespace`, `s3tables:CreateTable`,
  `s3tables:GetTable`, `s3tables:PutTablePolicy`,
  `kms:DescribeKey`, and `s3tables:PutTableEncryption` permissions.
  Additionally, ensure that the KMS key used to encrypt the table still exists, is active and
  has a resource policy granting access to the S3 service principals
  '`maintenance.s3tables.amazonaws.com`' and '`metadata.s3.amazonaws.com`'.
  To create a new metadata table, you must delete the metadata configuration for this bucket, and
  then create a new metadata configuration.
- `AccessDeniedWritingToTable` - Unable to write to the metadata table because of
  missing resource permissions. To fix the resource policy, Amazon S3 needs to create a new metadata
  table. To create a new metadata table, you must delete the metadata configuration for this bucket,
  and then create a new metadata configuration.
- `DestinationTableNotFound` - The destination table doesn't exist. To create a new
  metadata table, you must delete the metadata configuration for this bucket, and then create a new
  metadata configuration.
- `ServerInternalError` - An internal error has occurred. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `JournalTableAlreadyExists` - A journal table already exists in the Amazon Web Services managed table bucket's
  namespace. Delete the journal table, and then try again. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `InventoryTableAlreadyExists` - An inventory table already exists in the Amazon Web Services managed table
  bucket's namespace. Delete the inventory table, and then try again. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `JournalTableNotAvailable` - The journal table that the inventory table relies on
  has a `FAILED` status. An inventory table requires a journal table with an
  `ACTIVE` status. To create a new journal or inventory table, you must delete the metadata
  configuration for this bucket, along with any journal or inventory tables, and then create a new
  metadata configuration.
- `NoSuchBucket` - The specified general purpose bucket does not exist.

### `ErrorMessage` — string

If the V1 `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error message. The possible error codes and
error messages are as follows:

- `AccessDeniedCreatingResources` - You don't have sufficient permissions to create the
  required resources. Make sure that you have `s3tables:CreateNamespace`,
  `s3tables:CreateTable`, `s3tables:GetTable` and
  `s3tables:PutTablePolicy` permissions, and then try again. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `AccessDeniedWritingToTable` - Unable to write to the metadata table because of
  missing resource permissions. To fix the resource policy, Amazon S3 needs to create a new metadata
  table. To create a new metadata table, you must delete the metadata configuration for this bucket,
  and then create a new metadata configuration.
- `DestinationTableNotFound` - The destination table doesn't exist. To create a new
  metadata table, you must delete the metadata configuration for this bucket, and then create a new
  metadata configuration.
- `ServerInternalError` - An internal error has occurred. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `TableAlreadyExists` - The table that you specified already exists in the table
  bucket's namespace. Specify a different table name. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `TableBucketNotFound` - The table bucket that you specified doesn't exist in this
  Amazon Web Services Region and account. Create or choose a different table bucket. To create a new metadata table,
  you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.

If the V2 `CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code. The possible error codes and error
messages are as follows:

- `AccessDeniedCreatingResources` - You don't have sufficient permissions to create
  the required resources. Make sure that you have `s3tables:CreateTableBucket`,
  `s3tables:CreateNamespace`, `s3tables:CreateTable`,
  `s3tables:GetTable`, `s3tables:PutTablePolicy`,
  `kms:DescribeKey`, and `s3tables:PutTableEncryption` permissions.
  Additionally, ensure that the KMS key used to encrypt the table still exists, is active and
  has a resource policy granting access to the S3 service principals
  '`maintenance.s3tables.amazonaws.com`' and '`metadata.s3.amazonaws.com`'.
  To create a new metadata table, you must delete the metadata configuration for this bucket, and
  then create a new metadata configuration.
- `AccessDeniedWritingToTable` - Unable to write to the metadata table because of
  missing resource permissions. To fix the resource policy, Amazon S3 needs to create a new metadata
  table. To create a new metadata table, you must delete the metadata configuration for this bucket,
  and then create a new metadata configuration.
- `DestinationTableNotFound` - The destination table doesn't exist. To create a new
  metadata table, you must delete the metadata configuration for this bucket, and then create a new
  metadata configuration.
- `ServerInternalError` - An internal error has occurred. To create a new metadata
  table, you must delete the metadata configuration for this bucket, and then create a new metadata
  configuration.
- `JournalTableAlreadyExists` - A journal table already exists in the Amazon Web Services managed table bucket's
  namespace. Delete the journal table, and then try again. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `InventoryTableAlreadyExists` - An inventory table already exists in the Amazon Web Services managed table
  bucket's namespace. Delete the inventory table, and then try again. To create a new metadata table, you must delete
  the metadata configuration for this bucket, and then create a new metadata configuration.
- `JournalTableNotAvailable` - The journal table that the inventory table relies on
  has a `FAILED` status. An inventory table requires a journal table with an
  `ACTIVE` status. To create a new journal or inventory table, you must delete the metadata
  configuration for this bucket, along with any journal or inventory tables, and then create a new
  metadata configuration.
- `NoSuchBucket` - The specified general purpose bucket does not exist.

## ErrorDocument (structure)

The error information.

### `Key` — string · **required**

The object key name to use when a 4XX class error occurs.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

## Event (enum)

The bucket event for which to send notifications.

Values: `s3:ReducedRedundancyLostObject`, `s3:ObjectCreated:*`, `s3:ObjectCreated:Put`, `s3:ObjectCreated:Post`, `s3:ObjectCreated:Copy`, `s3:ObjectCreated:CompleteMultipartUpload`, `s3:ObjectRemoved:*`, `s3:ObjectRemoved:Delete`, `s3:ObjectRemoved:DeleteMarkerCreated`, `s3:ObjectRestore:*`, `s3:ObjectRestore:Post`, `s3:ObjectRestore:Completed`, `s3:Replication:*`, `s3:Replication:OperationFailedReplication`, `s3:Replication:OperationNotTracked`, `s3:Replication:OperationMissedThreshold`, `s3:Replication:OperationReplicatedAfterThreshold`, `s3:ObjectRestore:Delete`, `s3:LifecycleTransition`, `s3:IntelligentTiering`, `s3:ObjectAcl:Put`, `s3:LifecycleExpiration:*`, `s3:LifecycleExpiration:Delete`, `s3:LifecycleExpiration:DeleteMarkerCreated`, `s3:ObjectTagging:*`, `s3:ObjectTagging:Put`, `s3:ObjectTagging:Delete`, `s3:ObjectAnnotation:*`, `s3:ObjectAnnotation:Put`, `s3:ObjectAnnotation:Delete`, `s3:ObjectRetention:Put`

## EventBridgeConfiguration (structure)

A container for specifying the configuration for Amazon EventBridge.

## EventHoldDuration (structure)

Contains the event hold duration configuration, specified in either days or years.

### `Days` — integer

The number of days for the event hold duration. The minimum value is 1 and the maximum value is
36,500.

### `Years` — integer

The number of years for the event hold duration. The minimum value is 1 and the maximum value is
100.

## ExistingObjectReplication (structure)

Optional configuration to replicate existing source bucket objects.

This parameter is no longer supported. To replicate existing objects, see [Replicating
existing objects with S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) in the
*Amazon S3 User Guide*.

### `Status` — ExistingObjectReplicationStatus (enum) · **required**

Specifies whether Amazon S3 replicates existing source bucket objects.

Values: `Enabled`, `Disabled`

## ExistingObjectReplicationStatus (enum)

Values: `Enabled`, `Disabled`

## ExpirationState (enum)

Values: `ENABLED`, `DISABLED`

## ExpirationStatus (enum)

Values: `Enabled`, `Disabled`

## ExpressionType (enum)

Values: `SQL`

## FileHeaderInfo (enum)

Values: `USE`, `IGNORE`, `NONE`

## FilterRule (structure)

Specifies the Amazon S3 object key name to filter on. An object key name is the name assigned to an
object in your Amazon S3 bucket. You specify whether to filter on the suffix or prefix of the object key
name. A prefix is a specific string of characters at the beginning of an object key name, which you can
use to organize objects. For example, you can start the key names of related objects with a prefix, such
as `2023-` or `engineering/`. Then, you can use `FilterRule` to find
objects in a bucket with key names that have the same prefix. A suffix is similar to a prefix, but it is
at the end of the object key name instead of at the beginning.

### `Name` — FilterRuleName (enum)

The object key name prefix or suffix identifying one or more objects to which the filtering rule
applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported.
For more information, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide*.

Values: `prefix`, `suffix`

### `Value` — string

The value that the filter searches for in object key names.

## FilterRuleName (enum)

Values: `prefix`, `suffix`

## GetBucketMetadataConfigurationResult (structure)

The S3 Metadata configuration for a general purpose bucket.

### `MetadataConfigurationResult` — MetadataConfigurationResult · **required**

The metadata configuration for a general purpose bucket.

## GetBucketMetadataTableConfigurationResult (structure)

The V1 S3 Metadata configuration for a general purpose bucket.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `MetadataTableConfigurationResult` — MetadataTableConfigurationResult · **required**

The V1 S3 Metadata configuration for a general purpose bucket.

### `Status` — string · **required**

The status of the metadata table. The status values are:

- `CREATING` - The metadata table is in the process of being created in the specified
  table bucket.
- `ACTIVE` - The metadata table has been created successfully, and records are being
  delivered to the table.
- `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver
  records. See `ErrorDetails` for details.

### `Error` — ErrorDetails

If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code and error message.

## GetObjectAttributesParts (structure)

A collection of parts associated with a multipart upload.

### `TotalPartsCount` — integer

The total number of parts.

### `PartNumberMarker` — string

The marker for the current part.

### `NextPartNumberMarker` — string

When a list is truncated, this element specifies the last part in the list, as well as the value to
use for the `PartNumberMarker` request parameter in a subsequent request.

### `MaxParts` — integer

The maximum number of parts allowed in the response.

### `IsTruncated` — boolean

Indicates whether the returned list of parts is truncated. A value of `true` indicates
that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned
in the `MaxParts` element.

### `Parts` — list<ObjectPart>

A container for elements related to a particular part. A response can contain zero or more
`Parts` elements.

- **General purpose buckets** - For
  `GetObjectAttributes`, if an additional checksum (including
  `x-amz-checksum-crc32`, `x-amz-checksum-crc32c`,
  `x-amz-checksum-sha1`, or `x-amz-checksum-sha256`) isn't applied to the
  object specified in the request, the response doesn't return the `Part` element.
- **Directory buckets** - For
  `GetObjectAttributes`, regardless of whether an additional checksum is applied to the
  object specified in the request, the response returns the `Part` element.

## GlacierJobParameters (structure)

Container for S3 Glacier job parameters.

### `Tier` — Tier (enum) · **required**

Retrieval tier at which the restore will be processed.

Values: `Standard`, `Bulk`, `Expedited`

## Grant (structure)

Container for grant information.

### `Grantee` — Grantee

The person being granted permissions.

### `Permission` — Permission (enum)

Specifies the permission given to the grantee.

Values: `FULL_CONTROL`, `WRITE`, `WRITE_ACP`, `READ`, `READ_ACP`

## Grantee (structure)

Container for the person being granted permissions.

### `DisplayName` — string

### `EmailAddress` — string

### `ID` — string

The canonical user ID of the grantee.

### `URI` — string

URI of the grantee group.

### `Type` — Type (enum) · **required**

Type of grantee

Values: `CanonicalUser`, `AmazonCustomerByEmail`, `Group`

## IndexDocument (structure)

Container for the `Suffix` element.

### `Suffix` — string · **required**

A suffix that is appended to a request that is for a directory on the website endpoint. (For
example, if the suffix is `index.html` and you make a request to
`samplebucket/images/`, the data that is returned will be for the object with the key name
`images/index.html`.) The suffix must not be empty and must not include a slash
character.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

## Initiator (structure)

Container element that identifies who initiated the multipart upload.

### `ID` — string

If the principal is an Amazon Web Services account, it provides the Canonical User ID. If the principal is an
IAM User, it provides a user ARN value.

**Directory buckets** - If the principal is an Amazon Web Services account,
it provides the Amazon Web Services account ID. If the principal is an IAM User, it provides a user ARN
value.

### `DisplayName` — string

This functionality is not supported for directory buckets.

## InputSerialization (structure)

Describes the serialization format of the object.

### `CSV` — CSVInput

Describes the serialization of a CSV-encoded object.

### `CompressionType` — CompressionType (enum)

Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.

Values: `NONE`, `GZIP`, `BZIP2`

### `JSON` — JSONInput

Specifies JSON as object's input serialization format.

### `Parquet` — ParquetInput

Specifies Parquet as object's input serialization format.

## IntelligentTieringAccessTier (enum)

Values: `ARCHIVE_ACCESS`, `DEEP_ARCHIVE_ACCESS`

## IntelligentTieringAndOperator (structure)

A container for specifying S3 Intelligent-Tiering filters. The filters determine the subset of
objects to which the rule applies.

### `Prefix` — string

An object key name prefix that identifies the subset of objects to which the configuration
applies.

### `Tags` — list<Tag>

All of these tags must exist in the object's tag set in order for the configuration to apply.

## IntelligentTieringConfiguration (structure)

Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.

For information about the S3 Intelligent-Tiering storage class, see [Storage class for
automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

### `Id` — string · **required**

The ID used to identify the S3 Intelligent-Tiering configuration.

### `Filter` — IntelligentTieringFilter

Specifies a bucket filter. The configuration only includes objects that meet the filter's
criteria.

### `Status` — IntelligentTieringStatus (enum) · **required**

Specifies the status of the configuration.

Values: `Enabled`, `Disabled`

### `Tierings` — list<Tiering> · **required**

Specifies the S3 Intelligent-Tiering storage class tier of the configuration.

## IntelligentTieringFilter (structure)

The `Filter` is used to identify objects that the S3 Intelligent-Tiering configuration
applies to.

### `Prefix` — string

An object key name prefix that identifies the subset of objects to which the rule applies.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `Tag` — Tag

A container of a key value name pair.

### `And` — IntelligentTieringAndOperator

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
operator must have at least two predicates, and an object must match all of the predicates in order for
the filter to apply.

## IntelligentTieringStatus (enum)

Values: `Enabled`, `Disabled`

## InventoryConfiguration (structure)

Specifies the S3 Inventory configuration for an Amazon S3 bucket. For more information, see [GET Bucket
inventory](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.

### `Destination` — InventoryDestination · **required**

Contains information about where to publish the inventory results.

### `IsEnabled` — boolean · **required**

Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory
list is generated. If set to `False`, no inventory list is generated.

### `Filter` — InventoryFilter

Specifies an inventory filter. The inventory only includes objects that meet the filter's
criteria.

### `Id` — string · **required**

The ID used to identify the inventory configuration.

### `IncludedObjectVersions` — InventoryIncludedObjectVersions (enum) · **required**

Object versions to include in the inventory list. If set to `All`, the list includes all
the object versions, which adds the version-related fields `VersionId`,
`IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the
list does not contain these version-related fields.

Values: `All`, `Current`

### `OptionalFields` — list<InventoryOptionalField (enum)>

Contains the optional fields that are included in the inventory results.

The following optional fields are supported for directory buckets `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded |
EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate.` Throws MalformedXML error if unsupported optional field is provided.

### `Schedule` — InventorySchedule · **required**

Specifies the schedule for generating inventory results.

## InventoryConfigurationState (enum)

Values: `ENABLED`, `DISABLED`

## InventoryDestination (structure)

Specifies the S3 Inventory configuration for an Amazon S3 bucket.

### `S3BucketDestination` — InventoryS3BucketDestination · **required**

Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
inventory results are published.

## InventoryEncryption (structure)

Contains the type of server-side encryption used to encrypt the S3 Inventory results.

### `SSES3` — SSES3

Specifies the use of SSE-S3 to encrypt delivered inventory reports.

### `SSEKMS` — SSEKMS

Specifies the use of SSE-KMS to encrypt delivered inventory reports.

## InventoryFilter (structure)

Specifies an S3 Inventory filter. The inventory only includes objects that meet the filter's
criteria.

### `Prefix` — string · **required**

The prefix that an object must have to be included in the inventory results.

## InventoryFormat (enum)

Values: `CSV`, `ORC`, `Parquet`

## InventoryFrequency (enum)

Values: `Daily`, `Weekly`

## InventoryIncludedObjectVersions (enum)

Values: `All`, `Current`

## InventoryOptionalField (enum)

Values: `Size`, `LastModifiedDate`, `StorageClass`, `ETag`, `IsMultipartUploaded`, `ReplicationStatus`, `EncryptionStatus`, `ObjectLockRetainUntilDate`, `ObjectLockMode`, `ObjectLockLegalHoldStatus`, `ObjectLockEventHoldStatus`, `ObjectLockEventHoldDuration`, `IntelligentTieringAccessTier`, `BucketKeyStatus`, `ChecksumAlgorithm`, `ObjectAccessControlList`, `ObjectOwner`, `LifecycleExpirationDate`, `IntelligentTieringReferenceDate`

## InventoryS3BucketDestination (structure)

Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
S3 Inventory results are published.

### `AccountId` — string

The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not
validated before exporting data.

Although this value is optional, we strongly recommend that you set it to help prevent problems
if the destination bucket ownership changes.

### `Bucket` — string · **required**

The Amazon Resource Name (ARN) of the bucket where inventory results will be published.

### `Format` — InventoryFormat (enum) · **required**

Specifies the output format of the inventory results.

Values: `CSV`, `ORC`, `Parquet`

### `Prefix` — string

The prefix that is prepended to all inventory results.

### `Encryption` — InventoryEncryption

Contains the type of server-side encryption used to encrypt the inventory results.

## InventorySchedule (structure)

Specifies the schedule for generating S3 Inventory results.

### `Frequency` — InventoryFrequency (enum) · **required**

Specifies how frequently inventory results are produced.

Values: `Daily`, `Weekly`

## InventoryTableConfiguration (structure)

The inventory table configuration for an S3 Metadata configuration.

### `ConfigurationState` — InventoryConfigurationState (enum) · **required**

The configuration state of the inventory table, indicating whether the inventory table is enabled
or disabled.

Values: `ENABLED`, `DISABLED`

### `EncryptionConfiguration` — MetadataTableEncryptionConfiguration

The encryption configuration for the inventory table.

## InventoryTableConfigurationResult (structure)

The inventory table configuration for an S3 Metadata configuration.

### `ConfigurationState` — InventoryConfigurationState (enum) · **required**

The configuration state of the inventory table, indicating whether the inventory table is enabled
or disabled.

Values: `ENABLED`, `DISABLED`

### `TableStatus` — string

The status of the inventory table. The status values are:

- `CREATING` - The inventory table is in the process of being created in the specified
  Amazon Web Services managed table bucket.
- `BACKFILLING` - The inventory table is in the process of being backfilled. When
  you enable the inventory table for your metadata configuration, the table goes through a
  process known as backfilling, during which Amazon S3 scans your general purpose bucket to retrieve
  the initial metadata for all objects in the bucket. Depending on the number of objects in your
  bucket, this process can take several hours. When the backfilling process is finished, the
  status of your inventory table changes from `BACKFILLING` to `ACTIVE`.
  After backfilling is completed, updates to your objects are reflected in the inventory table
  within one hour.
- `ACTIVE` - The inventory table has been created successfully, and records are being
  delivered to the table.
- `FAILED` - Amazon S3 is unable to create the inventory table, or Amazon S3 is unable to deliver
  records.

### `Error` — ErrorDetails

If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2
`CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code and error message.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `TableName` — string

The name of the inventory table.

### `TableArn` — string

The Amazon Resource Name (ARN) for the inventory table.

## InventoryTableConfigurationUpdates (structure)

The specified updates to the S3 Metadata inventory table configuration.

### `ConfigurationState` — InventoryConfigurationState (enum) · **required**

The configuration state of the inventory table, indicating whether the inventory table is enabled
or disabled.

Values: `ENABLED`, `DISABLED`

### `EncryptionConfiguration` — MetadataTableEncryptionConfiguration

The encryption configuration for the inventory table.

## JSONInput (structure)

Specifies JSON as object's input serialization format.

### `Type` — JSONType (enum)

The type of JSON. Valid values: Document, Lines.

Values: `DOCUMENT`, `LINES`

## JSONOutput (structure)

Specifies JSON as request's output serialization format.

### `RecordDelimiter` — string

The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a
newline character ('\n').

## JSONType (enum)

Values: `DOCUMENT`, `LINES`

## JournalTableConfiguration (structure)

The journal table configuration for an S3 Metadata configuration.

### `RecordExpiration` — RecordExpiration · **required**

The journal table record expiration settings for the journal table.

### `EncryptionConfiguration` — MetadataTableEncryptionConfiguration

The encryption configuration for the journal table.

## JournalTableConfigurationResult (structure)

The journal table configuration for the S3 Metadata configuration.

### `TableStatus` — string · **required**

The status of the journal table. The status values are:

- `CREATING` - The journal table is in the process of being created in the specified
  table bucket.
- `ACTIVE` - The journal table has been created successfully, and records are being
  delivered to the table.
- `FAILED` - Amazon S3 is unable to create the journal table, or Amazon S3 is unable to deliver
  records.

### `Error` — ErrorDetails

If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2
`CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
unable to create the table, this structure contains the error code and error message.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `TableName` — string · **required**

The name of the journal table.

### `TableArn` — string

The Amazon Resource Name (ARN) for the journal table.

### `RecordExpiration` — RecordExpiration · **required**

The journal table record expiration settings for the journal table.

## JournalTableConfigurationUpdates (structure)

The specified updates to the S3 Metadata journal table configuration.

### `RecordExpiration` — RecordExpiration · **required**

The journal table record expiration settings for the journal table.

## LambdaFunctionConfiguration (structure)

A container for specifying the configuration for Lambda notifications.

### `Id` — string

An optional unique identifier for configurations in a notification configuration. If you don't
provide one, Amazon S3 will assign an ID.

### `LambdaFunctionArn` — string · **required**

The Amazon Resource Name (ARN) of the Lambda function that Amazon S3 invokes when the specified event
type occurs.

### `Events` — list<Event (enum)> · **required**

The Amazon S3 bucket event for which to invoke the Lambda function. For more information, see [Supported Event Types](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in
the *Amazon S3 User Guide*.

### `Filter` — NotificationConfigurationFilter

Specifies object key name filtering rules. For information about key name filtering, see [Configuring
event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the
*Amazon S3 User Guide*.

## LifecycleExpiration (structure)

Container for the expiration for the lifecycle of the object.

For more information see, [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in
the *Amazon S3 User Guide*.

### `Date` — timestamp

Indicates at what date the object is to be moved or deleted. The date value must conform to the ISO
8601 format. The time is always midnight UTC.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `Days` — integer

Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a
non-zero positive integer.

### `ExpiredObjectDeleteMarker` — boolean

Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the
delete marker will be expired; if set to false the policy takes no action. This cannot be specified with
Days or Date in a Lifecycle Expiration Policy.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

## LifecycleRule (structure)

A lifecycle rule for individual objects in an Amazon S3 bucket.

For more information see, [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in
the *Amazon S3 User Guide*.

### `Expiration` — LifecycleExpiration

Specifies the expiration for the lifecycle of the object in the form of date, days and, whether the
object has a delete marker.

### `ID` — string

Unique identifier for the rule. The value cannot be longer than 255 characters.

### `Prefix` — string · **deprecated**

The general purpose bucket prefix that identifies one or more objects to which the rule applies. We recommend using `Filter` instead of `Prefix` for new PUTs. Previous configurations where a prefix is defined will continue to operate as before.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `Filter` — LifecycleRuleFilter

The `Filter` is used to identify objects that a Lifecycle Rule applies to. A
`Filter` must have exactly one of `Prefix`, `Tag`,
`ObjectSizeGreaterThan`, `ObjectSizeLessThan`, or `And` specified.
`Filter` is required if the `LifecycleRule` does not contain a
`Prefix` element.

For more information about `Tag` filters, see [Adding filters to Lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-filters.html)
in the *Amazon S3 User Guide*.

`Tag` filters are not supported for directory buckets.

### `Status` — ExpirationStatus (enum) · **required**

If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being
applied.

Values: `Enabled`, `Disabled`

### `Transitions` — list<Transition>

Specifies when an Amazon S3 object transitions to a specified storage class.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `NoncurrentVersionTransitions` — list<NoncurrentVersionTransition>

Specifies the transition rule for the lifecycle rule that describes when noncurrent objects
transition to a specific storage class. If your bucket is versioning-enabled (or versioning is
suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to a
specific storage class at a set period in the object's lifetime.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `NoncurrentVersionExpiration` — NoncurrentVersionExpiration

Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the
noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning
enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in
the object's lifetime.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `AbortIncompleteMultipartUpload` — AbortIncompleteMultipartUpload

Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before
permanently removing all parts of the upload. For more information, see  [Aborting
Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) in the
*Amazon S3 User Guide*.

## LifecycleRuleAndOperator (structure)

This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The
Lifecycle Rule will apply to any object matching all of the predicates configured inside the And
operator.

### `Prefix` — string

Prefix identifying one or more objects to which the rule applies.

### `Tags` — list<Tag>

All of these tags must exist in the object's tag set in order for the rule to apply.

### `ObjectSizeGreaterThan` — long

Minimum object size to which the rule applies.

### `ObjectSizeLessThan` — long

Maximum object size to which the rule applies.

## LifecycleRuleFilter (structure)

The `Filter` is used to identify objects that a Lifecycle Rule applies to. A
`Filter` can have exactly one of `Prefix`, `Tag`,
`ObjectSizeGreaterThan`, `ObjectSizeLessThan`, or `And` specified. If
the `Filter` element is left empty, the Lifecycle Rule applies to all objects in the
bucket.

### `Prefix` — string

Prefix identifying one or more objects to which the rule applies.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `Tag` — Tag

This tag must exist in the object's tag set in order for the rule to apply.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `ObjectSizeGreaterThan` — long

Minimum object size to which the rule applies.

### `ObjectSizeLessThan` — long

Maximum object size to which the rule applies.

### `And` — LifecycleRuleAndOperator

This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The
Lifecycle Rule will apply to any object matching all of the predicates configured inside the And
operator.

## LocationInfo (structure)

Specifies the location where the bucket will be created.

For directory buckets, the location type is Availability Zone or Local Zone. For more information about
directory buckets, see [Working with
directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*.

This functionality is only supported by directory buckets.

### `Type` — LocationType (enum)

The type of location where the bucket will be created.

Values: `AvailabilityZone`, `LocalZone`

### `Name` — string

The name of the location where the bucket will be created.

For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where
the bucket will be created. An example AZ ID value is `usw2-az1`.

## LocationType (enum)

Values: `AvailabilityZone`, `LocalZone`

## LoggingEnabled (structure)

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a
bucket. For more information, see [PUT Bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html) in the
*Amazon S3 API Reference*.

### `TargetBucket` — string · **required**

Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs
delivered to any bucket that you own, including the same bucket that is being logged. You can also
configure multiple buckets to deliver their logs to the same target bucket. In this case, you should
choose a different `TargetPrefix` for each source bucket so that the delivered log files can
be distinguished by key.

### `TargetGrants` — list<TargetGrant>

Container for granting information.

Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants.
For more information, see [Permissions for server access log delivery](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general) in the
*Amazon S3 User Guide*.

### `TargetPrefix` — string · **required**

A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single
bucket, you can use a prefix to distinguish which log files came from which bucket.

### `TargetObjectKeyFormat` — TargetObjectKeyFormat

Amazon S3 key format for log objects.

## MFADelete (enum)

Values: `Enabled`, `Disabled`

## MFADeleteStatus (enum)

Values: `Enabled`, `Disabled`

## MetadataConfiguration (structure)

The S3 Metadata configuration for a general purpose bucket.

### `JournalTableConfiguration` — JournalTableConfiguration · **required**

The journal table configuration for a metadata configuration.

### `InventoryTableConfiguration` — InventoryTableConfiguration

The inventory table configuration for a metadata configuration.

### `AnnotationTableConfiguration` — AnnotationTableConfiguration

Optional annotation table configuration to include with the metadata configuration.

## MetadataConfigurationResult (structure)

The S3 Metadata configuration for a general purpose bucket.

### `DestinationResult` — DestinationResult · **required**

The destination settings for a metadata configuration.

### `JournalTableConfigurationResult` — JournalTableConfigurationResult

The journal table configuration for a metadata configuration.

### `InventoryTableConfigurationResult` — InventoryTableConfigurationResult

The inventory table configuration for a metadata configuration.

### `AnnotationTableConfigurationResult` — AnnotationTableConfigurationResult

The annotation table configuration result, if an annotation table is configured.

## MetadataDirective (enum)

Values: `COPY`, `REPLACE`

## MetadataEntry (structure)

A metadata key-value pair to store with an object.

### `Name` — string

Name of the object.

### `Value` — string

Value of the object.

## MetadataTableConfiguration (structure)

The V1 S3 Metadata configuration for a general purpose bucket.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `S3TablesDestination` — S3TablesDestination · **required**

The destination information for the metadata table configuration. The destination table bucket must
be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name
must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

## MetadataTableConfigurationResult (structure)

The V1 S3 Metadata configuration for a general purpose bucket. The destination table bucket must be
in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name
must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `S3TablesDestinationResult` — S3TablesDestinationResult · **required**

The destination information for the metadata table configuration. The destination table bucket must
be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name
must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

## MetadataTableEncryptionConfiguration (structure)

The encryption settings for an S3 Metadata journal table or inventory table configuration.

### `SseAlgorithm` — TableSseAlgorithm (enum) · **required**

The encryption type specified for a metadata table. To specify server-side encryption with
Key Management Service (KMS) keys (SSE-KMS), use the `aws:kms` value. To specify server-side
encryption with Amazon S3 managed keys (SSE-S3), use the `AES256` value.

Values: `aws:kms`, `AES256`

### `KmsKeyArn` — string

If server-side encryption with Key Management Service (KMS) keys (SSE-KMS) is specified, you must also
specify the KMS key Amazon Resource Name (ARN). You must specify a customer-managed KMS key
that's located in the same Region as the general purpose bucket that corresponds to the metadata
table configuration.

## Metrics (structure)

A container specifying replication metrics-related settings enabling replication metrics and
events.

### `Status` — MetricsStatus (enum) · **required**

Specifies whether the replication metrics are enabled.

Values: `Enabled`, `Disabled`

### `EventThreshold` — ReplicationTimeValue

A container specifying the time threshold for emitting the
`s3:Replication:OperationMissedThreshold` event.

## MetricsAndOperator (structure)

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
operator must have at least two predicates, and an object must match all of the predicates in order for
the filter to apply.

### `Prefix` — string

The prefix used when evaluating an AND predicate.

### `Tags` — list<Tag>

The list of tags used when evaluating an AND predicate.

`Tag` filters are not supported for directory buckets.

### `AccessPointArn` — string

The access point ARN used when evaluating an `AND` predicate.

## MetricsConfiguration (structure)

Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics
configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that
this is a full replacement of the existing metrics configuration. If you don't include the elements you
want to keep, they are erased. For more information, see [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html).

### `Id` — string · **required**

The ID used to identify the metrics configuration. The ID has a 64 character limit and can only
contain letters, numbers, periods, dashes, and underscores.

### `Filter` — MetricsFilter

Specifies a metrics configuration filter. The metrics configuration will only include objects that
meet the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a
conjunction (MetricsAndOperator).

Metrics configurations for directory buckets do not support tag filters.

## MetricsFilter (union)

Specifies a metrics configuration filter. The metrics configuration only includes objects that meet
the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction
(MetricsAndOperator). For more information, see [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html).

### `Prefix` — string

The prefix used when evaluating a metrics filter.

### `Tag` — Tag

The tag used when evaluating a metrics filter.

`Tag` filters are not supported for directory buckets.

### `AccessPointArn` — string

The access point ARN used when evaluating a metrics filter.

### `And` — MetricsAndOperator

A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
operator must have at least two predicates, and an object must match all of the predicates in order for
the filter to apply.

## MetricsStatus (enum)

Values: `Enabled`, `Disabled`

## MultipartUpload (structure)

Container for the `MultipartUpload` for the Amazon S3 object.

### `UploadId` — string

Upload ID that identifies the multipart upload.

### `Key` — string

Key of the object for which the multipart upload was initiated.

### `Initiated` — timestamp

Date and time at which the multipart upload was initiated.

### `StorageClass` — StorageClass (enum)

The class of storage used to store the object.

**Directory buckets** -
Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `Owner` — Owner

Specifies the owner of the object that is part of the multipart upload.

**Directory buckets** - The bucket owner is returned as the
object owner for all the objects.

### `Initiator` — Initiator

Identifies who initiated the multipart upload.

### `ChecksumAlgorithm` — ChecksumAlgorithm (enum)

The algorithm that was used to create a checksum of the object.

Values: `CRC32`, `CRC32C`, `SHA1`, `SHA256`, `CRC64NVME`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`

### `ChecksumType` — ChecksumType (enum)

The checksum type that is used to calculate the object’s checksum value. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

## NoncurrentVersionExpiration (structure)

Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the
noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning
enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in
the object's lifetime.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `NoncurrentDays` — integer

Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action.
The value must be a non-zero positive integer. For information about the noncurrent days calculations,
see [How Amazon S3 Calculates
When an Object Became Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations) in the *Amazon S3 User Guide*.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

### `NewerNoncurrentVersions` — integer

Specifies how many noncurrent versions Amazon S3 will retain. You can specify up to 100 noncurrent
versions to retain. Amazon S3 will permanently delete any additional noncurrent versions beyond the specified
number to retain. For more information about noncurrent versions, see [Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) in
the *Amazon S3 User Guide*.

This parameter applies to general purpose buckets only. It is not supported for directory bucket
lifecycle configurations.

## NoncurrentVersionTransition (structure)

Container for the transition rule that describes when noncurrent objects transition to the
`STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`,
`GLACIER_IR`, `GLACIER`, or `DEEP_ARCHIVE` storage class. If your
bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3
transition noncurrent object versions to the `STANDARD_IA`, `ONEZONE_IA`,
`INTELLIGENT_TIERING`, `GLACIER_IR`, `GLACIER`, or
`DEEP_ARCHIVE` storage class at a specific period in the object's lifetime.

### `NoncurrentDays` — integer

Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action.
For information about the noncurrent days calculations, see [How Amazon S3 Calculates
How Long an Object Has Been Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations) in the *Amazon S3 User Guide*.

### `StorageClass` — TransitionStorageClass (enum)

The class of storage used to store the object.

Values: `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`, `GLACIER_IR`

### `NewerNoncurrentVersions` — integer

Specifies how many noncurrent versions Amazon S3 will retain in the same storage class before
transitioning objects. You can specify up to 100 noncurrent versions to retain. Amazon S3 will transition any
additional noncurrent versions beyond the specified number to retain. For more information about
noncurrent versions, see [Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) in
the *Amazon S3 User Guide*.

## NotificationConfigurationFilter (structure)

Specifies object key name filtering rules. For information about key name filtering, see [Configuring
event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the
*Amazon S3 User Guide*.

### `Key` — S3KeyFilter

A container for object key name prefix and suffix filtering rules.

## Object (structure)

An object consists of data and its descriptive metadata.

### `Key` — string

The name that you assign to an object. You use the object key to retrieve the object.

### `LastModified` — timestamp

Creation date of the object.

### `ETag` — string

The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object,
not its metadata. The ETag may or may not be an MD5 digest of the object data. Whether or not it is
depends on how the object was created and how it is encrypted as described below:

- Objects created by the PUT Object, POST Object, or Copy operation, or through the Amazon Web Services
  Management Console, and are encrypted by SSE-S3 or plaintext, have ETags that are an MD5 digest of
  their object data.
- Objects created by the PUT Object, POST Object, or Copy operation, or through the Amazon Web Services
  Management Console, and are encrypted by SSE-C or SSE-KMS, have ETags that are not an MD5 digest of
  their object data.
- If an object is created by either the Multipart Upload or Part Copy operation, the ETag is not
  an MD5 digest, regardless of the method of encryption. If an object is larger than 16 MB, the Amazon Web Services
  Management Console will upload or copy that object as a Multipart Upload, and therefore the ETag
  will not be an MD5 digest.

**Directory buckets** - MD5 is not supported by directory buckets.

### `ChecksumAlgorithm` — list<ChecksumAlgorithm (enum)>

The algorithm that was used to create a checksum of the object.

### `ChecksumType` — ChecksumType (enum)

The checksum type that is used to calculate the object’s checksum value. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

### `Size` — long

Size in bytes of the object

### `StorageClass` — ObjectStorageClass (enum)

The class of storage used to store the object.

**Directory buckets** -
Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

### `Owner` — Owner

The owner of the object

**Directory buckets** - The bucket owner is returned as the
object owner.

### `RestoreStatus` — RestoreStatus

Specifies the restoration status of an object. Objects in certain storage classes must be restored
before they can be retrieved. For more information about these storage classes and how to work with
archived objects, see [Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

## ObjectAttributes (enum)

Values: `ETag`, `Checksum`, `ObjectParts`, `StorageClass`, `ObjectSize`

## ObjectCannedACL (enum)

Values: `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, `bucket-owner-full-control`

## ObjectEncryption (union)

The updated server-side encryption type for this object. The `UpdateObjectEncryption`
operation supports the SSE-S3 and SSE-KMS encryption types.

Valid Values: `SSES3` | `SSEKMS`

### `SSEKMS` — SSEKMSEncryption

Specifies to update the object encryption type to server-side encryption with Key Management Service (KMS) keys
(SSE-KMS).

## ObjectIdentifier (structure)

Object Identifier is unique value to identify objects.

### `Key` — string · **required**

Key name of the object.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `VersionId` — string

Version ID for the specific version of the object to delete.

This functionality is not supported for directory buckets.

### `ETag` — string

An entity tag (ETag) is an identifier assigned by a web server to a specific version of a resource
found at a URL. This header field makes the request method conditional on `ETags`.

Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings unique to the object.

### `LastModifiedTime` — timestamp

If present, the objects are deleted only if its modification times matches the provided
`Timestamp`.

This functionality is only supported for directory buckets.

### `Size` — long

If present, the objects are deleted only if its size matches the provided size in bytes.

This functionality is only supported for directory buckets.

## ObjectLockConfiguration (structure)

The container element for Object Lock configuration parameters.

### `ObjectLockEnabled` — ObjectLockEnabled (enum)

Indicates whether this bucket has an Object Lock configuration enabled. Enable
`ObjectLockEnabled` when you apply `ObjectLockConfiguration` to a bucket.

Values: `Enabled`

### `Rule` — ObjectLockRule

Specifies the Object Lock rule for the specified object. Enable the this rule when you apply
`ObjectLockConfiguration` to a bucket. Bucket settings require both a mode and a period.
The period can be either `Days` or `Years` but you must select one. You cannot
specify `Days` and `Years` at the same time.

## ObjectLockEnabled (enum)

Values: `Enabled`

## ObjectLockEventHold (enum)

Values: `ON`, `OFF`

## ObjectLockLegalHold (structure)

A legal hold configuration for an object.

### `Status` — ObjectLockLegalHoldStatus (enum)

Indicates whether the specified object has a legal hold in place.

Values: `ON`, `OFF`

## ObjectLockLegalHoldStatus (enum)

Values: `ON`, `OFF`

## ObjectLockMode (enum)

Values: `GOVERNANCE`, `COMPLIANCE`

## ObjectLockRetention (structure)

A Retention configuration for an object.

### `Mode` — ObjectLockRetentionMode (enum)

Indicates the Retention mode for the specified object.

Values: `GOVERNANCE`, `COMPLIANCE`

### `RetainUntilDate` — timestamp

The date on which this Object Lock Retention will expire.

### `EventHold` — ObjectLockEventHold (enum)

The event hold status for the object. Set to `ON` to enable an event hold or
`OFF` to disable it.

Values: `ON`, `OFF`

### `EventHoldDuration` — EventHoldDuration

The event hold duration for the object. Specifies how long the object remains protected after the
event hold is released.

## ObjectLockRetentionMode (enum)

Values: `GOVERNANCE`, `COMPLIANCE`

## ObjectLockRule (structure)

The container element for an Object Lock rule.

### `DefaultRetention` — DefaultRetention

The default Object Lock retention settings for new objects in this bucket. You can
specify:

- A default retention period, by using `Days` or `Years`.
- A default event hold duration, by using `DefaultEventHold`. This setting also
  uses days or years.

You can set one or both. You cannot use days and years in the same setting.

## ObjectOwnership (enum)

The container element for object ownership for a bucket's ownership controls.

`BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket
owner if the objects are uploaded with the `bucket-owner-full-control` canned ACL.

`ObjectWriter` - The uploading account will own the object if the object is uploaded with
the `bucket-owner-full-control` canned ACL.

`BucketOwnerEnforced` - Access control lists (ACLs) are disabled and no longer affect
permissions. The bucket owner automatically owns and has full control over every object in the bucket.
The bucket only accepts PUT requests that don't specify an ACL or specify bucket owner full control ACLs
(such as the predefined `bucket-owner-full-control` canned ACL or a custom ACL in XML format
that grants the same permissions).

By default, `ObjectOwnership` is set to `BucketOwnerEnforced` and ACLs are
disabled. We recommend keeping ACLs disabled, except in uncommon use cases where you must control access
for each object individually. For more information about S3 Object Ownership, see [Controlling
ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the
*Amazon S3 User Guide*.

This functionality is not supported for directory buckets. Directory buckets use the bucket owner enforced setting for S3 Object Ownership.

Values: `BucketOwnerPreferred`, `ObjectWriter`, `BucketOwnerEnforced`

## ObjectPart (structure)

A container for elements related to an individual part.

### `PartNumber` — integer

The part number identifying the part. This value is a positive integer between 1 and 10,000.

### `Size` — long

The size of the uploaded part in bytes.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if the
multipart upload request was created with the `CRC32` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if the
multipart upload request was created with the `CRC32C` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC64NVME` checksum algorithm, or if the
object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to
the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` checksum of the part. This checksum is present if the
multipart upload request was created with the `SHA1` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` checksum of the part. This checksum is present if
the multipart upload request was created with the `SHA256` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA512` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the part. This checksum is present if
the multipart upload request was created with the `MD5` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH64` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH3` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH128` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

## ObjectStorageClass (enum)

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

## ObjectVersion (structure)

The version of an object.

### `ETag` — string

The entity tag is an MD5 hash of that version of the object.

### `ChecksumAlgorithm` — list<ChecksumAlgorithm (enum)>

The algorithm that was used to create a checksum of the object.

### `ChecksumType` — ChecksumType (enum)

The checksum type that is used to calculate the object’s checksum value. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

Values: `COMPOSITE`, `FULL_OBJECT`

### `Size` — long

Size in bytes of the object.

### `StorageClass` — ObjectVersionStorageClass (enum)

The class of storage used to store the object.

Values: `STANDARD`

### `Key` — string

The object key.

### `VersionId` — string

Version ID of an object.

### `IsLatest` — boolean

Specifies whether the object is (true) or is not (false) the latest version of an object.

### `LastModified` — timestamp

Date and time when the object was last modified.

### `Owner` — Owner

Specifies the owner of the object.

### `RestoreStatus` — RestoreStatus

Specifies the restoration status of an object. Objects in certain storage classes must be restored
before they can be retrieved. For more information about these storage classes and how to work with
archived objects, see [Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html) in the *Amazon S3 User Guide*.

## ObjectVersionStorageClass (enum)

Values: `STANDARD`

## OptionalObjectAttributes (enum)

Values: `RestoreStatus`

## OutputLocation (structure)

Describes the location where the restore job's output is stored.

### `S3` — S3Location

Describes an S3 location that will receive the results of the restore request.

## OutputSerialization (structure)

Describes how results of the Select job are serialized.

### `CSV` — CSVOutput

Describes the serialization of CSV-encoded Select results.

### `JSON` — JSONOutput

Specifies JSON as request's output serialization format.

## Owner (structure)

Container for the owner's display name and ID.

### `DisplayName` — string

### `ID` — string

Container for the ID of the owner.

## OwnerOverride (enum)

Values: `Destination`

## OwnershipControls (structure)

The container element for a bucket's ownership controls.

### `Rules` — list<OwnershipControlsRule> · **required**

The container element for an ownership control rule.

## OwnershipControlsRule (structure)

The container element for an ownership control rule.

### `ObjectOwnership` — ObjectOwnership (enum) · **required**

The container element for object ownership for a bucket's ownership controls.

`BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket
owner if the objects are uploaded with the `bucket-owner-full-control` canned ACL.

`ObjectWriter` - The uploading account will own the object if the object is uploaded with
the `bucket-owner-full-control` canned ACL.

`BucketOwnerEnforced` - Access control lists (ACLs) are disabled and no longer affect
permissions. The bucket owner automatically owns and has full control over every object in the bucket.
The bucket only accepts PUT requests that don't specify an ACL or specify bucket owner full control ACLs
(such as the predefined `bucket-owner-full-control` canned ACL or a custom ACL in XML format
that grants the same permissions).

By default, `ObjectOwnership` is set to `BucketOwnerEnforced` and ACLs are
disabled. We recommend keeping ACLs disabled, except in uncommon use cases where you must control access
for each object individually. For more information about S3 Object Ownership, see [Controlling
ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the
*Amazon S3 User Guide*.

This functionality is not supported for directory buckets. Directory buckets use the bucket owner enforced setting for S3 Object Ownership.

Values: `BucketOwnerPreferred`, `ObjectWriter`, `BucketOwnerEnforced`

## ParquetInput (structure)

Container for Parquet.

## Part (structure)

Container for elements related to a part.

### `PartNumber` — integer

Part number identifying the part. This is a positive integer between 1 and 10,000.

### `LastModified` — timestamp

Date and time at which the part was uploaded.

### `ETag` — string

Entity tag returned when the part was uploaded.

### `Size` — long

Size in bytes of the uploaded part data.

### `ChecksumCRC32` — string

The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if the
object was uploaded with the `CRC32` checksum algorithm. For more information, see [Checking object
integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC32C` — string

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if the
object was uploaded with the `CRC32C` checksum algorithm. For more information, see [Checking object
integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumCRC64NVME` — string

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if
the multipart upload request was created with the `CRC64NVME` checksum algorithm, or if the
object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME`, to
the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumSHA1` — string

The Base64 encoded, 160-bit `SHA1` checksum of the part. This checksum is present if the
object was uploaded with the `SHA1` checksum algorithm. For more information, see [Checking object
integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA256` — string

The Base64 encoded, 256-bit `SHA256` checksum of the part. This checksum is present if
the object was uploaded with the `SHA256` checksum algorithm. For more information, see
[Checking
object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.

### `ChecksumSHA512` — string

The Base64 encoded, 512-bit `SHA512` digest of the part. This checksum is present if
the multipart upload request was created with the `SHA512` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumMD5` — string

The Base64 encoded, 128-bit `MD5` digest of the part. This checksum is present if
the multipart upload request was created with the `MD5` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH64` — string

The Base64 encoded, 64-bit `XXHASH64` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH64` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH3` — string

The Base64 encoded, 64-bit `XXHASH3` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH3` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

### `ChecksumXXHASH128` — string

The Base64 encoded, 128-bit `XXHASH128` checksum of the part. This checksum is present if
the multipart upload request was created with the `XXHASH128` checksum algorithm. For more
information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in
the *Amazon S3 User Guide*.

## PartitionDateSource (enum)

Values: `EventTime`, `DeliveryTime`

## PartitionedPrefix (structure)

Amazon S3 keys for log objects are partitioned in the following format:

`[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

PartitionedPrefix defaults to EventTime delivery when server access logs are delivered.

### `PartitionDateSource` — PartitionDateSource (enum)

Specifies the partition date source for the partitioned prefix. `PartitionDateSource` can
be `EventTime` or `DeliveryTime`.

For `DeliveryTime`, the time in the log file names corresponds to the delivery time for
the log files.

For `EventTime`, The logs delivered are for a specific day only. The year, month, and
day correspond to the day on which the event occurred, and the hour, minutes and seconds are set to 00
in the key.

Values: `EventTime`, `DeliveryTime`

## Payer (enum)

Values: `Requester`, `BucketOwner`

## Permission (enum)

Values: `FULL_CONTROL`, `WRITE`, `WRITE_ACP`, `READ`, `READ_ACP`

## PolicyStatus (structure)

The container element for a bucket's policy status.

### `IsPublic` — boolean

The policy status for this bucket. `TRUE` indicates that this bucket is public.
`FALSE` indicates that the bucket is not public.

## Progress (structure)

This data type contains information about progress of an operation.

### `BytesScanned` — long

The current number of object bytes scanned.

### `BytesProcessed` — long

The current number of uncompressed object bytes processed.

### `BytesReturned` — long

The current number of bytes of records payload data returned.

## ProgressEvent (structure)

This data type contains information about the progress event of an operation.

### `Details` — Progress

The Progress event details.

## Protocol (enum)

Values: `http`, `https`

## PublicAccessBlockConfiguration (structure)

The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can
enable the configuration options in any combination. Bucket-level settings work alongside
account-level settings (which may inherit from organization-level policies). For more
information about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.

### `BlockPublicAcls` — boolean

Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects
in this bucket. Setting this element to `TRUE` causes the following behavior:

- PUT Bucket ACL and PUT Object ACL calls fail if the specified ACL is public.
- PUT Object calls fail if the request includes a public ACL.
- PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesn't affect existing policies or ACLs.

### `IgnorePublicAcls` — boolean

Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting
this element to `TRUE` causes Amazon S3 to ignore all public ACLs on this bucket and objects in
this bucket.

Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new
public ACLs from being set.

### `BlockPublicPolicy` — boolean

Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to
`TRUE` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy
allows public access.

Enabling this setting doesn't affect existing bucket policies.

### `RestrictPublicBuckets` — boolean

Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element
to `TRUE` restricts access to this bucket to only Amazon Web Services service principals and
authorized users within this account if the bucket has a public policy.

Enabling this setting doesn't affect previously stored bucket policies, except that public and
cross-account access within any public bucket policy, including non-public delegation to specific
accounts, is blocked.

## QueueConfiguration (structure)

Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS)
queue when Amazon S3 detects specified events.

### `Id` — string

An optional unique identifier for configurations in a notification configuration. If you don't
provide one, Amazon S3 will assign an ID.

### `QueueArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it
detects events of the specified type.

### `Events` — list<Event (enum)> · **required**

A collection of bucket events for which to send notifications

### `Filter` — NotificationConfigurationFilter

Specifies object key name filtering rules. For information about key name filtering, see [Configuring
event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the
*Amazon S3 User Guide*.

## QuoteFields (enum)

Values: `ALWAYS`, `ASNEEDED`

## RecordExpiration (structure)

The journal table record expiration settings for a journal table in an S3 Metadata configuration.

### `Expiration` — ExpirationState (enum) · **required**

Specifies whether journal table record expiration is enabled or disabled.

Values: `ENABLED`, `DISABLED`

### `Days` — integer

If you enable journal table record expiration, you can set the number of days to retain your
journal table records. Journal table records must be retained for a minimum of 7 days. To set
this value, specify any whole number from `7` to `2147483647`. For example,
to retain your journal table records for one year, set this value to `365`.

## RecordsEvent (structure)

The container for the records event.

### `Payload` — blob

The byte array of partial, one or more result records. S3 Select doesn't guarantee that a record
will be self-contained in one record frame. To ensure continuous streaming of data, S3 Select might
split the same record across multiple record frames instead of aggregating the results in memory. Some
S3 clients (for example, the SDK for Java) handle this behavior by creating a
`ByteStream` out of the response by default. Other clients might not handle this behavior
by default. In those cases, you must aggregate the results on the client side and parse the
response.

## Redirect (structure)

Specifies how requests are redirected. In the event of an error, you can specify a different error
code to return.

### `HostName` — string

The host name to use in the redirect request.

### `HttpRedirectCode` — string

The HTTP redirect code to use on the response. Not required if one of the siblings is
present.

### `Protocol` — Protocol (enum)

Protocol to use when redirecting requests. The default is the protocol that is used in the original
request.

Values: `http`, `https`

### `ReplaceKeyPrefixWith` — string

The object key prefix to use in the redirect request. For example, to redirect requests for all
pages with prefix `docs/` (objects in the `docs/` folder) to
`documents/`, you can set a condition block with `KeyPrefixEquals` set to
`docs/` and in the Redirect set `ReplaceKeyPrefixWith` to
`/documents`. Not required if one of the siblings is present. Can be present only if
`ReplaceKeyWith` is not provided.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `ReplaceKeyWith` — string

The specific object key to use in the redirect request. For example, redirect request to
`error.html`. Not required if one of the siblings is present. Can be present only if
`ReplaceKeyPrefixWith` is not provided.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

## RedirectAllRequestsTo (structure)

Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

### `HostName` — string · **required**

Name of the host where requests are redirected.

### `Protocol` — Protocol (enum)

Protocol to use when redirecting requests. The default is the protocol that is used in the original
request.

Values: `http`, `https`

## ReplicaModifications (structure)

A filter that you can specify for selection for modifications on replicas. Amazon S3 doesn't replicate
replica modifications by default. In the latest version of replication configuration (when
`Filter` is specified), you can specify this element and set the status to
`Enabled` to replicate modifications on replicas.

If you don't specify the `Filter` element, Amazon S3 assumes that the replication
configuration is the earlier version, V1. In the earlier version, this element is not allowed.

### `Status` — ReplicaModificationsStatus (enum) · **required**

Specifies whether Amazon S3 replicates modifications on replicas.

Values: `Enabled`, `Disabled`

## ReplicaModificationsStatus (enum)

Values: `Enabled`, `Disabled`

## ReplicationConfiguration (structure)

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication
configuration is 2 MB.

### `Role` — string · **required**

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that Amazon S3 assumes when replicating
objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html) in the
*Amazon S3 User Guide*.

### `Rules` — list<ReplicationRule> · **required**

A container for one or more replication rules. A replication configuration must have at least one
rule and can contain a maximum of 1,000 rules.

## ReplicationRule (structure)

Specifies which Amazon S3 objects to replicate and where to store the replicas.

### `ID` — string

A unique identifier for the rule. The maximum value is 255 characters.

### `Priority` — integer

The priority indicates which rule has precedence whenever two or more replication rules conflict.
Amazon S3 will attempt to replicate objects according to all replication rules. However, if there are two or
more rules with the same destination bucket, then objects will be replicated according to the rule with
the highest priority. The higher the number, the higher the priority.

For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the *Amazon S3 User Guide*.

### `Prefix` — string · **deprecated**

An object key name prefix that identifies the object or objects to which the rule applies. The
maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `Filter` — ReplicationRuleFilter

A filter that identifies the subset of objects to which the replication rule applies. A
`Filter` must specify exactly one `Prefix`, `Tag`, or an
`And` child element.

### `Status` — ReplicationRuleStatus (enum) · **required**

Specifies whether the rule is enabled.

Values: `Enabled`, `Disabled`

### `SourceSelectionCriteria` — SourceSelectionCriteria

A container that describes additional filters for identifying the source objects that you want to
replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3
supports only the filter that you can specify for objects created with server-side encryption using a
customer managed key stored in Amazon Web Services Key Management Service (SSE-KMS).

### `ExistingObjectReplication` — ExistingObjectReplication

Optional configuration to replicate existing source bucket objects.

This parameter is no longer supported. To replicate existing objects, see [Replicating
existing objects with S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) in the
*Amazon S3 User Guide*.

### `Destination` — Destination · **required**

A container for information about the replication destination and its configurations including
enabling the S3 Replication Time Control (S3 RTC).

### `DeleteMarkerReplication` — DeleteMarkerReplication

Specifies whether Amazon S3 replicates delete markers. If you specify a `Filter` in your
replication configuration, you must also include a `DeleteMarkerReplication` element. If your
`Filter` includes a `Tag` element, the `DeleteMarkerReplication`
`Status` must be set to Disabled, because Amazon S3 does not support replicating delete markers
for tag-based rules. For an example configuration, see [Basic Rule
Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config).

For more information about delete marker replication, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html).

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of
delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations).

## ReplicationRuleAndOperator (structure)

A container for specifying rule filters. The filters determine the subset of objects to which the
rule applies. This element is required only if you specify more than one filter.

For example:

- If you specify both a `Prefix` and a `Tag` filter, wrap these filters in
  an `And` tag.
- If you specify a filter based on multiple tags, wrap the `Tag` elements in an
  `And` tag.

### `Prefix` — string

An object key name prefix that identifies the subset of objects to which the rule applies.

### `Tags` — list<Tag>

An array of tags containing key and value pairs.

## ReplicationRuleFilter (structure)

A filter that identifies the subset of objects to which the replication rule applies. A
`Filter` must specify exactly one `Prefix`, `Tag`, or an
`And` child element.

### `Prefix` — string

An object key name prefix that identifies the subset of objects to which the rule applies.

Replacement must be made for object keys containing special characters (such as carriage returns) when using
XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).

### `Tag` — Tag

A container for specifying a tag key and value.

The rule applies only to objects that have the tag in their tag set.

### `And` — ReplicationRuleAndOperator

A container for specifying rule filters. The filters determine the subset of objects to which the
rule applies. This element is required only if you specify more than one filter. For example:

- If you specify both a `Prefix` and a `Tag` filter, wrap these filters in
  an `And` tag.
- If you specify a filter based on multiple tags, wrap the `Tag` elements in an
  `And` tag.

## ReplicationRuleStatus (enum)

Values: `Enabled`, `Disabled`

## ReplicationStatus (enum)

Values: `COMPLETE`, `PENDING`, `FAILED`, `REPLICA`, `COMPLETED`

## ReplicationTime (structure)

A container specifying S3 Replication Time Control (S3 RTC) related information, including whether S3 RTC is enabled and
the time when all objects and operations on objects must be replicated. Must be specified together with
a `Metrics` block.

### `Status` — ReplicationTimeStatus (enum) · **required**

Specifies whether the replication time is enabled.

Values: `Enabled`, `Disabled`

### `Time` — ReplicationTimeValue · **required**

A container specifying the time by which replication should be complete for all objects and
operations on objects.

## ReplicationTimeStatus (enum)

Values: `Enabled`, `Disabled`

## ReplicationTimeValue (structure)

A container specifying the time value for S3 Replication Time Control (S3 RTC) and replication metrics
`EventThreshold`.

### `Minutes` — integer

Contains an integer specifying time in minutes.

Valid value: 15

## RequestCharged (enum)

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## RequestPayer (enum)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## RequestPaymentConfiguration (structure)

Container for Payer.

### `Payer` — Payer (enum) · **required**

Specifies who pays for the download and request fees.

Values: `Requester`, `BucketOwner`

## RequestProgress (structure)

Container for specifying if periodic `QueryProgress` messages should be sent.

### `Enabled` — boolean

Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default
value: FALSE.

## RestoreRequest (structure)

Container for restore job parameters.

### `Days` — integer

Lifetime of the active copy in days. Do not use with restores that specify
`OutputLocation`.

The Days element is required for regular restores, and must not be provided for select
requests.

### `GlacierJobParameters` — GlacierJobParameters

S3 Glacier related parameters pertaining to this job. Do not use with restores that specify
`OutputLocation`.

### `Type` — RestoreRequestType (enum)

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Type of restore request.

Values: `SELECT`

### `Tier` — Tier (enum)

Retrieval tier at which the restore will be processed.

Values: `Standard`, `Bulk`, `Expedited`

### `Description` — string

The optional description for the job.

### `SelectParameters` — SelectParameters

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Describes the parameters for Select job types.

### `OutputLocation` — OutputLocation

Describes the location where the restore job's output is stored.

## RestoreRequestType (enum)

Values: `SELECT`

## RestoreStatus (structure)

Specifies the restoration status of an object. Objects in certain storage classes must be restored
before they can be retrieved. For more information about these storage classes and how to work with
archived objects, see [Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

### `IsRestoreInProgress` — boolean

Specifies whether the object is currently being restored. If the object restoration is in progress,
the header returns the value `TRUE`. For example:

`x-amz-optional-object-attributes: IsRestoreInProgress="true"`

If the object restoration has completed, the header returns the value `FALSE`. For
example:

`x-amz-optional-object-attributes: IsRestoreInProgress="false",
RestoreExpiryDate="2012-12-21T00:00:00.000Z"`

If the object hasn't been restored, there is no header response.

### `RestoreExpiryDate` — timestamp

Indicates when the restored copy will expire. This value is populated only if the object has already
been restored. For example:

`x-amz-optional-object-attributes: IsRestoreInProgress="false",
RestoreExpiryDate="2012-12-21T00:00:00.000Z"`

## RoutingRule (structure)

Specifies the redirect behavior and when a redirect is applied. For more information about routing
rules, see [Configuring
advanced conditional redirects](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html#advanced-conditional-redirects) in the *Amazon S3 User Guide*.

### `Condition` — Condition

A container for describing a condition that must be met for the specified redirect to apply. For
example, 1. If request is for pages in the `/docs` folder, redirect to the
`/documents` folder. 2. If request results in HTTP error 4xx, redirect request to another
host where you might process the error.

### `Redirect` — Redirect · **required**

Container for redirect information. You can redirect requests to another host, to another page, or
with another protocol. In the event of an error, you can specify a different error code to
return.

## S3KeyFilter (structure)

A container for object key name prefix and suffix filtering rules.

### `FilterRules` — list<FilterRule>

A list of containers for the key-value pair that defines the criteria for the filter rule.

## S3Location (structure)

Describes an Amazon S3 location that will receive the results of the restore request.

### `BucketName` — string · **required**

The name of the bucket where the restore results will be placed.

### `Prefix` — string · **required**

The prefix that is prepended to the restore results for this request.

### `Encryption` — Encryption

Contains the type of server-side encryption used.

### `CannedACL` — ObjectCannedACL (enum)

The canned ACL to apply to the restore results.

Values: `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, `bucket-owner-full-control`

### `AccessControlList` — list<Grant>

A list of grants that control access to the staged results.

### `Tagging` — Tagging

The tag-set that is applied to the restore results.

### `UserMetadata` — list<MetadataEntry>

A list of metadata to store with the restore results in S3.

### `StorageClass` — StorageClass (enum)

The class of storage used to store the restore results.

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

## S3TablesBucketType (enum)

Values: `aws`, `customer`

## S3TablesDestination (structure)

The destination information for a V1 S3 Metadata configuration. The destination table bucket must
be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name
must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `TableBucketArn` — string · **required**

The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the
metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account
as the general purpose bucket.

### `TableName` — string · **required**

The name for the metadata table in your metadata table configuration. The specified metadata table
name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

## S3TablesDestinationResult (structure)

The destination information for a V1 S3 Metadata configuration. The destination table bucket must
be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name
must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create
a live inventory table.

### `TableBucketArn` — string · **required**

The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the
metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account
as the general purpose bucket.

### `TableName` — string · **required**

The name for the metadata table in your metadata table configuration. The specified metadata table
name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

### `TableArn` — string · **required**

The Amazon Resource Name (ARN) for the metadata table in the metadata table configuration. The
specified metadata table name must be unique within the `aws_s3_metadata` namespace in the
destination table bucket.

### `TableNamespace` — string · **required**

The table bucket namespace for the metadata table in your metadata table configuration. This value
is always `aws_s3_metadata`.

## SSEKMS (structure)

Specifies the use of SSE-KMS to encrypt delivered inventory reports.

### `KeyId` — string · **required**

Specifies the ID of the Key Management Service (KMS) symmetric encryption customer managed key to use for encrypting
inventory reports.

## SSEKMSEncryption (structure)

If `SSEKMS` is specified for `ObjectEncryption`, this data type specifies
the Amazon Web Services KMS key Amazon Resource Name (ARN) to use and whether to use an S3 Bucket Key for
server-side encryption using Key Management Service (KMS) keys (SSE-KMS).

### `KMSKeyArn` — string · **required**

Specifies the Amazon Web Services KMS key Amazon Resource Name (ARN) to use for the updated server-side encryption
type. Required if `ObjectEncryption` specifies `SSEKMS`.

You must specify the full Amazon Web Services KMS key ARN. The KMS key ID and KMS key alias aren't
supported.

Pattern: (`arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+`)

### `BucketKeyEnabled` — boolean

Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption
using Key Management Service (KMS) keys (SSE-KMS). If this value isn't specified, it defaults to `false`.
Setting this value to `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with
SSE-KMS. For more information, see
[Using Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) in the *Amazon S3 User Guide*.

Valid Values: `true` | `false`

## SSES3 (structure)

Specifies the use of SSE-S3 to encrypt delivered inventory reports.

## ScanRange (structure)

Specifies the byte range of the object to get the records from. A record is processed when its first
byte is contained by the range. This parameter is optional, but when specified, it must not be empty.
See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

### `Start` — long

Specifies the start of the byte range. This parameter is optional. Valid values: non-negative
integers. The default value is 0. If only `start` is supplied, it means scan from that point
to the end of the file. For example,
`50` means scan from byte 50
until the end of the file.

### `End` — long

Specifies the end of the byte range. This parameter is optional. Valid values: non-negative
integers. The default value is one less than the size of the object being queried. If only the End
parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For example,
`50` means scan the last 50
bytes.

## SelectObjectContentEventStream (union)

The container for selecting objects from a content event stream.

### `Records` — RecordsEvent

The Records Event.

### `Stats` — StatsEvent

The Stats Event.

### `Progress` — ProgressEvent

The Progress Event.

### `Cont` — ContinuationEvent

The Continuation Event.

### `End` — EndEvent

The End Event.

## SelectParameters (structure)

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Describes the parameters for Select job types.

Learn [How to
optimize querying your data in Amazon S3](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/) using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html), or client-side
filtering.

### `InputSerialization` — InputSerialization · **required**

Describes the serialization format of the object.

### `ExpressionType` — ExpressionType (enum) · **required**

The type of the provided expression (for example, SQL).

Values: `SQL`

### `Expression` — string · **required**

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

The expression that is used to query the object.

### `OutputSerialization` — OutputSerialization · **required**

Describes how the results of the Select job are serialized.

## ServerSideEncryption (enum)

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

## ServerSideEncryptionByDefault (structure)

Describes the default server-side encryption to apply to new objects in the bucket. If a PUT Object
request doesn't specify any server-side encryption, this default encryption will be applied. For more
information, see [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTencryption.html).

- **General purpose buckets** - If you don't specify a customer managed key
  at configuration, Amazon S3 automatically creates an Amazon Web Services KMS key (`aws/s3`) in your Amazon Web Services
  account the first time that you add an object encrypted with SSE-KMS to a bucket. By default, Amazon S3
  uses this KMS key for SSE-KMS.
- **Directory buckets** -
  Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket's lifetime.
  The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3`) isn't supported.
- **Directory buckets** -
  For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS.

### `SSEAlgorithm` — ServerSideEncryption (enum) · **required**

Server-side encryption algorithm to use for the default encryption.

For directory buckets, there are only two supported values for server-side encryption: `AES256` and `aws:kms`.

Values: `AES256`, `aws:fsx`, `aws:backup`, `aws:kms`, `aws:kms:dsse`

### `KMSMasterKeyID` — string

Amazon Web Services Key Management Service (KMS) customer managed key ID to use for the default encryption.

- **General purpose buckets** - This parameter is allowed if and
  only if `SSEAlgorithm` is set to `aws:kms` or
  `aws:kms:dsse`.
- **Directory buckets** - This parameter is allowed if and
  only if `SSEAlgorithm` is set to `aws:kms`.

You can specify the key ID, key alias, or the Amazon Resource Name (ARN) of the KMS key.

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN:
  `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Key Alias: `alias/alias-name`

If you are using encryption with cross-account or Amazon Web Services service operations, you must use a fully
qualified KMS key ARN. For more information, see [Using
encryption for cross-account operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-update-bucket-policy).

- **General purpose buckets** - If you're specifying a customer
  managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key
  alias instead, then KMS resolves the key within the requester’s account. This behavior can
  result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket
  owner. Also, if you use a key ID, you can run into a LogDestination undeliverable error when
  creating a VPC flow log.
- **Directory buckets** -
  When you specify an [KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in
Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Amazon Web Services Key Management Service Developer Guide*.

## ServerSideEncryptionConfiguration (structure)

Specifies the default server-side-encryption configuration.

### `Rules` — list<ServerSideEncryptionRule> · **required**

Container for information about a particular server-side encryption configuration rule.

## ServerSideEncryptionRule (structure)

Specifies the default server-side encryption configuration.

- **General purpose buckets** - If you're specifying a customer
  managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key
  alias instead, then KMS resolves the key within the requester’s account. This behavior can
  result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket
  owner.
- **Directory buckets** -
  When you specify an [KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

### `ApplyServerSideEncryptionByDefault` — ServerSideEncryptionByDefault

Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object
request doesn't specify any server-side encryption, this default encryption will be applied.

### `BucketKeyEnabled` — boolean

Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS)
for new objects in the bucket. Existing objects are not affected. Setting the
`BucketKeyEnabled` element to `true` causes Amazon S3 to use an S3 Bucket Key.

- **General purpose buckets** - By default, S3 Bucket Key is not
  enabled. For more information, see [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) in the
  *Amazon S3 User Guide*.
- **Directory buckets** -
  S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
  to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html), [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops), or
  [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job). In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.

### `BlockedEncryptionTypes` — BlockedEncryptionTypes

A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type. For example, blocking an encryption type will block `PutObject`, `CopyObject`, `PostObject`, multipart upload, and replication requests to the bucket for objects with the specified encryption type. However, you can continue to read and list any pre-existing objects already encrypted with the specified encryption type. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).

Currently, this parameter only supports blocking or unblocking server-side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).

## SessionCredentials (structure)

The established temporary security credentials of the session.

**Directory buckets** - These session credentials are only
supported for the authentication and authorization of Zonal endpoint API operations on directory buckets.

### `AccessKeyId` — string · **required**

A unique identifier that's associated with a secret access key. The access key ID and the secret
access key are used together to sign programmatic Amazon Web Services requests cryptographically.

### `SecretAccessKey` — string · **required**

A key that's used with the access key ID to cryptographically sign programmatic Amazon Web Services requests.
Signing a request identifies the sender and prevents the request from being altered.

### `SessionToken` — string · **required**

A part of the temporary security credentials. The session token is used to validate the temporary
security credentials.

### `Expiration` — timestamp · **required**

Temporary security credentials expire after a specified interval. After temporary credentials
expire, any calls that you make with those credentials will fail. So you must generate a new set of
temporary credentials. Temporary credentials cannot be extended or refreshed beyond the original
specified interval.

## SessionMode (enum)

Values: `ReadOnly`, `ReadWrite`

## SimplePrefix (structure)

To use simple format for S3 keys for log objects, set SimplePrefix to an empty object.

`[DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

## SourceSelectionCriteria (structure)

A container that describes additional filters for identifying the source objects that you want to
replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3
supports only the filter that you can specify for objects created with server-side encryption using a
customer managed key stored in Amazon Web Services Key Management Service (SSE-KMS).

### `SseKmsEncryptedObjects` — SseKmsEncryptedObjects

A container for filter information for the selection of Amazon S3 objects encrypted with Amazon Web Services KMS. If
you include `SourceSelectionCriteria` in the replication configuration, this element is
required.

### `ReplicaModifications` — ReplicaModifications

A filter that you can specify for selections for modifications on replicas. Amazon S3 doesn't replicate
replica modifications by default. In the latest version of replication configuration (when
`Filter` is specified), you can specify this element and set the status to
`Enabled` to replicate modifications on replicas.

If you don't specify the `Filter` element, Amazon S3 assumes that the replication
configuration is the earlier version, V1. In the earlier version, this element is not allowed

## SseKmsEncryptedObjects (structure)

A container for filter information for the selection of S3 objects encrypted with Amazon Web Services KMS.

### `Status` — SseKmsEncryptedObjectsStatus (enum) · **required**

Specifies whether Amazon S3 replicates objects created with server-side encryption using an Amazon Web Services KMS key
stored in Amazon Web Services Key Management Service.

Values: `Enabled`, `Disabled`

## SseKmsEncryptedObjectsStatus (enum)

Values: `Enabled`, `Disabled`

## Stats (structure)

Container for the stats details.

### `BytesScanned` — long

The total number of object bytes scanned.

### `BytesProcessed` — long

The total number of uncompressed object bytes processed.

### `BytesReturned` — long

The total number of bytes of records payload data returned.

## StatsEvent (structure)

Container for the Stats Event.

### `Details` — Stats

The Stats event details.

## StorageClass (enum)

Values: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`, `GLACIER_IR`, `SNOW`, `EXPRESS_ONEZONE`, `FSX_OPENZFS`, `FSX_ONTAP`, `AWS_BACKUP_WARM`, `AWS_BACKUP_LOW_COST_WARM`

## StorageClassAnalysis (structure)

Specifies data related to access patterns to be collected and made available to analyze the
tradeoffs between different storage classes for an Amazon S3 bucket.

### `DataExport` — StorageClassAnalysisDataExport

Specifies how data related to the storage class analysis for an Amazon S3 bucket should be
exported.

## StorageClassAnalysisDataExport (structure)

Container for data related to the storage class analysis for an Amazon S3 bucket for export.

### `OutputSchemaVersion` — StorageClassAnalysisSchemaVersion (enum) · **required**

The version of the output schema to use when exporting data. Must be `V_1`.

Values: `V_1`

### `Destination` — AnalyticsExportDestination · **required**

The place to store the data for an analysis.

## StorageClassAnalysisSchemaVersion (enum)

Values: `V_1`

## TableSseAlgorithm (enum)

Values: `aws:kms`, `AES256`

## Tag (structure)

A container of a key value name pair.

### `Key` — string · **required**

Name of the object key.

### `Value` — string · **required**

Value of the tag.

## Tagging (structure)

Container for `TagSet` elements.

### `TagSet` — list<Tag> · **required**

A collection for a set of tags

## TaggingDirective (enum)

Values: `COPY`, `REPLACE`

## TargetGrant (structure)

Container for granting information.

Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants.
For more information, see [Permissions server access log delivery](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general) in the *Amazon S3 User Guide*.

### `Grantee` — Grantee

Container for the person being granted permissions.

### `Permission` — BucketLogsPermission (enum)

Logging permissions assigned to the grantee for the bucket.

Values: `FULL_CONTROL`, `READ`, `WRITE`

## TargetObjectKeyFormat (structure)

Amazon S3 key format for log objects. Only one format, PartitionedPrefix or SimplePrefix, is
allowed.

### `SimplePrefix` — SimplePrefix

To use the simple format for S3 keys for log objects. To specify SimplePrefix format, set
SimplePrefix to {}.

### `PartitionedPrefix` — PartitionedPrefix

Partitioned S3 key for log objects.

## Tier (enum)

Values: `Standard`, `Bulk`, `Expedited`

## Tiering (structure)

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically
moving data to the most cost-effective storage access tier, without additional operational
overhead.

### `Days` — integer · **required**

The number of consecutive days of no access after which an object will be eligible to be
transitioned to the corresponding tier. The minimum number of days specified for Archive Access tier
must be at least 90 days and Deep Archive Access tier must be at least 180 days. The maximum can be up to
2 years (730 days).

### `AccessTier` — IntelligentTieringAccessTier (enum) · **required**

S3 Intelligent-Tiering access tier. See [Storage class for
automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access) for a list of access
tiers in the S3 Intelligent-Tiering storage class.

Values: `ARCHIVE_ACCESS`, `DEEP_ARCHIVE_ACCESS`

## TopicConfiguration (structure)

A container for specifying the configuration for publication of messages to an Amazon Simple
Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

### `Id` — string

An optional unique identifier for configurations in a notification configuration. If you don't
provide one, Amazon S3 will assign an ID.

### `TopicArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it
detects events of the specified type.

### `Events` — list<Event (enum)> · **required**

The Amazon S3 bucket event about which to send notifications. For more information, see [Supported Event Types](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in
the *Amazon S3 User Guide*.

### `Filter` — NotificationConfigurationFilter

Specifies object key name filtering rules. For information about key name filtering, see [Configuring
event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the
*Amazon S3 User Guide*.

## Transition (structure)

Specifies when an object transitions to a specified storage class. For more information about Amazon S3
lifecycle configuration rules, see [Transitioning Objects Using
Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html) in the *Amazon S3 User Guide*.

### `Date` — timestamp

Indicates when objects are transitioned to the specified storage class. The date value must be in
ISO 8601 format. The time is always midnight UTC.

### `Days` — integer

Indicates the number of days after creation when objects are transitioned to the specified storage
class. The value can be `0` or any positive integer. Be aware that some storage classes have a
minimum storage duration and that you're charged for transitioning objects before their minimum storage
duration. For more information, see  [Constraints and considerations for transitions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-configuration-constraints) in the *Amazon S3 User
Guide*.

### `StorageClass` — TransitionStorageClass (enum)

The storage class to which you want the object to transition.

Values: `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`, `GLACIER_IR`

## TransitionDefaultMinimumObjectSize (enum)

Values: `varies_by_storage_class`, `all_storage_classes_128K`

## TransitionStorageClass (enum)

Values: `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`, `GLACIER_IR`

## Type (enum)

Values: `CanonicalUser`, `AmazonCustomerByEmail`, `Group`

## VersioningConfiguration (structure)

Describes the versioning state of an Amazon S3 bucket. For more information, see [PUT Bucket
versioning](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTVersioningStatus.html) in the *Amazon S3 API Reference*.

### `MFADelete` — MFADelete (enum)

Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only
returned if the bucket has been configured with MFA delete. If the bucket has never been so configured,
this element is not returned.

Values: `Enabled`, `Disabled`

### `Status` — BucketVersioningStatus (enum)

The versioning state of the bucket.

Values: `Enabled`, `Suspended`

## WebsiteConfiguration (structure)

Specifies website configuration parameters for an Amazon S3 bucket.

### `ErrorDocument` — ErrorDocument

The name of the error document for the website.

### `IndexDocument` — IndexDocument

The name of the index document for the website.

### `RedirectAllRequestsTo` — RedirectAllRequestsTo

The redirect behavior for every request to this bucket's website endpoint.

If you specify this property, you can't specify any other property.

### `RoutingRules` — list<RoutingRule>

Rules that define when a redirect is applied and the redirect behavior.
