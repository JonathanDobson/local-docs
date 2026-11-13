# ListSecretVersionIds

Service: AWS Secrets Manager · SDK for JavaScript v3: `ListSecretVersionIdsCommand` from `@aws-sdk/client-secrets-manager` · Paginated (token `NextToken` → `NextToken`)

Lists the versions of a secret. Secrets Manager uses staging labels to indicate the different
versions of a secret. For more information, see  [Secrets Manager
concepts: Versions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version).

To list the secrets in the account, use ListSecrets.

`ListSecretVersionIds` only returns versions that contain a secret
value. To see all version IDs that have staging labels attached, including ones
without a secret value, call `DescribeSecret` and check
`VersionIdsToStages`.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:ListSecretVersionIds`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`ListSecretVersionIdsRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret whose versions you want to list.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `MaxResults` — integer

The number of results to include in the response.

If there are more results available, in the response, Secrets Manager includes
`NextToken`. To get the next results, call
`ListSecretVersionIds` again with the value from `NextToken`.

### `NextToken` — string

A token that indicates where the output should continue from, if a previous call did
not show all results. To get the next results, call `ListSecretVersionIds`
again with this value.

### `IncludeDeprecated` — boolean · default `null`

Specifies whether to include versions of secrets that don't have any staging labels
attached to them. Versions without staging labels are considered deprecated and are
subject to deletion by Secrets Manager. By default, versions without staging labels aren't
included.

## Output (`ListSecretVersionIdsResponse`)

### `Versions` — list<SecretVersionsListEntry>

A list of the versions of the secret.

### `NextToken` — string

Secrets Manager includes this value if there's more output available than what is included in
the current response. This can occur even when the response includes no values at all,
such as when you ask for a filtered view of a long list. To get the next results, call
`ListSecretVersionIds` again with this value.

### `ARN` — string

The ARN of the secret.

### `Name` — string

The name of the secret.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidNextTokenException` — The `NextToken` value is invalid.
- `InvalidParameterException` — The parameter name or value is invalid.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To list all of the secret versions associated with a secret

The following example shows how to retrieve a list of all of the versions of a secret, including those without any staging labels.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "IncludeDeprecated": true
}
```

Output:

```json
{
  "Versions": [
    {
      "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE",
      "VersionStages": [
        "AWSPREVIOUS"
      ],
      "CreatedDate": 1523477145.713
    },
    {
      "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE",
      "VersionStages": [
        "AWSCURRENT"
      ],
      "CreatedDate": 1523486221.391
    },
    {
      "CreatedDate": 1511974462.36,
      "VersionId": "EXAMPLE3-90ab-cdef-fedc-ba987EXAMPLE;"
    }
  ],
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret"
}
```
