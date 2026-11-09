---
title: "Query"
---

# Query

`POST /v1/vector/query`

**Deprecated.**

Conducts a query on scalar fields in a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies.
- `filter` (string) **required** — The filter used to find matches for the query.
- `limit` (integer) — The maximum number of entities to return.The sum of this value and that of `offset` should be less than **16384**. · minimum: `1` · maximum: `16384`
- `offset` (integer) — The number of entities to skip in the search results.The sum of this value and that of `limit` should be less than **16384**. · minimum: `0` · maximum: `16384`
- `outputFields` (array<string>) — An array of fields to return along with the search results. When setting this to `count(*)`, you need to set `limit` to 0 to get the total count of the entities that match the filter.

## Response 200

Returns the query results.

- **anyOf – success**: A possible response body for a successful query request.
  - `code` (integer) — Response code.
  - `data` (array<object>) — Response payload which is an array of objects that contain the specified output fields and their corresponding values.
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
      "color": "red_4794",
      "id": 4
    },
    {
      "color": "red_9392",
      "id": 6
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
