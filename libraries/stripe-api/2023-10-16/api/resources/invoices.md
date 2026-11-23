# Stripe API 2023-10-16 — invoices

Operations under `/v1/invoices` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/invoices

operationId: `GetInvoices`

You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`. |
| `created` | object or integer |  | Only return invoices that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return invoices for the customer specified by this customer ID. |
| `due_date` | object or integer |  |  |
| `due_date.gt` | integer |  |  |
| `due_date.gte` | integer |  |  |
| `due_date.lt` | integer |  |  |
| `due_date.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `draft`, `open`, `paid`, `uncollectible`, `void` |  | The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview) |
| `subscription` | string |  | Only return invoices for the subscription specified by this subscription ID. |

Returns: object

## POST /v1/invoices

operationId: `PostInvoices`

This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you [finalize](#finalize_invoice) the invoice, which allows you to [pay](#pay_invoice) or [send](#send_invoice) the invoice to your customers.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account_tax_ids` | array of string or "" (to unset) |  | The account tax IDs associated with the invoice. Only editable when the invoice is a draft. |
| `application_fee_amount` | integer |  | A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees). |
| `auto_advance` | boolean |  | Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action. |
| `automatic_tax` | object |  | Settings for automatic tax lookup for this invoice. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`. |
| `currency` | string |  | The currency to create this invoice in. Defaults to that of `customer` if not specified. |
| `custom_fields` | array of object or "" (to unset) |  | A list of up to 4 custom fields to be displayed on the invoice. |
| `custom_fields[].name` | string | yes |  |
| `custom_fields[].value` | string | yes |  |
| `customer` | string |  | The ID of the customer who will be billed. |
| `days_until_due` | integer |  | The number of days from when the invoice is created until it is due. Valid only for invoices where `collection_method=send_invoice`. |
| `default_payment_method` | string |  | ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings. |
| `default_source` | string |  | ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source. |
| `default_tax_rates` | array of string |  | The tax rates that will apply to any line item that does not have `tax_rates` set. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard. |
| `discounts` | array of object or "" (to unset) |  | The coupons and promotion codes to redeem into discounts for the invoice. If not specified, inherits the discount from the invoice's customer. Pass an empty string to avoid inheriting any discounts. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `due_date` | timestamp (Unix seconds) |  | The date on which payment for this invoice is due. Valid only for invoices where `collection_method=send_invoice`. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `footer` | string |  | Footer to be displayed on the invoice. |
| `from_invoice` | object |  | Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details. |
| `from_invoice.action` | enum: `revision` | yes |  |
| `from_invoice.invoice` | string | yes |  |
| `issuer` | object |  | The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account. |
| `issuer.account` | string |  |  |
| `issuer.type` | enum: `account`, `self` | yes |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `number` | string |  | Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically. |
| `on_behalf_of` | string |  | The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details. |
| `payment_settings` | object |  | Configuration settings for the PaymentIntent that is generated when the invoice is finalized. |
| `payment_settings.default_mandate` | string or "" (to unset) |  |  |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.installments` | object |  |  |
| `payment_settings.payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_settings.payment_method_options.card.installments.plan` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.installments.plan.count` | integer | yes |  |
| `payment_settings.payment_method_options.card.installments.plan.interval` | enum: `month` | yes |  |
| `payment_settings.payment_method_options.card.installments.plan.type` | enum: `fixed_count` | yes |  |
| `payment_settings.payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_settings.payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.type` | string |  |  |
| `payment_settings.payment_method_options.customer_balance.funding_type` | string |  |  |
| `payment_settings.payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` or "" (to unset) |  |  |
| `pending_invoice_items_behavior` | enum: `exclude`, `include` |  | How to handle pending invoice items on invoice creation. Defaults to `exclude` if the parameter is omitted. |
| `rendering` | object |  | The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page. |
| `rendering.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `rendering.pdf` | object |  |  |
| `rendering.pdf.page_size` | enum: `a4`, `auto`, `letter` |  |  |
| `shipping_cost` | object |  | Settings for the cost of shipping for this invoice. |
| `shipping_cost.shipping_rate` | string |  |  |
| `shipping_cost.shipping_rate_data` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum.value` | integer | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum.value` | integer | yes |  |
| `shipping_cost.shipping_rate_data.display_name` | string | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount` | object |  |  |
| `shipping_cost.shipping_rate_data.fixed_amount.amount` | integer | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount.currency` | string | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount.currency_options` | map (key → value) |  |  |
| `shipping_cost.shipping_rate_data.metadata` | map (key → value) |  |  |
| `shipping_cost.shipping_rate_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `shipping_cost.shipping_rate_data.tax_code` | string |  |  |
| `shipping_cost.shipping_rate_data.type` | enum: `fixed_amount` |  |  |
| `shipping_details` | object |  | Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer. |
| `shipping_details.address` | object | yes |  |
| `shipping_details.address.city` | string |  |  |
| `shipping_details.address.country` | string |  |  |
| `shipping_details.address.line1` | string |  |  |
| `shipping_details.address.line2` | string |  |  |
| `shipping_details.address.postal_code` | string |  |  |
| `shipping_details.address.state` | string |  |  |
| `shipping_details.name` | string | yes |  |
| `shipping_details.phone` | string or "" (to unset) |  |  |
| `statement_descriptor` | string |  | Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`. |
| `subscription` | string |  | The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription's billing cycle and regular subscription events won't be affected. |
| `transfer_data` | object |  | If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.destination` | string | yes |  |

