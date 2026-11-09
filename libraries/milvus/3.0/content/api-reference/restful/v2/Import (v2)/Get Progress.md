---
title: "Get Import Job Progress"
---

# Get Import Job Progress

`POST /v2/vectordb/jobs/import/describe`

This operation gets the progress of the specified bulk-import job.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- **oneOf – Job ID**: The request requires `jobId`; it may be combined with `clusterId`, combined with both `projectId` and `regionId`, or supplied alone.
  - `jobId` (string) **required** — The ID of the bulk-import job of your interest. The [Create Import Jobs](/reference/restful/create-import-jobs-v2) operation usually returns a job ID. You can also call [List Import Jobs](/reference/restful/list-import-jobs-v2) to get the IDs of all bulk-import jobs related to the specific cluster.

Example – by job ID (open-source Milvus):

```json
{
  "jobId": "job-xxxxxxxxxxxxxxxx"
}
```

## Response 200

成功

- **anyOf – success**: Response object containing the description of the import job.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which contains the progress of the specified bulk-import job in detail.
    - `collectionName` (string) — The name of the target collection of this bulk-import job.
    - `completeTime` (string) — The timestamp indicating when the bulk-import job is complete.
    - `details` (array<object>) — Statistics on data import oriented to data files.
      - `completeTime` (string) — The timestamp at which the file is processed.
      - `fileName` (string) — The name of a data file.
      - `fileSize` (string) — The size of the data file.
      - `progress` (string) — The progress in percentage.
      - `state` (string) — The processing state of the data file. · enum: `["Pending", "Importing", "Completed", "Failed"]`
      - `reason` (string) — The reason for the failure to bulk import data. This field stays empty if this job succeeds.
      - `importedRows` (string) — The number of rows imported from this file.
      - `totalRows` (string) — The number of rows in the specified collection upon the import from this file is complete.
    - `fileSize` (integer) — The uploaded file size in bytes.
    - `jobId` (integer) — The ID of this bulk-import job.
    - `createTime` (string) — The timestamp indicating when the bulk-import job was created.
    - `progress` (integer) — The progress in percentage of the current bulk-import job.
    - `state` (string) — The state of this bulk-import job. · enum: `["Pending", "Importing", "Completed", "Failed"]`
    - `reason` (string) — The reason for the failure to bulk import data. The field value stays empty if this job succeeds.
    - `importedRows` (integer) — The number of rows inserted into the specified collection upon this import.
    - `totalRows` (integer) — The number of rows in the specified collection.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "jobId": "448761313698322011",
    "collectionName": "medium_articles",
    "fileName": "medium_articles_2020_dpr.json",
    "fileSize": 3279917,
    "state": "Completed",
    "progress": 100,
    "completeTime": "2024-04-01T06:17:55Z",
    "reason": "",
    "totalRows": 100000,
    "details": [
      {
        "fileName": "medium_articles_2020_dpr.json",
        "fileSize": 3279917,
        "state": "Completed",
        "progress": 100,
        "completeTime": "2024-04-01T06:17:53Z",
        "reason": ""
      }
    ]
  }
}
```

Example – failure:

```json
{
  "code": 21119,
  "message": "The apikey is illegal."
}
```
