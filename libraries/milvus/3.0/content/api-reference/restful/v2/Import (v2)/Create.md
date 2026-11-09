---
title: "Create Import Jobs"
---

# Create Import Jobs

`POST /v2/vectordb/jobs/import/create`

This operation imports the prepared data files to a Milvus instance. To learn how to prepare your data files, read [Prepare Data Import](https://milvus.io/docs/prepare-source-data.md).

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- **oneOf – Object storage files**: One supported form of the import job creation request. Every form must specify the target `collectionName`.
  - `dbName` (string) — The name of the database that to which the collection belongs . Setting this to a non-existing database results in an error.
  - `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
  - `partitionName` (string) — The name of the target partition. Setting this to a non-existing partition results in an error.
  - `files` (array<array>) **required** — The files that contain the data to import. The files should reside within the Milvus bucket on the MinIO instance deployed along with your Milvus instance.
  - `options` (object) — Bulk-import options.
    - `timeout` (string) — The timeout duration of the created import jobs. The value should be a positive number suffixed by __s__ (seconds), __m__ (minutes), and __h__(hours). For example, _300s_, _1.5h_, and _1h45_ are all valid values.

Example – use external storage:

```json
{
  "files": [
    [
      "/d1782fa1-6b65-4ff3-b05a-43a436342445/1.json"
    ],
    [
      "/2a12dea7-2eff-4b34-97b6-9554063fd791/1/id.npy",
      "/2a12dea7-2eff-4b34-97b6-9554063fd791/1/vector.npy",
      "/2a12dea7-2eff-4b34-97b6-9554063fd791/1/$meta.npy"
    ],
    [
      "/a6fb2d1c-7b1b-427c-a8a3-178944e3b66d/1.parquet"
    ]
  ],
  "collectionName": "quick_setup"
}
```

## Response 200

The ID of the bulk-import job.

- **anyOf – success**: The successful response body returned when an import job is created.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<object>) — Response payload which carries the IDs of the created bulk-import jobs.
    - `jobId` (string) — The ID of the current bulk-import job.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "jobId": "job-xxxxxxxxxxxxxxxxxxxxx"
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
