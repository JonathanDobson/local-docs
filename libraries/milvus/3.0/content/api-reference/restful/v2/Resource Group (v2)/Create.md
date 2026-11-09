---
title: "Create Resource Group"
---

# Create Resource Group

`POST /v2/vectordb/resource_groups/create`

This operation creates a resource group. A Milvus instance begins with a default resource group that includes all available query nodes. You can create additional resource groups, reassign specific query nodes from the default group, and load collections into the query nodes in these newly configured groups. This operation always succeeds no matter whether the resource group exists.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `name` (string) **required** — The name of the resource group to create.
- `config` (object) — The configurations of the resource group to create.
  - `limits` (object) **required** — The maximum number of query nodes to allocate to the resource group.
    - `node_num` (integer) — The maximum number of query nodes to allocate to the resource group.
  - `node_filter` (object) — The node filter that constrains which nodes the resource group may be allocated on. It contains `node_labels`.
    - `node_labels` (object) — The node labels used by the node filter to match nodes. Labels are expressed as key-value pairs.
  - `requests` (object) **required** — The number of query nodes to allocate to the resource group.
    - `node_num` (integer) — The number of query nodes to allocate to the resource group.
  - `transfer_from` (array<object>) **required** — The list of source resource groups to transfer query nodes from.
    - `resource_group` (string) **required** — The name of the source resource group to transfer query nodes from.
  - `transfer_to` (array<object>) **required** — The list of target resource groups to transfer query nodes to.
    - `resource_group` (string) **required** — The name of the target resource group to transfer query nodes to.

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
