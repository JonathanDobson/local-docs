# GetMetricDataQueryDefinition

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetMetricDataQueryDefinitionCommand` from `@aws-sdk/client-cloudwatch`

Returns a metric data query definition, including its expression.

**Permissions**

To get a definition, you need the
`cloudwatch:GetMetricDataQueryDefinition` permission on the metric data
query definition resource. You can use the `aws:ResourceTag/${TagKey}`
condition key to control access based on the tags of the definition.

## Input (`GetMetricDataQueryDefinitionInput`)

### `Id` — string · **required**

The ID of the metric data query definition to retrieve.

## Output (`GetMetricDataQueryDefinitionOutput`)

### `Id` — string · **required**

The ID of the metric data query definition.

### `Arn` — string · **required**

The Amazon Resource Name (ARN) of the metric data query definition.

### `Path` — string · **required**

The path of the metric data query definition.

### `Expression` — string · **required**

The query expression.

### `Type` — QueryType (enum) · **required**

The language of the expression. Valid values are the following:

- `PROMQL` – A PromQL query.
- `SQL` – A CloudWatch Metrics Insights query.
- `METRIC_MATH` – A metric math expression.

Values: `PROMQL`, `SQL`, `METRIC_MATH`

### `CreatedAt` — timestamp · **required**

The date and time when you created the metric data query definition.

### `UpdatedAt` — timestamp · **required**

The date and time when you last updated the metric data query
definition.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
