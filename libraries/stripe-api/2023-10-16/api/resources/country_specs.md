# Stripe API 2023-10-16 — country specs

Operations under `/v1/country_specs` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/country_specs

operationId: `GetCountrySpecs`

Lists all Country Spec objects available in the API.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/country_specs/{country}

operationId: `GetCountrySpecsCountry`

Returns a Country Spec for a given Country code.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `country (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `country_spec`

# Objects returned

## The `country_spec` object

Stripe needs to collect certain pieces of information about each account
created. These requirements can differ depending on the account's country. The
Country Specs API makes these rules available to your integration.

You can also view the information from this API call as [an online
guide](https://stripe.com/docs/connect/required-verification-information).

Expandable fields (pass `expand[]=<field>`): `verification_fields`

| Field | Type | Required | Description |
|---|---|---|---|
| `default_currency` | string | yes | The default currency for this country. This applies to both payment methods and bank accounts. |
| `id` | string | yes | Unique identifier for the object. Represented as the ISO country code for this country. |
| `object` | enum: `country_spec` | yes | String representing the object's type. Objects of the same type share the same value. |
| `supported_bank_account_currencies` | map (key → value) | yes | Currencies that can be accepted in the specific country (for transfers). |
| `supported_payment_currencies` | array of string | yes | Currencies that can be accepted in the specified country (for payments). |
| `supported_payment_methods` | array of string | yes | Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges). |
| `supported_transfer_countries` | array of string | yes | Countries that can accept transfers from the specified country. |
| `verification_fields` | `country_spec_verification_fields` | yes |  |