Returns: `invoice`

## GET /v1/invoices/search

operationId: `GetInvoicesSearch`

Search for invoices you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices). |

Returns: object

## GET /v1/invoices/upcoming

operationId: `GetInvoicesUpcoming`

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the `subscription_proration_date` parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where `period[start]` is equal to the `subscription_proration_date` value passed in the request.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `automatic_tax` | object |  | Settings for automatic tax lookup for this invoice preview. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `coupon` | string |  | The ID of the coupon to apply to this phase of the subscription schedule. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `currency` | string |  | The currency to preview this invoice in. Defaults to that of `customer` if not specified. |
| `customer` | string |  | The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set. |
| `customer_details` | object |  | Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set. |
| `customer_details.address` | object or "" (to unset) |  |  |
| `customer_details.address.city` | string |  |  |
| `customer_details.address.country` | string |  |  |
| `customer_details.address.line1` | string |  |  |
| `customer_details.address.line2` | string |  |  |
| `customer_details.address.postal_code` | string |  |  |
| `customer_details.address.state` | string |  |  |
| `customer_details.shipping` | object or "" (to unset) |  |  |
| `customer_details.shipping.address` | object | yes |  |
| `customer_details.shipping.address.city` | string |  |  |
| `customer_details.shipping.address.country` | string |  |  |
| `customer_details.shipping.address.line1` | string |  |  |
| `customer_details.shipping.address.line2` | string |  |  |
| `customer_details.shipping.address.postal_code` | string |  |  |
| `customer_details.shipping.address.state` | string |  |  |
| `customer_details.shipping.name` | string | yes |  |
| `customer_details.shipping.phone` | string |  |  |
| `customer_details.tax` | object |  |  |
| `customer_details.tax.ip_address` | string or "" (to unset) |  |  |
| `customer_details.tax_exempt` | enum: ``, `exempt`, `none`, `reverse` |  |  |
| `customer_details.tax_ids` | array of object |  |  |
| `customer_details.tax_ids[].type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes |  |
| `customer_details.tax_ids[].value` | string | yes |  |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_items` | array of object |  | List of invoice items to add or update in the upcoming invoice preview. |
| `invoice_items[].amount` | integer |  |  |
| `invoice_items[].currency` | string |  |  |
| `invoice_items[].description` | string |  |  |
| `invoice_items[].discountable` | boolean |  |  |
| `invoice_items[].discounts` | array of object or "" (to unset) |  |  |
| `invoice_items[].discounts[].coupon` | string |  |  |
| `invoice_items[].discounts[].discount` | string |  |  |
| `invoice_items[].discounts[].promotion_code` | string |  |  |
| `invoice_items[].invoiceitem` | string |  |  |
| `invoice_items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `invoice_items[].period` | object |  |  |
| `invoice_items[].period.end` | timestamp (Unix seconds) | yes |  |
| `invoice_items[].period.start` | timestamp (Unix seconds) | yes |  |
| `invoice_items[].price` | string |  |  |
| `invoice_items[].price_data` | object |  |  |
| `invoice_items[].price_data.currency` | string | yes |  |
| `invoice_items[].price_data.product` | string | yes |  |
| `invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `invoice_items[].price_data.unit_amount` | integer |  |  |
| `invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `invoice_items[].quantity` | integer |  |  |
| `invoice_items[].tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `invoice_items[].tax_code` | string or "" (to unset) |  |  |
| `invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `invoice_items[].unit_amount` | integer |  |  |
| `invoice_items[].unit_amount_decimal` | string |  |  |
| `issuer` | object |  | The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account. |
| `issuer.account` | string |  |  |
| `issuer.type` | enum: `account`, `self` | yes |  |
| `on_behalf_of` | string or "" (to unset) |  | The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details. |
| `schedule` | string |  | The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields. |
| `subscription` | string |  | The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions. |
| `subscription_billing_cycle_anchor` | enum: `now`, `unchanged` or timestamp (Unix seconds) |  | For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`. |
| `subscription_cancel_at` | timestamp (Unix seconds) or "" (to unset) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `subscription_cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `subscription_cancel_now` | boolean |  | This simulates the subscription being canceled or expired immediately. |
| `subscription_default_tax_rates` | array of string or "" (to unset) |  | If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set. |
| `subscription_items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `subscription_items[].billing_thresholds` | object or "" (to unset) |  |  |
| `subscription_items[].billing_thresholds.usage_gte` | integer | yes |  |
| `subscription_items[].clear_usage` | boolean |  |  |
| `subscription_items[].deleted` | boolean |  |  |
| `subscription_items[].discounts` | array of object or "" (to unset) |  |  |
| `subscription_items[].discounts[].coupon` | string |  |  |
| `subscription_items[].discounts[].discount` | string |  |  |
| `subscription_items[].discounts[].promotion_code` | string |  |  |
| `subscription_items[].id` | string |  |  |
| `subscription_items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `subscription_items[].price` | string |  |  |
| `subscription_items[].price_data` | object |  |  |
| `subscription_items[].price_data.currency` | string | yes |  |
| `subscription_items[].price_data.product` | string | yes |  |
| `subscription_items[].price_data.recurring` | object | yes |  |
| `subscription_items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `subscription_items[].price_data.recurring.interval_count` | integer |  |  |
| `subscription_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `subscription_items[].price_data.unit_amount` | integer |  |  |
| `subscription_items[].price_data.unit_amount_decimal` | string |  |  |
| `subscription_items[].quantity` | integer |  |  |
| `subscription_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `subscription_proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `subscription_proration_date` | timestamp (Unix seconds) |  | If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration_behavior` cannot be set to 'none'. |
| `subscription_resume_at` | enum: `now` |  | For paused subscriptions, setting `subscription_resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed. |
| `subscription_start_date` | timestamp (Unix seconds) |  | Date a subscription is intended to start (can be future or past). |
| `subscription_trial_end` | enum: `now` or timestamp (Unix seconds) |  | If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required. |
| `subscription_trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |

