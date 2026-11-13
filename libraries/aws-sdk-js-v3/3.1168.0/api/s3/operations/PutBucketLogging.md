# PutBucketLogging

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketLoggingCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?logging`

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025,
the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following Amazon Web Services Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

This operation is not supported for directory buckets.

Set the logging parameters for a bucket and to specify permissions for who can view and modify the
logging parameters. All logs are saved to buckets in the same Amazon Web Services Region as the source bucket. To set
the logging status of a bucket, you must be the bucket owner.

The bucket owner is automatically granted FULL\_CONTROL to all logs. You use the `Grantee`
request element to grant access to other people. The `Permissions` request element specifies
the kind of access the grantee has to the logs.

If the target bucket for log delivery uses the bucket owner enforced setting for S3 Object
Ownership, you can't use the `Grantee` request element to grant access to others.
Permissions can only be granted using policies. For more information, see [Permissions for server access log delivery](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general) in the
*Amazon S3 User Guide*.

Grantee Values
:   You can specify the person (grantee) to whom you're assigning access rights (by using request
    elements) in the following ways. For examples of how to specify these grantee values in JSON
    format, see the Amazon Web Services CLI example in  [Enabling Amazon S3 server
    access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html) in the *Amazon S3 User Guide*.

    - By the person's ID:

      `<>ID<><>GranteesEmail<>`

      `DisplayName` is optional and ignored in the request.
    - By Email address:

      `<>Grantees@email.com<>`

      The grantee is resolved to the `CanonicalUser` and, in a response to a
      `GETObjectAcl` request, appears as the CanonicalUser.
    - By URI:

      `<>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<>`

To enable logging, you use `LoggingEnabled` and its children request elements. To disable
logging, you use an empty `BucketLoggingStatus` request element:

For more information about server access logging, see [Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) in the
*Amazon S3 User Guide*.

For more information about creating a bucket, see [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html). For more information about
returning the logging status of a bucket, see [GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html).

The following operations are related to `PutBucketLogging`:

- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketLoggingRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket for which to set the logging parameters.

### `BucketLoggingStatus` — BucketLoggingStatus · **required** · sent as httpPayload

Container for logging status information.

### `ContentMD5` — string · sent as header `Content-MD5`

The MD5 hash of the `PutBucketLogging` request body.

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

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set logging configuration for a bucket

The following example sets logging policy on a bucket. For the Log Delivery group to deliver logs to the destination bucket, it needs permission for the READ\_ACP action which the policy grants.

Input:

```json
{
  "Bucket": "sourcebucket",
  "BucketLoggingStatus": {
    "LoggingEnabled": {
      "TargetBucket": "targetbucket",
      "TargetPrefix": "MyBucketLogs/",
      "TargetGrants": [
        {
          "Grantee": {
            "Type": "Group",
            "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
          },
          "Permission": "READ"
        }
      ]
    }
  }
}
```
