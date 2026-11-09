---
title: "Alter Database Properties"
---

# Alter Database Properties

`POST /v2/vectordb/databases/alter`

This operation alters the properties of the specified database.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) **required** — The name of the new database to be created.
- `properties` (object) **required** — The properties to be modified in key-value pairs.
  - `database.replica.number` (integer) — The number of replicas for the specified database.
  - `database.resource_groups` (string) — The names of the resource groups associated with the specified database in a common-separated list.
  - `database.diskQuota.mb` (integer) — The maximum size of the disk space for the specified database, in megabytes (MB).
  - `database.max.collections` (integer) — The maximum number of collections allowed in the specified database.
  - `database.force.deny.writing` (boolean) — Whether to force the specified database to deny writing operations.
  - `database.force.deny.reading` (boolean) — Whether to force the specified database to deny reading operations.
  - `database.force.deny.ddl` (boolean) — Whether to force the specified database to deny all DDL operations.
  - `database.force.deny.collectionDDL` (boolean) — Whether to force the specified database to deny collection DDL operations.
  - `database.force.deny.partitionDDL` (boolean) — Whether to force the specified database to deny partition DDL operations.
  - `database.force.deny.index` (boolean) — Whether to force the specified database to deny index DDL operations.
  - `database.force.deny.flush` (boolean) — Whether to force the specified database to deny flush DDL operations.
  - `database.force.deny.compaction` (boolean) — Whether to force the specified database to deny compaction DDL operations.
  - `timezone` (string) — The IANA Time Zone ID for the specified database.
  - `cipher.enabled` (string) — Whether to enable CMEK encryption for the specified database. Set to "true" or "false".
  - `cipher.key` (string) — The CMEK encryption root key for the specified database.

## Response 200

Returns an empty response.

- **oneOf – success**: A successful response payload for the database property alteration operation.
  - `code` (integer) — Response code.
  - `data` (object) — An empty response.
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
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
