# DeleteDashboards

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteDashboardsCommand` from `@aws-sdk/client-cloudwatch`

Deletes all dashboards that you specify. You can specify up to 100 dashboards to
delete. If there is an error during this call, the operation attempts to delete as many
dashboards as possible.

## Input (`DeleteDashboardsInput`)

### `DashboardNames` — list<string> · **required**

The dashboards to be deleted. This parameter is required.

## Output (`DeleteDashboardsOutput`)

_None._

## Errors

- `ConflictException` — This operation attempted to create a resource that already exists.
- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
