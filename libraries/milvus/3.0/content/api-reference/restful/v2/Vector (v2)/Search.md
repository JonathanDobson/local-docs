---
title: "Search"
---

# Search

`POST /v2/vectordb/entities/search`

This operation conducts a vector similarity search with an optional scalar filtering expression.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `data` (array<array>) **required** — A list of vector embeddings.Milvus searches for the most similar vector embeddings to the specified ones.This parameter is mutually exclusive with **ids**.
- `ids` (array<any>) — A list of primary keys.Milvus searches for the most similar vector embeddings to those in the specified entities.This parameter is mutually exclusive with **data**.
- `annsField` (string) — The name of the vector field.
- `filter` (string) — The filter used to find matches for the search.
- `groupingField` (string) — Groups search results by a specified field to ensure diversity and avoid returning multiple results from the same group.
- `groupSize` (integer) — The number of entities to return for each group. This parameter is only valid when `groupingField` is specified.
- `strictGroupSize` (boolean) — Whether to return only the top k entities for each group. This parameter is only valid when `groupingField` is specified.
- `limit` (integer) — The total number of entities to return. You can use this parameter in combination with **offset** in **param** to enable pagination. The sum of this value and **offset** in **param** should be less than 16,384.
- `offset` (integer) — The number of records to skip in the search result. You can use this parameter in combination with limit to enable pagination. The sum of this value and limit should be less than 16,384.
- `outputFields` (array<string>) — An array of fields to return along with the search results.
- `searchParams` (object) — The parameter settings specific to this operation.
  - `metricType` (string) — The name of the metric type that applies to the current search. The value should be the same as the metric type of the target collection. · default: `"COSINE"` · enum: `["L2", "IP", "COSINE"]`
  - `params` (object) — Extra search parameters.
    - `radius` (number) — Determines the threshold of least similarity. When setting metric_type to L2, ensure that this value is greater than that of range_filter. Otherwise, this value should be lower than that of range_filter. · format: `"float64"`
    - `range_filter` (number) — Refines the search to vectors within a specific similarity range. When setting metric_type to IP or COSINE, ensure that this value is greater than that of radius. Otherwise, this value should be lower than that of radius. · format: `"float64"`
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies. Setting this parameter indicates that the search is within the specified partitions. Otherwise, the search is across all partitions in the collection.
- `consistencyLevel` (string) — The consistency level of the search operation. The value should be the same as the consistency level of the target collection. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
- `exprParams` (object) — A set of key-value pairs that can be filled back in to the `filter` parameter to enable filtering templating. For details, refer to [Filtering Templating](https://milvus.io/docs/filtering-templating.md).
- `functionScore` (object) — Function settings for the current search request.
  - `functions` (array<object>) — The functions applied when function-based scoring is used in the search request, listed in an array.
    - `description` (string) — The description of the function to apply.
    - `inputFieldNames` (array<string>) **required** — A list of scalar fields to use as input for the function.
    - `name` (string) **required** — The name of the function to apply.
    - `outputFieldNames` (array<string>) **required** — A list of vector fields to use as output for the function.
    - `params` (object) — Extra parameters for the function in key-value pairs.
    - `type` (string) **required** — The type of the function to apply. · enum: `["BM25", "TEXTEMBEDDING", "RERANK"]`
  - `params` (object) — Extra parameters for the function in key-value pairs.
- `params` (object) — Extra parameters for the search in key-value pairs.
- `functionChains` (array<object>) — Function chains applied during search reranking.
  - `name` (string) — The function-chain name.
  - `stage` (string) **required** — The execution stage of the function chain. · enum: `["FunctionChainStageL2Rerank"]`
  - `ops` (array<object>) **required** — The ordered operations in the function chain.
    - `op` (string) **required** — The operation name.
    - `expr` (object) — The optional expression evaluated by this operation.
      - `name` (string) **required** — The expression function name.
      - `args` (array<object>) — The ordered expression arguments.
        - `column` (string) — A column name. Exactly one of `column` and `literal` must be specified.
        - `literal` — A literal value. Exactly one of `column` and `literal` must be specified.
      - `params` (object) — Expression parameters in key-value pairs.
    - `inputs` (array<string>) — Input column names.
    - `outputs` (array<string>) — Output column names.
    - `params` (object) — Operation parameters in key-value pairs.
- `searchAggregation` (object) — Aggregation settings for the search results. This parameter cannot be combined with `ids`, `offset`, or grouping parameters.
  - `fields` (array<string>) **required** — The non-empty scalar fields used to form aggregation buckets.
  - `size` (integer) **required** — The number of aggregation buckets to return. · minimum: `1`
  - `searchSize` (integer) — The number of buckets considered during search. When specified, it must be greater than or equal to `size`. · minimum: `1`
  - `metrics` (object) — Named metric aggregations keyed by result name.
  - `order` (array<object>) — Ordering rules for aggregation buckets.
    - `key` (string) **required** — The bucket count or metric key used for ordering.
    - `direction` (string) **required** — The sort direction. · enum: `["asc", "desc"]`
  - `topHits` (object) — Top-hit settings for each aggregation bucket.
    - `size` (integer) **required** — The number of top hits returned for each bucket. · minimum: `1`
    - `sort` (array<object>) — Sort rules for top hits.
      - `fieldName` (string) **required** — The field used to sort top hits.
      - `direction` (string) **required** — The sort direction. · enum: `["asc", "desc"]`
  - `subAggregation` (object) — A nested aggregation applied within each bucket. A search aggregation may nest at most 3 levels of sub-aggregations beneath the top-level aggregation (4 levels in total; deeper requests are rejected).
    - `fields` (array<string>) **required** — The non-empty scalar fields used to form aggregation buckets.
    - `size` (integer) **required** — The number of aggregation buckets to return. · minimum: `1`
    - `searchSize` (integer) — The number of buckets considered during search. When specified, it must be greater than or equal to `size`. · minimum: `1`
    - `metrics` (object) — Named metric aggregations keyed by result name.
    - `order` (array<object>) — Ordering rules for aggregation buckets.
      - `key` (string) **required** — The bucket count or metric key used for ordering.
      - `direction` (string) **required** — The sort direction. · enum: `["asc", "desc"]`
    - `topHits` (object) — Top-hit settings for each aggregation bucket.
      - `size` (integer) **required** — The number of top hits returned for each bucket. · minimum: `1`
      - `sort` (array<object>) — Sort rules for top hits.
        - `fieldName` (string) **required** — The field used to sort top hits.
        - `direction` (string) **required** — The sort direction. · enum: `["asc", "desc"]`
    - `subAggregation` — A nested aggregation applied within each bucket. A search aggregation may nest at most 3 levels of sub-aggregations beneath the top-level aggregation (4 levels in total; deeper requests are rejected).
- `orderByFields` (array<string>) — The scalar fields used to sort the search results. Each item can be a field name, `fieldName:asc`, or `fieldName:desc`; the default sort direction is ascending.

## Response 200

Returns the search results.

- **anyOf – success**: One form of the successful response body, carrying the search results together with the `topks` and `recalls` arrays that describe each returned result group.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (array<object>) — A list of entity objects.
    - `id` (integer | string) — The primary key value of the returned entity. Milvus primary keys are Int64 or VarChar depending on the collection schema, so the value may arrive as a number or a string.
      - *oneOf – option 1*
      - *oneOf – option 2*
    - `distance` (number) — The similarity distance between the query vector and this returned entity.
    - `grp` (string) — The group that this result belongs to, present when groupingField is specified.
    - `buckets` (array<object>) — Aggregated search buckets, present when searchAggregation is specified.
      - `count` (number) — The number of entities aggregated into this bucket.
      - `hits` (array<object>) — The search results aggregated into this bucket.
      - `key` (array<object>) — The key values that define this bucket.
        - `fieldId` (integer) — The ID of the field that defines this bucket.
        - `fieldName` (string) — The name of the field that defines this bucket.
      - `metrics` (object) — Aggregation metrics computed over the hits in this bucket.
        - `avg` (number) — The average distance of the hits in this bucket.
        - `max` (number) — The maximum distance of the hits in this bucket.
        - `min` (number) — The minimum distance of the hits in this bucket.
        - `n` (number) — The number of hits aggregated into this bucket.
        - `total` (number) — The total distance of the hits in this bucket.
      - `subGroups` (array<object>) — Nested sub-groups of this bucket.
  - `recalls` (array<number>) — Recall values for each search result group.
  - `topks` (array<integer>) — The number of top-K results returned for each query vector.
  - `scanned_remote_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `scanned_total_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `cache_hit_ratio` (number) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `aggTopks` (array<number>) — The top-k limits of the aggregated search branches, present when searchAggregation is specified.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "color": "orange_6781",
      "distance": 1,
      "id": 448300048035776800
    },
    {
      "color": "red_4794",
      "distance": 0.9353201,
      "id": 448300048035776800
    },
    {
      "color": "grey_8510",
      "distance": 0.7733054,
      "id": 448300048035776800
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
