# ListFunctionVersionsByCapacityProvider

Service: AWS Lambda · SDK for JavaScript v3: `ListFunctionVersionsByCapacityProviderCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-11-30/capacity-providers/{CapacityProviderName}/function-versions` · Paginated (token `Marker` → `NextMarker`)

Returns a list of function versions that are configured to use a specific capacity provider.

## Input (`ListFunctionVersionsByCapacityProviderRequest`)

### `CapacityProviderName` — string · **required** · sent as httpLabel

The name of the capacity provider to list function versions for.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of function versions to return in the response.

## Output (`ListFunctionVersionsByCapacityProviderResponse`)

### `CapacityProviderArn` — string · **required**

The Amazon Resource Name (ARN) of the capacity provider.

### `FunctionVersions` — list<FunctionVersionsByCapacityProviderListItem> · **required**

A list of function versions that use the specified capacity provider.

### `NextMarker` — string

The pagination token that's included if more results are available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
