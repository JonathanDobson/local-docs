# Docker Sandboxes API v1 — Processes

## GET /sandboxes/v1/processes

operationId: `listProcesses`

ListProcesses lists processes in creation order.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an optional continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable fields are session and state. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListProcessesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/processes

operationId: `createProcess`

CreateProcess starts a durable interactive process and returns its resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): `CreateProcessRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Success | `Process` |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/processes/exec

operationId: `exec`

Exec runs one command to completion.

Exec runs one command to completion. A retry after transport failure may run it again.
Action at the collection root: it runs a command to completion instead of creating a
process a caller can address.

Request body (application/json): `ExecRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ExecResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/processes/{process}

operationId: `getProcess`

GetProcess reads one process by its endpoint-scoped resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `process` | path | string | yes | The process id. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Process` |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/processes/{process}/interact

operationId: `interact`

Interact binds the complete process name from the path to the first Attach frame.

Interact binds the complete process name from the path to the first Attach frame.
A conflicting name is INVALID_ARGUMENT before any attach.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `process` | path | string | yes | The process id. |

| Response | Description | Body |
|---|---|---|
| 101 | The connection becomes a sandboxes.v1 session: one InteractRequest per inbound text frame and one ProcessOutput per outbound one. Path parameters identify the target; the first attach frame must agree. Refusals after upgrade carry an error frame followed by a close code. |  |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/processes/{process}/output

operationId: `readOutput`

ReadOutput returns one page of retained output after a stream_sequence, the same cursor Interact resumes from, so a REST client can read what a process printed.

ReadOutput returns one page of retained output after a stream_sequence, the
same cursor Interact resumes from, so a REST client can read what a process printed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `process` | path | string | yes | The process id. |
| `resumeFrom` | query | ['integer', 'string', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | resume_from returns output after this stream_sequence; 0 means from the start. Missing output after this point fails with FAILED_PRECONDITION, as for Attach. |
| `maxBytes` | query | integer |  | max_bytes is a soft bound on the page's data: whole chunks only, and the first retained chunk always fits so a caller always advances. 0 means the backend's default page. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ReadOutputResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/processes/{process}/signal

operationId: `signal`

Signal sends one signal to an existing process.

Signal sends one signal to an existing process.
Action: a signal is delivered to a running process and leaves no representation to
replace.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `process` | path | string | yes | The process id. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `SignalResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
