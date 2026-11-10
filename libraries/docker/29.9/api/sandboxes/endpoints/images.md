# Docker Sandboxes API v1 — Images

## GET /sandboxes/v1/images

operationId: `listImages`

ListImages lists images in the caller's owner scope.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable fields are name, display_name, uid and status. |
| `orderBy` | query | string |  | order_by is a single order field with optional direction; the portable fields are created_at and name. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListImagesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/images

operationId: `createImage`

CreateImage registers pushed OCI content or disk content derived from a snapshot or sandbox.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `Idempotency-Key` | header | string |  | Replay key. Reusing it with a different payload fails with failedPrecondition; accepted keys are retained for at least 24 hours. |

Request body (application/json): `CreateImageRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Success | allOf(`Image`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`Image`, object) |
| 409 | Creation conflicts with an existing resource (ALREADY_EXISTS). The Idempotency-Key was already used with a different payload. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/images/{image}

operationId: `getImage`

GetImage reads one image by its resource name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `image` | path | string | yes | The image id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `Image` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/images/{image}

operationId: `deleteImage`

DeleteImage deletes an image; deleting an already absent image succeeds.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `image` | path | string | yes | The image id. |
| `If-Match` | header | string | yes | The complete quoted strong entity-tag observed on the resource, including its quotes. Every mutation of an existing resource requires it: an absent value answers 428 and a stale one 412, each carrying failedPrecondition in the body. |

| Response | Description | Body |
|---|---|---|
| 204 | Success. The response carries no body. |  |
| 409 | The target's preparation, capture, or import has not finished; deletion is refused until it settles to a terminal state. An admitted consumer or live resource holds a content lease on the target; deletion is refused while any lease remains held. | `Error` |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| 428 | No precondition was sent. The body carries failedPrecondition naming etag_required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/images/{image}/pull-spec

operationId: `getImagePullSpec`

GetImagePullSpec returns short-lived pull material through registry-transfer support.

GetImagePullSpec returns short-lived pull material through registry-transfer support.
Action: the pull spec is derived material about the image, not a sub-resource of it.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `image` | path | string | yes | The image id. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ImagePullSpec` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
