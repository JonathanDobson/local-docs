---
title: "Describe External Collection Refresh Job"
---

# Describe External Collection Refresh Job

`POST /v2/vectordb/jobs/external_collection/describe`

This operation returns the current state and progress of a single external-collection refresh job, identified by `jobId`.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `jobId` (integer) **required** — ID of the refresh job to describe. Obtain this value from the response of the refresh endpoint. · format: `"int64"`

## Response 200

Returns the state and progress of the specified refresh job.

- **anyOf – success**: One of the alternative response bodies that may be returned when describing an external Collection refresh job; only one variant is present in a given response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload describing the refresh job.
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
    "jobId": 449503829274509300,
    "collectionName": "ext_books",
    "state": "RefreshInProgress",
    "progress": 42,
    "externalSource": "{\"type\":\"s3\",\"path\":\"s3://my-bucket/books/\"}",
    "startTime": 1712832000000,
    "endTime": 0
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
