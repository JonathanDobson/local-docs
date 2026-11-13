# PutBucketCors

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `PutBucketCorsCommand` from `@aws-sdk/client-s3` · HTTP: `PUT /{Bucket}?cors`

This operation is not supported for directory buckets.

Sets the `cors` configuration for your bucket. If the configuration exists, Amazon S3 replaces
it.

To use this operation, you must be allowed to perform the `s3:PutBucketCORS` action. By
default, the bucket owner has this permission and can grant it to others.

You set this configuration on a bucket so that the bucket can service cross-origin requests. For
example, you might want to enable a request whose origin is `http://www.example.com` to
access your Amazon S3 bucket at `my.example.bucket.com` by using the browser's
`XMLHttpRequest` capability.

To enable cross-origin resource sharing (CORS) on a bucket, you add the `cors`
subresource to the bucket. The `cors` subresource is an XML document in which you configure
rules that identify origins and the HTTP methods that can be executed on your bucket. The document is
limited to 64 KB in size.

When Amazon S3 receives a cross-origin request (or a pre-flight OPTIONS request) against a bucket, it
evaluates the `cors` configuration on the bucket and uses the first `CORSRule`
rule that matches the incoming browser request to enable a cross-origin request. For a rule to match,
the following conditions must be met:

- The request's `Origin` header must match `AllowedOrigin` elements.
- The request method (for example, GET, PUT, HEAD, and so on) or the
  `Access-Control-Request-Method` header in case of a pre-flight `OPTIONS`
  request must be one of the `AllowedMethod` elements.
- Every header specified in the `Access-Control-Request-Headers` request header of a
  pre-flight request must match an `AllowedHeader` element.

For more information about CORS, go to [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the
*Amazon S3 User Guide*.

The following operations are related to `PutBucketCors`:

- [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)
- [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html)
- [RESTOPTIONSobject](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTOPTIONSobject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`PutBucketCorsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

Specifies the bucket impacted by the `cors`configuration.

### `CORSConfiguration` — CORSConfiguration · **required** · sent as httpPayload

Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information,
see [Enabling Cross-Origin Resource
Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the *Amazon S3 User Guide*.

### `ContentMD5` — string · sent as header `Content-MD5`

The Base64 encoded 128-bit `MD5` digest of the data. This header must be used as a
message integrity check to verify that the request body was not corrupted in transit. For more
information, go to [RFC 1864.](http://www.ietf.org/rfc/rfc1864.txt)

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

### To set cors configuration on a bucket.

The following example enables PUT, POST, and DELETE requests from www.example.com, and enables GET requests from any domain.

Input:

```json
{
  "Bucket": "",
  "CORSConfiguration": {
    "CORSRules": [
      {
        "AllowedOrigins": [
          "http://www.example.com"
        ],
        "AllowedHeaders": [
          "*"
        ],
        "AllowedMethods": [
          "PUT",
          "POST",
          "DELETE"
        ],
        "MaxAgeSeconds": 3000,
        "ExposeHeaders": [
          "x-amz-server-side-encryption"
        ]
      },
      {
        "AllowedOrigins": [
          "*"
        ],
        "AllowedHeaders": [
          "Authorization"
        ],
        "AllowedMethods": [
          "GET"
        ],
        "MaxAgeSeconds": 3000
      }
    ]
  },
  "ContentMD5": ""
}
```
