---
title: "Describe User"
---

# Describe User

`POST /v2/vectordb/users/describe`

This operation describes the detailed information of a specific user.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `userName` (string) **required** — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

## Response 200

Returns the name of the roles assigned to the specified user.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — Response payload which is a list of roles already assigned to the user.
  - `description` (string) — The description of the user.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "public"
  ],
  "description": "Read-only analyst account."
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
