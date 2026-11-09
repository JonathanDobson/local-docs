---
title: "List Collections"
---

# List Collections

`POST /v2/vectordb/collections/list`

This operation lists all collection names for the current connection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges or a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`
- `Authorization` (in header) **required** — The authentication token should be an API key with appropriate privileges. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.

## Response 200

This operation lists all collections in the database used in the current connection.

- **oneOf – success**: The response body containing the Collections returned by the list operation.
  - `code` (integer) — Response code.
  - `data` (array<string>) — Response payload which is a list of collection names.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "quick_setup_new",
    "customized_setup_1",
    "customized_setup_2"
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
