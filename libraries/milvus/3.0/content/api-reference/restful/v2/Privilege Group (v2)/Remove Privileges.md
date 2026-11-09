---
title: "Remove Privileges from Group"
---

# Remove Privileges from Group

`POST /v2/vectordb/privilege_groups/remove_privileges_from_group`

This operation removes one or more privileges from a privilege group.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `privilegeGroupName` (string) **required** — The name of the privilege group.
- `privileges` (array<string>) **required** — A list of privilege names to remove from the group.

## Response 200

None

- **anyOf – success**: A generic empty response object used when an operation returns no operation-specific payload.
  - `code` (integer) — Response code.
  - `data` (object) — A generic response payload object included in the response.
- **anyOf – failure**: Returns an error message.
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
  "code": 800,
  "message": "not enough permission"
}
```
