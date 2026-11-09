---
title: "Describe Collection"
---

# Describe Collection

`POST /v2/vectordb/collections/describe`

Describes the details of a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `partitionNames` (array<string>) — Names of the partitions to which this operation applies. When specified, the operation scope is limited to these partitions; otherwise the entire Collection is used.

## Response 200

Returns the specified collection in detail.

- **oneOf – success**: The response returned when a Collection is described successfully.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload, which carries detailed information about the specified collection.
    - `aliases` (array<string>) — A list aliases assigned to the collection.
    - `autoID` (boolean) — Whether the primary key of this collection automatically increments.
    - `collectionID` (integer) — The ID assigned to the collection upon creation. · format: `"int64"`
    - `collectionName` (string) — The name of the current collection.
    - `consistencyLevel` (string) — The consistency level of the current collection. · enum: `["Strong", "Bounded", "Session", "Eventually"]`
    - `description` (string) — The description of the collection.
    - `enableDynamicField` (boolean) — Whether the reserved dynamic field named $meta is enabled to save non-schema-defined fields and their values in key-value pairs.
    - `externalSource` (string) — The JSON-encoded external source configuration if this collection is an external collection. An object url in an S3 bucket applies.
    - `externalSpec` (string) — The JSON-encoded external specification if this collection is an external collection. The content of this field may vary depending on the connector type and the source data format, which may include, but not limited to, file format, field mapping, etc.
    - `fields` (array<object>) — The collection fields in an array
      - `name` (string) — The name of the current field.
      - `primaryKey` (boolean) — Indicates whether the current field is a primary key.
      - `partitionKey` (boolean) — Indicates whether the current field is a partition key.
      - `clusteringKey` (boolean) — Indicates whether the current field is a clustering key.
      - `autoId` (boolean) — Indicates whether the current field is an auto-generated ID.
      - `description` (string) — The description of the current field.
      - `nullable` (boolean) — Indicates whether the current field allows null values.
      - `defaultValue` (string) — The default value of the current field. This value is only available for fields that have a default value.
      - `isFunctionOutput` (boolean) — Indicates whether the current field is an derived field of a function. This value is only available for fields that are derived from a function.
      - `type` (string) — The data type of the current field.
      - `id` (string) — The unique identifier of the current field.
      - `params` (object) — The parameters of the current field. This value is only available for fields that have parameters.
      - `elementType` (string) — The data type of the elements in the current field. This value is only available for fields that are arrays.
    - `functions` (array<object>) — The collection functions in an array
      - `name` (string) — The name of the current function.
      - `description` (string) — The description of the current function.
      - `type` (string) — The type of the current function.
      - `id` (string) — The ID of the current function.
      - `inputFieldNames` (array<string>) — The input field names of the current function.
      - `outputFieldNames` (array<string>) — The output field names of the current function.
      - `params` (object) — The parameters of the current function.
    - `indexes` (array<object>) — The created indexes in an array
      - `indexName` (string) — The name of the current index.
      - `fieldName` (string) — The name of the field associated with the current index.
      - `metricType` (string) — The metric type of the current index.
    - `load` (string) — The load status of the current collection.
    - `partitionsNum` (integer) — The number of partitions in the collection.
    - `properties` (array<object>) — Extra collection properties in an array.
      - `key` (string) — The property name
      - `value` (string) — The property value.
    - `shardsNum` (integer) — The number of shards created along with the collection.
    - `structFields` (array<object>) — The struct array fields in the collection.
      - `name` (string) — The name of the struct array field.
      - `id` (string) — The unique identifier of the struct array field.
      - `description` (string) — The description of the struct array field.
      - `type` (string) — The data type of the field. · enum: `["ArrayOfStruct"]`
      - `fields` (array<object>) — The nested sub-fields. Each type is the scalar or vector type of the struct field.
        - `name` (string) — The name of the sub-field.
        - `id` (string) — The unique identifier of the sub-field.
        - `type` (string) — The scalar or vector type of the struct field. · enum: `["Bool", "Int8", "Int16", "Int32", "Int64", "Float", "Double", "VarChar", "BinaryVector", "FloatVector", "Float16Vector", "BFloat16Vector", "Int8Vector"]`
        - `params` (array<object>) — Parameters for the element type.
          - `key` (string) — The name of the extra parameter; together with `value` it forms one key-value pair.
          - `value` (string) — The value assigned to the parameter named by `key`.
      - `params` (array<object>) — Additional field parameters.
        - `key` (string) — The name of the extra parameter; together with `value` it forms one key-value pair.
        - `value` (string) — The value assigned to the parameter named by `key`.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
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

Example – Collection with a struct array field:

```json
{
  "code": 0,
  "data": {
    "collectionName": "documents_with_chunks",
    "fields": [
      {
        "id": 100,
        "name": "document_id",
        "primaryKey": true,
        "type": "Int64"
      },
      {
        "id": 101,
        "name": "document_vector",
        "primaryKey": false,
        "type": "FloatVector"
      }
    ],
    "structFields": [
      {
        "id": 102,
        "name": "chunks",
        "description": "Chunk-level scalar and vector values.",
        "type": "ArrayOfStruct",
        "fields": [
          {
            "id": 103,
            "name": "positions",
            "type": "Int32"
          },
          {
            "id": 104,
            "name": "vectors",
            "type": "FloatVector"
          }
        ]
      }
    ]
  }
}
```
