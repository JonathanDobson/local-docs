---
title: "List Databases"
---

# List Databases

`POST /v2/vectordb/databases/list`

This operation lists all databases in the current Milvus instance.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)


## Response 200

Returns a list of database names.

- **oneOf – success**: A response body returned by a successful database list request.
  - `code` (integer) — Response code.
  - `data` (array<string>) — A list of database names.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "default",
    "test"
  ]
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
