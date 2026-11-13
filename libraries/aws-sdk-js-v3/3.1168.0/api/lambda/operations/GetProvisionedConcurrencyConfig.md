# GetProvisionedConcurrencyConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetProvisionedConcurrencyConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2019-09-30/functions/{FunctionName}/provisioned-concurrency`

Retrieves the provisioned concurrency configuration for a function's alias or version.

## Input (`GetProvisionedConcurrencyConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · **required** · sent as query `Qualifier`

The version number or alias name.

## Output (`GetProvisionedConcurrencyConfigResponse`)

### `RequestedProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency requested.

### `AvailableProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency available.

### `AllocatedProvisionedConcurrentExecutions` — integer

The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, this value fluctuates depending on the amount of concurrency that is provisioned for the function versions.

### `Status` — ProvisionedConcurrencyStatusEnum (enum)

The status of the allocation process.

Values: `IN_PROGRESS`, `READY`, `FAILED`

### `StatusReason` — string

For failed allocations, the reason that provisioned concurrency could not be allocated.

### `LastModified` — string

The date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ProvisionedConcurrencyConfigNotFoundException` — The specified configuration does not exist.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a provisioned concurrency configuration

The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "BLUE"
}
```

Output:

```json
{
  "AllocatedProvisionedConcurrentExecutions": 100,
  "AvailableProvisionedConcurrentExecutions": 100,
  "LastModified": "2019-12-31T20:28:49+0000",
  "RequestedProvisionedConcurrentExecutions": 100,
  "Status": "READY"
}
```

### To view a provisioned concurrency configuration

The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.

Input:

```json
{
  "FunctionName": "my-function",
  "Qualifier": "BLUE"
}
```

Output:

```json
{
  "AllocatedProvisionedConcurrentExecutions": 100,
  "AvailableProvisionedConcurrentExecutions": 100,
  "LastModified": "2019-12-31T20:28:49+0000",
  "RequestedProvisionedConcurrentExecutions": 100,
  "Status": "READY"
}
```
