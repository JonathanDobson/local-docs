# EnableInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `EnableInsightRulesCommand` from `@aws-sdk/client-cloudwatch`

Enables the specified Contributor Insights rules. When rules are enabled, they
immediately begin analyzing log data.

## Input (`EnableInsightRulesInput`)

### `RuleNames` — list<string> · **required**

An array of the rule names to enable. If you need to find out the names of your rules,
use [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html).

## Output (`EnableInsightRulesOutput`)

### `Failures` — list<PartialFailure>

An array listing the rules that could not be enabled. You cannot disable or enable
built-in rules.

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `LimitExceededException` — The operation exceeded one or more limits.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
