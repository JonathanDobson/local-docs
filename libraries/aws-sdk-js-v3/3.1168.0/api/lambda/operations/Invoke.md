# Invoke

Service: AWS Lambda · SDK for JavaScript v3: `InvokeCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2015-03-31/functions/{FunctionName}/invocations`

Invokes a Lambda Event Function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the`InvocationType` is `RequestResponse`). To invoke a function asynchronously, set `InvocationType` to `Event`. Lambda passes the `ClientContext` object to your function for synchronous invocations only.

For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB.

For [synchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html), details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the [execution log](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html) and [trace](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html).

When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see [Error handling and automatic retries in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html).

For [asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html), Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a [dead-letter queue](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).

The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, [quota](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) errors, or issues with your function's code and configuration. For example, Lambda returns `TooManyRequestsException` if running the function would cause you to exceed a concurrency limit at either the account level (`ConcurrentInvocationLimitExceeded`) or function level (`ReservedFunctionConcurrentInvocationLimitExceeded`).

For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.

This operation requires permission for the [lambda:InvokeFunction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html) action. For details on how to set up permissions for cross-account invocations, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke).

## Input (`InvocationRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `InvocationType` — InvocationType (enum) · sent as header `X-Amz-Invocation-Type`

Choose from the following options.

- `RequestResponse` (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.
- `Event` – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.
- `DryRun` – Validate parameter values and verify that the user or role has permission to invoke the function.

Values: `Event`, `RequestResponse`, `DryRun`

### `LogType` — LogType (enum) · sent as header `X-Amz-Log-Type`

Set to `Tail` to include the execution log in the response. Applies to synchronously invoked functions only.

Values: `None`, `Tail`

### `ClientContext` — string · sent as header `X-Amz-Client-Context`

Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the `ClientContext` object to your function for synchronous invocations only.

### `DurableExecutionName` — string · sent as header `X-Amz-Durable-Execution-Name`

A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a `DurableExecutionAlreadyStartedException` error.

If not specified, Lambda generates a unique identifier automatically. For more information, see [Execution names](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names).

### `Payload` — blob · sent as httpPayload

The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.

You can enter the JSON directly. For example, `--payload '{ "key": "value" }'`. You can also specify a file path. For example, `--payload file://payload.json`.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version or alias to invoke a published version of the function.

### `TenantId` — string · sent as header `X-Amz-Tenant-Id`

The identifier of the tenant in a multi-tenant Lambda function.

## Output (`InvocationResponse`)

### `StatusCode` — integer · default `0`

The HTTP status code is in the 200 range for a successful request. For the `RequestResponse` invocation type, this status code is 200. For the `Event` invocation type, this status code is 202. For the `DryRun` invocation type, the status code is 204.

### `FunctionError` — string · sent as header `X-Amz-Function-Error`

If present, indicates that an error occurred during function execution. Details about the error are included in the response payload.

### `LogResult` — string · sent as header `X-Amz-Log-Result`

The last 4 KB of the execution log, which is base64-encoded.

### `Payload` — blob · sent as httpPayload

The response from the function, or an error object.

### `ExecutedVersion` — string · sent as header `X-Amz-Executed-Version`

The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.

### `DurableExecutionArn` — string · sent as header `X-Amz-Durable-Execution-Arn`

The ARN of the durable execution that was started. This is returned when invoking a durable function and provides a unique identifier for tracking the execution.

## Errors

- `CodeArtifactUserDeletedException` — The Lambda function couldn't be invoked because its code artifact user has been deleted.
- `CodeArtifactUserFailedException` — The Lambda function couldn't be invoked because provisioning of its code artifact user failed.
- `CodeArtifactUserPendingException` — The Lambda function couldn't be invoked because its code artifact user is still being provisioned.
- `DurableExecutionAlreadyStartedException` — The durable execution with the specified name has already been started.
- `EC2AccessDeniedException` — Need additional permissions to configure VPC settings.
- `EC2ThrottledException` — Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.
- `EC2UnexpectedException` — Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.
- `EFSIOException` — An error occurred when reading from or writing to a connected file system.
- `EFSMountConnectivityException` — The Lambda function couldn't make a network connection to the configured file system.
- `EFSMountFailureException` — The Lambda function couldn't mount the configured file system due to a permission or configuration issue.
- `EFSMountTimeoutException` — The Lambda function made a network connection to the configured file system, but the mount operation timed out.
- `ENILimitReachedException` — Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached.
- `ENINotReadyException` — Lambda couldn't invoke the Lambda function because the elastic network interface (ENI) configured for its VPC connection isn't ready yet.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `InvalidRequestContentException` — The request body could not be parsed as JSON, or a request header is invalid.
- `InvalidRuntimeException` — The runtime or runtime version specified is not supported.
- `InvalidSecurityGroupIDException` — The security group ID provided in the Lambda function VPC configuration is not valid.
- `InvalidSubnetIDException` — The subnet ID provided in the Lambda function VPC configuration is not valid.
- `InvalidZipFileException` — Lambda could not unzip the deployment package.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ModeNotSupportedException` — The Lambda function doesn't support the invocation mode requested.
- `NoPublishedVersionException` — The function has no published versions available.
- `RecursiveInvocationException` — Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.
- `RequestTooLargeException` — The request payload exceeded the `Invoke` request body JSON input quota.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ResourceNotReadyException` — The function is inactive and its VPC connection is no longer available.
- `S3FilesMountConnectivityException` — The Lambda function couldn't make a network connection to the configured S3 Files access point.
- `S3FilesMountFailureException` — The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.
- `S3FilesMountTimeoutException` — The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.
- `SerializedRequestEntityTooLargeException` — The request payload exceeded the maximum allowed size for serialized request entities.
- `ServiceException` — The Lambda service encountered an internal error.
- `ServiceQuotaExceededException` — The request would exceed a service quota.
- `SnapStartException` — The `afterRestore()` [runtime hook](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html) encountered an error.
- `SnapStartNotReadyException` — Lambda is initializing your function.
- `SnapStartRegenerationFailureException` — Lambda couldn't regenerate the SnapStart snapshot for the function.
- `SnapStartTimeoutException` — Lambda couldn't restore the snapshot within the timeout limit.
- `SubnetIPAddressLimitReachedException` — Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.
- `TooManyRequestsException` — The request throughput limit was exceeded.
- `UnsupportedMediaTypeException` — The content type of the `Invoke` request body is not JSON.

## Examples

### To invoke a Lambda function

The following example invokes version 1 of a function named my-function with an empty event payload.

Input:

```json
{
  "DurableExecutionName": "myExecution",
  "FunctionName": "my-function",
  "InvocationType": "Event",
  "Payload": "{}",
  "Qualifier": "1"
}
```

Output:

```json
{
  "Payload": "200 SUCCESS",
  "StatusCode": 200
}
```

### To invoke a Lambda function asynchronously

The following example invokes version 1 of a function named my-function asynchronously.

Input:

```json
{
  "FunctionName": "my-function",
  "InvocationType": "Event",
  "Payload": "{}",
  "Qualifier": "1"
}
```

Output:

```json
{
  "Payload": "",
  "StatusCode": 202
}
```
