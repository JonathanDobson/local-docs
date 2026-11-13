# PutInsightRule

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutInsightRuleCommand` from `@aws-sdk/client-cloudwatch`

Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs
log group, enabling you to find contributor data for the log events in that log group.
For more information, see [Using Contributor
Insights to Analyze High-Cardinality Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html).

If you create a rule, delete it, and then re-create it with the same name, historical
data from the first time the rule was created might not be available.

## Input (`PutInsightRuleInput`)

### `RuleName` — string · **required**

A unique name for the rule.

### `RuleState` — string

The state of the rule. Valid values are ENABLED and DISABLED.

### `RuleDefinition` — string · **required**

The definition of the rule, as a JSON object. For details on the valid syntax, see
[Contributor Insights Rule Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html).

### `Tags` — list<Tag>

A list of key-value pairs to associate with the Contributor Insights rule. You can
associate as many as 50 tags with a rule.

Tags can help you organize and categorize your resources. You can also use them to
scope user permissions, by granting a user permission to access or change only the
resources that have certain tag values.

To be able to associate tags with a rule, you must have the
`cloudwatch:TagResource` permission in addition to the
`cloudwatch:PutInsightRule` permission.

If you are using this operation to update an existing Contributor Insights rule, any
tags you specify in this parameter are ignored. To change the tags of an existing rule,
use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html).

### `ApplyOnTransformedLogs` — boolean

Specify `true` to have this rule evaluate log events after they have been
transformed by [Log
transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html). If you specify `true`, then the log events in log
groups that have transformers will be evaluated by Contributor Insights after being
transformed. Log groups that don't have transformers will still have their original log
events evaluated by Contributor Insights.

The default is `false`

If a log group has a transformer, and transformation fails for some log events,
those log events won't be evaluated by Contributor Insights. For information about
investigating log transformation failures, see [Transformation metrics and errors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html).

## Output (`PutInsightRuleOutput`)

_None._

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `LimitExceededException` — The operation exceeded one or more limits.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
