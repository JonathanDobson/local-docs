---
title: "Get Collection Load State"
---

# Get Collection Load State

`POST /v2/vectordb/collections/get_load_state`

This operation returns the load status of a specific collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `partitionNames` (array<string>) — A list of partition names. If any partition names are specified, releasing any of these partitions results in the return of a NotLoad state.

## Response 200

A LoadState object that indicates the load status of the specified collection.

- **anyOf – success**: Response containing the load state of a Collection.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — A LoadState object that indicates the load status and load progress of the specified collection.
    - `loadState` (string) — An object that indicates the load status of the specified collection.
    - `loadProgress` (integer) — An integer that indicates the load progress in the percentage of the specified collection.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "loadProgress": 100,
    "loadState": "LoadStateLoaded"
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
