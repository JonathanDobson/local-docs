---
title: "List File Resources"
---

# List File Resources

`POST /v2/vectordb/file_resources/list`

Lists the file resources registered with Milvus.

## Parameters

- `Authorization` (in header) — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)


## Response 200

Returns the registered file resources.

- **oneOf – success**: A successful response containing the registered file resources.
  - `code` (integer) **required** — Response code.
  - `data` (array<object>) **required** — The registered file resources.
    - `id` (integer) **required** — The unique identifier of the file resource. · format: `"int64"`
    - `name` (string) **required** — The unique name of the file resource.
    - `path` (string) **required** — The object path recorded for the file resource in the bucket used by Milvus persistent storage. The path includes the `minio.rootPath` prefix configured in the Milvus configuration file (typically `milvus.yaml`), if any. For details, refer to [Manage File Resources](https://milvus.io/docs/manage-file-resources.md#Manage-File-Resources).
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "id": 451799928999570200,
      "name": "synonyms",
      "path": "files/synonyms.txt"
    }
  ]
}
```

Example – failure:

```json
{
  "code": 65535,
  "message": "service unavailable"
}
```
