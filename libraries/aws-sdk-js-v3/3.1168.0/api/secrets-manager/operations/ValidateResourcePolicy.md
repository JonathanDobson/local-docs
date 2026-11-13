# ValidateResourcePolicy

Service: AWS Secrets Manager · SDK for JavaScript v3: `ValidateResourcePolicyCommand` from `@aws-sdk/client-secrets-manager`

Validates that a resource policy does not grant a wide range of principals access to
your secret. A resource-based policy is optional for secrets.

The API performs three checks when validating the policy:

- Sends a call to [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/), an automated reasoning engine, to ensure your resource
  policy does not allow broad access to your secret, for example policies that use
  a wildcard for the principal.
- Checks for correct syntax in a policy.
- Verifies the policy does not lock out a caller.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:ValidateResourcePolicy` and
`secretsmanager:PutResourcePolicy`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`ValidateResourcePolicyRequest`)

### `SecretId` — string

The ARN or name of the secret with the resource-based policy you want to
validate.

### `ResourcePolicy` — string · **required**

A JSON-formatted string that contains an Amazon Web Services resource-based policy. The policy in
the string identifies who can access or manage this secret and its versions. For example
policies, see [Permissions
policy examples](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html).

## Output (`ValidateResourcePolicyResponse`)

### `PolicyValidationPassed` — boolean · default `false`

True if your policy passes validation, otherwise false.

### `ValidationErrors` — list<ValidationErrorsEntry>

Validation errors if your policy didn't pass validation.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `MalformedPolicyDocumentException` — The resource policy has syntax errors.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To validate a resource-based policy to a secret

The following example shows how to validate a resource-based policy to a secret.

Input:

```json
{
  "SecretId": "MyTestDatabaseSecret",
  "ResourcePolicy": "{\n\"Version\":\"2012-10-17\",\n\"Statement\":[{\n\"Effect\":\"Allow\",\n\"Principal\":{\n\"AWS\":\"arn:aws:iam::123456789012:root\"\n},\n\"Action\":\"secretsmanager:GetSecretValue\",\n\"Resource\":\"*\"\n}]\n}"
}
```

Output:

```json
{
  "PolicyValidationPassed": true,
  "ValidationErrors": []
}
```
