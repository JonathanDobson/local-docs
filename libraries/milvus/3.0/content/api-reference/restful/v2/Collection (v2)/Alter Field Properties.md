---
title: "Alter Field Properties"
---

# Alter Field Properties

`POST /v2/vectordb/collections/fields/alter_properties`

This operation alters the properties of a field in a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `fieldName` (string) **required** — The name of the field whose properties are to be altered.
- `fieldParams` (object) — The properties of the field to alter.
  - `max_length` (integer) — The maximum length of the field. Setting this to a non-zero value restricts the maximum length of the field to the specified value.This parameter applies only when the field is of type `VarChar`.
  - `max_capacity` (integer) — The maximum capacity of the field. Setting this to a non-zero value restricts the maximum capacity of the field to the specified value.This parameter applies only when the field is of type `Array`.
  - `mmap_enabled` (boolean) — Whether to enable memory-mapped file for the field.This parameter applies only when the field is of type `Vector`.

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
