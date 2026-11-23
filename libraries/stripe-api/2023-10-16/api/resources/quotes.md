# Stripe API 2023-10-16 — quotes

Operations under `/v1/quotes` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/quotes

operationId: `GetQuotes`

Returns a list of your quotes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer` | string |  | The ID of the customer whose quotes will be retrieved. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `accepted`, `canceled`, `draft`, `open` |  | The status of the quote. |
| `test_clock` | string |  | Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set. |

Returns: object

## POST /v1/quotes

operationId: `PostQuotes`

A quote models prices and services for a customer. Default options for `header`, `description`, `footer`, and `expires_at` can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `application_fee_amount` | integer or "" (to unset) |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field. |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field. |
| `automatic_tax` | object |  | Settings for automatic tax lookup for this quote and resulting invoices and subscriptions. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `customer` | string |  | The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed. |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any line item that does not have `tax_rates` set. |
| `description` | string or "" (to unset) |  | A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used. |
| `discounts` | array of object or "" (to unset) |  | The discounts applied to the quote. You can only set up to one discount. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used. |
| `footer` | string or "" (to unset) |  | A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used. |
| `from_quote` | object |  | Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`. |
| `from_quote.is_revision` | boolean |  |  |
| `from_quote.quote` | string | yes |  |
| `header` | string or "" (to unset) |  | A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.days_until_due` | integer |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `line_items` | array of object |  | A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost. |
| `line_items[].discounts` | array of object or "" (to unset) |  |  |
| `line_items[].discounts[].coupon` | string |  |  |
| `line_items[].discounts[].discount` | string |  |  |
| `line_items[].discounts[].promotion_code` | string |  |  |
| `line_items[].price` | string |  |  |
| `line_items[].price_data` | object |  |  |
| `line_items[].price_data.currency` | string | yes |  |
| `line_items[].price_data.product` | string | yes |  |
| `line_items[].price_data.recurring` | object |  |  |
| `line_items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `line_items[].price_data.recurring.interval_count` | integer |  |  |
| `line_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `line_items[].price_data.unit_amount` | integer |  |  |
| `line_items[].price_data.unit_amount_decimal` | string |  |  |
| `line_items[].quantity` | integer |  |  |
| `line_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `on_behalf_of` | string or "" (to unset) |  | The account on behalf of which to charge. |
| `subscription_data` | object |  | When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created. |
| `subscription_data.description` | string |  |  |
| `subscription_data.effective_date` | enum: `current_period_end` or timestamp (Unix seconds) or "" (to unset) |  |  |
| `subscription_data.metadata` | map (key → value) |  |  |
| `subscription_data.trial_period_days` | integer or "" (to unset) |  |  |
| `test_clock` | string |  | ID of the test clock to attach to the quote. |
| `transfer_data` | object or "" (to unset) |  | The data with which to automatically create a Transfer for each of the invoices. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |

Returns: `quote`

## GET /v1/quotes/{quote}

operationId: `GetQuotesQuote`

Retrieves the quote with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `quote (path)` | string | yes |  |

Returns: `quote`

## POST /v1/quotes/{quote}

operationId: `PostQuotesQuote`

A quote models prices and services for a customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `quote (path)` | string | yes |  |
| `application_fee_amount` | integer or "" (to unset) |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field. |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field. |
| `automatic_tax` | object |  | Settings for automatic tax lookup for this quote and resulting invoices and subscriptions. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `customer` | string |  | The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed. |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any line item that does not have `tax_rates` set. |
| `description` | string or "" (to unset) |  | A description that will be displayed on the quote PDF. |
| `discounts` | array of object or "" (to unset) |  | The discounts applied to the quote. You can only set up to one discount. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. |
| `footer` | string or "" (to unset) |  | A footer that will be displayed on the quote PDF. |
| `header` | string or "" (to unset) |  | A header that will be displayed on the quote PDF. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.days_until_due` | integer |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `line_items` | array of object |  | A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost. |
| `line_items[].discounts` | array of object or "" (to unset) |  |  |
| `line_items[].discounts[].coupon` | string |  |  |
| `line_items[].discounts[].discount` | string |  |  |
| `line_items[].discounts[].promotion_code` | string |  |  |
| `line_items[].id` | string |  |  |
| `line_items[].price` | string |  |  |
| `line_items[].price_data` | object |  |  |
| `line_items[].price_data.currency` | string | yes |  |
| `line_items[].price_data.product` | string | yes |  |
| `line_items[].price_data.recurring` | object |  |  |
| `line_items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `line_items[].price_data.recurring.interval_count` | integer |  |  |
| `line_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `line_items[].price_data.unit_amount` | integer |  |  |
| `line_items[].price_data.unit_amount_decimal` | string |  |  |
| `line_items[].quantity` | integer |  |  |
| `line_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `on_behalf_of` | string or "" (to unset) |  | The account on behalf of which to charge. |
| `subscription_data` | object |  | When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created. |
| `subscription_data.description` | string or "" (to unset) |  |  |
| `subscription_data.effective_date` | enum: `current_period_end` or timestamp (Unix seconds) or "" (to unset) |  |  |
| `subscription_data.metadata` | map (key → value) |  |  |
| `subscription_data.trial_period_days` | integer or "" (to unset) |  |  |
| `transfer_data` | object or "" (to unset) |  | The data with which to automatically create a Transfer for each of the invoices. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |

