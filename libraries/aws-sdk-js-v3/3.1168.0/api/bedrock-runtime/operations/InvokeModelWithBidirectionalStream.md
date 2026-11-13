# InvokeModelWithBidirectionalStream

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `InvokeModelWithBidirectionalStreamCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /model/{modelId}/invoke-with-bidirectional-stream`

Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream. The response is returned in a stream that remains open for 8 minutes. A single session can contain multiple prompts and responses from the model. The prompts to the model are provided as audio files and the model's responses are spoken back to the user and transcribed.

It is possible for users to interrupt the model's response with a new prompt, which will halt the response speech. The model will retain contextual awareness of the conversation while pivoting to respond to the new prompt.

## Input (`InvokeModelWithBidirectionalStreamRequest`)

### `modelId` — string · **required** · sent as httpLabel

The model ID or ARN of the model ID to use. Currently, only `amazon.nova-sonic-v1:0` is supported.

### `body` — InvokeModelWithBidirectionalStreamInput · **required** · sent as httpPayload

The prompt and inference parameters in the format specified in the `BidirectionalInputPayloadPart` in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html). For more information, see [Run inference](https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html) in the Bedrock User Guide.

## Output (`InvokeModelWithBidirectionalStreamResponse`)

### `body` — InvokeModelWithBidirectionalStreamOutput · **required** · sent as httpPayload

Streaming response from the model in the format specified by the `BidirectionalOutputPayloadPart` header.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ModelErrorException` — The request failed due to an error while processing the model.
- `ModelNotReadyException` — The model specified in the request is not ready to serve inference requests.
- `ModelStreamErrorException` — An error occurred while streaming the response.
- `ModelTimeoutException` — The request took too long to process.
- `ResourceNotFoundException` — The specified resource ARN was not found.
- `ServiceQuotaExceededException` — Your request exceeds the service quota for your account.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
