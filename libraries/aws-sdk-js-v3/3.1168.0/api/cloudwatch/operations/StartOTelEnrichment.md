# StartOTelEnrichment

Service: Amazon CloudWatch · SDK for JavaScript v3: `StartOTelEnrichmentCommand` from `@aws-sdk/client-cloudwatch`

Enables enrichment and PromQL access for CloudWatch vended metrics for [supported Amazon Web Services resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html) in the account. Once enabled,
metrics that contain a resource identifier dimension (for example, EC2
`CPUUtilization` with an `InstanceId` dimension) are enriched
with resource ARN and resource tag labels and become queryable using PromQL.

Before calling this operation, you must enable resource tags on telemetry for your
account. For more information, see [Enable
resource tags on telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EnableResourceTagsOnTelemetry.html).

Optionally, `IncludeFilters` and `ExcludeFilters` limit
enrichment to a subset of the account's metrics. These filters are stored only when this
operation starts enrichment. Calling `StartOTelEnrichment` for an account
where enrichment is already running has no effect and does not modify the filters that
are applied. To change them, use [UpdateOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html).

## Input (`StartOTelEnrichmentInput`)

### `IncludeFilters` — list<OTelEnrichmentMetricSelector>

The metric namespaces, and the metric names, to enrich. If this parameter is
omitted, every namespace that Amazon CloudWatch supports for enrichment is in
scope.

A maximum of 100 filters is allowed across `IncludeFilters` and
`ExcludeFilters` combined.

### `ExcludeFilters` — list<OTelEnrichmentMetricSelector>

The metric namespaces, and the metric names, to leave unenriched. If this parameter
is omitted, nothing is excluded.

Amazon CloudWatch applies `ExcludeFilters` after
`IncludeFilters`, so a metric that both parameters match is not
enriched.

A maximum of 100 filters is allowed across `IncludeFilters` and
`ExcludeFilters` combined.

## Output (`StartOTelEnrichmentOutput`)

### `IncludeFilters` — list<OTelEnrichmentMetricSelector>

The include filters that are stored for the account.

### `ExcludeFilters` — list<OTelEnrichmentMetricSelector>

The exclude filters that are stored for the account.

### `CreatedAt` — timestamp

The date and time that enrichment started for the account.

### `UpdatedAt` — timestamp

The date and time that the enrichment configuration for the account was last
stored.

## Errors

- `ValidationException` — The request failed validation.
