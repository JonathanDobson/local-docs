# InvokeWithResponseStream

Service: AWS Lambda · SDK for JavaScript v3: `InvokeWithResponseStreamCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2021-11-15/functions/{FunctionName}/response-streaming-invocations`

Configure your Lambda Event Functions to stream response payloads back to clients. For more information, see [Configuring a Lambda function to stream responses](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html).

This operation requires permission for the [lambda:InvokeFunction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html) action. For details on how to set up permissions for cross-account invocations, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke).

## Input (`InvokeWithResponseStreamRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `LogType` — LogType (enum) · sent as header `X-Amz-Log-Type`

Set to `Tail` to include the execution log in the response. Applies to synchronously invoked functions only.

Values: `None`, `Tail`

### `ClientContext` — string · sent as header `X-Amz-Client-Context`

Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.

### `Qualifier` — string · sent as query `Qualifier`

The alias name.

### `Payload` — blob · sent as httpPayload

The JSON that you want to provide to your Lambda function as input.

You can enter the JSON directly. For example, `--payload '{ "key": "value" }'`. You can also specify a file path. For example, `--payload file://payload.json`.

### `TenantId` — string · sent as header `X-Amz-Tenant-Id`

The identifier of the tenant in a multi-tenant Lambda function.

### `InvocationType` — ResponseStreamingInvocationType (enum) · sent as header `X-Amz-Invocation-Type`

Use one of the following options:

- `RequestResponse` (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.
- `DryRun` – Validate parameter values and verify that the IAM user or role has permission to invoke the function.

Values: `RequestResponse`, `DryRun`

## Output (`InvokeWithResponseStreamResponse`)

### `StatusCode` — integer · default `0`

For a successful request, the HTTP status code is in the 200 range. For the `RequestResponse` invocation type, this status code is 200. For the `DryRun` invocation type, this status code is 204.

### `ExecutedVersion` — string · sent as header `X-Amz-Executed-Version`

The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.

### `EventStream` — InvokeWithResponseStreamResponseEvent · sent as httpPayload

The stream of response payloads.

### `ResponseStreamContentType` — string · sent as header `Content-Type`

The type of data the stream is returning.

## Errors

- `CodeArtifactUserDeletedException` — The Lambda function couldn't be invoked because its code artifact user has been deleted.
- `CodeArtifactUserFailedException` — The Lambda function couldn't be invoked because provisioning of its code artifact user failed.
- `CodeArtifactUserPendingException` — The Lambda function couldn't be invoked because its code artifact user is still being provisioned.
- `EC2AccessDeniedException` — Need additional permissions to configure VPC settings.
- `EC2ThrottledException` — Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.
- `EC2UnexpectedException` — Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.
- `EFSIOException` — An error occurred when reading from or writing to a connected file system.
- `EFSMountConnectivityException` — The Lambda function couldn't make a network connection to the configured file system.
- `EFSMountFailureException` — The Lambda function couldn't mount the configured file system due to a permission or configuration issue.
- `EFSMountTimeoutException` — The Lambda function made a network connection to the configured file system, but the mount operation timed out.
- `ENILimitReachedException` — Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached.
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
