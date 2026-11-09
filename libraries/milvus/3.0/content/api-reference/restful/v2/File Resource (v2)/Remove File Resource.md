---
title: "Remove File Resource"
---

# Remove File Resource

`POST /v2/vectordb/file_resources/remove`

Removes a file resource registered with Milvus.

## Parameters

- `Authorization` (in header) — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `name` (string) **required** — The unique name of the file resource to remove.

## Response 200

Returns an empty object.

- **oneOf – success**: A successful empty response.
  - `code` (integer) — Response code.
  - `data` (object) — An empty result object.
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
  "code": 1100,
  "message": "file resource not found"
}
```
