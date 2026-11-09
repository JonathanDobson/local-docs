---
title: "Create Collection"
---

# Create Collection

`POST /v2/vectordb/collections/create`

This operation creates a collection in a specified cluster.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- **oneOf – quick setup**: Defines a Collection to be created with a quick setup. `collectionName` and `dimension` are required.
  - `dbName` (string) — The name of the database.
  - `collectionName` (string) **required** — The name of the collection to create.
  - `dimension` (integer) **required** — The number of dimensions a vector value should have. This is required if **idType** of this field is set to **FloatVector** or **BinaryVector**.
  - `metricType` (string) — The metric type applied to this operation. · default: `"COSINE"` · enum: `["L2", "IP", "COSINE", "JACCARD", "HAMMING"]`
  - `idType` (string) — The data type of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined. · enum: `["VarChar", "Int64"]`
  - `autoID` (boolean) — Whether the primary field automatically increments. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined. · default: `false`
  - `primaryFieldName` (string) — The name of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
  - `vectorFieldName` (string) — The name of the vector field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
  - `description` (string) — The description of the current collection.
  - `params` (object) — Extra parameters for the collection.
    - `max_length` (integer) — The maximum number of bytes allowed in the primary field. This parameter is available only when the primary field is a string field.
    - `enableDynamicField` (boolean) — Whether to enable the dynamic field feature. · default: `true`
    - `shardsNum` (integer) — The number of shards to create along with the current collection.
    - `consistencyLevel` (string) — The consistency level of the collection. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
    - `ttlSeconds` (integer) — The time-to-live (TTL) period of the collection. If set, the collection is to be dropped once the period ends.
    - `mmap.enabled` (boolean) — Specifies whether to enable memory mapping for the collection.
    - `ttlField` (string) — The name of the field to use for TTL-based expiration.
    - `warmup.scalarField` (boolean) — Whether to preload scalar field data into memory on load.
    - `warmup.scalarIndex` (boolean) — Whether to preload scalar index data into memory on load.
    - `warmup.vectorField` (boolean) — Whether to preload vector field data into memory on load.
    - `warmup.vectorIndex` (boolean) — Whether to preload vector index data into memory on load.
  - `consistencyLevel` (string) — The consistency level applied to the collection described by this setup. It determines the consistency guarantee used when the collection is queried. · enum: `["Strong", "Eventually", "Session", "Bounded"]`
  - `properties` (object) — Additional properties of the Collection. Use it to specify extra settings for the Collection.
  - `vectorFieldType` (string) — The vector data type used for the vector field of the Collection created by quick setup.
