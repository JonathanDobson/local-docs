---
title: "Hybrid Search"
---

# Hybrid Search

`POST /v2/vectordb/entities/hybrid_search`

This operation searches for entities based on vector similarity and scalar filtering and reranks the results using a specified strategy.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies. Setting this parameter indicates that the search is within the specified partitions. Otherwise, the search is across all partitions in the collection.
- `search` (array<object>) **required** — The search parameters
  - `data` (array<number>) **required** — A list of vector embeddings.Milvus searches for the most similar vector embeddings to the specified ones.
  - `annsField` (string) **required** — The name of the vector field.
  - `filter` (string) **required** — A boolean expression filter.
  - `groupingField` (string) **required** — The name of the field that serve as the aggregation criteria.
  - `metricType` (string) — The name of the metric type that applies to the current search. The value should be the same as the metric type of the target collection. · default: `"COSINE"` · enum: `["L2", "IP", "COSINE"]`
  - `limit` (integer) **required** — The number of entities to return.
  - `offset` (integer) **required** — The number of entities to skip in the returned entities.
  - `ignoreGrowing` (boolean) **required** — Whether to ignore the entities found in the growing segments.
  - `params` (object) — Extra search parameters.
    - `radius` (number) — Determines the threshold of least similarity. When setting metric_type to L2, ensure that this value is greater than that of range_filter. Otherwise, this value should be lower than that of range_filter. · format: `"float64"`
    - `range_filter` (number) — Refines the search to vectors within a specific similarity range. When setting metric_type to IP or COSINE, ensure that this value is greater than that of radius. Otherwise, this value should be lower than that of radius. · format: `"float64"`
  - `exprParams` (object) — Expression template parameter values for parameterized filter expressions.
- `rerank` (object) — The reranking strategy.
  - `strategy` (string) — The name of the reranking strategy. · enum: `["rrf", "weighted"]`
  - `params` (object) **required** — A set of parameters related to the specified strategy
    - `k` (integer) **required** — A tunable constant in the RRF algorithm. This applies only when the strategy is set to `rrf`.
- `limit` (integer) — The total number of entities to return. You can use this parameter in combination with **offset** in **param** to enable pagination. The sum of this value and **offset** in **param** should be less than 16,384.
- `groupSize` (integer) — The number of entities to return for each group. This parameter is only valid when `groupingField` is specified.
- `strictGroupSize` (boolean) — Whether to return only the top k entities for each group. This parameter is only valid when `groupingField` is specified.
- `outputFields` (array<string>) — An array of fields to return along with the search results.
- `consistencyLevel` (string) — The consistency level of the search operation. The value should be the same as the consistency level of the target collection. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
- `functionScore` (object) — Function settings for the current search request.
  - `functions` (array<object>) — The function definitions that `functionScore` applies when scoring the hybrid search results.
    - `description` (string) — The description of the function to apply.
    - `inputFieldNames` (array<string>) **required** — A list of scalar fields to use as input for the function.
    - `name` (string) **required** — The name of the function to apply.
    - `outputFieldNames` (array<string>) **required** — A list of vector fields to use as output for the function.
    - `params` (object) — Extra parameters for the function in key-value pairs.
    - `type` (string) **required** — The type of the function to apply. · enum: `["BM25", "TEXTEMBEDDING", "RERANK"]`
  - `params` (object) — Extra parameters for the function in key-value pairs.
- `offset` (integer) — Number of records to skip in the search results.
- `groupingField` (string) — Name of the field to group search results by.
- `functionChains` (array<object>) — The function chains applied during search reranking.
  - `name` (string) — The name of the function to apply in the chain.
  - `ops` (array<object>) — The ordered operations executed by the function chain.
    - `expr` (object) — An optional expression evaluated by this operation.
      - `args` (array<object>) — The ordered arguments passed to the expression.
        - `column` (string) — The name of the column used as this argument. Exactly one of `column` and `literal` must be specified.
        - `literal` — A literal value used as this argument. Exactly one of `column` and `literal` must be specified.
      - `name` (string) — The name of the function to apply in this expression.
      - `params` (object) — Extra parameters for the search, supplied as key-value pairs.
    - `inputs` (array<string>) — The input column names for the operation.
    - `op` (string) — The name of the operation to perform in this function chain step.
    - `outputs` (array<string>) — The output column names produced by the operation.
    - `params` (object) — Extra search parameters for this operation, provided as key-value pairs.
  - `stage` (string) — The execution stage of the function chain. Supported value: `FunctionChainStageL2Rerank`.

## Response 200

Returns the search results.

- **anyOf – success**: A response object returned by the hybrid search operation.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (array<object>) — Search results
    - `id` (integer | string) — The primary key value of the returned entity. Milvus primary keys are Int64 or VarChar depending on the collection schema, so the value may arrive as a number or a string.
      - *oneOf – option 1*
      - *oneOf – option 2*
    - `distance` (number) — The similarity distance between the query vector and this returned entity.
    - `grp` (string) — The group that this result belongs to, present when groupingField is specified.
  - `topks` (array<integer>) — The number of top-K results returned for each query vector.
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
      "book_describe": "book_105",
      "distance": 0.09090909,
      "id": 450519760774180800,
      "user_id": 5,
      "word_count": 105
    },
    {
      "book_describe": "book_246",
      "distance": 0.09090909,
      "id": 450519760774180900,
      "user_id": 46,
      "word_count": 246
    },
    {
      "book_describe": "book_367",
      "distance": 0.08333333600000001,
      "id": 450519760774181060,
      "user_id": 67,
      "word_count": 367
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
