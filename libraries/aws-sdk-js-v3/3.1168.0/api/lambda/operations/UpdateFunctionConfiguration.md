# UpdateFunctionConfiguration

Service: AWS Lambda · SDK for JavaScript v3: `UpdateFunctionConfigurationCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2015-03-31/functions/{FunctionName}/configuration`

Modifies the version-specific settings of a Lambda Event Function.

When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can't modify the function, but you can still invoke it. The `LastUpdateStatus`, `LastUpdateStatusReason`, and `LastUpdateStatusReasonCode` fields in the response from GetFunctionConfiguration indicate when the update is complete and the function is processing events with the new configuration. For more information, see [Lambda function states](https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html).

These settings can vary between versions of a function and are locked when you publish a version. You can't modify the configuration of a published version, only the unpublished version.

To configure function concurrency, use PutFunctionConcurrency. To grant invoke permissions to an Amazon Web Services account or Amazon Web Services service, use AddPermission.

## Input (`UpdateFunctionConfigurationRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Role` — string

The Amazon Resource Name (ARN) of the function's execution role.

### `Handler` — string

The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see [Lambda programming model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html).

### `Description` — string

A description of the function.

### `Timeout` — integer

The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds, and the maximum allowed value is 900 seconds. For functions using Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum allowed value of 5,400 seconds (90 minutes). For more information, see [Lambda execution environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html).

### `MemorySize` — integer

The amount of [memory available to the function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console) at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.

### `VpcConfig` — VpcConfig

For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).

### `Environment` — Environment

Environment variables that are accessible from function code during execution.

### `Runtime` — Runtime (enum)

The identifier of the function's  [runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.

The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).

Values: `nodejs`, `nodejs4.3`, `nodejs6.10`, `nodejs8.10`, `nodejs10.x`, `nodejs12.x`, `nodejs14.x`, `nodejs16.x`, `nodejs18.x`, `nodejs20.x`, `nodejs22.x`, `nodejs24.x`, `java8`, `java8.al2`, `java11`, `java17`, `java21`, `java25`, `python2.7`, `python3.6`, `python3.7`, `python3.8`, `python3.9`, `python3.10`, `python3.11`, `python3.12`, `python3.13`, `python3.14`, `dotnetcore1.0`, `dotnetcore2.0`, `dotnetcore2.1`, `dotnetcore3.1`, `dotnet6`, `dotnet8`, `dotnet10`, `nodejs4.3-edge`, `go1.x`, `ruby2.5`, `ruby2.7`, `ruby3.2`, `ruby3.3`, `ruby3.4`, `ruby4.0`, `provided`, `provided.al2`, `provided.al2023`, `nodejs26.x`, `python3.15`, `java8.al2023`, `java11.al2023`, `java17.al2023`

### `DeadLetterConfig` — DeadLetterConfig

A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).

### `KMSKeyArn` — string

The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:

- The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
- The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
- When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see  [Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
- The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).

If you don't provide a customer managed key, Lambda uses an [Amazon Web Services owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).

### `TracingConfig` — TracingConfig

Set `Mode` to `Active` to sample and trace a subset of incoming requests with [X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html).

### `RevisionId` — string

Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.

### `Layers` — list<string>

A list of [function layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) to add to the function's execution environment. Specify each layer by its ARN, including the version.

### `FileSystemConfigs` — list<FileSystemConfig>

Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.

### `ImageConfig` — ImageConfig

[Container image configuration values](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms) that override the values in the container image Docker file.

### `EphemeralStorage` — EphemeralStorage

The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).

### `SnapStart` — SnapStart

The function's [SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.

### `LoggingConfig` — LoggingConfig

The function's Amazon CloudWatch Logs configuration settings.

### `CapacityProviderConfig` — CapacityProviderConfig

Configuration for the capacity provider that manages compute resources for Lambda functions.

### `DurableConfig` — DurableConfig

Configuration settings for [durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.

## Output (`FunctionConfiguration`)

### `FunctionName` — string

The name of the function.

### `FunctionArn` — string

The function's Amazon Resource Name (ARN).

### `Runtime` — Runtime (enum)

The identifier of the function's  [runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.

The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).

