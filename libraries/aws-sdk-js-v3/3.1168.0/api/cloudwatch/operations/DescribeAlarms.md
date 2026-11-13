# DescribeAlarms

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeAlarmsCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Retrieves the specified alarms. You can filter the results by specifying a prefix
for the alarm name, the alarm state, or a prefix for any action.

To use this operation and return information about composite alarms, you must be
signed on with the `cloudwatch:DescribeAlarms` permission that is scoped to
`*`. You can't return information about composite alarms if your
`cloudwatch:DescribeAlarms` permission has a narrower scope.

## Input (`DescribeAlarmsInput`)

### `AlarmNames` — list<string>

The names of the alarms to retrieve information about.

### `AlarmNamePrefix` — string

An alarm name prefix. If you specify this parameter, you receive information about
all alarms that have names that start with this prefix.

If this parameter is specified, you cannot specify
`AlarmNames`.

### `AlarmTypes` — list<AlarmType (enum)>

Use this parameter to specify whether you want the operation to return metric alarms,
composite alarms, or log alarms. If you omit this parameter, only metric alarms are
returned, even if composite alarms or log alarms exist in the account.

For example, if you omit this parameter or specify `MetricAlarms`, the
operation returns only a list of metric alarms. It does not return any composite alarms
or log alarms, even if they exist in the account.

If you specify `CompositeAlarms`, the operation returns only a list of
composite alarms, and does not return any metric alarms or log alarms.

If you specify `LogAlarms`, the operation returns only a list of log
alarms, and does not return any metric alarms or composite alarms.

### `ChildrenOfAlarmName` — string

If you use this parameter and specify the name of a composite alarm, the operation
returns information about the "children" alarms of the alarm you specify. These are the
metric alarms and composite alarms referenced in the `AlarmRule` field of the
composite alarm that you specify in `ChildrenOfAlarmName`. Information about
the composite alarm that you name in `ChildrenOfAlarmName` is not
returned.

If you specify `ChildrenOfAlarmName`, you cannot specify any other
parameters in the request except for `MaxRecords` and `NextToken`.
If you do so, you receive a validation error.

Only the `Alarm Name`, `ARN`, `StateValue`
(OK/ALARM/INSUFFICIENT\_DATA), and `StateUpdatedTimestamp` information are
returned by this operation when you use this parameter. To get complete information
about these alarms, perform another `DescribeAlarms` operation and
specify the parent alarm names in the `AlarmNames` parameter.

### `ParentsOfAlarmName` — string

If you use this parameter and specify the name of a metric or composite alarm, the
operation returns information about the "parent" alarms of the alarm you specify. These
are the composite alarms that have `AlarmRule` parameters that reference the
alarm named in `ParentsOfAlarmName`. Information about the alarm that you
specify in `ParentsOfAlarmName` is not returned.

If you specify `ParentsOfAlarmName`, you cannot specify any other
parameters in the request except for `MaxRecords` and `NextToken`.
If you do so, you receive a validation error.

Only the Alarm Name and ARN are returned by this operation when you use this
parameter. To get complete information about these alarms, perform another
`DescribeAlarms` operation and specify the parent alarm names in the
`AlarmNames` parameter.

### `StateValue` — StateValue (enum)

Specify this parameter to receive information only about alarms that are currently
in the state that you specify.

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

### `ActionPrefix` — string

Use this parameter to filter the results of the operation to only those alarms that
use a certain alarm action. For example, you could specify the ARN of an SNS topic to
find all alarms that send notifications to that topic.

### `MaxRecords` — integer

The maximum number of alarm descriptions to retrieve.

### `NextToken` — string

The token returned by a previous call to indicate that there is more data
available.

## Output (`DescribeAlarmsOutput`)

### `CompositeAlarms` — list<CompositeAlarm>

The information about any composite alarms returned by the operation.

### `MetricAlarms` — list<MetricAlarm>

The information about any metric alarms returned by the operation.

### `LogAlarms` — list<LogAlarm>

The information about any log alarms returned by the operation.

### `NextToken` — string

The token that marks the start of the next batch of returned results.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
