# TagResource

Service: AWS Secrets Manager · SDK for JavaScript v3: `TagResourceCommand` from `@aws-sdk/client-secrets-manager`

Attaches tags to a secret. Tags consist of a key name and a value. Tags are part of
the secret's metadata. They are not associated with specific versions of the secret.
This operation appends tags to the existing list of tags.

For tag quotas and naming restrictions, see [Service quotas for
Tagging](https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas) in the *Amazon Web Services General Reference guide*.

If you use tags as part of your security strategy, then adding or removing a tag
can change permissions. If successfully completing this operation would result in
you losing your permissions for this secret, then the operation is blocked and
returns an Access Denied error.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

**Required permissions:**
`secretsmanager:TagResource`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`TagResourceRequest`)

### `SecretId` — string · **required**

The identifier for the secret to attach tags to. You can specify either the Amazon
Resource Name (ARN) or the friendly name of the secret.

For an ARN, we recommend that you specify a complete ARN rather
than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).

### `Tags` — list<Tag> · **required**

The tags to attach to the secret as a JSON text string argument. Each element in the
list consists of a `Key` and a `Value`.

For storing multiple values, we recommend that you use a JSON text
string argument and specify key/value pairs. For more information, see [Specifying parameter values for the Amazon Web Services CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html)
in the Amazon Web Services CLI User Guide.

## Output (`Unit`)

_None._

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.
- `ResourceNotFoundException` — Secrets Manager can't find the resource that you asked for.

## Examples

### To add tags to a secret

The following example shows how to attach two tags each with a Key and Value to a secret. There is no output from this API. To see the result, use the DescribeSecret operation.

Input:

```json
{
  "SecretId": "MyExampleSecret",
  "Tags": [
    {
      "Key": "FirstTag",
      "Value": "SomeValue"
    },
    {
      "Key": "SecondTag",
      "Value": "AnotherValue"
    }
  ]
}
```
