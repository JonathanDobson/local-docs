# GetResourcePolicy

Service: AWS Secrets Manager · SDK for JavaScript v3: `GetResourcePolicyCommand` from `@aws-sdk/client-secrets-manager`

Retrieves the JSON text of the resource-based policy document attached to the secret.
For more information about permissions policies attached to a secret, see [Permissions policies attached to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:GetResourcePolicy`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`GetResourcePolicyRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to retrieve the attached resource-based policy
for.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `PolicyName` — string

The name of the resource policy to retrieve. If you don't specify this field, Secrets Manager
uses `default`. If you specify a name other than `default` and no
policy with that name exists, the operation returns a
`ResourceNotFoundException`.

## Output (`GetResourcePolicyResponse`)

### `ARN` — string

The ARN of the secret that the resource-based policy was retrieved for.

### `Name` — string

The name of the secret that the resource-based policy was retrieved for.

### `ResourcePolicy` — string

A JSON-formatted string that contains the permissions policy attached to the secret.
For more information about permissions policies, see [Authentication and access
control for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

### `PolicyName` — string

The name of the resource policy. If you didn't specify `PolicyName` in the
request, this is `default`.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To retrieve the resource-based policy attached to a secret

The following example shows how to retrieve the resource-based policy that is attached to a secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret"
}
```

Output:

```json
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "ResourcePolicy": "{\n\"Version\":\"2012-10-17\",\n\"Statement\":[{\n\"Effect\":\"Allow\",\n\"Principal\":{\n\"AWS\":\"arn:aws:iam::123456789012:root\"\n},\n\"Action\":\"secretsmanager:GetSecretValue\",\n\"Resource\":\"*\"\n}]\n}",
  "PolicyName": "default"
}
```
