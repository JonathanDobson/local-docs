# StartAsyncInvoke

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `StartAsyncInvokeCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /async-invoke`

Starts an asynchronous invocation.

This operation requires permission for the `bedrock:InvokeModel` action.

To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the Converse API actions ([Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference).

## Input (`StartAsyncInvokeRequest`)

### `clientRequestToken` — string

Specify idempotency token to ensure that requests are not duplicated.

### `modelId` — string · **required**

The model to invoke.

### `modelInput` — document · **required**

Input to send to the model.

### `outputDataConfig` — AsyncInvokeOutputDataConfig · **required**

Where to store the output.

### `tags` — list<Tag>

Tags to apply to the invocation.

## Output (`StartAsyncInvokeResponse`)

### `invocationArn` — string · **required**

The ARN of the invocation.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `ConflictException` — Error occurred because of a conflict while performing an operation.
- `InternalServerException` — An internal server error occurred.
- `ResourceNotFoundException` — The specified resource ARN was not found.
- `ServiceQuotaExceededException` — Your request exceeds the service quota for your account.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
