# DeleteMetricDataQueryDefinition

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteMetricDataQueryDefinitionCommand` from `@aws-sdk/client-cloudwatch`

Deletes a metric data query definition.

This operation is idempotent. If the definition doesn't exist, the operation succeeds
without returning an error.

**Permissions**

To delete a definition, you need the
`cloudwatch:DeleteMetricDataQueryDefinition` permission on the metric
data query definition resource. You can use the `aws:ResourceTag/${TagKey}`
condition key to control access based on the tags of the definition.

## Input (`DeleteMetricDataQueryDefinitionInput`)

### `Id` — string · **required**

The ID of the metric data query definition to delete.

## Output (`DeleteMetricDataQueryDefinitionOutput`)

_None._
