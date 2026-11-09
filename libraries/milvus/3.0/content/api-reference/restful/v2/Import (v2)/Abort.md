---
title: "Abort Import Job"
---

# Abort Import Job

`POST /v2/vectordb/jobs/import/abort`

Aborts the specified import job.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `jobId` (string) **required** — The ID of the import job to abort.

## Response 200

Returns an empty object.

- **oneOf – success**: Response object that carries `code` alongside either `data` or `message`.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — An empty result object.
- **oneOf – failure**: Response object that carries `code` alongside either `data` or `message`.
  - `code` (integer) **required** — Response code.
  - `message` (string) **required** — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {}
}
```

Example – failure:

```json
{
  "code": 1100,
  "message": "import job abort failed"
}
```
