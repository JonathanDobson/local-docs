# GetAsyncInvoke

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `GetAsyncInvokeCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `GET /async-invoke/{invocationArn}`

Retrieve information about an asynchronous invocation.

## Input (`GetAsyncInvokeRequest`)

### `invocationArn` — string · **required** · sent as httpLabel

The invocation's ARN.

## Output (`GetAsyncInvokeResponse`)

### `invocationArn` — string · **required**

The invocation's ARN.

### `modelArn` — string · **required**

The invocation's model ARN.

### `clientRequestToken` — string

The invocation's idempotency token.

### `status` — AsyncInvokeStatus (enum) · **required**

The invocation's status.

Values: `InProgress`, `Completed`, `Failed`

### `failureMessage` — string

An error message.

### `submitTime` — timestamp · **required**

When the invocation request was submitted.

### `lastModifiedTime` — timestamp

The invocation's last modified time.

### `endTime` — timestamp

When the invocation ended.

### `outputDataConfig` — AsyncInvokeOutputDataConfig · **required**

Output data settings.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
