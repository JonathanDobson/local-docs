---
title: "Docker Sandboxes API v1"
source: https://docs.docker.com/reference/api/sandboxes/latest/
---

# Docker Sandboxes API v1


[API catalog](/reference/api/) · [Docker Sandboxes overview](/reference/api/sandboxes/latest/) · [Product manual](https://docs.docker.com/ai/sandboxes-api/) · [OpenAPI specification](/reference/api/sandboxes/api.yaml)

API version: v1


> This API is experimental. Features, interfaces,
> and behavior may change.



## Overview

Use this API to create sandboxes, run processes, work with files, and manage sandbox resources. Start with a kit through the SDK, or use the HTTP operations here directly.

Management requests use an Authorization bearer token. File and process requests go to the sandbox endpoint in core.endpoint.uri and require a short-lived scoped endpoint credential, not the management token. The SDK obtains that credential for you. Each operation also checks its declared permissions. Direct Unix socket access uses the operating system's socket access controls instead of HTTP authentication. Interactive WebSocket operations describe their supported credential transports separately.

The Docker Cloud API base URL is https://connect.docker.com/sandboxes. Append each /v1 path without removing the base URL's path prefix. For sandbox endpoint operations, use the sandbox endpoint as the base URL instead.

Operations list their success and error responses. A 202 response means work is still in progress; read the resource until it reaches the expected state. Errors contain a stable code, a message, and optional details. Inspect the code as well as the HTTP status.

Send the current ETag in If-Match when an operation requires it. Operations that accept Idempotency-Key use that HTTP header to identify retries: the same key and payload return the first result; a different payload fails. Keys are retained for at least 24 hours.

Lists use pageSize and pageToken. Continue with nextPageToken until it is empty. Supported filters and ordering are listed on each operation. Resource names contain immutable identifiers; displayName is a label. A 64-bit integer is returned as a JSON string; inputs accept a number or a string.
## Connecting to the Docker Sandboxes API


### bearer

A bearer credential is required for every HTTP request. Management operations use an API credential; sandbox endpoint operations use an issued credential scoped to the sandbox, audience and permitted actions.

### sandboxBearer

A short-lived bearer issued by createEndpointCredential for this sandbox, audience and explicit permissions. Management credentials are not accepted.

### sandboxWebSocketBearer

Sandbox-scoped credential encoded in the non-echoed subprotocol offer declared by x-websocket. Offer the API subprotocol alongside it; use this carrier only when endpoint discovery advertises webSocketSubprotocol. Never combine it with Authorization.


Server: `https://connect.docker.com/sandboxes`




- [Authentication and authorization](https://docs.docker.com/ai/sandboxes-api/authentication/)


- [Run your first cloud sandbox](https://docs.docker.com/ai/sandboxes-api/get-started/)



## Files

Read, write, copy, and manage files inside a sandbox.

## Processes

Run commands and interact with processes inside a sandbox.

## Credentials

Exchange credentials for the authenticated owner.

## Images

Manage images used to create sandboxes.

## MCP gateways

Configure MCP gateways and authorize upstream servers.

## Network policies

Read enforced outbound network policies and their decision logs.

## Sandboxes

Create sandboxes and manage their lifecycle, ports, and SSH access.

## Secrets

Store credentials and read their metadata without returning secret material.

## Snapshots

Capture sandbox state and restore it into a new sandbox.

## Volumes

Manage persistent storage and attach it to sandboxes.

## Operations

- [GET /v1/files](/reference/api/sandboxes/latest/operations/list/): List lists directory entries by path ascending.

- [DELETE /v1/files](/reference/api/sandboxes/latest/operations/remove/): Remove deletes a path.

- [GET /v1/files/content](/reference/api/sandboxes/latest/operations/readFile/): ReadFile returns raw file content over HTTP; Stat exposes file metadata.

- [PUT /v1/files/content](/reference/api/sandboxes/latest/operations/writeFile/): WriteFile accepts raw content with path and mode query parameters.

- [PUT /v1/files/directories](/reference/api/sandboxes/latest/operations/mkdir/): Mkdir creates a directory.

- [GET /v1/files/download](/reference/api/sandboxes/latest/operations/download/): Download streams file headers, bytes, and per-file errors.

- [POST /v1/files/move](/reference/api/sandboxes/latest/operations/move/): Move renames or moves a path.

- [GET /v1/files/stat](/reference/api/sandboxes/latest/operations/stat/): Stat reads metadata for one path.

- [POST /v1/files/upload](/reference/api/sandboxes/latest/operations/upload/): Upload streams one or more files.

- [POST /v1/identity/exchange](/reference/api/sandboxes/latest/operations/exchangeDockerCredential/): ExchangeDockerCredential consumes an identity token once for the authenticated owner.

- [GET /v1/images](/reference/api/sandboxes/latest/operations/listImages/): ListImages lists images in the caller's owner scope.

- [POST /v1/images](/reference/api/sandboxes/latest/operations/createImage/): CreateImage registers pushed OCI content or disk content derived from a snapshot or sandbox.

- [GET /v1/images/{image}](/reference/api/sandboxes/latest/operations/getImage/): GetImage reads one image by its resource name.

- [DELETE /v1/images/{image}](/reference/api/sandboxes/latest/operations/deleteImage/): DeleteImage deletes an image; deleting an already absent image succeeds.

- [GET /v1/images/{image}/pull-spec](/reference/api/sandboxes/latest/operations/getImagePullSpec/): GetImagePullSpec returns short-lived pull material through registry-transfer support.

- [GET /v1/mcp-servers/{mcpServer}/authorization](/reference/api/sandboxes/latest/operations/getMcpAuthorization/): GetMcpAuthorization reads the owner-scoped flow, including its pending URL, under mcp.write.

- [POST /v1/mcp-servers/{mcpServer}/authorization/authorize](/reference/api/sandboxes/latest/operations/authorizeMcpServer/): AuthorizeMcpServer authorizes credentials for one named upstream.

- [GET /v1/network-policies](/reference/api/sandboxes/latest/operations/getNetworkPoliciesInOwnerScope/): GetNetworkPolicies returns effective and exact views of the same installed generation.

- [GET /v1/policy-logs](/reference/api/sandboxes/latest/operations/listPolicyLogEntriesInOwnerScope/): ListPolicyLogEntries lists observed policy decisions.

- [GET /v1/processes](/reference/api/sandboxes/latest/operations/listProcesses/): ListProcesses lists processes in creation order.

- [POST /v1/processes](/reference/api/sandboxes/latest/operations/createProcess/): CreateProcess starts a durable interactive process and returns its resource name.

- [POST /v1/processes/exec](/reference/api/sandboxes/latest/operations/exec/): Exec runs one command to completion.

- [GET /v1/processes/{process}](/reference/api/sandboxes/latest/operations/getProcess/): GetProcess reads one process by its endpoint-scoped resource name.

- [GET /v1/processes/{process}/interact](/reference/api/sandboxes/latest/operations/interact/): Interact binds the complete process name from the path to the first Attach frame.

- [GET /v1/processes/{process}/output](/reference/api/sandboxes/latest/operations/readOutput/): ReadOutput returns one page of retained output after a stream_sequence, the same cursor Interact resumes from, so a REST client can read what a process printed.

- [POST /v1/processes/{process}/signal](/reference/api/sandboxes/latest/operations/signal/): Signal sends one signal to an existing process.

- [GET /v1/sandboxes](/reference/api/sandboxes/latest/operations/listSandboxes/): ListSandboxes lists sandboxes in the caller's owner scope.

- [POST /v1/sandboxes](/reference/api/sandboxes/latest/operations/createSandbox/): CreateSandbox admits a sandbox.

- [GET /v1/sandboxes/{sandbox}](/reference/api/sandboxes/latest/operations/getSandbox/): GetSandbox reads one sandbox by its resource name.

- [DELETE /v1/sandboxes/{sandbox}](/reference/api/sandboxes/latest/operations/deleteSandbox/): DeleteSandbox returns the deleting resource while work remains, or an empty message when absent.

- [PATCH /v1/sandboxes/{sandbox}](/reference/api/sandboxes/latest/operations/updateSandbox/): UpdateSandbox changes only the display label under the observed etag.

- [POST /v1/sandboxes/{sandbox}/endpoint-credentials](/reference/api/sandboxes/latest/operations/createEndpointCredential/): CreateEndpointCredential grants short-lived access to one sandbox endpoint.

- [GET /v1/sandboxes/{sandbox}/mcp-gateway](/reference/api/sandboxes/latest/operations/getMcpGateway/): GetMcpGateway reads gateway state for the sandbox.

- [POST /v1/sandboxes/{sandbox}/mcp-gateway/servers](/reference/api/sandboxes/latest/operations/addMcpGatewayServer/): AddMcpGatewayServer adds one server to an existing ready gateway.

- [GET /v1/sandboxes/{sandbox}/network-policies](/reference/api/sandboxes/latest/operations/getNetworkPolicies/): GetNetworkPolicies returns effective and exact views of the same installed generation.

- [GET /v1/sandboxes/{sandbox}/policy-logs](/reference/api/sandboxes/latest/operations/listPolicyLogEntries/): ListPolicyLogEntries lists observed policy decisions.

- [GET /v1/sandboxes/{sandbox}/ports](/reference/api/sandboxes/latest/operations/listPorts/): ListPorts lists currently published ports for one sandbox.

- [POST /v1/sandboxes/{sandbox}/ports](/reference/api/sandboxes/latest/operations/createPort/): CreatePort makes one sandbox port reachable outside the sandbox.

- [GET /v1/sandboxes/{sandbox}/ports/{port}](/reference/api/sandboxes/latest/operations/getPort/): GetPort reads one published port by its resource name.

- [DELETE /v1/sandboxes/{sandbox}/ports/{port}](/reference/api/sandboxes/latest/operations/deletePort/): DeletePort withdraws one published port.

- [POST /v1/sandboxes/{sandbox}/renew-timeout](/reference/api/sandboxes/latest/operations/renewSandboxTimeout/): RenewSandboxTimeout sets a TTL when timeout renewal is supported.

- [POST /v1/sandboxes/{sandbox}/snapshots](/reference/api/sandboxes/latest/operations/createSnapshot/): CreateSnapshot checkpoints a running sandbox; a stopped source is rejected.

- [POST /v1/sandboxes/{sandbox}/ssh-certificates](/reference/api/sandboxes/latest/operations/issueSSHCert/): IssueSSHCert signs a caller-held public key for sandbox SSH access.

- [POST /v1/sandboxes/{sandbox}/start](/reference/api/sandboxes/latest/operations/startSandbox/): StartSandbox starts a stopped sandbox; a backend that preserved memory resumes it.

- [POST /v1/sandboxes/{sandbox}/stop](/reference/api/sandboxes/latest/operations/stopSandbox/): StopSandbox stops a running sandbox; a backend advertising memory preservation hibernates it.

- [GET /v1/secrets](/reference/api/sandboxes/latest/operations/listSecrets/): ListSecrets lists secret metadata in the caller's owner scope.

- [POST /v1/secrets](/reference/api/sandboxes/latest/operations/createSecret/): CreateSecret stores new secret material.

- [GET /v1/secrets/{secret}](/reference/api/sandboxes/latest/operations/getSecret/): GetSecret reads one secret's metadata; material is never returned.

- [PUT /v1/secrets/{secret}](/reference/api/sandboxes/latest/operations/updateSecret/): UpdateSecret replaces secret metadata and material.

- [DELETE /v1/secrets/{secret}](/reference/api/sandboxes/latest/operations/deleteSecret/): DeleteSecret deletes a secret; deleting an already absent secret succeeds.

- [GET /v1/snapshots](/reference/api/sandboxes/latest/operations/listSnapshots/): ListSnapshots lists snapshots in the caller's owner scope.

- [GET /v1/snapshots/{snapshot}](/reference/api/sandboxes/latest/operations/getSnapshot/): GetSnapshot reads one snapshot by its resource name.

- [DELETE /v1/snapshots/{snapshot}](/reference/api/sandboxes/latest/operations/deleteSnapshot/): DeleteSnapshot deletes a snapshot; deleting an already absent snapshot succeeds.

- [POST /v1/snapshots/{snapshot}/restore](/reference/api/sandboxes/latest/operations/restoreSnapshot/): RestoreSnapshot forks a new sandbox from a snapshot.

- [GET /v1/volumes](/reference/api/sandboxes/latest/operations/listVolumes/): ListVolumes lists volumes in the caller's owner scope.

- [POST /v1/volumes](/reference/api/sandboxes/latest/operations/createVolume/): CreateVolume creates a persistent volume.

- [GET /v1/volumes/{volume}](/reference/api/sandboxes/latest/operations/getVolume/): GetVolume reads one volume by its resource name.

- [DELETE /v1/volumes/{volume}](/reference/api/sandboxes/latest/operations/deleteVolume/): DeleteVolume deletes a volume; deleting an already absent volume succeeds.

## Schemas

- [AddMcpGatewayServerResponse](/reference/api/sandboxes/latest/schemas/AddMcpGatewayServerResponse/)

- [AppliedKit](/reference/api/sandboxes/latest/schemas/AppliedKit/)

- [AttachmentMode](/reference/api/sandboxes/latest/schemas/AttachmentMode/)

- [AttributedRule](/reference/api/sandboxes/latest/schemas/AttributedRule/)

- [BadRequest](/reference/api/sandboxes/latest/schemas/BadRequest/)

- [BadRequestErrorDetail](/reference/api/sandboxes/latest/schemas/BadRequestErrorDetail/)

- [BadRequestFieldViolation](/reference/api/sandboxes/latest/schemas/BadRequestFieldViolation/)

- [CaptureMode](/reference/api/sandboxes/latest/schemas/CaptureMode/)

- [CreateImageRequest](/reference/api/sandboxes/latest/schemas/CreateImageRequest/)

- [CreatePortRequestPortInput](/reference/api/sandboxes/latest/schemas/CreatePortRequestPortInput/)

- [CreateProcessRequest](/reference/api/sandboxes/latest/schemas/CreateProcessRequest/)

- [CreateSandboxRequest](/reference/api/sandboxes/latest/schemas/CreateSandboxRequest/)

- [CreateSecretRequest](/reference/api/sandboxes/latest/schemas/CreateSecretRequest/)

- [CreateVolumeRequest](/reference/api/sandboxes/latest/schemas/CreateVolumeRequest/)

- [CredentialFenceReceipt](/reference/api/sandboxes/latest/schemas/CredentialFenceReceipt/)

- [CustomInjection](/reference/api/sandboxes/latest/schemas/CustomInjection/)

- [CustomSecretMaterial](/reference/api/sandboxes/latest/schemas/CustomSecretMaterial/)

- [DebugInfo](/reference/api/sandboxes/latest/schemas/DebugInfo/)

- [DebugInfoErrorDetail](/reference/api/sandboxes/latest/schemas/DebugInfoErrorDetail/)

- [DeleteSecretResponse](/reference/api/sandboxes/latest/schemas/DeleteSecretResponse/)

- [Duration](/reference/api/sandboxes/latest/schemas/Duration/)

- [EffectiveCoreLifecycle](/reference/api/sandboxes/latest/schemas/EffectiveCoreLifecycle/)

- [EffectiveFeatures](/reference/api/sandboxes/latest/schemas/EffectiveFeatures/)

- [EffectiveManagedVolumes](/reference/api/sandboxes/latest/schemas/EffectiveManagedVolumes/)

- [EffectiveNetworkPolicy](/reference/api/sandboxes/latest/schemas/EffectiveNetworkPolicy/)

- [EffectiveTimeouts](/reference/api/sandboxes/latest/schemas/EffectiveTimeouts/)

- [EffectiveVolumeAttachment](/reference/api/sandboxes/latest/schemas/EffectiveVolumeAttachment/)

- [EndpointAuthentication](/reference/api/sandboxes/latest/schemas/EndpointAuthentication/)

- [EndpointAuthenticationScheme](/reference/api/sandboxes/latest/schemas/EndpointAuthenticationScheme/)

- [EndpointCredential](/reference/api/sandboxes/latest/schemas/EndpointCredential/)

- [EndpointCredentialTransport](/reference/api/sandboxes/latest/schemas/EndpointCredentialTransport/)

- [Error](/reference/api/sandboxes/latest/schemas/Error/)

- [ErrorCode](/reference/api/sandboxes/latest/schemas/ErrorCode/)

- [ErrorDetail](/reference/api/sandboxes/latest/schemas/ErrorDetail/)

- [ErrorInfo](/reference/api/sandboxes/latest/schemas/ErrorInfo/)

- [ErrorInfoErrorDetail](/reference/api/sandboxes/latest/schemas/ErrorInfoErrorDetail/)

- [EtagMismatch](/reference/api/sandboxes/latest/schemas/EtagMismatch/)

- [EtagMismatchErrorDetail](/reference/api/sandboxes/latest/schemas/EtagMismatchErrorDetail/)

- [ExactDestination](/reference/api/sandboxes/latest/schemas/ExactDestination/)

- [ExactDestinationKind](/reference/api/sandboxes/latest/schemas/ExactDestinationKind/)

- [ExactNetworkPolicy](/reference/api/sandboxes/latest/schemas/ExactNetworkPolicy/)

- [ExactPolicyConstant](/reference/api/sandboxes/latest/schemas/ExactPolicyConstant/)

- [ExactPolicyNode](/reference/api/sandboxes/latest/schemas/ExactPolicyNode/)

- [ExactPolicyOperands](/reference/api/sandboxes/latest/schemas/ExactPolicyOperands/)

- [ExactPolicyOrigin](/reference/api/sandboxes/latest/schemas/ExactPolicyOrigin/)

- [ExactPolicySource](/reference/api/sandboxes/latest/schemas/ExactPolicySource/)

- [ExchangeCompositionCredentialResponse](/reference/api/sandboxes/latest/schemas/ExchangeCompositionCredentialResponse/)

- [ExecRequest](/reference/api/sandboxes/latest/schemas/ExecRequest/)

- [ExecResponse](/reference/api/sandboxes/latest/schemas/ExecResponse/)

- [FeatureOptions](/reference/api/sandboxes/latest/schemas/FeatureOptions/)

- [FileError](/reference/api/sandboxes/latest/schemas/FileError/)

- [FileHeader](/reference/api/sandboxes/latest/schemas/FileHeader/)

- [FileInfo](/reference/api/sandboxes/latest/schemas/FileInfo/)

- [FileType](/reference/api/sandboxes/latest/schemas/FileType/)

- [FilesDownloadRequest](/reference/api/sandboxes/latest/schemas/FilesDownloadRequest/)

- [FilesDownloadResponse](/reference/api/sandboxes/latest/schemas/FilesDownloadResponse/)

- [FilesListResponse](/reference/api/sandboxes/latest/schemas/FilesListResponse/)

- [FilesMkdirRequest](/reference/api/sandboxes/latest/schemas/FilesMkdirRequest/)

- [FilesMkdirResponse](/reference/api/sandboxes/latest/schemas/FilesMkdirResponse/)

- [FilesMoveRequest](/reference/api/sandboxes/latest/schemas/FilesMoveRequest/)

- [FilesMoveResponse](/reference/api/sandboxes/latest/schemas/FilesMoveResponse/)

- [FilesReadFileRequest](/reference/api/sandboxes/latest/schemas/FilesReadFileRequest/)

- [FilesReadFileResponse](/reference/api/sandboxes/latest/schemas/FilesReadFileResponse/)

- [FilesRemoveResponse](/reference/api/sandboxes/latest/schemas/FilesRemoveResponse/)

- [FilesStatResponse](/reference/api/sandboxes/latest/schemas/FilesStatResponse/)

- [FilesUploadRequest](/reference/api/sandboxes/latest/schemas/FilesUploadRequest/)

- [FilesUploadResponse](/reference/api/sandboxes/latest/schemas/FilesUploadResponse/)

- [FilesWriteFileRequest](/reference/api/sandboxes/latest/schemas/FilesWriteFileRequest/)

- [FilesWriteFileResponse](/reference/api/sandboxes/latest/schemas/FilesWriteFileResponse/)

- [GetNetworkPoliciesResponse](/reference/api/sandboxes/latest/schemas/GetNetworkPoliciesResponse/)

- [Help](/reference/api/sandboxes/latest/schemas/Help/)

- [HelpErrorDetail](/reference/api/sandboxes/latest/schemas/HelpErrorDetail/)

- [HelpLink](/reference/api/sandboxes/latest/schemas/HelpLink/)

- [IdentityExchangeServiceExchangeDockerCredentialRequest](/reference/api/sandboxes/latest/schemas/IdentityExchangeServiceExchangeDockerCredentialRequest/)

- [Image](/reference/api/sandboxes/latest/schemas/Image/)

- [ImageBlobRef](/reference/api/sandboxes/latest/schemas/ImageBlobRef/)

- [ImageFromImage](/reference/api/sandboxes/latest/schemas/ImageFromImage/)

- [ImagePullSpec](/reference/api/sandboxes/latest/schemas/ImagePullSpec/)

- [ImagePushTarget](/reference/api/sandboxes/latest/schemas/ImagePushTarget/)

- [ImageSource](/reference/api/sandboxes/latest/schemas/ImageSource/)

- [ImageStatus](/reference/api/sandboxes/latest/schemas/ImageStatus/)

- [ImageSummary](/reference/api/sandboxes/latest/schemas/ImageSummary/)

- [InteractRequest](/reference/api/sandboxes/latest/schemas/InteractRequest/)

- [IssueSSHCertResponse](/reference/api/sandboxes/latest/schemas/IssueSSHCertResponse/)

- [KitArtifactInput](/reference/api/sandboxes/latest/schemas/KitArtifactInput/)

- [KitFieldDisposition](/reference/api/sandboxes/latest/schemas/KitFieldDisposition/)

- [KitFieldOutcome](/reference/api/sandboxes/latest/schemas/KitFieldOutcome/)

- [KitFieldOutcomeReport](/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReport/)

- [KitFieldOutcomeReportErrorDetail](/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReportErrorDetail/)

- [KitFieldReason](/reference/api/sandboxes/latest/schemas/KitFieldReason/)

- [KitInput](/reference/api/sandboxes/latest/schemas/KitInput/)

- [KitRef](/reference/api/sandboxes/latest/schemas/KitRef/)

- [KitStartup](/reference/api/sandboxes/latest/schemas/KitStartup/)

- [KitStartupCommand](/reference/api/sandboxes/latest/schemas/KitStartupCommand/)

- [ListImagesResponse](/reference/api/sandboxes/latest/schemas/ListImagesResponse/)

- [ListPolicyLogEntriesResponse](/reference/api/sandboxes/latest/schemas/ListPolicyLogEntriesResponse/)

- [ListPortsResponse](/reference/api/sandboxes/latest/schemas/ListPortsResponse/)

- [ListProcessesResponse](/reference/api/sandboxes/latest/schemas/ListProcessesResponse/)

- [ListSandboxesResponse](/reference/api/sandboxes/latest/schemas/ListSandboxesResponse/)

- [ListSecretsResponse](/reference/api/sandboxes/latest/schemas/ListSecretsResponse/)

- [ListSnapshotsResponse](/reference/api/sandboxes/latest/schemas/ListSnapshotsResponse/)

- [ListVolumesResponse](/reference/api/sandboxes/latest/schemas/ListVolumesResponse/)

- [LocalizedMessage](/reference/api/sandboxes/latest/schemas/LocalizedMessage/)

- [LocalizedMessageErrorDetail](/reference/api/sandboxes/latest/schemas/LocalizedMessageErrorDetail/)

- [ManagedVolumeOptions](/reference/api/sandboxes/latest/schemas/ManagedVolumeOptions/)

- [McpAuthorization](/reference/api/sandboxes/latest/schemas/McpAuthorization/)

- [McpAuthorizationStatus](/reference/api/sandboxes/latest/schemas/McpAuthorizationStatus/)

- [McpConfigurationMode](/reference/api/sandboxes/latest/schemas/McpConfigurationMode/)

- [McpConfigurationOutcome](/reference/api/sandboxes/latest/schemas/McpConfigurationOutcome/)

- [McpConfigurationReport](/reference/api/sandboxes/latest/schemas/McpConfigurationReport/)

- [McpConfigurationReportErrorDetail](/reference/api/sandboxes/latest/schemas/McpConfigurationReportErrorDetail/)

- [McpConfiguredServer](/reference/api/sandboxes/latest/schemas/McpConfiguredServer/)

- [McpCreateSpec](/reference/api/sandboxes/latest/schemas/McpCreateSpec/)

- [McpGateway](/reference/api/sandboxes/latest/schemas/McpGateway/)

- [McpGatewayState](/reference/api/sandboxes/latest/schemas/McpGatewayState/)

- [McpServer](/reference/api/sandboxes/latest/schemas/McpServer/)

- [McpServerType](/reference/api/sandboxes/latest/schemas/McpServerType/)

- [NetworkPolicy](/reference/api/sandboxes/latest/schemas/NetworkPolicy/)

- [NetworkPolicyMode](/reference/api/sandboxes/latest/schemas/NetworkPolicyMode/)

- [OAuthConfig](/reference/api/sandboxes/latest/schemas/OAuthConfig/)

- [OAuthRefreshMaterial](/reference/api/sandboxes/latest/schemas/OAuthRefreshMaterial/)

- [OutputRetention](/reference/api/sandboxes/latest/schemas/OutputRetention/)

- [Permission](/reference/api/sandboxes/latest/schemas/Permission/)

- [Platform](/reference/api/sandboxes/latest/schemas/Platform/)

- [PolicyDecision](/reference/api/sandboxes/latest/schemas/PolicyDecision/)

- [PolicyDomain](/reference/api/sandboxes/latest/schemas/PolicyDomain/)

- [PolicyLayer](/reference/api/sandboxes/latest/schemas/PolicyLayer/)

- [PolicyLogEntry](/reference/api/sandboxes/latest/schemas/PolicyLogEntry/)

- [Port](/reference/api/sandboxes/latest/schemas/Port/)

- [PreconditionFailure](/reference/api/sandboxes/latest/schemas/PreconditionFailure/)

- [PreconditionFailureErrorDetail](/reference/api/sandboxes/latest/schemas/PreconditionFailureErrorDetail/)

- [PreconditionFailureViolation](/reference/api/sandboxes/latest/schemas/PreconditionFailureViolation/)

- [Process](/reference/api/sandboxes/latest/schemas/Process/)

- [ProcessAttach](/reference/api/sandboxes/latest/schemas/ProcessAttach/)

- [ProcessChunk](/reference/api/sandboxes/latest/schemas/ProcessChunk/)

- [ProcessExited](/reference/api/sandboxes/latest/schemas/ProcessExited/)

- [ProcessHeartbeat](/reference/api/sandboxes/latest/schemas/ProcessHeartbeat/)

- [ProcessOutput](/reference/api/sandboxes/latest/schemas/ProcessOutput/)

- [ProcessSignal](/reference/api/sandboxes/latest/schemas/ProcessSignal/)

- [ProcessState](/reference/api/sandboxes/latest/schemas/ProcessState/)

- [Protocol](/reference/api/sandboxes/latest/schemas/Protocol/)

- [PtyConfig](/reference/api/sandboxes/latest/schemas/PtyConfig/)

- [PublishedPort](/reference/api/sandboxes/latest/schemas/PublishedPort/)

- [QuotaFailure](/reference/api/sandboxes/latest/schemas/QuotaFailure/)

- [QuotaFailureErrorDetail](/reference/api/sandboxes/latest/schemas/QuotaFailureErrorDetail/)

- [QuotaFailureViolation](/reference/api/sandboxes/latest/schemas/QuotaFailureViolation/)

- [RawImageStartup](/reference/api/sandboxes/latest/schemas/RawImageStartup/)

- [ReadOutputResponse](/reference/api/sandboxes/latest/schemas/ReadOutputResponse/)

- [ReceiptKind](/reference/api/sandboxes/latest/schemas/ReceiptKind/)

- [RequestInfo](/reference/api/sandboxes/latest/schemas/RequestInfo/)

- [RequestInfoErrorDetail](/reference/api/sandboxes/latest/schemas/RequestInfoErrorDetail/)

- [ResourceInfo](/reference/api/sandboxes/latest/schemas/ResourceInfo/)

- [ResourceInfoErrorDetail](/reference/api/sandboxes/latest/schemas/ResourceInfoErrorDetail/)

- [Resources](/reference/api/sandboxes/latest/schemas/Resources/)

- [RetryInfo](/reference/api/sandboxes/latest/schemas/RetryInfo/)

- [RetryInfoErrorDetail](/reference/api/sandboxes/latest/schemas/RetryInfoErrorDetail/)

- [Sandbox](/reference/api/sandboxes/latest/schemas/Sandbox/)

- [SandboxCore](/reference/api/sandboxes/latest/schemas/SandboxCore/)

- [SandboxEndpoint](/reference/api/sandboxes/latest/schemas/SandboxEndpoint/)

- [SandboxEndpointProtocol](/reference/api/sandboxes/latest/schemas/SandboxEndpointProtocol/)

- [SandboxStatus](/reference/api/sandboxes/latest/schemas/SandboxStatus/)

- [Secret](/reference/api/sandboxes/latest/schemas/Secret/)

- [SecretType](/reference/api/sandboxes/latest/schemas/SecretType/)

- [SignalResponse](/reference/api/sandboxes/latest/schemas/SignalResponse/)

- [Snapshot](/reference/api/sandboxes/latest/schemas/Snapshot/)

- [SnapshotStatus](/reference/api/sandboxes/latest/schemas/SnapshotStatus/)

- [SnapshotSummary](/reference/api/sandboxes/latest/schemas/SnapshotSummary/)

- [StartupArgv](/reference/api/sandboxes/latest/schemas/StartupArgv/)

- [StartupExecution](/reference/api/sandboxes/latest/schemas/StartupExecution/)

- [StopMemoryOutcome](/reference/api/sandboxes/latest/schemas/StopMemoryOutcome/)

- [StoredSecretOptions](/reference/api/sandboxes/latest/schemas/StoredSecretOptions/)

- [StreamType](/reference/api/sandboxes/latest/schemas/StreamType/)

- [TerminalSize](/reference/api/sandboxes/latest/schemas/TerminalSize/)

- [TimeoutAction](/reference/api/sandboxes/latest/schemas/TimeoutAction/)

- [TimeoutOptions](/reference/api/sandboxes/latest/schemas/TimeoutOptions/)

- [Timestamp](/reference/api/sandboxes/latest/schemas/Timestamp/)

- [TokenSecretMaterial](/reference/api/sandboxes/latest/schemas/TokenSecretMaterial/)

- [UnknownErrorDetail](/reference/api/sandboxes/latest/schemas/UnknownErrorDetail/)

- [UpdateSecretBody](/reference/api/sandboxes/latest/schemas/UpdateSecretBody/)

- [ValidationFieldPath](/reference/api/sandboxes/latest/schemas/ValidationFieldPath/)

- [ValidationFieldPathElement](/reference/api/sandboxes/latest/schemas/ValidationFieldPathElement/)

- [ValidationFieldType](/reference/api/sandboxes/latest/schemas/ValidationFieldType/)

- [ValidationViolation](/reference/api/sandboxes/latest/schemas/ValidationViolation/)

- [ValidationViolations](/reference/api/sandboxes/latest/schemas/ValidationViolations/)

- [ValidationViolationsErrorDetail](/reference/api/sandboxes/latest/schemas/ValidationViolationsErrorDetail/)

- [Volume](/reference/api/sandboxes/latest/schemas/Volume/)

- [VolumeAttachment](/reference/api/sandboxes/latest/schemas/VolumeAttachment/)
