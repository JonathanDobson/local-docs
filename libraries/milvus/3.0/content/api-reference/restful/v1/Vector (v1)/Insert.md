---
title: "Insert"
---

# Insert

`POST /v1/vector/insert`

**Deprecated.**

Inserts one or more entities into a collection. You can add a maximum of 100 entities at a time. To insert large volumn of data, you are advised to use the bulk-insert API. For details, refer to [Data Import](/docs/data-import).

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which entities will be inserted.
- `partitionName` (string) — The name of the partition to which this operation applies.
- `data` (object | array) **required** — An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema
  - *oneOf – option 1*: A single entity, whose structure should match the schema of the target collection.
  - *oneOf – option 2*: An array of entities to insert into the Collection.

Example – Option 1:

```json
{
  "collectionName": "my_collection",
  "data": {
    "id": 1,
    "vector": [
      0.1,
      0.2,
      0.3,
      0.5,
      0.6
    ]
  }
}
```

Example – Option 2:

```json
{
  "collectionName": "my_collection",
  "data": [
    {
      "id": 1,
      "vector": [
        0.1,
        0.2,
        0.3,
        0.5,
        0.6
      ]
    },
    {
      "id": 2,
      "vector": [
        0.2,
        0.3,
        0.4,
        0.6,
        0.7
      ]
    }
  ]
}
```

## Response 200

Returns the number of inserted entities and an array of their IDs.

- **oneOf – success**: A possible response body for a successful insert request.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is the statistics on the insert results.
    - `insertCount` (integer) — The number of inserted entities.
    - `insertIds` (array<string>) — Response payload which is an array of the IDs of inserted entities.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {
    "insertCount": 4,
    "insertIds": [
      "id1",
      "id2"
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
