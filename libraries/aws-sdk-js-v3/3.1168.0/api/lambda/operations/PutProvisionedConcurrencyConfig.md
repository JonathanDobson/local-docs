# PutProvisionedConcurrencyConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutProvisionedConcurrencyConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2019-09-30/functions/{FunctionName}/provisioned-concurrency`

Adds a provisioned concurrency configuration to a function's alias or version.

## Input (`PutProvisionedConcurrencyConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · **required** · sent as query `Qualifier`

The version number or alias name.

### `ProvisionedConcurrentExecutions` — integer · **required**

The amount of provisioned concurrency to allocate for the version or alias.

## Output (`PutProvisionedConcurrencyConfigResponse`)

### `RequestedProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency requested.

### `AllocatedProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, this value fluctuates depending on the amount of concurrency that is provisioned for the function versions.

### `AvailableProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency available.

### `Status` — ProvisionedConcurrencyStatusEnum (enum)

The status of the allocation process.

Values: `IN_PROGRESS`, `READY`, `FAILED`

### `StatusReason` — string

For failed allocations, the reason that provisioned concurrency could not be allocated.

### `LastModified` — string

The date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To allocate provisioned concurrency

The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.

Input:

```json
{
  "FunctionName": "my-function",
  "ProvisionedConcurrentExecutions": 100,
  "Qualifier": "BLUE"
}
```

Output:

```json
{
  "AllocatedProvisionedConcurrentExecutions": 0,
  "LastModified": "2019-11-21T19:32:12+0000",
  "RequestedProvisionedConcurrentExecutions": 100,
  "Status": "IN_PROGRESS"
}
```
