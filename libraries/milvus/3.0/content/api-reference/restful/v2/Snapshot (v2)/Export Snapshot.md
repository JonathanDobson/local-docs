---
title: "Export Snapshot"
---

# Export Snapshot

`POST /v2/vectordb/jobs/snapshot/export`

Exports a collection snapshot to the configured object storage.

## Parameters

- `Authorization` (in header) — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database that contains the collection.
- `collectionName` (string) **required** — The name of the collection to snapshot.
- `snapshotName` (string) **required** — The name of the snapshot.
- `targetS3Path` (string) **required** — The root path in S3-compatible object storage under which Milvus writes the exported snapshot data and metadata. It must be a writable URI such as `s3://bucket-name/export-root`. Milvus appends snapshot-specific metadata paths below this root; the response returns the generated `snapshotMetadataURI`.
- `externalSpec` (string) — Optional JSON configuration for external object storage. When `targetS3Path` points to storage outside the Milvus-managed bucket, pass an `extfs` object to override how Milvus accesses that bucket. Supported JSON fields: - `format`: `"parquet"`, `"lance-table"`, or `"vortex"`; defaults to `"parquet"` when omitted or when the whole value is empty. - `columns`: optional array of column names to load. - `extfs`: optional map of object-storage overrides. Allowed keys are `cloud_provider`, `region`, `use_iam`, `use_ssl`, `use_virtual_host`, `iam_endpoint`, `storage_type`, `ssl_ca_cert`, `access_key_id`, and `access_key_value`. Requirements: - The value must be valid JSON. - `format` must be one of the supported values above. - `extfs` keys are allowlisted; unsupported keys are rejected. - `use_iam`, `use_ssl`, and `use_virtual_host` must be the strings `"true"` or `"false"`. - Use `extfs` only when the target bucket requires credentials or connectivity settings different from the Milvus-managed bucket. Omit `externalSpec` or pass an empty string to use the default Milvus-managed storage. Example: `{"format":"parquet","extfs":{"cloud_provider":"aws","region":"us-west-2","use_iam":"true"}}`.

## Response 200

Exports a collection snapshot to the configured object storage.

- **oneOf – success**: A response envelope containing either `code` and `data` for a successful snapshot export, or `code` and `message` for an error response.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — Response payload containing `snapshotMetadataURI`, the URI of the exported snapshot metadata.
    - `snapshotMetadataURI` (string) **required** — The object-storage URI of the exported snapshot metadata.
- **oneOf – failure**: A response envelope containing either `code` and `data` for a successful snapshot export, or `code` and `message` for an error response.
  - `code` (integer) **required** — Response code.
  - `message` (string) **required** — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "snapshotMetadataURI": "s3://bucket/snapshots/snapshot_2026_01"
  }
}
```

Example – failure:

```json
{
  "code": 1100,
  "message": "snapshot operation failed"
}
```
