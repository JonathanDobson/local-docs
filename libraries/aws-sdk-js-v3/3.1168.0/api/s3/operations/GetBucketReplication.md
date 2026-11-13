# GetBucketReplication

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetBucketReplicationCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?replication`

This operation is not supported for directory buckets.

Returns the replication configuration of a bucket.

It can take a while to propagate the put or delete a replication configuration to all Amazon S3
systems. Therefore, a get request soon after put or delete can return a wrong result.

For information about replication configuration, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the
*Amazon S3 User Guide*.

This action requires permissions for the `s3:GetReplicationConfiguration` action. For
more information about permissions, see [Using Bucket Policies and User
Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).

If you include the `Filter` element in a replication configuration, you must also include
the `DeleteMarkerReplication` and `Priority` elements. The response also returns
those elements.

For information about `GetBucketReplication` errors, see [List of replication-related
error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ReplicationErrorCodeList)

The following operations are related to `GetBucketReplication`:

- [PutBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html)
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetBucketReplicationRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name for which to get the replication information.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetBucketReplicationOutput`)

### `ReplicationConfiguration` — ReplicationConfiguration · sent as httpPayload

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication
configuration is 2 MB.

## Examples

### To get replication configuration set on a bucket

The following example returns replication configuration set on a bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "ReplicationConfiguration": {
    "Rules": [
      {
        "Status": "Enabled",
        "Prefix": "Tax",
        "Destination": {
          "Bucket": "arn:aws:s3:::destination-bucket"
        },
        "ID": "MWIwNTkwZmItMTE3MS00ZTc3LWJkZDEtNzRmODQwYzc1OTQy"
      }
    ],
    "Role": "arn:aws:iam::acct-id:role/example-role"
  }
}
```
