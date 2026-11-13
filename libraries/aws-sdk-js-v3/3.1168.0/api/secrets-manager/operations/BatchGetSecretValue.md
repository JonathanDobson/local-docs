# BatchGetSecretValue

Service: AWS Secrets Manager · SDK for JavaScript v3: `BatchGetSecretValueCommand` from `@aws-sdk/client-secrets-manager` · Paginated (token `NextToken` → `NextToken`)

Retrieves the contents of the encrypted fields `SecretString` or
`SecretBinary` for up to 20 secrets. To retrieve a single secret, call
GetSecretValue.

To choose which secrets to retrieve, you can specify a list of secrets by name or ARN,
or you can use filters. If Secrets Manager encounters errors such as
`AccessDeniedException` while attempting to retrieve any of the secrets,
you can see the errors in `Errors` in the response.

Secrets Manager generates CloudTrail
`GetSecretValue` log entries for each secret you request when you call this
action. Do not include sensitive information in request parameters because it might be
logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:BatchGetSecretValue`, and you must have
`secretsmanager:GetSecretValue` for each secret. If you use filters, you
must also have `secretsmanager:ListSecrets`. If the secrets are encrypted
using customer-managed keys instead of the Amazon Web Services managed key
`aws/secretsmanager`, then you also need `kms:Decrypt`
permissions for the keys. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`BatchGetSecretValueRequest`)

### `SecretIdList` — list<string>

The ARN or names of the secrets to retrieve. You must include `Filters` or
`SecretIdList`, but not both.

### `Filters` — list<Filter>

The filters to choose which secrets to retrieve. You must include `Filters`
or `SecretIdList`, but not both.

### `MaxResults` — integer

The number of results to include in the response.

If there are more results available, in the response, Secrets Manager includes
`NextToken`. To get the next results, call
`BatchGetSecretValue` again with the value from `NextToken`.
To use this parameter, you must also use the `Filters` parameter.

### `NextToken` — string

A token that indicates where the output should continue from, if a previous call did
not show all results. To get the next results, call `BatchGetSecretValue`
again with this value.

## Output (`BatchGetSecretValueResponse`)

### `SecretValues` — list<SecretValueEntry>

A list of secret values.

### `NextToken` — string

Secrets Manager includes this value if there's more output available than what is included in
the current response. This can occur even when the response includes no values at all,
such as when you ask for a filtered view of a long list. To get the next results, call
`BatchGetSecretValue` again with this value.

### `Errors` — list<APIErrorType>

A list of errors Secrets Manager encountered while attempting to retrieve individual
secrets.

## Errors

- `DecryptionFailure` — Secrets Manager can't decrypt the protected secret text using the provided KMS key.
- `InternalServiceError` — An error occurred on the server side.
- `InvalidNextTokenException` — The `NextToken` value is invalid.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To retrieve the secret values for a group of secrets listed by name

The following example gets the values for three secrets.

Input:

```json
{
  "SecretIdList": [
    "MySecret1",
    "MySecret2",
    "MySecret3"
  ]
}
```

Output:

```json
{
  "SecretValues": [
    {
      "ARN": "&region-arn;&asm-service-name;:us-west-2:&ExampleAccountId;:secret:MySecret1-a1b2c3",
      "CreatedDate": 1700591229.801,
      "Name": "MySecret1",
      "SecretString": "{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}",
      "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
      "VersionStages": [
        "AWSCURRENT"
      ]
    },
    {
      "ARN": "&region-arn;&asm-service-name;:us-west-2:&ExampleAccountId;:secret:MySecret2-a1b2c3",
      "CreatedDate": 1699911394.105,
      "Name": "MySecret2",
      "SecretString": "{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"",
      "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
      "VersionStages": [
        "AWSCURRENT"
      ]
    },
    {
      "ARN": "&region-arn;&asm-service-name;:us-west-2:&ExampleAccountId;:secret:MySecret3-a1b2c3",
      "CreatedDate": 1699911394.105,
      "Name": "MySecret3",
      "SecretString": "{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"",
      "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc",
      "VersionStages": [
        "AWSCURRENT"
      ]
    }
  ],
  "Errors": []
}
```
