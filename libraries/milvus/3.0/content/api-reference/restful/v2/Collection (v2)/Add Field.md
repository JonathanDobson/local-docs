---
title: "Add Collection Field"
---

# Add Collection Field

`POST /v2/vectordb/collections/fields/add`

This operation adds a field to a collection without recreating the collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `schema` (object) **required** — A field schema object.
  - `fieldName` (string) **required** — The name of the field to create in the target collection
  - `dataType` (string) **required** — The data type of the field values. · enum: `["Bool", "Int8", "Int16", "Int32", "Int64", "Float", "Double", "VarChar", "Array", "Json", "Geometry", "BinaryVector", "FloatVector", "Float16Vector", "BFloat16Vector", "SparseFloatVector", "Int8Vector"]`
  - `elementDataType` (string) — The data type of the elements in an array field. This is required if the current field is of the array type. · enum: `["Bool", "Int8", "Int16", "Int32", "Int64", "Float", "Double", "VarChar"]`
  - `nullable` (boolean) — Whether the field can be null. If set to `true`, the field can contain null values.
  - `defaultValue` (string) — The default value of the field. This is required if the current field is of the `VarChar` type.
  - `isPrimary` (boolean) — Whether the current field is the primary field. Setting this to True makes the current field the primary field.
  - `isPartitionKey` (boolean) — Whether the current field serves as the partition key. Setting this to True makes the current field serve as the partition key. In this case, Milvus manages all partitions in the current collection.
  - `isClusteringKey` (boolean) — Whether the current field serves as the clustering key. Setting this to True makes the current field serve as the clustering key. You can read more about the cluster key in Clustering Compaction.
  - `elementTypeParams` (object) — Extra field parameters.
    - `max_length` (integer) — An optional parameter for VarChar values that determines the maximum length of the value in the current field.
    - `dim` (integer) — An optional parameter for FloatVector or BinaryVector fields that determines the vector dimension.
    - `max_capacity` (integer) — An optional parameter for Array field values that determines the maximum number of elements in the current array field.
  - `externalField` (string) — The name of the corresponding column in the external source. Required when creating an external collection.

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
