# DeleteResourceMetricsConfiguration

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteResourceMetricsConfigurationCommand` from `@aws-sdk/client-cloudwatch`

Deletes the resource metrics configuration for an Amazon Web Services resource. After
you delete the configuration, Amazon CloudWatch stops collecting detailed metrics
for the resource. Metric data that Amazon CloudWatch already collected for the
resource is not deleted.

This operation returns a `ResourceNotFoundException` if no resource metrics
configuration exists for the specified resource ARN. Verify that the resource ARN is
correct.

To delete a resource metrics configuration, you must have the
`cloudwatch:DeleteResourceMetricsConfiguration` permission. For information about scoping
this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the
*Amazon CloudWatch User Guide*.

## Input (`DeleteResourceMetricsConfigurationInput`)

### `ResourceArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon Web Services resource to delete the
resource metrics configuration for.

## Output (`DeleteResourceMetricsConfigurationOutput`)

_None._

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
