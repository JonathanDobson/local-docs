---
title: "List Aliases"
---

# List Aliases

`POST /v2/vectordb/aliases/list`

This operation lists all existing collection aliases in the specified database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of an existing database. · default: `"default"`
- `collectionName` (string) — The name of an existing collection. If specified, only returns aliases of the specified collection. If not specified, returns aliases of all collections in the database. · default: `"default"`

## Response 200

A list of collection aliases.

- **anyOf – success**: A response payload returned by the alias list operation.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — Response payload which is a list of item objects.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "bob"
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