Returns: `quote`

## POST /v1/quotes/{quote}/accept

operationId: `PostQuotesQuoteAccept`

Accepts the specified quote.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `quote (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `quote`

## POST /v1/quotes/{quote}/cancel

operationId: `PostQuotesQuoteCancel`

Cancels the quote.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `quote (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `quote`

## GET /v1/quotes/{quote}/computed_upfront_line_items

operationId: `GetQuotesQuoteComputedUpfrontLineItems`

When retrieving a quote, there is an includable [**computed.upfront.line_items**](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `quote (path)` | string | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/quotes/{quote}/finalize

operationId: `PostQuotesQuoteFinalize`

Finalizes the quote.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `quote (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. |

Returns: `quote`

## GET /v1/quotes/{quote}/line_items

operationId: `GetQuotesQuoteLineItems`

When retrieving a quote, there is an includable **line_items** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `quote (path)` | string | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/quotes/{quote}/pdf

operationId: `GetQuotesQuotePdf`

Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.corp.stripe.com/quotes/overview#quote_pdf)

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `quote (path)` | string | yes |  |

Returns: see spec

# Objects returned

## The `quote` object

A Quote is a way to model prices that you'd like to provide to a customer.
Once accepted, it will automatically create an invoice, subscription or subscription schedule.

Expandable fields (pass `expand[]=<field>`): `application`, `automatic_tax`, `computed`, `customer`, `default_tax_rates`, `discounts`, `from_quote`, `invoice`, `invoice_settings`, `line_items`, `on_behalf_of`, `status_transitions`, `subscription`, `subscription_data`, `subscription_schedule`, `test_clock`, `total_details`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_subtotal` | integer | yes | Total before any discounts or taxes are applied. |
| `amount_total` | integer | yes | Total after discounts and taxes are applied. |
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the quote. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote. |
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote. |
| `automatic_tax` | `quotes_resource_automatic_tax` | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` | yes | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `computed` | `quotes_resource_computed` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` or `deleted_customer` |  | The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed. |
| `default_tax_rates` | array of string or `tax_rate` |  | The tax rates applied to this quote. |
| `description` | string |  | A description that will be displayed on the quote PDF. |
| `discounts` | array of string or `discount` | yes | The discounts applied to this quote. |
| `expires_at` | timestamp (Unix seconds) | yes | The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. |
| `footer` | string |  | A footer that will be displayed on the quote PDF. |
| `from_quote` | `quotes_resource_from_quote` |  | Details of the quote that was cloned. See the [cloning documentation](https://stripe.com/docs/quotes/clone) for more details. |
| `header` | string |  | A header that will be displayed on the quote PDF. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` or `deleted_invoice` |  | The invoice that was created from this quote. |
| `invoice_settings` | `invoice_setting_quote_setting` | yes |  |
| `line_items` | object |  | A list of items the customer is being quoted for. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `number` | string |  | A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize). |
| `object` | enum: `quote` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details. |
| `status` | enum: `accepted`, `canceled`, `draft`, `open` | yes | The status of the quote. |
| `status_transitions` | `quotes_resource_status_transitions` | yes |  |
| `subscription` | string or `subscription` |  | The subscription that was created or updated from this quote. |
| `subscription_data` | `quotes_resource_subscription_data_subscription_data` | yes |  |
| `subscription_schedule` | string or `subscription_schedule` |  | The subscription schedule that was created or updated from this quote. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this quote belongs to. |
| `total_details` | `quotes_resource_total_details` | yes |  |
| `transfer_data` | `quotes_resource_transfer_data` |  | The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices. |

