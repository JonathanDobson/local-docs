---
title: "Import"
---

# Import

`POST /v1/vector/collections/import`

**Deprecated.**

Imports data from files stored in a specified object storage bucket.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `clusterId` (string) **required** — The ID of a cluster to which this operation applies.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `partitionName` (string) — The name of the partition to which this operation applies.
- `objectUrl` (string) **required** — The URL of the object that stores the data to be imported.
- `accessKey` (string) — The access key used to access the specified object.
- `secretKey` (string) — The secret access key used to access the specified object.

Example – request:

```json
{
  "clusterId": "inxx-xxxxxxxxxxxxxxx",
  "collectionName": "medium_articles",
  "objectUrl": "gs://docs-demo/1af78216-xxxx-2b0a73c566ed/1.parquet",
  "accessKey": "xxxxxx",
  "secretKey": "xxxxxx"
}
```

## Response 200

Returns a import task job ID.

- **oneOf – success**: A single response payload returned by the import operation.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload, which is an object containing the import job ID.
    - `jobId` (string) **required** — The ID of the import job that has been submitted.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "jobId": "job-xxxxxxxxxxxxxxxxxxxxxx"
  }
}
```

Example – failure:

```json
{
  "code": 80002,
  "message": "Token not found or unauthorized: The provided token does not exist in our records, or you do not have the necessary permissions to use this token. Please ensure you have the correct token."
}
```
