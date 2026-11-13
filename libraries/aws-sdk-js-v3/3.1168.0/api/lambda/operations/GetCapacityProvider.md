# GetCapacityProvider

Service: AWS Lambda · SDK for JavaScript v3: `GetCapacityProviderCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-11-30/capacity-providers/{CapacityProviderName}`

Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.

## Input (`GetCapacityProviderRequest`)

### `CapacityProviderName` — string · **required** · sent as httpLabel

The name of the capacity provider to retrieve.

## Output (`GetCapacityProviderResponse`)

### `CapacityProvider` — CapacityProvider · **required**

Information about the capacity provider, including its configuration and current state.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
