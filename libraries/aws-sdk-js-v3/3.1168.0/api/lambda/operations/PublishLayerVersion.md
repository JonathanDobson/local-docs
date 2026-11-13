# PublishLayerVersion

Service: AWS Lambda · SDK for JavaScript v3: `PublishLayerVersionCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2018-10-31/layers/{LayerName}/versions`

Creates an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) from a ZIP archive. Each time you call `PublishLayerVersion` with the same layer name, a new version is created.

Add layers to your function with CreateFunction or UpdateFunctionConfiguration.

## Input (`PublishLayerVersionRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `Description` — string

The description of the version.

### `Content` — LayerVersionContentInput · **required**

The function layer archive.

### `CompatibleArchitectures` — list<Architecture (enum)>

A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).

### `CompatibleRuntimes` — list<Runtime (enum)>

A list of compatible [function runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Used for filtering with ListLayers and ListLayerVersions.

The following list includes deprecated runtimes. For more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy).

### `LicenseInfo` — string

The layer's software license. It can be any of the following:

- An [SPDX license identifier](https://spdx.org/licenses/). For example, `MIT`.
- The URL of a license hosted on the internet. For example, `https://opensource.org/licenses/MIT`.
- The full text of the license.

## Output (`PublishLayerVersionResponse`)

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

- `CodeStorageExceededException` — Your Amazon Web Services account has exceeded its maximum total code size.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To create a Lambda layer version

The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.

Input:

```json
{
  "CompatibleRuntimes": [
    "python3.6",
    "python3.7"
  ],
  "Content": {
    "S3Bucket": "lambda-layers-us-west-2-123456789012",
    "S3Key": "layer.zip"
  },
  "Description": "My Python layer",
  "LayerName": "my-layer",
  "LicenseInfo": "MIT"
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
    "Location": "https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH..."
  },
  "CreatedDate": "2018-11-14T23:03:52.894+0000",
  "Description": "My Python layer",
  "LayerArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer",
  "LayerVersionArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1",
  "LicenseInfo": "MIT",
  "Version": 1
}
```
