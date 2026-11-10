# Docker Sandboxes API v1 — Snapshots

## POST /sandboxes/v1/sandboxes/{sandbox}/snapshots

operationId: `createSnapshot`

CreateSnapshot checkpoints a running sandbox; a stopped source is rejected.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 201 | Success | allOf(`Snapshot`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Snapshot`, object) |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/snapshots

operationId: `listSnapshots`

ListSnapshots lists snapshots in the caller's owner scope.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | query | string |  | (OPTIONAL) sandbox is the complete resource name, in the form sandboxes/{sandbox}. |
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable fields are name, display_name and uid. |
| `orderBy` | query | string |  | order_by is a single order field with optional direction; the portable fields are created_at and name. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListSnapshotsResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/snapshots/{snapshot}

operationId: `getSnapshot`

GetSnapshot reads one snapshot by its resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot` | path | string | yes | The snapshot id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Snapshot` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/snapshots/{snapshot}

operationId: `deleteSnapshot`

DeleteSnapshot deletes a snapshot; deleting an already absent snapshot succeeds.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot` | path | string | yes | The snapshot id. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

| Response | Description | Body |
|---|---|---|
| 204 | Success. The response carries no body. |  |
| 409 | The target's preparation, capture, or import has not finished; deletion is refused until it settles to a terminal state. An admitted consumer or live resource holds a content lease on the target; deletion is refused while any lease remains held. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/snapshots/{snapshot}/restore

operationId: `restoreSnapshot`

RestoreSnapshot forks a new sandbox from a snapshot.

RestoreSnapshot forks a new sandbox from a snapshot.
Action: a restore creates a sandbox, so the snapshot in the path is the source and not
the created resource.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `snapshot` | path | string | yes | The snapshot id. |
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 201 | Success | allOf(`Sandbox`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Sandbox`, object) |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
