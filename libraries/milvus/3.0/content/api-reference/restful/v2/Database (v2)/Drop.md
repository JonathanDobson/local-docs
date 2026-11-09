---
title: "Drop Database"
---

# Drop Database

`POST /v2/vectordb/databases/drop`

This operation drops the specified database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) **required** — The name of the new database to be created.

## Response 200

Returns an empty response.

- **oneOf – success**: A successful response payload for the database deletion operation.
  - `code` (integer) — Response code.
  - `data` (object) — An empty response.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

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
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
