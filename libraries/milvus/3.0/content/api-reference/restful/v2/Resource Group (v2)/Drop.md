---
title: "Drop Resource Group"
---

# Drop Resource Group

`POST /v2/vectordb/resource_groups/drop`

This operation drops the specified resource group.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `name` (string) **required** — The name of the resource group to drop.
- `config` (object) — The configuration for the drop action, covering resource limits, requested query nodes, and source and target resource groups for query node transfers.
  - `limits` (object) **required** — The resource limits for the resource group, including the maximum number of query nodes that can be allocated.
    - `node_num` (integer) — The maximum number of query nodes to allocate to the resource group.
  - `node_filter` (object) — The node filter configuration for the resource group.
    - `node_labels` (object) — The node labels used by the node filter.
  - `requests` (object) **required** — The requested query node allocation for the resource group.
    - `node_num` (integer) — The number of query nodes requested for the resource group.
  - `transfer_from` (array<object>) **required** — The list of source resource groups from which query nodes are transferred.
    - `resource_group` (string) **required** — The name of the source resource group from which query nodes are transferred.
  - `transfer_to` (array<object>) **required** — The list of target resource groups to which query nodes are transferred.
    - `resource_group` (string) **required** — The name of the target resource group to which query nodes are transferred from the resource group being dropped.

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
