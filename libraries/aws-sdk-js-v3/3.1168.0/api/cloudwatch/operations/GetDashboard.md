# GetDashboard

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetDashboardCommand` from `@aws-sdk/client-cloudwatch`

Displays the details of the dashboard that you specify.

To copy an existing dashboard, use `GetDashboard`, and then use the data
returned within `DashboardBody` as the template for the new dashboard when
you call `PutDashboard` to create the copy.

You might have recently enabled an [opt-in Region (Region that is disabled by default)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) for your account. In
that Region, `GetDashboard` can return an access denied error for up to 24
hours after you enable the Region. This delay occurs while dashboard data propagates.
The error does not
indicate a problem with your permissions. Because dashboards are global, you can call
`GetDashboard` in any other enabled Region, or retry after propagation
completes.

## Input (`GetDashboardInput`)

### `DashboardName` — string · **required**

The name of the dashboard to be described.

## Output (`GetDashboardOutput`)

### `DashboardArn` — string

The Amazon Resource Name (ARN) of the dashboard.

### `DashboardBody` — string

The detailed information about the dashboard, including what widgets are included
and their location on the dashboard. For more information about the
`DashboardBody` syntax, see [Dashboard Body Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Dashboard-Body-Structure.html).

### `DashboardName` — string

The name of the dashboard.

## Errors

- `DashboardNotFoundError` — The specified dashboard does not exist.
- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
