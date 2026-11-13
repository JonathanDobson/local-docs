# UpdateOTelEnrichment

Service: Amazon CloudWatch · SDK for JavaScript v3: `UpdateOTelEnrichmentCommand` from `@aws-sdk/client-cloudwatch`

Replaces the filters that determine which CloudWatch vended metrics are enriched
with resource ARN and resource tag labels for the account. Enrichment must already be
running for the account. If it is not, this operation returns a
`ResourceNotFoundException`. To start enrichment, use [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html).

The filters in the request completely replace the stored filters; they are not
merged with them. `IncludeFilters` and `ExcludeFilters` are
replaced as a pair, so a request that specifies only `IncludeFilters` also
clears the stored `ExcludeFilters`, and a request that specifies neither
clears both.

## Input (`UpdateOTelEnrichmentInput`)

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

## Output (`UpdateOTelEnrichmentOutput`)

### `IncludeFilters` — list<OTelEnrichmentMetricSelector>

The include filters that are stored for the account after the replacement. This
parameter is omitted when the request cleared the include filters, which means that
every supported namespace is in scope.

### `ExcludeFilters` — list<OTelEnrichmentMetricSelector>

The exclude filters that are stored for the account after the replacement. This
parameter is omitted when the request cleared the exclude filters, which means that
nothing is excluded.

### `CreatedAt` — timestamp

The date and time that enrichment started for the account.

### `UpdatedAt` — timestamp

The date and time that the enrichment configuration for the account was last
stored.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
- `ValidationException` — The request failed validation.
