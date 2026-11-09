---
title: "List External Collection Refresh Jobs"
---

# List External Collection Refresh Jobs

`POST /v2/vectordb/jobs/external_collection/list`

This operation lists external-collection refresh jobs. When `collectionName` is omitted or empty, returns refresh jobs across all external collections in the target database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — Name of the database to list refresh jobs from.
- `collectionName` (string) — Name of the external collection. Leave empty or omit to list refresh jobs for all external collections in the database.

## Response 200

Returns the list of refresh jobs.

- **anyOf – success**: One of the alternative response bodies that may be returned when listing external Collection refresh jobs; only one variant is present in a given response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload that wraps the list of refresh jobs.
    - `records` (array<object>) — List of refresh jobs in detail.
      - `jobId` (integer) — ID of the refresh job. · format: `"int64"`
      - `collectionName` (string) — Name of the external collection associated with this refresh job.
      - `state` (string) — Current state of the refresh job. · enum: `["RefreshPending", "RefreshInProgress", "RefreshCompleted", "RefreshFailed"]`
      - `progress` (integer) — Refresh progress in percentage (0-100).
      - `externalSource` (string) — JSON-encoded source configuration this job is refreshing from. An object url in an S3 bucket applies.
      - `startTime` (integer) — Unix timestamp at which the refresh job started. · format: `"int64"`
      - `endTime` (integer) — Unix timestamp at which the refresh job ended; `0` when the job is still running. · format: `"int64"`
      - `reason` (string) — Failure reason. Present only when `state` is `RefreshFailed`.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "records": [
      {
        "jobId": 449503829274509300,
        "collectionName": "ext_books",
        "state": "RefreshCompleted",
        "progress": 100,
        "externalSource": "{\"type\":\"s3\",\"path\":\"s3://my-bucket/books/\"}",
        "startTime": 1712832000000,
        "endTime": 1712832600000
      },
      {
        "jobId": 449503829274509300,
        "collectionName": "ext_movies",
        "state": "RefreshInProgress",
        "progress": 42,
        "externalSource": "{\"type\":\"s3\",\"path\":\"s3://my-bucket/movies/\"}",
        "startTime": 1712833000000,
        "endTime": 0
      }
    ]
  }
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
