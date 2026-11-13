# RemoveLayerVersionPermission

Service: AWS Lambda · SDK for JavaScript v3: `RemoveLayerVersionPermissionCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy/{StatementId}`

Removes a statement from the permissions policy for a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). For more information, see AddLayerVersionPermission.

## Input (`RemoveLayerVersionPermissionRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `VersionNumber` — long · **required** · sent as httpLabel · default `null`

The version number.

### `StatementId` — string · **required** · sent as httpLabel

The identifier that was specified when the statement was added.

### `RevisionId` — string · sent as query `RevisionId`

Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To delete layer-version permissions

The following example deletes permission for an account to configure a layer version.

Input:

```json
{
  "LayerName": "my-layer",
  "StatementId": "xaccount",
  "VersionNumber": 1
}
```
