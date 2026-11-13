# CreateResourceMetricsConfiguration

Service: Amazon CloudWatch · SDK for JavaScript v3: `CreateResourceMetricsConfigurationCommand` from `@aws-sdk/client-cloudwatch`

Creates a resource metrics configuration for an Amazon Web Services resource. After you
create a configuration, Amazon CloudWatch collects detailed metrics for that
resource.

Each Amazon Web Services resource can have only one resource metrics configuration. If a
configuration already exists for the specified resource ARN, this operation returns a
`ConflictException`. To modify an existing configuration, use [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html).

If the Amazon Web Services resource that you specify in `ResourceArn` does
not exist, this operation returns a `ResourceNotFoundException`. Verify that
the resource ARN is correct and that the resource exists before you retry the
request.

To create a resource metrics configuration, you must have the
`cloudwatch:CreateResourceMetricsConfiguration` permission. For information about scoping
this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the
*Amazon CloudWatch User Guide*.

## Input (`CreateResourceMetricsConfigurationInput`)

### `ResourceArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon Web Services resource to enable detailed
monitoring for.

### `MetricSelections` — list<ResourceMetricSelection>

Specifies which metrics Amazon CloudWatch collects for the resource. If you omit
this parameter, Amazon CloudWatch collects all available detailed metrics for the
resource.

## Output (`CreateResourceMetricsConfigurationOutput`)

### `ResourceMetricsConfiguration` — ResourceMetricsConfiguration · **required**

The resource metrics configuration that was created by this operation.

## Errors

- `ConflictException` — This operation attempted to create a resource that already exists.
- `ResourceNotFoundException` — The named resource does not exist.
