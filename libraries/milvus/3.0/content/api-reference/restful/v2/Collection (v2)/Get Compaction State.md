---
title: "Get Compaction State"
---

# Get Compaction State

`POST /v2/vectordb/collections/get_compaction_state`

This operation gets the state of the latest compaction task for a specified collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `jobID` (integer) — The ID of the compaction job.

## Response 200

Returns the state of the compaction task.

- **oneOf – success**: Response containing the compaction state.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload that carries the compaction state result.
    - `compactionID` (integer) — The ID of the compaction task. · format: `"int64"`
    - `state` (string) — The state of the compaction task.
    - `executingPlanNumber` (number) — The number of executing plans.
    - `timeoutPlanNumber` (number) — The number of timeout plans.
    - `completedPlanNumber` (number) — The number of completed plans.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "compactionID": 470224091360920600,
    "state": "Completed",
    "executingPlanNumber": 0,
    "timeoutPlanNumber": 0,
    "completedPlanNumber": 5
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
