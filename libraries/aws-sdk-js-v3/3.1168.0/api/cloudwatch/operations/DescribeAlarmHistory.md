# DescribeAlarmHistory

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeAlarmHistoryCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Retrieves the history for the specified alarm. You can filter the results by date
range or item type. If an alarm name is not specified, the histories for either all
metric alarms or all composite alarms are returned.

CloudWatch retains the history of an alarm even if you delete the alarm.

To use this operation and return information about a composite alarm, you must be
signed on with the `cloudwatch:DescribeAlarmHistory` permission that is
scoped to `*`. You can't return information about composite alarms if your
`cloudwatch:DescribeAlarmHistory` permission has a narrower scope.

## Input (`DescribeAlarmHistoryInput`)

### `AlarmName` — string

The name of the alarm.

### `AlarmContributorId` — string

The unique identifier of a specific alarm contributor to filter the alarm history
results.

### `AlarmTypes` — list<AlarmType (enum)>

Use this parameter to specify whether you want the operation to return metric alarms,
composite alarms, or log alarms. If you omit this parameter, only metric alarms are
returned.

### `HistoryItemType` — HistoryItemType (enum)

The type of alarm histories to retrieve.

Values: `ConfigurationUpdate`, `StateUpdate`, `Action`, `AlarmContributorStateUpdate`, `AlarmContributorAction`

### `StartDate` — timestamp

The starting date to retrieve alarm history.

### `EndDate` — timestamp

The ending date to retrieve alarm history.

### `MaxRecords` — integer

The maximum number of alarm history records to retrieve.

### `NextToken` — string

The token returned by a previous call to indicate that there is more data
available.

### `ScanBy` — ScanBy (enum)

Specified whether to return the newest or oldest alarm history first. Specify
`TimestampDescending` to have the newest event history returned first,
and specify `TimestampAscending` to have the oldest history returned
first.

Values: `TimestampDescending`, `TimestampAscending`

## Output (`DescribeAlarmHistoryOutput`)

### `AlarmHistoryItems` — list<AlarmHistoryItem>

The alarm histories, in JSON format.

### `NextToken` — string

The token that marks the start of the next batch of returned results.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
