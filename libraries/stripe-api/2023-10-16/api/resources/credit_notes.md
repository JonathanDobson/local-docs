# Stripe API 2023-10-16 — credit notes

Operations under `/v1/credit_notes` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/credit_notes

operationId: `GetCreditNotes`

Returns a list of credit notes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return credit notes that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return credit notes for the customer specified by this customer ID. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string |  | Only return credit notes for the invoice specified by this invoice ID. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/credit_notes

operationId: `PostCreditNotes`

Issue a credit note to adjust the amount of a finalized invoice. For a `status=open` invoice, a credit note reduces
its `amount_due`. For a `status=paid` invoice, a credit note does not affect its `amount_due`. Instead, it can result
in any combination of the following:

- Refund: create a new refund (using `refund_amount`) or link an existing refund (using `refund`).

- Customer balance credit: credit the customer’s balance (using `credit_amount`) which will be automatically applied to their next invoice when it’s finalized.

- Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using `out_of_band_amount`).

For post-payment credit notes the sum of the refund, credit and outside of Stripe amounts must equal the credit note total.

You may issue multiple credit notes for an invoice. Each credit note will increment the invoice’s `pre_payment_credit_notes_amount`
or `post_payment_credit_notes_amount` depending on its `status` at the time of credit note creation.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The integer amount in cents (or local equivalent) representing the total amount of the credit note. |
| `credit_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string | yes | ID of the invoice. |
| `lines` | array of object |  | Line items that make up the credit note. |
| `lines[].amount` | integer |  |  |
| `lines[].description` | string |  |  |
| `lines[].invoice_line_item` | string |  |  |
| `lines[].quantity` | integer |  |  |
| `lines[].tax_amounts` | array of object or "" (to unset) |  |  |
| `lines[].tax_amounts[].amount` | integer | yes |  |
| `lines[].tax_amounts[].tax_rate` | string | yes |  |
| `lines[].tax_amounts[].taxable_amount` | integer | yes |  |
| `lines[].tax_rates` | array of string or "" (to unset) |  |  |
| `lines[].type` | enum: `custom_line_item`, `invoice_line_item` | yes |  |
| `lines[].unit_amount` | integer |  |  |
| `lines[].unit_amount_decimal` | string |  |  |
| `memo` | string |  | The credit note's memo appears on the credit note PDF. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `out_of_band_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe. |
| `reason` | enum: `duplicate`, `fraudulent`, `order_change`, `product_unsatisfactory` |  | Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory` |
| `refund` | string |  | ID of an existing refund to link this credit note to. |
| `refund_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice. |
| `shipping_cost` | object |  | When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note. |
| `shipping_cost.shipping_rate` | string |  |  |

Returns: `credit_note`

## GET /v1/credit_notes/preview

operationId: `GetCreditNotesPreview`

Get a preview of a credit note without creating it.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The integer amount in cents (or local equivalent) representing the total amount of the credit note. |
| `credit_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string | yes | ID of the invoice. |
| `lines` | array of object |  | Line items that make up the credit note. |
| `lines[].amount` | integer |  |  |
| `lines[].description` | string |  |  |
| `lines[].invoice_line_item` | string |  |  |
| `lines[].quantity` | integer |  |  |
| `lines[].tax_amounts` | array of object or "" (to unset) |  |  |
| `lines[].tax_amounts[].amount` | integer | yes |  |
| `lines[].tax_amounts[].tax_rate` | string | yes |  |
| `lines[].tax_amounts[].taxable_amount` | integer | yes |  |
| `lines[].tax_rates` | array of string or "" (to unset) |  |  |
| `lines[].type` | enum: `custom_line_item`, `invoice_line_item` | yes |  |
| `lines[].unit_amount` | integer |  |  |
| `lines[].unit_amount_decimal` | string |  |  |
| `memo` | string |  | The credit note's memo appears on the credit note PDF. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `out_of_band_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe. |
| `reason` | enum: `duplicate`, `fraudulent`, `order_change`, `product_unsatisfactory` |  | Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory` |
| `refund` | string |  | ID of an existing refund to link this credit note to. |
| `refund_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice. |
| `shipping_cost` | object |  | When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note. |
| `shipping_cost.shipping_rate` | string |  |  |

Returns: `credit_note`

## GET /v1/credit_notes/preview/lines

operationId: `GetCreditNotesPreviewLines`

