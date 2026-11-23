# Stripe API 2023-10-16 — prices

Operations under `/v1/prices` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/prices

operationId: `GetPrices`

Returns a list of your active prices, excluding [inline prices](https://stripe.com/docs/products-prices/pricing-models#inline-pricing). For the list of inactive prices, set `active` to false.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices). |
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `currency` | string |  | Only return prices for the given currency. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `lookup_keys` | array of string |  | Only return the price with these lookup_keys, if any exist. |
| `product` | string |  | Only return prices for the given product. |
| `recurring` | object |  | Only return prices with these recurring fields. |
| `recurring.interval` | enum: `day`, `month`, `week`, `year` |  |  |
| `recurring.meter` | string |  |  |
| `recurring.usage_type` | enum: `licensed`, `metered` |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | enum: `one_time`, `recurring` |  | Only return prices of type `recurring` or `one_time`. |

Returns: object

## POST /v1/prices

operationId: `PostPrices`

Creates a new price for an existing product. The price can be recurring or one-time.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the price can be used for new purchases. Defaults to `true`. |
| `billing_scheme` | enum: `per_unit`, `tiered` |  | Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `currency_options` | map (key → value) |  | Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `custom_unit_amount` | object |  | When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links. |
| `custom_unit_amount.enabled` | boolean | yes |  |
| `custom_unit_amount.maximum` | integer |  |  |
| `custom_unit_amount.minimum` | integer |  |  |
| `custom_unit_amount.preset` | integer |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `lookup_key` | string |  | A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nickname` | string |  | A brief description of the price, hidden from customers. |
| `product` | string |  | The ID of the product that this price will belong to. |
| `product_data` | object |  | These fields can be used to create a new product that this price will belong to. |
| `product_data.active` | boolean |  |  |
| `product_data.id` | string |  |  |
| `product_data.metadata` | map (key → value) |  |  |
| `product_data.name` | string | yes |  |
| `product_data.statement_descriptor` | string |  |  |
| `product_data.tax_code` | string |  |  |
| `product_data.unit_label` | string |  |  |
| `recurring` | object |  | The recurring components of a price such as `interval` and `usage_type`. |
| `recurring.aggregate_usage` | enum: `last_during_period`, `last_ever`, `max`, `sum` |  |  |
| `recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `recurring.interval_count` | integer |  |  |
| `recurring.meter` | string |  |  |
| `recurring.usage_type` | enum: `licensed`, `metered` |  |  |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `tiers` | array of object |  | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`. |
| `tiers[].flat_amount` | integer |  |  |
| `tiers[].flat_amount_decimal` | string |  |  |
| `tiers[].unit_amount` | integer |  |  |
| `tiers[].unit_amount_decimal` | string |  |  |
| `tiers[].up_to` | enum: `inf` or integer | yes |  |
| `tiers_mode` | enum: `graduated`, `volume` |  | Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows. |
| `transfer_lookup_key` | boolean |  | If set to true, will atomically remove the lookup key from the existing price, and assign it to this price. |
| `transform_quantity` | object |  | Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`. |
| `transform_quantity.divide_by` | integer | yes |  |
| `transform_quantity.round` | enum: `down`, `up` | yes |  |
| `unit_amount` | integer |  | A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount` or `custom_unit_amount` is required, unless `billing_scheme=tiered`. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set. |

Returns: `price`

## GET /v1/prices/search

operationId: `GetPricesSearch`

Search for prices you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices). |

Returns: object

## GET /v1/prices/{price}

operationId: `GetPricesPrice`

Retrieves the price with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `price (path)` | string | yes |  |

Returns: `price`

## POST /v1/prices/{price}

operationId: `PostPricesPrice`

Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `price (path)` | string | yes |  |
| `active` | boolean |  | Whether the price can be used for new purchases. Defaults to `true`. |
| `currency_options` | map (key → value) or "" (to unset) |  | Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `lookup_key` | string |  | A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nickname` | string |  | A brief description of the price, hidden from customers. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `transfer_lookup_key` | boolean |  | If set to true, will atomically remove the lookup key from the existing price, and assign it to this price. |

Returns: `price`

# Objects returned

## The `price` object

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
[Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).

Expandable fields (pass `expand[]=<field>`): `currency_options`, `custom_unit_amount`, `product`, `recurring`, `tiers`, `transform_quantity`

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Whether the price can be used for new purchases. |
| `billing_scheme` | enum: `per_unit`, `tiered` | yes | Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `currency_options` | map (key → value) |  | Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `custom_unit_amount` | `custom_unit_amount` |  | When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `lookup_key` | string |  | A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `nickname` | string |  | A brief description of the price, hidden from customers. |
| `object` | enum: `price` | yes | String representing the object's type. Objects of the same type share the same value. |
| `product` | string or `product` or `deleted_product` | yes | The ID of the product this price is associated with. |
| `recurring` | `recurring` |  | The recurring components of a price such as `interval` and `usage_type`. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `tiers` | array of `price_tier` |  | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`. |
| `tiers_mode` | enum: `graduated`, `volume` |  | Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows. |
| `transform_quantity` | `transform_quantity` |  | Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`. |
| `type` | enum: `one_time`, `recurring` | yes | One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase. |
| `unit_amount` | integer |  | The unit amount in cents (or local equivalent) to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`. |
| `unit_amount_decimal` | string |  | The unit amount in cents (or local equivalent) to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`. |

