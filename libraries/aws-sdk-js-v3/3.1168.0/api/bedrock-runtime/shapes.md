# Amazon Bedrock Runtime — data types

Structures, unions and enums used by the operations (operation inputs and outputs are on the operation pages).

## AnyToolChoice (structure)

The model must request at least one tool (no text is generated). For example, `{"any" : {}}`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## AppliedGuardrailDetails (structure)

Details about the specific guardrail that was applied during this assessment, including its identifier, version, ARN, origin, and ownership information.

### `guardrailId` — string

The unique ID of the guardrail that was applied.

### `guardrailVersion` — string

The version of the guardrail that was applied.

### `guardrailArn` — string

The ARN of the guardrail that was applied.

### `guardrailOrigin` — list<GuardrailOrigin (enum)>

The origin of how the guardrail was applied. This can be either requested at the API level or enforced at the account or organization level as a default guardrail.

### `guardrailOwnership` — GuardrailOwnership (enum)

The ownership type of the guardrail, indicating whether it is owned by the requesting account or is a cross-account guardrail shared from another AWS account.

Values: `SELF`, `CROSS_ACCOUNT`

## AsyncInvokeOutputDataConfig (union)

Asynchronous invocation output data settings.

### `s3OutputDataConfig` — AsyncInvokeS3OutputDataConfig

A storage location for the output data in an S3 bucket

## AsyncInvokeS3OutputDataConfig (structure)

Asynchronous invocation output data settings.

### `s3Uri` — string · **required**

An object URI starting with `s3://`.

### `kmsKeyId` — string

A KMS encryption key ID.

### `bucketOwner` — string

If the bucket belongs to another AWS account, specify that account's ID.

## AsyncInvokeStatus (enum)

Values: `InProgress`, `Completed`, `Failed`

## AsyncInvokeSummary (structure)

A summary of an asynchronous invocation.

### `invocationArn` — string · **required**

The invocation's ARN.

### `modelArn` — string · **required**

The invoked model's ARN.

### `clientRequestToken` — string

The invocation's idempotency token.

### `status` — AsyncInvokeStatus (enum)

The invocation's status.

Values: `InProgress`, `Completed`, `Failed`

### `failureMessage` — string

An error message.

### `submitTime` — timestamp · **required**

When the invocation was submitted.

### `lastModifiedTime` — timestamp

When the invocation was last modified.

### `endTime` — timestamp

When the invocation ended.

### `outputDataConfig` — AsyncInvokeOutputDataConfig · **required**

The invocation's output data settings.

## AudioBlock (structure)

An audio content block that contains audio data in various supported formats.

### `format` — AudioFormat (enum) · **required**

The format of the audio data, such as MP3, WAV, FLAC, or other supported audio formats.

Values: `mp3`, `opus`, `wav`, `aac`, `flac`, `mp4`, `ogg`, `mkv`, `mka`, `x-aac`, `m4a`, `mpeg`, `mpga`, `pcm`, `webm`

### `source` — AudioSource · **required**

The source of the audio data, which can be provided as raw bytes or an S3 location.

### `error` — ErrorBlock

Error information if the audio block could not be processed or contains invalid data.

## AudioFormat (enum)

Values: `mp3`, `opus`, `wav`, `aac`, `flac`, `mp4`, `ogg`, `mkv`, `mka`, `x-aac`, `m4a`, `mpeg`, `mpga`, `pcm`, `webm`

## AudioSource (union)

The source of audio data, which can be provided either as raw bytes or a reference to an S3 location.

### `bytes` — blob

Audio data encoded in base64.

### `s3Location` — S3Location

A reference to audio data stored in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

## AutoToolChoice (structure)

The Model automatically decides if a tool should be called or whether to generate text instead. For example, `{"auto" : {}}`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide

## BidirectionalInputPayloadPart (structure)

Payload content for the bidirectional input. The input is an audio stream.

### `bytes` — blob

The audio content for the bidirectional input.

## BidirectionalOutputPayloadPart (structure)

Output from the bidirectional stream. The output is speech and a text transcription.

### `bytes` — blob

The speech output of the bidirectional stream.

## CacheDetail (structure)

Cache creation metrics for a specific TTL duration

### `ttl` — CacheTTL (enum) · **required**

TTL duration for these cached tokens

Values: `5m`, `1h`

### `inputTokens` — integer · **required**

Number of tokens written to cache with this TTL (cache creation tokens)

## CachePointBlock (structure)

Defines a section of content to be cached for reuse in subsequent API calls.

### `type` — CachePointType (enum) · **required**

Specifies the type of cache point within the CachePointBlock.

Values: `default`

### `ttl` — CacheTTL (enum)

Optional TTL duration for cache entries. When specified, enables extended TTL caching with the specified duration. When omitted, uses `type` value for caching behavior.

Values: `5m`, `1h`

## CachePointType (enum)

Values: `default`

## CacheTTL (enum)

Time-to-live duration for ephemeral cache entries

Values: `5m`, `1h`

## Citation (structure)

Contains information about a citation that references a specific source document. Citations provide traceability between the model's generated response and the source documents that informed that response.

### `title` — string

The title or identifier of the source document being cited.

### `source` — string

The source from the original search result that provided the cited content.

### `sourceContent` — list<CitationSourceContent>

The specific content from the source document that was referenced or cited in the generated response.

### `location` — CitationLocation

The precise location within the source document where the cited content can be found, including character positions, page numbers, or chunk identifiers.

## CitationGeneratedContent (union)

Contains the generated text content that corresponds to or is supported by a citation from a source document.

### `text` — string

The text content that was generated by the model and is supported by the associated citation.

## CitationLocation (union)

Specifies the precise location within a source document where cited content can be found. This can include character-level positions, page numbers, or document chunks depending on the document type and indexing method.

### `web` — WebLocation

The web URL that was cited for this reference.

### `documentChar` — DocumentCharLocation

The character-level location within the document where the cited content is found.

### `documentPage` — DocumentPageLocation

The page-level location within the document where the cited content is found.

### `documentChunk` — DocumentChunkLocation

The chunk-level location within the document where the cited content is found, typically used for documents that have been segmented into logical chunks.

### `searchResultLocation` — SearchResultLocation

The search result location where the cited content is found, including the search result index and block positions within the content array.

## CitationSourceContent (union)

Contains the actual text content from a source document that is being cited or referenced in the model's response.

### `text` — string

The text content from the source document that is being cited.

## CitationSourceContentDelta (structure)

Contains incremental updates to the source content text during streaming responses, allowing clients to build up the cited content progressively.

### `text` — string

An incremental update to the text content from the source document that is being cited.

## CitationsConfig (structure)

Configuration settings for enabling and controlling document citations in Converse API responses. When enabled, the model can include citation information that links generated content back to specific source documents.

### `enabled` — boolean · **required**

Specifies whether citations from the selected document should be used in the model's response. When set to true, the model can generate citations that reference the source documents used to inform the response.

## CitationsContentBlock (structure)

A content block that contains both generated text and associated citation information. This block type is returned when document citations are enabled, providing traceability between the generated content and the source documents that informed the response.

### `content` — list<CitationGeneratedContent>

The generated content that is supported by the associated citations.

### `citations` — list<Citation>

An array of citations that reference the source documents used to generate the associated content.

## CitationsDelta (structure)

Contains incremental updates to citation information during streaming responses. This allows clients to build up citation data progressively as the response is generated.

### `title` — string

The title or identifier of the source document being cited.

### `source` — string

The source from the original search result that provided the cited content.

### `sourceContent` — list<CitationSourceContentDelta>

The specific content from the source document that was referenced or cited in the generated response.

### `location` — CitationLocation

Specifies the precise location within a source document where cited content can be found. This can include character-level positions, page numbers, or document chunks depending on the document type and indexing method.

## ContentBlock (union)

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

### `text` — string

Text to include in the message.

### `image` — ImageBlock

Image to include in the message.

This field is only supported by Anthropic Claude 3 models.

### `document` — DocumentBlock

A document to include in the message.

### `video` — VideoBlock

Video to include in the message.

### `audio` — AudioBlock

An audio content block containing audio data in the conversation.

### `toolUse` — ToolUseBlock

Information about a tool use request from a model.

### `toolResult` — ToolResultBlock

The result for a tool request that a model makes.

### `guardContent` — GuardrailConverseContentBlock

