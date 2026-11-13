# DeleteResourcePolicy

Service: AWS Lambda · SDK for JavaScript v3: `DeleteResourcePolicyCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2026-07-09/resource-policy/{ResourceArn}`

Deletes a [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) from a Lambda resource.

## Input (`DeleteResourcePolicyRequest`)

### `ResourceArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the Lambda resource you want to delete the policy from. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.

### `RevisionId` — string · sent as query `RevisionId`

The revision ID that the existing policy must match for the deletion to proceed. If the revision ID doesn't match, the operation fails with a `PreconditionFailedException` error. To retrieve the current revision ID, use the GetResourcePolicy operation.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
