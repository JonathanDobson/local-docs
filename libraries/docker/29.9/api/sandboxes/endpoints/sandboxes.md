# Docker Sandboxes API v1 — Sandboxes

## GET /sandboxes/v1/sandboxes

operationId: `listSandboxes`

ListSandboxes lists sandboxes in the caller's owner scope.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable fields are name, display_name, uid, status and agent. |
| `orderBy` | query | string |  | order_by is a single order field with optional direction; the portable fields are created_at and name. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListSandboxesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes

operationId: `createSandbox`

CreateSandbox admits a sandbox.

CreateSandbox admits a sandbox. Unknown fields at any level are rejected before
replay lookup, reservation, policy binding, or workload effects.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): `CreateSandboxRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Success | allOf(`Sandbox`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Sandbox`, object) |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). Kit admission was refused; an available settled report describes the rejected fields. The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}

operationId: `getSandbox`

GetSandbox reads one sandbox by its resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Sandbox` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## PATCH /sandboxes/v1/sandboxes/{sandbox}

operationId: `updateSandbox`

UpdateSandbox changes only the display label under the observed etag.

UpdateSandbox changes only the display label under the observed etag.
Its resource name, backing identity and child addresses remain unchanged.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string | yes | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Sandbox` |
| 409 | The Idempotency-Key was already used with a different payload. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/sandboxes/{sandbox}

operationId: `deleteSandbox`

DeleteSandbox returns the deleting resource while work remains, or an empty message when absent.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |
| `force` | query | boolean |  | force requests deletion even when the backend would otherwise refuse the state. |

| Response | Description | Body |
|---|---|---|
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Sandbox`, object) |
| 204 | Success. The response carries no body. |  |
| 409 | The Idempotency-Key was already used with a different payload. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/endpoint-credentials

operationId: `createEndpointCredential`

CreateEndpointCredential grants short-lived access to one sandbox endpoint.

CreateEndpointCredential grants short-lived access to one sandbox endpoint.
Issuance checks current authority and never stores a token in the replay ledger.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `EndpointCredential` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}/ports

operationId: `listPorts`

ListPorts lists currently published ports for one sandbox.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListPortsResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/ports

operationId: `createPort`

CreatePort makes one sandbox port reachable outside the sandbox.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 201 | Success | `Port` |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The sandbox already publishes this port number. The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}/ports/{port}

operationId: `getPort`

GetPort reads one published port by its resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `port` | path | string | yes | The port id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Port` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | No publication exists for this port resource name. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/sandboxes/{sandbox}/ports/{port}

operationId: `deletePort`

DeletePort withdraws one published port.

DeletePort withdraws one published port. A name that is not published
succeeds, so a retried delete reports the same result as the first.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `port` | path | string | yes | The port id. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

| Response | Description | Body |
|---|---|---|
| 204 | Success. The response carries no body. |  |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/renew-timeout

operationId: `renewSandboxTimeout`

RenewSandboxTimeout sets a TTL when timeout renewal is supported.

RenewSandboxTimeout sets a TTL when timeout renewal is supported. The TTL starts at acceptance, and the response returns the new expires_at with the sandbox's timeout configuration preserved.
Action: the TTL restarts at acceptance, so the result is not a value the caller could
PUT.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Sandbox` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/ssh-certificates

operationId: `issueSSHCert`

IssueSSHCert signs a caller-held public key for sandbox SSH access.

IssueSSHCert signs a caller-held public key for sandbox SSH access.
A create: each call mints one certificate under the sandbox's certificate collection.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 201 | Success | `IssueSSHCertResponse` |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). | `Error` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/start

operationId: `startSandbox`

StartSandbox starts a stopped sandbox; a backend that preserved memory resumes it.

StartSandbox starts a stopped sandbox; a backend that preserved memory resumes it.
Action: a lifecycle transition is not a representation a caller can PUT.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | allOf(`Sandbox`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Sandbox`, object) |
| 409 | The Idempotency-Key was already used with a different payload. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/stop

operationId: `stopSandbox`

StopSandbox stops a running sandbox; a backend advertising memory preservation hibernates it.

StopSandbox stops a running sandbox; a backend advertising memory preservation hibernates it.
Action: a lifecycle transition is not a representation a caller can PUT.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | allOf(`Sandbox`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Sandbox`, object) |
| 409 | The Idempotency-Key was already used with a different payload. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
