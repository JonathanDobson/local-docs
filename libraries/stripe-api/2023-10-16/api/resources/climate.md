# Stripe API 2023-10-16 — climate

Operations under `/v1/climate` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/climate/orders

operationId: `GetClimateOrders`

Lists all Climate order objects. The orders are returned sorted by creation date, with the
most recently created orders appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/climate/orders

operationId: `PostClimateOrders`

Creates a Climate order object for a given Climate product. The order will be processed immediately
after creation and payment will be deducted your Stripe balance.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | Requested amount of carbon removal units. Either this or `metric_tons` must be specified. |
| `beneficiary` | object |  | Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set. |
| `beneficiary.public_name` | string | yes |  |
| `currency` | string |  | Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `metric_tons` | string |  | Requested number of tons for the order. Either this or `amount` must be specified. |
| `product` | string | yes | Unique identifier of the Climate product. |

Returns: `climate.order`

## GET /v1/climate/orders/{order}

operationId: `GetClimateOrdersOrder`

Retrieves the details of a Climate order object with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `order (path)` | string | yes | Unique identifier of the order. |

Returns: `climate.order`

## POST /v1/climate/orders/{order}

operationId: `PostClimateOrdersOrder`

Updates the specified order by setting the values of the parameters passed.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `order (path)` | string | yes | Unique identifier of the order. |
| `beneficiary` | object or "" (to unset) |  | Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set. |
| `beneficiary.public_name` | string or "" (to unset) | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `climate.order`

## POST /v1/climate/orders/{order}/cancel

operationId: `PostClimateOrdersOrderCancel`

Cancels a Climate order. You can cancel an order within 30 days of creation. Stripe refunds the
reservation `amount_subtotal`, but not the `amount_fees` for user-triggered cancellations. Frontier
might cancel reservations if suppliers fail to deliver. If Frontier cancels the reservation, Stripe
provides 90 days advance notice and refunds the `amount_total`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `order (path)` | string | yes | Unique identifier of the order. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `climate.order`

## GET /v1/climate/products

operationId: `GetClimateProducts`

Lists all available Climate product objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/climate/products/{product}

operationId: `GetClimateProductsProduct`

Retrieves the details of a Climate product with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `product (path)` | string | yes |  |

Returns: `climate.product`

## GET /v1/climate/suppliers

operationId: `GetClimateSuppliers`

Lists all available Climate supplier objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/climate/suppliers/{supplier}

operationId: `GetClimateSuppliersSupplier`

Retrieves a Climate supplier object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `supplier (path)` | string | yes |  |

Returns: `climate.supplier`

# Objects returned

## The `climate.order` object

Orders represent your intent to purchase a particular Climate product. When you create an order, the
payment is deducted from your merchant balance.

Expandable fields (pass `expand[]=<field>`): `beneficiary`, `delivery_details`, `product`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_fees` | integer | yes | Total amount of [Frontier](https://frontierclimate.com/)'s service fees in the currency's smallest unit. |
| `amount_subtotal` | integer | yes | Total amount of the carbon removal in the currency's smallest unit. |
| `amount_total` | integer | yes | Total amount of the order including fees in the currency's smallest unit. |
| `beneficiary` | `climate_removals_beneficiary` |  |  |
| `canceled_at` | timestamp (Unix seconds) |  | Time at which the order was canceled. Measured in seconds since the Unix epoch. |
| `cancellation_reason` | enum: `expired`, `product_unavailable`, `requested` |  | Reason for the cancellation of this order. |
| `certificate` | string |  | For delivered orders, a URL to a delivery certificate for the order. |
| `confirmed_at` | timestamp (Unix seconds) |  | Time at which the order was confirmed. Measured in seconds since the Unix epoch. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase, representing the currency for this order. |
| `delayed_at` | timestamp (Unix seconds) |  | Time at which the order's expected_delivery_year was delayed. Measured in seconds since the Unix epoch. |
| `delivered_at` | timestamp (Unix seconds) |  | Time at which the order was delivered. Measured in seconds since the Unix epoch. |
| `delivery_details` | array of `climate_removals_order_deliveries` | yes | Details about the delivery of carbon removal for this order. |
| `expected_delivery_year` | integer | yes | The year this order is expected to be delivered. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `metric_tons` | string | yes | Quantity of carbon removal that is included in this order. |
| `object` | enum: `climate.order` | yes | String representing the object's type. Objects of the same type share the same value. |
| `product` | string or `climate.product` | yes | Unique ID for the Climate `Product` this order is purchasing. |
| `product_substituted_at` | timestamp (Unix seconds) |  | Time at which the order's product was substituted for a different product. Measured in seconds since the Unix epoch. |
| `status` | enum: `awaiting_funds`, `canceled`, `confirmed`, `delivered`, `open` | yes | The current status of this order. |

## The `climate.product` object

A Climate product represents a type of carbon removal unit available for reservation.
You can retrieve it to see the current price and availability.

Expandable fields (pass `expand[]=<field>`): `current_prices_per_metric_ton`, `suppliers`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `current_prices_per_metric_ton` | map (key → value) | yes | Current prices for a metric ton of carbon removal in a currency's smallest unit. |
| `delivery_year` | integer |  | The year in which the carbon removal is expected to be delivered. |
| `id` | string | yes | Unique identifier for the object. For convenience, Climate product IDs are human-readable strings that start with `climsku_`. See [carbon removal inventory](https://stripe.com/docs/climate/orders/carbon-removal-inventory) for a list of available carbon removal products. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metric_tons_available` | string | yes | The quantity of metric tons available for reservation. |
| `name` | string | yes | The Climate product's name. |
| `object` | enum: `climate.product` | yes | String representing the object's type. Objects of the same type share the same value. |
| `suppliers` | array of `climate.supplier` | yes | The carbon removal suppliers that fulfill orders for this Climate product. |

## The `climate.supplier` object

A supplier of carbon removal.

Expandable fields (pass `expand[]=<field>`): `locations`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique identifier for the object. |
| `info_url` | string | yes | Link to a webpage to learn more about the supplier. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `locations` | array of `climate_removals_location` | yes | The locations in which this supplier operates. |
| `name` | string | yes | Name of this carbon removal supplier. |
| `object` | enum: `climate.supplier` | yes | String representing the object’s type. Objects of the same type share the same value. |
| `removal_pathway` | enum: `biomass_carbon_removal_and_storage`, `direct_air_capture`, `enhanced_weathering` | yes | The scientific pathway used for carbon removal. |