Returns: `invoice`

## GET /v1/invoices/upcoming/lines

operationId: `GetInvoicesUpcomingLines`

When retrieving an upcoming invoice, you’ll get a **lines** property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `automatic_tax` | object |  | Settings for automatic tax lookup for this invoice preview. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `coupon` | string |  | The ID of the coupon to apply to this phase of the subscription schedule. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `currency` | string |  | The currency to preview this invoice in. Defaults to that of `customer` if not specified. |
| `customer` | string |  | The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set. |
| `customer_details` | object |  | Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set. |
| `customer_details.address` | object or "" (to unset) |  |  |
| `customer_details.address.city` | string |  |  |
| `customer_details.address.country` | string |  |  |
| `customer_details.address.line1` | string |  |  |
| `customer_details.address.line2` | string |  |  |
| `customer_details.address.postal_code` | string |  |  |
| `customer_details.address.state` | string |  |  |
| `customer_details.shipping` | object or "" (to unset) |  |  |
| `customer_details.shipping.address` | object | yes |  |
| `customer_details.shipping.address.city` | string |  |  |
| `customer_details.shipping.address.country` | string |  |  |
| `customer_details.shipping.address.line1` | string |  |  |
| `customer_details.shipping.address.line2` | string |  |  |
| `customer_details.shipping.address.postal_code` | string |  |  |
| `customer_details.shipping.address.state` | string |  |  |
| `customer_details.shipping.name` | string | yes |  |
| `customer_details.shipping.phone` | string |  |  |
| `customer_details.tax` | object |  |  |
| `customer_details.tax.ip_address` | string or "" (to unset) |  |  |
| `customer_details.tax_exempt` | enum: ``, `exempt`, `none`, `reverse` |  |  |
| `customer_details.tax_ids` | array of object |  |  |
| `customer_details.tax_ids[].type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes |  |
| `customer_details.tax_ids[].value` | string | yes |  |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_items` | array of object |  | List of invoice items to add or update in the upcoming invoice preview. |
| `invoice_items[].amount` | integer |  |  |
| `invoice_items[].currency` | string |  |  |
| `invoice_items[].description` | string |  |  |
| `invoice_items[].discountable` | boolean |  |  |
| `invoice_items[].discounts` | array of object or "" (to unset) |  |  |
| `invoice_items[].discounts[].coupon` | string |  |  |
| `invoice_items[].discounts[].discount` | string |  |  |
| `invoice_items[].discounts[].promotion_code` | string |  |  |
| `invoice_items[].invoiceitem` | string |  |  |
| `invoice_items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `invoice_items[].period` | object |  |  |
| `invoice_items[].period.end` | timestamp (Unix seconds) | yes |  |
| `invoice_items[].period.start` | timestamp (Unix seconds) | yes |  |
| `invoice_items[].price` | string |  |  |
| `invoice_items[].price_data` | object |  |  |
| `invoice_items[].price_data.currency` | string | yes |  |
| `invoice_items[].price_data.product` | string | yes |  |
| `invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `invoice_items[].price_data.unit_amount` | integer |  |  |
| `invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `invoice_items[].quantity` | integer |  |  |
| `invoice_items[].tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `invoice_items[].tax_code` | string or "" (to unset) |  |  |
| `invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `invoice_items[].unit_amount` | integer |  |  |
| `invoice_items[].unit_amount_decimal` | string |  |  |
| `issuer` | object |  | The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account. |
| `issuer.account` | string |  |  |
| `issuer.type` | enum: `account`, `self` | yes |  |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `on_behalf_of` | string or "" (to unset) |  | The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details. |
| `schedule` | string |  | The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `subscription` | string |  | The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions. |
| `subscription_billing_cycle_anchor` | enum: `now`, `unchanged` or timestamp (Unix seconds) |  | For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`. |
| `subscription_cancel_at` | timestamp (Unix seconds) or "" (to unset) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `subscription_cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `subscription_cancel_now` | boolean |  | This simulates the subscription being canceled or expired immediately. |
| `subscription_default_tax_rates` | array of string or "" (to unset) |  | If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set. |
| `subscription_items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `subscription_items[].billing_thresholds` | object or "" (to unset) |  |  |
| `subscription_items[].billing_thresholds.usage_gte` | integer | yes |  |
| `subscription_items[].clear_usage` | boolean |  |  |
| `subscription_items[].deleted` | boolean |  |  |
| `subscription_items[].discounts` | array of object or "" (to unset) |  |  |
| `subscription_items[].discounts[].coupon` | string |  |  |
| `subscription_items[].discounts[].discount` | string |  |  |
| `subscription_items[].discounts[].promotion_code` | string |  |  |
| `subscription_items[].id` | string |  |  |
| `subscription_items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `subscription_items[].price` | string |  |  |
| `subscription_items[].price_data` | object |  |  |
| `subscription_items[].price_data.currency` | string | yes |  |
| `subscription_items[].price_data.product` | string | yes |  |
| `subscription_items[].price_data.recurring` | object | yes |  |
| `subscription_items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `subscription_items[].price_data.recurring.interval_count` | integer |  |  |
| `subscription_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `subscription_items[].price_data.unit_amount` | integer |  |  |
| `subscription_items[].price_data.unit_amount_decimal` | string |  |  |
| `subscription_items[].quantity` | integer |  |  |
| `subscription_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `subscription_proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `subscription_proration_date` | timestamp (Unix seconds) |  | If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration_behavior` cannot be set to 'none'. |
| `subscription_resume_at` | enum: `now` |  | For paused subscriptions, setting `subscription_resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed. |
| `subscription_start_date` | timestamp (Unix seconds) |  | Date a subscription is intended to start (can be future or past). |
| `subscription_trial_end` | enum: `now` or timestamp (Unix seconds) |  | If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required. |
| `subscription_trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |

