# GetFunctionConcurrency

Service: AWS Lambda · SDK for JavaScript v3: `GetFunctionConcurrencyCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2019-09-30/functions/{FunctionName}/concurrency`

Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use PutFunctionConcurrency.

## Input (`GetFunctionConcurrencyRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

## Output (`GetFunctionConcurrencyResponse`)

### `ReservedConcurrentExecutions` — integer

The number of simultaneous executions that are reserved for the function.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get the reserved concurrency setting for a function

The following example returns the reserved concurrency setting for a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "ReservedConcurrentExecutions": 250
}
```
