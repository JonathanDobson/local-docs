# Stripe API 2023-10-16 — tax codes

Operations under `/v1/tax_codes` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/tax_codes

operationId: `GetTaxCodes`

A list of [all tax codes available](https://stripe.com/docs/tax/tax-categories) to add to Products in order to allow specific tax calculations.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/tax_codes/{id}

operationId: `GetTaxCodesId`

Retrieves the details of an existing tax code. Supply the unique tax code ID and Stripe will return the corresponding tax code information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `tax_code`

# Objects returned

## The `tax_code` object

[Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string | yes | A detailed description of which types of products the tax code represents. |
| `id` | string | yes | Unique identifier for the object. |
| `name` | string | yes | A short name for the tax code. |
| `object` | enum: `tax_code` | yes | String representing the object's type. Objects of the same type share the same value. |