Returns: object

## GET /v1/invoices/{invoice}

operationId: `GetInvoicesInvoice`

Retrieves the invoice with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice (path)` | string | yes |  |

Returns: `invoice`

## POST /v1/invoices/{invoice}

operationId: `PostInvoicesInvoice`

Draft invoices are fully editable. Once an invoice is [finalized](https://stripe.com/docs/billing/invoices/workflow#finalized),
monetary values, as well as `collection_method`, become uneditable.

If you would like to stop the Stripe Billing engine from automatically finalizing, reattempting payments on,
sending reminders for, or [automatically reconciling](https://stripe.com/docs/billing/invoices/reconciliation) invoices, pass
`auto_advance=false`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `account_tax_ids` | array of string or "" (to unset) |  | The account tax IDs associated with the invoice. Only editable when the invoice is a draft. |
| `application_fee_amount` | integer |  | A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees). |
| `auto_advance` | boolean |  | Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. |
| `automatic_tax` | object |  | Settings for automatic tax lookup for this invoice. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically` or `send_invoice`. This field can be updated only on `draft` invoices. |
| `custom_fields` | array of object or "" (to unset) |  | A list of up to 4 custom fields to be displayed on the invoice. If a value for `custom_fields` is specified, the list specified will replace the existing custom field list on this invoice. Pass an empty string to remove previously-defined fields. |
| `custom_fields[].name` | string | yes |  |
| `custom_fields[].value` | string | yes |  |
| `days_until_due` | integer |  | The number of days from which the invoice is created until it is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices. |
| `default_payment_method` | string |  | ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings. |
| `default_source` | string or "" (to unset) |  | ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source. |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any line item that does not have `tax_rates` set. Pass an empty string to remove previously-defined tax rates. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard. |
| `discounts` | array of object or "" (to unset) |  | The discounts that will apply to the invoice. Pass an empty string to remove previously-defined discounts. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `due_date` | timestamp (Unix seconds) |  | The date on which payment for this invoice is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices. |
| `effective_at` | timestamp (Unix seconds) or "" (to unset) |  | The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `footer` | string |  | Footer to be displayed on the invoice. |
| `issuer` | object |  | The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account. |
| `issuer.account` | string |  |  |
| `issuer.type` | enum: `account`, `self` | yes |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `number` | string or "" (to unset) |  | Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically. |
| `on_behalf_of` | string or "" (to unset) |  | The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details. |
| `payment_settings` | object |  | Configuration settings for the PaymentIntent that is generated when the invoice is finalized. |
| `payment_settings.default_mandate` | string or "" (to unset) |  |  |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.installments` | object |  |  |
| `payment_settings.payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_settings.payment_method_options.card.installments.plan` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.installments.plan.count` | integer | yes |  |
| `payment_settings.payment_method_options.card.installments.plan.interval` | enum: `month` | yes |  |
| `payment_settings.payment_method_options.card.installments.plan.type` | enum: `fixed_count` | yes |  |
| `payment_settings.payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_settings.payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.type` | string |  |  |
| `payment_settings.payment_method_options.customer_balance.funding_type` | string |  |  |
| `payment_settings.payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` or "" (to unset) |  |  |
| `rendering` | object |  | The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page. |
| `rendering.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `rendering.pdf` | object |  |  |
| `rendering.pdf.page_size` | enum: `a4`, `auto`, `letter` |  |  |
| `shipping_cost` | object or "" (to unset) |  | Settings for the cost of shipping for this invoice. |
| `shipping_cost.shipping_rate` | string |  |  |
| `shipping_cost.shipping_rate_data` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.maximum.value` | integer | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum` | object |  |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_cost.shipping_rate_data.delivery_estimate.minimum.value` | integer | yes |  |
| `shipping_cost.shipping_rate_data.display_name` | string | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount` | object |  |  |
| `shipping_cost.shipping_rate_data.fixed_amount.amount` | integer | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount.currency` | string | yes |  |
| `shipping_cost.shipping_rate_data.fixed_amount.currency_options` | map (key → value) |  |  |
| `shipping_cost.shipping_rate_data.metadata` | map (key → value) |  |  |
| `shipping_cost.shipping_rate_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `shipping_cost.shipping_rate_data.tax_code` | string |  |  |
| `shipping_cost.shipping_rate_data.type` | enum: `fixed_amount` |  |  |
| `shipping_details` | object or "" (to unset) |  | Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer. |
| `shipping_details.address` | object | yes |  |
| `shipping_details.address.city` | string |  |  |
| `shipping_details.address.country` | string |  |  |
| `shipping_details.address.line1` | string |  |  |
| `shipping_details.address.line2` | string |  |  |
| `shipping_details.address.postal_code` | string |  |  |
| `shipping_details.address.state` | string |  |  |
| `shipping_details.name` | string | yes |  |
| `shipping_details.phone` | string or "" (to unset) |  |  |
| `statement_descriptor` | string |  | Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`. |
| `transfer_data` | object or "" (to unset) |  | If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge. This will be unset if you POST an empty value. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.destination` | string | yes |  |

Returns: `invoice`

## DELETE /v1/invoices/{invoice}

operationId: `DeleteInvoicesInvoice`

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be [voided](#void_invoice).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |

Returns: `deleted_invoice`

## POST /v1/invoices/{invoice}/finalize

operationId: `PostInvoicesInvoiceFinalize`

Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `auto_advance` | boolean |  | Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `invoice`

## GET /v1/invoices/{invoice}/lines

operationId: `GetInvoicesInvoiceLines`

When retrieving an invoice, you’ll get a **lines** property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice (path)` | string | yes |  |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/invoices/{invoice}/lines/{line_item_id}

