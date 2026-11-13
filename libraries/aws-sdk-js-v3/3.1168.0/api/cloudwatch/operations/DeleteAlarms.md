# DeleteAlarms

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteAlarmsCommand` from `@aws-sdk/client-cloudwatch`

Deletes the specified alarms. You can delete up to 100 alarms in one operation.
However, this total can include no more than one composite alarm. For example, you could
delete 99 metric alarms and one composite alarms with one operation, but you can't
delete two composite alarms with one operation. Log alarms cannot be batch deleted.

If you specify any incorrect alarm names, the alarms you specify with correct
names are still deleted. Other syntax errors might result in no alarms being deleted. To
confirm that alarms were deleted successfully, you can use the [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) operation after using `DeleteAlarms`.

It is possible to create a loop or cycle of composite alarms, where composite
alarm A depends on composite alarm B, and composite alarm B also depends on
composite alarm A. In this scenario, you can't delete any composite alarm that is
part of the cycle because there is always still a composite alarm that depends on
that alarm that you want to delete.

To get out of such a situation, you must break the cycle by changing the rule of
one of the composite alarms in the cycle to remove a dependency that creates the
cycle. The simplest change to make to break a cycle is to change the
`AlarmRule` of one of the alarms to `false`.

Additionally, the evaluation of composite alarms stops if CloudWatch
detects a cycle in the evaluation path.

## Input (`DeleteAlarmsInput`)

### `AlarmNames` — list<string> · **required**

The alarms to be deleted. Do not enclose the alarm names in quote marks.

## Output (`Unit`)

_None._

## Errors

- `ResourceConflict` — The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.
- `ResourceNotFound` — The named resource does not exist.
