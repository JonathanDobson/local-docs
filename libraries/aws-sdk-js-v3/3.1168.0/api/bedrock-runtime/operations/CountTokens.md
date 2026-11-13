# CountTokens

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `CountTokensCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /model/{modelId}/count-tokens`

Returns the token count for a given inference request. This operation helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.

Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model in an `InvokeModel` or `Converse` request.

You can use this operation to:

- Estimate costs before sending inference requests.
- Optimize prompts to fit within token limits.
- Plan for token usage in your applications.

This operation accepts the same input formats as `InvokeModel` and `Converse`, allowing you to count tokens for both raw text inputs and structured conversation formats.

The following operations are related to `CountTokens`:

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_InvokeModel.html) - Sends inference requests to foundation models
- [Converse](https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_Converse.html) - Sends conversation-based inference requests to foundation models

## Input (`CountTokensRequest`)

### `modelId` — string · **required** · sent as httpLabel

The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.

### `input` — CountTokensInput · **required**

The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an `InvokeModel` or `Converse` request:

- For `InvokeModel` requests, provide the request body in the `invokeModel` field
- For `Converse` requests, provide the messages and system content in the `converse` field

The input format must be compatible with the model specified in the `modelId` parameter.

## Output (`CountTokensResponse`)

### `inputTokens` — integer · **required**

The number of tokens in the provided input according to the specified model's tokenization rules. This count represents the number of input tokens that would be processed if the same input were sent to the model in an inference request. Use this value to estimate costs and ensure your inputs stay within model token limits.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ResourceNotFoundException` — The specified resource ARN was not found.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
