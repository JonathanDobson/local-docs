# ListCapacityProviders

Service: AWS Lambda · SDK for JavaScript v3: `ListCapacityProvidersCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-11-30/capacity-providers` · Paginated (token `Marker` → `NextMarker`)

Returns a list of capacity providers in your account.

## Input (`ListCapacityProvidersRequest`)

### `State` — CapacityProviderState (enum) · sent as query `State`

Filter capacity providers by their current state.

Values: `Pending`, `Active`, `Failed`, `Deleting`

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of capacity providers to return.

## Output (`ListCapacityProvidersResponse`)

### `CapacityProviders` — list<CapacityProvider> · **required**

A list of capacity providers in your account.

### `NextMarker` — string

The pagination token that's included if more results are available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
