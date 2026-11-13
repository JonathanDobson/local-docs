# UpdateResourceMetricsConfiguration

Service: Amazon CloudWatch · SDK for JavaScript v3: `UpdateResourceMetricsConfigurationCommand` from `@aws-sdk/client-cloudwatch`

Updates the resource metrics configuration for an Amazon Web Services resource. The
`MetricSelections` value that you provide replaces any existing metric
selections for the resource; it is not merged with them.

If you omit `MetricSelections`, Amazon CloudWatch removes any existing
metric selection filter and collects all available detailed metrics for the
resource.

This operation returns a `ResourceNotFoundException` if no resource metrics
configuration exists for the specified resource ARN. To create a configuration, use
[CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html).

To update a resource metrics configuration, you must have the
`cloudwatch:UpdateResourceMetricsConfiguration` permission. For information about scoping
this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the
*Amazon CloudWatch User Guide*.

## Input (`UpdateResourceMetricsConfigurationInput`)

### `ResourceArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon Web Services resource to update the
resource metrics configuration for.

### `MetricSelections` — list<ResourceMetricSelection>

Specifies which metrics Amazon CloudWatch collects for the resource. The selections
that you provide completely replace any existing metric selections.

If you omit this parameter, Amazon CloudWatch removes any existing metric selection
filter and collects all available detailed metrics for the resource.

## Output (`UpdateResourceMetricsConfigurationOutput`)

### `ResourceMetricsConfiguration` — ResourceMetricsConfiguration · **required**

The resource metrics configuration after the update was applied.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
