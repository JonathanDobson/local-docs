# SelectObjectContent

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `SelectObjectContentCommand` from `@aws-sdk/client-s3` · HTTP: `POST /{Bucket}/{Key+}?select&select-type=2`

This operation is not supported for directory buckets.

This action filters the contents of an Amazon S3 object based on a simple structured query language (SQL)
statement. In the request, along with the SQL expression, you must also specify a data serialization
format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format to parse object data into
records, and returns only records that match the specified SQL expression. You must also specify the
data serialization format for the response.

This functionality is not supported for Amazon S3 on Outposts.

For more information about Amazon S3 Select, see [Selecting Content from Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html)
and [SELECT Command](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-glacier-select-sql-reference-select.html) in
the *Amazon S3 User Guide*.

Permissions
:   You must have the `s3:GetObject` permission for this operation. Amazon S3 Select does
    not support anonymous access. For more information about permissions, see [Specifying Permissions
    in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) in the *Amazon S3 User Guide*.

Object Data Formats
:   You can use Amazon S3 Select to query objects that have the following format properties:

    - *CSV, JSON, and Parquet* - Objects must be in CSV, JSON, or Parquet
      format.
    - *UTF-8* - UTF-8 is the only encoding type Amazon S3 Select supports.
    - *GZIP or BZIP2* - CSV and JSON files can be compressed using GZIP or
      BZIP2. GZIP and BZIP2 are the only compression formats that Amazon S3 Select supports for CSV and
      JSON files. Amazon S3 Select supports columnar compression for Parquet using GZIP or Snappy. Amazon S3
      Select does not support whole-object compression for Parquet objects.
    - *Server-side encryption* - Amazon S3 Select supports querying objects that
      are protected with server-side encryption.

      For objects that are encrypted with customer-provided encryption keys (SSE-C), you must
      use HTTPS, and you must use the headers that are documented in the [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html). For more information about
      SSE-C, see [Server-Side Encryption
      (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
      *Amazon S3 User Guide*.

      For objects that are encrypted with Amazon S3 managed keys (SSE-S3) and Amazon Web Services KMS keys
      (SSE-KMS), server-side encryption is handled transparently, so you don't need to specify
      anything. For more information about server-side encryption, including SSE-S3 and SSE-KMS, see
      [Protecting
      Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the
      *Amazon S3 User Guide*.

Working with the Response Body
:   Given the response size is unknown, Amazon S3 Select streams the response as a series of messages
    and includes a `Transfer-Encoding` header with `chunked` as its value in the
    response. For more information, see [Appendix: SelectObjectContent
    Response](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTSelectObjectAppendix.html).

GetObject Support
:   The `SelectObjectContent` action does not support the following
    `GetObject` functionality. For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

    - `Range`: Although you can specify a scan range for an Amazon S3 Select request (see
      [SelectObjectContentRequest - ScanRange](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html#AmazonS3-SelectObjectContent-request-ScanRange) in the request parameters), you
      cannot specify the range of bytes of an object to return.
    - The `GLACIER`, `DEEP_ARCHIVE`, and `REDUCED_REDUNDANCY`
      storage classes, or the `ARCHIVE_ACCESS` and `DEEP_ARCHIVE_ACCESS`
      access tiers of the `INTELLIGENT_TIERING` storage class: You cannot query objects
      in the `GLACIER`, `DEEP_ARCHIVE`, or `REDUCED_REDUNDANCY`
      storage classes, nor objects in the `ARCHIVE_ACCESS` or
      `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING`
      storage class. For more information about storage classes, see [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
      in the *Amazon S3 User Guide*.

Special Errors
:   For a list of special errors for this operation, see [List of SELECT
    Object Content Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#SelectObjectContentErrorCodeList)

The following operations are related to `SelectObjectContent`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`SelectObjectContentRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The S3 bucket.

### `Key` — string · **required** · sent as httpLabel

The object key.

### `SSECustomerAlgorithm` — string · sent as header `x-amz-server-side-encryption-customer-algorithm`

The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created
using a checksum algorithm. For more information,
see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

### `SSECustomerKey` — string · sent as header `x-amz-server-side-encryption-customer-key`

The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm.
For more information, see
[Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

### `SSECustomerKeyMD5` — string · sent as header `x-amz-server-side-encryption-customer-key-MD5`

The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum
algorithm. For more information,
see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the
*Amazon S3 User Guide*.

### `Expression` — string · **required**

The expression that is used to query the object.

### `ExpressionType` — ExpressionType (enum) · **required**

The type of the provided expression (for example, SQL).

Values: `SQL`

### `RequestProgress` — RequestProgress

Specifies if periodic request progress information should be enabled.

### `InputSerialization` — InputSerialization · **required**

Describes the format of the data in the object that is being queried.

### `OutputSerialization` — OutputSerialization · **required**

Describes the format of the data that you want Amazon S3 to return in response.

### `ScanRange` — ScanRange

Specifies the byte range of the object to get the records from. A record is processed when its first
byte is contained by the range. This parameter is optional, but when specified, it must not be empty.
See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

`ScanRange`may be used in the following ways:

- `50100`
  - process only the records starting between the bytes 50 and 100 (inclusive, counting from
  zero)
- `50` - process only the
  records starting after the byte 50
- `50` - process only the
  records within the last 50 bytes of the file.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Output (`SelectObjectContentOutput`)

### `Payload` — SelectObjectContentEventStream · sent as httpPayload

The array of results.
