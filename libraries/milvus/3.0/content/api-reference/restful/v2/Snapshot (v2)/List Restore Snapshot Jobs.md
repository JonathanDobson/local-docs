---
title: "List Restore Snapshot Jobs"
---

# List Restore Snapshot Jobs

`POST /v2/vectordb/jobs/snapshot/list`

Lists restore snapshot jobs, optionally filtered by database or collection.

## Parameters

- `Authorization` (in header) — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to filter by.
- `collectionName` (string) — The name of the collection to filter by.

## Response 200

Lists restore snapshot jobs, optionally filtered by database or collection.

- **oneOf – success**: The response body for listing snapshot jobs, including a `code` and either a `data` payload or a `message`.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — The response payload containing the snapshot job `records` returned by the list operation.
    - `records` (array<object>) **required** — The restore snapshot jobs matching the request filters.
      - `jobId` (integer) **required** — The unique identifier of the restore job. · format: `"int64"`
      - `snapshotName` (string) **required** — The name of the snapshot being restored.
      - `dbName` (string) **required** — The target database name.
      - `collectionName` (string) **required** — The target collection name.
      - `state` (string) **required** — The current state of the restore job.
      - `progress` (integer) **required** — The progress of the restore job as a percentage.
      - `reason` (string) — The failure reason when the restore job fails.
      - `startTime` (string) — The timestamp when the restore job started.
      - `timeCost` (integer) — The elapsed time of the restore job in milliseconds. · format: `"int64"`
- **oneOf – failure**: The response body for listing snapshot jobs, including a `code` and either a `data` payload or a `message`.
  - `code` (integer) **required** — Response code.
  - `message` (string) **required** — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "records": [
      {
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
    ]
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
