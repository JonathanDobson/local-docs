# PutFunctionEventInvokeConfig

Service: AWS Lambda · SDK for JavaScript v3: `PutFunctionEventInvokeConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2019-09-25/functions/{FunctionName}/event-invoke-config`

Configures options for [asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use UpdateFunctionEventInvokeConfig.

By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with UpdateFunctionConfiguration.

To send an invocation record to a queue, topic, S3 bucket, function, or event bus, specify a [destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations). You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue.

S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.

## Input (`PutFunctionEventInvokeConfigRequest`)

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

### To configure error handling for asynchronous invocation

The following example sets a maximum event age of one hour and disables retries for the specified function.

Input:

```json
{
  "FunctionName": "my-function",
  "MaximumEventAgeInSeconds": 3600,
  "MaximumRetryAttempts": 0
}
```

Output:

```json
{
  "DestinationConfig": {
    "OnFailure": {},
    "OnSuccess": {}
  },
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST",
  "LastModified": "2016-11-21T19:49:20.006Z",
  "MaximumEventAgeInSeconds": 3600,
  "MaximumRetryAttempts": 0
}
```
