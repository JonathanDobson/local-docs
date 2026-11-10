# Docker Sandboxes API v1 — schemas

## AddMcpGatewayServerResponse

AddMcpGatewayServerResponse returns the added or already-present server.

| Field | Type | Required | Description |
|---|---|---|---|
| `server` | `McpServer` |  | server is the gateway server. |

## AppliedKit

AppliedKit records kit content that was applied to a sandbox.

| Field | Type | Required | Description |
|---|---|---|---|
| `ref` | string |  | ref is the kit reference supplied or resolved by the backend. |
| `kind` | string enum: sandbox, mixin | yes | kind is normalized to "sandbox" or "mixin". |
| `appliedAt` | `Timestamp` |  | applied_at is when the kit became active. |
| `digest` | string |  | digest identifies the exact applied content. |

## AttachmentMode

AttachmentMode fixes attachment ownership independently of backend placement.

Values:
unspecified: unspecified selects exclusive read-write attachment.
exclusive: exclusive permits one sandbox to attach the volume read-write.

Type: string enum: unspecified, exclusive

## AttributedRule

AttributedRule reports a rule and the layer that supplied it.

| Field | Type | Required | Description |
|---|---|---|---|
| `network` | string |  | network is the network name or CIDR. |
| `layer` | `PolicyLayer` |  | layer identifies where the rule came from. |

## BadRequest

Describes violations in a client request. This error type focuses on the
syntactic aspects of the request.

| Field | Type | Required | Description |
|---|---|---|---|
| `fieldViolations` | array of `BadRequestFieldViolation` |  | Describes all violations in a client request. |

## BadRequestErrorDetail

Describes violations in a client request. This error type focuses on the
syntactic aspects of the request.

| Field | Type | Required | Description |
|---|---|---|---|
| `fieldViolations` | array of `BadRequestFieldViolation` |  | Describes all violations in a client request. |
| `@type` | string | yes |  |

## BadRequestFieldViolation

A message type used to describe a single bad request field.

| Field | Type | Required | Description |
|---|---|---|---|
| `field` | string |  | A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field. Consider the following: message CreateContactRequest { message EmailAddress { enum Type { TYPE_UNSPECIFIED = 0; HOME = 1; WORK = 2; } optional string email = 1; repeated EmailType type = 2; } string full_name = 1; repeated EmailAddress email_addresses = 2; } In this example, in proto `field` could take one of the following values: * `full_name` for a violation in the `full_name` value * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message. In JSON, the same values are represented as: * `fullName` for a violation in the `fullName` value * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message. |
| `description` | string |  | A description of why the request element is bad. |
| `reason` | string |  | The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. |
| `localizedMessage` | `LocalizedMessage` |  | Provides a localized error message for field-level errors that is safe to return to the API consumer. |

## CaptureMode

CaptureMode selects whether captured images include memory.

Values:
unspecified: unspecified means disk-only capture.
all: all captures memory and disk and requires memory-capture support.
disk: disk captures disk only.

Type: string enum: unspecified, all, disk

## CreateImageRequest

CreateImageRequest creates a managed image.

Type: allOf(object, oneOf(object))

## CreatePortRequestPortInput

| Field | Type | Required | Description |
|---|---|---|---|
| `number` | integer (int32) | yes | (IMMUTABLE) number is immutable and unique within the sandbox; duplicates refuse ALREADY_EXISTS. |
| `protocol` | string enum: unspecified, tcp |  | (IMMUTABLE) protocol defaults to TCP when unspecified. |

## CreateProcessRequest

CreateProcessRequest starts an interactive process.

| Field | Type | Required | Description |
|---|---|---|---|
| `cmd` | array of string | yes | cmd is the argv vector. |
| `env` | object |  | env adds environment variables. |
| `workingDir` | string |  | working_dir is the process working directory. |
| `user` | string |  | user is the user to run as. |
| `pty` | `PtyConfig` |  | pty requests a pseudo-terminal; absence uses separate stdin/stdout/stderr pipes. |
| `session` | string |  | session is an optional opaque session tag stored verbatim; empty means untagged. |
| `label` | ['string', 'null'] |  | (OPTIONAL) label is unique within the sandbox; omission retains the server-generated default. |

## CreateSandboxRequest

CreateSandboxRequest validates typed composition intent before replay and
persists accepted guarantees, distinct enough from legacy create that old
servers cannot silently drop it.
display_name and display_name_prefix are mutually exclusive At most one of image, imageRef is set.

Type: allOf(object, object)

## CreateSecretRequest

CreateSecretRequest stores new secret material.
service_type must be empty for custom material (server-assigned)

Type: allOf(object, oneOf(object, object, object))

## CreateVolumeRequest

CreateVolumeRequest creates one volume.

| Field | Type | Required | Description |
|---|---|---|---|
| `displayName` | string | yes | display_name is a scoped label; the backend assigns the immutable resource ID. |

## CredentialFenceReceipt

CredentialFenceReceipt acknowledges one completed generation without granting current use.

| Field | Type | Required | Description |
|---|---|---|---|
| `target` | string | yes | target is the complete Sandbox or Secret resource name bound to this receipt. |
| `generation` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] | yes | generation increases for each accepted material/rule replacement on that target. |

## CustomInjection

CustomInjection is caller-authored, non-secret metadata for a custom
secret: which exact hosts receive the value, in which header and format,
and how the placeholder is shaped and delivered. Unlike secret material,
reads return it.

| Field | Type | Required | Description |
|---|---|---|---|
| `hosts` | array of string | yes | hosts are exact lowercase DNS names. Wildcards, IP literals, ports, schemes, paths, and hosts a managed integration already serves are rejected. |
| `header` | string | yes | header is the HTTP header the value is written to. Routing, framing, and cookie headers are rejected. |
| `format` | string |  | format renders the value with exactly one %s; %% escapes a literal percent, and any other % sequence is rejected. Empty means "%s". |
| `envVar` | string |  | env_var optionally names a sandbox environment variable that carries the secret's placeholder (never the value) as a delivery convenience. |
| `placeholderTemplate` | string |  | placeholder_template optionally shapes the placeholder for clients that validate credential shape before sending (e.g. "sk-corp-{rand}"). Each {rand} token is expanded server-side; {rand} is the only token. Empty uses the backend default ("sbx-cs-{rand}"). |

## CustomSecretMaterial

CustomSecretMaterial is an opaque secret value plus its injection routing.

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | string | yes | value is the secret value. |
| `injection` | `CustomInjection` | yes | injection is the caller-authored routing. |

## DebugInfo

Describes additional debugging info.

| Field | Type | Required | Description |
|---|---|---|---|
| `stackEntries` | array of string |  | The stack trace entries indicating where the error occurred. |
| `detail` | string |  | Additional debugging information provided by the server. |

## DebugInfoErrorDetail

Describes additional debugging info.

| Field | Type | Required | Description |
|---|---|---|---|
| `stackEntries` | array of string |  | The stack trace entries indicating where the error occurred. |
| `detail` | string |  | Additional debugging information provided by the server. |
| `@type` | string | yes |  |

## DeleteSecretResponse

DeleteSecretResponse acknowledges deletion and optional consumer fencing.

| Field | Type | Required | Description |
|---|---|---|---|
| `credentialFence` | `CredentialFenceReceipt` |  | credential_fence remains the original historical receipt after deletion or name reuse. |

## Duration

Seconds with a trailing s, for example 30s or 1.5s.

Type: string

## EffectiveCoreLifecycle

EffectiveCoreLifecycle is persisted at admission and cannot silently degrade.

| Field | Type | Required | Description |
|---|---|---|---|
| `stopMemoryOutcome` | `StopMemoryOutcome` | yes | stop_memory_outcome is the selected stop/start guarantee for this sandbox. |
| `canCaptureMemory` | boolean |  | can_capture_memory is this sandbox's ALL snapshot support, independently set. |
| `autoResume` | ['boolean', 'null'] |  | auto_resume is the configured authenticated auto-resume setting; absent means unknown. Snapshot readback preserves the capture-time value, not current support or a resume guarantee. |

## EffectiveFeatures

EffectiveFeatures is emitted only through the composition representation.

| Field | Type | Required | Description |
|---|---|---|---|
| `lifecycle` | `EffectiveCoreLifecycle` | yes | lifecycle is required even when no optional feature is selected. |
| `outputRetention` | `OutputRetention` | yes | output_retention is the persisted per-process reconnect guarantee. |
| `managedVolumes` | `EffectiveManagedVolumes` |  | managed_volumes records stable volume identities and concrete attachment modes. |
| `timeouts` | `EffectiveTimeouts` |  | timeouts records frozen defaults and the currently armed deadline, if any. |

## EffectiveManagedVolumes

EffectiveManagedVolumes records storage that is not deleted with the sandbox.

| Field | Type | Required | Description |
|---|---|---|---|
| `attachments` | array of `EffectiveVolumeAttachment` | yes | attachments retains admission order and stable volume identities. |

## EffectiveNetworkPolicy

EffectiveNetworkPolicy is the policy after layering and fail-closed defaults.

| Field | Type | Required | Description |
|---|---|---|---|
| `mode` | `NetworkPolicyMode` | yes | mode is the effective mode and is always concrete in conforming responses. |
| `allowNetworks` | array of `AttributedRule` |  | allow_networks are effective allowed rules with attribution. |
| `denyNetworks` | array of `AttributedRule` |  | deny_networks are effective denied rules with attribution. |

## EffectiveTimeouts

EffectiveTimeouts retains the selected behavior and current action deadline.
DELETE and STOP retain a resume timeout; RESTART (and its deprecated alias KEEP) does not use one

