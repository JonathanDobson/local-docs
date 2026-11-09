---
title: "Search"
---

# Search

`POST /v1/vector/search`

**Deprecated.**

Conducts a similarity search on the vector field in a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies. Setting this parameter indicates that the search scope should be limited to the specified partitions. If not specified, the search scope is the entire collection.
- `filter` (string) — The filter used to find matches for the search
- `limit` (integer) — The maximum number of entities to return. The sum of this value of that of `offset` should be less than **16,384**. · default: `100` · minimum: `1` · maximum: `16384`
- `offset` (integer) — The number of entities to skip in the search results.The sum of this value and that of `limit` should not be greater than **16,384**. · minimum: `0` · maximum: `16384`
- `outputFields` (array<string>) — An array of fields to return along with the search results.
- `vector` (array<number>) **required** — The query vector in the form of a list of floating numbers. The length of the query vector should match the dimension of the vector field in the collection.
- `params` (object) — List of search parameters
  - `radius` (number) — The angle where the vector with the least similarity resides. · format: `"float64"`
  - `range_filter` (number) **required** — Used in combination to filter vector field values whose similarity to the query vector falls into a specific range. · format: `"float64"`

## Response 200

Returns the search results.

- **anyOf – success**: A possible response body for a successful vector search request.
  - `code` (integer) — Response code.
  - `data` (array<object>) — Response payload that carries the search results.
    - `id` (integer) — The ID of the entity.
    - `distance` (number) — The similarity score of the entity to the query vector. · format: `"float32"`
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": [
    {
      "color": "pink_8682",
      "distance": 1,
      "id": 0
    },
    {
      "color": "red_7025",
      "distance": 0.6290165,
      "id": 1
    },
    {
      "color": "red_4794",
      "distance": 0.5975797,
      "id": 4
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
