---
title: "Describe Resource Group"
---

# Describe Resource Group

`POST /v2/vectordb/resource_groups/describe`

This operation returns the configuration of the specified resource group.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `name` (string) **required** — The name of the resource group to describe.
- `config` (object) — The configuration settings applied by the request. It contains `limits`, `requests`, `transfer_from`, and `transfer_to`.
  - `limits` (object) **required** — The allocation limits for the resource group. It contains `node_num`, the number of query nodes allocated to the resource group.
    - `node_num` (integer) — The number of query nodes to allocate to the resource group.
  - `node_filter` (object) — The node filter that constrains which nodes the resource group may use. It contains `node_labels`.
    - `node_labels` (object) — The node labels used by the node filter to match nodes. Labels are expressed as key-value pairs.
  - `requests` (object) **required** — The query node allocation settings for the resource group.
    - `node_num` (integer) — The number of query nodes to allocate to the resource group.
  - `transfer_from` (array<object>) **required** — The list of source resource groups to transfer query nodes from.
    - `resource_group` (string) **required** — The name of the source resource group to transfer query nodes from.
  - `transfer_to` (array<object>) **required** — The list of target resource groups to transfer query nodes to.
    - `resource_group` (string) **required** — The name of the target resource group to transfer query nodes to.

## Response 200

Returns the configuration of the specified resource group.

- **oneOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — The response payload containing the result of the request.
    - `resource_groups` (object) — The configurations of the resource group to update. You can include multiple resource groups in the request body with the name of each resource group as the key and its configuration as the value.
      - `<resource_group_name>` (object) — The updated configuration of the resource group specified by the key.
        - `requests` (object) — The number of query nodes to allocate to the resource group.
          - `node_num` (integer) — The number of query nodes to allocate to the resource group.
        - `limits` (object) — The maximum number of query nodes to allocate to the resource group.
          - `node_num` (integer) — The maximum number of query nodes to allocate to the resource group.
        - `transfer_from` (array<object>) — The list of source resource groups to transfer query nodes from.
          - `resource_group` (string) — The name of the source resource group to transfer query nodes from.
        - `transfer_to` (array<object>) — The list of target resource groups to transfer query nodes to.
          - `resource_group` (string) — The name of the target resource group to transfer query nodes to.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "resource_groups": {
      "group1": {
        "requests": {
          "node_num": 1
        },
        "limits": {
          "node_num": 10000
        },
        "transfer_from": [
          {
            "resource_group": "default"
          }
        ],
        "transfer_to": [
          {
            "resource_group": "default"
          }
        ]
      }
    }
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
