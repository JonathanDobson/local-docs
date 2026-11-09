---
title: "List Import Jobs"
---

# List Import Jobs

`POST /v2/vectordb/jobs/import/list`

This operation lists all import jobs of a specific cluster.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`
- `Accept` (in header) — Use `application/json`. · example: `application/json`

## Request body (application/json)

- **oneOf – Milvus**: The request body for listing import jobs; `clusterId` is required when the request targets a cluster.
  - `dbName` (string) — Name of the database to which the import job belongs.
  - `collectionName` (string) — The name of the Collection to which the import job listing request applies.

## Response 200

Returns a list of import jobs

- **anyOf – success**: The successful response body for the import job listing request.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload, which is a list of import jobs in detail.
    - *oneOf – Milvus*: The import job listing data returned in the response.
      - `records` (array<object>) — The import job records returned by the listing request.
        - `collectionName` (string) — Name of the target collection of this import job.
        - `jobId` (string) — ID of this import job.
        - `state` (string) — State of this import job. · enum: `["Pending", "InProgress", "Completed", "Failed"]`
        - `progress` (number) — Progress of this import job.
        - `reason` (string) — Reason for the failure of this import job.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "count": 1,
    "currentPage": 1,
    "pageSize": 10,
    "records": [
      {
        "collectionName": "test_collection",
        "jobId": "job-xxxxxxxxxxxxxxxxxxxxx",
        "state": "Completed"
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
