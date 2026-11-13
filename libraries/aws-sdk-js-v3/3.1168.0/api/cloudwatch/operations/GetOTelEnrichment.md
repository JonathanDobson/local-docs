# GetOTelEnrichment

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetOTelEnrichmentCommand` from `@aws-sdk/client-cloudwatch`

Returns the current status of vended metric enrichment for the account, including
whether CloudWatch vended metrics are enriched with resource ARN and resource tag labels
and queryable using PromQL. For the list of supported resources, see [Supported Amazon Web Services infrastructure metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html).

## Input (`GetOTelEnrichmentInput`)

_None._

## Output (`GetOTelEnrichmentOutput`)

### `Status` — OTelEnrichmentStatus (enum) · **required**

The status of OTel enrichment for the account. Valid values are
`Running` (enrichment is enabled) and `Stopped` (enrichment is
disabled).

Values: `Running`, `Stopped`

### `IncludeFilters` — list<OTelEnrichmentMetricSelector>

The metric namespaces, and the metric names, that are enriched. This parameter is
omitted when enrichment is stopped, and when enrichment is running with no include
filters, which means that every supported namespace is in scope.

### `ExcludeFilters` — list<OTelEnrichmentMetricSelector>

The metric namespaces, and the metric names, that are left unenriched. This
parameter is omitted when enrichment is stopped, and when enrichment is running with no
exclude filters, which means that nothing is excluded.

### `CreatedAt` — timestamp

The date and time that enrichment started for the account. This parameter is
omitted when enrichment is stopped.

### `UpdatedAt` — timestamp

The date and time that the enrichment configuration for the account was last
stored.
