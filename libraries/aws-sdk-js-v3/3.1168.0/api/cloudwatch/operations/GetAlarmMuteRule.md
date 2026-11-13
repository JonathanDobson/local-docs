# GetAlarmMuteRule

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetAlarmMuteRuleCommand` from `@aws-sdk/client-cloudwatch`

Retrieves details for a specific alarm mute rule.

This operation returns complete information about the mute rule, including its
configuration, status, targeted alarms, and metadata.

The returned status indicates the current state of the mute rule:

- **SCHEDULED**: The mute rule is configured and
  will become active in the future
- **ACTIVE**: The mute rule is currently muting
  alarm actions
- **EXPIRED**: The mute rule has passed its
  expiration date and will no longer become active

**Permissions**

To retrieve details for a mute rule, you need the
`cloudwatch:GetAlarmMuteRule` permission on the alarm mute rule
resource.

## Input (`GetAlarmMuteRuleInput`)

### `AlarmMuteRuleName` — string · **required**

The name of the alarm mute rule to retrieve.

## Output (`GetAlarmMuteRuleOutput`)

### `Name` — string

The name of the alarm mute rule.

### `AlarmMuteRuleArn` — string

The Amazon Resource Name (ARN) of the alarm mute rule.

### `Description` — string

The description of the alarm mute rule.

### `Rule` — Rule

The configuration that defines when and how long alarms are muted.

### `MuteTargets` — MuteTargets

Specifies which alarms this rule applies to.

### `StartDate` — timestamp

The date and time when the mute rule becomes active. If not set, the rule is active
immediately.

### `ExpireDate` — timestamp

The date and time when the mute rule expires and is no longer evaluated.

### `Status` — AlarmMuteRuleStatus (enum)

The current status of the alarm mute rule. Valid values are `SCHEDULED`,
`ACTIVE`, or `EXPIRED`.

Values: `SCHEDULED`, `ACTIVE`, `EXPIRED`

### `LastUpdatedTimestamp` — timestamp

The date and time when the mute rule was last updated.

### `MuteType` — string

Indicates whether the mute rule is one-time or recurring. Valid values are
`ONE_TIME` or `RECURRING`.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
