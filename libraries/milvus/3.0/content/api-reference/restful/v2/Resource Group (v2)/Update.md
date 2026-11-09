---
title: "Update Resource Group"
---

# Update Resource Group

`POST /v2/vectordb/resource_groups/alter`

This operation updates the configuration of the specified resource group.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `resource_groups` (object) **required** — The configurations of the resource group to update. You can include multiple resource groups in the request body with the name of each resource group as the key and its configuration as the value.
  - `<resource_group_name>` (object) — The updated configuration of the resource group specified by the key.
    - `requests` (object) — The number of query nodes to allocate to the resource group.
      - `node_num` (integer) — The number of query nodes to allocate to the resource group.
    - `limits` (object) — The maximum number of query nodes to allocate to the resource group.
      - `node_num` (integer) — The maximum number of query nodes to allocate to the resource group.
    - `transfer_from` (array<object>) — The list of source resource groups to transfer query nodes from.
      - `resource_group` (string) — The name of the source resource group to transfer query nodes from.
    - `transfer_to` (array<object>) — The list of target resource groups to transfer query nodes to.
      - `resource_group` (string) — The name of the target resource group to transfer query nodes to.

## Response 200

Returns an empty object.

- **anyOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which is an empty object.
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
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
