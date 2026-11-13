# PutLogAlarm

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutLogAlarmCommand` from `@aws-sdk/client-cloudwatch`

Creates or updates a log alarm. A log alarm evaluates the results of a CloudWatch Logs scheduled query against the configured threshold and comparison operator to determine its state.

When you create a log alarm, the operation creates a service-managed CloudWatch Logs scheduled query that runs the query string you provide on the schedule you configure. Each scheduled query execution returns one or more aggregated values determined by the `AggregationExpression`, and each aggregated value is compared against the alarm `Threshold` to determine the alarm state. The alarm uses M-out-of-N evaluation: if `QueryResultsToAlarm` out of the most recent `QueryResultsToEvaluate` query results breach the threshold, the alarm transitions to `ALARM`.

Log alarms support the alarm states (`OK`, `ALARM`, `INSUFFICIENT_DATA`). Configure transition actions using `OKActions`, `AlarmActions`, and `InsufficientDataActions`.

If you call this operation with the name of an existing log alarm, the operation replaces the previous configuration of that alarm.

**Permissions**

To create or update a log alarm, you must have the `cloudwatch:PutLogAlarm` permission. The IAM role specified in `ScheduledQueryRoleARN` must grant the CloudWatch Alarms service permission to execute scheduled queries on the specified log groups. If you set `ActionLogLineCount`, the role specified in `ActionLogLineRoleArn` must grant permission to retrieve log events for inclusion in alarm notifications.

## Input (`PutLogAlarmInput`)

### `AlarmName` — string · **required**

The name for the alarm. This name must be unique within the Amazon Web Services account and Region.

### `AlarmDescription` — string

The description for the alarm.

### `ScheduledQueryConfiguration` — ScheduledQueryConfiguration · **required**

The configuration of the underlying CloudWatch Logs scheduled query that this alarm evaluates, including the query string, log groups, schedule, and aggregation expression.

### `ActionLogLineCount` — integer

The number of log lines from the most recent scheduled query execution to include in alarm action notifications. Valid range is 0 through 50. The default is 0, which means no log lines are included.

### `ActionLogLineRoleArn` — string

The Amazon Resource Name (ARN) of an IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Required when `ActionLogLineCount` is greater than 0.

### `ActionsEnabled` — boolean

Indicates whether actions should be executed during any changes to the alarm state. The default is `true`.

### `OKActions` — list<string>

The actions to execute when this alarm transitions to the `OK` state
from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values:

**Amazon SNS actions:**

`arn:aws:sns:region:account-id:sns-topic-name`

**Lambda actions:**

- Invoke the latest version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name`
- Invoke a specific version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:version-number`
- Invoke a function by using an alias Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:alias-name`

### `AlarmActions` — list<string>

The actions to execute when this alarm transitions to the `ALARM` state
from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values:

**Amazon SNS actions:**

`arn:aws:sns:region:account-id:sns-topic-name`

**Lambda actions:**

- Invoke the latest version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name`
- Invoke a specific version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:version-number`
- Invoke a function by using an alias Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:alias-name`

**Systems Manager actions:**

`arn:aws:ssm:region:account-id:opsitem:severity`

### `InsufficientDataActions` — list<string>

The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state
from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values:

**Amazon SNS actions:**

`arn:aws:sns:region:account-id:sns-topic-name`

**Lambda actions:**

- Invoke the latest version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name`
- Invoke a specific version of a Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:version-number`
- Invoke a function by using an alias Lambda function:
  `arn:aws:lambda:region:account-id:function:function-name:alias-name`

### `QueryResultsToEvaluate` — integer · **required**

The number of most recent scheduled query results to evaluate against the threshold (the N in M-of-N evaluation). Valid range is 1 through 100.

### `QueryResultsToAlarm` — integer · **required**

The number of query results, out of the most recent `QueryResultsToEvaluate` results, that must breach the threshold to trigger the alarm to transition to `ALARM` (the M in M-of-N evaluation). Must be less than or equal to `QueryResultsToEvaluate`.

### `Threshold` — double · **required**

The value to compare with the aggregated query result.

### `ComparisonOperator` — ComparisonOperator (enum) · **required**

The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand. Valid values are `GreaterThanThreshold`, `GreaterThanOrEqualToThreshold`, `LessThanThreshold`, and `LessThanOrEqualToThreshold`.

Values: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`, `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, `GreaterThanUpperThreshold`

### `TreatMissingData` — string

Sets how this alarm is to handle missing data points. Valid values are `breaching`, `notBreaching`, `ignore`, and `missing`. If this parameter is omitted, the default behavior of `missing` is used.

### `Tags` — list<Tag>

A list of key-value pairs to associate with the alarm. You can use tags to categorize and manage your alarms.

### `WarmUpConfiguration` — WarmUpConfiguration

The warm-up configuration for the alarm. A warm-up period delays alarm evaluation
after you create or update the alarm. The warm-up period reduces alarm noise from
missing data while a new resource or service starts publishing data.

For more information, see [Alarm warm-up
periods](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html) in the *Amazon CloudWatch User Guide*.

### `ActionConfiguration` — ActionConfiguration

Settings that change the content of the notifications and events that the alarm
sends when its state changes. These settings apply to the alarm's actions, whichever
state triggers them.

## Output (`Unit`)

_None._

## Errors

- `LimitExceededFault` — The quota for alarms for this customer has already been reached.
- `ResourceConflict` — The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.
