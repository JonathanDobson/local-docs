# GetAccountSettings

Service: AWS Lambda · SDK for JavaScript v3: `GetAccountSettingsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2016-08-19/account-settings`

Retrieves details about your account's [limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) and usage in an Amazon Web Services Region.

## Input (`GetAccountSettingsRequest`)

_None._

## Output (`GetAccountSettingsResponse`)

### `AccountLimit` — AccountLimit

Limits that are related to concurrency and code storage.

### `AccountUsage` — AccountUsage

The number of functions and amount of storage in use.

## Errors

- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get account settings

This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.

Output:

```json
{
  "AccountLimit": {
    "CodeSizeUnzipped": 262144000,
    "CodeSizeZipped": 52428800,
    "ConcurrentExecutions": 1000,
    "TotalCodeSize": 80530636800,
    "UnreservedConcurrentExecutions": 1000
  },
  "AccountUsage": {
    "FunctionCount": 4,
    "TotalCodeSize": 9426
  }
}
```
