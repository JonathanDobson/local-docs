---
title: "Upsert"
---

# Upsert

`POST /v2/vectordb/entities/upsert`

This operation inserts new records into the database or updates existing ones.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection in which to upsert data.
- `partitionName` (string) — The name of a partition in the current collection. If specified, the data is to be inserted into the specified partition.
- `data` (object) **required** — An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema
- `partialUpdate` (boolean) — Whether to enable partial updates. When enabled, only the specified fields are updated. Use fieldOps to select replacement or array-specific update behavior for individual fields.
- `fieldOps` (array<object>) — Field-level operations to apply during a partial update. Each entry selects a field and specifies how its value is updated.
  - `fieldName` (string) **required** — The name of the field to update.
  - `op` (string) **required** — The update operation. REPLACE replaces the field value, ARRAY_APPEND appends array elements, and ARRAY_REMOVE removes matching array elements. · enum: `["REPLACE", "ARRAY_APPEND", "ARRAY_REMOVE"]`

Example – Upsert entities:

```json
{
  "data": [
    {
      "id": 0,
      "vector": [
        0.3580376395471989,
        -0.6023495712049978,
        0.18414012509913835,
        -0.26286205330961354,
        0.9029438446296592
      ],
      "color": "pink_8682"
    },
    {
      "id": 1,
      "vector": [
        0.19886812562848388,
        0.06023560599112088,
        0.6976963061752597,
        0.2614474506242501,
        0.838729485096104
      ],
      "color": "red_7025"
    },
    {
      "id": 2,
      "vector": [
        0.43742130801983836,
        -0.5597502546264526,
        0.6457887650909682,
        0.7894058910881185,
        0.20785793220625592
      ],
      "color": "orange_6781"
    },
    {
      "id": 3,
      "vector": [
        0.3172005263489739,
        0.9719044792798428,
        -0.36981146090600725,
        -0.4860894583077995,
        0.95791889146345
      ],
      "color": "pink_9298"
    },
    {
      "id": 4,
      "vector": [
        0.4452349528804562,
        -0.8757026943054742,
        0.8220779437047674,
        0.46406290649483184,
        0.30337481143159106
      ],
      "color": "red_4794"
    },
    {
      "id": 5,
      "vector": [
        0.985825131989184,
        -0.8144651566660419,
        0.6299267002202009,
        0.1206906911183383,
        -0.1446277761879955
      ],
      "color": "yellow_4222"
    },
    {
      "id": 6,
      "vector": [
        0.8371977790571115,
        -0.015764369584852833,
        -0.31062937026679327,
        -0.562666951622192,
        -0.8984947637863987
      ],
      "color": "red_9392"
    },
    {
      "id": 7,
      "vector": [
        -0.33445148015177995,
        -0.2567135004164067,
        0.8987539745369246,
        0.9402995886420709,
        0.5378064918413052
      ],
      "color": "grey_8510"
    },
    {
      "id": 8,
      "vector": [
        0.39524717779832685,
        0.4000257286739164,
        -0.5890507376891594,
        -0.8650502298996872,
        -0.6140360785406336
      ],
      "color": "white_9381"
    },
    {
      "id": 9,
      "vector": [
        0.5718280481994695,
        0.24070317428066512,
        -0.3737913482606834,
        -0.06726932177492717,
        -0.6980531615588608
      ],
      "color": "purple_4976"
    }
  ],
  "collectionName": "quick_setup"
}
```

Example – Partial update with ARRAY_APPEND:

```json
{
  "collectionName": "product_catalog",
  "data": [
    {
      "id": 1,
      "tags": [
        "featured"
      ]
    }
  ],
  "partialUpdate": true,
  "fieldOps": [
    {
      "fieldName": "tags",
      "op": "ARRAY_APPEND"
    }
  ]
}
```

## Response 200

A MutationResult object.

- **anyOf – success**: A response payload variant returned by the upsert operation.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (object) — Response payload which carries the result of the upsert operation.
    - `upsertCount` (integer) — The number of upserted entities. · example: `4`
    - `upsertIds` (array<object>) — An array of the IDs of upserted entities. Note: IDs are returned as strings unless the request includes the header `Accept-Type-Allow-Int64: true`.
      - **oneOf – option 1**
      - **oneOf – option 2**
  - `scanned_remote_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `scanned_total_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `cache_hit_ratio` (number) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "upsertCount": 10,
    "upsertIds": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
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
