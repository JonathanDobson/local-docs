# ListMultipartUploads

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListMultipartUploadsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}?uploads`

This operation lists in-progress multipart uploads in a bucket. An in-progress multipart upload is a
multipart upload that has been initiated by the `CreateMultipartUpload` request, but has not
yet been completed or aborted.

**Directory buckets** - If multipart uploads in a
directory bucket are in progress, you can't delete the bucket until all the in-progress multipart
uploads are aborted or completed. To delete these in-progress multipart uploads, use the
`ListMultipartUploads` operation to list the in-progress multipart uploads in the bucket
and use the `AbortMultipartUpload` operation to abort all the in-progress multipart
uploads.

The `ListMultipartUploads` operation returns a maximum of 1,000 multipart uploads in the
response. The limit of 1,000 multipart uploads is also the default value. You can further limit the
number of uploads in a response by specifying the `max-uploads` request parameter. If there
are more than 1,000 multipart uploads that satisfy your `ListMultipartUploads` request, the
response returns an `IsTruncated` element with the value of `true`, a
`NextKeyMarker` element, and a `NextUploadIdMarker` element. To list the
remaining multipart uploads, you need to make subsequent `ListMultipartUploads` requests. In
these requests, include two query parameters: `key-marker` and `upload-id-marker`.
Set the value of `key-marker` to the `NextKeyMarker` value from the previous
response. Similarly, set the value of `upload-id-marker` to the
`NextUploadIdMarker` value from the previous response.

**Directory buckets** - The `upload-id-marker`
element and the `NextUploadIdMarker` element aren't supported by directory buckets. To
list the additional multipart uploads, you only need to set the value of `key-marker` to
the `NextKeyMarker` value from the previous response.

For more information about multipart uploads, see [Uploading Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) in
the *Amazon S3 User Guide*.

**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://amzn-s3-demo-bucket.s3express-zone-id.region-code.amazonaws.com/key-name`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the
*Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the
*Amazon S3 User Guide*.

Permissions
:   - **General purpose bucket permissions** - For information
      about permissions required to use the multipart upload API, see [Multipart Upload and Permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html) in
      the *Amazon S3 User Guide*.
    - **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html) API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use.
      Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html).

Sorting of multipart uploads in response
:   - **General purpose bucket** - In the
      `ListMultipartUploads` response, the multipart uploads are sorted based on two
      criteria:

      - Key-based sorting - Multipart uploads are initially sorted in ascending order
        based on their object keys.
      - Time-based sorting - For uploads that share the same object key, they are
        further sorted in ascending order based on the upload initiation time. Among uploads with
        the same key, the one that was initiated first will appear before the ones that were
        initiated later.
    - **Directory bucket** - In the
      `ListMultipartUploads` response, the multipart uploads aren't sorted
      lexicographically based on the object keys.

HTTP Host header syntax
:   **Directory buckets**  - The HTTP Host header syntax is `Bucket-name.s3express-zone-id.region-code.amazonaws.com`.