| Field | Type | Required | Description |
|---|---|---|---|
| `onTimeout` | `TimeoutAction` | yes | on_timeout remains the accepted disposition through renewal and restart. |
| `autoResume` | boolean |  | auto_resume is explicit; endpoint authorization still precedes any wake-up. |
| `initialTimeout` | `Duration` | yes | Records the accepted initial TTL, not the recurring interval for RESTART or KEEP. |
| `expiresAt` | `Timestamp` |  | expires_at is present only while a deadline is armed, not before first readiness or while stopped. |
| `resumeTimeout` | `Duration` |  | Freezes the action's default for later starts; RESTART and KEEP manage their own interval. |

## EffectiveVolumeAttachment

EffectiveVolumeAttachment retains the identity, not a reusable name lookup.

| Field | Type | Required | Description |
|---|---|---|---|
| `volume` | string |  | volume is the resource name recorded for this reference. |
| `volumeUid` | ['string', 'null'] |  | volume_uid retains the observed backing incarnation when the backend provides one. |
| `target` | string | yes | target is the accepted normalized absolute guest path. |
| `mode` | `AttachmentMode` | yes | mode is explicit and survives sandbox stop/start and backend restart. |

## EndpointAuthentication

EndpointAuthentication describes credential issuance without publishing a token.
local sockets cannot advertise bearer credential transports
scoped bearer discovery states the five-minute credential lifetime; local sockets carry no token lifetime

| Field | Type | Required | Description |
|---|---|---|---|
| `scheme` | `EndpointAuthenticationScheme` | yes |  |
| `defaultTtl` | `Duration` |  | default_ttl and max_ttl describe CreateEndpointCredential's provider policy. |
| `maxTtl` | `Duration` |  |  |
| `credentialTransports` | array of `EndpointCredentialTransport` |  | Omission retains Authorization-header clients; browsers require an explicit subprotocol offer. |

## EndpointAuthenticationScheme

Values:
unspecified
scopedBearer
localSocket

Type: string enum: unspecified, scopedBearer, localSocket

## EndpointCredential

EndpointCredential is returned once with Cache-Control: no-store; never log its token.

| Field | Type | Required | Description |
|---|---|---|---|
| `token` | string | yes |  |
| `expireTime` | `Timestamp` | yes |  |
| `permissions` | array of `Permission` | yes | Allowed values: sandboxesExec, sandboxesFilesRead, sandboxesFilesWrite. |
| `sandbox` | string | yes |  |
| `audience` | string | yes |  |

## EndpointCredentialTransport

Values:
unspecified
authorizationHeader
webSocketSubprotocol

Type: string enum: unspecified, authorizationHeader, webSocketSubprotocol

## Error

An HTTP refusal, resource failure, or terminal stream error. Clients preserve unknown codes and structured details.

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | anyOf(`ErrorCode`, string) | yes |  |
| `message` | string |  |  |
| `details` | array of `ErrorDetail` |  |  |

## ErrorCode

Known public failure categories. Error.code also accepts future strings.

Type: string enum: canceled, unknown, invalidArgument, deadlineExceeded, notFound, alreadyExists, permissionDenied, resourceExhausted, failedPrecondition, aborted, outOfRange, unimplemented

## ErrorDetail

Type: oneOf(`BadRequestErrorDetail`, `DebugInfoErrorDetail`, `ErrorInfoErrorDetail`, `HelpErrorDetail`, `LocalizedMessageErrorDetail`, `PreconditionFailureErrorDetail`, `QuotaFailureErrorDetail`, `RequestInfoErrorDetail`, `ResourceInfoErrorDetail`, `RetryInfoErrorDetail`, `ValidationViolationsErrorDetail`, `EtagMismatchErrorDetail`, `KitFieldOutcomeReportErrorDetail`, `McpConfigurationReportErrorDetail`, `UnknownErrorDetail`)

## ErrorInfo

Describes the cause of the error with structured details.

Example of an error when contacting the "pubsub.googleapis.com" API when it
is not enabled:

{ "reason": "API_DISABLED"
"domain": "googleapis.com"
"metadata": {
"resource": "projects/123",
"service": "pubsub.googleapis.com"
}
}

This response indicates that the pubsub.googleapis.com API is not enabled.

Example of an error that is returned when attempting to create a Spanner
instance in a region that is out of stock:

{ "reason": "STOCKOUT"
"domain": "spanner.googleapis.com",
"metadata": {
"availableRegions": "us-central1,us-east2"
}
}

| Field | Type | Required | Description |
|---|---|---|---|
| `reason` | string |  | The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. |
| `domain` | string |  | The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com". |
| `metadata` | object |  | Additional structured details about this error. Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request. |

## ErrorInfoErrorDetail

Describes the cause of the error with structured details.

Example of an error when contacting the "pubsub.googleapis.com" API when it
is not enabled:

{ "reason": "API_DISABLED"
"domain": "googleapis.com"
"metadata": {
"resource": "projects/123",
"service": "pubsub.googleapis.com"
}
}

This response indicates that the pubsub.googleapis.com API is not enabled.

Example of an error that is returned when attempting to create a Spanner
instance in a region that is out of stock:

{ "reason": "STOCKOUT"
"domain": "spanner.googleapis.com",
"metadata": {
"availableRegions": "us-central1,us-east2"
}
}

| Field | Type | Required | Description |
|---|---|---|---|
| `reason` | string |  | The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. |
| `domain` | string |  | The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com". |
| `metadata` | object |  | Additional structured details about this error. Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request. |
| `@type` | string | yes |  |

## EtagMismatch

EtagMismatch is the status detail a stale precondition carries, so a client learns the
current version for an explicit conflict-resolution decision.

| Field | Type | Required | Description |
|---|---|---|---|
| `currentEtag` | string | yes | current_etag is informational; clients must not silently retry with it. |

## EtagMismatchErrorDetail

EtagMismatch is the status detail a stale precondition carries, so a client learns the
current version for an explicit conflict-resolution decision.

| Field | Type | Required | Description |
|---|---|---|---|
| `currentEtag` | string | yes | current_etag is informational; clients must not silently retry with it. |
| `@type` | string | yes |  |

## ExactDestination

ExactDestination uses canonical selector values, never legacy glob syntax.
dnsLabelPrefix requires a canonical DNS label prefix and suffix

| Field | Type | Required | Description |
|---|---|---|---|
| `kind` | `ExactDestinationKind` | yes | kind selects a matching rule; dnsLabelPrefix requires destination.v2. |
| `value` | string | yes | For dnsLabelPrefix, crl.digicert.com matches a first label starting with crl and remaining labels exactly digicert.com; every value label is canonical ASCII DNS. |
| `port` | ['integer', 'null'] |  | An absent port matches all numeric ports; zero is invalid when present. |

## ExactDestinationKind

ExactDestinationKind keeps DNS and IP-literal decisions distinct.

Values:
unspecified
dns
dnsLabel
dnsSubtree
ip
cidr
dnsLabelPrefix

Type: string enum: unspecified, dns, dnsLabel, dnsSubtree, ip, cidr, dnsLabelPrefix

## ExactNetworkPolicy

ExactNetworkPolicy is a complete consumer-installed generation; its last node is the root.
dnsLabelPrefix requires destination.v2

| Field | Type | Required | Description |
|---|---|---|---|
| `revision` | string | yes | revision binds authority, configuration and resolved conditions to the installed generation. |
| `selectorVersion` | string enum: destination.v1, destination.v2 | yes | selector_version fixes matching semantics across implementations. |
| `nodes` | array of `ExactPolicyNode` | yes | nodes are complete and topologically ordered; the final node is the root. |

## ExactPolicyConstant

ExactPolicyConstant makes both Boolean identities explicit.

Values:
unspecified
true
false

Type: string enum: unspecified, true, false

## ExactPolicyNode

ExactPolicyNode is topologically ordered; references must precede this node.

Type: allOf(object, oneOf(object, object, object, object, object))

## ExactPolicyOperands

ExactPolicyOperands contains earlier node indexes; empty Boolean groups are invalid.

| Field | Type | Required | Description |
|---|---|---|---|
| `nodes` | array of integer | yes | nodes must all precede the enclosing operator. |

## ExactPolicyOrigin

ExactPolicyOrigin separates governance from attached and runtime-owned permissions.

Values:
unspecified
organization
owner
attached
kit
gateway
default

Type: string enum: unspecified, organization, owner, attached, kit, gateway, default

## ExactPolicySource

ExactPolicySource identifies the nonsecret authority of a leaf expression.

| Field | Type | Required | Description |
|---|---|---|---|
| `origin` | `ExactPolicyOrigin` | yes | origin distinguishes the authority that supplied this leaf. |
| `id` | string | yes | id identifies that source without exposing credentials or policy content. |

## ExchangeCompositionCredentialResponse

Type: object

## ExecRequest

ExecRequest runs a command to completion.

| Field | Type | Required | Description |
|---|---|---|---|
| `cmd` | array of string | yes | cmd is the argv vector. |
| `env` | object |  | env adds environment variables. |
| `workingDir` | string |  | working_dir is the process working directory. |
| `user` | string |  | user is the user to run as. |

## ExecResponse

ExecResponse returns process output after the command exits.

| Field | Type | Required | Description |
|---|---|---|---|
| `exitCode` | integer (int32) |  | exit_code is the process exit code. |
| `stdout` | string (byte) |  | stdout is captured stdout, up to the capture limit when incomplete. |
| `stderr` | string (byte) |  | stderr is captured stderr, up to the capture limit when incomplete. |
| `incomplete` | boolean |  | incomplete is true when the combined capture limit forced stdout and/or stderr to discard some of the command's real output; false whenever every byte the command produced was retained, even if that total lands exactly at the limit. exit_code is still the real, final exit code: the command ran to completion, only its captured output was capped. A retry would rerun the command, so this stays a normal successful response rather than an error a client might retry. |

