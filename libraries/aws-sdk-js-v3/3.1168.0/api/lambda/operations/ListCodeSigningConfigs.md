# ListCodeSigningConfigs

Service: AWS Lambda · SDK for JavaScript v3: `ListCodeSigningConfigsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2020-04-22/code-signing-configs` · Paginated

Returns a list of [code signing configurations](https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html). A request returns up to 10,000 configurations per call. You can use the `MaxItems` parameter to return fewer configurations per call.

## Input (`ListCodeSigningConfigsRequest`)

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

Maximum number of items to return.

## Output (`ListCodeSigningConfigsResponse`)

### `NextMarker` — string

The pagination token that's included if more results are available.

### `CodeSigningConfigs` — list<CodeSigningConfig>

The code signing configurations

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ServiceException` — The Lambda service encountered an internal error.
