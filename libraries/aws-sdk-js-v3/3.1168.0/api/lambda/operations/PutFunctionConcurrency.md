# PutFunctionConcurrency

Service: AWS Lambda · SDK for JavaScript v3: `PutFunctionConcurrencyCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2017-10-31/functions/{FunctionName}/concurrency`

Sets the maximum number of simultaneous executions for a Lambda Event Function, and reserves capacity for that concurrency level.

Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use GetFunction to see the current setting for a function.

Use GetAccountSettings to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html).

## Input (`PutFunctionConcurrencyRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `ReservedConcurrentExecutions` — integer · **required**

The number of simultaneous executions to reserve for the function.

## Output (`Concurrency`)

### `ReservedConcurrentExecutions` — integer

The number of concurrent executions that are reserved for this function. For more information, see [Managing Lambda reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To configure a reserved concurrency limit for a function

The following example configures 100 reserved concurrent executions for the my-function function.

Input:

```json
{
  "FunctionName": "my-function",
  "ReservedConcurrentExecutions": 100
}
```

Output:

```json
{
  "ReservedConcurrentExecutions": 100
}
```
