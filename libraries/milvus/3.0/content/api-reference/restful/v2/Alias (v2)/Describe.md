---
title: "Describe Alias"
---

# Describe Alias

`POST /v2/vectordb/aliases/describe`

This operation describes the details of a specific alias.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to which the alias belongs.
- `aliasName` (string) **required** — The name of the alias whose details are to be listed.

## Response 200

An alias object that contains the detailed description of an alias.

- **anyOf – success**: A response payload returned by the alias describe operation.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which carries the detailed description of an alias.
    - `dbName` (string) — The name of the database to which the collection belongs.
    - `collectionName` (string) — the name of the collection to which an alias belongs.
    - `aliasName` (string) — The name of the alias.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "aliasName": "alice",
    "collectionName": "quick_setup",
    "dbName": "default"
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