Contains the content to assess with the guardrail. If you don't specify `guardContent` in a call to the Converse API, the guardrail (if passed in the Converse API) assesses the entire message.

For more information, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide*.

### `cachePoint` — CachePointBlock

CachePoint to include in the message.

### `reasoningContent` — ReasoningContentBlock

Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### `citationsContent` — CitationsContentBlock

A content block that contains both generated text and associated citation information, providing traceability between the response and source documents.

### `searchResult` — SearchResultBlock

Search result to include in the message.

### `toolAddition` — ToolAdditionBlock

A content block for adding a tool to the available tool set mid-conversation. Each block references a single tool via its `tool` field. Use within a `system` role message to make a tool available without re-sending the full tool configuration.

### `toolRemoval` — ToolRemovalBlock

A content block for removing a tool from the available tool set mid-conversation. Each block references a single tool via its `tool` field. Use within a `system` role message to remove a tool without re-sending the full tool configuration.

## ContentBlockDelta (union)

A block of content in a streaming response.

### `text` — string

The content text.

### `toolUse` — ToolUseBlockDelta

Information about a tool that the model is requesting to use.

### `toolResult` — list<ToolResultBlockDelta>

An incremental update that contains the results from a tool call.

### `reasoningContent` — ReasoningContentBlockDelta

Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### `citation` — CitationsDelta

Incremental citation information that is streamed as part of the response generation process.

### `image` — ImageBlockDelta

A streaming delta event containing incremental image data.

## ContentBlockDeltaEvent (structure)

The content block delta event.

### `delta` — ContentBlockDelta · **required**

The delta for a content block delta event.

### `contentBlockIndex` — integer · **required**

The block index for a content block delta event.

## ContentBlockStart (union)

Content block start information.

### `toolUse` — ToolUseBlockStart

Information about a tool that the model is requesting to use.

### `toolResult` — ToolResultBlockStart

The

### `image` — ImageBlockStart

The initial event indicating the start of a streaming image block.

## ContentBlockStartEvent (structure)

Content block start event.

### `start` — ContentBlockStart · **required**

Start information about a content block start event.

### `contentBlockIndex` — integer · **required**

The index for a content block start event.

## ContentBlockStopEvent (structure)

A content block stop event.

### `contentBlockIndex` — integer · **required**

The index for a content block.

## ConversationRole (enum)

Values: `user`, `assistant`, `system`

## ConverseMetrics (structure)

Metrics for a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html).

### `latencyMs` — long · **required**

The latency of the call to `Converse`, in milliseconds.

## ConverseOutput (union)

The output from a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html).

### `message` — Message

The message that the model generates.

## ConverseStreamMetadataEvent (structure)

A conversation stream metadata event.

### `usage` — TokenUsage · **required**

Usage information for the conversation stream event.

### `metrics` — ConverseStreamMetrics · **required**

The metrics for the conversation stream metadata event.

### `trace` — ConverseStreamTrace

The trace object in the response from [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) that contains information about the guardrail behavior.

### `performanceConfig` — PerformanceConfiguration

Model performance configuration metadata for the conversation stream event.

### `serviceTier` — ServiceTier

Specifies the processing tier configuration used for serving the request.

## ConverseStreamMetrics (structure)

Metrics for the stream.

### `latencyMs` — long · **required**

The latency for the streaming request, in milliseconds.

## ConverseStreamOutput (union)

The messages output stream

### `messageStart` — MessageStartEvent

Message start information.

### `contentBlockStart` — ContentBlockStartEvent

Start information for a content block.

### `contentBlockDelta` — ContentBlockDeltaEvent

The messages output content block delta.

### `contentBlockStop` — ContentBlockStopEvent

Stop information for a content block.

### `messageStop` — MessageStopEvent

Message stop information.

### `metadata` — ConverseStreamMetadataEvent

Metadata for the converse output stream.

### `internalServerException` — InternalServerException

An internal server error occurred. Retry your request.

### `modelStreamErrorException` — ModelStreamErrorException

A streaming error occurred. Retry your request.

### `validationException` — ValidationException

The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide.

### `throttlingException` — ThrottlingException

Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide.

### `serviceUnavailableException` — ServiceUnavailableException

The service isn't currently available. For troubleshooting this error, see [ServiceUnavailable](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable) in the Amazon Bedrock User Guide

## ConverseStreamTrace (structure)

