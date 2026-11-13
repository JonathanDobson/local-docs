# ListProvisionedConcurrencyConfigs

Service: AWS Lambda · SDK for JavaScript v3: `ListProvisionedConcurrencyConfigsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2019-09-30/functions/{FunctionName}/provisioned-concurrency?List=ALL` · Paginated

Retrieves a list of provisioned concurrency configurations for a function.

## Input (`ListProvisionedConcurrencyConfigsRequest`)

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

Specify a number to limit the number of configurations returned.

## Output (`ListProvisionedConcurrencyConfigsResponse`)

### `ProvisionedConcurrencyConfigs` — list<ProvisionedConcurrencyConfigListItem>

A list of provisioned concurrency configurations.

### `NextMarker` — string

The pagination token that's included if more results are available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a list of provisioned concurrency configurations

The following example returns a list of provisioned concurrency configurations for a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "ProvisionedConcurrencyConfigs": [
    {
      "AllocatedProvisionedConcurrentExecutions": 100,
      "AvailableProvisionedConcurrentExecutions": 100,
      "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN",
      "LastModified": "2019-12-31T20:29:00+0000",
      "RequestedProvisionedConcurrentExecutions": 100,
      "Status": "READY"
    },
    {
      "AllocatedProvisionedConcurrentExecutions": 100,
      "AvailableProvisionedConcurrentExecutions": 100,
      "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE",
      "LastModified": "2019-12-31T20:28:49+0000",
      "RequestedProvisionedConcurrentExecutions": 100,
      "Status": "READY"
    }
  ]
}
```