The following operations are related to `ListMultipartUploads`:

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListMultipartUploadsRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The name of the bucket to which the multipart upload was initiated.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `bucket-base-name--zone-id--x-s3` (for example, `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming
restrictions, see [Directory bucket naming
rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the
form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

### `Delimiter` — string · sent as query `delimiter`

Character you use to group keys.

All keys that contain the same string between the prefix, if specified, and the first occurrence of
the delimiter after the prefix are grouped under a single result element, `CommonPrefixes`.
If you don't specify the prefix parameter, then the substring starts at the beginning of the key. The
keys that are grouped under `CommonPrefixes` result element are not returned elsewhere in the
response.

`CommonPrefixes` is filtered out from results if it is not lexicographically greater than
the key-marker.

**Directory buckets** - For directory buckets, `/` is the only supported delimiter.

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

Specifies the multipart upload after which listing should begin.

- **General purpose buckets** - For general purpose buckets,
  `key-marker` is an object key. Together with `upload-id-marker`, this
  parameter specifies the multipart upload after which listing should begin.

  If `upload-id-marker` is not specified, only the keys lexicographically greater
  than the specified `key-marker` will be included in the list.

  If `upload-id-marker` is specified, any multipart uploads for a key equal to the
  `key-marker` might also be included, provided those multipart uploads have upload IDs
  lexicographically greater than the specified `upload-id-marker`.
- **Directory buckets** - For directory buckets,
  `key-marker` is obfuscated and isn't a real object key. The
  `upload-id-marker` parameter isn't supported by directory buckets. To list the
  additional multipart uploads, you only need to set the value of `key-marker` to the
  `NextKeyMarker` value from the previous response.

  In the `ListMultipartUploads` response, the multipart uploads aren't sorted
  lexicographically based on the object keys.

### `MaxUploads` — integer · sent as query `max-uploads`

Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000
is the maximum number of uploads that can be returned in a response.

### `Prefix` — string · sent as query `prefix`

Lists in-progress uploads only for those keys that begin with the specified prefix. You can use
prefixes to separate a bucket into different grouping of keys. (You can think of using
`prefix` to make groups in the same way that you'd use a folder in a file system.)

**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.

### `UploadIdMarker` — string · sent as query `upload-id-marker`

Together with key-marker, specifies the multipart upload after which listing should begin. If
key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads
for a key equal to the key-marker might be included in the list only if they have an upload ID
lexicographically greater than the specified `upload-id-marker`.

This functionality is not supported for directory buckets.

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

## Output (`ListMultipartUploadsOutput`)

### `Bucket` — string

The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or
access point alias if used.

### `KeyMarker` — string

The key at or after which the listing began.

### `UploadIdMarker` — string

Together with key-marker, specifies the multipart upload after which listing should begin. If
key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads
for a key equal to the key-marker might be included in the list only if they have an upload ID
lexicographically greater than the specified `upload-id-marker`.

This functionality is not supported for directory buckets.

### `NextKeyMarker` — string

When a list is truncated, this element specifies the value that should be used for the key-marker
request parameter in a subsequent request.

### `Prefix` — string

When a prefix is provided in the request, this field contains the specified prefix. The result
contains only keys starting with the specified prefix.

**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.

### `Delimiter` — string

Contains the delimiter you specified in the request. If you don't specify a delimiter in your
request, this element is absent from the response.

**Directory buckets** - For directory buckets, `/` is the only supported delimiter.

### `NextUploadIdMarker` — string

When a list is truncated, this element specifies the value that should be used for the
`upload-id-marker` request parameter in a subsequent request.

This functionality is not supported for directory buckets.

### `MaxUploads` — integer

Maximum number of multipart uploads that could have been included in the response.

### `IsTruncated` — boolean

Indicates whether the returned list of multipart uploads is truncated. A value of true indicates
that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the
limit allowed or specified by max uploads.

### `Uploads` — list<MultipartUpload>

Container for elements related to a particular multipart upload. A response can contain zero or more
`Upload` elements.

### `CommonPrefixes` — list<CommonPrefix>

If you specify a delimiter in the request, then the result returns each distinct key prefix
containing the delimiter in a `CommonPrefixes` element. The distinct key prefixes are
returned in the `Prefix` child element.

**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.

### `EncodingType` — EncodingType (enum)

Encoding type used by Amazon S3 to encode object keys in the response.

If you specify the `encoding-type` request parameter, Amazon S3 includes this element in the
response, and returns encoded key name values in the following response elements:

`Delimiter`, `KeyMarker`, `Prefix`, `NextKeyMarker`,
`Key`.

Values: `url`

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Examples

### List next set of multipart uploads when previous result is truncated

The following example specifies the upload-id-marker and key-marker from previous truncated response to retrieve next setup of multipart uploads.

Input:

```json
{
  "Bucket": "examplebucket",
  "KeyMarker": "nextkeyfrompreviousresponse",
  "MaxUploads": 2,
  "UploadIdMarker": "valuefrompreviousresponse"
}
```

Output:

```json
{
  "UploadIdMarker": "",
  "NextKeyMarker": "someobjectkey",
  "Bucket": "acl1",
  "NextUploadIdMarker": "examplelo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--",
  "Uploads": [
    {
      "Initiator": {
        "DisplayName": "ownder-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Initiated": "2014-05-01T05:40:58.000Z",
      "UploadId": "gZ30jIqlUa.CInXklLQtSMJITdUnoZ1Y5GACB5UckOtspm5zbDMCkPF_qkfZzMiFZ6dksmcnqxJyIBvQMG9X9Q--",
      "StorageClass": "STANDARD",
      "Key": "JavaFile",
      "Owner": {
        "DisplayName": "mohanataws",
        "ID": "852b113e7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      }
    },
    {
      "Initiator": {
        "DisplayName": "ownder-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Initiated": "2014-05-01T05:41:27.000Z",
      "UploadId": "b7tZSqIlo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--",
      "StorageClass": "STANDARD",
      "Key": "JavaFile",
      "Owner": {
        "DisplayName": "ownder-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      }
    }
  ],
  "KeyMarker": "",
  "MaxUploads": 2,
  "IsTruncated": true
}
```

### To list in-progress multipart uploads on a bucket

The following example lists in-progress multipart uploads on a specific bucket.

Input:

```json
{
  "Bucket": "examplebucket"
}
```

Output:

```json
{
  "Uploads": [
    {
      "Initiator": {
        "DisplayName": "display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Initiated": "2014-05-01T05:40:58.000Z",
      "UploadId": "examplelUa.CInXklLQtSMJITdUnoZ1Y5GACB5UckOtspm5zbDMCkPF_qkfZzMiFZ6dksmcnqxJyIBvQMG9X9Q--",
      "StorageClass": "STANDARD",
      "Key": "JavaFile",
      "Owner": {
        "DisplayName": "display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      }
    },
    {
      "Initiator": {
        "DisplayName": "display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Initiated": "2014-05-01T05:41:27.000Z",
      "UploadId": "examplelo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--",
      "StorageClass": "STANDARD",
      "Key": "JavaFile",
      "Owner": {
        "DisplayName": "display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      }
    }
  ]
}
```