The trace object in a response from [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

### `guardrail` — GuardrailTraceAssessment

The guardrail trace object.

### `promptRouter` — PromptRouterTrace

The request's prompt router.

## ConverseTokensRequest (structure)

The inputs from a `Converse` API request for token counting.

This structure mirrors the input format for the `Converse` operation, allowing you to count tokens for conversation-based inference requests.

### `messages` — list<Message>

An array of messages to count tokens for.

### `system` — list<SystemContentBlock>

The system content blocks to count tokens for. System content provides instructions or context to the model about how it should behave or respond. The token count will include any system content provided.

### `toolConfig` — ToolConfiguration

The toolConfig of Converse input request to count tokens for. Configuration information for the tools that the model can use when generating a response.

### `additionalModelRequestFields` — document

The additionalModelRequestFields of Converse input request to count tokens for. Use this field when you want to pass additional parameters that the model supports.

## ConverseTrace (structure)

The trace object in a response from [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html).

### `guardrail` — GuardrailTraceAssessment

The guardrail trace object.

### `promptRouter` — PromptRouterTrace

The request's prompt router.

## CountTokensInput (union)

The input value for token counting. The value should be either an `InvokeModel` or `Converse` request body.

### `invokeModel` — InvokeModelTokensRequest

An `InvokeModel` request for which to count tokens. Use this field when you want to count tokens for a raw text input that would be sent to the `InvokeModel` operation.

### `converse` — ConverseTokensRequest

A `Converse` request for which to count tokens. Use this field when you want to count tokens for a conversation-based input that would be sent to the `Converse` operation.

## DocumentBlock (structure)

A document to include in a message.

### `format` — DocumentFormat (enum) · default `"txt"`

The format of a document, or its extension.

Values: `pdf`, `csv`, `doc`, `docx`, `xls`, `xlsx`, `html`, `txt`, `md`

### `name` — string · **required**

A name for the document. The name can only contain the following characters:

- Alphanumeric characters
- Whitespace characters (no more than one in a row)
- Hyphens
- Parentheses
- Square brackets

This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.

### `source` — DocumentSource · **required**

Contains the content of the document.

### `context` — string

Contextual information about how the document should be processed or interpreted by the model when generating citations.

### `citations` — CitationsConfig

Configuration settings that control how citations should be generated for this specific document.

## DocumentCharLocation (structure)

Specifies a character-level location within a document, providing precise positioning information for cited content using start and end character indices.

### `documentIndex` — integer

The index of the document within the array of documents provided in the request.

### `start` — integer

The starting character position of the cited content within the document.

### `end` — integer

The ending character position of the cited content within the document.

## DocumentChunkLocation (structure)

Specifies a chunk-level location within a document, providing positioning information for cited content using logical document segments or chunks.

### `documentIndex` — integer

The index of the document within the array of documents provided in the request.

### `start` — integer

The starting chunk identifier or index of the cited content within the document.

### `end` — integer

The ending chunk identifier or index of the cited content within the document.

## DocumentContentBlock (union)

Contains the actual content of a document that can be processed by the model and potentially cited in the response.

### `text` — string

The text content of the document.

## DocumentFormat (enum)

Values: `pdf`, `csv`, `doc`, `docx`, `xls`, `xlsx`, `html`, `txt`, `md`

## DocumentPageLocation (structure)

Specifies a page-level location within a document, providing positioning information for cited content using page numbers.

### `documentIndex` — integer

The index of the document within the array of documents provided in the request.

### `start` — integer

The starting page number of the cited content within the document.

### `end` — integer

The ending page number of the cited content within the document.

## DocumentSource (union)

Contains the content of a document.

### `bytes` — blob

The raw bytes for the document. If you use an Amazon Web Services SDK, you don't need to encode the bytes in base64.

### `s3Location` — S3Location

The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

### `text` — string

The text content of the document source.

### `content` — list<DocumentContentBlock>

The structured content of the document source, which may include various content blocks such as text, images, or other document elements.

## ErrorBlock (structure)

A block containing error information when content processing fails.

### `message` — string

A human-readable error message describing what went wrong during content processing.

## GuardrailAction (enum)

Values: `NONE`, `GUARDRAIL_INTERVENED`

## GuardrailAssessment (structure)

A behavior assessment of the guardrail policies used in a call to the Converse API.

### `topicPolicy` — GuardrailTopicPolicyAssessment

The topic policy.

### `contentPolicy` — GuardrailContentPolicyAssessment

The content policy.

### `wordPolicy` — GuardrailWordPolicyAssessment

The word policy.

### `sensitiveInformationPolicy` — GuardrailSensitiveInformationPolicyAssessment

The sensitive information policy.

### `contextualGroundingPolicy` — GuardrailContextualGroundingPolicyAssessment

The contextual grounding policy used for the guardrail assessment.

### `automatedReasoningPolicy` — GuardrailAutomatedReasoningPolicyAssessment

The automated reasoning policy assessment results, including logical validation findings for the input content.

### `invocationMetrics` — GuardrailInvocationMetrics

The invocation metrics for the guardrail assessment.

### `appliedGuardrailDetails` — AppliedGuardrailDetails

Details about the specific guardrail that was applied during this assessment, including its identifier, version, ARN, origin, and ownership information.

## GuardrailAutomatedReasoningFinding (union)

Represents a logical validation result from automated reasoning policy evaluation. The finding indicates whether claims in the input are logically valid, invalid, satisfiable, impossible, or have other logical issues.

### `valid` — GuardrailAutomatedReasoningValidFinding

Contains the result when the automated reasoning evaluation determines that the claims in the input are logically valid and definitively true based on the provided premises and policy rules.

### `invalid` — GuardrailAutomatedReasoningInvalidFinding

Contains the result when the automated reasoning evaluation determines that the claims in the input are logically invalid and contradict the established premises or policy rules.

### `satisfiable` — GuardrailAutomatedReasoningSatisfiableFinding

Contains the result when the automated reasoning evaluation determines that the claims in the input could be either true or false depending on additional assumptions not provided in the input context.

### `impossible` — GuardrailAutomatedReasoningImpossibleFinding

Contains the result when the automated reasoning evaluation determines that no valid logical conclusions can be drawn due to contradictions in the premises or policy rules themselves.

### `translationAmbiguous` — GuardrailAutomatedReasoningTranslationAmbiguousFinding

Contains the result when the automated reasoning evaluation detects that the input has multiple valid logical interpretations, requiring additional context or clarification to proceed with validation.

### `tooComplex` — GuardrailAutomatedReasoningTooComplexFinding

Contains the result when the automated reasoning evaluation cannot process the input due to its complexity or volume exceeding the system's processing capacity for logical analysis.

### `noTranslations` — GuardrailAutomatedReasoningNoTranslationsFinding

Contains the result when the automated reasoning evaluation cannot extract any relevant logical information from the input that can be validated against the policy rules.

## GuardrailAutomatedReasoningImpossibleFinding (structure)

Indicates that no valid claims can be made due to logical contradictions in the premises or rules.

### `translation` — GuardrailAutomatedReasoningTranslation

The logical translation of the input that this finding evaluates.

### `contradictingRules` — list<GuardrailAutomatedReasoningRule>

The automated reasoning policy rules that contradict the claims and/or premises in the input.

### `logicWarning` — GuardrailAutomatedReasoningLogicWarning

Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.

## GuardrailAutomatedReasoningInputTextReference (structure)

References a portion of the original input text that corresponds to logical elements.

### `text` — string

The specific text from the original input that this reference points to.

## GuardrailAutomatedReasoningInvalidFinding (structure)

Indicates that the claims are logically false and contradictory to the established rules or premises.

### `translation` — GuardrailAutomatedReasoningTranslation

The logical translation of the input that this finding invalidates.

### `contradictingRules` — list<GuardrailAutomatedReasoningRule>

The automated reasoning policy rules that contradict the claims in the input.

### `logicWarning` — GuardrailAutomatedReasoningLogicWarning

Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.

## GuardrailAutomatedReasoningLogicWarning (structure)

Identifies logical issues in the translated statements that exist independent of any policy rules, such as statements that are always true or always false.

### `type` — GuardrailAutomatedReasoningLogicWarningType (enum)

The category of the detected logical issue, such as statements that are always true or always false.

Values: `ALWAYS_FALSE`, `ALWAYS_TRUE`

### `premises` — list<GuardrailAutomatedReasoningStatement>

The logical statements that serve as premises under which the claims are validated.

### `claims` — list<GuardrailAutomatedReasoningStatement>

The logical statements that are validated while assuming the policy and premises.

## GuardrailAutomatedReasoningLogicWarningType (enum)

Values: `ALWAYS_FALSE`, `ALWAYS_TRUE`

## GuardrailAutomatedReasoningNoTranslationsFinding (structure)

Indicates that no relevant logical information could be extracted from the input for validation.

## GuardrailAutomatedReasoningPolicyAssessment (structure)

Contains the results of automated reasoning policy evaluation, including logical findings about the validity of claims made in the input content.

### `findings` — list<GuardrailAutomatedReasoningFinding>

List of logical validation results produced by evaluating the input content against automated reasoning policies.

## GuardrailAutomatedReasoningRule (structure)

References a specific automated reasoning policy rule that was applied during evaluation.

### `identifier` — string

The unique identifier of the automated reasoning rule.

### `policyVersionArn` — string

The ARN of the automated reasoning policy version that contains this rule.

## GuardrailAutomatedReasoningSatisfiableFinding (structure)

Indicates that the claims could be either true or false depending on additional assumptions not provided in the input.

### `translation` — GuardrailAutomatedReasoningTranslation

The logical translation of the input that this finding evaluates.

### `claimsTrueScenario` — GuardrailAutomatedReasoningScenario

An example scenario demonstrating how the claims could be logically true.

### `claimsFalseScenario` — GuardrailAutomatedReasoningScenario

An example scenario demonstrating how the claims could be logically false.

### `logicWarning` — GuardrailAutomatedReasoningLogicWarning

Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.

## GuardrailAutomatedReasoningScenario (structure)

Represents a logical scenario where claims can be evaluated as true or false, containing specific logical assignments.

### `statements` — list<GuardrailAutomatedReasoningStatement>

List of logical assignments and statements that define this scenario.

## GuardrailAutomatedReasoningStatement (structure)

A logical statement that includes both formal logic representation and natural language explanation.

### `logic` — string

The formal logical representation of the statement.

### `naturalLanguage` — string

The natural language explanation of the logical statement.

## GuardrailAutomatedReasoningTooComplexFinding (structure)

Indicates that the input exceeds the processing capacity due to the volume or complexity of the logical information.

## GuardrailAutomatedReasoningTranslation (structure)

Contains the logical translation of natural language input into formal logical statements, including premises, claims, and confidence scores.

### `premises` — list<GuardrailAutomatedReasoningStatement>

The logical statements that serve as the foundation or assumptions for the claims.

### `claims` — list<GuardrailAutomatedReasoningStatement>

The logical statements that are being validated against the premises and policy rules.

### `untranslatedPremises` — list<GuardrailAutomatedReasoningInputTextReference>

References to portions of the original input text that correspond to the premises but could not be fully translated.

### `untranslatedClaims` — list<GuardrailAutomatedReasoningInputTextReference>

References to portions of the original input text that correspond to the claims but could not be fully translated.

### `confidence` — double

A confidence score between 0 and 1 indicating how certain the system is about the logical translation.

## GuardrailAutomatedReasoningTranslationAmbiguousFinding (structure)

Indicates that the input has multiple valid logical interpretations, requiring additional context or clarification.

### `options` — list<GuardrailAutomatedReasoningTranslationOption>

Different logical interpretations that were detected during translation of the input.

### `differenceScenarios` — list<GuardrailAutomatedReasoningScenario>

Scenarios showing how the different translation options differ in meaning.

## GuardrailAutomatedReasoningTranslationOption (structure)

Represents one possible logical interpretation of ambiguous input content.

### `translations` — list<GuardrailAutomatedReasoningTranslation>

Example translations that provide this possible interpretation of the input.

## GuardrailAutomatedReasoningValidFinding (structure)

Indicates that the claims are definitively true and logically implied by the premises, with no possible alternative interpretations.

### `translation` — GuardrailAutomatedReasoningTranslation

The logical translation of the input that this finding validates.

### `claimsTrueScenario` — GuardrailAutomatedReasoningScenario

An example scenario demonstrating how the claims are logically true.

### `supportingRules` — list<GuardrailAutomatedReasoningRule>

The automated reasoning policy rules that support why this result is considered valid.

### `logicWarning` — GuardrailAutomatedReasoningLogicWarning

Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.

## GuardrailChecksConfig (structure)

The configuration for inline guardrail checks. Specify one or more check types to run against the messages.

### `contentFilter` — GuardrailChecksContentFilterConfig

The content filter check configuration.

### `promptAttack` — GuardrailChecksPromptAttackConfig

The prompt attack check configuration.

### `sensitiveInformation` — GuardrailChecksSensitiveInformationConfig

The sensitive information check configuration.

## GuardrailChecksContentBlock (union)

A content block within a message to evaluate.

### `text` — string

The text content to evaluate.

## GuardrailChecksContentFilterCategory (enum)

The category for content filter evaluation.

Values: `VIOLENCE`, `HATE`, `SEXUAL`, `MISCONDUCT`, `INSULTS`

## GuardrailChecksContentFilterCategoryConfig (structure)

The configuration for a single content filter category to evaluate.

### `category` — GuardrailChecksContentFilterCategory (enum) · **required**

The content filter category to evaluate.

Values: `VIOLENCE`, `HATE`, `SEXUAL`, `MISCONDUCT`, `INSULTS`

## GuardrailChecksContentFilterConfig (structure)

The configuration for the content filter check, specifying which categories to evaluate.

### `categories` — list<GuardrailChecksContentFilterCategoryConfig> · **required**

The content filter categories to evaluate.

## GuardrailChecksContentFilterResult (structure)

The content filter check results.

### `results` — list<GuardrailChecksContentFilterResultEntry> · **required**

The per-category content filter results.

## GuardrailChecksContentFilterResultEntry (structure)

The evaluation result for a single content filter category.

### `category` — GuardrailChecksContentFilterCategory (enum) · **required**

The content filter category that was evaluated.

Values: `VIOLENCE`, `HATE`, `SEXUAL`, `MISCONDUCT`, `INSULTS`

### `severityScore` — double · **required**

The severity score for the category, ranging from 0.0 to 1.0. Higher values indicate greater severity.

## GuardrailChecksContentFilterUsage (structure)

The text unit usage for the content filter check.

### `textUnits` — integer · **required**

The number of text units consumed by the content filter check.

## GuardrailChecksMessage (structure)

A message to evaluate against guardrail checks, containing a role and content blocks.

### `role` — GuardrailChecksRole (enum) · **required**

The role of the message sender.

Values: `user`, `assistant`, `system`

### `content` — list<GuardrailChecksContentBlock> · **required**

The content blocks for the message.

## GuardrailChecksPromptAttackCategory (enum)

The category for prompt attack evaluation.

Values: `JAILBREAK`, `PROMPT_INJECTION`, `PROMPT_LEAKAGE`

## GuardrailChecksPromptAttackCategoryConfig (structure)

The configuration for a single prompt attack category to evaluate.

### `category` — GuardrailChecksPromptAttackCategory (enum) · **required**

The prompt attack category to evaluate.

Values: `JAILBREAK`, `PROMPT_INJECTION`, `PROMPT_LEAKAGE`

## GuardrailChecksPromptAttackConfig (structure)

The configuration for the prompt attack check, specifying which categories to evaluate.

### `categories` — list<GuardrailChecksPromptAttackCategoryConfig> · **required**

The prompt attack categories to evaluate.

## GuardrailChecksPromptAttackResult (structure)

The prompt attack check results.

### `results` — list<GuardrailChecksPromptAttackResultEntry> · **required**

The per-category prompt attack results.

## GuardrailChecksPromptAttackResultEntry (structure)

The evaluation result for a single prompt attack category.

### `category` — GuardrailChecksPromptAttackCategory (enum) · **required**

The prompt attack category that was evaluated.

Values: `JAILBREAK`, `PROMPT_INJECTION`, `PROMPT_LEAKAGE`

### `severityScore` — double · **required**

The severity score for the category, ranging from 0.0 to 1.0. Higher values indicate greater severity.

## GuardrailChecksPromptAttackUsage (structure)

The text unit usage for the prompt attack check.

### `textUnits` — integer · **required**

The number of text units consumed by the prompt attack check.

## GuardrailChecksResults (structure)

The results from the guardrail checks evaluation, organized by check type.

### `contentFilter` — GuardrailChecksContentFilterResult

The content filter check results.

### `promptAttack` — GuardrailChecksPromptAttackResult

The prompt attack check results.

### `sensitiveInformation` — GuardrailChecksSensitiveInformationResult

The sensitive information check results.

## GuardrailChecksRole (enum)

The role of the message sender in the conversation.

Values: `user`, `assistant`, `system`

## GuardrailChecksSensitiveInformationConfig (structure)

The configuration for the sensitive information check, specifying which entity types to detect.

### `entities` — list<GuardrailChecksSensitiveInformationEntityConfig> · **required**

The sensitive information entity types to detect.

## GuardrailChecksSensitiveInformationEntityConfig (structure)

The configuration for a single sensitive information entity type to detect.

### `type` — GuardrailChecksSensitiveInformationEntityType (enum) · **required**

The PII entity type to detect.

Values: `ADDRESS`, `AGE`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `CA_HEALTH_NUMBER`, `CA_SOCIAL_INSURANCE_NUMBER`, `CREDIT_DEBIT_CARD_CVV`, `CREDIT_DEBIT_CARD_EXPIRY`, `CREDIT_DEBIT_CARD_NUMBER`, `DRIVER_ID`, `EMAIL`, `INTERNATIONAL_BANK_ACCOUNT_NUMBER`, `IP_ADDRESS`, `LICENSE_PLATE`, `MAC_ADDRESS`, `NAME`, `PASSWORD`, `PHONE`, `PIN`, `SWIFT_CODE`, `UK_NATIONAL_HEALTH_SERVICE_NUMBER`, `UK_NATIONAL_INSURANCE_NUMBER`, `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`, `URL`, `USERNAME`, `US_BANK_ACCOUNT_NUMBER`, `US_BANK_ROUTING_NUMBER`, `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER`, `US_PASSPORT_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`

## GuardrailChecksSensitiveInformationEntityType (enum)

The type of personally identifiable information (PII) entity to detect.

Values: `ADDRESS`, `AGE`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `CA_HEALTH_NUMBER`, `CA_SOCIAL_INSURANCE_NUMBER`, `CREDIT_DEBIT_CARD_CVV`, `CREDIT_DEBIT_CARD_EXPIRY`, `CREDIT_DEBIT_CARD_NUMBER`, `DRIVER_ID`, `EMAIL`, `INTERNATIONAL_BANK_ACCOUNT_NUMBER`, `IP_ADDRESS`, `LICENSE_PLATE`, `MAC_ADDRESS`, `NAME`, `PASSWORD`, `PHONE`, `PIN`, `SWIFT_CODE`, `UK_NATIONAL_HEALTH_SERVICE_NUMBER`, `UK_NATIONAL_INSURANCE_NUMBER`, `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`, `URL`, `USERNAME`, `US_BANK_ACCOUNT_NUMBER`, `US_BANK_ROUTING_NUMBER`, `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER`, `US_PASSPORT_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`

## GuardrailChecksSensitiveInformationResult (structure)

The sensitive information check results.

### `results` — list<GuardrailChecksSensitiveInformationResultEntry> · **required**

The detected sensitive information entities.

### `truncated` — boolean

Specifies whether the results were truncated because the number of detected entities exceeded the maximum limit.

## GuardrailChecksSensitiveInformationResultEntry (structure)

The detection result for a single sensitive information entity found in the evaluated messages.

### `type` — GuardrailChecksSensitiveInformationEntityType (enum) · **required**

The PII entity type that was detected.

Values: `ADDRESS`, `AGE`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `CA_HEALTH_NUMBER`, `CA_SOCIAL_INSURANCE_NUMBER`, `CREDIT_DEBIT_CARD_CVV`, `CREDIT_DEBIT_CARD_EXPIRY`, `CREDIT_DEBIT_CARD_NUMBER`, `DRIVER_ID`, `EMAIL`, `INTERNATIONAL_BANK_ACCOUNT_NUMBER`, `IP_ADDRESS`, `LICENSE_PLATE`, `MAC_ADDRESS`, `NAME`, `PASSWORD`, `PHONE`, `PIN`, `SWIFT_CODE`, `UK_NATIONAL_HEALTH_SERVICE_NUMBER`, `UK_NATIONAL_INSURANCE_NUMBER`, `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`, `URL`, `USERNAME`, `US_BANK_ACCOUNT_NUMBER`, `US_BANK_ROUTING_NUMBER`, `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER`, `US_PASSPORT_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`

### `confidenceScore` — double · **required**

The confidence score for the detection, ranging from 0.0 to 1.0. Higher values indicate greater confidence.

### `beginOffset` — integer · **required**

The start character offset of the detected entity within the content block.

### `endOffset` — integer · **required**

The end character offset of the detected entity within the content block.

### `messageIndex` — integer · **required**

The zero-based index of the message in the input messages array where the entity was detected.

### `contentIndex` — integer · **required**

The zero-based index of the content block within the message where the entity was detected.

## GuardrailChecksSensitiveInformationUsage (structure)

The text unit usage for the sensitive information check.

### `textUnits` — integer · **required**

The number of text units consumed by the sensitive information check.

## GuardrailChecksUsageResults (structure)

The text unit usage for the guardrail checks evaluation, organized by check type.

### `contentFilter` — GuardrailChecksContentFilterUsage

The text unit usage for the content filter check.

### `promptAttack` — GuardrailChecksPromptAttackUsage

The text unit usage for the prompt attack check.

### `sensitiveInformation` — GuardrailChecksSensitiveInformationUsage

The text unit usage for the sensitive information check.

## GuardrailConfiguration (structure)

Configuration information for a guardrail that you use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) operation.

