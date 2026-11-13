# ListResourcePolicies

Service: AWS Secrets Manager · SDK for JavaScript v3: `ListResourcePoliciesCommand` from `@aws-sdk/client-secrets-manager` · Paginated (token `NextToken` → `NextToken`)

Lists the resource-based policies attached to a secret. The response contains only the
names of the policies, not their contents. Secrets Manager lists `default` first,
followed by any other policies in alphabetical order. To get the contents of a policy,
use GetResourcePolicy. You can modify only the `default`
policy.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:ListResourcePolicies`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`ListResourcePoliciesRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `MaxResults` — integer

The number of results to include in the response. If you don't specify this value,
the service returns up to 100 results.

If there are more results available, in the response, Secrets Manager includes
`NextToken`. To get the next results, call
`ListResourcePolicies` again with the value from
`NextToken`.

### `NextToken` — string

A token that indicates where the output should continue from, if a previous call did
not show all results. To get the next results, call
`ListResourcePolicies` again with this value.

## Output (`ListResourcePoliciesResponse`)

### `ResourcePolicies` — list<ResourcePolicySummary> · **required**

A list of the resource policies attached to the secret.

### `NextToken` — string

Secrets Manager includes this value if there's more output available than what is included in
the current response. To get the next results, call
`ListResourcePolicies` again with this value.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidNextTokenException` — The `NextToken` value is invalid.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To list the resource-based policies attached to a secret

The following example shows how to list the resource-based policies attached to a secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret"
}
```

Output:

```json
{
  "ResourcePolicies": [
    {
      "PolicyName": "default"
    }
  ]
}
```
