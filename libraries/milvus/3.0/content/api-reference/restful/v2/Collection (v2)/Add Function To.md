---
title: "Add Function to Collection"
---

# Add Function to Collection

`POST /v2/vectordb/collections/add_function`

This operation adds a function to the schema of an existing collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection.
- `function` (object) **required** — The function definition to add to the Collection.
  - `description` (string) — The description of the function to create.
  - `inputFieldNames` (array<string>) **required** — The names of the input fields for the function to create.
  - `name` (string) **required** — The name of the function to create.
  - `outputFieldNames` (array<string>) **required** — The names of the output fields for the function to create.
  - `params` (object) — Configuration parameters specific to the current function. Once the function type is set to `BM25`, no parameter is required. For applicable parameters to functions of `TEXTEMBEDDING` or `RERANK`, refer to Embedding Functions and Reranking Functions
  - `type` (string) **required** — The type of the function to create. · enum: `["BM25", "TEXTEMBEDDING", "RERANK"]`

## Response 200

None

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
  "code": 800,
  "message": "not enough permission"
}
```