### `guardrailIdentifier` — string · default `""`

The identifier for the guardrail.

### `guardrailVersion` — string · default `""`

The version of the guardrail.

### `trace` — GuardrailTrace (enum) · default `"disabled"`

The trace behavior for the guardrail.

Values: `enabled`, `disabled`, `enabled_full`

## GuardrailContentBlock (union)

The content block to be evaluated by the guardrail.

### `text` — GuardrailTextBlock

Text within content block to be evaluated by the guardrail.

### `image` — GuardrailImageBlock

Image within guardrail content block to be evaluated by the guardrail.

## GuardrailContentFilter (structure)

The content filter for a guardrail.

### `type` — GuardrailContentFilterType (enum) · **required**

The guardrail type.

Values: `INSULTS`, `HATE`, `SEXUAL`, `VIOLENCE`, `MISCONDUCT`, `PROMPT_ATTACK`

### `confidence` — GuardrailContentFilterConfidence (enum) · **required**

The guardrail confidence.

Values: `NONE`, `LOW`, `MEDIUM`, `HIGH`

### `filterStrength` — GuardrailContentFilterStrength (enum)

The filter strength setting for the guardrail content filter.

Values: `NONE`, `LOW`, `MEDIUM`, `HIGH`

### `action` — GuardrailContentPolicyAction (enum) · **required**

