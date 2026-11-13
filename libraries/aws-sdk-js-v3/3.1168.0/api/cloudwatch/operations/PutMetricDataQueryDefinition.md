# PutMetricDataQueryDefinition

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutMetricDataQueryDefinitionCommand` from `@aws-sdk/client-cloudwatch`

Creates or updates a metric data query definition.

A metric data query definition saves a metric query so that you can reuse it later.
It includes the query expression, the query language, and a path that names the
definition and can organize it into folders. When you save a definition,
CloudWatch doesn't validate or run its expression.

To create a definition, omit `Id`. CloudWatch generates the ID and
returns it. To update a definition, specify its `Id`. An update replaces the
path, expression, and type, and keeps the creation time.

The path must be unique in your account and Region. If another definition already
uses the path, the request fails with a `ConflictException`.

You can have up to 1,000 metric data query definitions in each Region of your
account. A request that would create more fails with a
`LimitExceededException`.

**Permissions**

To create or update a definition, you need the
`cloudwatch:PutMetricDataQueryDefinition` permission on the metric data
query definition resource. The resource ARN has the format
`arn:aws:cloudwatch:Region:account-id:metric-query-definition/Id`.

To add tags when you create a definition, you also need the
`cloudwatch:TagResource` permission. You can use the
`aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys
to control which tags can be added.

## Input (`PutMetricDataQueryDefinitionInput`)

### `Id` — string

The ID of the metric data query definition to update. Omit this parameter to
create a definition. CloudWatch then generates the ID and returns it in the
response.

### `Path` — string · **required**

The name of the metric data query definition. Use slashes (`/`) to
organize definitions into folders, for example `team/web/latency`. The path
must meet the following requirements:

- It must be unique in your account and Region.
- It can't start or end with a slash.
- It can't contain an empty folder name (`//`).
- It can be at most 1,015 bytes when encoded as UTF-8.

### `Expression` — string · **required**

The query expression, in the language that `Type` specifies.
CloudWatch doesn't validate or run the expression when you save it.

### `Type` — QueryType (enum) · **required**

The language of the expression. Valid values are the following:

- `PROMQL` – A PromQL query.
- `SQL` – A CloudWatch Metrics Insights query.
- `METRIC_MATH` – A metric math expression.

Values: `PROMQL`, `SQL`, `METRIC_MATH`

### `Tags` — list<Tag>

A list of key-value pairs to associate with the metric data query definition. You
can use tags to categorize definitions and to control access to them. Tags are applied
only when the request creates a definition, that is, when you omit `Id`. To
change the tags of an existing definition, use `TagResource` and
`UntagResource`.

## Output (`PutMetricDataQueryDefinitionOutput`)

### `Id` — string · **required**

The ID of the metric data query definition.

### `Arn` — string · **required**

The Amazon Resource Name (ARN) of the metric data query definition.

### `Path` — string · **required**

The path of the metric data query definition.

### `Expression` — string · **required**

The query expression.

### `Type` — QueryType (enum) · **required**

The language of the expression.

Values: `PROMQL`, `SQL`, `METRIC_MATH`

### `CreatedAt` — timestamp · **required**

The date and time when you created the metric data query definition.

### `UpdatedAt` — timestamp · **required**

The date and time when you last updated the metric data query
definition.

## Errors

- `ConflictException` — This operation attempted to create a resource that already exists.
- `LimitExceededException` — The operation exceeded one or more limits.
- `ResourceNotFoundException` — The named resource does not exist.
