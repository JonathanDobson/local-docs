---
title: "List Resource Groups"
---

# List Resource Groups

`POST /v2/vectordb/resource_groups/list`

This operation returns the list of resource group names.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)


## Response 200

Returns the list of resource group names.

- **oneOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — The list of resource group names.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "__default_resource_group",
    "group1"
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
