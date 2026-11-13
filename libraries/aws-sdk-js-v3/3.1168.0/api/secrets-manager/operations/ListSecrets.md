# ListSecrets

Service: AWS Secrets Manager · SDK for JavaScript v3: `ListSecretsCommand` from `@aws-sdk/client-secrets-manager` · Paginated (token `NextToken` → `NextToken`)

Lists the secrets that are stored by Secrets Manager in the Amazon Web Services account, not including secrets
that are marked for deletion. To see secrets marked for deletion, use the Secrets Manager
console.

All Secrets Manager operations are eventually consistent. ListSecrets might not
reflect changes from the last five minutes. You can get more recent information for a
specific secret by calling DescribeSecret.

To list the versions of a secret, use ListSecretVersionIds.

To retrieve the values for the secrets, call BatchGetSecretValue or
GetSecretValue.

For information about finding secrets in the console, see [Find secrets in
Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:ListSecrets`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`ListSecretsRequest`)

### `IncludePlannedDeletion` — boolean · default `null`

Specifies whether to include secrets scheduled for deletion. By default, secrets
scheduled for deletion aren't included.

### `MaxResults` — integer

The number of results to include in the response.

If there are more results available, in the response, Secrets Manager includes
`NextToken`. To get the next results, call `ListSecrets` again
with the value from `NextToken`.

### `NextToken` — string

A token that indicates where the output should continue from, if a previous call did
not show all results. To get the next results, call `ListSecrets` again with
this value.

### `Filters` — list<Filter>

The filters to apply to the list of secrets.

### `SortOrder` — SortOrderType (enum)

Secrets are listed by `CreatedDate`.

Values: `asc`, `desc`

### `SortBy` — SortByType (enum)

If not specified, secrets are listed by `CreatedDate`.

Values: `created-date`, `last-accessed-date`, `last-changed-date`, `name`

## Output (`ListSecretsResponse`)

### `SecretList` — list<SecretListEntry>

A list of the secrets in the account.

### `NextToken` — string

Secrets Manager includes this value if there's more output available than what is included in
the current response. This can occur even when the response includes no values at all,
such as when you ask for a filtered view of a long list. To get the next results, call
`ListSecrets` again with this value.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidNextTokenException` — The `NextToken` value is invalid.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.

## Examples

### To list the secrets in your account

The following example shows how to list all of the secrets in your account.

Output:

```json
{
  "SecretList": [
    {
      "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
      "Name": "MyTestDatabaseSecret",
      "Description": "My test database secret",
      "LastChangedDate": 1523477145.729,
      "SecretVersionsToStages": {
        "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE": [
          "AWSCURRENT"
        ]
      }
    },
    {
      "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret1-d4e5f6",
      "Name": "MyTestDatabaseSecret1",
      "Description": "Another secret created for a different database",
      "LastChangedDate": 1523482025.685,
      "SecretVersionsToStages": {
        "EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE": [
          "AWSCURRENT"
        ]
      }
    }
  ]
}
```
