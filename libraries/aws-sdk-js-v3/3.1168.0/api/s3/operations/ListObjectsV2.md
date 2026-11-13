# ListObjectsV2

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListObjectsV2Command` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?list-type=2` · Paginated (token `ContinuationToken` → `NextContinuationToken`)

Returns some or all (up to 1,000) of the objects in a bucket with each request. You can use the
request parameters as selection criteria to return a subset of the objects in a bucket. A `200
OK` response can contain valid or invalid XML. Make sure to design your application to parse the
contents of the response and handle it appropriately. For more information about listing objects, see
[Listing object
keys programmatically](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html) in the *Amazon S3 User Guide*. To get a list of your
buckets, see [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html).

- **General purpose bucket** - For general purpose buckets,
  `ListObjectsV2` doesn't return prefixes that are related only to in-progress
  multipart uploads.
- **Directory buckets** - For directory buckets,
  `ListObjectsV2` response includes the prefixes that are related only to in-progress
  multipart uploads.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
  *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
  *Amazon S3 User Guide*.

Permissions
:   - **General purpose bucket permissions** - To use this
      operation, you must have READ access to the bucket. You must have permission to perform the
      `s3:ListBucket` action. The bucket owner has this permission by default and can
      grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access
      Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the
      *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

Sorting order of returned objects
:   - **General purpose bucket** - For general purpose buckets,
      `ListObjectsV2` returns objects in lexicographical order based on their key
      names.
    - **Directory bucket** - For directory buckets,
      `ListObjectsV2` does not return objects in lexicographical order.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

This section describes the latest revision of this action. We recommend that you use this revised
API operation for application development. For backward compatibility, Amazon S3 continues to support the
prior version of this API operation, [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html).

The following operations are related to `ListObjectsV2`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListObjectsV2Request`)

### `Bucket` — string · **required** · sent as httpLabel

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Delimiter` — string · sent as query `delimiter`

A delimiter is a character that you use to group keys.

`CommonPrefixes` is filtered out from results if it is not lexicographically greater than
the `StartAfter` value.

- **Directory buckets** - For directory buckets, `/` is the only supported delimiter.
- **Directory buckets**  - When you query
  `ListObjectsV2` with a delimiter during in-progress multipart uploads, the
  `CommonPrefixes` response parameter contains the prefixes that are associated with
  the in-progress multipart uploads. For more information about multipart uploads, see [Multipart Upload
  Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) in the *Amazon S3 User Guide*.

### `EncodingType` — EncodingType (enum) · sent as query `encoding-type`

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

### `MaxKeys` — integer · sent as query `max-keys`

Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000
key names. The response might contain fewer keys but will never contain more.

### `Prefix` — string · sent as query `prefix`

Limits the response to keys that begin with the specified prefix.

**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.

### `ContinuationToken` — string · sent as query `continuation-token`

`ContinuationToken` indicates to Amazon S3 that the list is being continued on this bucket
with a token. `ContinuationToken` is obfuscated and is not a real key. You can use this
`ContinuationToken` for pagination of the list results.

### `FetchOwner` — boolean · sent as query `fetch-owner`

The owner field is not present in `ListObjectsV2` by default. If you want to return the
owner field with each key in the result, then set the `FetchOwner` field to
`true`.

**Directory buckets** - For directory buckets, the bucket
owner is returned as the object owner for all objects.

### `StartAfter` — string · sent as query `start-after`

StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified
key. StartAfter can be any key in the bucket.

This functionality is not supported for directory buckets.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that she or he will be charged for the list objects request in V2
style. Bucket owners need not specify this parameter in their requests.

This functionality is not supported for directory buckets.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `OptionalObjectAttributes` — list<OptionalObjectAttributes (enum)> · sent as header `x-amz-optional-object-attributes`

Specifies the optional fields that you want returned in the response. Fields that you do not specify
are not returned.

This functionality is not supported for directory buckets.

## Output (`ListObjectsV2Output`)

### `IsTruncated` — boolean

