---
title: "Delete"
---

# Delete

`POST /v1/vector/delete`

**Deprecated.**

Deletes one or more entities from a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `id` (string | array | integer | array) **required** — The primary key of the entity to delete. Use this parameter instead of `filter` to delete a single entity by its ID.
  - *oneOf – option 1*: The ID of the entity to be deleted
  - *oneOf – option 2*: An array of IDs of the entities to be deleted
  - *oneOf – option 3*: The ID of the entity to be deleted
  - *oneOf – option 4*: An array of IDs of the entities to be deleted

Example – Option 1:

```json
{
  "dbName": "default",
  "collectionName": "my_collection",
  "id": "4321034832910"
}
```

## Response 200

Returns an empty object.

- **oneOf – success**: An object returned when the delete operation succeeds.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is an empty object.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
  "data": {}
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