## FeatureOptions

FeatureOptions carries typed admission intent; unknown fields are refused.

| Field | Type | Required | Description |
|---|---|---|---|
| `managedVolumes` | `ManagedVolumeOptions` |  | managed_volumes selects persistent resources and guest targets. |
| `timeouts` | `TimeoutOptions` |  | timeouts enables an explicit deadline; omission enables none. |
| `storedSecrets` | `StoredSecretOptions` |  | stored_secrets selects authorized stored references, never raw material. |

## FileError

FileError reports a path-level file error.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string |  | path is the path that failed. |
| `failure` | `Error` | yes | failure retains the shared typed code and details for this path. |

## FileHeader

FileHeader starts a file in an upload or download stream.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string | yes | path is the sandbox path. |
| `mode` | integer |  | mode carries Unix permission bits. Upload applies mode & 0777, or 0644 when that value is zero, without subtracting umask; Download reports stored bits. |

## FileInfo

FileInfo is file metadata.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string |  | path is the sandbox path. |
| `size` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | size is the file size in bytes. |
| `mode` | integer |  | mode is the stored Unix permission bits (0777), without type or special bits. |
| `isDir` | boolean |  | is_dir reports whether the path is a directory and stays populated on every backend and every caller. type is the richer authority, and type == directory iff is_dir. |
| `type` | `FileType` |  | type classifies the object, and Stat and List populate it for every caller. Stat and List resolve an in-jail symlink and report the resolved target's type; a link that cannot be resolved in-jail (dangling, looping, or escaping) reports symlink for itself rather than disclosing an out-of-jail target. |
| `linkTarget` | string |  | link_target is the literal readlink() text when type is symlink, since that is the only case where nothing else lets the caller learn what the link names; empty otherwise. |

## FileType

FileType classifies the object at a path.

Values:
unspecified: unspecified means the backend has not classified the object. Stat and List always classify it.
regular: regular is a regular file.
directory: directory is a directory.
symlink: symlink is a symbolic link that could not be resolved to a target inside the jail.
other: other is a socket, FIFO, device, or other non-regular, non-directory, non-symlink object.

Type: string enum: unspecified, regular, directory, symlink, other

## FilesDownloadRequest

DownloadRequest asks for one or more paths.

| Field | Type | Required | Description |
|---|---|---|---|
| `paths` | array of string | yes | paths naming stable regular files or absent entries at canonical absolute paths yield contiguous results in request order, including duplicates. |

## FilesDownloadResponse

DownloadResponse is one frame in a download stream. At most one of data, error, header is set.

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | string (byte) |  | data carries bytes for the current file. |
| `error` | `FileError` |  | error reports a path-level failure without aborting the whole stream. |
| `header` | `FileHeader` |  | header starts a downloaded file. |

## FilesListResponse

ListResponse returns directory entries and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `entries` | array of `FileInfo` |  | entries is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## FilesMkdirRequest

MkdirRequest creates a directory.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string | yes | path is the directory path. |
| `mode` | integer |  | mode supplies the new leaf's Unix permission bits: mode & 0777, or 0755 when that value is zero, without subtracting umask. |
| `parents` | boolean |  | parents creates missing parents when true. |

## FilesMkdirResponse

MkdirResponse has no fields.

Type: object

## FilesMoveRequest

MoveRequest moves or renames a path.

| Field | Type | Required | Description |
|---|---|---|---|
| `from` | string | yes | from is the source path. |
| `to` | string | yes | to is the exact destination path. |

## FilesMoveResponse

MoveResponse has no fields.

Type: object

## FilesReadFileRequest

ReadFileRequest names one regular file.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string | yes | path is the sandbox path of a regular file. |

## FilesReadFileResponse

ReadFileResponse carries the whole file; HTTP selects data as its raw response body.

| Field | Type | Required | Description |
|---|---|---|---|
| `info` | `FileInfo` | yes | info remains available to the internal adapter; HTTP clients use Stat for metadata. |
| `data` | string (byte) |  | data is the complete content; a file above the message cap is refused. |

## FilesRemoveResponse

RemoveResponse reports partial recursive progress to every caller: check failed_path,
not the operation status, when Remove stops partway. Effects are never rolled back.

| Field | Type | Required | Description |
|---|---|---|---|
| `completedPaths` | array of string |  | completed_paths lists removed paths in traversal order, bounded to the first 1000; completed_count carries the true total when it exceeds that bound. |
| `completedCount` | integer |  | completed_count is the total number of paths removed, which may exceed len(completed_paths). |
| `failedPath` | string |  | failed_path is the path where a recursive removal stopped; empty on full success. Every path in completed_paths was removed before this one. |

## FilesStatResponse

StatResponse returns file metadata.

| Field | Type | Required | Description |
|---|---|---|---|
| `info` | `FileInfo` |  | info is metadata for the path. |

## FilesUploadRequest

UploadRequest is one frame in an upload stream.

Type: oneOf(object, object)

## FilesUploadResponse

UploadResponse reports completed file writes.

| Field | Type | Required | Description |
|---|---|---|---|
| `filesWritten` | integer |  | files_written is the number of files successfully written. |

## FilesWriteFileRequest

WriteFileRequest replaces one file.

| Field | Type | Required | Description |
|---|---|---|---|
| `header` | `FileHeader` | yes | header names the path and mode, as an Upload header does. |
| `data` | string (byte) |  | data is the complete new content; empty writes an empty file. |

## FilesWriteFileResponse

WriteFileResponse reports the written file.

| Field | Type | Required | Description |
|---|---|---|---|
| `info` | `FileInfo` | yes | info is the file's metadata after the write. |

## GetNetworkPoliciesResponse

GetNetworkPoliciesResponse binds both views to exact.revision; a partial read fails.

| Field | Type | Required | Description |
|---|---|---|---|
| `effective` | `EffectiveNetworkPolicy` | yes |  |
| `exact` | `ExactNetworkPolicy` | yes |  |

## Help

Provides links to documentation or for performing an out of band action.

For example, if a quota check failed with an error indicating the calling
project hasn't enabled the accessed service, this can contain a URL pointing
directly to the right place in the developer console to flip the bit.

| Field | Type | Required | Description |
|---|---|---|---|
| `links` | array of `HelpLink` |  | URL(s) pointing to additional information on handling the current error. |

## HelpErrorDetail

Provides links to documentation or for performing an out of band action.

For example, if a quota check failed with an error indicating the calling
project hasn't enabled the accessed service, this can contain a URL pointing
directly to the right place in the developer console to flip the bit.

| Field | Type | Required | Description |
|---|---|---|---|
| `links` | array of `HelpLink` |  | URL(s) pointing to additional information on handling the current error. |
| `@type` | string | yes |  |

## HelpLink

Describes a URL link.

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | Describes what the link offers. |
| `url` | string |  | The URL of the link. |

## IdentityExchangeServiceExchangeDockerCredentialRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `idToken` | string | yes | id_token is single-use identity material, never an owner selector. |

## Image

Image is the detailed managed image view.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | (IDENTIFIER) name ends in the immutable backing ID and never changes with display_name. |
| `description` | string |  | description is caller-supplied text. |
| `status` | `ImageStatus` | yes | status is the image readiness state. |
| `imageRef` | string |  | image_ref is the registry or backend image reference when available. |
| `imageDigest` | string |  | image_digest is the content digest when known. |
| `resources` | `Resources` |  | resources describes the image's preferred runtime resources. |
| `startCmd` | array of string |  | start_cmd is the command used by raw image sandboxes. |
| `readyCmd` | array of string |  | ready_cmd is the readiness command used by raw image sandboxes. |
| `platform` | `Platform` |  | platform is the image platform. |
| `totalSizeBytes` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | total_size_bytes is the approximate stored image size. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `updatedAt` | `Timestamp` | yes | updated_at is the last update timestamp. |
| `failure` | `Error` |  | failure is set when status is FAILED. |
| `source` | `ImageSource` |  | source records how the image was created. |
| `captureMode` | `CaptureMode` |  | capture_mode records whether captured content includes memory. |
| `etag` | string | yes | etag identifies the observed version of this resource. It is opaque and strong, changes on every visible change, and is what a mutation sends as its precondition. |
| `pushTarget` | `ImagePushTarget` |  | push_target appears only in from_image create responses awaiting upload, never reads. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## ImageBlobRef

ImageBlobRef describes one pullable blob.

| Field | Type | Required | Description |
|---|---|---|---|
| `digest` | string |  | digest is the content digest. |
| `mediaType` | string |  | media_type is the OCI media type. |
| `size` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | size is the blob size in bytes. |
| `url` | string |  | url is a short-lived pull URL. |

## ImageFromImage

ImageFromImage registers a target for pushed OCI content.

| Field | Type | Required | Description |
|---|---|---|---|
| `resources` | `Resources` |  | resources describes preferred runtime resources for the resulting image. |
| `platform` | `Platform` |  | platform is the platform for the pushed content. |
| `captureMode` | string enum: unspecified, disk |  | capture_mode must be unspecified or disk; pushed OCI content cannot include memory. |
| `platformHint` | `Platform` |  | platform_hint picks among a multi-platform push when platform is absent. A hint the backend cannot honor is ignored, never an error. |
| `kitStartup` | `KitStartup` |  | Startup commands copied from the source sandbox. Services with startup replay run these commands when a sandbox created from the image boots. Services without startup replay accept valid commands without running them. |

## ImagePullSpec

ImagePullSpec describes short-lived pull material for placement.

