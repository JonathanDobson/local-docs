# PutResourcePolicy

Service: AWS Secrets Manager · SDK for JavaScript v3: `PutResourcePolicyCommand` from `@aws-sdk/client-secrets-manager`

Attaches a resource-based permission policy to a secret. A resource-based policy is
optional. For more information, see [Authentication and access control for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)

For information about attaching a policy in the console, see [Attach a permissions policy to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:PutResourcePolicy`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`PutResourcePolicyRequest`)

### `SecretId` — string · **required**

The ARN or name of the secret to attach the resource-based policy.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `ResourcePolicy` — string · **required**

A JSON-formatted string for an Amazon Web Services resource-based policy. For example policies, see
[Permissions policy examples](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html).

### `PolicyName` — string

The name of the resource policy to attach. If you don't specify this field, Secrets Manager uses
`default`. You can only attach the `default` policy; if you
specify any other name, the operation returns an
`InvalidParameterException`.

### `BlockPublicPolicy` — boolean · default `null`

Specifies whether to block resource-based policies that allow broad access to the
secret, for example those that use a wildcard for the principal. By default, public
policies aren't blocked.

Resource policy validation and the BlockPublicPolicy parameter help protect your
resources by preventing public access from being granted through the resource
policies that are directly attached to your secrets. In addition to using these
features, carefully inspect the following policies to confirm that they do not grant
public access:

- Identity-based policies attached to associated Amazon Web Services
  principals (for example, IAM roles)
- Resource-based policies attached to associated Amazon Web Services
  resources (for example, Key Management Service (KMS)
  keys)

To review permissions to your secrets, see [Determine who has permissions to your secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html).

## Output (`PutResourcePolicyResponse`)

### `ARN` — string

The ARN of the secret.

### `Name` — string

The name of the secret.

### `PolicyName` — string

The name of the resource policy. If you didn't specify `PolicyName` in the
request, this is `default`.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `MalformedPolicyDocumentException` — The resource policy has syntax errors.
- `PublicPolicyException` — The `BlockPublicPolicy` parameter is set to true, and the resource policy did not prevent broad access to the secret.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To add a resource-based policy to a secret

The following example shows how to add a resource-based policy to a secret.

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
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "PolicyName": "default"
}
```
