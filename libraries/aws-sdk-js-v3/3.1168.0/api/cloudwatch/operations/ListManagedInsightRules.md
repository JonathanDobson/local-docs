# ListManagedInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `ListManagedInsightRulesCommand` from `@aws-sdk/client-cloudwatch` · Paginated (token `NextToken` → `NextToken`)

Returns a list that contains the number of managed Contributor Insights rules in your
account.

## Input (`ListManagedInsightRulesInput`)

### `ResourceARN` — string · **required**

The ARN of an Amazon Web Services resource that has managed Contributor Insights
rules.

### `NextToken` — string

Include this value to get the next set of rules if the value was returned by the
previous operation.

### `MaxResults` — integer

The maximum number of results to return in one operation. If you omit this parameter,
the default number is used. The default number is `100`.

## Output (`ListManagedInsightRulesOutput`)

### `ManagedRules` — list<ManagedRuleDescription>

The managed rules that are available for the specified Amazon Web Services resource.

### `NextToken` — string

Include this value to get the next set of rules if the value was returned by the
previous operation.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
