# AddLayerVersionPermission

Service: AWS Lambda · SDK for JavaScript v3: `AddLayerVersionPermissionCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy`

Adds permissions to the resource-based policy of a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all Amazon Web Services accounts.

To revoke permission, call RemoveLayerVersionPermission with the statement ID that you specified when you added it.

## Input (`AddLayerVersionPermissionRequest`)

### `LayerName` — string · **required** · sent as httpLabel

The name or Amazon Resource Name (ARN) of the layer.

### `VersionNumber` — long · **required** · sent as httpLabel · default `null`

The version number.

### `StatementId` — string · **required**

An identifier that distinguishes the policy from others on the same layer version.

### `Action` — string · **required**

The API action that grants access to the layer. For example, `lambda:GetLayerVersion`.

### `Principal` — string · **required**

An account ID, or `*` to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accounts (if `organizationId` is not specified). For the last case, make sure that you really do want all Amazon Web Services accounts to have usage permission to this layer.

### `OrganizationId` — string

With the principal set to `*`, grant permission to all accounts in the specified organization.

### `RevisionId` — string · sent as query `RevisionId`

Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

## Output (`AddLayerVersionPermissionResponse`)

### `Statement` — string

The permission statement.

### `RevisionId` — string

A unique identifier for the current revision of the policy.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PolicyLengthExceededException` — The permissions policy for the resource is too large.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To add permissions to a layer version

The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.

Input:

```json
{
  "Action": "lambda:GetLayerVersion",
  "LayerName": "my-layer",
  "Principal": "223456789012",
  "StatementId": "xaccount",
  "VersionNumber": 1
}
```

Output:

```json
{
  "RevisionId": "35d87451-f796-4a3f-a618-95a3671b0a0c",
  "Statement": "{\"Sid\":\"xaccount\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::223456789012:root\"},\"Action\":\"lambda:GetLayerVersion\",\"Resource\":\"arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1\"}"
}
```
