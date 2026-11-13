# GetLayerVersionByArn

Service: AWS Lambda · SDK for JavaScript v3: `GetLayerVersionByArnCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2018-10-31/layers?find=LayerVersion`

Returns information about a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html), with a link to download the layer archive that's valid for 10 minutes.

## Input (`GetLayerVersionByArnRequest`)

### `Arn` — string · **required** · sent as query `Arn`

The ARN of the layer version.

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

The following example returns information about the layer version with the specified Amazon Resource Name (ARN).

Input:

```json
{
  "Arn": "arn:aws:lambda:ca-central-1:123456789012:layer:blank-python-lib:3"
}
```

Output:

```json
{
  "CompatibleRuntimes": [
    "python3.8"
  ],
  "Content": {
    "CodeSha256": "6x+xmpl/M3BnQUk7gS9sGmfeFsR/npojXoA3fZUv4eU=",
    "CodeSize": 9529009,
    "Location": "https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/blank-python-lib-e5212378-xmpl-44ee-8398-9d8ec5113949?versionId=WbZnvf..."
  },
  "CreatedDate": "2020-03-31T00:35:18.949+0000",
  "Description": "Dependencies for the blank-python sample app.",
  "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:blank-python-lib",
  "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:blank-python-lib:3",
  "Version": 3
}
```
