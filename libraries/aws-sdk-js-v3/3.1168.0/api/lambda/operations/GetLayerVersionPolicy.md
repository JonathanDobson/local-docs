# GetLayerVersionPolicy

Service: AWS Lambda · SDK for JavaScript v3: `GetLayerVersionPolicyCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy`

Returns the permission policy for a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). For more information, see AddLayerVersionPermission.

## Input (`GetLayerVersionPolicyRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `VersionNumber` — long · **required** · sent as httpLabel · default `null`

The version number.

## Output (`GetLayerVersionPolicyResponse`)

### `Policy` — string

The policy document.

### `RevisionId` — string

A unique identifier for the current revision of the policy.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
