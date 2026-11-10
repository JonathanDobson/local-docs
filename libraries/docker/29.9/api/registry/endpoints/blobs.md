# Supported registry API for Docker Hub 2 — Blobs

## POST /v2/{name}/blobs/uploads/

operationId: `InitiateBlobUpload`

Initiate blob upload or attempt cross-repository blob mount

Initiate an upload session for a blob (layer or config) in a repository.

This is the first step in uploading a blob. It returns a `Location` URL where the blob can be uploaded using `PATCH` (chunked) or `PUT` (monolithic).

Instead of uploading a blob, a client may attempt to mount a blob from another repository (if it has read access) by including the `mount` and `from` query parameters.

If successful, the registry responds with `201 Created` and the blob is reused without re-upload.

If the mount fails, the upload proceeds as usual and returns a `202 Accepted`.

You must authenticate with `push` access to the target repository.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the target repository |
| `mount` | query | string |  | Digest of the blob to mount from another repository |
| `from` | query | string |  | Source repository to mount the blob from |

| Response | Description | Body |
|---|---|---|
| 201 | Blob successfully mounted from another repository. |  |
| 202 | Upload initiated successfully (fallback if mount fails). |  |
| 401 | Authentication required. |  |
| 403 | Access denied. |  |
| 404 | Repository not found. |  |
| 429 | Too many requests. |  |

## GET /v2/{name}/blobs/{digest}

operationId: `GetBlob`

Retrieve blob

Download the blob identified by digest from the registry.

Blobs include image layers and configuration objects. Clients must use the digest from the manifest to retrieve a blob.

This endpoint may return a `307 Temporary Redirect` to a CDN or storage location. Clients must follow the redirect to obtain the actual blob content.

The blob content is typically a gzipped tarball (for layers) or JSON (for configs). The MIME type is usually `application/octet-stream`.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Repository Name |
| `digest` | path | string | yes | Digest of the Blob |

| Response | Description | Body |
|---|---|---|
| 200 | Blob content returned directly | string (binary) |
| 307 | Temporary redirect to blob location |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Blob not found |  |
| 429 | Too many requests |  |

## HEAD /v2/{name}/blobs/{digest}

operationId: `CheckBlobExists`

Check existence of blob

Check whether a blob (layer or config) exists in the registry.

This is useful before uploading a blob to avoid duplicates.

If the blob is present, the registry returns a `200 OK` response with headers like `Content-Length` and `Docker-Content-Digest`.

If the blob does not exist, the response will be `404 Not Found`.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the Repository |
| `digest` | path | string | yes | Digest of the blob |

| Response | Description | Body |
|---|---|---|
| 200 | Blob exists |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Blob not found |  |
| 429 | Too many requests |  |

## GET /v2/{name}/blobs/uploads/{uuid}

operationId: `GetBlobUploadStatus`

Get blob upload status

Retrieve the current status of an in-progress blob upload.

This is useful for:
- Resuming an interrupted upload
- Determining how many bytes have been accepted so far
- Retrying from the correct offset in chunked uploads

The response includes the `Range` header indicating the byte range received so far, and a `Docker-Upload-UUID` for identifying the session.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Repository Name |
| `uuid` | path | string | yes | Upload session UUID |

| Response | Description | Body |
|---|---|---|
| 204 | Upload in progress. No body is returned. |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Upload session not found |  |
| 429 | Too many requests |  |

## PUT /v2/{name}/blobs/uploads/{uuid}

operationId: `CompleteBlobUpload`

Complete blob upload

Complete the upload of a blob by finalizing an upload session.

This request must include the `digest` query parameter and optionally the last chunk of data. When the registry receives this request, it verifies the digest and stores the blob.

This endpoint supports:
- Monolithic uploads (upload entire blob in this request)
- Finalizing chunked uploads (last chunk plus `digest`)

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Repository name |
| `uuid` | path | string | yes | Upload session UUID returned from the POST request |
| `digest` | query | string | yes | Digest of the uploaded blob |

Request body (application/octet-stream): string (binary)

| Response | Description | Body |
|---|---|---|
| 201 | Upload completed successfully |  |
| 400 | Invalid digest or missing parameters |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Upload session not found |  |
| 416 | Requested range not satisfiable (if used in chunked mode) |  |
| 429 | Too many requests |  |

## PATCH /v2/{name}/blobs/uploads/{uuid}

operationId: `UploadBlobChunk`

Upload blob chunk

Upload a chunk of a blob to an active upload session.

Use this method for **chunked uploads**, especially for large blobs or when resuming interrupted uploads.

The client sends binary data using `PATCH`, optionally including a `Content-Range` header.

After each chunk is accepted, the registry returns a `202 Accepted` response with:
- `Range`: current byte range stored
- `Docker-Upload-UUID`: identifier for the upload session
- `Location`: URL to continue the upload or finalize with `PUT`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Repository name |
| `uuid` | path | string | yes | Upload session UUID |
| `Content-Range` | header | string |  | Optional. Byte range of the chunk being sent |

Request body (application/octet-stream): string (binary)

| Response | Description | Body |
|---|---|---|
| 202 | Chunk accepted and stored |  |
| 400 | Malformed content or range |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Upload session not found |  |
| 416 | Range error (e.g., chunk out of order) |  |
| 429 | Too many requests |  |

## DELETE /v2/{name}/blobs/uploads/{uuid}

operationId: `CancelBlobUpload`

Cancel blob upload

Cancel an in-progress blob upload session.

This operation discards any data that has been uploaded and invalidates the upload session.

Use this when:
- An upload fails or is aborted mid-process
- The client wants to clean up unused upload sessions

After cancellation, the UUID is no longer valid and a new `POST` must be issued to restart the upload.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the repository |
| `uuid` | path | string | yes | Upload session UUID |

| Response | Description | Body |
|---|---|---|
| 204 | Upload session cancelled successfully. No body is returned. |  |
| 401 | Authentication required |  |
| 403 | Access denied |  |
| 404 | Upload session not found |  |
| 429 | Too many requests |  |
