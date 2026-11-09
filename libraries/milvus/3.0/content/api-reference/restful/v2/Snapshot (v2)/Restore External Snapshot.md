---
title: "Restore External Snapshot"
---

# Restore External Snapshot

`POST /v2/vectordb/jobs/snapshot/restore_external`

Restores a collection from an externally stored snapshot.

## Parameters

- `Authorization` (in header) — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The target database name.
- `targetCollectionName` (string) **required** — The name of the target collection.
- `snapshotMetadataURI` (string) **required** — The object-storage URI of the snapshot metadata to restore.
- `externalSpec` (string) — Optional external storage specification.

## Response 200

Restores a collection from an externally stored snapshot.

- **oneOf – success**: The response body for an external snapshot restore request, including a `code` and either a `data` payload or a `message`.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — The response payload containing the `jobId` of the external snapshot restore job.
    - `jobId` (integer) **required** — The unique identifier of the created restore job. · format: `"int64"`
- **oneOf – failure**: The response body for an external snapshot restore request, including a `code` and either a `data` payload or a `message`.
  - `code` (integer) **required** — Response code.
  - `message` (string) **required** — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "jobId": 451799928999570200
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
