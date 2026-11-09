---
title: "Add File Resource"
---

# Add File Resource

`POST /v2/vectordb/file_resources/add`

Adds a file resource that can be referenced by Milvus features such as analyzers.

## Parameters

- `Authorization` (in header) — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `name` (string) **required** — The unique name of the file resource.
- `path` (string) **required** — The object path of the file in the bucket used by Milvus persistent storage. Include the `minio.rootPath` prefix configured in the Milvus configuration file (typically `milvus.yaml`), if any. The file must already exist. For details, refer to [Manage File Resources](https://milvus.io/docs/manage-file-resources.md#Manage-File-Resources).

## Response 200

Returns an empty object.

- **oneOf – success**: A successful empty response.
  - `code` (integer) — Response code.
  - `data` (object) — An empty result object.
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
  "code": 1100,
  "message": "file resource already exists"
}
```
