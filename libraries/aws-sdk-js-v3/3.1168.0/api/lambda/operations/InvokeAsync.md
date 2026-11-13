# InvokeAsync

Service: AWS Lambda · SDK for JavaScript v3: `InvokeAsyncCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2014-11-13/functions/{FunctionName}/invoke-async` · **Deprecated**

For asynchronous function invocation, use Invoke.

Invokes a function asynchronously.

The payload limit is 256KB. For larger payloads, for up to 1MB, use Invoke.



If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.

## Input (`InvokeAsyncRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `InvokeArgs` — blob · **required** · sent as httpPayload

The JSON that you want to provide to your Lambda function as input.

## Output (`InvokeAsyncResponse`)

### `Status` — integer · default `0`

The status code.

## Errors

- `EC2AccessDeniedException` — Need additional permissions to configure VPC settings.
- `EC2ThrottledException` — Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.
- `EC2UnexpectedException` — Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.
- `EFSIOException` — An error occurred when reading from or writing to a connected file system.
- `EFSMountConnectivityException` — The Lambda function couldn't make a network connection to the configured file system.
- `EFSMountFailureException` — The Lambda function couldn't mount the configured file system due to a permission or configuration issue.
- `EFSMountTimeoutException` — The Lambda function made a network connection to the configured file system, but the mount operation timed out.
- `ENILimitReachedException` — Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached.
- `InvalidRequestContentException` — The request body could not be parsed as JSON, or a request header is invalid.
- `InvalidRuntimeException` — The runtime or runtime version specified is not supported.
- `InvalidSecurityGroupIDException` — The security group ID provided in the Lambda function VPC configuration is not valid.
- `InvalidSubnetIDException` — The subnet ID provided in the Lambda function VPC configuration is not valid.
- `KMSAccessDeniedException` — Lambda couldn't decrypt the environment variables because KMS access was denied.
- `KMSDisabledException` — Lambda couldn't decrypt the environment variables because the KMS key used is disabled.
- `KMSInvalidStateException` — Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt.
- `KMSNotFoundException` — Lambda couldn't decrypt the environment variables because the KMS key was not found.
- `ModeNotSupportedException` — The Lambda function doesn't support the invocation mode requested.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `S3FilesMountConnectivityException` — The Lambda function couldn't make a network connection to the configured S3 Files access point.
- `S3FilesMountFailureException` — The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.
- `S3FilesMountTimeoutException` — The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.
- `ServiceException` — The Lambda service encountered an internal error.
- `ServiceQuotaExceededException` — The request would exceed a service quota.
- `SnapStartException` — The `afterRestore()` [runtime hook](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html) encountered an error.
- `SnapStartNotReadyException` — Lambda is initializing your function.
- `SnapStartRegenerationFailureException` — Lambda couldn't regenerate the SnapStart snapshot for the function.
- `SnapStartTimeoutException` — Lambda couldn't restore the snapshot within the timeout limit.
- `SubnetIPAddressLimitReachedException` — Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.

## Examples

### To invoke a Lambda function asynchronously

The following example invokes a Lambda function asynchronously

Input:

```json
{
  "FunctionName": "my-function",
  "InvokeArgs": "{}"
}
```

Output:

```json
{
  "Status": 202
}
```
