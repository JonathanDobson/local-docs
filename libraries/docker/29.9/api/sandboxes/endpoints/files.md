# Docker Sandboxes API v1 — Files

## GET /sandboxes/v1/files

operationId: `list`

List lists directory entries by path ascending.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `path` | query | string | yes | path is the directory path. |
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an optional continuation token. |
| `orderBy` | query | string |  | order_by is a single order field with optional direction; the portable field is path. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesListResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## DELETE /sandboxes/v1/files

operationId: `remove`

Remove deletes a path.

Remove deletes a path. Removing an absent path succeeds. A nonrecursive
removal of a nonempty directory returns FAILED_PRECONDITION unchanged.
A recursive removal that stops partway still answers OK: check
RemoveResponse.failed_path, not the operation status. Removed paths stay removed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `path` | query | string | yes | path is the sandbox path to remove. |
| `recursive` | query | boolean |  | recursive removes directory contents when true. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesRemoveResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/files/content

operationId: `readFile`

ReadFile returns raw file content over HTTP; Stat exposes file metadata.

ReadFile returns raw file content over HTTP; Stat exposes file metadata.
Content above the unary message cap is refused, never truncated.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `path` | query | string | yes | path is the sandbox path of a regular file. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | object |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## PUT /sandboxes/v1/files/content

operationId: `writeFile`

WriteFile accepts raw content with path and mode query parameters.

WriteFile accepts raw content with path and mode query parameters.
It replaces the complete target state and carries no request_id.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `path` | query | string | yes | path is the sandbox path. |
| `mode` | query | integer |  | mode carries Unix permission bits. Upload applies mode & 0777, or 0644 when that value is zero, without subtracting umask; Download reports stored bits. |

Request body (application/octet-stream): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesWriteFileResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## PUT /sandboxes/v1/files/directories

operationId: `mkdir`

Mkdir creates a directory.

Mkdir creates a directory. Without parents, a missing parent returns
NOT_FOUND without creating directories. A repeated Mkdir converges when
the leaf already exists as a directory. A converged call leaves
the directory's mode unchanged on every request.

Request body (application/json): `FilesMkdirRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesMkdirResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/files/download

operationId: `download`

Download streams file headers, bytes, and per-file errors.

Download streams file headers, bytes, and per-file errors. A path that
leaves the jail through a symlink, or names a non-regular object, reports
a FileError with a error reason instead of reading through it.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `paths` | query | array of string | yes | paths naming stable regular files or absent entries at canonical absolute paths yield contiguous results in request order, including duplicates. |

| Response | Description | Body |
|---|---|---|
| 200 | Success Read metadata followed by one continuous raw content part. JSON controls are separate parts with Content-Type application/json; binary content uses application/octet-stream. A final stream-error part carries the shared Error for a whole-stream failure. A clean closing delimiter with no stream-error is required for success; aborted connections are failures. |  |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/files/move

operationId: `move`

Move renames or moves a path.

Move renames or moves a path. The destination is exact: an existing regular
file is replaced, the source basename is never appended, and a directory
destination is refused unchanged. A source or destination that leaves the jail
through a symlink refuses with FAILED_PRECONDITION and a error reason.

Request body (application/json): `FilesMoveRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesMoveResponse` |
| 409 | The path resolves through a symlink that does not resolve to a target inside the sandbox jail. The path names an existing socket, FIFO, device, or other non-regular object where a regular file is required. `from` names a regular file and `to` an existing directory, which `Move` refuses rather than moving the file into it. `from` names a directory and `to` an existing path, which `Move` refuses rather than replacing. `from` and `to` are on different filesystems, and `Move` never copies the contents to cross the boundary. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/files/stat

operationId: `stat`

Stat reads metadata for one path.

Stat reads metadata for one path.
A metadata read has a different response from the file-content resource.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `path` | query | string | yes | path is the sandbox path. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesStatResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/files/upload

operationId: `upload`

Upload streams one or more files.

Upload streams one or more files. The first frame must be FileHeader.
Writing through a symlink that leaves the jail, or onto an existing
non-regular object, refuses with FAILED_PRECONDITION and a error reason.

Request body (multipart/form-data): 

| Response | Description | Body |
|---|---|---|
| 200 | Success | `FilesUploadResponse` |
| 409 | The path resolves through a symlink that does not resolve to a target inside the sandbox jail. The path names an existing socket, FIFO, device, or other non-regular object where a regular file is required. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
