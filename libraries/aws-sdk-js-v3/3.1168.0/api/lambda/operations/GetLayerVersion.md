# GetLayerVersion

Service: AWS Lambda · SDK for JavaScript v3: `GetLayerVersionCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2018-10-31/layers/{LayerName}/versions/{VersionNumber}`

Returns information about a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html), with a link to download the layer archive that's valid for 10 minutes.

## Input (`GetLayerVersionRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `VersionNumber` — long · **required** · sent as httpLabel · default `null`

The version number.

## Output (`GetLayerVersionResponse`)

### `Content` — LayerVersionContentOutput

Details about the layer version.

### `LayerArn` — string

The ARN of the layer.

### `LayerVersionArn` — string

The ARN of the layer version.

### `Description` — string

The description of the version.

### `CreatedDate` — string

The date that the layer version was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

### `Version` — long · default `0`

The version number.

### `CompatibleArchitectures` — list<Architecture (enum)>

A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).

### `CompatibleRuntimes` — list<Runtime (enum)>

The layer's compatible runtimes.

The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).

### `LicenseInfo` — string

The layer's software license.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get information about a Lambda layer version

The following example returns information for version 1 of a layer named my-layer.

Input:

```json
{
  "LayerName": "my-layer",
  "VersionNumber": 1
}
```

Output:

```json
{
  "CompatibleRuntimes": [
    "python3.6",
    "python3.7"
  ],
  "Content": {
    "CodeSha256": "tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=",
    "CodeSize": 169,
    "Location": "https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH..."
  },
  "CreatedDate": "2018-11-14T23:03:52.894+0000",
  "Description": "My Python layer",
  "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer",
  "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1",
  "LicenseInfo": "MIT",
  "Version": 1
}
```
