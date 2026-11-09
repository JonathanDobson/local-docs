---
title: "Run Analyzer"
---

# Run Analyzer

`POST /v2/vectordb/common/run_analyzer`

This operation runs an analyzer on the provided text and returns the tokenization result.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `text` (array<string>) **required** — A list of text strings to analyze.
- `analyzerParams` (string) — The analyzer parameters as a JSON string.
- `withDetail` (boolean) — Whether to return detailed token information.
- `withHash` (boolean) — Whether to include hash values in the result.
- `collectionName` (string) — The name of the collection whose field analyzer to use.
- `fieldName` (string) — The name of the field whose analyzer to use.
- `analyzerNames` (array<string>) — A list of analyzer names to use.

## Response 200

None

- **anyOf – success**: One possible shape of the analyze response, containing a `code` and a `data` payload.
  - `code` (integer) — The response code indicating whether the request succeeded.
  - `data` (array<object>) — The list of analysis results returned by the analyzer.
    - `tokens` (array<string>) — The tokens the analyzer produced for the text.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "tokens": [
        "hello",
        "world"
      ]
    }
  ]
}
```

Example – failure:

```json
{
  "code": 800,
  "message": "not enough permission"
}
```
