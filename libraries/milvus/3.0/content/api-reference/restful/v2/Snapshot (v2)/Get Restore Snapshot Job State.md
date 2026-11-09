---
title: "Get Restore Snapshot Job State"
---

# Get Restore Snapshot Job State

`POST /v2/vectordb/jobs/snapshot/describe`

Retrieves the current state of a restore snapshot job.

## Parameters

- `Authorization` (in header) — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `jobId` (string) **required** — The ID of the restore snapshot job.

## Response 200

Retrieves the current state of a restore snapshot job.

- **oneOf – success**: A response envelope containing either `code` and `data` for a successful snapshot job description, or `code` and `message` for an error response.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — Detailed information about a restore snapshot job.
    - `jobId` (integer) **required** — The unique identifier of the restore job. · format: `"int64"`
    - `snapshotName` (string) **required** — The name of the snapshot being restored.
    - `dbName` (string) **required** — The target database name.
    - `collectionName` (string) **required** — The target collection name.
    - `state` (string) **required** — The current state of the restore job.
    - `progress` (integer) **required** — The progress of the restore job as a percentage.
    - `reason` (string) — The failure reason when the restore job fails.
    - `startTime` (string) — The timestamp when the restore job started.
    - `timeCost` (integer) — The elapsed time of the restore job in milliseconds. · format: `"int64"`
- **oneOf – failure**: A response envelope containing either `code` and `data` for a successful snapshot job description, or `code` and `message` for an error response.
  - `code` (integer) **required** — Response code.
  - `message` (string) **required** — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "jobId": 451799928999570200,
    "snapshotName": "snapshot_2026_01",
    "dbName": "default",
    "collectionName": "my_collection",
    "state": "RestoreSnapshotCompleted",
    "progress": 100,
    "reason": "",
    "startTime": "2026-01-01T00:00:00Z",
    "timeCost": 1200
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
