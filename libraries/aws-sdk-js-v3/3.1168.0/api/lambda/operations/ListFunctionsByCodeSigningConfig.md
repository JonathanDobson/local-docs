# ListFunctionsByCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `ListFunctionsByCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2020-04-22/code-signing-configs/{CodeSigningConfigArn}/functions` · Paginated

List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.

## Input (`ListFunctionsByCodeSigningConfigRequest`)

### `CodeSigningConfigArn` — string · **required** · sent as httpLabel

The The Amazon Resource Name (ARN) of the code signing configuration.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

Maximum number of items to return.

## Output (`ListFunctionsByCodeSigningConfigResponse`)

### `NextMarker` — string

The pagination token that's included if more results are available.

### `FunctionArns` — list<string>

The function ARNs.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
