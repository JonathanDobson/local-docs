# UpdateFunctionCode

Service: AWS Lambda · SDK for JavaScript v3: `UpdateFunctionCodeCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2015-03-31/functions/{FunctionName}/code`

Updates a Lambda Event Function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see [Configuring code signing for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html).

If the function's package type is `Image`, then you must specify the code package in `ImageUri` as the URI of a [container image](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html) in the Amazon ECR registry.

If the function's package type is `Zip`, then you must specify the deployment package as a [.zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip). Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the `ZipFile` field.

The code in the deployment package must be compatible with the target instruction set architecture of the function (`x86-64` or `arm64`).

The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version.

For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.

## Input (`UpdateFunctionCodeRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `ZipFile` — blob

The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.

### `S3Bucket` — string

An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account. Use only with a function defined with a .zip file archive deployment package.

### `S3Key` — string

The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.

### `S3ObjectVersion` — string

For versioned objects, the version of the deployment package object to use.

### `S3ObjectStorageMode` — S3ObjectStorageMode (enum)

Specifies how the deployment package is stored. Valid values:

- `COPY` (default) – Uploads a copy of your deployment package to Lambda.
- `REFERENCE` – Lambda references the deployment package from the specified Amazon S3 bucket.

Values: `COPY`, `REFERENCE`

### `ImageUri` — string

URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.

### `Architectures` — list<Architecture (enum)>

The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86\_64). The default value is `x86_64`.

### `Publish` — boolean · default `false`

Set to true to publish a new version of the function after updating the code. This has the same effect as calling PublishVersion separately.

### `PublishTo` — FunctionVersionLatestPublished (enum)

Specifies where to publish the function version or configuration.

Values: `LATEST_PUBLISHED`

### `DryRun` — boolean · default `false`

Set to true to validate the request parameters and access permissions without modifying the function code.

### `RevisionId` — string

Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.

### `SourceKMSKeyArn` — string

The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an Amazon Web Services managed key.

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
- `CodeStorageExceededException` — Your Amazon Web Services account has exceeded its maximum total code size.
- `CodeVerificationFailedException` — The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE.
- `InvalidCodeSignatureException` — The code signature failed the integrity check.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To update a Lambda function's code

The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.

Input:

```json
{
  "FunctionName": "my-function",
  "S3Bucket": "my-bucket-1xpuxmplzrlbh",
  "S3Key": "function.zip"
}
```

Output:

```json
{
  "CodeSha256": "PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=",
  "CodeSize": 308,
  "Description": "",
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
  "FunctionName": "my-function",
  "Handler": "index.handler",
  "LastModified": "2019-08-14T22:26:11.234+0000",
  "MemorySize": 128,
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
