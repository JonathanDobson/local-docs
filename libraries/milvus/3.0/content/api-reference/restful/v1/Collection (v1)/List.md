---
title: "List Collections"
---

# List Collections

`GET /v1/vector/collections`

**Deprecated.**

Lists collections in a cluster.

## Parameters

- `dbName` (in query) — The name of the database · example: `default`
- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Response 200

Returns a list of collections in the specified cluster.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code.
  - `data` (array<string>) — Response payload which is a list of collection names.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": [
    "custom_setup_not_indexed",
    "quick_setup",
    "custom_setup_indexed"
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
