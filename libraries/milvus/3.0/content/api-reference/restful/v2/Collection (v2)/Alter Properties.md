---
title: "Alter Collection Properties"
---

# Alter Collection Properties

`POST /v2/vectordb/collections/alter_properties`

This operation alters the properties of a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `properties` (object) **required** — The properties of the collection to alter.
  - `collection.ttl.seconds` (integer) — The time-to-live (TTL) period of the collection in seconds.
  - `collection.autocompaction.enabled` (boolean) — Whether to enable automatic compaction for the collection.
  - `collection.description` (string) — The description of the collection.
  - `collection.on.truncating` (boolean) — Whether the collection is currently truncating. When true, compaction is forbidden.
  - `collection.function.allowInsertNonBM25FunctionOutputs` (boolean) — Whether to allow inserting non-BM25 function outputs.
  - `collection.insertRate.max.mb` (number) — The maximum insert rate limit in MB/s.
  - `collection.insertRate.min.mb` (number) — The minimum insert rate limit in MB/s.
  - `collection.deleteRate.max.mb` (number) — The maximum delete rate limit in MB/s.
  - `collection.deleteRate.min.mb` (number) — The minimum delete rate limit in MB/s.
  - `collection.bulkLoadRate.max.mb` (number) — The maximum bulk load rate limit in MB/s.
  - `collection.bulkLoadRate.min.mb` (number) — The minimum bulk load rate limit in MB/s.
  - `collection.queryRate.max.qps` (number) — The maximum query rate limit in QPS.
  - `collection.queryRate.min.qps` (number) — The minimum query rate limit in QPS.
  - `collection.searchRate.max.vps` (number) — The maximum search rate limit in VPS.
  - `collection.searchRate.min.vps` (number) — The minimum search rate limit in VPS.
  - `collection.diskProtection.diskQuota.mb` (number) — The maximum disk quota for the collection in MB.
  - `collection.replica.number` (integer) — The number of replicas for the collection.
  - `collection.resource_groups` (string) — A comma-separated list of resource group names associated with the collection.
  - `mmap.enabled` (boolean) — Whether to enable memory mapping for the collection.
  - `partitionkey.isolation` (boolean) — Whether to enable partition key isolation for the collection.
  - `ttl_field` (string) — The name of the field to use for TTL-based expiration.
  - `warmup.scalarField` (boolean) — Whether to preload scalar field data into memory on load.
  - `warmup.scalarIndex` (boolean) — Whether to preload scalar index data into memory on load.
  - `warmup.vectorField` (boolean) — Whether to preload vector field data into memory on load.
  - `warmup.vectorIndex` (boolean) — Whether to preload vector index data into memory on load.

## Response 200

Returns an empty object.

- **oneOf – success**: A generic response envelope returned by operations that carry no operation-specific result data. It still includes a `data` object.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object. Its contents depend on the operation that returns it.
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
