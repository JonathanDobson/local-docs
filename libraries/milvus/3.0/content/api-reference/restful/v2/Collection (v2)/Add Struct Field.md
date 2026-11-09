---
title: "Add Collection Struct Field"
---

# Add Collection Struct Field

`POST /v2/vectordb/collections/struct_fields/add`

This operation adds a StructArray field to an existing collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection.
- `schema` (object) **required** — The StructArray field schema.
  - `fieldName` (string) **required** — The name of the StructArray field.
  - `description` (string) — A description of the StructArray field.
  - `dataType` (string) **required** — The StructArray data type. Use ArrayOfStruct, or Array together with elementDataType set to Struct. · enum: `["ArrayOfStruct", "Array"]`
  - `elementDataType` (string) — The element type when dataType is Array. · enum: `["Struct"]`
  - `fields` (array<object>) **required** — The scalar or vector sub-fields in the StructArray field.
    - `fieldName` (string) **required** — The name of the sub-field.
    - `dataType` (string) **required** — The scalar or vector type of the struct field. · enum: `["Bool", "Int8", "Int16", "Int32", "Int64", "Float", "Double", "VarChar", "BinaryVector", "FloatVector", "Float16Vector", "BFloat16Vector", "Int8Vector"]`
    - `elementTypeParams` (object) — Parameters for the element type, such as max_length for VarChar or dim for vector types.
  - `typeParams` (object) — Parameters for the struct array field. `max_capacity` is required and specifies the maximum number of struct elements allowed per entity.
    - `max_capacity` (integer) — The maximum number of struct elements allowed per entity. · minimum: `1` · maximum: `4096`
  - `nullable` (boolean) — Whether the StructArray field can be null.

## Response 200

Returns an empty object.

- **oneOf – success**: A generic response envelope returned by operations that carry no operation-specific result data. It still includes a `data` object.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object. Its contents depend on the operation that returns it.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.
