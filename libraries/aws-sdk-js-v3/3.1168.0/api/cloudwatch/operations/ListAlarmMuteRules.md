# ListAlarmMuteRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListAlarmMuteRulesCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Lists alarm mute rules in your Amazon Web Services account and region.

You can filter the results by alarm name to find all mute rules targeting a specific
alarm, or by status to find rules that are scheduled, active, or expired.

This operation supports pagination for accounts with many mute rules. Use the
`MaxRecords` and `NextToken` parameters to retrieve results in
multiple calls.

**Permissions**

To list mute rules, you need the `cloudwatch:ListAlarmMuteRules`
permission.

## Input (`ListAlarmMuteRulesInput`)

### `AlarmName` — string

Filter results to show only mute rules that target the specified alarm
name.

### `Statuses` — list<AlarmMuteRuleStatus (enum)>

Filter results to show only mute rules with the specified statuses. Valid values
are `SCHEDULED`, `ACTIVE`, or `EXPIRED`.

### `MaxRecords` — integer

The maximum number of mute rules to return in one call. The default is
50.

### `NextToken` — string

The token returned from a previous call to indicate where to continue retrieving
results.

## Output (`ListAlarmMuteRulesOutput`)

### `AlarmMuteRuleSummaries` — list<AlarmMuteRuleSummary>

A list of alarm mute rule summaries.

### `NextToken` — string

The token to use when requesting the next set of results. If this field is absent,
there are no more results to retrieve.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
- `ResourceNotFoundException` — The named resource does not exist.
