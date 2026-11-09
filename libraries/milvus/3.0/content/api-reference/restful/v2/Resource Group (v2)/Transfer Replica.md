---
title: "Transfer Collection Replica"
---

# Transfer Collection Replica

`POST /v2/vectordb/resource_groups/transfer_replica`

This operation transfers the replicas of the specified collection from the source resource group to the target resource group.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `sourceRgName` (string) **required** — The name of the source resource group.
- `targetRgName` (string) **required** — The name of the target resource group.
- `collectionName` (string) **required** — The name of the target collection.
- `replicaNum` (integer) **required** — The number of replicas to transfer.

## Response 200

Returns an empty object.

- **oneOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which is an empty object.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
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
