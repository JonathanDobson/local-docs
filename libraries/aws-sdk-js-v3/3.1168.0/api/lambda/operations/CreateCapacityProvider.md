# CreateCapacityProvider

Service: AWS Lambda · SDK for JavaScript v3: `CreateCapacityProviderCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2025-11-30/capacity-providers`

Creates a capacity provider that manages compute resources for Lambda Event Functions

## Input (`CreateCapacityProviderRequest`)

### `CapacityProviderName` — string · **required**

The name of the capacity provider.

### `VpcConfig` — CapacityProviderVpcConfig · **required**

The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.

### `PermissionsConfig` — CapacityProviderPermissionsConfig · **required**

The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.

### `InstanceRequirements` — InstanceRequirements

The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.

### `CapacityProviderScalingConfig` — CapacityProviderScalingConfig

The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.

### `KmsKeyArn` — string

The ARN of the KMS key used to encrypt data associated with the capacity provider.

### `Tags` — map<string, string>

A list of tags to associate with the capacity provider.

### `PropagateTags` — PropagateTags

The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.

### `TelemetryConfig` — CapacityProviderTelemetryConfig

The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.

## Output (`CreateCapacityProviderResponse`)

### `CapacityProvider` — CapacityProvider · **required**

Information about the capacity provider that was created.

## Errors

- `CapacityProviderLimitExceededException` — The maximum number of capacity providers for your account has been exceeded.
- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