The guardrail action.

Values: `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether content that breaches the guardrail configuration is detected.

## GuardrailContentFilterConfidence (enum)

Values: `NONE`, `LOW`, `MEDIUM`, `HIGH`

## GuardrailContentFilterStrength (enum)

Values: `NONE`, `LOW`, `MEDIUM`, `HIGH`

## GuardrailContentFilterType (enum)

Values: `INSULTS`, `HATE`, `SEXUAL`, `VIOLENCE`, `MISCONDUCT`, `PROMPT_ATTACK`

## GuardrailContentPolicyAction (enum)

Values: `BLOCKED`, `NONE`

## GuardrailContentPolicyAssessment (structure)

An assessment of a content policy for a guardrail.

### `filters` — list<GuardrailContentFilter> · **required**

The content policy filters.

## GuardrailContentQualifier (enum)

Values: `grounding_source`, `query`, `guard_content`

## GuardrailContentSource (enum)

Values: `INPUT`, `OUTPUT`

## GuardrailContextualGroundingFilter (structure)

The details for the guardrails contextual grounding filter.

### `type` — GuardrailContextualGroundingFilterType (enum) · **required**

The contextual grounding filter type.

Values: `GROUNDING`, `RELEVANCE`

### `threshold` — double · **required**

The threshold used by contextual grounding filter to determine whether the content is grounded or not.

### `score` — double · **required**

The score generated by contextual grounding filter.

### `action` — GuardrailContextualGroundingPolicyAction (enum) · **required**

The action performed by the guardrails contextual grounding filter.

Values: `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether content that fails the contextual grounding evaluation (grounding or relevance score less than the corresponding threshold) was detected.

## GuardrailContextualGroundingFilterType (enum)

Values: `GROUNDING`, `RELEVANCE`

## GuardrailContextualGroundingPolicyAction (enum)

Values: `BLOCKED`, `NONE`

## GuardrailContextualGroundingPolicyAssessment (structure)

The policy assessment details for the guardrails contextual grounding filter.

### `filters` — list<GuardrailContextualGroundingFilter>

The filter details for the guardrails contextual grounding filter.

## GuardrailConverseContentBlock (union)

A content block for selective guarding with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

### `text` — GuardrailConverseTextBlock

The text to guard.

### `image` — GuardrailConverseImageBlock

Image within converse content block to be evaluated by the guardrail.

## GuardrailConverseContentQualifier (enum)

Values: `grounding_source`, `query`, `guard_content`

## GuardrailConverseImageBlock (structure)

An image block that contains images that you want to assess with a guardrail.

### `format` — GuardrailConverseImageFormat (enum) · **required**

The format details for the image type of the guardrail converse image block.

Values: `png`, `jpeg`

### `source` — GuardrailConverseImageSource · **required**

The image source (image bytes) of the guardrail converse image block.

## GuardrailConverseImageFormat (enum)

Values: `png`, `jpeg`

## GuardrailConverseImageSource (union)

The image source (image bytes) of the guardrail converse image source.

### `bytes` — blob

The raw image bytes for the image.

## GuardrailConverseTextBlock (structure)

A text block that contains text that you want to assess with a guardrail. For more information, see [GuardrailConverseContentBlock](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailConverseContentBlock.html).

### `text` — string · **required**

The text that you want to guard.

### `qualifiers` — list<GuardrailConverseContentQualifier (enum)>

The qualifier details for the guardrails contextual grounding filter.

## GuardrailCoverage (structure)

The action of the guardrail coverage details.

### `textCharacters` — GuardrailTextCharactersCoverage

The text characters of the guardrail coverage details.

### `images` — GuardrailImageCoverage

The guardrail coverage for images (the number of images that guardrails guarded).

## GuardrailCustomWord (structure)

A custom word configured in a guardrail.

### `match` — string · **required**

The match for the custom word.

### `action` — GuardrailWordPolicyAction (enum) · **required**

The action for the custom word.

Values: `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether custom word content that breaches the guardrail configuration is detected.

## GuardrailImageBlock (structure)

Contain an image which user wants guarded. This block is accepted by the guardrails independent API.

### `format` — GuardrailImageFormat (enum) · **required**

The format details for the file type of the image blocked by the guardrail.

Values: `png`, `jpeg`

### `source` — GuardrailImageSource · **required**

The image source (image bytes) details of the image blocked by the guardrail.

## GuardrailImageCoverage (structure)

The details of the guardrail image coverage.

### `guarded` — integer

The count (integer) of images guardrails guarded.

### `total` — integer

Represents the total number of images (integer) that were in the request (guarded and unguarded).

## GuardrailImageFormat (enum)

Values: `png`, `jpeg`

## GuardrailImageSource (union)

The image source (image bytes) of the guardrail image source. Object used in independent api.

### `bytes` — blob

The bytes details of the guardrail image source. Object used in independent api.

## GuardrailInvocationMetrics (structure)

The invocation metrics for the guardrail.

### `guardrailProcessingLatency` — long

The processing latency details for the guardrail invocation metrics.

### `usage` — GuardrailUsage

The usage details for the guardrail invocation metrics.

### `guardrailCoverage` — GuardrailCoverage

The coverage details for the guardrail invocation metrics.

## GuardrailManagedWord (structure)

A managed word configured in a guardrail.

### `match` — string · **required**

The match for the managed word.

### `type` — GuardrailManagedWordType (enum) · **required**

The type for the managed word.

Values: `PROFANITY`

### `action` — GuardrailWordPolicyAction (enum) · **required**

The action for the managed word.

Values: `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether managed word content that breaches the guardrail configuration is detected.

