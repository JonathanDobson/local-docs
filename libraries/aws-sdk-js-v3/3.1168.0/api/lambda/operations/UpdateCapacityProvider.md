# UpdateCapacityProvider

Service: AWS Lambda · SDK for JavaScript v3: `UpdateCapacityProviderCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2025-11-30/capacity-providers/{CapacityProviderName}`

Updates the configuration of an existing capacity provider.

## Input (`UpdateCapacityProviderRequest`)

### `CapacityProviderName` — string · **required** · sent as httpLabel

The name of the capacity provider to update.

### `CapacityProviderScalingConfig` — CapacityProviderScalingConfig

The updated scaling configuration for the capacity provider.

### `PropagateTags` — PropagateTags

Configuration for tag propagation to managed resources launched by the capacity provider.

### `TelemetryConfig` — CapacityProviderTelemetryConfig

The updated telemetry configuration for the capacity provider.

## Output (`UpdateCapacityProviderResponse`)

### `CapacityProvider` — CapacityProvider · **required**

Information about the updated capacity provider.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
