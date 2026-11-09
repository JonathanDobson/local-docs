---
title: "Alter Database Properties (Compatibility Alias)"
---

# Alter Database Properties (Compatibility Alias)

`POST /v2/vectordb/databases/alter_properties`

This compatibility alias alters the properties of a database. It uses the same server handler as `/v2/vectordb/databases/alter`.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) **required** — The name of the database to alter.
- `properties` (object) — The properties to set on the database as key-value pairs.

## Response 200

None

- **anyOf – success**: An empty response body returned when an operation completes without additional data.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object returned by the operation.
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
