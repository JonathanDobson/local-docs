---
title: "List Privilege Groups"
---

# List Privilege Groups

`POST /v2/vectordb/privilege_groups/list`

This operation lists all privilege groups in the current database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.

## Response 200

None

- **anyOf – success**: One possible response shape returned on success, carrying the `code` and `data` fields.
  - `code` (integer) — The response code indicating whether the request succeeded.
  - `data` (object) — The response payload, which holds the privilege groups returned by the request.
    - `privilegeGroups` (array<object>) — The privilege groups returned by the request.
      - `privilegeGroupName` (string) — The name of the privilege group.
      - `privileges` (string) — The privileges included in the privilege group, joined by commas.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "privilegeGroups": [
      {
        "privilegeGroupName": "my_priv_group",
        "privileges": "Insert,Search"
      }
    ]
  }
}
```

Example – failure:

```json
{
  "code": 800,
  "message": "not enough permission"
}
```
