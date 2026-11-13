# PutManagedInsightRules

Service: Amazon CloudWatch · SDK for JavaScript v3: `PutManagedInsightRulesCommand` from `@aws-sdk/client-cloudwatch`

Creates a managed Contributor Insights rule for a specified Amazon Web Services
resource. When you enable a managed rule, you create a Contributor Insights rule that
collects data from Amazon Web Services services. You cannot edit these rules with
`PutInsightRule`. The rules can be enabled, disabled, and deleted using
`EnableInsightRules`, `DisableInsightRules`, and
`DeleteInsightRules`. If a previously created managed rule is currently
disabled, a subsequent call to this API will re-enable it. Use
`ListManagedInsightRules` to describe all available rules.

## Input (`PutManagedInsightRulesInput`)

### `ManagedRules` — list<ManagedRule> · **required**

A list of `ManagedRules` to enable.

## Output (`PutManagedInsightRulesOutput`)

### `Failures` — list<PartialFailure>

An array that lists the rules that could not be enabled.

## Errors

- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `MissingRequiredParameterException` — An input parameter that is required is missing.
