# GetObjectTorrent

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetObjectTorrentCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?torrent`

This operation is not supported for directory buckets.

Returns torrent files from a bucket. BitTorrent can save you bandwidth when you're distributing
large files.

You can get torrent only for objects that are less than 5 GB in size, and that are not encrypted
using server-side encryption with a customer-provided encryption key.

To use GET, you must have READ access to the object.

This functionality is not supported for Amazon S3 on Outposts.

The following action is related to `GetObjectTorrent`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetObjectTorrentRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket containing the object for which to get the torrent files.

### `Key` — string · **required** · sent as httpLabel

The object key for which to get the information.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`GetObjectTorrentOutput`)

### `Body` — blob · sent as httpPayload · default `""`

A Bencoded dictionary as defined by the BitTorrent specification

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### To retrieve torrent files for an object

The following example retrieves torrent files of an object.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg"
}
```
