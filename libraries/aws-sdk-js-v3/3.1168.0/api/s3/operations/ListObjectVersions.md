# ListObjectVersions

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListObjectVersionsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?versions`

This operation is not supported for directory buckets.

Returns metadata about all versions of the objects in a bucket. You can also use request parameters
as selection criteria to return metadata about a subset of all the object versions.

To use this operation, you must have permission to perform the `s3:ListBucketVersions`
action. Be aware of the name difference.

A `200 OK` response can contain valid or invalid XML. Make sure to design your
application to parse the contents of the response and handle it appropriately.

To use this operation, you must have READ access to the bucket.

The following operations are related to `ListObjectVersions`:

- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListObjectVersionsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name that contains the objects.

### `Delimiter` — string · sent as query `delimiter`

A delimiter is a character that you specify to group keys. All keys that contain the same string
between the `prefix` and the first occurrence of the delimiter are grouped under a single
result element in `CommonPrefixes`. These groups are counted as one result against the
`max-keys` limitation. These keys are not returned elsewhere in the response.

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

### `KeyMarker` — string · sent as query `key-marker`

Specifies the key to start with when listing objects in a bucket.

### `MaxKeys` — integer · sent as query `max-keys`

Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000
key names. The response might contain fewer keys but will never contain more. If additional keys satisfy
the search criteria, but were not returned because `max-keys` was exceeded, the response
contains `true`. To return the additional keys, see
`key-marker` and `version-id-marker`.

### `Prefix` — string · sent as query `prefix`

Use this parameter to select only those keys that begin with the specified prefix. You can use
prefixes to separate a bucket into different groupings of keys. (You can think of using
`prefix` to make groups in the same way that you'd use a folder in a file system.) You can
use `prefix` with `delimiter` to roll up numerous objects into a single result
under `CommonPrefixes`.

### `VersionIdMarker` — string · sent as query `version-id-marker`

Specifies the object version you want to start listing from.

### `ExpectedBucketOwner` — string · sent as header `x-amz-expected-bucket-owner`

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### `RequestPayer` — RequestPayer (enum) · sent as header `x-amz-request-payer`

Confirms that the requester knows that they will be charged for the request. Bucket owners need not
specify this parameter in their requests. If either the source or destination S3 bucket has Requester
Pays enabled, the requester will pay for the corresponding charges. For information about
downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

This functionality is not supported for directory buckets.

Values: `requester`

### `OptionalObjectAttributes` — list<OptionalObjectAttributes (enum)> · sent as header `x-amz-optional-object-attributes`

Specifies the optional fields that you want returned in the response. Fields that you do not specify
are not returned.

## Output (`ListObjectVersionsOutput`)

### `IsTruncated` — boolean

A flag that indicates whether Amazon S3 returned all of the results that satisfied the search criteria.
If your results were truncated, you can make a follow-up paginated request by using the
`NextKeyMarker` and `NextVersionIdMarker` response parameters as a starting
place in another request to return the rest of the results.

### `KeyMarker` — string

Marks the last key returned in a truncated response.

### `VersionIdMarker` — string

Marks the last version of the key returned in a truncated response.

### `NextKeyMarker` — string

When the number of responses exceeds the value of `MaxKeys`, `NextKeyMarker`
specifies the first key not returned that satisfies the search criteria. Use this value for the
key-marker request parameter in a subsequent request.

### `NextVersionIdMarker` — string

When the number of responses exceeds the value of `MaxKeys`,
`NextVersionIdMarker` specifies the first object version not returned that satisfies the
search criteria. Use this value for the `version-id-marker` request parameter in a subsequent
request.

### `Versions` — list<ObjectVersion>

Container for version information.

### `DeleteMarkers` — list<DeleteMarkerEntry>

Container for an object that is a delete marker. To learn more about delete markers, see [Working with delete
markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).

### `Name` — string

The bucket name.

### `Prefix` — string

Selects objects that start with the value supplied by this parameter.

### `Delimiter` — string

The delimiter grouping the included keys. A delimiter is a character that you specify to group keys.
All keys that contain the same string between the prefix and the first occurrence of the delimiter are
grouped under a single result element in `CommonPrefixes`. These groups are counted as one
result against the `max-keys` limitation. These keys are not returned elsewhere in the
response.

### `MaxKeys` — integer

Specifies the maximum number of objects to return.

### `CommonPrefixes` — list<CommonPrefix>

All of the keys rolled up into a common prefix count as a single return when calculating the number
of returns.

### `EncodingType` — EncodingType (enum)

Encoding type used by Amazon S3 to encode object key names in the XML response.

If you specify the `encoding-type` request parameter, Amazon S3 includes this element in the
response, and returns encoded key name values in the following response elements:

`KeyMarker, NextKeyMarker, Prefix, Key`, and `Delimiter`.

Values: `url`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### To list object versions

The following example returns versions of an object with specific key name prefix.

Input:

```json
{
  "Bucket": "examplebucket",
  "Prefix": "HappyFace.jpg"
}
```

Output:

```json
{
  "Versions": [
    {
      "LastModified": "2016-12-15T01:19:41.000Z",
      "VersionId": "null",
      "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
      "StorageClass": "STANDARD",
      "Key": "HappyFace.jpg",
      "Owner": {
        "DisplayName": "owner-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "IsLatest": true,
      "Size": 3191
    },
    {
      "LastModified": "2016-12-13T00:58:26.000Z",
      "VersionId": "PHtexPGjH2y.zBgT8LmB7wwLI2mpbz.k",
      "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
      "StorageClass": "STANDARD",
      "Key": "HappyFace.jpg",
      "Owner": {
        "DisplayName": "owner-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "IsLatest": false,
      "Size": 3191
    }
  ]
}
```
