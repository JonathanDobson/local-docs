# ListBuckets

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `ListBucketsCommand` from `@aws-sdk/client-s3` · HTTP: `GET /?x-id=ListBuckets` · Paginated (token `ContinuationToken` → `ContinuationToken`)

This operation is not supported for directory buckets.

Returns a list of all buckets owned by the authenticated sender of the request. To grant IAM
permission to use this operation, you must add the `s3:ListAllMyBuckets` policy action.

For information about Amazon S3 buckets, see [Creating, configuring, and working with Amazon S3
buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html).

We strongly recommend using only paginated `ListBuckets` requests. Unpaginated
`ListBuckets` requests are only supported for Amazon Web Services accounts set to the default general
purpose bucket quota of 10,000. If you have an approved general purpose bucket quota above 10,000, you
must send paginated `ListBuckets` requests to list your account’s buckets. All unpaginated
`ListBuckets` requests will be rejected for Amazon Web Services accounts with a general purpose bucket
quota greater than 10,000.

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`ListBucketsRequest`)

### `MaxBuckets` — integer · sent as query `max-buckets`

Maximum number of buckets to be returned in response. When the number is more than the count of
buckets that are owned by an Amazon Web Services account, return all the buckets in response.

### `ContinuationToken` — string · sent as query `continuation-token`

`ContinuationToken` indicates to Amazon S3 that the list is being continued on this bucket
with a token. `ContinuationToken` is obfuscated and is not a real key. You can use this
`ContinuationToken` for pagination of the list results.

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No.

If you specify the `bucket-region`, `prefix`, or
`continuation-token` query parameters without using `max-buckets` to set the
maximum number of buckets returned in the response, Amazon S3 applies a default page size of 10,000 and
provides a continuation token if there are more buckets.

### `Prefix` — string · sent as query `prefix`

Limits the response to bucket names that begin with the specified bucket name prefix.

### `BucketRegion` — string · sent as query `bucket-region`

Limits the response to buckets that are located in the specified Amazon Web Services Region. The Amazon Web Services Region must
be expressed according to the Amazon Web Services Region code, such as `us-west-2` for the US West (Oregon)
Region. For a list of the valid values for all of the Amazon Web Services Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

Requests made to a Regional endpoint that is different from the `bucket-region`
parameter are not supported. For example, if you want to limit the response to your buckets in Region
`us-west-2`, the request must be made to an endpoint in Region
`us-west-2`.

## Output (`ListBucketsOutput`)

### `Buckets` — list<Bucket>

The list of buckets owned by the requester.

### `Owner` — Owner

The owner of the buckets listed.

### `ContinuationToken` — string

`ContinuationToken` is included in the response when there are more buckets that can be
listed with pagination. The next `ListBuckets` request to Amazon S3 can be continued with this
`ContinuationToken`. `ContinuationToken` is obfuscated and is not a real
bucket.

### `Prefix` — string

If `Prefix` was sent with the request, it is included in the response.

All bucket names in the response begin with the specified bucket name prefix.

## Examples

### To list all buckets

The following example returns all the buckets owned by the sender of this request.

Output:

```json
{
  "Owner": {
    "DisplayName": "own-display-name",
    "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31"
  },
  "Buckets": [
    {
      "CreationDate": "2012-02-15T21:03:02.000Z",
      "Name": "examplebucket"
    },
    {
      "CreationDate": "2011-07-24T19:33:50.000Z",
      "Name": "examplebucket2"
    },
    {
      "CreationDate": "2010-12-17T00:56:49.000Z",
      "Name": "examplebucket3"
    }
  ]
}
```
