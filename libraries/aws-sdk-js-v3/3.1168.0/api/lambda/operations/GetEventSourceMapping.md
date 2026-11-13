# GetEventSourceMapping

Service: AWS Lambda · SDK for JavaScript v3: `GetEventSourceMappingCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/event-source-mappings/{UUID}`

Returns details about an event source mapping. You can get the identifier of a mapping from the output of ListEventSourceMappings.

## Input (`GetEventSourceMappingRequest`)

### `UUID` — string · **required** · sent as httpLabel

The identifier of the event source mapping.

## Output (`EventSourceMappingConfiguration`)

### `UUID` — string

The identifier of the event source mapping.

### `StartingPosition` — EventSourcePosition (enum)

The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. `AT_TIMESTAMP` is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.

Values: `TRIM_HORIZON`, `LATEST`, `AT_TIMESTAMP`

### `StartingPositionTimestamp` — timestamp

With `StartingPosition` set to `AT_TIMESTAMP`, the time from which to start reading. `StartingPositionTimestamp` cannot be in the future.

### `BatchSize` — integer

The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).

Default value: Varies by service. For Amazon SQS, the default is 10. For all other services, the default is 100.

Related setting: When you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.

### `MaximumBatchingWindowInSeconds` — integer

The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.

For streams and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.

Related setting: For streams and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.

### `ParallelizationFactor` — integer

(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.

### `EventSourceArn` — string

The Amazon Resource Name (ARN) of the event source.

### `FilterCriteria` — FilterCriteria

An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).

If filter criteria is encrypted, this field shows up as `null` in the response of ListEventSourceMapping API calls. You can view this field in plaintext in the response of GetEventSourceMapping and DeleteEventSourceMapping calls if you have `kms:Decrypt` permissions for the correct KMS key.

### `FilterCriteriaError` — FilterCriteriaError

An object that contains details about an error related to filter criteria encryption.

### `KMSKeyArn` — string

The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics).

### `MetricsConfig` — EventSourceMappingMetricsConfig

The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).

### `LoggingConfig` — EventSourceMappingLoggingConfig

(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see [Event source mapping logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html).

### `ScalingConfig` — ScalingConfig

(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency).

### `FunctionArn` — string

The ARN of the Lambda function.

### `LastModified` — timestamp

The date that the event source mapping was last updated or that its state changed.

### `LastProcessingResult` — string

The result of the event source mapping's last processing attempt.

### `State` — string

The state of the event source mapping. It can be one of the following: `Creating`, `Enabling`, `Enabled`, `Disabling`, `Disabled`, `Updating`, or `Deleting`.

### `StateTransitionReason` — string

Indicates whether a user or Lambda made the last change to the event source mapping.

### `DestinationConfig` — DestinationConfig

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.

### `Topics` — list<string>

The name of the Kafka topic.

### `Queues` — list<string>

(Amazon MQ) The name of the Amazon MQ broker destination queue to consume.

### `SourceAccessConfigurations` — list<SourceAccessConfiguration>

An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.

### `SelfManagedEventSource` — SelfManagedEventSource

The self-managed Apache Kafka cluster for your event source.

### `MaximumRecordAgeInSeconds` — integer

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.

The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed

### `BisectBatchOnFunctionError` — boolean

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry. The default value is false.

### `MaximumRetryAttempts` — integer

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.

### `TumblingWindowInSeconds` — integer

(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.

### `FunctionResponseTypes` — list<FunctionResponseType (enum)>

(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.

### `AmazonManagedKafkaEventSourceConfig` — AmazonManagedKafkaEventSourceConfig

Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.

### `SelfManagedKafkaEventSourceConfig` — SelfManagedKafkaEventSourceConfig

Specific configuration settings for a self-managed Apache Kafka event source.

### `DocumentDBEventSourceConfig` — DocumentDBEventSourceConfig

Specific configuration settings for a DocumentDB event source.

### `EventSourceMappingArn` — string

The Amazon Resource Name (ARN) of the event source mapping.

### `ProvisionedPollerConfig` — ProvisionedPollerConfig

(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode).

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a Lambda function's event source mapping

The following example returns details about an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

Input:

```json
{
  "UUID": "14e0db71-xmpl-4eb5-b481-8945cf9d10c2"
}
```

Output:

```json
{
  "BatchSize": 500,
  "BisectBatchOnFunctionError": false,
  "DestinationConfig": {},
  "EventSourceArn": "arn:aws:sqs:us-east-2:123456789012:mySQSqueue",
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:myFunction",
  "LastModified": "2016-11-21T19:49:20.006Z",
  "LastProcessingResult": "No records processed",
  "MaximumRecordAgeInSeconds": 604800,
  "MaximumRetryAttempts": 10000,
  "State": "Creating",
  "StateTransitionReason": "User action",
  "UUID": "14e0db71-xmpl-4eb5-b481-8945cf9d10c2"
}
```