Set to `false` if all of the results were returned. Set to `true` if more keys
are available to return. If the number of results exceeds that specified by `MaxKeys`, all of
the results might not be returned.

### `Contents` — list<Object>

Metadata about each object returned.

### `Name` — string

The bucket name.

### `Prefix` — string

Keys that begin with the indicated prefix.

**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.

### `Delimiter` — string

Causes keys that contain the same string between the `prefix` and the first occurrence of
the delimiter to be rolled up into a single result element in the `CommonPrefixes`
collection. These rolled-up keys are not returned elsewhere in the response. Each rolled-up result
counts as only one return against the `MaxKeys` value.

**Directory buckets** - For directory buckets, `/` is the only supported delimiter.

### `MaxKeys` — integer

Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000
key names. The response might contain fewer keys but will never contain more.

### `CommonPrefixes` — list<CommonPrefix>

All of the keys (up to 1,000) that share the same prefix are grouped together. When counting the
total numbers of returns by this API operation, this group of keys is considered as one item.

A response can contain `CommonPrefixes` only if you specify a delimiter.

`CommonPrefixes` contains all (if there are any) keys between `Prefix` and the
next occurrence of the string specified by a delimiter.

`CommonPrefixes` lists keys that act like subdirectories in the directory specified by
`Prefix`.

For example, if the prefix is `notes/` and the delimiter is a slash (`/`) as
in `notes/summer/july`, the common prefix is `notes/summer/`. All of the keys that
roll up into a common prefix count as a single return when calculating the number of returns.

- **Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.
- **Directory buckets**  - When you query
  `ListObjectsV2` with a delimiter during in-progress multipart uploads, the
  `CommonPrefixes` response parameter contains the prefixes that are associated with
  the in-progress multipart uploads. For more information about multipart uploads, see [Multipart Upload
  Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) in the *Amazon S3 User Guide*.

### `EncodingType` — EncodingType (enum)

Encoding type used by Amazon S3 to encode object key names in the XML response.

If you specify the `encoding-type` request parameter, Amazon S3 includes this element in the
response, and returns encoded key name values in the following response elements:

`Delimiter, Prefix, Key,` and `StartAfter`.

Values: `url`

### `KeyCount` — integer

`KeyCount` is the number of keys returned with this request. `KeyCount` will
always be less than or equal to the `MaxKeys` field. For example, if you ask for 50 keys,
your result will include 50 keys or fewer.

### `ContinuationToken` — string

If `ContinuationToken` was sent with the request, it is included in the response. You
can use the returned `ContinuationToken` for pagination of the list response.

### `NextContinuationToken` — string

`NextContinuationToken` is sent when `isTruncated` is true, which means there
are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with
this `NextContinuationToken`. `NextContinuationToken` is obfuscated and is not a
real key

### `StartAfter` — string

If StartAfter was sent with the request, it is included in the response.

This functionality is not supported for directory buckets.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `NoSuchBucket` — The specified bucket does not exist.

## Examples

### To get object list

The following example retrieves object list. The request specifies max keys to limit response to include only 2 object keys.

Input:

```json
{
  "Bucket": "DOC-EXAMPLE-BUCKET",
  "MaxKeys": 2
}
```

Output:

```json
{
  "Name": "DOC-EXAMPLE-BUCKET",
  "MaxKeys": 2,
  "Prefix": "",
  "KeyCount": 2,
  "NextContinuationToken": "1w41l63U0xa8q7smH50vCxyTQqdxo69O3EmK28Bi5PcROI4wI/EyIJg==",
  "IsTruncated": true,
  "Contents": [
    {
      "LastModified": "2014-11-21T19:40:05.000Z",
      "ETag": "\"70ee1738b6b21e2c8a43f3a5ab0eee71\"",
      "StorageClass": "STANDARD",
      "Key": "happyface.jpg",
      "Size": 11
    },
    {
      "LastModified": "2014-05-02T04:51:50.000Z",
      "ETag": "\"becf17f89c30367a9a44495d62ed521a-1\"",
      "StorageClass": "STANDARD",
      "Key": "test.jpg",
      "Size": 4192256
    }
  ]
}
```
