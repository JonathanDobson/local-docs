# Stripe API 2023-10-16 — tax rates

Operations under `/v1/tax_rates` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/tax_rates

operationId: `GetTaxRates`

Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Optional flag to filter by tax rates that are either active or inactive (archived). |
| `created` | object or integer |  | Optional range for filtering created date. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `inclusive` | boolean |  | Optional flag to filter by tax rates that are inclusive (or those that are not inclusive). |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/tax_rates

operationId: `PostTaxRates`

Creates a new tax rate.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set. |
| `country` | string |  | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `description` | string |  | An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers. |
| `display_name` | string | yes | The display name of the tax rate, which will be shown to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `inclusive` | boolean | yes | This specifies if the tax rate is inclusive or exclusive. |
| `jurisdiction` | string |  | The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `percentage` | number | yes | This represents the tax rate percent out of 100. |
| `state` | string |  | [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States. |
| `tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` |  | The high-level tax type, such as `vat` or `sales_tax`. |

Returns: `tax_rate`

## GET /v1/tax_rates/{tax_rate}

operationId: `GetTaxRatesTaxRate`

Retrieves a tax rate with the given ID

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `tax_rate (path)` | string | yes |  |

Returns: `tax_rate`

## POST /v1/tax_rates/{tax_rate}

operationId: `PostTaxRatesTaxRate`

Updates an existing tax rate.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `tax_rate (path)` | string | yes |  |
| `active` | boolean |  | Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set. |
| `country` | string |  | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `description` | string |  | An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers. |
| `display_name` | string |  | The display name of the tax rate, which will be shown to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `jurisdiction` | string |  | The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `state` | string |  | [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States. |
| `tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` |  | The high-level tax type, such as `vat` or `sales_tax`. |

Returns: `tax_rate`

# Objects returned

## The `tax_rate` object

Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set. |
| `country` | string |  | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `description` | string |  | An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers. |
| `display_name` | string | yes | The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page. |
| `effective_percentage` | number |  | Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product's taxability and whether the user is registered to collect taxes in the corresponding jurisdiction. |
| `id` | string | yes | Unique identifier for the object. |
| `inclusive` | boolean | yes | This specifies if the tax rate is inclusive or exclusive. |
| `jurisdiction` | string |  | The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice. |
| `jurisdiction_level` | enum: `city`, `country`, `county`, `district`, `multiple`, `state` |  | The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `tax_rate` | yes | String representing the object's type. Objects of the same type share the same value. |
| `percentage` | number | yes | Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions. |
| `state` | string |  | [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States. |
| `tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` |  | The high-level tax type, such as `vat` or `sales_tax`. |

