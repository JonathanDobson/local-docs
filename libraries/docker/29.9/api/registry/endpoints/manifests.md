# Supported registry API for Docker Hub 2 — Manifests

## GET /v2/{name}/manifests/{reference}

operationId: `GetImageManifest`

Get image manifest

Fetch the manifest identified by `name` and `reference`, where `reference` can be a tag (e.g., `latest`) or a digest (e.g., `sha256:...`).

The manifest contains metadata about the image, including configuration and layer digests. It is required for pulling images from the registry.

This endpoint requires authentication. Use the `Authorization: Bearer <token>` header.

Use the `Accept` header to select the manifest representation. Supported media types:

- `application/vnd.docker.distribution.manifest.v2+json`
- `application/vnd.docker.distribution.manifest.list.v2+json`
- `application/vnd.oci.image.manifest.v1+json`
- `application/vnd.oci.image.index.v1+json`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the target repository |
| `reference` | path | string | yes | Tag or digest of the target manifest |

| Response | Description | Body |
|---|---|---|
| 200 | Manifest fetched successfully. | object |
| 400 | Invalid name or reference. |  |
| 401 | Authentication required. |  |
| 403 | Access denied. |  |
| 404 | Repository or manifest not found. |  |
| 429 | Too many requests. |  |

## PUT /v2/{name}/manifests/{reference}

operationId: `PutImageManifest`

Put image manifest

Upload an image manifest for a given tag or digest. This operation registers a manifest in a repository, allowing it to be pulled using the specified reference.

This endpoint is typically used after all layer and config blobs have been uploaded to the registry.

The manifest must conform to the expected schema and media type. For Docker image manifest schema version 2, use:
`application/vnd.docker.distribution.manifest.v2+json`

Requires authentication via a bearer token with `push` scope for the target repository.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the target Repository |
| `reference` | path | string | yes | Tag or digest to associate with the uploaded Manifest |

Request body (application/vnd.docker.distribution.manifest.v2+json): object

| Response | Description | Body |
|---|---|---|
| 201 | Manifest created successfully. |  |
| 400 | Invalid name, reference, or manifest. |  |
| 401 | Authentication required. |  |
| 403 | Access denied. |  |
| 404 | Repository not found. |  |
| 405 | Operation not allowed. |  |
| 429 | Too many requests. |  |

## DELETE /v2/{name}/manifests/{reference}

operationId: `DeleteImageManifest`

Delete image manifest

Delete an image manifest from a repository by digest.

Only untagged or unreferenced manifests can be deleted. If the manifest is still referenced by a tag or another image, the registry will return `403 Forbidden`.

This operation requires `delete` access to the repository.

> **Note**
>
> Manifest deletion operations may take some time and could return a `500 Internal Server Error`. The system automatically retries the deletion in the background. Manual intervention is not required.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the repository |
| `reference` | path | string | yes | Digest of the manifest to delete (e.g., `sha256:...`) |

| Response | Description | Body |
|---|---|---|
| 202 | Manifest deleted successfully. No content returned. |  |
| 401 | Authentication required. |  |
| 403 | Access denied. The manifest may still be referenced. |  |
| 404 | Manifest or repository not found. |  |
| 405 | Only digest-based deletion is allowed. |  |
| 429 | Too many requests. |  |

## HEAD /v2/{name}/manifests/{reference}

operationId: `HeadImageManifest`

Check if manifest exists

Use this endpoint to verify whether a manifest exists by tag or digest.

This is a lightweight operation that returns only headers (no body). It is useful for:
- Checking for the existence of a specific image version
- Determining the digest or size of a manifest before downloading or deleting

This endpoint requires authentication with pull scope.

Use the `Accept` header to select the manifest representation. Supported media types:

- `application/vnd.docker.distribution.manifest.v2+json`
- `application/vnd.docker.distribution.manifest.list.v2+json`
- `application/vnd.oci.image.manifest.v1+json`
- `application/vnd.oci.image.index.v1+json`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the Repository |
| `reference` | path | string | yes | Tag or digest to check |

| Response | Description | Body |
|---|---|---|
| 200 | Manifest exists. |  |
| 401 | Authentication required. |  |
| 403 | Access denied. |  |
| 404 | Manifest not found. |  |
| 429 | Too many requests. |  |