When retrieving a credit note preview, you’ll get a **lines** property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The integer amount in cents (or local equivalent) representing the total amount of the credit note. |
| `credit_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice` | string | yes | ID of the invoice. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `lines` | array of object |  | Line items that make up the credit note. |
| `lines[].amount` | integer |  |  |
| `lines[].description` | string |  |  |
| `lines[].invoice_line_item` | string |  |  |
| `lines[].quantity` | integer |  |  |
| `lines[].tax_amounts` | array of object or "" (to unset) |  |  |
| `lines[].tax_amounts[].amount` | integer | yes |  |
| `lines[].tax_amounts[].tax_rate` | string | yes |  |
| `lines[].tax_amounts[].taxable_amount` | integer | yes |  |
| `lines[].tax_rates` | array of string or "" (to unset) |  |  |
| `lines[].type` | enum: `custom_line_item`, `invoice_line_item` | yes |  |
| `lines[].unit_amount` | integer |  |  |
| `lines[].unit_amount_decimal` | string |  |  |
| `memo` | string |  | The credit note's memo appears on the credit note PDF. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `out_of_band_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe. |
| `reason` | enum: `duplicate`, `fraudulent`, `order_change`, `product_unsatisfactory` |  | Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory` |
| `refund` | string |  | ID of an existing refund to link this credit note to. |
| `refund_amount` | integer |  | The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice. |
| `shipping_cost` | object |  | When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note. |
| `shipping_cost.shipping_rate` | string |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/credit_notes/{credit_note}/lines

operationId: `GetCreditNotesCreditNoteLines`

When retrieving a credit note, you’ll get a **lines** property containing the the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `credit_note (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/credit_notes/{id}

operationId: `GetCreditNotesId`

Retrieves the credit note object with the given identifier.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `credit_note`

## POST /v1/credit_notes/{id}

operationId: `PostCreditNotesId`

Updates an existing credit note.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `memo` | string |  | Credit note memo. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `credit_note`

## POST /v1/credit_notes/{id}/void

operationId: `PostCreditNotesIdVoid`

Marks a credit note as void. Learn more about [voiding credit notes](https://stripe.com/docs/billing/invoices/credit-notes#voiding).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `credit_note`

# Objects returned

## The `credit_note` object

Issue a credit note to adjust an invoice's amount after the invoice is finalized.

Related guide: [Credit notes](https://stripe.com/docs/billing/invoices/credit-notes)

Expandable fields (pass `expand[]=<field>`): `customer`, `customer_balance_transaction`, `discount_amounts`, `invoice`, `lines`, `refund`, `shipping_cost`, `tax_amounts`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The integer amount in cents (or local equivalent) representing the total amount of the credit note, including tax. |
| `amount_shipping` | integer | yes | This is the sum of all the shipping amounts. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` or `deleted_customer` | yes | ID of the customer. |
| `customer_balance_transaction` | string or `customer_balance_transaction` |  | Customer balance transaction related to this credit note. |
| `discount_amount` | integer | yes | The integer amount in cents (or local equivalent) representing the total amount of discount that was credited. |
| `discount_amounts` | array of `discounts_resource_discount_amount` | yes | The aggregate amounts calculated per discount for all line items. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` | yes | ID of the invoice. |
| `lines` | object | yes | Line items that make up the credit note |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `memo` | string |  | Customer-facing text that appears on the credit note PDF. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `number` | string | yes | A unique number that identifies this particular credit note and appears on the PDF of the credit note and its associated invoice. |
| `object` | enum: `credit_note` | yes | String representing the object's type. Objects of the same type share the same value. |
| `out_of_band_amount` | integer |  | Amount that was credited outside of Stripe. |
| `pdf` | string | yes | The link to download the PDF of the credit note. |
| `reason` | enum: `duplicate`, `fraudulent`, `order_change`, `product_unsatisfactory` |  | Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory` |
| `refund` | string or `refund` |  | Refund related to this credit note. |
| `shipping_cost` | `invoices_resource_shipping_cost` |  | The details of the cost of shipping, including the ShippingRate applied to the invoice. |
| `status` | enum: `issued`, `void` | yes | Status of this credit note, one of `issued` or `void`. Learn more about [voiding credit notes](https://stripe.com/docs/billing/invoices/credit-notes#voiding). |
| `subtotal` | integer | yes | The integer amount in cents (or local equivalent) representing the amount of the credit note, excluding exclusive tax and invoice level discounts. |
| `subtotal_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the amount of the credit note, excluding all tax and invoice level discounts. |
| `tax_amounts` | array of `credit_note_tax_amount` | yes | The aggregate amounts calculated per tax rate for all line items. |
| `total` | integer | yes | The integer amount in cents (or local equivalent) representing the total amount of the credit note, including tax and all discount. |
| `total_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the total amount of the credit note, excluding tax, but including discounts. |
| `type` | enum: `post_payment`, `pre_payment` | yes | Type of this credit note, one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid. |
| `voided_at` | timestamp (Unix seconds) |  | The time that the credit note was voided. |

