---
title: "Commit Import Job"
---

# Commit Import Job

`POST /v2/vectordb/jobs/import/commit`

Commits the specified import job so its imported data can become visible.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `jobId` (string) **required** — The ID of the import job to commit.

## Response 200

Returns an empty object.

- **oneOf – success**: A response payload for the import job commit operation; it includes `code` together with `data` or `message`.
  - `code` (integer) **required** — Response code.
  - `data` (object) **required** — An empty result object.
- **oneOf – failure**: A response payload for the import job commit operation; it includes `code` together with `data` or `message`.
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
  "message": "import job commit failed"
}
```
