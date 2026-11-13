# UpdateFunctionEventInvokeConfig

Service: AWS Lambda · SDK for JavaScript v3: `UpdateFunctionEventInvokeConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2019-09-25/functions/{FunctionName}/event-invoke-config`

Updates the configuration for asynchronous invocation for a function, version, or alias.

To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig.

## Input (`UpdateFunctionEventInvokeConfigRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** - `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
- **Partial ARN** - `123456789012:function:my-function`.

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

### `Qualifier` — string · sent as query `Qualifier`

A version number or alias name.

### `MaximumRetryAttempts` — integer

The maximum number of times to retry when the function returns an error.

### `MaximumEventAgeInSeconds` — integer

The maximum age of a request that Lambda sends to a function for processing.

### `DestinationConfig` — DestinationConfig

A destination for events after they have been sent to a function for processing.

**Destinations**

- **Function** - The Amazon Resource Name (ARN) of a Lambda function.
- **Queue** - The ARN of a standard SQS queue.
- **Bucket** - The ARN of an Amazon S3 bucket.
- **Topic** - The ARN of a standard SNS topic.
- **Event Bus** - The ARN of an Amazon EventBridge event bus.

S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.

## Output (`FunctionEventInvokeConfig`)

### `LastModified` — timestamp

The date and time that the configuration was last updated.

### `FunctionArn` — string

The Amazon Resource Name (ARN) of the function.

### `MaximumRetryAttempts` — integer

The maximum number of times to retry when the function returns an error.

### `MaximumEventAgeInSeconds` — integer

The maximum age of a request that Lambda sends to a function for processing.

### `DestinationConfig` — DestinationConfig

A destination for events after they have been sent to a function for processing.

**Destinations**

- **Function** - The Amazon Resource Name (ARN) of a Lambda function.
- **Queue** - The ARN of a standard SQS queue.
- **Bucket** - The ARN of an Amazon S3 bucket.
- **Topic** - The ARN of a standard SNS topic.
- **Event Bus** - The ARN of an Amazon EventBridge event bus.

S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To update an asynchronous invocation configuration

The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.

Input:

```json
{
  "DestinationConfig": {
    "OnFailure": {
      "Destination": "arn:aws:sqs:us-east-2:123456789012:destination"
    }
  },
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "DestinationConfig": {
    "OnFailure": {
      "Destination": "arn:aws:sqs:us-east-2:123456789012:destination"
    },
    "OnSuccess": {}
  },
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST",
  "LastModified": 1573687896.493,
  "MaximumEventAgeInSeconds": 3600,
  "MaximumRetryAttempts": 0
}
```