Values: `nodejs`, `nodejs4.3`, `nodejs6.10`, `nodejs8.10`, `nodejs10.x`, `nodejs12.x`, `nodejs14.x`, `nodejs16.x`, `nodejs18.x`, `nodejs20.x`, `nodejs22.x`, `nodejs24.x`, `java8`, `java8.al2`, `java11`, `java17`, `java21`, `java25`, `python2.7`, `python3.6`, `python3.7`, `python3.8`, `python3.9`, `python3.10`, `python3.11`, `python3.12`, `python3.13`, `python3.14`, `dotnetcore1.0`, `dotnetcore2.0`, `dotnetcore2.1`, `dotnetcore3.1`, `dotnet6`, `dotnet8`, `dotnet10`, `nodejs4.3-edge`, `go1.x`, `ruby2.5`, `ruby2.7`, `ruby3.2`, `ruby3.3`, `ruby3.4`, `ruby4.0`, `provided`, `provided.al2`, `provided.al2023`, `nodejs26.x`, `python3.15`, `java8.al2023`, `java11.al2023`, `java17.al2023`

### `Role` — string

The function's execution role.

### `Handler` — string

The function that Lambda calls to begin running your function.

### `CodeSize` — long · default `0`

The size of the function's deployment package, in bytes.

### `Description` — string

The function's description.

### `Timeout` — integer

The amount of time in seconds that Lambda allows a function to run before stopping it.

### `MemorySize` — integer

The amount of memory available to the function at runtime.

### `LastModified` — string

The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

### `CodeSha256` — string

The SHA256 hash of the function's deployment package.

### `Version` — string

The version of the Lambda function.

### `VpcConfig` — VpcConfigResponse

The function's networking configuration.

### `DeadLetterConfig` — DeadLetterConfig

The function's dead letter queue.

### `Environment` — EnvironmentResponse

The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html). Omitted from CloudTrail logs.

### `KMSKeyArn` — string

The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:

- The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
- The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
- When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see  [Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
- The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).

If you don't provide a customer managed key, Lambda uses an [Amazon Web Services owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).

### `TracingConfig` — TracingConfigResponse

The function's X-Ray tracing configuration.

### `MasterArn` — string

For Lambda@Edge functions, the ARN of the main function.

### `RevisionId` — string

The latest updated revision of the function or alias.

### `Layers` — list<Layer>

The function's [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

### `State` — State (enum)

The current state of the function. When the state is `Inactive`, you can reactivate the function by invoking it.

Values: `Pending`, `Active`, `Inactive`, `Failed`, `Deactivating`, `Deactivated`, `ActiveNonInvocable`, `Deleting`

### `StateReason` — string

The reason for the function's current state.

### `StateReasonCode` — StateReasonCode (enum)

The reason code for the function's current state. When the code is `Creating`, you can't invoke or modify the function.

Values: `Idle`, `Creating`, `Restoring`, `EniLimitExceeded`, `InsufficientRolePermissions`, `InvalidConfiguration`, `InternalError`, `SubnetOutOfIPAddresses`, `InvalidSubnet`, `InvalidSecurityGroup`, `ImageDeleted`, `ImageAccessDenied`, `InvalidImage`, `KMSKeyAccessDenied`, `KMSKeyNotFound`, `InvalidStateKMSKey`, `DisabledKMSKey`, `EFSIOError`, `EFSMountConnectivityError`, `EFSMountFailure`, `EFSMountTimeout`, `InvalidRuntime`, `InvalidZipFileException`, `FunctionError`, `ServiceQuotaExceededException`, `VcpuLimitExceeded`, `CapacityProviderScalingLimitExceeded`, `InsufficientCapacity`, `EC2RequestLimitExceeded`, `FunctionError.InitTimeout`, `FunctionError.RuntimeInitError`, `FunctionError.ExtensionInitError`, `FunctionError.InvalidEntryPoint`, `FunctionError.InvalidWorkingDirectory`, `FunctionError.PermissionDenied`, `FunctionError.TooManyExtensions`, `FunctionError.InitResourceExhausted`, `DisallowedByVpcEncryptionControl`, `DrainingDurableExecutions`, `DependencyError`