## GuardrailManagedWordType (enum)

Values: `PROFANITY`

## GuardrailOrigin (enum)

Values: `REQUEST`, `ACCOUNT_ENFORCED`, `ORGANIZATION_ENFORCED`

## GuardrailOutputContent (structure)

The output content produced by the guardrail.

### `text` — string

The specific text for the output content produced by the guardrail.

## GuardrailOutputScope (enum)

Values: `INTERVENTIONS`, `FULL`

## GuardrailOwnership (enum)

Values: `SELF`, `CROSS_ACCOUNT`

## GuardrailPiiEntityFilter (structure)

A Personally Identifiable Information (PII) entity configured in a guardrail.

### `match` — string · **required**

The PII entity filter match.

### `type` — GuardrailPiiEntityType (enum) · **required**

The PII entity filter type.

Values: `ADDRESS`, `AGE`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `CA_HEALTH_NUMBER`, `CA_SOCIAL_INSURANCE_NUMBER`, `CREDIT_DEBIT_CARD_CVV`, `CREDIT_DEBIT_CARD_EXPIRY`, `CREDIT_DEBIT_CARD_NUMBER`, `DRIVER_ID`, `EMAIL`, `INTERNATIONAL_BANK_ACCOUNT_NUMBER`, `IP_ADDRESS`, `LICENSE_PLATE`, `MAC_ADDRESS`, `NAME`, `PASSWORD`, `PHONE`, `PIN`, `SWIFT_CODE`, `UK_NATIONAL_HEALTH_SERVICE_NUMBER`, `UK_NATIONAL_INSURANCE_NUMBER`, `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`, `URL`, `USERNAME`, `US_BANK_ACCOUNT_NUMBER`, `US_BANK_ROUTING_NUMBER`, `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER`, `US_PASSPORT_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`

### `action` — GuardrailSensitiveInformationPolicyAction (enum) · **required**

The PII entity filter action.

Values: `ANONYMIZED`, `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether personally identifiable information (PII) that breaches the guardrail configuration is detected.

## GuardrailPiiEntityType (enum)

Values: `ADDRESS`, `AGE`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `CA_HEALTH_NUMBER`, `CA_SOCIAL_INSURANCE_NUMBER`, `CREDIT_DEBIT_CARD_CVV`, `CREDIT_DEBIT_CARD_EXPIRY`, `CREDIT_DEBIT_CARD_NUMBER`, `DRIVER_ID`, `EMAIL`, `INTERNATIONAL_BANK_ACCOUNT_NUMBER`, `IP_ADDRESS`, `LICENSE_PLATE`, `MAC_ADDRESS`, `NAME`, `PASSWORD`, `PHONE`, `PIN`, `SWIFT_CODE`, `UK_NATIONAL_HEALTH_SERVICE_NUMBER`, `UK_NATIONAL_INSURANCE_NUMBER`, `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`, `URL`, `USERNAME`, `US_BANK_ACCOUNT_NUMBER`, `US_BANK_ROUTING_NUMBER`, `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER`, `US_PASSPORT_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`

## GuardrailRegexFilter (structure)

A Regex filter configured in a guardrail.

### `name` — string

The regex filter name.

### `match` — string

The regesx filter match.

### `regex` — string

The regex query.

### `action` — GuardrailSensitiveInformationPolicyAction (enum) · **required**

The region filter action.

Values: `ANONYMIZED`, `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether custom regex entities that breach the guardrail configuration are detected.

## GuardrailSensitiveInformationPolicyAction (enum)

Values: `ANONYMIZED`, `BLOCKED`, `NONE`

## GuardrailSensitiveInformationPolicyAssessment (structure)

The assessment for a Personally Identifiable Information (PII) policy.

### `piiEntities` — list<GuardrailPiiEntityFilter> · **required**

The PII entities in the assessment.

### `regexes` — list<GuardrailRegexFilter> · **required**

The regex queries in the assessment.

## GuardrailStreamConfiguration (structure)

Configuration information for a guardrail that you use with the [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) action.

### `guardrailIdentifier` — string · default `""`

The identifier for the guardrail.

### `guardrailVersion` — string · default `""`

The version of the guardrail.

### `trace` — GuardrailTrace (enum) · default `"disabled"`

The trace behavior for the guardrail.

Values: `enabled`, `disabled`, `enabled_full`

### `streamProcessingMode` — GuardrailStreamProcessingMode (enum) · default `"sync"`

The processing mode.

The processing mode. For more information, see *Configure streaming response behavior* in the *Amazon Bedrock User Guide*.

Values: `sync`, `async`

## GuardrailStreamProcessingMode (enum)

Values: `sync`, `async`

## GuardrailTextBlock (structure)

The text block to be evaluated by the guardrail.

### `text` — string · **required**

The input text details to be evaluated by the guardrail.

### `qualifiers` — list<GuardrailContentQualifier (enum)>

The qualifiers describing the text block.

## GuardrailTextCharactersCoverage (structure)

The guardrail coverage for the text characters.

### `guarded` — integer

The text characters that were guarded by the guardrail coverage.

### `total` — integer

The total text characters by the guardrail coverage.

## GuardrailTopic (structure)

Information about a topic guardrail.

### `name` — string · **required**

The name for the guardrail.

### `type` — GuardrailTopicType (enum) · **required**

The type behavior that the guardrail should perform when the model detects the topic.

Values: `DENY`

### `action` — GuardrailTopicPolicyAction (enum) · **required**

The action the guardrail should take when it intervenes on a topic.

Values: `BLOCKED`, `NONE`

### `detected` — boolean

Indicates whether topic content that breaches the guardrail configuration is detected.

## GuardrailTopicPolicyAction (enum)

Values: `BLOCKED`, `NONE`

## GuardrailTopicPolicyAssessment (structure)

A behavior assessment of a topic policy.

### `topics` — list<GuardrailTopic> · **required**

The topics in the assessment.

## GuardrailTopicType (enum)

Values: `DENY`

## GuardrailTrace (enum)

Values: `enabled`, `disabled`, `enabled_full`

## GuardrailTraceAssessment (structure)

A Top level guardrail trace object. For more information, see [ConverseTrace](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseTrace.html).

### `modelOutput` — list<string>

The output from the model.

### `inputAssessment` — map<string, GuardrailAssessment>

The input assessment.

### `outputAssessments` — map<string, list<GuardrailAssessment>>

the output assessments.

### `actionReason` — string

Provides the reason for the action taken when harmful content is detected.

## GuardrailUsage (structure)

The details on the use of the guardrail.

### `topicPolicyUnits` — integer · **required**

The topic policy units processed by the guardrail.

### `contentPolicyUnits` — integer · **required**

The content policy units processed by the guardrail.

### `wordPolicyUnits` — integer · **required**

The word policy units processed by the guardrail.

### `sensitiveInformationPolicyUnits` — integer · **required**

The sensitive information policy units processed by the guardrail.

### `sensitiveInformationPolicyFreeUnits` — integer · **required**

The sensitive information policy free units processed by the guardrail.

### `contextualGroundingPolicyUnits` — integer · **required**

The contextual grounding policy units processed by the guardrail.

### `contentPolicyImageUnits` — integer

The content policy image units processed by the guardrail.

### `automatedReasoningPolicyUnits` — integer

The number of text units processed by the automated reasoning policy.

### `automatedReasoningPolicies` — integer

The number of automated reasoning policies that were processed during the guardrail evaluation.

## GuardrailWordPolicyAction (enum)

Values: `BLOCKED`, `NONE`

## GuardrailWordPolicyAssessment (structure)

The word policy assessment.

### `customWords` — list<GuardrailCustomWord> · **required**

Custom words in the assessment.

### `managedWordLists` — list<GuardrailManagedWord> · **required**

Managed word lists in the assessment.

## ImageBlock (structure)

Image content for a message.

### `format` — ImageFormat (enum) · **required**

The format of the image.

Values: `png`, `jpeg`, `gif`, `webp`

### `source` — ImageSource · **required**

The source for the image.

### `error` — ErrorBlock

Error information if the image block could not be processed or contains invalid data.

## ImageBlockDelta (structure)

A streaming delta event that contains incremental image data during streaming responses.

### `source` — ImageSource

The incremental image source data for this delta event.

### `error` — ErrorBlock

Error information if this image delta could not be processed.

