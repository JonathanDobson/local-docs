---
title: "Get"
---

# Get

`POST /v1/vector/get`

**Deprecated.**

Gets entities by the specified IDs. You can set an ID in string or integer or set a set of IDs in a list of strings or a list of integers as shown in the four types of request bodies below.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies. Setting this indicates that the operation should be applied to only these partitions. If not set, the operation will be applied to all partitions in the collection.
- `outputFields` (array<string>) — An array of fields to return along with the query results.
- `id` (string | array | integer | array) **required** — The ID of the entity to retrieve. Supply one or more primary key values to fetch the corresponding entities.
  - *oneOf – option 1*: The ID of the entity to be retrieved
  - *oneOf – option 2*: An array of IDs of the entities to be retrieved
  - *oneOf – option 3*: The ID of entity to be retrieved
  - *oneOf – option 4*: An array of IDs of the entities to be retrieved

## Response 200

Returns the query results.

- **anyOf – success**: One of the possible result shapes returned by a successful get request.
  - `code` (integer) — Response code.
  - `data` (array<object>) — Query results.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": [
    {
      "color": "red_7025",
      "id": 1
    },
    {
      "color": "pink_9298",
      "id": 3
    },
    {
      "color": "yellow_4222",
      "id": 5
    }
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
