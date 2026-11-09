---
title: "Describe Role"
---

# Describe Role

`POST /v2/vectordb/roles/describe`

This operation describes the details of a specified role.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `roleName` (string) **required** — The name of the role.
- `dbName` (string) — Name of the database. If not specified, the default database is used.
- `description` (string) — An optional description string, providing human-readable text for the addressed object.

Example – example:

```json
{
  "roleName": "root"
}
```

## Response 200

An object that contains the detailed desription of a role.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<object>) — Response payload which is a list of privilege items.
    - `object_type` (string) — The type of the object to which the privilege belongs.
    - `privilege` (string) — The privilege that is granted to the role.
    - `object_name` (string) — The name of the object to which the role is granted the specified privilege.
    - `db_name` (string) — The name of the database in which this operation has been executed.
    - `grantor` (string) — The name of the user who granted a specific role to a user.
  - `description` (string) — The description of the role.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "db_name": "*",
      "grantor": "root",
      "object_name": "*",
      "object_type": "Global",
      "privilege": "ShowCollections"
    },
    {
      "db_name": "*",
      "grantor": "root",
      "object_name": "*",
      "object_type": "Global",
      "privilege": "ShowCollections"
    },
    {
      "db_name": "*",
      "grantor": "root",
      "object_name": "*",
      "object_type": "Global",
      "privilege": "ShowCollections"
    }
  ],
  "description": "Grants read-only access to analytics collections."
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