### `LastUpdateStatus` — LastUpdateStatus (enum)

The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.

Values: `Successful`, `Failed`, `InProgress`

### `LastUpdateStatusReason` — string

The reason for the last update that was performed on the function.

### `LastUpdateStatusReasonCode` — LastUpdateStatusReasonCode (enum)

The reason code for the last update that was performed on the function.

Values: `EniLimitExceeded`, `InsufficientRolePermissions`, `InvalidConfiguration`, `InternalError`, `SubnetOutOfIPAddresses`, `InvalidSubnet`, `InvalidSecurityGroup`, `ImageDeleted`, `ImageAccessDenied`, `InvalidImage`, `KMSKeyAccessDenied`, `KMSKeyNotFound`, `InvalidStateKMSKey`, `DisabledKMSKey`, `EFSIOError`, `EFSMountConnectivityError`, `EFSMountFailure`, `EFSMountTimeout`, `InvalidRuntime`, `InvalidZipFileException`, `FunctionError`, `ServiceQuotaExceededException`, `VcpuLimitExceeded`, `CapacityProviderScalingLimitExceeded`, `InsufficientCapacity`, `EC2RequestLimitExceeded`, `FunctionError.InitTimeout`, `FunctionError.RuntimeInitError`, `FunctionError.ExtensionInitError`, `FunctionError.InvalidEntryPoint`, `FunctionError.InvalidWorkingDirectory`, `FunctionError.PermissionDenied`, `FunctionError.TooManyExtensions`, `FunctionError.InitResourceExhausted`, `DisallowedByVpcEncryptionControl`, `DependencyError`

### `FileSystemConfigs` — list<FileSystemConfig>

Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).

### `SigningProfileVersionArn` — string

The ARN of the signing profile version.

### `SigningJobArn` — string

The ARN of the signing job.

### `PackageType` — PackageType (enum)

The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.

Values: `Zip`, `Image`

### `ImageConfigResponse` — ImageConfigResponse

The function's image configuration values.

### `Architectures` — list<Architecture (enum)>

The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.

### `EphemeralStorage` — EphemeralStorage

The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).

### `SnapStart` — SnapStartResponse

Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).

### `RuntimeVersionConfig` — RuntimeVersionConfig

The ARN of the runtime and any errors that occured.

### `LoggingConfig` — LoggingConfig

The function's Amazon CloudWatch Logs configuration settings.

### `TenancyConfig` — TenancyConfig

The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.

### `CapacityProviderConfig` — CapacityProviderConfig

Configuration for the capacity provider that manages compute resources for Lambda functions.

### `ConfigSha256` — string

The SHA256 hash of the function configuration.

### `DurableConfig` — DurableConfig

The function's durable execution configuration settings, if the function is configured for durability.

## Errors

- `CodeSigningConfigNotFoundException` — The specified code signing configuration does not exist.
- `CodeVerificationFailedException` — The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE.
- `InvalidCodeSignatureException` — The code signature failed the integrity check.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To update a Lambda function's configuration

The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.

Input:

```json
{
  "DurableConfig": {
    "ExecutionTimeout": 3600,
    "RetentionPeriodInDays": 45
  },
  "FunctionName": "my-function",
  "MemorySize": 256
}
```

Output:

```json
{
  "CodeSha256": "PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=",
  "CodeSize": 308,
  "Description": "",
  "DurableConfig": {
    "ExecutionTimeout": 3600,
    "RetentionPeriodInDays": 45
  },
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
  "FunctionName": "my-function",
  "Handler": "index.handler",
  "LastModified": "2019-08-14T22:26:11.234+0000",
  "MemorySize": 256,
  "RevisionId": "873282ed-xmpl-4dc8-a069-d0c647e470c6",
  "Role": "arn:aws:iam::123456789012:role/lambda-role",
  "Runtime": "nodejs12.x",
  "Timeout": 3,
  "TracingConfig": {
    "Mode": "PassThrough"
  },
  "Version": "$LATEST"
}
```
