# ListObjects

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListObjectsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}`

This operation is not supported for directory buckets.

Returns some or all (up to 1,000) of the objects in a bucket. You can use the request parameters as
selection criteria to return a subset of the objects in a bucket. A 200 OK response can contain valid or
invalid XML. Be sure to design your application to parse the contents of the response and handle it
appropriately.

This action has been revised. We recommend that you use the newer version, [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html), when
developing applications. For backward compatibility, Amazon S3 continues to support
`ListObjects`.

The following operations are related to `ListObjects`:

- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListObjectsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket containing the objects.

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
the key-marker.

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

### `Marker` — string · sent as query `marker`

Marker is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified
key. Marker can be any key in the bucket.

### `MaxKeys` — integer · sent as query `max-keys`

Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000
key names. The response might contain fewer keys but will never contain more.

### `Prefix` — string · sent as query `prefix`

Limits the response to keys that begin with the specified prefix.

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that she or he will be charged for the list objects request.
Bucket owners need not specify this parameter in their requests.

Values: `requester`

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `OptionalObjectAttributes` — list<OptionalObjectAttributes (enum)> · sent as header `x-amz-optional-object-attributes`

Specifies the optional fields that you want returned in the response. Fields that you do not specify
are not returned.

## Output (`ListObjectsOutput`)

### `IsTruncated` — boolean

A flag that indicates whether Amazon S3 returned all of the results that satisfied the search
criteria.

### `Marker` — string

Indicates where in the bucket listing begins. Marker is included in the response if it was sent with
the request.

### `NextMarker` — string

When the response is truncated (the `IsTruncated` element value in the response is
`true`), you can use the key name in this field as the `marker` parameter in the
subsequent request to get the next set of objects. Amazon S3 lists objects in alphabetical order.

This element is returned only if you have the `delimiter` request parameter specified.
If the response does not include the `NextMarker` element and it is truncated, you can use
the value of the last `Key` element in the response as the `marker` parameter in
the subsequent request to get the next set of object keys.

### `Contents` — list<Object>

Metadata about each object returned.

### `Name` — string

The bucket name.

### `Prefix` — string

Keys that begin with the indicated prefix.

### `Delimiter` — string

Causes keys that contain the same string between the prefix and the first occurrence of the
delimiter to be rolled up into a single result element in the `CommonPrefixes` collection.
These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts as only
one return against the `MaxKeys` value.

### `MaxKeys` — integer

The maximum number of keys returned in the response body.

### `CommonPrefixes` — list<CommonPrefix>

All of the keys (up to 1,000) rolled up in a common prefix count as a single return when calculating
the number of returns.

A response can contain `CommonPrefixes` only if you specify a delimiter.

`CommonPrefixes` contains all (if there are any) keys between `Prefix` and the
next occurrence of the string specified by the delimiter.

`CommonPrefixes` lists keys that act like subdirectories in the directory specified by
`Prefix`.

For example, if the prefix is `notes/` and the delimiter is a slash (`/`), as
in `notes/summer/july`, the common prefix is `notes/summer/`. All of the keys that
roll up into a common prefix count as a single return when calculating the number of returns.

### `EncodingType` — EncodingType (enum)

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

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `NoSuchBucket` — The specified bucket does not exist.

## Examples

### To list objects in a bucket

The following example list two objects in a bucket.

Input:

```json
{
  "Bucket": "examplebucket",
  "MaxKeys": 2
}
```

Output:

```json
{
  "NextMarker": "eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==",
  "Contents": [
    {
      "LastModified": "2014-11-21T19:40:05.000Z",
      "ETag": "\"70ee1738b6b21e2c8a43f3a5ab0eee71\"",
      "StorageClass": "STANDARD",
      "Key": "example1.jpg",
      "Owner": {
        "DisplayName": "myname",
        "ID": "12345example25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Size": 11
    },
    {
      "LastModified": "2013-11-15T01:10:49.000Z",
      "ETag": "\"9c8af9a76df052144598c115ef33e511\"",
      "StorageClass": "STANDARD",
      "Key": "example2.jpg",
      "Owner": {
        "DisplayName": "myname",
        "ID": "12345example25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Size": 713193
    }
  ]
}
```
