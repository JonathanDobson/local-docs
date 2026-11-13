# InvokeModelWithResponseStream

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `InvokeModelWithResponseStreamCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /model/{modelId}/invoke-with-response-stream`

Invoke the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. The response is returned in a stream.

To see if a model supports streaming, call [GetFoundationModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html) and check the `responseStreamingSupported` field in the response.

The CLI doesn't support streaming operations in Amazon Bedrock, including `InvokeModelWithResponseStream`.

For example code, see *Invoke model with streaming code example* in the *Amazon Bedrock User Guide*.

This operation requires permissions to perform the `bedrock:InvokeModelWithResponseStream` action.

To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the Converse API actions ([Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference).

For troubleshooting some of the common errors you might encounter when using the `InvokeModelWithResponseStream` API, see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

## Input (`InvokeModelWithResponseStreamRequest`)

### `body` — blob · sent as httpPayload

The prompt and inference parameters in the format specified in the `contentType` in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html). For more information, see [Run inference](https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html) in the Bedrock User Guide.

### `contentType` — string · sent as header `Content-Type`

The MIME type of the input data in the request. You must specify `application/json`.

### `accept` — string · sent as header `X-Amzn-Bedrock-Accept`

The desired MIME type of the inference body in the response. The default value is `application/json`.

### `modelId` — string · **required** · sent as httpLabel

The unique identifier of the model to invoke to run inference.

The `modelId` to provide depends on the type of model or throughput that you use:

- If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see [Amazon Bedrock base model IDs (on-demand throughput)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns) in the Amazon Bedrock User Guide.
- If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see [Supported Regions and models for cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the Amazon Bedrock User Guide.
- If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see [Run inference using a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html) in the Amazon Bedrock User Guide.
- If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see [Use a custom model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html) in the Amazon Bedrock User Guide.
- If you use an [imported model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), specify the ARN of the imported model. You can get the model ARN from a successful call to [CreateModelImportJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html) or from the Imported models page in the Amazon Bedrock console.

### `trace` — Trace (enum) · sent as header `X-Amzn-Bedrock-Trace`

Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.

Values: `ENABLED`, `DISABLED`, `ENABLED_FULL`

### `guardrailIdentifier` — string · sent as header `X-Amzn-Bedrock-GuardrailIdentifier`

The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.

An error is thrown in the following situations.

- You don't provide a guardrail identifier but you specify the `amazon-bedrock-guardrailConfig` field in the request body.
- You enable the guardrail but the `contentType` isn't `application/json`.
- You provide a guardrail identifier, but `guardrailVersion` isn't specified.

### `guardrailVersion` — string · sent as header `X-Amzn-Bedrock-GuardrailVersion`

The version number for the guardrail. The value can also be `DRAFT`.

### `performanceConfigLatency` — PerformanceConfigLatency (enum) · sent as header `X-Amzn-Bedrock-PerformanceConfig-Latency` · default `"standard"`

Model performance settings for the request.

Values: `standard`, `optimized`

### `serviceTier` — ServiceTierType (enum) · sent as header `X-Amzn-Bedrock-Service-Tier`

Specifies the processing tier type used for serving the request.

Values: `priority`, `default`, `flex`, `reserved`

### `requestMetadata` — string · sent as header `X-Amzn-Bedrock-Request-Metadata`

Key-value pairs that you can use to filter invocation logs.

## Output (`InvokeModelWithResponseStreamResponse`)

### `body` — ResponseStream · **required** · sent as httpPayload

Inference response from the model in the format specified by the `contentType` header. To see the format and content of this field for different models, refer to [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `contentType` — string · **required** · sent as header `X-Amzn-Bedrock-Content-Type`

The MIME type of the inference result.

### `performanceConfigLatency` — PerformanceConfigLatency (enum) · sent as header `X-Amzn-Bedrock-PerformanceConfig-Latency`

Model performance settings for the request.

Values: `standard`, `optimized`

### `serviceTier` — ServiceTierType (enum) · sent as header `X-Amzn-Bedrock-Service-Tier`

Specifies the processing tier type used for serving the request.

Values: `priority`, `default`, `flex`, `reserved`

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
