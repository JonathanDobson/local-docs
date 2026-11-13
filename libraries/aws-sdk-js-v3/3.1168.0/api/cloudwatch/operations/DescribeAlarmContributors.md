# DescribeAlarmContributors

Service: Amazon CloudWatch · SDK for JavaScript v3: `DescribeAlarmContributorsCommand` from `@aws-sdk/client-cloudwatch`

Returns the information of the current alarm contributors that are in
`ALARM` state. This operation returns details about the individual time
series that contribute to the alarm's state.

## Input (`DescribeAlarmContributorsInput`)

### `AlarmName` — string · **required**

The name of the alarm for which to retrieve contributor information.

### `NextToken` — string

The token returned by a previous call to indicate that there is more data
available.

## Output (`DescribeAlarmContributorsOutput`)

### `AlarmContributors` — list<AlarmContributor> · **required**

A list of alarm contributors that provide details about the individual time series
contributing to the alarm's state.

### `NextToken` — string

The token that marks the start of the next batch of returned results.

## Errors

- `InvalidNextToken` — The next token specified is invalid.
- `ResourceNotFoundException` — The named resource does not exist.
