# Stripe API 2023-10-16 — customers

Operations under `/v1/customers` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/customers

operationId: `GetCustomers`

Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return customers that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `email` | string |  | A case-sensitive filter on the list based on the customer's `email` field. The value must be a string. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `test_clock` | string |  | Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set. |

Returns: object

## POST /v1/customers

operationId: `PostCustomers`

Creates a new customer object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | object or "" (to unset) |  | The customer's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `balance` | integer |  | An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice. |
| `cash_balance` | object |  | Balance information and default balance settings for this customer. |
| `cash_balance.settings` | object |  |  |
| `cash_balance.settings.reconciliation_mode` | enum: `automatic`, `manual`, `merchant_default` |  |  |
| `coupon` | string |  |  |
| `description` | string |  | An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard. |
| `email` | string |  | Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_prefix` | string |  | The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers. |
| `invoice_settings` | object |  | Default invoice settings for this customer. |
| `invoice_settings.custom_fields` | array of object or "" (to unset) |  |  |
| `invoice_settings.custom_fields[].name` | string | yes |  |
| `invoice_settings.custom_fields[].value` | string | yes |  |
| `invoice_settings.default_payment_method` | string |  |  |
| `invoice_settings.footer` | string |  |  |
| `invoice_settings.rendering_options` | object or "" (to unset) |  |  |
| `invoice_settings.rendering_options.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | The customer's full name or business name. |
| `next_invoice_sequence` | integer |  | The sequence to be used on the customer's next invoice. Defaults to 1. |
| `payment_method` | string |  |  |
| `phone` | string |  | The customer's phone number. |
| `preferred_locales` | array of string |  | Customer's preferred languages, ordered by preference. |
| `promotion_code` | string |  | The ID of a promotion code to apply to the customer. The customer will have a discount applied on all recurring payments. Charges you create through the API will not have the discount. |
| `shipping` | object or "" (to unset) |  | The customer's shipping information. Appears on invoices emailed to this customer. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `source` | string (open enum) |  |  |
| `tax` | object |  | Tax details about the customer. |
| `tax.ip_address` | string or "" (to unset) |  |  |
| `tax.validate_location` | enum: `deferred`, `immediately` |  |  |
| `tax_exempt` | enum: ``, `exempt`, `none`, `reverse` |  | The customer's tax exemption. One of `none`, `exempt`, or `reverse`. |
| `tax_id_data` | array of object |  | The customer's tax IDs. |
| `tax_id_data[].type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes |  |
| `tax_id_data[].value` | string | yes |  |
| `test_clock` | string |  | ID of the test clock to attach to the customer. |

Returns: `customer`

## GET /v1/customers/search

operationId: `GetCustomersSearch`

Search for customers you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers). |

Returns: object

## GET /v1/customers/{customer}

operationId: `GetCustomersCustomer`

Retrieves a Customer object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `customer` or `deleted_customer`

## POST /v1/customers/{customer}

operationId: `PostCustomersCustomer`

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged. For example, if you pass the **source** parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the **source** parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the `past_due` state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the **default_source** for a customer will not trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `address` | object or "" (to unset) |  | The customer's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `balance` | integer |  | An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice. |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `card` | object or string |  | A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js). |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.metadata` | map (key → value) |  |  |
| `card.name` | string |  |  |
| `card.number` | string | yes |  |
| `card.object` | enum: `card` |  |  |
| `cash_balance` | object |  | Balance information and default balance settings for this customer. |
| `cash_balance.settings` | object |  |  |
| `cash_balance.settings.reconciliation_mode` | enum: `automatic`, `manual`, `merchant_default` |  |  |
| `coupon` | string |  |  |
| `default_alipay_account` | string |  | ID of Alipay account to make the customer's new default for invoice payments. |
| `default_bank_account` | string |  | ID of bank account to make the customer's new default for invoice payments. |
| `default_card` | string |  | ID of card to make the customer's new default for invoice payments. |
| `default_source` | string |  | If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) parameter.<br>Provide the ID of a payment source already attached to this customer to make it this customer's default payment source.<br>If you want to add a new payment source and make it the default, see the [source](https://stripe.com/docs/api/customers/update#update_customer-source) property. |
| `description` | string |  | An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard. |
| `email` | string |  | Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_prefix` | string |  | The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers. |
| `invoice_settings` | object |  | Default invoice settings for this customer. |
| `invoice_settings.custom_fields` | array of object or "" (to unset) |  |  |
| `invoice_settings.custom_fields[].name` | string | yes |  |
| `invoice_settings.custom_fields[].value` | string | yes |  |
| `invoice_settings.default_payment_method` | string |  |  |
| `invoice_settings.footer` | string |  |  |
| `invoice_settings.rendering_options` | object or "" (to unset) |  |  |
| `invoice_settings.rendering_options.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | The customer's full name or business name. |
| `next_invoice_sequence` | integer |  | The sequence to be used on the customer's next invoice. Defaults to 1. |
| `phone` | string |  | The customer's phone number. |
| `preferred_locales` | array of string |  | Customer's preferred languages, ordered by preference. |
| `promotion_code` | string |  | The ID of a promotion code to apply to the customer. The customer will have a discount applied on all recurring payments. Charges you create through the API will not have the discount. |
| `shipping` | object or "" (to unset) |  | The customer's shipping information. Appears on invoices emailed to this customer. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `source` | string (open enum) |  |  |
| `tax` | object |  | Tax details about the customer. |
| `tax.ip_address` | string or "" (to unset) |  |  |
| `tax.validate_location` | enum: `deferred`, `immediately` |  |  |
| `tax_exempt` | enum: ``, `exempt`, `none`, `reverse` |  | The customer's tax exemption. One of `none`, `exempt`, or `reverse`. |

Returns: `customer`

## DELETE /v1/customers/{customer}

operationId: `DeleteCustomersCustomer`

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |

Returns: `deleted_customer`

## GET /v1/customers/{customer}/balance_transactions

