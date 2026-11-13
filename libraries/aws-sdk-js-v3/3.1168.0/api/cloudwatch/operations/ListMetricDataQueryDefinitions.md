# ListMetricDataQueryDefinitions

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListMetricDataQueryDefinitionsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Lists the metric data query definitions in your account and Region.

The results are summaries that don't include the expression. To get the full
definition, call `GetMetricDataQueryDefinition` with its ID.

This operation supports pagination. Use the `MaxResults` and
`NextToken` parameters to retrieve results in multiple calls.

**Permissions**

To list definitions, you need the
`cloudwatch:ListMetricDataQueryDefinitions` permission. This permission
applies to all definitions in the account and Region. The results aren't filtered by
tags.

## Input (`ListMetricDataQueryDefinitionsInput`)

### `MaxResults` — integer

The maximum number of metric data query definitions to return in one call. The
default is 100.

### `NextToken` — string

The token returned by a previous call to indicate where to continue retrieving
results.

## Output (`ListMetricDataQueryDefinitionsOutput`)

### `Items` — list<MetricDataQueryDefinitionSummary> · **required**

A list of metric data query definition summaries.

### `NextToken` — string

The token to use when requesting the next set of results. If this field is absent,
there are no more results to retrieve.
