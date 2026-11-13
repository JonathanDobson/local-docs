# InvokeGuardrailChecks

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `InvokeGuardrailChecksCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /guardrail-checks/invoke`

Evaluates messages against inline guardrail checks. You specify the check configurations directly in the request, and Amazon Bedrock returns per-check results with severity or confidence scores.

## Input (`InvokeGuardrailChecksRequest`)

### `messages` — list<GuardrailChecksMessage> · **required**

The messages to evaluate against the specified guardrail checks. Each message includes a role and one or more content blocks.

### `checks` — GuardrailChecksConfig · **required**

The inline check configurations that specify which guardrail checks to run against the messages.

## Output (`InvokeGuardrailChecksResponse`)

### `results` — GuardrailChecksResults · **required**

The per-check results containing findings from the guardrail evaluation.

### `usage` — GuardrailChecksUsageResults · **required**

The per-check text unit consumption for the guardrail evaluation.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
