---
title: "Get Import Progress"
---

# Get Import Progress

`GET /v1/vector/collections/import/get`

**Deprecated.**

Retrieves the progress of a specified import task.

## Parameters

- `jobId` (in query) **required** — The ID of the import task in concern · example: `job-xxxxxxxxxxxxxxxxxx`
- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Response 200

Returns the progress of the specified job ID in percentage.

- **oneOf – success**: A single response payload returned by the import status query.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is an object containing the progress of the import task.
    - `fileName` (string) — The path of the data file object in the object storage.
    - `fileSize` (integer) — The size of the data file object. · format: `"int64"`
    - `readyPercentage` (number) — The indicator of the import progress · format: `"float"`
    - `completeTime` (string) — The time at which the import task completes. `null` indicates that the file import is going on.
    - `errorMessage` (string) — The message that explains the reason for an import failure. `null` indicates that no error occurs.
    - `collectionName` (string) — The target collection name of the import task.
    - `jobId` (string) — The ID of an import task.
    - `details` (array<object>) — The import task details
      - `fileName` (string) — The path to a file being imported.
      - `fileSize` (integer) — The size of a file being imported. · format: `"int64"`
      - `readyPercentage` (number) — The import progress of a specific file. · format: `"float"`
      - `completeTime` (string) — The time at which the import progress ends for a specific file. `null` indicates that the file import is going on.
      - `errorMessage` (string) — The message that explains the reason for an import failure. `null` indicates that no error occurs.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "collectionName": "medium_articles",
    "fileName": "1af78216-xxxx-xxxx-xxxx-2b0a73c566ed/1.parquet",
    "fileSize": 19599887,
    "readyPercentage": 0,
    "completeTime": null,
    "errorMessage": null,
    "jobId": "job-xxxxxxxxxxxxxxxxxxxxxx",
    "details": [
      {
        "fileName": "1af78216-xxxx-xxxx-xxxx-2b0a73c566ed/1.parquet",
        "fileSize": 19599887,
        "readyPercentage": 0,
        "completeTime": null,
        "errorMessage": null
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