## ImageBlockStart (structure)

The initial event in a streaming image block that indicates the start of image content.

### `format` — ImageFormat (enum) · **required**

The format of the image data that will be streamed in subsequent delta events.

Values: `png`, `jpeg`, `gif`, `webp`

## ImageFormat (enum)

Values: `png`, `jpeg`, `gif`, `webp`

## ImageSource (union)

The source for an image.

### `bytes` — blob

The raw image bytes for the image. If you use an AWS SDK, you don't need to encode the image bytes in base64.

### `s3Location` — S3Location

The location of an image object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

## InferenceConfiguration (structure)

Base inference parameters to pass to a model in a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html). For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

If you need to pass additional parameters that the model supports, use the `additionalModelRequestFields` request field in the call to `Converse` or `ConverseStream`. For more information, see [Model parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `maxTokens` — integer

The maximum number of tokens to allow in the generated response. The default value is the maximum allowed value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `temperature` — float

The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.

The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `topP` — float

The percentage of most-likely candidates that the model considers for the next token. For example, if you choose a value of 0.8 for `topP`, the model selects from the top 80% of the probability distribution of tokens that could be next in the sequence.

The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### `stopSequences` — list<string>

A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.

## InvokeModelTokensRequest (structure)

The body of an `InvokeModel` API request for token counting. This structure mirrors the input format for the `InvokeModel` operation, allowing you to count tokens for raw text inference requests.

### `body` — blob · **required**

The request body to count tokens for, formatted according to the model's expected input format. To learn about the input format for different models, see [Model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

## InvokeModelWithBidirectionalStreamInput (union)

Payload content, the speech chunk, for the bidirectional input of the invocation step.

### `chunk` — BidirectionalInputPayloadPart

The audio chunk that is used as input for the invocation step.

## InvokeModelWithBidirectionalStreamOutput (union)

Output from the bidirectional stream that was used for model invocation.

### `chunk` — BidirectionalOutputPayloadPart

The speech chunk that was provided as output from the invocation step.

### `internalServerException` — InternalServerException

The request encountered an unknown internal error.

### `modelStreamErrorException` — ModelStreamErrorException

The request encountered an error with the model stream.

### `validationException` — ValidationException

The input fails to satisfy the constraints specified by an Amazon Web Services service.

### `throttlingException` — ThrottlingException

The request was denied due to request throttling.

### `modelTimeoutException` — ModelTimeoutException

The connection was closed because a request was not received within the timeout period.

### `serviceUnavailableException` — ServiceUnavailableException

The request has failed due to a temporary failure of the server.

## JsonSchemaDefinition (structure)

JSON schema structured output format options.

### `schema` — string · **required**

The JSON schema to constrain the model's output. For more information, see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference).

### `name` — string

The name of the JSON schema.

### `description` — string

A description of the JSON schema.

## Message (structure)

A message input, or returned from, a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

### `role` — ConversationRole (enum) · **required**

The role that the message plays in the message.

Values: `user`, `assistant`, `system`

### `content` — list<ContentBlock> · **required**

The message content. Note the following restrictions:

- You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.
- You can include up to five documents. Each document's size must be no more than 4.5 MB.
- If you include a `ContentBlock` with a `document` field in the array, you must also include a `ContentBlock` with a `text` field.
- You can only include images and documents if the `role` is `user`.

## MessageStartEvent (structure)

The start of a message.

### `role` — ConversationRole (enum) · **required**

The role for the message.

Values: `user`, `assistant`, `system`

## MessageStopEvent (structure)

The stop event for a message.

### `stopReason` — StopReason (enum) · **required**

The reason why the model stopped generating output.

Values: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `guardrail_intervened`, `content_filtered`, `malformed_model_output`, `malformed_tool_use`, `model_context_window_exceeded`

### `additionalModelResponseFields` — document

The additional model response fields.

## OutputConfig (structure)

Output configuration for a model response in a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

### `textFormat` — OutputFormat

Structured output parameters to control the model's text response.

### `effort` — string

The effort level for the model to use when generating a response. Higher effort levels allow the model to spend more time reasoning before responding. Supported values are `low`, `medium`, `high`, `xhigh`, and `max`.

When extended thinking is disabled, the effort level is capped at `high`. Use effort `high` or below, or enable thinking to use higher effort levels.

## OutputFormat (structure)

Structured output parameters to control the model's response.

### `type` — OutputFormatType (enum) · **required**

The type of structured output format.

Values: `json_schema`

### `structure` — OutputFormatStructure · **required**

The structure that the model's output must adhere to.

## OutputFormatStructure (union)

The structure that the model's output must adhere to.

### `jsonSchema` — JsonSchemaDefinition

A JSON schema structure that the model's output must adhere to.

## OutputFormatType (enum)

The type of structured output format. Available options are: json\_schema.

Values: `json_schema`

## PayloadPart (structure)

Payload content included in the response.

### `bytes` — blob

Base64-encoded bytes of payload data.

## PerformanceConfigLatency (enum)

Values: `standard`, `optimized`

## PerformanceConfiguration (structure)

Performance settings for a model.

### `latency` — PerformanceConfigLatency (enum) · default `"standard"`

To use a latency-optimized version of the model, set to `optimized`.

Values: `standard`, `optimized`

## PromptRouterTrace (structure)

A prompt router trace.

### `invokedModelId` — string

The ID of the invoked model.

## PromptVariableValues (union)

Contains a map of variables in a prompt from Prompt management to an object containing the values to fill in for them when running model invocation. For more information, see [How Prompt management works](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-how.html).

### `text` — string

The text value that the variable maps to.

## ReasoningContentBlock (union)

Contains content regarding the reasoning that is carried out by the model with respect to the content in the content block. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### `reasoningText` — ReasoningTextBlock

The reasoning that the model used to return the output.

### `redactedContent` — blob

The content in the reasoning that was encrypted by the model provider for safety reasons. The encryption doesn't affect the quality of responses.

## ReasoningContentBlockDelta (union)

Contains content regarding the reasoning that is carried out by the model with respect to the content in the content block. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### `text` — string

The reasoning that the model used to return the output.

### `redactedContent` — blob

The content in the reasoning that was encrypted by the model provider for safety reasons. The encryption doesn't affect the quality of responses.

### `signature` — string

A token that verifies that the reasoning text was generated by the model. If you pass a reasoning block back to the API in a multi-turn conversation, include the text and its signature unmodified.

## ReasoningTextBlock (structure)

Contains the reasoning that the model used to return the output.

### `text` — string · **required**

The reasoning that the model used to return the output.

### `signature` — string

A token that verifies that the reasoning text was generated by the model. If you pass a reasoning block back to the API in a multi-turn conversation, include the text and its signature unmodified.

## ResponseStream (union)

Definition of content in the response stream.

### `chunk` — PayloadPart

Content included in the response.

### `internalServerException` — InternalServerException

An internal server error occurred. Retry your request.

### `modelStreamErrorException` — ModelStreamErrorException

An error occurred while streaming the response. Retry your request.

### `validationException` — ValidationException

Input validation failed. Check your request parameters and retry the request.

### `throttlingException` — ThrottlingException

Your request was throttled because of service-wide limitations. Resubmit your request later or in a different region. You can also purchase [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to increase the rate or number of tokens you can process.

### `modelTimeoutException` — ModelTimeoutException

The request took too long to process. Processing time exceeded the model timeout length.

### `serviceUnavailableException` — ServiceUnavailableException

The service isn't available. Try again later.

## S3Location (structure)

A storage location in an Amazon S3 bucket.

### `uri` — string · **required**

An object URI starting with `s3://`.

### `bucketOwner` — string

If the bucket belongs to another AWS account, specify that account's ID.

## SearchResultBlock (structure)

A search result block that enables natural citations with proper source attribution for retrieved content.

This field is only supported by Anthropic Claude Opus 4.1, Opus 4, Sonnet 4.5, Sonnet 4, Sonnet 3.7, and 3.5 Haiku models.

### `source` — string · **required**

The source URL or identifier for the content.

### `title` — string · **required**

A descriptive title for the search result.

### `content` — list<SearchResultContentBlock> · **required**

An array of search result content block.

### `citations` — CitationsConfig

Configuration setting for citations

## SearchResultContentBlock (structure)

A block within a search result that contains the content.

### `text` — string · **required**

The actual text content

## SearchResultLocation (structure)

Specifies a search result location within the content array, providing positioning information for cited content using search result index and block positions.

### `searchResultIndex` — integer

The index of the search result content block where the cited content is found.

### `start` — integer

The starting position in the content array where the cited content begins.

### `end` — integer

The ending position in the content array where the cited content ends.

## ServiceTier (structure)

Specifies the processing tier configuration used for serving the request.

### `type` — ServiceTierType (enum) · **required**

Specifies the processing tier type used for serving the request.

Values: `priority`, `default`, `flex`, `reserved`

## ServiceTierType (enum)

Values: `priority`, `default`, `flex`, `reserved`

## SortAsyncInvocationBy (enum)

Values: `SubmissionTime`

## SortOrder (enum)

Values: `Ascending`, `Descending`

## SpecificToolChoice (structure)

The model must request a specific tool. For example, `{"tool" : {"name" : "Your tool name"}}`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide

This field is only supported by Anthropic Claude 3 models.

### `name` — string · **required**

The name of the tool that the model must request.

## StopReason (enum)

Values: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `guardrail_intervened`, `content_filtered`, `malformed_model_output`, `malformed_tool_use`, `model_context_window_exceeded`

## SystemContentBlock (union)

Contains configurations for instructions to provide the model for how to handle input. To learn more, see [Using the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html).

### `text` — string

A system prompt for the model.

### `guardContent` — GuardrailConverseContentBlock

A content block to assess with the guardrail. Use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

For more information, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide*.

### `cachePoint` — CachePointBlock

CachePoint to include in the system prompt.

## SystemTool (structure)

Specifies a system-defined tool for the model to use. *System-defined tools* are tools that are created and provided by the model provider.

### `name` — string · **required**

The name of the system-defined tool that you want to call.

## Tag (structure)

A tag.

### `key` — string · **required**

The tag's key.

### `value` — string · **required**

The tag's value.

## TokenUsage (structure)

The tokens used in a message API inference call.

### `inputTokens` — integer · **required**

The number of tokens sent in the request to the model.

### `outputTokens` — integer · **required**

The number of tokens that the model generated for the request.

### `totalTokens` — integer · **required**

The total of input tokens and tokens generated by the model.

### `cacheReadInputTokens` — integer

The number of input tokens read from the cache for the request.

### `cacheWriteInputTokens` — integer

The number of input tokens written to the cache for the request.

### `cacheDetails` — list<CacheDetail>

Detailed breakdown of cache writes by TTL. Empty if no cache creation occurred. Sorted by TTL duration (1h before 5m).

## Tool (union)

Information about a tool that you can use with the Converse API. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `toolSpec` — ToolSpecification

The specfication for the tool.

### `systemTool` — SystemTool

Specifies the system-defined tool that you want use.

### `cachePoint` — CachePointBlock

CachePoint to include in the tool configuration.

## ToolAdditionBlock (structure)

A content block for adding a tool to the available tool set mid-conversation. Each block references a single tool via its `tool` field. Use within a `system` role message to make a tool available without re-sending the full tool configuration.

### `tool` — ToolReference · **required**

A reference to the tool to add to the available tool set.

## ToolChoice (union)

Determines which tools the model should request in a call to `Converse` or `ConverseStream`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `auto` — AutoToolChoice

(Default). The Model automatically decides if a tool should be called or whether to generate text instead.

### `any` — AnyToolChoice

The model must request at least one tool (no text is generated).

### `tool` — SpecificToolChoice

The Model must request the specified tool. Only supported by Anthropic Claude 3 and Amazon Nova models.

## ToolConfiguration (structure)

Configuration information for the tools that you pass to a model. For more information, see [Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `tools` — list<Tool> · **required**

An array of tools that you want to pass to a model.

### `toolChoice` — ToolChoice

If supported by model, forces the model to request a tool.

## ToolInputSchema (union)

The schema for the tool. The top level schema type must be `object`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `json` — document

The JSON schema for the tool. For more information, see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference).

## ToolReference (structure)

A reference to a tool in the tool configuration. Used with `ToolAdditionBlock` and `ToolRemovalBlock` to identify which tool to add or remove mid-conversation.

### `type` — string

The type of tool reference.

### `name` — string

The name of the tool. Must match the name of a tool declared in the top-level tool configuration.

### `serverName` — string

The name of the MCP server that provides the tool. Required when referencing an MCP tool.

## ToolRemovalBlock (structure)

A content block for removing a tool from the available tool set mid-conversation. Each block references a single tool via its `tool` field. Use within a `system` role message to remove a tool without re-sending the full tool configuration.

### `tool` — ToolReference · **required**

A reference to the tool to remove from the available tool set.

## ToolResultBlock (structure)

A tool result block that contains the results for a tool request that the model previously made. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `toolUseId` — string · **required**

The ID of the tool request that this is the result for.

### `content` — list<ToolResultContentBlock> · **required**

The content for tool result content block.

### `status` — ToolResultStatus (enum)

The status for the tool result content block.

This field is only supported by Amazon Nova and Anthropic Claude 3 and 4 models.

Values: `success`, `error`

### `type` — string

The type for the tool result content block.

## ToolResultBlockDelta (union)

Contains incremental updates to tool results information during streaming responses. This allows clients to build up tool results data progressively as the response is generated.

### `text` — string

The reasoning the model used to return the output.

### `json` — document

The JSON schema for the tool result content block. see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference).

## ToolResultBlockStart (structure)

The start of a tool result block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `toolUseId` — string · **required**

The ID of the tool that was used to generate this tool result block.

### `type` — string

The type for the tool that was used to generate this tool result block.

### `status` — ToolResultStatus (enum)

The status of the tool result block.

Values: `success`, `error`

## ToolResultContentBlock (union)

The tool result content block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `json` — document

A tool result that is JSON format data.

### `text` — string

A tool result that is text.

### `image` — ImageBlock

A tool result that is an image.

This field is only supported by Amazon Nova and Anthropic Claude 3 and 4 models.

### `document` — DocumentBlock

A tool result that is a document.

### `video` — VideoBlock

A tool result that is video.

### `searchResult` — SearchResultBlock

A tool result that is a search result.

## ToolResultStatus (enum)

Values: `success`, `error`

## ToolSpecification (structure)

The specification for the tool. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `name` — string · **required**

The name for the tool.

### `description` — string

The description for the tool.

### `inputSchema` — ToolInputSchema · **required**

The input schema for the tool in JSON format.

### `strict` — boolean

Flag to enable structured output enforcement on a tool usage response.

## ToolUseBlock (structure)

A tool use content block. Contains information about a tool that the model is requesting be run., The model uses the result from the tool to generate a response. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `toolUseId` — string · **required**

The ID for the tool request.

### `name` — string · **required**

The name of the tool that the model wants to use.

### `input` — document · **required**

The input to pass to the tool.

### `type` — ToolUseType (enum)

The type for the tool request.

Values: `server_tool_use`

## ToolUseBlockDelta (structure)

The delta for a tool use block.

### `input` — string · **required**

The input for a requested tool.

## ToolUseBlockStart (structure)

The start of a tool use block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### `toolUseId` — string · **required**

The ID for the tool request.

### `name` — string · **required**

The name of the tool that the model is requesting to use.

### `type` — ToolUseType (enum)

The type for the tool request.

Values: `server_tool_use`

## ToolUseType (enum)

Values: `server_tool_use`

## Trace (enum)

Values: `ENABLED`, `DISABLED`, `ENABLED_FULL`

## VideoBlock (structure)

A video block.

### `format` — VideoFormat (enum) · **required**

The block's format.

Values: `mkv`, `mov`, `mp4`, `webm`, `flv`, `mpeg`, `mpg`, `wmv`, `three_gp`

### `source` — VideoSource · **required**

The block's source.

## VideoFormat (enum)

Values: `mkv`, `mov`, `mp4`, `webm`, `flv`, `mpeg`, `mpg`, `wmv`, `three_gp`

## VideoSource (union)

A video source. You can upload a smaller video as a base64-encoded string as long as the encoded file is less than 25MB. You can also transfer videos up to 1GB in size from an S3 bucket.

### `bytes` — blob

Video content encoded in base64.

### `s3Location` — S3Location

The location of a video object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

## WebLocation (structure)

Provides the URL and domain information for the website that was cited when performing a web search.

### `url` — string

The URL that was cited when performing a web search.

### `domain` — string

The domain that was cited when performing a web search.
