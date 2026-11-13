# ListDashboards

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListDashboardsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Returns a list of the dashboards for your account. If you include
`DashboardNamePrefix`, only those dashboards with names starting with the
prefix are listed. Otherwise, all dashboards in your account are listed.

`ListDashboards` returns up to 1000 results on one page. If there are
more than 1000 dashboards, you can call `ListDashboards` again and include
the value you received for `NextToken` in the first call, to receive the next
1000 results.

You might have recently enabled an [opt-in Region (Region that is disabled by default)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) for your account. In
that Region, `ListDashboards` can return an access denied error for up to 24
hours after you enable the Region. This delay occurs while dashboard data propagates.
The error does not
indicate a problem with your permissions. Because dashboards are global, you can call
`ListDashboards` in any other enabled Region, or retry after propagation
completes.

## Input (`ListDashboardsInput`)

### `DashboardNamePrefix` — string

If you specify this parameter, only the dashboards with names starting with the
specified string are listed. The maximum length is 255, and valid characters are A-Z,
a-z, 0-9, ".", "-", and "\_".

### `NextToken` — string

The token returned by a previous call to indicate that there is more data
available.

## Output (`ListDashboardsOutput`)

### `DashboardEntries` — list<DashboardEntry>

The list of matching dashboards.

### `NextToken` — string

The token that marks the start of the next batch of returned results.

## Errors

- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
