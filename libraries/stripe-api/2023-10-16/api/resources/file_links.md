# Stripe API 2023-10-16 — file links

Operations under `/v1/file_links` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/file_links

operationId: `GetFileLinks`

Returns a list of file links.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return links that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expired` | boolean |  | Filter links by their expiration status. By default, Stripe returns all links. |
| `file` | string |  | Only return links for the given file. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/file_links

operationId: `PostFileLinks`

Creates a new file link object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | The link isn't usable after this future timestamp. |
| `file` | string | yes | The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `identity_document_downloadable`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `file_link`

## GET /v1/file_links/{link}

operationId: `GetFileLinksLink`

Retrieves the file link with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `link (path)` | string | yes |  |

Returns: `file_link`

## POST /v1/file_links/{link}

operationId: `PostFileLinksLink`

Updates an existing file link object. Expired links can no longer be updated.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `link (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | enum: `now` or timestamp (Unix seconds) or "" (to unset) |  | A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `file_link`

# Objects returned

## The `file_link` object

To share the contents of a `File` object with non-Stripe users, you can
create a `FileLink`. `FileLink`s contain a URL that you can use to
retrieve the contents of the file without authentication.

Expandable fields (pass `expand[]=<field>`): `file`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expired` | boolean | yes | Returns if the link is already expired. |
| `expires_at` | timestamp (Unix seconds) |  | Time that the link expires. |
| `file` | string or `file` | yes | The file object this link points to. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `file_link` | yes | String representing the object's type. Objects of the same type share the same value. |
| `url` | string |  | The publicly accessible URL to download the file. |