| Field | Type | Required | Description |
|---|---|---|---|
| `manifestDigest` | string |  | manifest_digest is the manifest digest. |
| `manifestMediaType` | string |  | manifest_media_type is the manifest media type. |
| `config` | `ImageBlobRef` |  | config is the image config blob. |
| `layers` | array of `ImageBlobRef` |  | layers are the image layer blobs. |
| `expiresAt` | `Timestamp` |  | expires_at is when the pull material expires. |

## ImagePushTarget

ImagePushTarget carries short-lived upload credentials.

| Field | Type | Required | Description |
|---|---|---|---|
| `imageRef` | string |  | image_ref is the registry reference to push. |
| `accessToken` | string |  | access_token is the short-lived push credential. |
| `accessTokenExpiresAt` | `Timestamp` |  | access_token_expires_at is the token expiry. |

## ImageSource

ImageSource records how the image was created.

Values:
unspecified: unspecified means the source is unknown or not reported.
image: image means the image came from pushed or imported image bytes.
sandbox: sandbox means the image came from a sandbox capture.

Type: string enum: unspecified, image, sandbox

## ImageStatus

ImageStatus is the image readiness state.

Values:
unspecified: unspecified is never a concrete known state.
pending: pending means an asynchronous build has not started or reported progress.
waitingForPush: waitingForPush means the backend is waiting for OCI content upload.
preparing: preparing means the backend is preparing pushed or captured content.
completed: completed means the image is ready to use.
failed: failed means image preparation reached a terminal failure.
deleted: deleted means the backend exposes a retained delete tombstone.

Type: string enum: unspecified, pending, waitingForPush, preparing, completed, failed, deleted

## ImageSummary

ImageSummary is the list view of an image.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | name ends in the immutable backing ID and never changes with display_name. |
| `status` | `ImageStatus` | yes | status is the image readiness state. |
| `source` | `ImageSource` |  | source records how the image was created. |
| `totalSizeBytes` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | total_size_bytes is the approximate stored image size. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `updatedAt` | `Timestamp` | yes | updated_at is the last update timestamp. |
| `imageRef` | string |  | image_ref is the registry or backend image reference when available. |
| `imageDigest` | string |  | image_digest is the content digest when known. |
| `captureMode` | `CaptureMode` |  | capture_mode records whether captured content includes memory. |
| `platform` | `Platform` |  | platform is the image platform. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## InteractRequest

InteractRequest is one frame on the bidirectional interaction stream.

Type: oneOf(object, object, object, object)

## IssueSSHCertResponse

IssueSSHCertResponse returns signed SSH client material, never a private key.

| Field | Type | Required | Description |
|---|---|---|---|
| `certificate` | string |  | certificate is the signed SSH certificate. |
| `sshConfig` | string |  | ssh_config optionally renders the connection fields as OpenSSH client configuration; the structured fields are canonical. |
| `knownHosts` | string |  | known_hosts is host key material that authenticates the SSH endpoint. |
| `expiresAt` | `Timestamp` |  | expires_at is the instant after which the certificate is invalid. |
| `host` | string |  | host is the SSH endpoint host to connect to. |
| `port` | integer |  | port is the SSH endpoint port to connect to. |
| `username` | string |  | username is the SSH username to present; it carries no authorization. |

## KitArtifactInput

KitArtifactInput carries a v2 artifact inline or by staged digest.

Type: allOf(object, oneOf(object))

## KitFieldDisposition

KitFieldDisposition describes a declaration that was not applied.

Values:
unspecified: unspecified is invalid in a report.
skipped: skipped identifies a contract-permitted optional skip.
refused: refused prevents guest or kit effects.

Type: string enum: unspecified, skipped, refused

## KitFieldOutcome

KitFieldOutcome identifies one non-applied declaration without exposing its value.

| Field | Type | Required | Description |
|---|---|---|---|
| `kitIndex` | integer |  | kit_index is the zero-based position in the originating request's kits. |
| `ref` | string | yes | ref preserves the exact requested kit reference. |
| `digest` | string |  | digest is the resolved content identity when resolution succeeded. |
| `fieldPath` | string | yes | field_path is an RFC 6901 pointer into the pinned JSON artifact. |
| `disposition` | `KitFieldDisposition` | yes | disposition never claims that an accepted declaration has executed. |
| `reason` | `KitFieldReason` | yes | reason is a bounded category, not caller-controlled diagnostic content. |
| `reasonText` | string |  | reason_text contains nonsecret explanatory text, never values or command content. |

## KitFieldOutcomeReport

KitFieldOutcomeReport records settled diagnostics on a sandbox or an admission refusal.

| Field | Type | Required | Description |
|---|---|---|---|
| `complete` | boolean |  | complete means every refused or skipped declaration is accounted for; absence proves nothing. |
| `outcomes` | array of `KitFieldOutcome` |  | outcomes follow request index then UTF-8 field-path order and are never truncated. |

## KitFieldOutcomeReportErrorDetail

KitFieldOutcomeReport records settled diagnostics on a sandbox or an admission refusal.

| Field | Type | Required | Description |
|---|---|---|---|
| `complete` | boolean |  | complete means every refused or skipped declaration is accounted for; absence proves nothing. |
| `outcomes` | array of `KitFieldOutcome` |  | outcomes follow request index then UTF-8 field-path order and are never truncated. |
| `@type` | string | yes |  |

## KitFieldReason

KitFieldReason provides stable, nonsecret diagnostic categories.

Values:
unspecified: unspecified is invalid in a report.
unsupported: unsupported means the backend cannot honor the declaration.
unknownField: unknownField means the pinned schema does not recognize the declaration.
credentialUnavailable: credentialUnavailable means the declared credential cannot be injected.

Type: string enum: unspecified, unsupported, unknownField, credentialUnavailable

## KitInput

KitInput is one kit in either shape.

Type: oneOf(object)

## KitRef

KitRef names a kit to apply.

| Field | Type | Required | Description |
|---|---|---|---|
| `ref` | string | yes | ref names the kit source. |
| `kind` | string enum: , sandbox, mixin |  | kind is "sandbox", "mixin", or empty to defer to the kit's own manifest. |

## KitStartup

Startup commands retained when creating an image. Services with startup replay run them at each boot; services without it accept valid commands without running them.

| Field | Type | Required | Description |
|---|---|---|---|
| `kits` | array of string | yes | kits names the kit identities the commands derive from, in composition order. Required. |
| `commands` | array of `KitStartupCommand` | yes | commands run in order at sandbox boot, on a backend that replays them. |

## KitStartupCommand

KitStartupCommand is one startup command in a KitStartup set, run in order
by a backend that replays it at sandbox boot.

| Field | Type | Required | Description |
|---|---|---|---|
| `argv` | array of string | yes | argv is the command and its arguments, exec-style. An argument other than the executable itself may be empty (an intentional empty string, as in `printf %s ""`); only the vector itself is required non-empty. |
| `user` | string |  | user runs the command as this user; empty means the backend default. |
| `background` | boolean |  | background launches the command detached instead of waiting for it. |

## ListImagesResponse

ListImagesResponse returns image results and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `images` | array of `ImageSummary` |  | images is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListPolicyLogEntriesResponse

ListPolicyLogEntriesResponse returns policy log entries and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `entries` | array of `PolicyLogEntry` |  | entries is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListPortsResponse

ListPortsResponse returns currently published ports.

| Field | Type | Required | Description |
|---|---|---|---|
| `published` | array of `Port` |  | published is ordered by number ascending. |

## ListProcessesResponse

ListProcessesResponse returns processes and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `processes` | array of `Process` |  | processes is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListSandboxesResponse

ListSandboxesResponse returns sandbox results and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `sandboxes` | array of `Sandbox` |  | sandboxes is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListSecretsResponse

ListSecretsResponse returns secrets and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `secrets` | array of `Secret` |  | secrets is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListSnapshotsResponse

ListSnapshotsResponse returns snapshot results and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `snapshots` | array of `SnapshotSummary` |  | snapshots is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## ListVolumesResponse

ListVolumesResponse returns volumes and a next-page token.

| Field | Type | Required | Description |
|---|---|---|---|
| `volumes` | array of `Volume` |  | volumes is the current page. |
| `nextPageToken` | string |  | next_page_token is empty when there are no more pages. |

## LocalizedMessage

Provides a localized error message that is safe to return to the user
which can be attached to an operation error.

| Field | Type | Required | Description |
|---|---|---|---|
| `locale` | string |  | The locale used following the specification defined at https://www.rfc-editor.org/rfc/bcp/bcp47.txt. Examples are: "en-US", "fr-CH", "es-MX" |
| `message` | string |  | The localized error message in the above locale. |

## LocalizedMessageErrorDetail

Provides a localized error message that is safe to return to the user
which can be attached to an operation error.

| Field | Type | Required | Description |
|---|---|---|---|
| `locale` | string |  | The locale used following the specification defined at https://www.rfc-editor.org/rfc/bcp/bcp47.txt. Examples are: "en-US", "fr-CH", "es-MX" |
| `message` | string |  | The localized error message in the above locale. |
| `@type` | string | yes |  |

## ManagedVolumeOptions

ManagedVolumeOptions selects existing volumes; it does not create storage.

| Field | Type | Required | Description |
|---|---|---|---|
| `attachments` | array of `VolumeAttachment` | yes | attachments cannot repeat a volume identity or overlap another mount target. |

## McpAuthorization

McpAuthorization is the current authorization incarnation for one named upstream.

| Field | Type | Required | Description |
|---|---|---|---|
| `server` | string |  | (OPTIONAL) server is the complete resource name, in the form mcp-servers/{server}. |
| `uid` | ['string', 'null'] |  | (IMMUTABLE) uid is the existing immutable backing identity, omitted when none is available. |
| `status` | `McpAuthorizationStatus` |  |  |
| `authorizationUrl` | string |  | authorization_url is present only while interaction is pending. |
| `createdAt` | `Timestamp` |  |  |
| `updatedAt` | `Timestamp` |  |  |
| `expiresAt` | `Timestamp` |  | expires_at bounds the pending flow; expiry records FAILED on this incarnation. |
| `failure` | `Error` |  |  |
| `etag` | string |  | etag identifies this incarnation and changes with every visible authorization update. |
| `name` | string |  | (IDENTIFIER) name is the complete singleton resource name. |

