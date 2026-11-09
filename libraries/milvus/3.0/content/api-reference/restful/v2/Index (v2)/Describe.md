---
title: "Describe Index"
---

# Describe Index

`POST /v2/vectordb/indexes/describe`

This operation describes the current index.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to which the collection belongs.
- `collectionName` (string) **required** — The name of the collection to which the index belongs.
- `indexName` (string) **required** — The name of the index to describe.
- `timestamp` (integer) — An integer timestamp associated with the index description request.

## Response 200

An array that contains the detailed descriptions of the current indexes.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<object>) — Response payload containing the detailed descriptions of the indexes.
    - `indexName` (string) — The name of the index.
    - `fieldName` (string) — The name of the target field.
    - `indexType` (string) — The type of this index.
    - `metricType` (string) — The type of the similarity metric.
    - `mmap.enabled` (string) — Whether memory mapping is enabled for this index.
    - `indexoffsetcache.enabled` (string) — Whether to cache the index offset in memory.
    - `warmup` (string) — Whether to load the index into memory when the index is created or updated.sync: Warm up before a segment is considered loadedasync: Warm up in background after loaddisable: Do not proactively warm up; load on demand · enum: `["", "sync", "async", "disable"]`
    - `totalRows` (integer) — The total number of entities/rows.
    - `pendingRows` (integer) — The number of entities/rows that are waiting to be indexed.
    - `indexedRows` (integer) — The total number of entities/rows that have been indexed.
    - `indexState` (string) — The status of the indexing progress.
    - `failReason` (string) — The reason for the failure to build indexes.
    - `minIndexVersion` (integer) — The minimum version of the index. · format: `"int32"`
    - `maxIndexVersion` (integer) — The maximum version of the index. · format: `"int32"`
    - `indexParams` (array<object>) — The index parameters used to build the index in a list of key-value pairs.
      - `key` (string) — The name of the index parameter.
      - `value` (string) — The value of the index parameter.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "indexName": "embedding_idx",
      "fieldName": "embedding",
      "indexType": "IVF_FLAT",
      "metricType": "COSINE",
      "mmap.enabled": "false",
      "indexoffsetcache.enabled": "false",
      "warmup": "sync",
      "totalRows": 10000,
      "pendingRows": 0,
      "indexedRows": 10000,
      "indexState": "Finished",
      "failReason": "",
      "minIndexVersion": 0,
      "maxIndexVersion": 0,
      "indexParams": [
        {
          "key": "index_type",
          "value": "IVF_FLAT"
        },
        {
          "key": "metric_type",
          "value": "L2"
        },
        {
          "key": "params",
          "value": "{\"nlist\":128}"
        }
      ]
    }
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
