# DeleteCapacityProvider

Service: AWS Lambda · SDK for JavaScript v3: `DeleteCapacityProviderCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2025-11-30/capacity-providers/{CapacityProviderName}`

Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions.

## Input (`DeleteCapacityProviderRequest`)

### `CapacityProviderName` — string · **required** · sent as httpLabel

The name of the capacity provider to delete.

## Output (`DeleteCapacityProviderResponse`)

### `CapacityProvider` — CapacityProvider · **required**

Information about the deleted capacity provider.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
