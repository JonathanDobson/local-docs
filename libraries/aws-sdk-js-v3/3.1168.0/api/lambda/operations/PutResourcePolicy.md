# PutResourcePolicy

Service: AWS Lambda · SDK for JavaScript v3: `PutResourcePolicyCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2026-07-09/resource-policy/{ResourceArn}`

Adds a [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) to a Lambda resource. Resource-based policies grant access to other [Amazon Web Services accounts](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-cross-account.html), [organizations](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-organization.html), or [services](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-services.html). Resource-based policies apply to a single Lambda resource (for example, a function, function version, or function alias).

This operation replaces any existing policy on the Lambda resource. If you previously added permissions using the AddPermission operation, the new policy overwrites those permissions.

## Input (`PutResourcePolicyRequest`)

### `ResourceArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the Lambda resource you want to add the policy to. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.

### `Policy` — string · **required**

The policy document you want to add to your Lambda resource. This is formatted as a JSON string.

For more information, see [Working with resource-based policies in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *Lambda Developer Guide*.

### `RevisionId` — string

The revision ID that the existing policy must match for the replacement to proceed. If the revision ID doesn't match, the operation fails with a `PreconditionFailedException` error. To retrieve the current revision ID, use the GetResourcePolicy operation.

## Output (`PutResourcePolicyResponse`)

### `Policy` — string

The resource-based policy that Lambda adds to the resource.

### `RevisionId` — string

The revision ID of the policy that Lambda adds to your Lambda resource.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PolicyLengthExceededException` — The permissions policy for the resource is too large.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `PublicPolicyException` — The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
