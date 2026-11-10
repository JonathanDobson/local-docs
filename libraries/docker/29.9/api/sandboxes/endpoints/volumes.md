# Docker Sandboxes API v1 — Volumes

## GET /sandboxes/v1/volumes

operationId: `listVolumes`

ListVolumes lists volumes in the caller's owner scope.

ListVolumes lists volumes in the caller's owner scope.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable fields are name, display_name and uid. |
| `orderBy` | query | string |  | order_by is a single order field with optional direction; the portable fields are created_at and name. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListVolumesResponse` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/volumes

operationId: `createVolume`

CreateVolume creates a persistent volume.

CreateVolume creates a persistent volume.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): `CreateVolumeRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Success | `Volume` |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The Idempotency-Key was already used with a different payload. | `Error` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/volumes/{volume}

operationId: `getVolume`

GetVolume reads one volume by its resource name.

GetVolume reads one volume by its resource name.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `volume` | path | string | yes | The volume id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Volume` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/volumes/{volume}

operationId: `deleteVolume`

DeleteVolume deletes a volume; deleting an already absent volume succeeds.

DeleteVolume deletes a volume; deleting an already absent volume succeeds.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `volume` | path | string | yes | The volume id. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

| Response | Description | Body |
|---|---|---|
| 204 | Success. The response carries no body. |  |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
