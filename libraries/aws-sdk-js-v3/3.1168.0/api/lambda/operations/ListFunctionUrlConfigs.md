# ListFunctionUrlConfigs

Service: AWS Lambda · SDK for JavaScript v3: `ListFunctionUrlConfigsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2021-10-31/functions/{FunctionName}/urls` · Paginated

Returns a list of Lambda function URLs for the specified function.

## Input (`ListFunctionUrlConfigsRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of function URLs to return in the response. Note that `ListFunctionUrlConfigs` returns a maximum of 50 items in each response, even if you set the number higher.

## Output (`ListFunctionUrlConfigsResponse`)

### `FunctionUrlConfigs` — list<FunctionUrlConfig> · **required**

A list of function URL configurations.

### `NextMarker` — string

The pagination token that's included if more results are available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
