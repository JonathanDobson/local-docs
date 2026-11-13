# DeleteInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `DeleteInsightRulesCommand` from `@aws-sdk/client-cloudwatch`

Permanently deletes the specified Contributor Insights rules.

If you create a rule, delete it, and then re-create it with the same name, historical
data from the first time the rule was created might not be available.

## Input (`DeleteInsightRulesInput`)

### `RuleNames` — list<string> · **required**

An array of the rule names to delete. If you need to find out the names of your rules,
use [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html).

## Output (`DeleteInsightRulesOutput`)

### `Failures` — list<PartialFailure>

An array listing the rules that could not be deleted. You cannot delete built-in
rules.

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
