---
title: "Delete"
---

# Delete

`POST /v2/vectordb/entities/delete`

This operation deletes entities by their IDs or with a boolean expression.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection from which entities are to be deleted.
- `filter` (string) **required** — A scalar filtering condition to filter matching entities. You can set this parameter to an empty string to skip scalar filtering. To build a scalar filtering condition, refer to [Boolean Expression Rules](https://milvus.io/docs/boolean.md).
- `partitionName` (string) — The name of a partition in the current collection. If specified, the data is to be deleted from the specified partition.
- `id` (string) — The primary key of the entity to delete. You can use this parameter instead of `filter` to delete a single entity by its ID.
- `exprParams` (object) — Expression template parameter values for parameterized filter expressions.

Example – Option 1:

```json
{
  "collectionName": "medium_articles",
  "filter": "id == 4321034832910"
}
```

Example – Option 2:

```json
{
  "collectionName": "medium_articles",
  "filter": "reading_time > 15"
}
```

Example – Option 3:

```json
{
  "collectionName": "medium_articles",
  "id": "4321034832910"
}
```

## Response 200

Returns an empty object.

- **oneOf – success**: One of the possible result shapes returned by a successful delete request.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (object) — Response payload containing the number of entities deleted.
    - `deleteCount` (integer) — The number of entities removed by the request.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
  "data": {
    "deleteCount": 1
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
