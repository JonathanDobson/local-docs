---
title: "Upsert"
---

# Upsert

`POST /v1/vector/upsert`

**Deprecated.**

Upserts one or more entities into a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which entities will be upserted.
- `data` (object | array) **required** — An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema
  - *oneOf – option 1*: A single entity, whose structure should match the schema of the target collection.
  - *oneOf – option 2*: A list of entities, each of which should match the schema of the target collection.

## Response 200

Returns the number of inserted entities and an array of their IDs.

- **anyOf – success**: A possible response body for a successful upsert request.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload.
    - `upsertCount` (integer) — The number of upserted entities. · example: `4`
    - `upsertIds` (array<string>) — An array of the IDs of inserted entities.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "upsertCount": 10,
    "upsertIds": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ]
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
