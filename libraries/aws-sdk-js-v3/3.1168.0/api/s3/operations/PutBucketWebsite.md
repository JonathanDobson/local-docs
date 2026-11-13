# PutBucketWebsite

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketWebsiteCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?website`

This operation is not supported for directory buckets.

Sets the configuration of the website that is specified in the `website` subresource. To
configure a bucket as a website, you can add this subresource on the bucket with website configuration
information such as the file name of the index document and any redirect rules. For more information,
see [Hosting Websites on
Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

This PUT action requires the `S3:PutBucketWebsite` permission. By default, only the
bucket owner can configure the website attached to a bucket; however, bucket owners can allow other
users to set the website configuration by writing a bucket policy that grants them the
`S3:PutBucketWebsite` permission.

To redirect all website requests sent to the bucket's website endpoint, you add a website
configuration with the following elements. Because all requests are sent to another website, you don't
need to provide index document name for the bucket.

- `WebsiteConfiguration`
- `RedirectAllRequestsTo`
- `HostName`
- `Protocol`

If you want granular control over redirects, you can use the following elements to add routing rules
that describe conditions for redirecting requests and information about the redirect destination. In
this case, the website configuration must provide an index document for the bucket, because some
requests might not be redirected.

- `WebsiteConfiguration`
- `IndexDocument`
- `Suffix`
- `ErrorDocument`
- `Key`
- `RoutingRules`
- `RoutingRule`
- `Condition`
- `HttpErrorCodeReturnedEquals`
- `KeyPrefixEquals`
- `Redirect`
- `Protocol`
- `HostName`
- `ReplaceKeyPrefixWith`
- `ReplaceKeyWith`
- `HttpRedirectCode`

Amazon S3 has a limitation of 50 routing rules per website configuration. If you require more than 50
routing rules, you can use object redirect. For more information, see [Configuring an Object Redirect](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html) in the
*Amazon S3 User Guide*.

The maximum request length is limited to 128 KB.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketWebsiteRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name.

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

### `WebsiteConfiguration` — WebsiteConfiguration · **required** · sent as httpPayload

Container for the request.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`Unit`)

_None._

## Examples

### Set website configuration on a bucket

The following example adds website configuration to a bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "ContentMD5": "",
  "WebsiteConfiguration": {
    "IndexDocument": {
      "Suffix": "index.html"
    },
    "ErrorDocument": {
      "Key": "error.html"
    }
  }
}
```
