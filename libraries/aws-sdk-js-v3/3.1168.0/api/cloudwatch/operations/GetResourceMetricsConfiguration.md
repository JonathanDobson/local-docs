# GetResourceMetricsConfiguration

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetResourceMetricsConfigurationCommand` from `@aws-sdk/client-cloudwatch`

Retrieves the current resource metrics configuration for an Amazon Web Services
resource. The response includes the resource ARN, any metric selections, and the times
at which the configuration was created and last updated.

This operation returns a `ResourceNotFoundException` if no resource metrics
configuration exists for the specified resource ARN. To create a configuration, use [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html).

To retrieve a resource metrics configuration, you must have the
`cloudwatch:GetResourceMetricsConfiguration` permission. For information
about scoping this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the
*Amazon CloudWatch User Guide*.

## Input (`GetResourceMetricsConfigurationInput`)

### `ResourceArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon Web Services resource to retrieve the
resource metrics configuration for.

## Output (`GetResourceMetricsConfigurationOutput`)

### `ResourceMetricsConfiguration` — ResourceMetricsConfiguration · **required**

The resource metrics configuration for the specified resource.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
