# Stripe API 2023-10-16 — invoiceitems

Operations under `/v1/invoiceitems` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/invoiceitems

operationId: `GetInvoiceitems`

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return invoice items that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string |  | Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `pending` | boolean |  | Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/invoiceitems

operationId: `PostInvoiceitems`

Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string | yes | The ID of the customer who will be billed when this invoice item is billed. |
| `description` | string |  | An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking. |
| `discountable` | boolean |  | Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. |
| `discounts` | array of object or "" (to unset) |  | The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string |  | The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `period` | object |  | The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details. |
| `period.end` | timestamp (Unix seconds) | yes |  |
| `period.start` | timestamp (Unix seconds) | yes |  |
| `price` | string |  | The ID of the price object. |
| `price_data` | object |  | Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. |
| `price_data.currency` | string | yes |  |
| `price_data.product` | string | yes |  |
| `price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `price_data.unit_amount` | integer |  |  |
| `price_data.unit_amount_decimal` | string |  |  |
| `quantity` | integer |  | Non-negative integer. The quantity of units for the invoice item. |
| `subscription` | string |  | The ID of a subscription to add this invoice item to. When left blank, the invoice item will be be added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `tax_code` | string or "" (to unset) |  | A [tax code](https://stripe.com/docs/tax/tax-categories) ID. |
| `tax_rates` | array of string |  | The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. |
| `unit_amount` | integer |  | The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount` will reduce the `amount_due` on the invoice. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set. |

Returns: `invoiceitem`

## GET /v1/invoiceitems/{invoiceitem}

operationId: `GetInvoiceitemsInvoiceitem`

Retrieves the invoice item with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoiceitem (path)` | string | yes |  |

Returns: `invoiceitem`

## POST /v1/invoiceitems/{invoiceitem}

operationId: `PostInvoiceitemsInvoiceitem`

Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoiceitem (path)` | string | yes |  |
| `amount` | integer |  | The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount. |
| `description` | string |  | An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking. |
| `discountable` | boolean |  | Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations. |
| `discounts` | array of object or "" (to unset) |  | The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `period` | object |  | The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details. |
| `period.end` | timestamp (Unix seconds) | yes |  |
| `period.start` | timestamp (Unix seconds) | yes |  |
| `price` | string |  | The ID of the price object. |
| `price_data` | object |  | Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. |
| `price_data.currency` | string | yes |  |
| `price_data.product` | string | yes |  |
| `price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `price_data.unit_amount` | integer |  |  |
| `price_data.unit_amount_decimal` | string |  |  |
| `quantity` | integer |  | Non-negative integer. The quantity of units for the invoice item. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `tax_code` | string or "" (to unset) |  | A [tax code](https://stripe.com/docs/tax/tax-categories) ID. |
| `tax_rates` | array of string or "" (to unset) |  | The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates. |
| `unit_amount` | integer |  | The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set. |

Returns: `invoiceitem`

## DELETE /v1/invoiceitems/{invoiceitem}

operationId: `DeleteInvoiceitemsInvoiceitem`

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoiceitem (path)` | string | yes |  |

Returns: `deleted_invoiceitem`

# Objects returned

## The `invoiceitem` object

Invoice Items represent the component lines of an [invoice](https://stripe.com/docs/api/invoices). An invoice item is added to an
invoice by creating or updating it with an `invoice` field, at which point it will be included as
[an invoice line item](https://stripe.com/docs/api/invoices/line_item) within
[invoice.lines](https://stripe.com/docs/api/invoices/object#invoice_object-lines).

Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined
with a [subscription](https://stripe.com/docs/api/subscriptions). Sometimes you want to add a charge or credit to a customer, but actually charge
or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges
(to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

Related guides: [Integrate with the Invoicing API](https://stripe.com/docs/invoicing/integration), [Subscription Invoices](https://stripe.com/docs/billing/invoices/subscription#adding-upcoming-invoice-items).

Expandable fields (pass `expand[]=<field>`): `customer`, `discounts`, `invoice`, `period`, `price`, `subscription`, `tax_rates`, `test_clock`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` or `deleted_customer` | yes | The ID of the customer who will be billed when this invoice item is billed. |
| `date` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `discountable` | boolean | yes | If true, discounts will apply to this invoice item. Always false for prorations. |
| `discounts` | array of string or `discount` |  | The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` |  | The ID of the invoice this invoice item belongs to. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `invoiceitem` | yes | String representing the object's type. Objects of the same type share the same value. |
| `period` | `invoice_line_item_period` | yes |  |
| `price` | `price` |  | The price of the invoice item. |
| `proration` | boolean | yes | Whether the invoice item was created automatically as a proration adjustment when the customer switched plans. |
| `quantity` | integer | yes | Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for. |
| `subscription` | string or `subscription` |  | The subscription that this invoice item has been created for, if any. |
| `subscription_item` | string |  | The subscription item that this invoice item has been created for, if any. |
| `tax_rates` | array of `tax_rate` |  | The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this invoice item belongs to. |
| `unit_amount` | integer |  | Unit amount (in the `currency` specified) of the invoice item. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but contains a decimal value with at most 12 decimal places. |

## The `deleted_invoiceitem` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `invoiceitem` | yes | String representing the object's type. Objects of the same type share the same value. |