operationId: `PostInvoicesInvoiceLinesLineItemId`

Updates an invoice’s line item. Some fields, such as `tax_amounts`, only live on the invoice line item,
so they can only be updated through this endpoint. Other fields, such as `amount`, live on both the invoice
item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.
Updating an invoice’s line item is only possible before the invoice is finalized.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes | Invoice ID of line item |
| `line_item_id (path)` | string | yes | Invoice line item ID |
| `amount` | integer |  | The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount. |
| `description` | string |  | An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking. |
| `discountable` | boolean |  | Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations. |
| `discounts` | array of object or "" (to unset) |  | The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts. |
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
| `price_data.product` | string |  |  |
| `price_data.product_data` | object |  |  |
| `price_data.product_data.description` | string |  |  |
| `price_data.product_data.images` | array of string |  |  |
| `price_data.product_data.metadata` | map (key → value) |  |  |
| `price_data.product_data.name` | string | yes |  |
| `price_data.product_data.tax_code` | string |  |  |
| `price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `price_data.unit_amount` | integer |  |  |
| `price_data.unit_amount_decimal` | string |  |  |
| `quantity` | integer |  | Non-negative integer. The quantity of units for the line item. |
| `tax_amounts` | array of object or "" (to unset) |  | A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://stripe.com/docs/api/invoices/object#invoice_object-default_tax_rates) or uses [automatic tax](https://stripe.com/docs/tax/invoicing). Pass an empty string to remove previously defined tax amounts. |
| `tax_amounts[].amount` | integer | yes |  |
| `tax_amounts[].tax_rate_data` | object | yes |  |
| `tax_amounts[].tax_rate_data.country` | string |  |  |
| `tax_amounts[].tax_rate_data.description` | string |  |  |
| `tax_amounts[].tax_rate_data.display_name` | string | yes |  |
| `tax_amounts[].tax_rate_data.inclusive` | boolean | yes |  |
| `tax_amounts[].tax_rate_data.jurisdiction` | string |  |  |
| `tax_amounts[].tax_rate_data.percentage` | number | yes |  |
| `tax_amounts[].tax_rate_data.state` | string |  |  |
| `tax_amounts[].tax_rate_data.tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` |  |  |
| `tax_amounts[].taxable_amount` | integer | yes |  |
| `tax_rates` | array of string or "" (to unset) |  | The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates. |

Returns: `line_item`

## POST /v1/invoices/{invoice}/mark_uncollectible

operationId: `PostInvoicesInvoiceMarkUncollectible`

Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `invoice`

## POST /v1/invoices/{invoice}/pay

operationId: `PostInvoicesInvoicePay`

Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `forgive` | boolean |  | In cases where the source used to pay the invoice has insufficient funds, passing `forgive=true` controls whether a charge should be attempted for the full amount available on the source, up to the amount to fully pay the invoice. This effectively forgives the difference between the amount available on the source and the amount due. <br>Passing `forgive=false` will fail the charge if the source hasn't been pre-funded with the right amount. An example for this case is with ACH Credit Transfers and wires: if the amount wired is less than the amount due by a small amount, you might want to forgive the difference. Defaults to `false`. |
| `mandate` | string or "" (to unset) |  | ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the payment_method param or the invoice's default_payment_method or default_source, if set. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `true` (off-session). |
| `paid_out_of_band` | boolean |  | Boolean representing whether an invoice is paid outside of Stripe. This will result in no charge being made. Defaults to `false`. |
| `payment_method` | string |  | A PaymentMethod to be charged. The PaymentMethod must be the ID of a PaymentMethod belonging to the customer associated with the invoice being paid. |
| `source` | string |  | A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid. |

Returns: `invoice`

## POST /v1/invoices/{invoice}/send

operationId: `PostInvoicesInvoiceSend`

Stripe will automatically send invoices to customers according to your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). However, if you’d like to manually send an invoice to your customer out of the normal schedule, you can do so. When sending invoices that have already been paid, there will be no reference to the payment in the email.

Requests made in test-mode result in no emails being sent, despite sending an `invoice.sent` event.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `invoice`

## POST /v1/invoices/{invoice}/void

operationId: `PostInvoicesInvoiceVoid`

Mark a finalized invoice as void. This cannot be undone. Voiding an invoice is similar to [deletion](#delete_invoice), however it only applies to finalized invoices and maintains a papertrail where the invoice can still be found.

Consult with local regulations to determine whether and how an invoice might be amended, canceled, or voided in the jurisdiction you’re doing business in. You might need to [issue another invoice](#create_invoice) or [credit note](#create_credit_note) instead. Stripe recommends that you consult with your legal counsel for advice specific to your business.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `invoice (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `invoice`

# Objects returned

## The `invoice` object

Invoices are statements of amounts owed by a customer, and are either
generated one-off, or generated periodically from a subscription.

They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
that may be caused by subscription upgrades/downgrades (if necessary).

If your invoice is configured to be billed through automatic charges,
Stripe automatically finalizes your invoice and attempts payment. Note
that finalizing the invoice,
[when automatic](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection), does
not happen immediately as the invoice is created. Stripe waits
until one hour after the last webhook was successfully sent (or the last
webhook timed out after failing). If you (and the platforms you may have
connected to) have no webhooks configured, Stripe waits one hour after
creation to finalize the invoice.

If your invoice is configured to be billed by sending an email, then based on your
[email settings](https://dashboard.stripe.com/account/billing/automatic),
Stripe will email the invoice to your customer and await payment. These
emails can contain a link to a hosted page to pay the invoice.

Stripe applies any customer credit on the account before determining the
amount due for the invoice (i.e., the amount that will be actually
charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
per currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts), the
invoice is automatically marked paid, and we add the amount due to the
customer's credit balance which is applied to the next invoice.

More details on the customer's credit balance are
[here](https://stripe.com/docs/billing/customer/balance).

Related guide: [Send invoices to customers](https://stripe.com/docs/billing/invoices/sending)

Expandable fields (pass `expand[]=<field>`): `account_tax_ids`, `application`, `automatic_tax`, `charge`, `custom_fields`, `customer`, `customer_address`, `customer_shipping`, `customer_tax_ids`, `default_payment_method`, `default_source`, `default_tax_rates`, `discount`, `discounts`, `from_invoice`, `issuer`, `last_finalization_error`, `latest_revision`, `lines`, `on_behalf_of`, `payment_intent`, `payment_settings`, `quote`, `rendering`, `shipping_cost`, `shipping_details`, `status_transitions`, `subscription`, `subscription_details`, `test_clock`, `threshold_reason`, `total_discount_amounts`, `total_tax_amounts`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_country` | string |  | The country of the business associated with this invoice, most often the business creating the invoice. |
| `account_name` | string |  | The public name of the business associated with this invoice, most often the business creating the invoice. |
| `account_tax_ids` | array of string or `tax_id` or `deleted_tax_id` |  | The account tax IDs associated with the invoice. Only editable when the invoice is a draft. |
| `amount_due` | integer | yes | Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`. |
| `amount_paid` | integer | yes | The amount, in cents (or local equivalent), that was paid. |
| `amount_remaining` | integer | yes | The difference between amount_due and amount_paid, in cents (or local equivalent). |
| `amount_shipping` | integer | yes | This is the sum of all the shipping amounts. |
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the invoice. |
| `application_fee_amount` | integer |  | The fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid. |
| `attempt_count` | integer | yes | Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule. |
| `attempted` | boolean | yes | Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users. |
| `auto_advance` | boolean |  | Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action. |
| `automatic_tax` | `automatic_tax` | yes |  |
| `billing_reason` | enum: `automatic_pending_invoice_item_invoice`, `manual`, `quote_accept`, `subscription`, `subscription_create`, `subscription_cycle`, `subscription_threshold`, `subscription_update`, `upcoming` |  | Indicates the reason why the invoice was created.<br>* `manual`: Unrelated to a subscription, for example, created via the invoice editor. * `subscription`: No longer in use. Applies to subscriptions from before May 2018 where no distinction was made between updates, cycles, and thresholds. * `subscription_create`: A new subscription was created. * `subscription_cycle`: A subscription advanced into a new period. * `subscription_threshold`: A subscription reached a billing threshold. * `subscription_update`: A subscription was updated. * `upcoming`: Reserved for simulated invoices, per the upcoming invoice endpoint. |
| `charge` | string or `charge` |  | ID of the latest charge generated for this invoice, if any. |
| `collection_method` | enum: `charge_automatically`, `send_invoice` | yes | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `custom_fields` | array of `invoice_setting_custom_field` |  | Custom fields displayed on the invoice. |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer who will be billed. |
| `customer_address` | `address` |  | The customer's address. Until the invoice is finalized, this field will equal `customer.address`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_email` | string |  | The customer's email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_name` | string |  | The customer's name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_phone` | string |  | The customer's phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_shipping` | `shipping` |  | The customer's shipping information. Until the invoice is finalized, this field will equal `customer.shipping`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_tax_exempt` | enum: `exempt`, `none`, `reverse` |  | The customer's tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated. |
| `customer_tax_ids` | array of `invoices_resource_invoice_tax_id` |  | The customer's tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated. |
| `default_payment_method` | string or `payment_method` |  | ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings. |
| `default_source` | string or `bank_account` or `card` or `source` |  | ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source. |
| `default_tax_rates` | array of `tax_rate` | yes | The tax rates applied to this invoice, if any. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard. |
| `discount` | `discount` |  | Describes the current discount applied to this invoice, if there is one. Not populated if there are multiple discounts. |
| `discounts` | array of string or `discount` or `deleted_discount` | yes | The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount. |
| `due_date` | timestamp (Unix seconds) |  | The date on which payment for this invoice is due. This value will be `null` for invoices where `collection_method=charge_automatically`. |
| `effective_at` | timestamp (Unix seconds) |  | The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt. |
| `ending_balance` | integer |  | Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null. |
| `footer` | string |  | Footer displayed on the invoice. |
| `from_invoice` | `invoices_resource_from_invoice` |  | Details of the invoice that was cloned. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details. |
| `hosted_invoice_url` | string |  | The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null. |
| `id` | string |  | Unique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See [Retrieve an upcoming invoice](https://stripe.com/docs/api/invoices/upcoming) for more details. |
| `invoice_pdf` | string |  | The link to download the PDF for the invoice. If the invoice has not been finalized yet, this will be null. |
| `issuer` | `connect_account_reference` | yes |  |
| `last_finalization_error` | `api_errors` |  | The error encountered during the previous attempt to finalize the invoice. This field is cleared when the invoice is successfully finalized. |
| `latest_revision` | string or `invoice` |  | The ID of the most recent non-draft revision of this invoice |
| `lines` | object | yes | The individual line items that make up the invoice. `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `next_payment_attempt` | timestamp (Unix seconds) |  | The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`. |
| `number` | string |  | A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified. |
| `object` | enum: `invoice` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details. |
| `paid` | boolean | yes | Whether payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance. |
| `paid_out_of_band` | boolean | yes | Returns true if the invoice was manually marked paid, returns false if the invoice hasn't been paid yet or was paid on Stripe. |
| `payment_intent` | string or `payment_intent` |  | The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent. |
| `payment_settings` | `invoices_payment_settings` | yes |  |
| `period_end` | timestamp (Unix seconds) | yes | End of the usage period during which invoice items were added to this invoice. |
| `period_start` | timestamp (Unix seconds) | yes | Start of the usage period during which invoice items were added to this invoice. |
| `post_payment_credit_notes_amount` | integer | yes | Total amount of all post-payment credit notes issued for this invoice. |
| `pre_payment_credit_notes_amount` | integer | yes | Total amount of all pre-payment credit notes issued for this invoice. |
| `quote` | string or `quote` |  | The quote this invoice was generated from. |
| `receipt_number` | string |  | This is the transaction number that appears on email receipts sent for this invoice. |
| `rendering` | `invoices_resource_invoice_rendering` |  | The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page. |
| `shipping_cost` | `invoices_resource_shipping_cost` |  | The details of the cost of shipping, including the ShippingRate applied on the invoice. |
| `shipping_details` | `shipping` |  | Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer. |
| `starting_balance` | integer | yes | Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice. |
| `statement_descriptor` | string |  | Extra information about an invoice for the customer's credit card statement. |
| `status` | enum: `draft`, `open`, `paid`, `uncollectible`, `void` |  | The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview) |
| `status_transitions` | `invoices_resource_status_transitions` | yes |  |
| `subscription` | string or `subscription` |  | The subscription that this invoice was prepared for, if any. |
| `subscription_details` | `subscription_details_data` |  | Details about the subscription that created this invoice. |
| `subscription_proration_date` | integer |  | Only set for upcoming invoices that preview prorations. The time used to calculate prorations. |
| `subtotal` | integer | yes | Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated |
| `subtotal_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated |
| `tax` | integer |  | The amount of tax on this invoice. This is the sum of all the tax amounts on this invoice. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this invoice belongs to. |
| `threshold_reason` | `invoice_threshold_reason` |  |  |
| `total` | integer | yes | Total after discounts and taxes. |
| `total_discount_amounts` | array of `discounts_resource_discount_amount` |  | The aggregate amounts calculated per discount across all line items. |
| `total_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the total amount of the invoice including all discounts but excluding all tax. |
| `total_tax_amounts` | array of `invoice_tax_amount` | yes | The aggregate amounts calculated per tax rate for all line items. |
| `transfer_data` | `invoice_transfer_data` |  | The account (if any) the payment will be attributed to for tax reporting, and where funds from the payment will be transferred to for the invoice. |
| `webhooks_delivered_at` | timestamp (Unix seconds) |  | Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://stripe.com/docs/billing/webhooks#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created. |

## The `deleted_invoice` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `invoice` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `line_item` object

Expandable fields (pass `expand[]=<field>`): `discount_amounts`, `discounts`, `invoice_item`, `period`, `price`, `proration_details`, `subscription`, `subscription_item`, `tax_amounts`, `tax_rates`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount, in cents (or local equivalent). |
| `amount_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the amount for this line item, excluding all tax and discounts. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `discount_amounts` | array of `discounts_resource_discount_amount` |  | The amount of discount calculated per discount for this line item. |
| `discountable` | boolean | yes | If true, discounts will apply to this line item. Always false for prorations. |
| `discounts` | array of string or `discount` | yes | The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string |  | The ID of the invoice that contains this line item. |
| `invoice_item` | string or `invoiceitem` |  | The ID of the [invoice item](https://stripe.com/docs/api/invoiceitems) associated with this line item if any. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription` this will reflect the metadata of the subscription that caused the line item to be created. |
| `object` | enum: `line_item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `period` | `invoice_line_item_period` | yes |  |
| `price` | `price` |  | The price of the line item. |
| `proration` | boolean | yes | Whether this is a proration. |
| `proration_details` | `invoices_resource_line_items_proration_details` |  | Additional details for proration line items |
| `quantity` | integer |  | The quantity of the subscription, if the line item is a subscription or a proration. |
| `subscription` | string or `subscription` |  | The subscription that the invoice item pertains to, if any. |
| `subscription_item` | string or `subscription_item` |  | The subscription item that generated this line item. Left empty if the line item is not an explicit result of a subscription. |
| `tax_amounts` | array of `invoice_tax_amount` |  | The amount of tax calculated per tax rate for this line item |
| `tax_rates` | array of `tax_rate` |  | The tax rates which apply to the line item. |
| `type` | enum: `invoiceitem`, `subscription` | yes | A string identifying the type of the source of this line item, either an `invoiceitem` or a `subscription`. |
| `unit_amount_excluding_tax` | string |  | The amount in cents (or local equivalent) representing the unit amount for this line item, excluding all tax and discounts. |

