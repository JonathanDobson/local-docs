---
title: "Describe Database"
---

# Describe Database

`POST /v2/vectordb/databases/describe`

This operation describes the specified database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) **required** — The name of the new database to be created.

## Response 200

Returns the properties of the specified database.

- **oneOf – success**: A response body returned by a successful database describe request.
  - `code` (integer) — Response code.
  - `data` (object) — The details of the specified database.
    - `dbName` (string) — The name of the database.
    - `dbID` (integer) — The ID of the database.
    - `properties` (array<object>) — The properties of the specified database in key-value pairs.
      - `key` (string) — The property name. · enum: `["database.replica.number", "database.resource_groups", "database.diskQuota.mb", "database.max.collections", "database.force.deny.writing", "database.force.deny.reading", "database.force.deny.ddl", "database.force.deny.collectionDDL", "database.force.deny.partitionDDL", "database.force.deny.index", "database.force.deny.flush", "database.force.deny.compaction", "timezone", "cipher.enabled", "cipher.key"]`
      - `value` (string) — The property value.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
  "data": {
    "dbName": "my_database",
    "dbID": 123,
    "properties": [
      {
        "key": "database.replica.number",
        "value": "1"
      }
    ]
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