operationId: `GetCustomersCustomerBalanceTransactions`

Returns a list of transactions that updated the customer’s [balances](https://stripe.com/docs/billing/customer/balance).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/balance_transactions

operationId: `PostCustomersCustomerBalanceTransactions`

Creates an immutable transaction that updates the customer’s credit [balance](https://stripe.com/docs/billing/customer/balance).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `amount` | integer | yes | The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `customer_balance_transaction`

## GET /v1/customers/{customer}/balance_transactions/{transaction}

operationId: `GetCustomersCustomerBalanceTransactionsTransaction`

Retrieves a specific customer balance transaction that updated the customer’s [balances](https://stripe.com/docs/billing/customer/balance).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transaction (path)` | string | yes |  |

Returns: `customer_balance_transaction`

## POST /v1/customers/{customer}/balance_transactions/{transaction}

operationId: `PostCustomersCustomerBalanceTransactionsTransaction`

Most credit balance transaction fields are immutable, but you may update its `description` and `metadata`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `transaction (path)` | string | yes |  |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `customer_balance_transaction`

## GET /v1/customers/{customer}/bank_accounts

operationId: `GetCustomersCustomerBankAccounts`

**Deprecated.**

You can see a list of the bank accounts belonging to a Customer. Note that the 10 most recent sources are always available by default on the Customer. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional bank accounts.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/bank_accounts

operationId: `PostCustomersCustomerBankAccounts`

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default.
However, if the owner already has a default, then it will not change.
To change the default, you should [update the customer](https://stripe.com/docs/api#update_customer) to have a new `default_source`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `alipay_account` | string |  | A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details. |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `card` | object or string |  | A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js). |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.metadata` | map (key → value) |  |  |
| `card.name` | string |  |  |
| `card.number` | string | yes |  |
| `card.object` | enum: `card` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `source` | string (open enum) |  | Please refer to full [documentation](https://stripe.com/docs/api) instead. |

Returns: `payment_source`

## GET /v1/customers/{customer}/bank_accounts/{id}

operationId: `GetCustomersCustomerBankAccountsId`

**Deprecated.**

By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `bank_account`

## POST /v1/customers/{customer}/bank_accounts/{id}

operationId: `PostCustomersCustomerBankAccountsId`

Update a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | enum: `company`, `individual` |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `exp_month` | string |  | Two digit number representing the card’s expiration month. |
| `exp_year` | string |  | Four digit number representing the card’s expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Cardholder name. |
| `owner` | object |  |  |
| `owner.address` | object |  |  |
| `owner.address.city` | string |  |  |
| `owner.address.country` | string |  |  |
| `owner.address.line1` | string |  |  |
| `owner.address.line2` | string |  |  |
| `owner.address.postal_code` | string |  |  |
| `owner.address.state` | string |  |  |
| `owner.email` | string |  |  |
| `owner.name` | string |  |  |
| `owner.phone` | string |  |  |

Returns: `card` or `bank_account` or `source`

## DELETE /v1/customers/{customer}/bank_accounts/{id}

operationId: `DeleteCustomersCustomerBankAccountsId`

Delete a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_source` or `deleted_payment_source`

## POST /v1/customers/{customer}/bank_accounts/{id}/verify

operationId: `PostCustomersCustomerBankAccountsIdVerify`

Verify a specified bank account for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `amounts` | array of integer |  | Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `bank_account`

## GET /v1/customers/{customer}/cards

operationId: `GetCustomersCustomerCards`

**Deprecated.**

You can see a list of the cards belonging to a customer.
Note that the 10 most recent sources are always available on the `Customer` object.
If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional cards.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/cards

operationId: `PostCustomersCustomerCards`

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default.
However, if the owner already has a default, then it will not change.
To change the default, you should [update the customer](https://stripe.com/docs/api#update_customer) to have a new `default_source`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `alipay_account` | string |  | A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details. |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `card` | object or string |  | A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js). |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.metadata` | map (key → value) |  |  |
| `card.name` | string |  |  |
| `card.number` | string | yes |  |
| `card.object` | enum: `card` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `source` | string (open enum) |  | Please refer to full [documentation](https://stripe.com/docs/api) instead. |

Returns: `payment_source`

## GET /v1/customers/{customer}/cards/{id}

operationId: `GetCustomersCustomerCardsId`

**Deprecated.**

You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `card`

## POST /v1/customers/{customer}/cards/{id}

operationId: `PostCustomersCustomerCardsId`

Update a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | enum: `company`, `individual` |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `exp_month` | string |  | Two digit number representing the card’s expiration month. |
| `exp_year` | string |  | Four digit number representing the card’s expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Cardholder name. |
| `owner` | object |  |  |
| `owner.address` | object |  |  |
| `owner.address.city` | string |  |  |
| `owner.address.country` | string |  |  |
| `owner.address.line1` | string |  |  |
| `owner.address.line2` | string |  |  |
| `owner.address.postal_code` | string |  |  |
| `owner.address.state` | string |  |  |
| `owner.email` | string |  |  |
| `owner.name` | string |  |  |
| `owner.phone` | string |  |  |

Returns: `card` or `bank_account` or `source`

## DELETE /v1/customers/{customer}/cards/{id}

operationId: `DeleteCustomersCustomerCardsId`

Delete a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_source` or `deleted_payment_source`

## GET /v1/customers/{customer}/cash_balance

operationId: `GetCustomersCustomerCashBalance`

Retrieves a customer’s cash balance.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `cash_balance`

## POST /v1/customers/{customer}/cash_balance

operationId: `PostCustomersCustomerCashBalance`

Changes the settings on a customer’s cash balance.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `settings` | object |  | A hash of settings for this cash balance. |
| `settings.reconciliation_mode` | enum: `automatic`, `manual`, `merchant_default` |  |  |

Returns: `cash_balance`

## GET /v1/customers/{customer}/cash_balance_transactions

operationId: `GetCustomersCustomerCashBalanceTransactions`

Returns a list of transactions that modified the customer’s [cash balance](https://stripe.com/docs/payments/customer-balance).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/customers/{customer}/cash_balance_transactions/{transaction}

operationId: `GetCustomersCustomerCashBalanceTransactionsTransaction`

Retrieves a specific cash balance transaction, which updated the customer’s [cash balance](https://stripe.com/docs/payments/customer-balance).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transaction (path)` | string | yes |  |

Returns: `customer_cash_balance_transaction`

## GET /v1/customers/{customer}/discount

operationId: `GetCustomersCustomerDiscount`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `discount`

## DELETE /v1/customers/{customer}/discount

operationId: `DeleteCustomersCustomerDiscount`

Removes the currently applied discount on a customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |

Returns: `deleted_discount`

## POST /v1/customers/{customer}/funding_instructions

operationId: `PostCustomersCustomerFundingInstructions`

Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
funding instructions will be created. If funding instructions have already been created for a given customer, the same
funding instructions will be retrieved. In other words, we will return the same funding instructions each time.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `bank_transfer` | object | yes | Additional parameters for `bank_transfer` funding types |
| `bank_transfer.eu_bank_transfer` | object |  |  |
| `bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `bank_transfer.requested_address_types` | array of enum: `iban`, `sort_code`, `spei`, `zengin` |  |  |
| `bank_transfer.type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes |  |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `funding_type` | enum: `bank_transfer` | yes | The `funding_type` to get the instructions for. |

Returns: `funding_instructions`

## GET /v1/customers/{customer}/payment_methods

operationId: `GetCustomersCustomerPaymentMethods`

Returns a list of PaymentMethods for a given Customer

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` |  | An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request. |

Returns: object

## GET /v1/customers/{customer}/payment_methods/{payment_method}

operationId: `GetCustomersCustomerPaymentMethodsPaymentMethod`

Retrieves a PaymentMethod object for a given Customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_method (path)` | string | yes |  |

Returns: `payment_method`

## GET /v1/customers/{customer}/sources

operationId: `GetCustomersCustomerSources`

List sources for a specified customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `object` | string |  | Filter sources according to a particular object type. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/sources

operationId: `PostCustomersCustomerSources`

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default.
However, if the owner already has a default, then it will not change.
To change the default, you should [update the customer](https://stripe.com/docs/api#update_customer) to have a new `default_source`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `alipay_account` | string |  | A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details. |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `card` | object or string |  | A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js). |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.metadata` | map (key → value) |  |  |
| `card.name` | string |  |  |
| `card.number` | string | yes |  |
| `card.object` | enum: `card` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `source` | string (open enum) |  | Please refer to full [documentation](https://stripe.com/docs/api) instead. |

Returns: `payment_source`

## GET /v1/customers/{customer}/sources/{id}

operationId: `GetCustomersCustomerSourcesId`

Retrieve a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `payment_source`

## POST /v1/customers/{customer}/sources/{id}

operationId: `PostCustomersCustomerSourcesId`

Update a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | enum: `company`, `individual` |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `exp_month` | string |  | Two digit number representing the card’s expiration month. |
| `exp_year` | string |  | Four digit number representing the card’s expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Cardholder name. |
| `owner` | object |  |  |
| `owner.address` | object |  |  |
| `owner.address.city` | string |  |  |
| `owner.address.country` | string |  |  |
| `owner.address.line1` | string |  |  |
| `owner.address.line2` | string |  |  |
| `owner.address.postal_code` | string |  |  |
| `owner.address.state` | string |  |  |
| `owner.email` | string |  |  |
| `owner.name` | string |  |  |
| `owner.phone` | string |  |  |

Returns: `card` or `bank_account` or `source`

## DELETE /v1/customers/{customer}/sources/{id}

operationId: `DeleteCustomersCustomerSourcesId`

Delete a specified source for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_source` or `deleted_payment_source`

## POST /v1/customers/{customer}/sources/{id}/verify

operationId: `PostCustomersCustomerSourcesIdVerify`

Verify a specified bank account for a given customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `amounts` | array of integer |  | Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `bank_account`

## GET /v1/customers/{customer}/subscriptions

operationId: `GetCustomersCustomerSubscriptions`

You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/subscriptions

operationId: `PostCustomersCustomerSubscriptions`

Creates a new subscription on an existing customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `add_invoice_items` | array of object |  | A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items. |
| `add_invoice_items[].discounts` | array of object |  |  |
| `add_invoice_items[].discounts[].coupon` | string |  |  |
| `add_invoice_items[].discounts[].discount` | string |  |  |
| `add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `add_invoice_items[].price` | string |  |  |
| `add_invoice_items[].price_data` | object |  |  |
| `add_invoice_items[].price_data.currency` | string | yes |  |
| `add_invoice_items[].price_data.product` | string | yes |  |
| `add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `add_invoice_items[].quantity` | integer |  |  |
| `add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions). |
| `automatic_tax` | object |  | Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `backdate_start_date` | timestamp (Unix seconds) |  | For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor. |
| `billing_cycle_anchor` | timestamp (Unix seconds) |  | A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. |
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.amount_gte` | integer |  |  |
| `billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `cancel_at` | timestamp (Unix seconds) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `coupon` | string |  | The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`. |
| `default_payment_method` | string |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `items[].billing_thresholds` | object or "" (to unset) |  |  |
| `items[].billing_thresholds.usage_gte` | integer | yes |  |
| `items[].discounts` | array of object or "" (to unset) |  |  |
| `items[].discounts[].coupon` | string |  |  |
| `items[].discounts[].discount` | string |  |  |
| `items[].discounts[].promotion_code` | string |  |  |
| `items[].metadata` | map (key → value) |  |  |
| `items[].price` | string |  |  |
| `items[].price_data` | object |  |  |
| `items[].price_data.currency` | string | yes |  |
| `items[].price_data.product` | string | yes |  |
| `items[].price_data.recurring` | object | yes |  |
| `items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `items[].price_data.recurring.interval_count` | integer |  |  |
| `items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `items[].price_data.unit_amount` | integer |  |  |
| `items[].price_data.unit_amount_decimal` | string |  |  |
| `items[].quantity` | integer |  |  |
| `items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Only applies to subscriptions with `collection_method=charge_automatically`.<br>Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.<br>`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.<br>Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status. |
| `payment_settings` | object |  | Payment settings to pass to invoices created by the subscription. |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount` | integer |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` |  |  |
| `payment_settings.payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_settings.payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
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
| `payment_settings.save_default_payment_method` | enum: `off`, `on_subscription` |  |  |
| `pending_invoice_item_interval` | object or "" (to unset) |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_invoice_item_interval.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `pending_invoice_item_interval.interval_count` | integer |  |  |
| `promotion_code` | string |  | The ID of a promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`. |
| `transfer_data` | object |  | If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |
| `trial_end` | enum: `now` or timestamp (Unix seconds) |  | Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_period_days` | integer |  | Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_settings` | object |  | Settings related to subscription trials. |
| `trial_settings.end_behavior` | object | yes |  |
| `trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |

Returns: `subscription`

## GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

operationId: `GetCustomersCustomerSubscriptionsSubscriptionExposedId`

Retrieves the subscription with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `subscription_exposed_id (path)` | string | yes |  |

Returns: `subscription`

## POST /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

operationId: `PostCustomersCustomerSubscriptionsSubscriptionExposedId`

Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the [upcoming invoice](#upcoming_invoice) endpoint.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `subscription_exposed_id (path)` | string | yes |  |
| `add_invoice_items` | array of object |  | A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items. |
| `add_invoice_items[].discounts` | array of object |  |  |
| `add_invoice_items[].discounts[].coupon` | string |  |  |
| `add_invoice_items[].discounts[].discount` | string |  |  |
| `add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `add_invoice_items[].price` | string |  |  |
| `add_invoice_items[].price_data` | object |  |  |
| `add_invoice_items[].price_data.currency` | string | yes |  |
| `add_invoice_items[].price_data.product` | string | yes |  |
| `add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `add_invoice_items[].quantity` | integer |  |  |
| `add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions). |
| `automatic_tax` | object |  | Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `billing_cycle_anchor` | enum: `now`, `unchanged` |  | Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle). |
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.amount_gte` | integer |  |  |
| `billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `cancel_at` | timestamp (Unix seconds) or "" (to unset) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `cancellation_details` | object |  | Details about why this subscription was cancelled |
| `cancellation_details.comment` | string or "" (to unset) |  |  |
| `cancellation_details.feedback` | enum: ``, `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` |  |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `coupon` | string |  | The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`. |
| `default_payment_method` | string |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string or "" (to unset) |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates. |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `items[].billing_thresholds` | object or "" (to unset) |  |  |
| `items[].billing_thresholds.usage_gte` | integer | yes |  |
| `items[].clear_usage` | boolean |  |  |
| `items[].deleted` | boolean |  |  |
| `items[].discounts` | array of object or "" (to unset) |  |  |
| `items[].discounts[].coupon` | string |  |  |
| `items[].discounts[].discount` | string |  |  |
| `items[].discounts[].promotion_code` | string |  |  |
| `items[].id` | string |  |  |
| `items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `items[].price` | string |  |  |
| `items[].price_data` | object |  |  |
| `items[].price_data.currency` | string | yes |  |
| `items[].price_data.product` | string | yes |  |
| `items[].price_data.recurring` | object | yes |  |
| `items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `items[].price_data.recurring.interval_count` | integer |  |  |
| `items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `items[].price_data.unit_amount` | integer |  |  |
| `items[].price_data.unit_amount_decimal` | string |  |  |
| `items[].quantity` | integer |  |  |
| `items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. |
| `pause_collection` | object or "" (to unset) |  | If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](/billing/subscriptions/pause-payment). |
| `pause_collection.behavior` | enum: `keep_as_draft`, `mark_uncollectible`, `void` | yes |  |
| `pause_collection.resumes_at` | timestamp (Unix seconds) |  |  |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.<br>Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more. |
| `payment_settings` | object |  | Payment settings to pass to invoices created by the subscription. |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount` | integer |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` |  |  |
| `payment_settings.payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_settings.payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
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
| `payment_settings.save_default_payment_method` | enum: `off`, `on_subscription` |  |  |
| `pending_invoice_item_interval` | object or "" (to unset) |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_invoice_item_interval.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `pending_invoice_item_interval.interval_count` | integer |  |  |
| `promotion_code` | string |  | The promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#upcoming_invoice) endpoint. It can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations. |
| `transfer_data` | object or "" (to unset) |  | If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value. |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |
| `trial_end` | enum: `now` or timestamp (Unix seconds) |  | Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. |
| `trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_settings` | object |  | Settings related to subscription trials. |
| `trial_settings.end_behavior` | object | yes |  |
| `trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |

Returns: `subscription`

## DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

operationId: `DeleteCustomersCustomerSubscriptionsSubscriptionExposedId`

Cancels a customer’s subscription. If you set the `at_period_end` parameter to `true`, the subscription will remain active until the end of the period, at which point it will be canceled and not renewed. Otherwise, with the default `false` value, the subscription is terminated immediately. In either case, the customer will not be charged again for the subscription.

Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually [deleted](#delete_invoiceitem). If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.

By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `subscription_exposed_id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_now` | boolean |  | Can be set to `true` if `at_period_end` is not set to `true`. Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. |
| `prorate` | boolean |  | Can be set to `true` if `at_period_end` is not set to `true`. Will generate a proration invoice item that credits remaining unused time until the subscription period end. |

Returns: `subscription`

## GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

operationId: `GetCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `subscription_exposed_id (path)` | string | yes |  |

Returns: `discount`

## DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

operationId: `DeleteCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount`

Removes the currently applied discount on a customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `subscription_exposed_id (path)` | string | yes |  |

Returns: `deleted_discount`

## GET /v1/customers/{customer}/tax_ids

operationId: `GetCustomersCustomerTaxIds`

Returns a list of tax IDs for a customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/customers/{customer}/tax_ids

operationId: `PostCustomersCustomerTaxIds`

Creates a new `tax_id` object for a customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes | Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat` |
| `value` | string | yes | Value of the tax ID. |

Returns: `tax_id`

## GET /v1/customers/{customer}/tax_ids/{id}

operationId: `GetCustomersCustomerTaxIdsId`

Retrieves the `tax_id` object with the given identifier.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `tax_id`

## DELETE /v1/customers/{customer}/tax_ids/{id}

operationId: `DeleteCustomersCustomerTaxIdsId`

Deletes an existing `tax_id` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `id (path)` | string | yes |  |

Returns: `deleted_tax_id`

# Objects returned

## The `customer` object

This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment)

Expandable fields (pass `expand[]=<field>`): `address`, `cash_balance`, `default_source`, `discount`, `invoice_settings`, `shipping`, `sources`, `subscriptions`, `tax`, `tax_ids`, `test_clock`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  | The customer's address. |
| `balance` | integer |  | The current balance, if any, that's stored on the customer. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that's added to their next invoice. The balance only considers amounts that Stripe hasn't successfully applied to any invoice. It doesn't reflect unpaid invoices. This balance is only taken into account after invoices finalize. |
| `cash_balance` | `cash_balance` |  | The current funds being held by Stripe on behalf of the customer. You can apply these funds towards payment intents when the source is "cash_balance". The `settings[reconciliation_mode]` field describes if these funds apply to these payment intents manually or automatically. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes. |
| `default_source` | string or `bank_account` or `card` or `source` |  | ID of the default payment source for the customer.<br>If you use payment methods created through the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) field instead. |
| `delinquent` | boolean |  | Tracks the most recent state change on any invoice belonging to the customer. Paying an invoice or marking it uncollectible via the API will set this field to false. An automatic payment failure or passing the `invoice.due_date` will set this field to `true`.<br>If an invoice becomes uncollectible by [dunning](https://stripe.com/docs/billing/automatic-collection), `delinquent` doesn't reset to `false`.<br>If you care whether the customer has paid their most recent subscription invoice, use `subscription.status` instead. Paying or marking uncollectible any customer invoice regardless of whether it is the latest invoice for a subscription will always set this field to `false`. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `discount` | `discount` |  | Describes the current discount active on the customer, if there is one. |
| `email` | string |  | The customer's email address. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice_credit_balance` | map (key → value) |  | The current multi-currency balances, if any, that's stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that's added to their next invoice denominated in that currency. These balances don't apply to unpaid invoices. They solely track amounts that Stripe hasn't successfully applied to any invoice. Stripe only applies a balance in a specific currency to an invoice after that invoice (which is in the same currency) finalizes. |
| `invoice_prefix` | string |  | The prefix for the customer used to generate unique invoice numbers. |
| `invoice_settings` | `invoice_setting_customer_setting` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string |  | The customer's full name or business name. |
| `next_invoice_sequence` | integer |  | The suffix of the customer's next invoice number (for example, 0001). |
| `object` | enum: `customer` | yes | String representing the object's type. Objects of the same type share the same value. |
| `phone` | string |  | The customer's phone number. |
| `preferred_locales` | array of string |  | The customer's preferred locales (languages), ordered by preference. |
| `shipping` | `shipping` |  | Mailing and shipping address for the customer. Appears on invoices emailed to this customer. |
| `sources` | object |  | The customer's payment sources, if any. |
| `subscriptions` | object |  | The customer's current subscriptions, if any. |
| `tax` | `customer_tax` |  |  |
| `tax_exempt` | enum: `exempt`, `none`, `reverse` |  | Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the following text: **"Reverse charge"**. |
| `tax_ids` | object |  | The customer's tax IDs. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock that this customer belongs to. |

## The `deleted_customer` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `customer` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `customer_balance_transaction` object

Each customer has a [Balance](https://stripe.com/docs/api/customers/object#customer_object-balance) value,
which denotes a debit or credit that's automatically applied to their next invoice upon finalization.
You may modify the value directly by using the [update customer API](https://stripe.com/docs/api/customers/update),
or by creating a Customer Balance Transaction, which increments or decrements the customer's `balance` by the specified `amount`.

Related guide: [Customer balance](https://stripe.com/docs/billing/customer/balance)

Expandable fields (pass `expand[]=<field>`): `credit_note`, `customer`, `invoice`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount of the transaction. A negative value is a credit for the customer's balance, and a positive value is a debit to the customer's `balance`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `credit_note` | string or `credit_note` |  | The ID of the credit note (if any) related to the transaction. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` | yes | The ID of the customer the transaction belongs to. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `ending_balance` | integer | yes | The customer's `balance` after the transaction was applied. A negative value decreases the amount due on the customer's next invoice. A positive value increases the amount due on the customer's next invoice. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` |  | The ID of the invoice (if any) related to the transaction. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `customer_balance_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `type` | enum: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `migration`, `unapplied_from_invoice`, `unspent_receiver_credit` | yes | Transaction type: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `unspent_receiver_credit`, or `unapplied_from_invoice`. See the [Customer Balance page](https://stripe.com/docs/billing/customer/balance#types) to learn more about transaction types. |

## The `payment_source` object

Type: `account` or `bank_account` or `card` or `source`

## The `bank_account` object

These bank accounts are payment methods on `Customer` objects.

On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
They can be bank accounts or debit cards as well, and are documented in the links above.

Related guide: [Bank debits and transfers](https://stripe.com/docs/payments/bank-debits-transfers)

Expandable fields (pass `expand[]=<field>`): `account`, `customer`, `future_requirements`, `requirements`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` |  | The ID of the account that the bank account is associated with. |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | string |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `account_type` | string |  | The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`. |
| `available_payout_methods` | array of enum: `instant`, `standard` |  | A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout. |
| `bank_name` | string |  | Name of the bank associated with the routing number (e.g., `WELLS FARGO`). |
| `country` | string | yes | Two-letter ISO code representing the country the bank account is located in. |
| `currency` | string | yes | Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account. |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer that the bank account is associated with. |
| `default_for_currency` | boolean |  | Whether this bank account is the default external account for its currency. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `future_requirements` | `external_account_requirements` |  | Information about the [upcoming new requirements for the bank account](https://stripe.com/docs/connect/custom-accounts/future-requirements), including what information needs to be collected, and by when. |
| `id` | string | yes | Unique identifier for the object. |
| `last4` | string | yes | The last four digits of the bank account number. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `bank_account` | yes | String representing the object's type. Objects of the same type share the same value. |
| `requirements` | `external_account_requirements` |  | Information about the requirements for the bank account, including what information needs to be collected. |
| `routing_number` | string |  | The routing transit number for the bank account. |
| `status` | string | yes | For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a payout sent to this bank account fails, we'll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.<br>For external accounts, possible values are `new`, `errored` and `verification_failed`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can't [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we'll set the status to `verification_failed`. Other validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply. |

## The `card` object

You can store multiple cards on a customer in order to charge the customer
later. You can also store multiple debit cards on a recipient in order to
transfer to those cards later.

Related guide: [Card payments with Sources](https://stripe.com/docs/sources/cards)

Expandable fields (pass `expand[]=<field>`): `account`, `customer`, `networks`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` |  | The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line1_check` | string |  | If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `address_zip_check` | string |  | If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. |
| `available_payout_methods` | array of enum: `instant`, `standard` |  | A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout. |
| `brand` | string | yes | Card brand. Can be `American Express`, `Diners Club`, `Discover`, `Eftpos Australia`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`. |
| `country` | string |  | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected. |
| `currency` | string |  | Three-letter [ISO code for currency](https://stripe.com/docs/payouts). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency. |
| `customer` | string or `customer` or `deleted_customer` |  | The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead. |
| `cvc_check` | string |  | If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn't been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge). |
| `default_for_currency` | boolean |  | Whether this card is the default external account for its currency. |
| `dynamic_last4` | string |  | (For tokenized numbers only.) The last four digits of the device account number. |
| `exp_month` | integer | yes | Two-digit number representing the card's expiration month. |
| `exp_year` | integer | yes | Four-digit number representing the card's expiration year. |
| `fingerprint` | string |  | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.<br>*As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.* |
| `funding` | string | yes | Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`. |
| `id` | string | yes | Unique identifier for the object. |
| `last4` | string | yes | The last four digits of the card. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string |  | Cardholder name. |
| `networks` | `token_card_networks` |  |  |
| `object` | enum: `card` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | string |  | For external accounts that are cards, possible values are `new` and `errored`. If a payout fails, the status is set to `errored` and [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) are stopped until account details are updated. |
| `tokenization_method` | string |  | If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null. |

## The `source` object

`Source` objects allow you to accept a variety of payment methods. They
represent a customer's payment instrument, and can be used with the Stripe API
just like a `Card` object: once chargeable, they can be charged, or can be
attached to customers.

Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
This newer API provides access to our latest features and payment method types.

Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).

Expandable fields (pass `expand[]=<field>`): `code_verification`, `owner`, `receiver`, `redirect`, `source_order`

| Field | Type | Required | Description |
|---|---|---|---|
| `ach_credit_transfer` | `source_type_ach_credit_transfer` |  |  |
| `ach_debit` | `source_type_ach_debit` |  |  |
| `acss_debit` | `source_type_acss_debit` |  |  |
| `alipay` | `source_type_alipay` |  |  |
| `amount` | integer |  | A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. |
| `au_becs_debit` | `source_type_au_becs_debit` |  |  |
| `bancontact` | `source_type_bancontact` |  |  |
| `card` | `source_type_card` |  |  |
| `card_present` | `source_type_card_present` |  |  |
| `client_secret` | string | yes | The client secret of the source. Used for client-side retrieval using a publishable key. |
| `code_verification` | `source_code_verification_flow` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources. |
| `customer` | string |  | The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer. |
| `eps` | `source_type_eps` |  |  |
| `flow` | string | yes | The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. |
| `giropay` | `source_type_giropay` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `ideal` | `source_type_ideal` |  |  |
| `klarna` | `source_type_klarna` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `multibanco` | `source_type_multibanco` |  |  |
| `object` | enum: `source` | yes | String representing the object's type. Objects of the same type share the same value. |
| `owner` | `source_owner` |  | Information about the owner of the payment instrument that may be used or required by particular source types. |
| `p24` | `source_type_p24` |  |  |
| `receiver` | `source_receiver_flow` |  |  |
| `redirect` | `source_redirect_flow` |  |  |
| `sepa_debit` | `source_type_sepa_debit` |  |  |
| `sofort` | `source_type_sofort` |  |  |
| `source_order` | `source_order` |  |  |
| `statement_descriptor` | string |  | Extra information about a source. This will appear on your customer's statement every time you charge the source. |
| `status` | string | yes | The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge. |
| `three_d_secure` | `source_type_three_d_secure` |  |  |
| `type` | enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, `wechat` | yes | The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used. |
| `usage` | string |  | Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned. |
| `wechat` | `source_type_wechat` |  |  |

## The `deleted_payment_source` object

Type: `deleted_bank_account` or `deleted_card`

## The `cash_balance` object

A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.

Expandable fields (pass `expand[]=<field>`): `settings`

| Field | Type | Required | Description |
|---|---|---|---|
| `available` | map (key → value) |  | A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `customer` | string | yes | The ID of the customer whose cash balance this object represents. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `cash_balance` | yes | String representing the object's type. Objects of the same type share the same value. |
| `settings` | `customer_balance_customer_balance_settings` | yes |  |

## The `customer_cash_balance_transaction` object

Customers with certain payments enabled have a cash balance, representing funds that were paid
by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
to payments, and refunds to the customer.

Expandable fields (pass `expand[]=<field>`): `adjusted_for_overdraft`, `applied_to_payment`, `customer`, `funded`, `refunded_from_payment`, `transferred_to_balance`, `unapplied_from_payment`

| Field | Type | Required | Description |
|---|---|---|---|
| `adjusted_for_overdraft` | `customer_balance_resource_cash_balance_transaction_resource_adjusted_for_overdraft` |  |  |
| `applied_to_payment` | `customer_balance_resource_cash_balance_transaction_resource_applied_to_payment_transaction` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` | yes | The customer whose available cash balance changed as a result of this transaction. |
| `ending_balance` | integer | yes | The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `funded` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `net_amount` | integer | yes | The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance. |
| `object` | enum: `customer_cash_balance_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `refunded_from_payment` | `customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction` |  |  |
| `transferred_to_balance` | `customer_balance_resource_cash_balance_transaction_resource_transferred_to_balance` |  |  |
| `type` | enum: `adjusted_for_overdraft`, `applied_to_payment`, `funded`, `funding_reversed`, `refunded_from_payment`, `return_canceled`, `return_initiated`, `transferred_to_balance`, `unapplied_from_payment` | yes | The type of the cash balance transaction. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types. |
| `unapplied_from_payment` | `customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction` |  |  |

## The `discount` object

A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
It contains information about when the discount began, when it will end, and what it is applied to.

Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)

Expandable fields (pass `expand[]=<field>`): `coupon`, `customer`, `promotion_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `checkout_session` | string |  | The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode. |
| `coupon` | `coupon` | yes |  |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer associated with this discount. |
| `end` | timestamp (Unix seconds) |  | If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null. |
| `id` | string | yes | The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array. |
| `invoice` | string |  | The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice. |
| `invoice_item` | string |  | The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item. |
| `object` | enum: `discount` | yes | String representing the object's type. Objects of the same type share the same value. |
| `promotion_code` | string or `promotion_code` |  | The promotion code applied to create this discount. |
| `start` | timestamp (Unix seconds) | yes | Date that the coupon was applied. |
| `subscription` | string |  | The subscription that this coupon is applied to, if it is applied to a particular subscription. |
| `subscription_item` | string |  | The subscription item that this coupon is applied to, if it is applied to a particular subscription item. |

## The `deleted_discount` object

Expandable fields (pass `expand[]=<field>`): `coupon`, `customer`, `promotion_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `checkout_session` | string |  | The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode. |
| `coupon` | `coupon` | yes |  |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer associated with this discount. |
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array. |
| `invoice` | string |  | The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice. |
| `invoice_item` | string |  | The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item. |
| `object` | enum: `discount` | yes | String representing the object's type. Objects of the same type share the same value. |
| `promotion_code` | string or `promotion_code` |  | The promotion code applied to create this discount. |
| `start` | timestamp (Unix seconds) | yes | Date that the coupon was applied. |
| `subscription` | string |  | The subscription that this coupon is applied to, if it is applied to a particular subscription. |
| `subscription_item` | string |  | The subscription item that this coupon is applied to, if it is applied to a particular subscription item. |

## The `funding_instructions` object

Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) that is
automatically applied to future invoices and payments using the `customer_balance` payment method.
Customers can fund this balance by initiating a bank transfer to any account in the
`financial_addresses` field.
Related guide: [Customer balance funding instructions](https://stripe.com/docs/payments/customer-balance/funding-instructions)

Expandable fields (pass `expand[]=<field>`): `bank_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_transfer` | `funding_instructions_bank_transfer` | yes |  |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `funding_type` | enum: `bank_transfer` | yes | The `funding_type` of the returned instructions |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `funding_instructions` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `payment_method` object

PaymentMethod objects represent your customer's payment instruments.
You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
Customer objects to store instrument details for future payments.

Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billing_details`, `blik`, `boleto`, `card`, `card_present`, `cashapp`, `customer`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `interac_present`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `radar_options`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `payment_method_acss_debit` |  |  |
| `affirm` | `payment_method_affirm` |  |  |
| `afterpay_clearpay` | `payment_method_afterpay_clearpay` |  |  |
| `alipay` | `payment_flows_private_payment_methods_alipay` |  |  |
| `au_becs_debit` | `payment_method_au_becs_debit` |  |  |
| `bacs_debit` | `payment_method_bacs_debit` |  |  |
| `bancontact` | `payment_method_bancontact` |  |  |
| `billing_details` | `billing_details` | yes |  |
| `blik` | `payment_method_blik` |  |  |
| `boleto` | `payment_method_boleto` |  |  |
| `card` | `payment_method_card` |  |  |
| `card_present` | `payment_method_card_present` |  |  |
| `cashapp` | `payment_method_cashapp` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` |  | The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer. |
| `customer_balance` | `payment_method_customer_balance` |  |  |
| `eps` | `payment_method_eps` |  |  |
| `fpx` | `payment_method_fpx` |  |  |
| `giropay` | `payment_method_giropay` |  |  |
| `grabpay` | `payment_method_grabpay` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `ideal` | `payment_method_ideal` |  |  |
| `interac_present` | `payment_method_interac_present` |  |  |
| `klarna` | `payment_method_klarna` |  |  |
| `konbini` | `payment_method_konbini` |  |  |
| `link` | `payment_method_link` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `mobilepay` | `payment_method_mobilepay` |  |  |
| `object` | enum: `payment_method` | yes | String representing the object's type. Objects of the same type share the same value. |
| `oxxo` | `payment_method_oxxo` |  |  |
| `p24` | `payment_method_p24` |  |  |
| `paynow` | `payment_method_paynow` |  |  |
| `paypal` | `payment_method_paypal` |  |  |
| `pix` | `payment_method_pix` |  |  |
| `promptpay` | `payment_method_promptpay` |  |  |
| `radar_options` | `radar_radar_options` |  |  |
| `revolut_pay` | `payment_method_revolut_pay` |  |  |
| `sepa_debit` | `payment_method_sepa_debit` |  |  |
| `sofort` | `payment_method_sofort` |  |  |
| `swish` | `payment_method_swish` |  |  |
| `type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `card_present`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `interac_present`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` | yes | The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type. |
| `us_bank_account` | `payment_method_us_bank_account` |  |  |
| `wechat_pay` | `payment_method_wechat_pay` |  |  |
| `zip` | `payment_method_zip` |  |  |

## The `subscription` object

Subscriptions allow you to charge a customer on a recurring basis.

Related guide: [Creating subscriptions](https://stripe.com/docs/billing/subscriptions/creating)

Expandable fields (pass `expand[]=<field>`): `application`, `automatic_tax`, `billing_cycle_anchor_config`, `billing_thresholds`, `cancellation_details`, `customer`, `default_payment_method`, `default_source`, `default_tax_rates`, `discount`, `discounts`, `items`, `latest_invoice`, `on_behalf_of`, `pause_collection`, `payment_settings`, `pending_invoice_item_interval`, `pending_setup_intent`, `pending_update`, `schedule`, `test_clock`, `transfer_data`, `trial_settings`

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the subscription. |
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. |
| `automatic_tax` | `subscription_automatic_tax` | yes |  |
| `billing_cycle_anchor` | timestamp (Unix seconds) | yes | The reference point that aligns future [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format. |
| `billing_cycle_anchor_config` | `subscriptions_resource_billing_cycle_anchor_config` |  | The fixed values used to calculate the `billing_cycle_anchor`. |
| `billing_thresholds` | `subscription_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period |
| `cancel_at` | timestamp (Unix seconds) |  | A date in the future at which the subscription will automatically get canceled |
| `cancel_at_period_end` | boolean | yes | If the subscription has been canceled with the `at_period_end` flag set to `true`, `cancel_at_period_end` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period. |
| `canceled_at` | timestamp (Unix seconds) |  | If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state. |
| `cancellation_details` | `cancellation_details` |  | Details about why this subscription was cancelled |
| `collection_method` | enum: `charge_automatically`, `send_invoice` | yes | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `current_period_end` | timestamp (Unix seconds) | yes | End of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created. |
| `current_period_start` | timestamp (Unix seconds) | yes | Start of the current period that the subscription has been invoiced for. |
| `customer` | string or `customer` or `deleted_customer` | yes | ID of the customer who owns the subscription. |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`. |
| `default_payment_method` | string or `payment_method` |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string or `bank_account` or `card` or `source` |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of `tax_rate` |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. |
| `description` | string |  | The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `discount` | `discount` |  | Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `discounts` | array of string or `discount` | yes | The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount. |
| `ended_at` | timestamp (Unix seconds) |  | If the subscription has ended, the date the subscription ended. |
| `id` | string | yes | Unique identifier for the object. |
| `items` | object | yes | List of subscription items, each with an attached price. |
| `latest_invoice` | string or `invoice` |  | The most recent invoice this subscription has generated. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `next_pending_invoice_item_invoice` | timestamp (Unix seconds) |  | Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`. |
| `object` | enum: `subscription` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) the charge was made on behalf of for charges associated with this subscription. See the Connect documentation for details. |
| `pause_collection` | `subscriptions_resource_pause_collection` |  | If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](/billing/subscriptions/pause-payment). |
| `payment_settings` | `subscriptions_resource_payment_settings` |  | Payment settings passed on to invoices created by the subscription. |
| `pending_invoice_item_interval` | `subscription_pending_invoice_item_interval` |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_setup_intent` | string or `setup_intent` |  | You can use this [SetupIntent](https://stripe.com/docs/api/setup_intents) to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication#scenario-2). |
| `pending_update` | `subscriptions_resource_pending_update` |  | If specified, [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates) that will be applied to the subscription once the `latest_invoice` has been paid. |
| `schedule` | string or `subscription_schedule` |  | The schedule attached to the subscription |
| `start_date` | timestamp (Unix seconds) | yes | Date when the subscription was first created. The date might differ from the `created` date due to backdating. |
| `status` | enum: `active`, `canceled`, `incomplete`, `incomplete_expired`, `past_due`, `paused`, `trialing`, `unpaid` | yes | Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`. <br>For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated. <br>A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over. <br>A subscription can only enter a `paused` status [when a trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment). A `paused` subscription doesn't generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](/billing/subscriptions/pause-payment), which still generates invoices and leaves the subscription's status unchanged. <br>If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings). <br>If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this subscription belongs to. |
| `transfer_data` | `subscription_transfer_data` |  | The account (if any) the subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices. |
| `trial_end` | timestamp (Unix seconds) |  | If the subscription has a trial, the end of that trial. |
| `trial_settings` | `subscriptions_trials_resource_trial_settings` |  | Settings related to subscription trials. |
| `trial_start` | timestamp (Unix seconds) |  | If the subscription has a trial, the beginning of that trial. |

## The `tax_id` object

You can add one or multiple tax IDs to a [customer](https://stripe.com/docs/api/customers) or account.
Customer and account tax IDs get displayed on related invoices and credit notes.

Related guides: [Customer tax identification numbers](https://stripe.com/docs/billing/taxes/tax-ids), [Account tax IDs](https://stripe.com/docs/invoicing/connect#account-tax-ids)

Expandable fields (pass `expand[]=<field>`): `customer`, `owner`, `verification`

| Field | Type | Required | Description |
|---|---|---|---|
| `country` | string |  | Two-letter ISO code representing the country of the tax ID. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` |  | ID of the customer. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `tax_id` | yes | String representing the object's type. Objects of the same type share the same value. |
| `owner` | `tax_i_ds_owner` |  | The account or customer the tax ID belongs to. |
| `type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `unknown`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes | Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`. Note that some legacy tax IDs have type `unknown` |
| `value` | string | yes | Value of the tax ID. |
| `verification` | `tax_id_verification` |  | Tax ID verification information. |

## The `deleted_tax_id` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `tax_id` | yes | String representing the object's type. Objects of the same type share the same value. |