## McpAuthorizationStatus

McpAuthorizationStatus reports the current upstream authorization outcome.

Values:
unspecified
pending
authorized
failed

Type: string enum: unspecified, pending, authorized, failed

## McpConfigurationMode

McpConfigurationMode identifies desired hosting ownership and discovery behavior.

Values:
unspecified: unspecified is not a concrete report mode.
dynamic: dynamic uses a backend-minted gateway with discovery.
static: static uses a backend-minted gateway without discovery.
attached: attached retains a read-only external binding.

Type: string enum: unspecified, dynamic, static, attached

## McpConfigurationOutcome

McpConfigurationOutcome describes one requested server in the reported generation.

Values:
unspecified: unspecified is not a concrete outcome.
pending: pending has not settled and cannot establish completeness.
applied: applied is confirmed membership, not upstream authorization.
skipped: skipped requires an explicitly applicable compatibility rule.
failed: failed retains intent that could not be provisioned.

Type: string enum: unspecified, pending, applied, skipped, failed

## McpConfigurationReport

McpConfigurationReport is also returned in Error.details on accepted provisioning failure.

| Field | Type | Required | Description |
|---|---|---|---|
| `generation` | string | yes | generation is an opaque durable fence, never ordered or synthesized by callers. |
| `mode` | `McpConfigurationMode` | yes | mode separates minted discovery behavior from read-only attachment. |
| `complete` | boolean |  | complete means every active requested server is applied or explicitly permitted to skip. |
| `servers` | array of `McpConfiguredServer` |  | servers is the complete active requested set; together with dormant_servers it matches McpGateway.servers. |
| `dormantServers` | array of `McpServer` |  | dormant_servers retains earlier minted intent while attached; it is empty in minted modes. |

## McpConfigurationReportErrorDetail

McpConfigurationReport is also returned in Error.details on accepted provisioning failure.

| Field | Type | Required | Description |
|---|---|---|---|
| `generation` | string | yes | generation is an opaque durable fence, never ordered or synthesized by callers. |
| `mode` | `McpConfigurationMode` | yes | mode separates minted discovery behavior from read-only attachment. |
| `complete` | boolean |  | complete means every active requested server is applied or explicitly permitted to skip. |
| `servers` | array of `McpConfiguredServer` |  | servers is the complete active requested set; together with dormant_servers it matches McpGateway.servers. |
| `dormantServers` | array of `McpServer` |  | dormant_servers retains earlier minted intent while attached; it is empty in minted modes. |
| `@type` | string | yes |  |

## McpConfiguredServer

McpConfiguredServer preserves one canonical requested identity and its provisioning outcome.

| Field | Type | Required | Description |
|---|---|---|---|
| `server` | `McpServer` | yes | server is the resolved requested server; its type cannot silently change within retained intent. |
| `outcome` | `McpConfigurationOutcome` | yes | outcome is concrete even when the gateway remains ready after a failed add. |
| `reason` | string |  | reason is nonsecret context and never carries credentials or credential-bearing URLs. |

## McpCreateSpec

McpCreateSpec configures the sandbox's MCP gateway before the workload starts.
servers must be empty when gateway_url is set

| Field | Type | Required | Description |
|---|---|---|---|
| `servers` | array of string |  | servers are initial server names for a backend-minted gateway. |
| `static` | boolean |  | static pins the requested server set and closes gateway-side discovery. |
| `gatewayUrl` | ['string', 'null', ' ', '(', 'u', 'r', 'i', ')'] |  | gateway_url attaches read-only to a pre-existing shareable gateway when supported. |

## McpGateway

McpGateway is gateway state for one sandbox.

| Field | Type | Required | Description |
|---|---|---|---|
| `url` | string |  | url is the gateway endpoint. |
| `state` | `McpGatewayState` |  | state is the gateway readiness state. |
| `servers` | array of `McpServer` |  | servers is the accumulated requested set, not live gateway truth. |
| `reused` | boolean |  | reused is true when the response reused an existing gateway. |
| `uid` | ['string', 'null'] |  | (IMMUTABLE) uid is the existing immutable backing identity, omitted when none is available. |
| `name` | string |  | (IDENTIFIER) name is the complete singleton resource name. |

## McpGatewayState

McpGatewayState reports gateway readiness.

Values:
unspecified: unspecified is never a concrete known state.
provisioning: provisioning means the gateway is starting.
ready: ready means the gateway can accept server operations.
failed: failed means gateway setup failed.

Type: string enum: unspecified, provisioning, ready, failed

## McpServer

McpServer projects one external server key configured on a gateway.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | name is the external configured server key, not an API resource name. |
| `type` | `McpServerType` |  | type is the configured server type. |

## McpServerType

McpServerType identifies a gateway server integration style.

Values:
unspecified: unspecified is not a concrete server type.
remote: remote is an HTTP remote MCP server.
container: container is a container-backed MCP server.
stdio: stdio is a stdio-backed MCP server.

Type: string enum: unspecified, remote, container, stdio

## NetworkPolicy

NetworkPolicy is an inline policy request materialized in the governance plane.

| Field | Type | Required | Description |
|---|---|---|---|
| `mode` | string enum: denyAll | yes | mode is required and cannot be UNSPECIFIED. |
| `allowNetworks` | array of string |  | allow_networks are exact network names or CIDRs allowed by this document. |
| `denyNetworks` | array of string |  | deny_networks are exact network names or CIDRs denied by this document. |

## NetworkPolicyMode

NetworkPolicyMode is the top-level egress disposition.

Values:
unspecified: unspecified is invalid in policy documents and in conforming responses.
allowAll: allowAll allows egress unless denied by a narrower rule.
denyAll: denyAll denies egress unless allowed by a narrower rule.

Type: string enum: unspecified, allowAll, denyAll

## OAuthConfig

OAuthConfig is non-secret OAuth metadata returned on reads.

| Field | Type | Required | Description |
|---|---|---|---|
| `tokenEndpoint` | string |  | token_endpoint is the OAuth token endpoint. |
| `clientId` | string |  | client_id is the OAuth client id. |

## OAuthRefreshMaterial

OAuthRefreshMaterial is OAuth secret material. Unlike OAuthRefreshMaterialV2 it pairs
no bootstrap token with an expiry and stores client_id as the caller supplied it.

| Field | Type | Required | Description |
|---|---|---|---|
| `refreshToken` | string | yes | refresh_token is the OAuth refresh token. |
| `initialAccessToken` | string |  | initial_access_token is an optional bootstrap access token. |
| `expiresAt` | `Timestamp` |  | expires_at is the access token expiry when supplied. |
| `scopes` | array of string |  | scopes are requested OAuth scopes. |
| `providerAccountId` | string |  | provider_account_id identifies the provider account. |
| `idToken` | string |  | id_token is an optional OpenID Connect id token. |
| `clientId` | string |  | client_id is the OAuth client id. |

## OutputRetention

OutputRetention records minimum reconnect coverage independently of location.
output retention requires a duration or byte floor

| Field | Type | Required | Description |
|---|---|---|---|
| `minDuration` | `Duration` |  | min_duration retains each process's output for at least this age when set. |
| `minBytes` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | min_bytes retains at least this many recent bytes per process when nonzero. a byte retention floor must be zero or at least 64 KiB |

## Permission

The actions a credential is allowed to perform. Each operation declares its required permissions; service support does not grant permission.

Type: string enum: unspecified, sandboxesRead, sandboxesCreate, sandboxesExec, sandboxesFilesRead, sandboxesFilesWrite, imagesPull, secretsWrite, sandboxesDelete, sandboxesLifecycle, sandboxesKits, sandboxesPorts

## Platform

Platform is the OCI platform tuple.

| Field | Type | Required | Description |
|---|---|---|---|
| `os` | string |  | os is the operating system, for example "linux". |
| `architecture` | string |  | architecture is the CPU architecture, for example "amd64" or "arm64". |

## PolicyDecision

PolicyDecision is the outcome of an evaluated access attempt.

Values:
unspecified: unspecified means the decision is unknown or not reported.
allowed: allowed means the attempt was allowed.
blocked: blocked means the attempt was blocked.

Type: string enum: unspecified, allowed, blocked

## PolicyDomain

PolicyDomain identifies a policy subsystem.

Values:
unspecified: unspecified is not a concrete policy domain.
network: network is network egress policy.

Type: string enum: unspecified, network

## PolicyLayer

PolicyLayer identifies where an effective rule came from. ORG and OWNER are
the two governance scopes; exactly one governs a caller, so a conforming effective view never mixes them.

Values:
unspecified: unspecified means the layer is unknown or not reported.
org: org is org-level governance policy.
owner: owner is owner-level governance policy.
kit: kit is the sandbox-scoped policy a kit contributes.
attached: attached is a governance policy bound to the sandbox: an inline document or a referenced policy id, materialized and bound by the governance plane at create.
gateway: gateway is an enforced runtime-owned gateway policy contribution, not a backend service-route exemption.
default: default is an explicit installed default-policy contribution, not a substitute for unknown provenance or an owner-level policy.

Type: string enum: unspecified, org, owner, kit, attached, gateway, default

## PolicyLogEntry

PolicyLogEntry is an aggregated observed policy decision.

