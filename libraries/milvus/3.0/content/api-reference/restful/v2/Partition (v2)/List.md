---
title: "List Partitions"
---

# List Partitions

`POST /v2/vectordb/partitions/list`

This operation lists all partitions in the database used in the current connection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the target database.
- `collectionName` (string) **required** — The name of the target collection to which the partition belongs.
- `partitionNames` (array<string>) — The names of the partitions to which this operation applies. When specified, the operation is limited to those partitions; when omitted, the entire Collection is covered.

## Response 200

A list of partition names.

- **anyOf – success**: A response payload object that the operation may return.
  - `code` (integer) — Response code.
  - `data` (array<string>) — A list of partition names
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "_default"
  ]
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
