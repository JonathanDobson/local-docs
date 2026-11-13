# GetObjectAcl

Service: Amazon Simple Storage Service · SDK for JavaScript v3: `GetObjectAclCommand` from `@aws-sdk/client-s3` · HTTP: `GET /{Bucket}/{Key+}?acl`

This operation is not supported for directory buckets.

Returns the access control list (ACL) of an object. To use this operation, you must have
`s3:GetObjectAcl` permissions or `READ_ACP` access to the object. For more
information, see [Mapping of ACL
permissions and access policy permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#acl-access-policy-permission-mapping) in the *Amazon S3 User Guide*

This functionality is not supported for Amazon S3 on Outposts.

By default, GET returns ACL information about the current version of an object. To return ACL
information about a different version, use the versionId subresource.

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, requests to read
ACLs are still supported and return the `bucket-owner-full-control` ACL with the owner
being the account that created the bucket. For more information, see  [Controlling object ownership and
disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.

The following operations are related to `GetObjectAcl`:

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Input (`GetObjectAclRequest`)

### `Bucket` — string · **required** · sent as httpLabel

The bucket name that contains the object for which to get the ACL information.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.

### `Key` — string · **required** · sent as httpLabel

The key of the object for which to get the ACL information.

### `VersionId` — string · sent as query `versionId`

Version ID used to reference a specific version of the object.

This functionality is not supported for directory buckets.

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

## Output (`GetObjectAclOutput`)

### `Owner` — Owner

Container for the bucket owner's ID.

### `Grants` — list<Grant>

A list of grants.

### `RequestCharged` — RequestCharged (enum) · sent as header `x-amz-request-charged`

If present, indicates that the requester was successfully charged for the request. For more
information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple
Storage Service user guide*.

This functionality is not supported for directory buckets.

Values: `requester`

## Errors

- `NoSuchKey` — The specified key does not exist.

## Examples

### To retrieve object ACL

The following example retrieves access control list (ACL) of an object.

Input:

```json
{
  "Bucket": "examplebucket",
  "Key": "HappyFace.jpg"
}
```

Output:

```json
{
  "Owner": {
    "DisplayName": "owner-display-name",
    "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
  },
  "Grants": [
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "DisplayName": "owner-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Permission": "WRITE"
    },
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "DisplayName": "owner-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Permission": "WRITE_ACP"
    },
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "DisplayName": "owner-display-name",
        "ID": "examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Permission": "READ"
    },
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "DisplayName": "owner-display-name",
        "ID": "852b113eexamplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
      },
      "Permission": "READ_ACP"
    }
  ]
}
```