| Field | Type | Required | Description |
|---|---|---|---|
| `resource` | string |  | resource is the requested destination or resource. |
| `decision` | `PolicyDecision` |  | decision is the observed allow or block outcome. |
| `proxyType` | string |  | proxy_type is the proxy or enforcement path that observed the decision. |
| `rule` | string |  | rule is the matching rule when available. |
| `reason` | string |  | reason is backend-readable context. |
| `count` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | count is the number of coalesced observations. |
| `firstSeen` | `Timestamp` |  | first_seen is the first observation timestamp. |
| `lastSeen` | `Timestamp` |  | last_seen is the most recent observation timestamp. |
| `sandbox` | string |  | sandbox is the resource name recorded for this reference. |
| `sandboxUid` | ['string', 'null'] |  | sandbox_uid retains the observed backing incarnation when the backend provides one. |
| `domain` | `PolicyDomain` |  | domain is the policy domain that emitted the entry. |

## Port

Port is one sandbox port made reachable from outside the sandbox. The same
facts appear inline on SandboxCore.ports for a caller reading the sandbox.

| Field | Type | Required | Description |
|---|---|---|---|
| `number` | integer (int32) | yes | (IMMUTABLE) number is immutable and unique within the sandbox; duplicates refuse ALREADY_EXISTS. |
| `protocol` | `Protocol` |  | (IMMUTABLE) protocol defaults to TCP when unspecified. |
| `url` | string |  | url is the required externally reachable address, including host-local addresses. |
| `etag` | string |  | etag identifies the observed version of this port. |
| `uid` | ['string', 'null'] |  | (IMMUTABLE) uid is the durable publication incarnation when the backend provides one. |
| `name` | string |  | (IDENTIFIER) name identifies the published port number under its sandbox resource name. |

## PreconditionFailure

Describes what preconditions have failed.

For example, if an operation failed because it required the Terms of Service to be
acknowledged, it could list the terms of service violation in the
PreconditionFailure message.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `PreconditionFailureViolation` |  | Describes all precondition violations. |

## PreconditionFailureErrorDetail

Describes what preconditions have failed.

For example, if an operation failed because it required the Terms of Service to be
acknowledged, it could list the terms of service violation in the
PreconditionFailure message.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `PreconditionFailureViolation` |  | Describes all precondition violations. |
| `@type` | string | yes |  |

## PreconditionFailureViolation

A message type used to describe a single precondition failure.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string |  | The type of PreconditionFailure. We recommend using a service-specific enum type to define the supported precondition violation subjects. For example, "TOS" for "Terms of Service violation". |
| `subject` | string |  | The subject, relative to the type, that failed. For example, "google.com/cloud" relative to the "TOS" type would indicate which terms of service is being referenced. |
| `description` | string |  | A description of how the precondition failed. Developers can use this description to understand how to fix the failure. For example: "Terms of service not accepted". |

## Process

Process is the handle returned before interaction begins.

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string', 'null'] |  | (IMMUTABLE) uid is the existing process incarnation, also used as the resource name terminal. |
| `pid` | integer (int32) |  | pid is the process id inside the sandbox when available. |
| `session` | string |  | session is the session tag from the create, empty when untagged. |
| `state` | `ProcessState` |  | state is the process state, concrete in conforming responses. |
| `lastStreamSequence` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | last_stream_sequence is the highest stream_sequence emitted for the process when this report was assembled; 0 before any output. |
| `receiptKind` | `ReceiptKind` |  | receipt_kind classifies this response on CreateProcess; every other operation returning a Process, including ListProcesses, always reports unspecified. |
| `exitCode` | ['integer', 'null', ' ', '(', 'i', 'n', 't', '3', '2', ')'] |  | exit_code is the process exit code, set only when state is exited and absent otherwise. |
| `label` | string | yes | (IMMUTABLE) label retains the unique, immutable process label and its generated default. |
| `name` | string |  | (IDENTIFIER) name is scoped to the discovered sandbox endpoint API base. |

## ProcessAttach

Attach selects the process and output resume point.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | name is the complete resource name, in the form processes/{process}. |
| `resumeFrom` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | resume_from resumes after a received or published stream_sequence; 0 means from the start. Missing output after this point fails with FAILED_PRECONDITION. |

## ProcessChunk

Chunk carries process output.

| Field | Type | Required | Description |
|---|---|---|---|
| `stream` | `StreamType` |  | stream identifies stdout, stderr, or PTY output. |
| `data` | string (byte) |  | data is output bytes. |
| `streamSequence` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | stream_sequence is one-based and strictly increases per process output stream. |

## ProcessExited

Exited reports process completion.

| Field | Type | Required | Description |
|---|---|---|---|
| `exitCode` | integer (int32) |  | exit_code is the process exit code. |
| `reason` | string |  | reason is backend-readable exit context. |

## ProcessHeartbeat

Heartbeat is an idle keepalive frame.

Type: object

## ProcessOutput

Output is one server frame on an interaction stream. At most one of chunk, exited, heartbeat is set.

| Field | Type | Required | Description |
|---|---|---|---|
| `chunk` | `ProcessChunk` |  | chunk carries ordered process output. |
| `exited` | `ProcessExited` |  | exited reports process completion. |
| `heartbeat` | `ProcessHeartbeat` |  | heartbeat keeps an idle stream alive and carries no resume position. |

## ProcessSignal

Signal is a process signal.

Values:
unspecified: unspecified is invalid.
term: term requests graceful termination.
kill: kill requests immediate termination.
int: int requests interrupt.
hup: hup requests hangup.
quit: quit requests quit.
usr1: usr1 requests user signal 1.
usr2: usr2 requests user signal 2.

Type: string enum: unspecified, term, kill, int, hup, quit, usr1, usr2

## ProcessState

ProcessState is the coarse process lifecycle a process report carries.

Values:
unspecified: unspecified is not a concrete state; conforming responses never use it.
running: running means the process has not exited.
exited: exited means the process has exited.

Type: string enum: unspecified, running, exited

## Protocol

Protocol names the transport protocol for a published port.

Values:
unspecified: unspecified means the backend default, TCP.
tcp: tcp publishes TCP traffic.
udp: udp publishes UDP traffic.
tcp4: tcp4 publishes IPv4 TCP traffic.
tcp6: tcp6 publishes IPv6 TCP traffic.
udp4: udp4 publishes IPv4 UDP traffic.
udp6: udp6 publishes IPv6 UDP traffic.

Type: string enum: unspecified, tcp, udp, tcp4, tcp6, udp4, udp6

## PtyConfig

PtyConfig configures pseudo-terminal creation.

| Field | Type | Required | Description |
|---|---|---|---|
| `initialSize` | `TerminalSize` |  | initial_size requests an initial terminal size; absence selects a backend-defined size. |

## PublishedPort

PublishedPort reports external reachability for one sandbox port.

| Field | Type | Required | Description |
|---|---|---|---|
| `hostIp` | string |  | host_ip is the local host bind address when relevant. |
| `hostPort` | integer |  | host_port is the local host port when relevant. |
| `sandboxPort` | integer |  | sandbox_port is the port inside the sandbox. |
| `protocol` | `Protocol` |  | protocol is the published protocol. |
| `url` | string |  | url is the required externally reachable address, including host-local addresses. |

## QuotaFailure

Describes how a quota check failed.

For example if a daily limit was exceeded for the calling project,
a service could respond with a QuotaFailure detail containing the project
id and the description of the quota limit that was exceeded.  If the
calling project hasn't enabled the service in the developer console, then
a service could respond with the project id and set `service_disabled`
to true.

Also see RetryInfo and Help types for other details about handling a
quota failure.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `QuotaFailureViolation` |  | Describes all quota violations. |

## QuotaFailureErrorDetail

Describes how a quota check failed.

For example if a daily limit was exceeded for the calling project,
a service could respond with a QuotaFailure detail containing the project
id and the description of the quota limit that was exceeded.  If the
calling project hasn't enabled the service in the developer console, then
a service could respond with the project id and set `service_disabled`
to true.

Also see RetryInfo and Help types for other details about handling a
quota failure.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `QuotaFailureViolation` |  | Describes all quota violations. |
| `@type` | string | yes |  |

## QuotaFailureViolation

A message type used to describe a single quota violation.  For example, a
daily quota or a custom quota that was exceeded.

