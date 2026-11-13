# PutFunctionRecursionConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutFunctionRecursionConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2024-08-31/functions/{FunctionName}/recursion-config`

Sets the [recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) configuration for a Lambda Event Function.

When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.

Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to `Terminate`, it stops your function being invoked and notifies you.

## Input (`PutFunctionRecursionConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `RecursiveLoop` — RecursiveLoop (enum) · **required**

If you set your function's recursive loop detection configuration to `Allow`, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes it.

If you set your function's recursive loop detection configuration to `Terminate`, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.

By default, Lambda sets your function's configuration to `Terminate`.

If your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your Amazon Web Services account. To learn more about best practices for using recursive invocation patterns, see [Recursive patterns that cause run-away Lambda functions](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway) in Serverless Land.

Values: `Allow`, `Terminate`

## Output (`PutFunctionRecursionConfigResponse`)

### `RecursiveLoop` — RecursiveLoop (enum)

The status of your function's recursive loop detection configuration.

When this value is set to `Allow`and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.

When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.

Values: `Allow`, `Terminate`

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
