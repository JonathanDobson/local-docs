# DisableInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `DisableInsightRulesCommand` from `@aws-sdk/client-cloudwatch`

Disables the specified Contributor Insights rules. When rules are disabled, they do
not analyze log groups and do not incur costs.

## Input (`DisableInsightRulesInput`)

### `RuleNames` — list<string> · **required**

An array of the rule names to disable. If you need to find out the names of your
rules, use [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html).

## Output (`DisableInsightRulesOutput`)

### `Failures` — list<PartialFailure>

An array listing the rules that could not be disabled. You cannot disable built-in
rules.

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
