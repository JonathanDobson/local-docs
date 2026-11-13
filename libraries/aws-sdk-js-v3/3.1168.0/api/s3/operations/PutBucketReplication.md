# PutBucketReplication

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketReplicationCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?replication`

This operation is not supported for directory buckets.

Creates a replication configuration or replaces an existing one. For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the
*Amazon S3 User Guide*.

Specify the replication configuration in the request body. In the replication configuration, you
provide the name of the destination bucket or buckets where you want Amazon S3 to replicate objects, the
IAM role that Amazon S3 can assume to replicate objects on your behalf, and other relevant information. You
can invoke this request for a specific Amazon Web Services Region by using the [`aws:RequestedRegion`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion) condition key.

A replication configuration must include at least one rule, and can contain a maximum of 1,000. Each
rule identifies a subset of objects to replicate by filtering the objects in the source bucket. To
choose additional subsets of objects to replicate, add a rule for each subset.

To specify a subset of the objects in the source bucket to apply a replication rule to, add the
Filter element as a child of the Rule element. You can filter objects based on an object key prefix, one
or more object tags, or both. When you add the Filter element in the configuration, you must also add
the following elements: `DeleteMarkerReplication`, `Status`, and
`Priority`.

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of
delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations).

For information about enabling versioning on a bucket, see [Using Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html).

Handling Replication of Encrypted Objects
:   By default, Amazon S3 doesn't replicate objects that are stored at rest using server-side
    encryption with KMS keys. To replicate Amazon Web Services KMS-encrypted objects, add the following:
    `SourceSelectionCriteria`, `SseKmsEncryptedObjects`, `Status`,
    `EncryptionConfiguration`, and `ReplicaKmsKeyID`. For information about
    replication configuration, see [Replicating Objects Created
    with SSE Using KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html).

    For information on `PutBucketReplication` errors, see [List of
    replication-related error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ReplicationErrorCodeList)

Permissions
:   To create a `PutBucketReplication` request, you must have
    `s3:PutReplicationConfiguration` permissions for the bucket.

    By default, a resource owner, in this case the Amazon Web Services account that created the bucket, can
    perform this operation. The resource owner can also grant others permissions to perform the
    operation. For more information about permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html)
    and [Managing
    Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

    To perform this operation, the user or role performing the action must have the [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) permission.

The following operations are related to `PutBucketReplication`:

- [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html)
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketReplicationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
message integrity check to verify that the request body was not corrupted in transit. For more
information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt).

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

### `ReplicationConfiguration` — ReplicationConfiguration · **required** · sent as httpPayload

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication
configuration is 2 MB.

### `Token` — string · sent as header `x-amz-bucket-object-lock-token`

A token to allow Object Lock to be enabled for an existing bucket.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set replication configuration on a bucket

The following example sets replication configuration on a bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "ReplicationConfiguration": {
    "Role": "arn:aws:iam::123456789012:role/examplerole",
    "Rules": [
      {
        "Prefix": "",
        "Status": "Enabled",
        "Destination": {
          "Bucket": "arn:aws:s3:::destinationbucket",
          "StorageClass": "STANDARD"
        }
      }
    ]
  }
}
```
