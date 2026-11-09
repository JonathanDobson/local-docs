---
title: "Query"
---

# Query

`POST /v2/vectordb/entities/query`

This operation conducts a filtering on the scalar field with a specified boolean expression.

## Parameters

- `Authorization` (in header) — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `filter` (string) — The filter used to find matches for the search.
- `outputFields` (array<string>) — An array of fields to return along with the query results.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies. Setting this parameter restricts the operation to the specified partitions. If not set, the operation applies to all partitions in the collection.
- `limit` (integer) — The total number of entities to return. You can use this parameter in combination with **offset** in **param** to enable pagination. The sum of this value and **offset** in **param** should be less than 16,384.
- `offset` (integer) — The number of records to skip in the search result. You can use this parameter in combination with limit to enable pagination. The sum of this value and limit should be less than 16,384.
- `exprParams` (object) — Expression template parameter values for parameterized filter expressions.
- `consistencyLevel` (string) — Consistency level. Possible values are **Strong**, **Session**, **Bounded**, and **Eventually**. · enum: `["Strong", "Session", "Bounded", "Eventually"]`
- `orderByFields` (array<string>) — The scalar fields used to sort query results. Each item can be a field name, `fieldName:asc`, or `fieldName:desc`. The default sort direction is ascending. · example: `["word_count:desc", "book_id:asc"]`
- `groupByFields` (array<string>) — The names of the fields used to group the query results. Each entry identifies one grouping field.

## Response 200

A list of dictionaries with each dictionary representing a queried entity.

- **anyOf – success**: A response payload variant that the query operation can return.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (array<object>) — A list of dictionaries with each dictionary representing a queried entity.
    - `id` (integer | string) — The primary key value of the returned entity. Milvus primary keys are Int64 or VarChar depending on the collection schema, so the value may arrive as a number or a string.
      - *oneOf – option 1*
      - *oneOf – option 2*
    - `grp` (string) — The group that this result belongs to, present when groupingField is specified.
    - `count(*)` (number) — The aggregated count of the group, present when a group-by count-only query is performed.
  - `scanned_remote_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `scanned_total_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `cache_hit_ratio` (number) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
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
