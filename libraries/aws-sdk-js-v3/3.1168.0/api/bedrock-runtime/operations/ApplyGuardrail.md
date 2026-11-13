# ApplyGuardrail

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `ApplyGuardrailCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `POST /guardrail/{guardrailIdentifier}/version/{guardrailVersion}/apply`

The action to apply a guardrail.

For troubleshooting some of the common errors you might encounter when using the `ApplyGuardrail` API, see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

## Input (`ApplyGuardrailRequest`)

### `guardrailIdentifier` — string · **required** · sent as httpLabel

The guardrail identifier used in the request to apply the guardrail.

### `guardrailVersion` — string · **required** · sent as httpLabel

The guardrail version used in the request to apply the guardrail.

### `source` — GuardrailContentSource (enum) · **required**

The source of data used in the request to apply the guardrail.

Values: `INPUT`, `OUTPUT`

### `content` — list<GuardrailContentBlock> · **required**

The content details used in the request to apply the guardrail.

### `outputScope` — GuardrailOutputScope (enum)

Specifies the scope of the output that you get in the response. Set to `FULL` to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.

Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).

Values: `INTERVENTIONS`, `FULL`

## Output (`ApplyGuardrailResponse`)

### `usage` — GuardrailUsage · **required**

The usage details in the response from the guardrail.

### `action` — GuardrailAction (enum) · **required**

The action taken in the response from the guardrail.

Values: `NONE`, `GUARDRAIL_INTERVENED`

### `actionReason` — string

The reason for the action taken when harmful content is detected.

### `outputs` — list<GuardrailOutputContent> · **required**

The output details in the response from the guardrail.

### `assessments` — list<GuardrailAssessment> · **required**

The assessment details in the response from the guardrail.

### `guardrailCoverage` — GuardrailCoverage

The guardrail coverage details in the apply guardrail response.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ResourceNotFoundException` — The specified resource ARN was not found.
- `ServiceQuotaExceededException` — Your request exceeds the service quota for your account.
- `ServiceUnavailableException` — The service isn't currently available.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
