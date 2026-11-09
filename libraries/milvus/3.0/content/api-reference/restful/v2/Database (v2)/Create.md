---
title: "Create Database"
---

# Create Database

`POST /v2/vectordb/databases/create`

This operation creates a new database in the specified cluster.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) **required** — The name of the new database to be created.
- `properties` (object) — The properties of the new database in key-value pairs.
  - `database.replica.number` (integer) — The number of replicas for the new database.
  - `database.resource_groups` (string) — The names of the resource groups associated with the new database in a common-separated list.
  - `database.diskQuota.mb` (integer) — The maximum size of the disk space for the new database, in megabytes (MB).
  - `database.max.collections` (integer) — The maximum number of collections allowed in the new database.
  - `database.force.deny.writing` (boolean) — Whether to force the new database to deny writing operations.
  - `database.force.deny.reading` (boolean) — Whether to force the new database to deny reading operations.
  - `database.force.deny.ddl` (boolean) — Whether to force the new database to deny all DDL operations.
  - `database.force.deny.collectionDDL` (boolean) — Whether to force the new database to deny collection DDL operations.
  - `database.force.deny.partitionDDL` (boolean) — Whether to force the new database to deny partition DDL operations.
  - `database.force.deny.index` (boolean) — Whether to force the new database to deny index DDL operations.
  - `database.force.deny.flush` (boolean) — Whether to force the new database to deny flush DDL operations.
  - `database.force.deny.compaction` (boolean) — Whether to force the new database to deny compaction DDL operations.
  - `timezone` (string) — The IANA Time Zone ID for the new database.
  - `cipher.enabled` (string) — Whether to enable CMEK encryption for the new database. Set to "true" or "false".
  - `cipher.key` (string) — The CMEK encryption root key for the new database.

## Response 200

Returns an empty object.

- **oneOf – success**: A response body returned by a successful database creation request.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is an empty object.
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
