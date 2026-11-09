---
title: "Describe Collection"
---

# Describe Collection

`GET /v1/vector/collections/describe`

**Deprecated.**

Describes the details of a collection.

## Parameters

- `collectionName` (in query) **required** — The name of the collection to describe.
- `dbName` (in query) — The name of the database. · example: `default`
- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Response 200

Returns the specified collection in detail.

- **anyOf – success**: An object describing a Collection returned by the describe operation.
  - `code` (integer) — response code.
  - `data` (object) — Response payload which carries the collection details.
    - `collectionName` (string) — The name of the collection.
    - `description` (string) — An optional description of the collection.
    - `fields` (array<object>) — An field array
      - `autoId` (boolean) — Whether the primary key automatically increments. This field applies only when the current field is the primary key.
      - `description` (string) — An optional description of the field.
      - `name` (string) — The name of the field.
      - `primaryKey` (boolean) — Whether the field is a primary field.
      - `type` (string) — The data type of the values in this field.
    - `indexes` (array<object>) — An index array
      - `fieldName` (string) — The name of the indexed field.
      - `indexName` (string) — The name of the generated index files.
      - `metricType` (string) — The metric type used to measure similarity between vectors
    - `load` (string) — The load status of the collection. · enum: `["unload", "loading", "loaded"]`
    - `shardsNum` (integer) — The number of shards in the collection.
    - `enableDynamicField` (boolean) — Whether the dynamic field feature is enabled for this collection.
- **anyOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "aliases": [],
    "autoId": false,
    "collectionID": 448707763883002000,
    "collectionName": "test_collection",
    "consistencyLevel": "Bounded",
    "description": "",
    "enableDynamicField": true,
    "fields": [
      {
        "autoId": false,
        "description": "",
        "id": 100,
        "name": "id",
        "partitionKey": false,
        "primaryKey": true,
        "type": "Int64"
      },
      {
        "autoId": false,
        "description": "",
        "id": 101,
        "name": "vector",
        "params": [
          {
            "key": "dim",
            "value": "5"
          }
        ],
        "partitionKey": false,
        "primaryKey": false,
        "type": "FloatVector"
      }
    ],
    "indexes": [
      {
        "fieldName": "vector",
        "indexName": "vector",
        "metricType": "COSINE"
      }
    ],
    "load": "LoadStateLoaded",
    "partitionsNum": 1,
    "properties": [],
    "shardsNum": 1
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
