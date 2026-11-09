---
title: "Refresh External Collection"
---

# Refresh External Collection

`POST /v2/vectordb/jobs/external_collection/refresh`

This operation triggers an asynchronous data refresh job for an existing external collection, re-syncing the collection's data from its underlying external source. `externalSource` and `externalSpec` must be both provided or both omitted; when both are omitted, the collection's previously persisted source and spec are reused.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to refresh.
- `externalSource` (string) — JSON-encoded specification of the external data source. When provided, `externalSpec` must also be provided. When omitted, the collection's persisted source is reused. An object url in an S3 bucket applies.This parameters applies only to Iceberg tables.
- `externalSpec` (string) — JSON-encoded specification describing how the external data maps to the collection. When provided, `externalSource` must also be provided. When omitted, the collection's persisted spec is reused.This parameters applies only to Iceberg tables.

Example – Refresh from an S3 source:

```json
{
  "dbName": "default",
  "collectionName": "ext_books"
}
```

## Response 200

Returns the ID of the newly created refresh job.

- **anyOf – success**: One of the alternative response bodies that may be returned for the refresh request; only one variant is present in a given response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload carrying the new refresh job's identifier.
    - `jobId` (integer) — ID of the newly created refresh job. Use this value to query progress via the describe endpoint. · format: `"int64"`
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "jobId": 449503829274509300
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
