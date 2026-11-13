# GetResourcePolicy

Service: AWS Lambda · SDK for JavaScript v3: `GetResourcePolicyCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2026-07-09/resource-policy/{ResourceArn}`

Retrieves the [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) attached to a Lambda resource.

## Input (`GetResourcePolicyRequest`)

### `ResourceArn` — string · **required** · sent as httpLabel

The Amazon Resource Name (ARN) of the Lambda resource you want to retrieve the policy for. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.

## Output (`GetResourcePolicyResponse`)

### `Policy` — string

The resource-based policy attached to the Lambda resource you specified.

### `RevisionId` — string

The revision ID of the policy. Pass this value as the `RevisionId` in a PutResourcePolicy or DeleteResourcePolicy request. Doing so ensures the operation acts on the expected version of the policy.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
