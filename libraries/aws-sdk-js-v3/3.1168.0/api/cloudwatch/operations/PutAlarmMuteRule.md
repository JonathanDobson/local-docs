# PutAlarmMuteRule

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutAlarmMuteRuleCommand` from `@aws-sdk/client-cloudwatch`

Creates or updates an alarm mute rule.

Alarm mute rules automatically mute alarm actions during predefined time windows. When
a mute rule is active, targeted alarms continue to evaluate metrics and transition
between states, but their configured actions (such as Amazon SNS notifications
or Auto Scaling actions) are muted.

You can create mute rules with recurring schedules using `cron` expressions
or one-time mute windows using `at` expressions. Each mute rule can target up
to 100 specific alarms by name.

If you specify a rule name that already exists, this operation updates the existing
rule with the new configuration.

**Permissions**

To create or update a mute rule, you must have the
`cloudwatch:PutAlarmMuteRule` permission on two types of resources: the
alarm mute rule resource itself, and each alarm that the rule targets.

For example, If you want to allow a user to create mute rules that target only
specific alarms named "WebServerCPUAlarm" and "DatabaseConnectionAlarm", you would
create an IAM policy with one statement granting
`cloudwatch:PutAlarmMuteRule` on the alarm mute rule resource
(`arn:aws:cloudwatch:[REGION]:123456789012:alarm-mute-rule:*`), and
another statement granting `cloudwatch:PutAlarmMuteRule` on the targeted
alarm resources
(`arn:aws:cloudwatch:[REGION]:123456789012:alarm:WebServerCPUAlarm` and
`arn:aws:cloudwatch:[REGION]:123456789012:alarm:DatabaseConnectionAlarm`).

You can also use IAM policy conditions to allow targeting alarms based on resource
tags. For example, you can restrict users to create/update mute rules to only target
alarms that have a specific tag key-value pair, such as `Team=TeamA`.

## Input (`PutAlarmMuteRuleInput`)

### `Name` — string · **required**

The name of the alarm mute rule. This name must be unique within your Amazon Web Services account and region.

### `Description` — string

A description of the alarm mute rule that helps you identify its purpose.

### `Rule` — Rule · **required**

The configuration that defines when and how long alarms should be muted.

### `MuteTargets` — MuteTargets

Specifies which alarms this rule applies to.

### `Tags` — list<Tag>

A list of key-value pairs to associate with the alarm mute rule. You can use tags
to categorize and manage your mute rules.

### `StartDate` — timestamp

The date and time after which the mute rule takes effect, specified as a timestamp
in ISO 8601 format (for example, `2026-04-15T08:00:00Z`). If not specified,
the mute rule takes effect immediately upon creation and the mutes are applied as per
the schedule expression.

### `ExpireDate` — timestamp

The date and time when the mute rule expires and is no longer evaluated, specified
as a timestamp in ISO 8601 format (for example, `2026-12-31T23:59:59Z`).
After this time, the rule status becomes EXPIRED and will no longer mute the targeted
alarms.

## Output (`Unit`)

_None._

## Errors

- `LimitExceededFault` — The quota for alarms for this customer has already been reached.
