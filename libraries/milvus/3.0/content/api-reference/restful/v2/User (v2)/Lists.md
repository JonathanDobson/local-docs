---
title: "List Users"
---

# List Users

`POST /v2/vectordb/users/list`

This operation lists the information of all existing users.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database whose users you want to list.

## Response 200

An object that contains contains the user information.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — Response payload which is a list of usernames.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "root"
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
