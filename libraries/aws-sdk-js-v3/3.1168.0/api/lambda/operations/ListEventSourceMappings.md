# ListEventSourceMappings

Service: AWS Lambda · SDK for JavaScript v3: `ListEventSourceMappingsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/event-source-mappings` · Paginated

Lists event source mappings. Specify an `EventSourceArn` to show only event source mappings for a single event source.

## Input (`ListEventSourceMappingsRequest`)

### `EventSourceArn` — string · sent as query `EventSourceArn`

The Amazon Resource Name (ARN) of the event source.

- **Amazon Kinesis** – The ARN of the data stream or a stream consumer.
- **Amazon DynamoDB Streams** – The ARN of the stream.
- **Amazon Simple Queue Service** – The ARN of the queue.
- **Amazon Managed Streaming for Apache Kafka** – The ARN of the cluster or the ARN of the VPC connection (for [cross-account event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc)).
- **Amazon MQ** – The ARN of the broker.
- **Amazon DocumentDB** – The ARN of the DocumentDB change stream.

### `FunctionName` — string · sent as query `FunctionName`

The name or ARN of the Lambda function.

**Name formats**

- **Function name** – `MyFunction`.
- **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
- **Version or Alias ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`.
- **Partial ARN** – `123456789012:function:MyFunction`.

The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.

### `Marker` — string · sent as query `Marker`

A pagination token returned by a previous call.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items in each response, even if you set the number higher.

## Output (`ListEventSourceMappingsResponse`)

### `NextMarker` — string

A pagination token that's returned when the response doesn't contain all event source mappings.

### `EventSourceMappings` — list<EventSourceMappingConfiguration>

A list of event source mappings.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To list the event source mappings for a function

The following example returns a list of the event source mappings for a function named my-function.

Input:

```json
{
  "FunctionName": "my-function"
}
```

Output:

```json
{
  "EventSourceMappings": [
    {
      "BatchSize": 5,
      "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue",
      "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
      "LastModified": 1569284520.333,
      "State": "Enabled",
      "StateTransitionReason": "USER_INITIATED",
      "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
    }
  ]
}
```
