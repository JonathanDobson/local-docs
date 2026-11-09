---
title: "Alter Index Properties"
---

# Alter Index Properties

`POST /v2/vectordb/indexes/alter_properties`

This operation alters the properties of an index.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `indexName` (string) **required** — The name of the target index.
- `properties` (object) **required** — The new index parameters to be set.
  - `mmap.enabled` (boolean) — Whether to enable memory mapping for the current index.
  - `indexoffsetcache.enabled` (boolean) — Whether to cache the index offset in memory.
  - `warmup` (boolean) — Whether to warm up the index.sync: Warm up before a segment is considered loadedasync: Warm up in background after loaddisable: Do not proactively warm up; load on demand · enum: `["sync", "async", "disable"]`

## Response 200

Returns an empty response.

- **oneOf – success**: A response body variant returned for the alter index properties request.
  - `code` (integer) — Response code.
  - `data` (object) — The payload returned after the index properties are altered.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
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
