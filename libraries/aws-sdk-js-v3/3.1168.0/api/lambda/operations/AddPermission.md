# AddPermission

Service: AWS Lambda · SDK for JavaScript v3: `AddPermissionCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2015-03-31/functions/{FunctionName}/policy`

Grants a [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST.

To grant permission to another account, specify the account ID as the `Principal`. To grant permission to an organization defined in Organizations, specify the organization ID as the `PrincipalOrgID`. For Amazon Web Services services, the principal is a domain-style identifier that the service defines, such as `s3.amazonaws.com` or `sns.amazonaws.com`. For Amazon Web Services services, you can also specify the ARN of the associated resource as the `SourceArn`. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.

This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see [Using resource-based policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).

## Input (`AddPermissionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `StatementId` — string · **required**

A statement identifier that differentiates the statement from others in the same policy.

### `Action` — string · **required**

The action that the principal can use on the function. For example, `lambda:InvokeFunction` or `lambda:GetFunction`.

### `Principal` — string · **required**

The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you specify a service, use `SourceArn` or `SourceAccount` to limit who can invoke the function through that service.

### `SourceArn` — string

For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.

Note that Lambda configures the comparison using the `StringLike` operator.

### `FunctionUrlAuthType` — FunctionUrlAuthType (enum)

The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).

Values: `NONE`, `AWS_IAM`

### `InvokedViaFunctionUrl` — boolean

Indicates whether the permission applies when the function is invoked through a function URL.

### `SourceAccount` — string

For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together with `SourceArn` to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.

### `EventSourceToken` — string

For Alexa Smart Home functions, a token that the invoker must supply.

### `Qualifier` — string · sent as query `Qualifier`

Specify a version or alias to add permissions to a published version of the function.

### `RevisionId` — string

Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.

### `PrincipalOrgID` — string

The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services accounts under this organization.

## Output (`AddPermissionResponse`)

### `Statement` — string

The permission statement that's added to the function policy.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `PolicyLengthExceededException` — The permissions policy for the resource is too large.
- `PreconditionFailedException` — The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
- `PublicPolicyException` — The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To grant Amazon S3 permission to invoke a function

The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.

Input:

```json
{
  "Action": "lambda:InvokeFunction",
  "FunctionName": "my-function",
  "Principal": "s3.amazonaws.com",
  "SourceAccount": "123456789012",
  "SourceArn": "arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*",
  "StatementId": "s3"
}
```

Output:

```json
{
  "Statement": "{\"Sid\":\"s3\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-2:123456789012:function:my-function\",\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"123456789012\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::my-bucket-1xpuxmplzrlbh\"}}}"
}
```

### To grant another account permission to invoke a function

The following example adds permission for account 223456789012 invoke a Lambda function named my-function.

Input:

```json
{
  "Action": "lambda:InvokeFunction",
  "FunctionName": "my-function",
  "Principal": "223456789012",
  "StatementId": "xaccount"
}
```

Output:

```json
{
  "Statement": "{\"Sid\":\"xaccount\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::223456789012:root\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-2:123456789012:function:my-function\"}"
}
```
