# ListFunctionEventInvokeConfigs

Service: AWS Lambda · SDK for JavaScript v3: `ListFunctionEventInvokeConfigsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2019-09-25/functions/{FunctionName}/event-invoke-config/list` · Paginated

Retrieves a list of configurations for asynchronous invocation for a Lambda Event Function. To retrieve more configurations, use the `Marker` parameter.

To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig.

## Input (`ListFunctionEventInvokeConfigsRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `my-function`.
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** - `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of configurations to return.

## Output (`ListFunctionEventInvokeConfigsResponse`)

### `FunctionEventInvokeConfigs` — list<FunctionEventInvokeConfig>

A list of configurations.

### `NextMarker` — string

The pagination token that's included if more results are available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To view a list of asynchronous invocation configurations

The following example returns a list of asynchronous invocation configurations for a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "FunctionEventInvokeConfigs": [
    {
      "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN",
      "LastModified": 1577824406.719,
      "MaximumEventAgeInSeconds": 1800,
      "MaximumRetryAttempts": 2
    },
    {
      "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE",
      "LastModified": 1577824396.653,
      "MaximumEventAgeInSeconds": 3600,
      "MaximumRetryAttempts": 0
    }
  ]
}
```
