# DescribeInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeInsightRulesCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Returns a list of all the Contributor Insights rules in your account.

For more information about Contributor Insights, see [Using Contributor
Insights to Analyze High-Cardinality Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html).

## Input (`DescribeInsightRulesInput`)

### `NextToken` — string

Include this value, if it was returned by the previous operation, to get the next set
of rules.

### `MaxResults` — integer

The maximum number of results to return in one operation. If you omit this parameter,
the default of 500 is used.

## Output (`DescribeInsightRulesOutput`)

### `NextToken` — string

If this parameter is present, it is a token that marks the start of the next batch of
returned results.

### `InsightRules` — list<InsightRule>

The rules returned by the operation.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
