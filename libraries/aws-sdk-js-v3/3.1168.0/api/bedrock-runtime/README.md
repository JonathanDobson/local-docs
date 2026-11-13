# Amazon Bedrock Runtime — API reference

API version `2023-09-30` · protocol restJson1 · SDK for JavaScript v3 client `@aws-sdk/client-bedrock-runtime`

Describes the API operations for running inference using Amazon Bedrock models.

## Operations (11)

- [`ApplyGuardrail`](operations/ApplyGuardrail.md) — The action to apply a guardrail.
- [`Converse`](operations/Converse.md) — Sends messages to the specified Amazon Bedrock model.
- [`ConverseStream`](operations/ConverseStream.md) — Sends messages to the specified Amazon Bedrock model and returns the response in a stream.
- [`CountTokens`](operations/CountTokens.md) — Returns the token count for a given inference request.
- [`GetAsyncInvoke`](operations/GetAsyncInvoke.md) — Retrieve information about an asynchronous invocation.
- [`InvokeGuardrailChecks`](operations/InvokeGuardrailChecks.md) — Evaluates messages against inline guardrail checks.
- [`InvokeModel`](operations/InvokeModel.md) — Invokes the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body.
- [`InvokeModelWithBidirectionalStream`](operations/InvokeModelWithBidirectionalStream.md) — Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream.
- [`InvokeModelWithResponseStream`](operations/InvokeModelWithResponseStream.md) — Invoke the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body.
- [`ListAsyncInvokes`](operations/ListAsyncInvokes.md) — Lists asynchronous invocations.
- [`StartAsyncInvoke`](operations/StartAsyncInvoke.md) — Starts an asynchronous invocation.