| Field | Type | Required | Description |
|---|---|---|---|
| `subject` | string |  | The subject on which the quota check failed. For example, "clientip:<ip address of client>" or "project:<Google developer project id>". |
| `description` | string |  | A description of how the quota check failed. Clients can use this description to find more about the quota configuration in the service's public documentation, or find the relevant quota limit to adjust through developer console. For example: "Service disabled" or "Daily Limit for read operations exceeded". |
| `apiService` | string |  | The API Service from which the `QuotaFailure.Violation` orginates. In some cases, Quota issues originate from an API Service other than the one that was called. In other words, a dependency of the called API Service could be the cause of the `QuotaFailure`, and this field would have the dependency API service name. For example, if the called API is Kubernetes Engine API (container.googleapis.com), and a quota violation occurs in the Kubernetes Engine API itself, this field would be "container.googleapis.com". On the other hand, if the quota violation occurs when the Kubernetes Engine API creates VMs in the Compute Engine API (compute.googleapis.com), this field would be "compute.googleapis.com". |
| `quotaMetric` | string |  | The metric of the violated quota. A quota metric is a named counter to measure usage, such as API requests or CPUs. When an activity occurs in a service, such as Virtual Machine allocation, one or more quota metrics may be affected. For example, "compute.googleapis.com/cpus_per_vm_family", "storage.googleapis.com/internet_egress_bandwidth". |
| `quotaId` | string |  | The id of the violated quota. Also know as "limit name", this is the unique identifier of a quota in the context of an API service. For example, "CPUS-PER-VM-FAMILY-per-project-region". |
| `quotaDimensions` | object |  | The dimensions of the violated quota. Every non-global quota is enforced on a set of dimensions. While quota metric defines what to count, the dimensions specify for what aspects the counter should be increased. For example, the quota "CPUs per region per VM family" enforces a limit on the metric "compute.googleapis.com/cpus_per_vm_family" on dimensions "region" and "vm_family". And if the violation occurred in region "us-central1" and for VM family "n1", the quota_dimensions would be, { "region": "us-central1", "vm_family": "n1", } When a quota is enforced globally, the quota_dimensions would always be empty. |
| `quotaValue` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | The enforced quota value at the time of the `QuotaFailure`. For example, if the enforced quota value at the time of the `QuotaFailure` on the number of CPUs is "10", then the value of this field would reflect this quantity. |
| `futureQuotaValue` | ['integer', 'string', 'null', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | The new quota value being rolled out at the time of the violation. At the completion of the rollout, this value will be enforced in place of quota_value. If no rollout is in progress at the time of the violation, this field is not set. For example, if at the time of the violation a rollout is in progress changing the number of CPUs quota from 10 to 20, 20 would be the value of this field. |

## RawImageStartup

RawImageStartup resolves identity and working directory from the pinned image.

| Field | Type | Required | Description |
|---|---|---|---|
| `start` | `StartupArgv` |  | start replaces the complete launch argv; omission uses the image command. |

## ReadOutputResponse

ReadOutputResponse is one page of ordered output.

| Field | Type | Required | Description |
|---|---|---|---|
| `chunks` | array of `ProcessChunk` |  | chunks is retained output in stream_sequence order, possibly empty. |
| `nextResumeFrom` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | next_resume_from is the stream_sequence to pass next; equal to resume_from when nothing new was retained. |
| `exited` | `ProcessExited` |  | exited is set once the process has exited and no retained bytes follow next_resume_from. |

## ReceiptKind

ReceiptKind classifies whether a CreateProcess response was freshly assembled or
is the retained receipt of an earlier accepted request.

Values:
unspecified: unspecified is not a concrete classification; a backend or a client generated before this field existed reports or reads this. It asserts neither freshness nor replay.
fresh: fresh means this Process was assembled for this specific accepted request; last_stream_sequence reflects live state as of that acceptance.
replay: replay means the backend returned the retained result of an earlier accepted request under the synchronous mutation replay rule; last_stream_sequence is frozen at the value observed during that original acceptance.

Type: string enum: unspecified, fresh, replay

## RequestInfo

Contains metadata about the request that clients can attach when filing a bug
or providing other forms of feedback.

| Field | Type | Required | Description |
|---|---|---|---|
| `requestId` | string |  | An opaque string that should only be interpreted by the service generating it. For example, it can be used to identify requests in the service's logs. |
| `servingData` | string |  | Any data that was used to serve this request. For example, an encrypted stack trace that can be sent back to the service provider for debugging. |

## RequestInfoErrorDetail

Contains metadata about the request that clients can attach when filing a bug
or providing other forms of feedback.

| Field | Type | Required | Description |
|---|---|---|---|
| `requestId` | string |  | An opaque string that should only be interpreted by the service generating it. For example, it can be used to identify requests in the service's logs. |
| `servingData` | string |  | Any data that was used to serve this request. For example, an encrypted stack trace that can be sent back to the service provider for debugging. |
| `@type` | string | yes |  |

## ResourceInfo

Describes the resource that is being accessed.

| Field | Type | Required | Description |
|---|---|---|---|
| `resourceType` | string |  | A name for the type of resource being accessed, e.g. "sql table", "cloud storage bucket", "file", "Google calendar"; or the type URL of the resource: e.g. "type.googleapis.com/google.pubsub.v1.Topic". |
| `resourceName` | string |  | The name of the resource being accessed. For example, a shared calendar name: "example.com_4fghdhgsrgh@group.calendar.google.com", if the current error is [CodePERMISSION_DENIED][CodePERMISSION_DENIED]. |
| `owner` | string |  | The owner of the resource (optional). For example, "user:<owner email>" or "project:<Google developer project id>". |
| `description` | string |  | Describes what error is encountered when accessing this resource. For example, updating a cloud project may require the `writer` permission on the developer console project. |

## ResourceInfoErrorDetail

Describes the resource that is being accessed.

| Field | Type | Required | Description |
|---|---|---|---|
| `resourceType` | string |  | A name for the type of resource being accessed, e.g. "sql table", "cloud storage bucket", "file", "Google calendar"; or the type URL of the resource: e.g. "type.googleapis.com/google.pubsub.v1.Topic". |
| `resourceName` | string |  | The name of the resource being accessed. For example, a shared calendar name: "example.com_4fghdhgsrgh@group.calendar.google.com", if the current error is [CodePERMISSION_DENIED][CodePERMISSION_DENIED]. |
| `owner` | string |  | The owner of the resource (optional). For example, "user:<owner email>" or "project:<Google developer project id>". |
| `description` | string |  | Describes what error is encountered when accessing this resource. For example, updating a cloud project may require the `writer` permission on the developer console project. |
| `@type` | string | yes |  |

## Resources

Resources describes sandbox CPU and memory allocation.

| Field | Type | Required | Description |
|---|---|---|---|
| `cpus` | ['integer', 'null'] |  | cpus is present only when the caller or backend chooses a CPU count. |
| `memoryMib` | ['integer', 'string', 'null', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | memory_mib is present only when the caller or backend chooses memory. |

## RetryInfo

Describes when the clients can retry a failed request. Clients could ignore
the recommendation here or retry when this information is missing from error
responses.

It's always recommended that clients should use exponential backoff when
retrying.

Clients should wait until `retry_delay` amount of time has passed since
receiving the error response before retrying.  If retrying requests also
fail, clients should use an exponential backoff scheme to gradually increase
the delay between retries based on `retry_delay`, until either a maximum
number of retries have been reached or a maximum retry delay cap has been
reached.

| Field | Type | Required | Description |
|---|---|---|---|
| `retryDelay` | `Duration` |  | Clients should wait at least this long between retrying the same request. |

## RetryInfoErrorDetail

Describes when the clients can retry a failed request. Clients could ignore
the recommendation here or retry when this information is missing from error
responses.

It's always recommended that clients should use exponential backoff when
retrying.

Clients should wait until `retry_delay` amount of time has passed since
receiving the error response before retrying.  If retrying requests also
fail, clients should use an exponential backoff scheme to gradually increase
the delay between retries based on `retry_delay`, until either a maximum
number of retries have been reached or a maximum retry delay cap has been
reached.

| Field | Type | Required | Description |
|---|---|---|---|
| `retryDelay` | `Duration` |  | Clients should wait at least this long between retrying the same request. |
| `@type` | string | yes |  |

## Sandbox

Sandbox carries shared core state and the effective state of its selected features.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `core` | `SandboxCore` | yes | core is the backend-neutral sandbox view. |
| `effectiveFeatures` | `EffectiveFeatures` |  | effective_features is emitted only by the composition contract projection. |
| `failure` | `Error` |  | failure is present only while status is FAILED and clears on recovery. |
| `name` | string | yes | (IDENTIFIER) name ends in the immutable backing ID and never changes with display_name. |
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `displayName` | string |  | display_name is the scoped label; UpdateSandbox changes it without changing identity. |

## SandboxCore

SandboxCore is the backend-neutral sandbox view. At most one of image, imageRef is set.

Type: allOf(object, object)

## SandboxEndpoint

SandboxEndpoint tells a client where sandbox endpoint services are served.
network endpoints require scoped credentials; Unix sockets use actual socket access controls
sandbox must contain the endpoint's immutable sandbox UID

| Field | Type | Required | Description |
|---|---|---|---|
| `uri` | string |  | uri is the endpoint API base; preserve its path prefix when appending /v1 routes. |
| `protocol` | `SandboxEndpointProtocol` |  | protocol identifies the endpoint transport. |
| `credentialAudience` | string |  | credential_audience is server-controlled and required for network endpoints. |
| `sandbox` | string | yes | sandbox names the immutable sandbox incarnation served by this endpoint. |
| `sandboxUid` | ['string'] | yes |  |
| `apiVersion` | string | yes | api_version identifies the /v1 endpoint contract before the client connects. |
| `capabilities` | array of string | yes | capabilities lists supported public operation IDs, independently of caller grants. |
| `authentication` | `EndpointAuthentication` | yes |  |

## SandboxEndpointProtocol

SandboxEndpointProtocol identifies the transport used by a sandbox endpoint.

Values:
unspecified: unspecified is not a concrete endpoint protocol.
http: http is the REST API over HTTP.
unixSocket: unixSocket is a local unix socket.

Type: string enum: unspecified, http, unixSocket

## SandboxStatus

SandboxStatus is the backend-neutral lifecycle state.

Values:
unspecified: unspecified is never a concrete known state.
creating: creating means provisioning has not completed.
starting: starting means a stopped sandbox is starting or resuming.
running: running means the sandbox is running.
stopping: stopping means the sandbox is stopping or hibernating.
stopped: stopped means the sandbox is not running and may be started.
failed: failed means the sandbox reached an unrecoverable failure.
deleting: deleting means deletion is accepted; reads continue until removal.
degraded: degraded means runtime contact is lost; recovery or failure may follow.

Type: string enum: unspecified, creating, starting, running, stopping, stopped, failed, deleting, degraded

## Secret

Secret is returned metadata and never includes secret material.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | (IDENTIFIER) name ends in the immutable backing ID and never changes with display_name. |
| `serviceType` | string |  | service_type identifies the consuming service. |
| `type` | `SecretType` |  | type identifies the stored material shape. |
| `oauthConfig` | `OAuthConfig` |  | oauth_config is returned only for OAuth-shaped secrets. |
| `scopes` | array of string |  | scopes are non-secret OAuth scopes. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `updatedAt` | `Timestamp` | yes | updated_at is the last update timestamp. |
| `injection` | `CustomInjection` |  | injection is returned only for custom-shaped secrets. |
| `placeholder` | string |  | placeholder is server-generated per custom secret and stable across value rotation; it is not secret material. A client presents it where the credential would go; for the configured hosts the backend replaces the configured header's value at egress regardless of what was sent. |
| `etag` | string | yes | etag identifies the observed version of this resource. It is opaque and strong, changes on every visible change, and is what a mutation sends as its precondition. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## SecretType

The stored credential shape: token, OAuth refresh material, custom injection, registry credentials, or a credential resolved from an approved host-owned source. Secret material is never returned.

Type: string enum: unspecified, token, oauthRefresh, custom, registryV2, hostResolved

## SignalResponse

SignalResponse has no fields.

Type: object

## Snapshot

Snapshot is the detailed snapshot view.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | (IDENTIFIER) name ends in the immutable backing ID and never changes with display_name. |
| `description` | string |  | description is caller-supplied text. |
| `sandbox` | string |  | sandbox is the resource name recorded for this reference. |
| `sandboxUid` | ['string', 'null'] |  | sandbox_uid retains the observed backing incarnation when the backend provides one. |
| `status` | `SnapshotStatus` | yes | status is the snapshot readiness state. |
| `totalSizeBytes` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | total_size_bytes is the approximate stored snapshot size. |
| `resources` | `Resources` |  | resources describes the captured sandbox resources. |
| `platform` | `Platform` |  | platform is the captured sandbox platform. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `failure` | `Error` |  | failure is set when status is FAILED. |
| `captureMode` | `CaptureMode` |  | capture_mode is the mode the snapshot was captured with. |
| `etag` | string | yes | etag identifies the observed version of this resource. It is opaque and strong, changes on every visible change, and is what a mutation sends as its precondition. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## SnapshotStatus

SnapshotStatus is snapshot readiness state.

Values:
unspecified: unspecified is never a concrete known state.
creating: creating means capture has not completed.
ready: ready means the snapshot can be restored.
failed: failed means capture reached a terminal failure.
deleted: deleted means the backend exposes a retained delete tombstone.

Type: string enum: unspecified, creating, ready, failed, deleted

## SnapshotSummary

SnapshotSummary is the list view of a snapshot.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | name ends in the immutable backing ID and never changes with display_name. |
| `sandbox` | string |  | sandbox is the resource name recorded for this reference. |
| `sandboxUid` | ['string', 'null'] |  | sandbox_uid retains the observed backing incarnation when the backend provides one. |
| `status` | `SnapshotStatus` | yes | status is the snapshot readiness state. |
| `totalSizeBytes` | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | total_size_bytes is the approximate stored snapshot size. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `captureMode` | `CaptureMode` |  | capture_mode is the mode the snapshot was captured with. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## StartupArgv

StartupArgv preserves literal arguments, including empty positional arguments.
startup argv requires a nonempty executable

| Field | Type | Required | Description |
|---|---|---|---|
| `argv` | array of string | yes | argv is executed without shell expansion. It carries at least one element, and that first element is the executable and must not be empty. |

## StartupExecution

StartupExecution retains the accepted execution promise across fresh boots.
It is ordinary create input.

Type: oneOf(object)

## StopMemoryOutcome

StopMemoryOutcome records the stop/start guarantee independently of location.

Values:
unspecified: unspecified is not an advertised or accepted guarantee.
discard: discard retains disk and starts a fresh process tree.
preserve: preserve restores the stopped process tree on start.

Type: string enum: unspecified, discard, preserve

## StoredSecretOptions

StoredSecretOptions resolves owner-scoped references before the workload can run.

| Field | Type | Required | Description |
|---|---|---|---|
| `secrets` | array of string | yes | secrets are complete Secret resource names resolved once at admission. |

## StreamType

StreamType identifies the source of an output chunk.

Values:
unspecified: unspecified is not a concrete output stream.
stdout: stdout is stdout.
stderr: stderr is stderr.
pty: pty is merged PTY output.

Type: string enum: unspecified, stdout, stderr, pty

## TerminalSize

TerminalSize is a terminal rows/columns pair; 1 through 65535 is the portable range.
bounded requires rows and cols in 1..65535

| Field | Type | Required | Description |
|---|---|---|---|
| `rows` | integer |  | rows is the terminal row count. |
| `cols` | integer |  | cols is the terminal column count. |
| `bounded` | boolean |  | bounded requests the portable range enforced on this size, with no opt in to perform first. Unset or false keeps the unenforced behavior. |

## TimeoutAction

TimeoutAction selects the lifecycle action taken at the reported deadline.

Values:
unspecified: unspecified is invalid when explicitly supplied.
delete: delete deletes the sandbox at expiry.
stop: stop applies the sandbox's persisted stop guarantee at expiry.
keep: Deprecated alias for the restart action, still accepted on input and output. New clients should use the canonical restart action.
restart: Preserves memory through backend-managed stop/resume cycles at expiry. Requires memory preservation and the always-on entitlement.

Type: string enum: unspecified, delete, stop, keep, restart

## TimeoutOptions

TimeoutOptions selects deadline behavior; presence enables this feature for the sandbox.
an explicit RESTART (or its deprecated alias KEEP) initial timeout must be at least one hour

| Field | Type | Required | Description |
|---|---|---|---|
| `timeout` | `Duration` |  | timeout is the initial TTL; omission selects the advertised action default. |
| `onTimeout` | oneOf(`TimeoutAction`, null) |  | on_timeout defaults to DELETE; an explicit UNSPECIFIED is invalid. |
| `autoResume` | ['boolean', 'null'] |  | Omission selects the advertised default; false does not disable RESTART or KEEP cycles. |

## Timestamp

An RFC 3339 timestamp in UTC, for example 2026-01-02T03:04:05Z.

Type: string (date-time)

## TokenSecretMaterial

TokenSecretMaterial is opaque token material.

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | string | yes | value is the secret token. |

## UnknownErrorDetail

A structured error detail identified by @type. Its decoded JSON fields appear beside the type URL.

| Field | Type | Required | Description |
|---|---|---|---|
| `@type` | string | yes |  |

## UpdateSecretBody

UpdateSecretRequest replaces secret material.
service_type must be empty for custom material (server-assigned)

Type: allOf(object, oneOf(object, object, object))

## ValidationFieldPath

A path to a field, including any parent fields.

| Field | Type | Required | Description |
|---|---|---|---|
| `elements` | array of `ValidationFieldPathElement` |  | `elements` contains each element of the path, starting from the root and recursing downward. |

## ValidationFieldPathElement

One field in a validation path. For a map or list, the subscript identifies the selected element.

Type: allOf(object, oneOf(object, object, object, object, object))

## ValidationFieldType

Type: string enum: TYPE_DOUBLE, TYPE_FLOAT, TYPE_INT64, TYPE_UINT64, TYPE_INT32, TYPE_FIXED64, TYPE_FIXED32, TYPE_BOOL, TYPE_STRING, TYPE_GROUP, TYPE_MESSAGE, TYPE_BYTES

## ValidationViolation

A validation failure, with the affected field, rule, and a human-readable message.

| Field | Type | Required | Description |
|---|---|---|---|
| `field` | oneOf(`ValidationFieldPath`, null) |  | The field that failed validation, including its parent fields. |
| `rule` | oneOf(`ValidationFieldPath`, null) |  | The validation rule that failed. |
| `ruleId` | ['string', 'null'] |  | `rule_id` is the unique identifier of the `Rule` that was not fulfilled. This is the same `id` that was specified in the `Rule` message, allowing easy tracing of which rule was violated. |
| `message` | ['string', 'null'] |  | `message` is a human-readable error message that describes the nature of the violation. This can be the default error message from the violated `Rule`, or it can be a custom message that gives more context about the violation. |
| `forKey` | ['boolean', 'null'] |  | `for_key` indicates whether the violation was caused by a map key, rather than a value. |

## ValidationViolations

The validation failures returned for a request.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `ValidationViolation` |  | `violations` is a repeated field that contains all the `Violation` messages corresponding to the violations detected. |

## ValidationViolationsErrorDetail

The validation failures returned for a request.

| Field | Type | Required | Description |
|---|---|---|---|
| `violations` | array of `ValidationViolation` |  | `violations` is a repeated field that contains all the `Violation` messages corresponding to the violations detected. |
| `@type` | string | yes |  |

## Volume

Volume is persistent storage metadata within its owner and contract scope.
uid must equal the immutable resource ID in name

| Field | Type | Required | Description |
|---|---|---|---|
| `uid` | ['string'] | yes | (IMMUTABLE) uid is the existing backing ID, equal to the resource name's terminal segment. |
| `name` | string | yes | (IDENTIFIER) name ends in the immutable backing ID and never changes with display_name. |
| `createdAt` | `Timestamp` | yes | created_at is the creation timestamp. |
| `etag` | string | yes | etag identifies the observed version of this resource. It is opaque and strong, changes on every visible change, and is what a mutation sends as its precondition. |
| `displayName` | string |  | display_name is a scoped label and never selects the resource. |

## VolumeAttachment

VolumeAttachment binds an existing owner-scoped volume before guest execution.

| Field | Type | Required | Description |
|---|---|---|---|
| `volume` | string | yes | volume is the complete resource name, in the form volumes/{volume}. |
| `target` | string | yes | target is an absolute guest path and cannot overlap another mount target. |
| `mode` | `AttachmentMode` |  | mode defaults to exclusive; it never silently enables shared writers. |

