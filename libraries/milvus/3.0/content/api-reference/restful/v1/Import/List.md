---
title: "List Import Jobs"
---

# List Import Jobs

`GET /v1/vector/collections/import/list`

**Deprecated.**

List all import jobs specific to a cluster.

## Parameters

- `pageSize` (in query) — The number of records to return at each request. · example: `10`
- `currentPage` (in query) — The current page number. · example: `1`
- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Response 200

Returns a list of import jobs.

- **oneOf – success**: A single response payload returned by the import list query.
  - `code` (string) — Response code.
  - `data` (object) — Response payload which is a list containing import jobs in detail.
    - `count` (string) — Total number of records listed in this response.
    - `currentPage` (string) — The current page number for your reference.
    - `pageSize` (string) — The maximum number of records to be included in each return.
    - `tasks` (array<object>) — A list of import jobs in detail.
      - `collectionName` (string) — The target collection name of a import task.
      - `jobId` (string) — The ID of an import task.
      - `state` (string) — The corresponding status of the import task. Possible values are ImportRunning, ImportCompleted and ImportFailed.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "tasks": [
      {
        "collectionName": "medium_articles",
        "jobId": "job-xxxxxxxxxxxxxxxxxxxxxx",
        "state": "ImportRunning"
      },
      {
        "collectionName": "medium_articles",
        "jobId": "2b93fef7-xxxx-xxxx-xxxx-f82afd598ff1",
        "state": "ImportCompleted"
      }
    ],
    "count": 2,
    "currentPage": 1,
    "pageSize": 10
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