- **oneOf – custom setup**: A Collection setup whose configuration is supplied explicitly, including the required `collectionName`.
  - `dbName` (string) — The name of the database.
  - `collectionName` (string) **required** — The name of the collection to create.
  - `schema` — The schema is responsible for organizing data in the target collection. A valid schema should have multiple fields, which must include a primary key, a vector field, and several scalar fields. Setting this parameter means that `dimension`, `idType`, `autoID`, `primaryFieldName`, and `vectorFieldName` will be ignored.
  - `indexParams` (array<object>) — The parameters that apply to the index-building process.
    - `metricType` (string) **required** — The similarity metric type used to build the index. For more information, refer to Similarity Metrics](https://milvus.io/docs/metric.md). · default: `"COSINE"` · enum: `["L2", "IP", "COSINE", "JACCARD", "HAMMING"]`
    - `fieldName` (string) **required** — The name of the target field on which an index is to be created.
    - `indexName` (string) **required** — The name of the index to create. The value defaults to the target field name.
    - `params` (object) — The index type and related settings. For details, refer to [Vector Indexes](https://milvus.io/docs/index.md).
      - `index_type` (string) **required** — The type of the index to create
      - `M` (integer) — The maximum degree of the node. This applies only when **index_type** is set to __HNSW__.
      - `efConstruction` (integer) — The search scope. This applies only when **index_type** is set to __HNSW__.
      - `nlist` (integer) — The number of cluster units. This applies only when **index_type** is set to __IVF-related__ index types.
  - `params` (object) — Extra parameters for the collection.
    - `shardsNum` (integer) — The number of shards to create along with the current collection.
    - `consistencyLevel` (string) — The consistency level of the collection. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
    - `partitionsNum` (integer) — The number of partitions to create along with the current collection. This parameter is mandatory if one field of the collection has been designated as the partition key.
    - `ttlSeconds` (integer) — The time-to-live (TTL) period of the collection. If set, the collection is to be dropped once the period ends.
    - `partitionKeyIsolation` (boolean) — Specifies whether to enable partition key isolation for the collection. · default: `false`
    - `mmap.enabled` (boolean) — Specifies whether to enable memory mapping for the collection.
    - `ttlField` (string) — The name of the field to use for TTL-based expiration.
    - `warmup.scalarField` (boolean) — Whether to preload scalar field data into memory on load.
    - `warmup.scalarIndex` (boolean) — Whether to preload scalar index data into memory on load.
    - `warmup.vectorField` (boolean) — Whether to preload vector field data into memory on load.
    - `warmup.vectorIndex` (boolean) — Whether to preload vector index data into memory on load.
  - `description` (string) — The description of the current collection.
  - `consistencyLevel` (string) — The consistency level applied to the collection described by this setup. It determines the consistency guarantee used when the collection is queried. · enum: `["Strong", "Eventually", "Session", "Bounded"]`
  - `properties` (object) — Additional Collection properties, given as key-value pairs.
- **oneOf – external setup**: A Collection setup that refers to an existing external Collection, identified by the required `collectionName`.
  - `dbName` (string) — The name of the database.
  - `collectionName` (string) **required** — The name of the collection to create.
  - `schema` — The schema for an external collection. Must include fields with externalField mappings, plus externalSource and externalSpec.
  - `indexParams` (array<object>) — The parameters that apply to the index-building process.
    - `metricType` (string) **required** — The similarity metric type used to build the index. For more information, refer to Similarity Metrics](https://milvus.io/docs/metric.md). · default: `"COSINE"` · enum: `["L2", "IP", "COSINE", "JACCARD", "HAMMING"]`
    - `fieldName` (string) **required** — The name of the target field on which an index is to be created.
    - `indexName` (string) **required** — The name of the index to create. The value defaults to the target field name.
    - `params` (object) — The index type and related settings. For details, refer to [Vector Indexes](https://milvus.io/docs/index.md).
      - `index_type` (string) **required** — The type of the index to create
      - `M` (integer) — The maximum degree of the node. This applies only when **index_type** is set to __HNSW__.
      - `efConstruction` (integer) — The search scope. This applies only when **index_type** is set to __HNSW__.
      - `nlist` (integer) — The number of cluster units. This applies only when **index_type** is set to __IVF-related__ index types.
  - `params` (object) — Extra parameters for the collection.
    - `shardsNum` (integer) — The number of shards to create along with the current collection.
    - `consistencyLevel` (string) — The consistency level of the collection. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
    - `partitionsNum` (integer) — The number of partitions to create along with the current collection. This parameter is mandatory if one field of the collection has been designated as the partition key.
    - `ttlSeconds` (integer) — The time-to-live (TTL) period of the collection. If set, the collection is to be dropped once the period ends.
    - `partitionKeyIsolation` (boolean) — Specifies whether to enable partition key isolation for the collection. · default: `false`
    - `mmap.enabled` (boolean) — Specifies whether to enable memory mapping for the collection.
    - `ttlField` (string) — The name of the field to use for TTL-based expiration.
    - `warmup.scalarField` (boolean) — Whether to preload scalar field data into memory on load.
    - `warmup.scalarIndex` (boolean) — Whether to preload scalar index data into memory on load.
    - `warmup.vectorField` (boolean) — Whether to preload vector field data into memory on load.
    - `warmup.vectorIndex` (boolean) — Whether to preload vector index data into memory on load.
  - `description` (string) — The description of the current collection.
  - `consistencyLevel` (string) — The consistency level applied to the collection described by this setup. It determines the consistency guarantee used when the collection is queried. · enum: `["Strong", "Eventually", "Session", "Bounded"]`
  - `properties` (object) — Additional properties to apply to the Collection.

Example – Quick setup:

```json
{
  "collectionName": "test_collection",
  "dimension": 5
}
```

Example – Quick setup with custom fields:

```json
{
  "collectionName": "custom_quick_setup",
  "dimension": 5,
  "primaryFieldName": "my_id",
  "idType": "VarChar",
  "vectorFieldName": "my_vector",
  "metric_type": "L2",
  "autoId": true,
  "params": {
    "max_length": "512"
  }
}
```

Example – Custom setup:

```json
{
  "collectionName": "custom_setup",
  "schema": {
    "autoId": false,
    "enableDynamicField": false,
    "fields": [
      {
        "fieldName": "my_id",
        "dataType": "Int64",
        "isPrimary": true
      },
      {
        "fieldName": "my_vector",
        "dataType": "FloatVector",
        "elementTypeParams": {
          "dim": "5"
        }
      }
    ]
  }
}
```

Example – Custom setup with index:

```json
{
  "collectionName": "custom_setup_indexed",
  "schema": {
    "autoId": false,
    "enableDynamicField": false,
    "fields": [
      {
        "fieldName": "my_id",
        "dataType": "Int64",
        "isPrimary": true
      },
      {
        "fieldName": "my_vector",
        "dataType": "FloatVector",
        "elementTypeParams": {
          "dim": "5"
        }
      }
    ]
  },
  "indexParams": [
    {
      "fieldName": "my_vector",
      "metricType": "COSINE",
      "indexName": "my_vector",
      "params": {
        "index_type": "IVF_FLAT",
        "nlist": 1024
      }
    },
    {
      "fieldName": "my_id",
      "indexName": "my_id",
      "params": {
        "index_type": "STL_SORT"
      }
    }
  ]
}
```

Example – External setup:

```json
{
  "collectionName": "test_collection",
  "schema": {
    "externalSource": "s3://s3.<region-id>.amazonaws.com/<bucket>/",
    "externalSpec": "{\"format\": \"parquet\", \"extfs\": {\"access_key_id\": \"AKIA...\", \"access_key_value\": \"u4Lh...\", \"region\": \"us-west-2\", \"cloud_provider\": \"aws\", \"use_ssl\": \"true\", \"use_virtual_host\": \"true\"}}",
    "fields": [
      {
        "fieldName": "product_id",
        "dataType": "Int64",
        "externalField": "id"
      },
      {
        "fieldName": "product_name",
        "dataType": "VarChar",
        "elementTypeParams": {
          "max_length": "256"
        },
        "externalField": "name"
      },
      {
        "fieldName": "embedding",
        "dataType": "FloatVector",
        "elementTypeParams": {
          "dim": "768"
        },
        "externalField": "vector"
      }
    ]
  }
}
```

Example – Custom setup with a struct array field:

```json
{
  "collectionName": "documents_with_chunks",
  "schema": {
    "autoId": false,
    "fields": [
      {
        "fieldName": "document_id",
        "dataType": "Int64",
        "isPrimary": true
      },
      {
        "fieldName": "document_vector",
        "dataType": "FloatVector",
        "elementTypeParams": {
          "dim": 2
        }
      }
    ],
    "structFields": [
      {
        "fieldName": "chunks",
        "description": "Chunk-level scalar and vector values.",
        "typeParams": {
          "max_capacity": 4
        },
        "fields": [
          {
            "fieldName": "positions",
            "dataType": "Int32"
          },
          {
            "fieldName": "vectors",
            "dataType": "FloatVector",
            "elementTypeParams": {
              "dim": 2
            }
          }
        ]
      }
    ]
  },
  "indexParams": [
    {
      "fieldName": "document_vector",
      "indexName": "document_vector_idx",
      "metricType": "L2"
    },
    {
      "fieldName": "chunks[vectors]",
      "indexName": "chunk_vectors_idx",
      "metricType": "L2"
    }
  ]
}
```

## Response 200

Returns a collection object.

- **anyOf – success**: A generic response envelope returned by operations that carry no operation-specific result data. It still includes a `data` object.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object. Its contents depend on the operation that returns it.
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
  "code": 1800,
  "message": "User hasn't authenticated"
}
```

Example – success:

```json
{
  "code": 0,
  "data": {}
}
```
