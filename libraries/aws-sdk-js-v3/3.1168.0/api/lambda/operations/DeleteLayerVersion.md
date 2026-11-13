# DeleteLayerVersion

Service: AWS Lambda · SDK for JavaScript v3: `DeleteLayerVersionCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2018-10-31/layers/{LayerName}/versions/{VersionNumber}`

Deletes a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.

## Input (`DeleteLayerVersionRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `VersionNumber` — long · **required** · sent as httpLabel · default `null`

The version number.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete a version of a Lambda layer

The following example deletes version 2 of a layer named my-layer.

Input:

```json
{
  "LayerName": "my-layer",
  "VersionNumber": 2
}
```
