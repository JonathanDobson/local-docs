# Converse

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `ConverseCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /model/{modelId}/converse`

Sends messages to the specified Amazon Bedrock model. `Converse` provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.

Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.

You can submit a prompt by including it in the `messages` field, specifying the `modelId` of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.

You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the `promptVariables` field. You can append more messages to the prompt by using the `messages` field. If you use a prompt from Prompt management, you can't include the following fields in the request: `additionalModelRequestFields`, `inferenceConfig`, `system`, or `toolConfig`. Instead, these fields must be defined through Prompt management. For more information, see [Use a prompt from Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html).

For information about the Converse API, see *Use the Converse API* in the *Amazon Bedrock User Guide*. To use a guardrail, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide*. To use a tool with a model, see *Tool use (Function calling)* in the *Amazon Bedrock User Guide*

For example code, see *Converse API examples* in the *Amazon Bedrock User Guide*.

This operation requires permission for the `bedrock:InvokeModel` action.

To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the base inference actions ([InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference).

For troubleshooting some of the common errors you might encounter when using the `Converse` API, see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

## Input (`ConverseRequest`)

### `modelId` — string · **required** · sent as httpLabel

Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:

- If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see [Amazon Bedrock base model IDs (on-demand throughput)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns) in the Amazon Bedrock User Guide.
- If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see [Supported Regions and models for cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the Amazon Bedrock User Guide.
- If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see [Run inference using a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html) in the Amazon Bedrock User Guide.
- If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see [Use a custom model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html) in the Amazon Bedrock User Guide.
- To include a prompt that was defined in [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html), specify the ARN of the prompt version to use.

The Converse API doesn't support [imported models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html).

### `messages` — list<Message>

The messages that you want to send to the model.

### `system` — list<SystemContentBlock>

A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.

### `inferenceConfig` — InferenceConfiguration

Inference parameters to pass to the model. `Converse` and `ConverseStream` support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the `additionalModelRequestFields` request field.

### `toolConfig` — ToolConfiguration

Configuration information for the tools that the model can use when generating a response.

For information about models that support tool use, see [Supported models and model features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features).

### `guardrailConfig` — GuardrailConfiguration

Configuration information for a guardrail that you want to use in the request. If you include `guardContent` blocks in the `content` field in the `messages` field, the guardrail operates only on those messages. If you include no `guardContent` blocks, the guardrail operates on all messages in the request body and in any included prompt resource.

### `additionalModelRequestFields` — document

Additional inference parameters that the model supports, beyond the base set of inference parameters that `Converse` and `ConverseStream` support in the `inferenceConfig` field. For more information, see [Model parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `promptVariables` — map<string, PromptVariableValues>

Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the `modelId` field.

### `additionalModelResponseFieldPaths` — list<string>

Additional model parameters field paths to return in the response. `Converse` and `ConverseStream` return the requested fields as a JSON Pointer object in the `additionalModelResponseFields` field. The following is example JSON for `additionalModelResponseFieldPaths`.

`[ "/stop_sequence" ]`

For information about the JSON Pointer syntax, see the [Internet Engineering Task Force (IETF)](https://datatracker.ietf.org/doc/html/rfc6901) documentation.

`Converse` and `ConverseStream` reject an empty JSON Pointer or incorrectly structured JSON Pointer with a `400` error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by `Converse`.

### `requestMetadata` — map<string, string>

Key-value pairs that you can use to filter invocation logs.

### `performanceConfig` — PerformanceConfiguration

Model performance settings for the request.

### `serviceTier` — ServiceTier

Specifies the processing tier configuration used for serving the request.

### `outputConfig` — OutputConfig

Output configuration for a model response.

## Output (`ConverseResponse`)

### `output` — ConverseOutput · **required**

The result from the call to `Converse`.

### `stopReason` — StopReason (enum) · **required**

The reason why the model stopped generating output.

Values: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `guardrail_intervened`, `content_filtered`, `malformed_model_output`, `malformed_tool_use`, `model_context_window_exceeded`

### `usage` — TokenUsage · **required**

The total number of tokens used in the call to `Converse`. The total includes the tokens input to the model and the tokens generated by the model.

### `metrics` — ConverseMetrics · **required**

Metrics for the call to `Converse`.

### `additionalModelResponseFields` — document

Additional fields in the response that are unique to the model.

### `trace` — ConverseTrace

A trace object that contains information about the Guardrail behavior.

### `performanceConfig` — PerformanceConfiguration

Model performance settings for the request.

### `serviceTier` — ServiceTier

Specifies the processing tier configuration used for serving the request.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ModelErrorException` — The request failed due to an error while processing the model.
- `ModelNotReadyException` — The model specified in the request is not ready to serve inference requests.
- `ModelTimeoutException` — The request took too long to process.
- `ResourceNotFoundException` — The specified resource ARN was not found.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
