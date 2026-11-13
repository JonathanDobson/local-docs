# SetAlarmState

Service: Amazon CloudWatch · SDK for JavaScript v3: `SetAlarmStateCommand` from `@aws-sdk/client-cloudwatch`

Temporarily sets the state of an alarm for testing purposes. When the updated state
differs from the previous value, the action configured for the appropriate state is
invoked. For example, if your alarm is configured to send an Amazon SNS message when an
alarm is triggered, temporarily changing the alarm state to `ALARM` sends an
SNS message.

Metric alarms returns to their actual state quickly, often within seconds. Because
the metric alarm state change happens quickly, it is typically only visible in the
alarm's **History** tab in the Amazon CloudWatch console or
through [DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html).

If you use `SetAlarmState` on a composite alarm, the composite alarm is
not guaranteed to return to its actual state. It returns to its actual state only once
any of its children alarms change state. It is also reevaluated if you update its
configuration.

If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling
policies, you must include information in the `StateReasonData` parameter to
enable the policy to take the correct action.

## Input (`SetAlarmStateInput`)

### `AlarmName` — string · **required**

The name of the alarm.

### `StateValue` — StateValue (enum) · **required**

The value of the state.

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

### `StateReason` — string · **required**

The reason that this alarm is set to this specific state, in text format.

### `StateReasonData` — string

The reason that this alarm is set to this specific state, in JSON format.

For SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling
or application Auto Scaling alarm actions, the Auto Scaling policy uses the information
in this field to take the correct action.

## Output (`Unit`)

_None._

## Errors

- `InvalidFormatFault` — Data was not syntactically valid JSON.
- `ResourceNotFound` — The named resource does not exist.
