# DeleteAlarmMuteRule

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteAlarmMuteRuleCommand` from `@aws-sdk/client-cloudwatch`

Deletes a specific alarm mute rule.

When you delete a mute rule, any alarms that are currently being muted by that rule
are immediately unmuted. If those alarms are in an ALARM state, their configured actions
will trigger.

This operation is idempotent. If you delete a mute rule that does not exist, the
operation succeeds without returning an error.

**Permissions**

To delete a mute rule, you need the `cloudwatch:DeleteAlarmMuteRule`
permission on the alarm mute rule resource.

## Input (`DeleteAlarmMuteRuleInput`)

### `AlarmMuteRuleName` — string · **required**

The name of the alarm mute rule to delete.

## Output (`Unit`)

_None._
