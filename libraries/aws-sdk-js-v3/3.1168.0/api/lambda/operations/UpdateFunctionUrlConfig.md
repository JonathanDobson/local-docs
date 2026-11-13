# UpdateFunctionUrlConfig

Service: AWS Lambda · SDK for JavaScript v3: `UpdateFunctionUrlConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2021-10-31/functions/{FunctionName}/url`

Updates the configuration for a function URL of a Lambda Event Function.

## Input (`UpdateFunctionUrlConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `my-function`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** – `123456789012:function:my-function`.

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

The alias name.

### `AuthType` — FunctionUrlAuthType (enum)

The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).

Values: `NONE`, `AWS_IAM`

### `Cors` — Cors

The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.

### `InvokeMode` — InvokeMode (enum)

Use one of the following options:

- `BUFFERED` – This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
- `RESPONSE_STREAM` – Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 200 MB.

Values: `BUFFERED`, `RESPONSE_STREAM`

## Output (`UpdateFunctionUrlConfigResponse`)

### `FunctionUrl` — string · **required**

The HTTP URL endpoint for your function.

### `FunctionArn` — string · **required**

The Amazon Resource Name (ARN) of your function.

### `AuthType` — FunctionUrlAuthType (enum) · **required**

The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).

Values: `NONE`, `AWS_IAM`

### `Cors` — Cors

The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.

### `CreationTime` — string · **required**

When the function URL was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

### `LastModifiedTime` — string · **required**

When the function URL configuration was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

### `InvokeMode` — InvokeMode (enum)

Use one of the following options:

- `BUFFERED` – This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
- `RESPONSE_STREAM` – Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 200 MB.

Values: `BUFFERED`, `RESPONSE_STREAM`

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
