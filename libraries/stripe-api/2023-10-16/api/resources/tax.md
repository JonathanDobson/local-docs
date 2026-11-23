# Stripe API 2023-10-16 — tax

Operations under `/v1/tax` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/tax/calculations

operationId: `PostTaxCalculations`

Calculates tax based on input and returns a Tax `Calculation` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`. |
| `customer_details` | object |  | Details about the customer, including address and tax IDs. |
| `customer_details.address` | object |  |  |
| `customer_details.address.city` | string or "" (to unset) |  |  |
| `customer_details.address.country` | string | yes |  |
| `customer_details.address.line1` | string or "" (to unset) |  |  |
| `customer_details.address.line2` | string or "" (to unset) |  |  |
| `customer_details.address.postal_code` | string or "" (to unset) |  |  |
| `customer_details.address.state` | string or "" (to unset) |  |  |
| `customer_details.address_source` | enum: `billing`, `shipping` |  |  |
| `customer_details.ip_address` | string |  |  |
| `customer_details.tax_ids` | array of object |  |  |
| `customer_details.tax_ids[].type` | enum: `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, `za_vat` | yes |  |
| `customer_details.tax_ids[].value` | string | yes |  |
| `customer_details.taxability_override` | enum: `customer_exempt`, `none`, `reverse_charge` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `line_items` | array of object | yes | A list of items the customer is purchasing. |
| `line_items[].amount` | integer | yes |  |
| `line_items[].product` | string |  |  |
| `line_items[].quantity` | integer |  |  |
| `line_items[].reference` | string |  |  |
| `line_items[].tax_behavior` | enum: `exclusive`, `inclusive` |  |  |
| `line_items[].tax_code` | string |  |  |
| `shipping_cost` | object |  | Shipping cost details to be used for the calculation. |
| `shipping_cost.amount` | integer |  |  |
| `shipping_cost.shipping_rate` | string |  |  |
| `shipping_cost.tax_behavior` | enum: `exclusive`, `inclusive` |  |  |
| `shipping_cost.tax_code` | string |  |  |
| `tax_date` | integer |  | Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future. |

Returns: `tax.calculation`

## GET /v1/tax/calculations/{calculation}/line_items

operationId: `GetTaxCalculationsCalculationLineItems`

Retrieves the line items of a persisted tax calculation as a collection.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `calculation (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/tax/registrations

operationId: `GetTaxRegistrations`

Returns a list of Tax `Registration` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `all`, `expired`, `scheduled` |  | The status of the Tax Registration. |

Returns: object

## POST /v1/tax/registrations

operationId: `PostTaxRegistrations`

Creates a new Tax `Registration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active_from` | enum: `now` or timestamp (Unix seconds) | yes | Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch. |
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `country_options` | object | yes | Specific options for a registration in the specified `country`. |
| `country_options.ae` | object |  |  |
| `country_options.ae.type` | enum: `standard` | yes |  |
| `country_options.at` | object |  |  |
| `country_options.at.standard` | object |  |  |
| `country_options.at.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.at.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.au` | object |  |  |
| `country_options.au.type` | enum: `standard` | yes |  |
| `country_options.be` | object |  |  |
| `country_options.be.standard` | object |  |  |
| `country_options.be.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.be.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.bg` | object |  |  |
| `country_options.bg.standard` | object |  |  |
| `country_options.bg.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.bg.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.ca` | object |  |  |
| `country_options.ca.province_standard` | object |  |  |
| `country_options.ca.province_standard.province` | string | yes |  |
| `country_options.ca.type` | enum: `province_standard`, `simplified`, `standard` | yes |  |
| `country_options.ch` | object |  |  |
| `country_options.ch.type` | enum: `standard` | yes |  |
| `country_options.cl` | object |  |  |
| `country_options.cl.type` | enum: `simplified` | yes |  |
| `country_options.co` | object |  |  |
| `country_options.co.type` | enum: `simplified` | yes |  |
| `country_options.cy` | object |  |  |
| `country_options.cy.standard` | object |  |  |
| `country_options.cy.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.cy.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.cz` | object |  |  |
| `country_options.cz.standard` | object |  |  |
| `country_options.cz.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.cz.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.de` | object |  |  |
| `country_options.de.standard` | object |  |  |
| `country_options.de.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.de.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.dk` | object |  |  |
| `country_options.dk.standard` | object |  |  |
| `country_options.dk.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.dk.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.ee` | object |  |  |
| `country_options.ee.standard` | object |  |  |
| `country_options.ee.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.ee.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.es` | object |  |  |
| `country_options.es.standard` | object |  |  |
| `country_options.es.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.es.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.fi` | object |  |  |
| `country_options.fi.standard` | object |  |  |
| `country_options.fi.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.fi.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.fr` | object |  |  |
| `country_options.fr.standard` | object |  |  |
| `country_options.fr.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.fr.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.gb` | object |  |  |
| `country_options.gb.type` | enum: `standard` | yes |  |
| `country_options.gr` | object |  |  |
| `country_options.gr.standard` | object |  |  |
| `country_options.gr.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.gr.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.hr` | object |  |  |
| `country_options.hr.standard` | object |  |  |
| `country_options.hr.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.hr.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.hu` | object |  |  |
| `country_options.hu.standard` | object |  |  |
| `country_options.hu.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.hu.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.id` | object |  |  |
| `country_options.id.type` | enum: `simplified` | yes |  |
| `country_options.ie` | object |  |  |
| `country_options.ie.standard` | object |  |  |
| `country_options.ie.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.ie.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.is` | object |  |  |
| `country_options.is.type` | enum: `standard` | yes |  |
| `country_options.it` | object |  |  |
| `country_options.it.standard` | object |  |  |
| `country_options.it.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.it.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.jp` | object |  |  |
| `country_options.jp.type` | enum: `standard` | yes |  |
| `country_options.kr` | object |  |  |
| `country_options.kr.type` | enum: `simplified` | yes |  |
| `country_options.lt` | object |  |  |
| `country_options.lt.standard` | object |  |  |
| `country_options.lt.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.lt.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.lu` | object |  |  |
| `country_options.lu.standard` | object |  |  |
| `country_options.lu.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.lu.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.lv` | object |  |  |
| `country_options.lv.standard` | object |  |  |
| `country_options.lv.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.lv.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.mt` | object |  |  |
| `country_options.mt.standard` | object |  |  |
| `country_options.mt.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.mt.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.mx` | object |  |  |
| `country_options.mx.type` | enum: `simplified` | yes |  |
| `country_options.my` | object |  |  |
| `country_options.my.type` | enum: `simplified` | yes |  |
| `country_options.nl` | object |  |  |
| `country_options.nl.standard` | object |  |  |
| `country_options.nl.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.nl.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.no` | object |  |  |
| `country_options.no.type` | enum: `standard` | yes |  |
| `country_options.nz` | object |  |  |
| `country_options.nz.type` | enum: `standard` | yes |  |
| `country_options.pl` | object |  |  |
| `country_options.pl.standard` | object |  |  |
| `country_options.pl.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.pl.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.pt` | object |  |  |
| `country_options.pt.standard` | object |  |  |
| `country_options.pt.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.pt.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.ro` | object |  |  |
| `country_options.ro.standard` | object |  |  |
| `country_options.ro.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.ro.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.sa` | object |  |  |
| `country_options.sa.type` | enum: `simplified` | yes |  |
| `country_options.se` | object |  |  |
| `country_options.se.standard` | object |  |  |
| `country_options.se.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.se.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.sg` | object |  |  |
| `country_options.sg.type` | enum: `standard` | yes |  |
| `country_options.si` | object |  |  |
| `country_options.si.standard` | object |  |  |
| `country_options.si.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.si.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.sk` | object |  |  |
| `country_options.sk.standard` | object |  |  |
| `country_options.sk.standard.place_of_supply_scheme` | enum: `small_seller`, `standard` | yes |  |
| `country_options.sk.type` | enum: `ioss`, `oss_non_union`, `oss_union`, `standard` | yes |  |
| `country_options.th` | object |  |  |
| `country_options.th.type` | enum: `simplified` | yes |  |
| `country_options.tr` | object |  |  |
| `country_options.tr.type` | enum: `simplified` | yes |  |
| `country_options.us` | object |  |  |
| `country_options.us.local_amusement_tax` | object |  |  |
| `country_options.us.local_amusement_tax.jurisdiction` | string | yes |  |
| `country_options.us.local_lease_tax` | object |  |  |
| `country_options.us.local_lease_tax.jurisdiction` | string | yes |  |
| `country_options.us.state` | string | yes |  |
| `country_options.us.type` | enum: `local_amusement_tax`, `local_lease_tax`, `state_communications_tax`, `state_sales_tax` | yes |  |
| `country_options.vn` | object |  |  |
| `country_options.vn.type` | enum: `simplified` | yes |  |
| `country_options.za` | object |  |  |
| `country_options.za.type` | enum: `standard` | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch. |

Returns: `tax.registration`

## GET /v1/tax/registrations/{id}

operationId: `GetTaxRegistrationsId`

Returns a Tax `Registration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `tax.registration`

## POST /v1/tax/registrations/{id}

operationId: `PostTaxRegistrationsId`

Updates an existing Tax `Registration` object.

A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting `expires_at`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `active_from` | enum: `now` or timestamp (Unix seconds) |  | Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | enum: `now` or timestamp (Unix seconds) or "" (to unset) |  | If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch. |

Returns: `tax.registration`

## GET /v1/tax/settings

operationId: `GetTaxSettings`

Retrieves Tax `Settings` for a merchant.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `tax.settings`

## POST /v1/tax/settings

operationId: `PostTaxSettings`

Updates Tax `Settings` parameters used in tax calculations. All parameters are editable but none can be removed once set.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `defaults` | object |  | Default configuration to be used on Stripe Tax calculations. |
| `defaults.tax_behavior` | enum: `exclusive`, `inclusive`, `inferred_by_currency` |  |  |
| `defaults.tax_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `head_office` | object |  | The place where your business is located. |
| `head_office.address` | object | yes |  |
| `head_office.address.city` | string |  |  |
| `head_office.address.country` | string |  |  |
| `head_office.address.line1` | string |  |  |
| `head_office.address.line2` | string |  |  |
| `head_office.address.postal_code` | string |  |  |
| `head_office.address.state` | string |  |  |

Returns: `tax.settings`

## POST /v1/tax/transactions/create_from_calculation

operationId: `PostTaxTransactionsCreateFromCalculation`

Creates a Tax `Transaction` from a calculation.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `calculation` | string | yes | Tax Calculation ID to be used as input when creating the transaction. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `reference` | string | yes | A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals. |

Returns: `tax.transaction`

## POST /v1/tax/transactions/create_reversal

operationId: `PostTaxTransactionsCreateReversal`

Partially or fully reverses a previously created `Transaction`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `flat_amount` | integer |  | A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes. |
| `line_items` | array of object |  | The line item amounts to reverse. |
| `line_items[].amount` | integer | yes |  |
| `line_items[].amount_tax` | integer | yes |  |
| `line_items[].metadata` | map (key → value) |  |  |
| `line_items[].original_line_item` | string | yes |  |
| `line_items[].quantity` | integer |  |  |
| `line_items[].reference` | string | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `mode` | enum: `full`, `partial` | yes | If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed. |
| `original_transaction` | string | yes | The ID of the Transaction to partially or fully reverse. |
| `reference` | string | yes | A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports). |
| `shipping_cost` | object |  | The shipping cost to reverse. |
| `shipping_cost.amount` | integer | yes |  |
| `shipping_cost.amount_tax` | integer | yes |  |

Returns: `tax.transaction`

## GET /v1/tax/transactions/{transaction}

operationId: `GetTaxTransactionsTransaction`

Retrieves a Tax `Transaction` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transaction (path)` | string | yes |  |

Returns: `tax.transaction`

## GET /v1/tax/transactions/{transaction}/line_items

operationId: `GetTaxTransactionsTransactionLineItems`

Retrieves the line items of a committed standalone transaction as a collection.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `transaction (path)` | string | yes |  |

Returns: object

# Objects returned

## The `tax.calculation` object

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom)

Expandable fields (pass `expand[]=<field>`): `customer_details`, `line_items`, `shipping_cost`, `tax_breakdown`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_total` | integer | yes | Total after taxes. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource. |
| `customer_details` | `tax_product_resource_customer_details` | yes |  |
| `expires_at` | timestamp (Unix seconds) |  | Timestamp of date at which the tax calculation will expire. |
| `id` | string |  | Unique identifier for the calculation. |
| `line_items` | object |  | The list of items the customer is purchasing. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `tax.calculation` | yes | String representing the object's type. Objects of the same type share the same value. |
| `shipping_cost` | `tax_product_resource_tax_calculation_shipping_cost` |  | The shipping cost details for the calculation. |
| `tax_amount_exclusive` | integer | yes | The amount of tax to be collected on top of the line item prices. |
| `tax_amount_inclusive` | integer | yes | The amount of tax already included in the line item prices. |
| `tax_breakdown` | array of `tax_product_resource_tax_breakdown` | yes | Breakdown of individual tax amounts that add up to the total. |
| `tax_date` | timestamp (Unix seconds) | yes | Timestamp of date at which the tax rules and rates in effect applies for the calculation. |

## The `tax.registration` object

A Tax `Registration` lets us know that your business is registered to collect tax on payments within a region, enabling you to [automatically collect tax](https://stripe.com/docs/tax).

Stripe doesn't register on your behalf with the relevant authorities when you create a Tax `Registration` object. For more information on how to register to collect tax, see [our guide](https://stripe.com/docs/tax/registering).

Related guide: [Using the Registrations API](https://stripe.com/docs/tax/registrations-api)

Expandable fields (pass `expand[]=<field>`): `country_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `active_from` | timestamp (Unix seconds) | yes | Time at which the registration becomes active. Measured in seconds since the Unix epoch. |
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `country_options` | `tax_product_registrations_resource_country_options` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires_at` | timestamp (Unix seconds) |  | If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `tax.registration` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `active`, `expired`, `scheduled` | yes | The status of the registration. This field is present for convenience and can be deduced from `active_from` and `expires_at`. |

## The `tax.settings` object

You can use Tax `Settings` to manage configurations used by Stripe Tax calculations.

Related guide: [Using the Settings API](https://stripe.com/docs/tax/settings-api)

Expandable fields (pass `expand[]=<field>`): `defaults`, `head_office`, `status_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `defaults` | `tax_product_resource_tax_settings_defaults` | yes |  |
| `head_office` | `tax_product_resource_tax_settings_head_office` |  | The place where your business is located. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `tax.settings` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `active`, `pending` | yes | The `active` status indicates you have all required settings to calculate tax. A status can transition out of `active` when new required settings are introduced. |
| `status_details` | `tax_product_resource_tax_settings_status_details` | yes |  |

## The `tax.transaction` object

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom#tax-transaction)

Expandable fields (pass `expand[]=<field>`): `customer_details`, `line_items`, `reversal`, `shipping_cost`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource. |
| `customer_details` | `tax_product_resource_customer_details` | yes |  |
| `id` | string | yes | Unique identifier for the transaction. |
| `line_items` | object |  | The tax collected or refunded, by line item. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `tax.transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reference` | string | yes | A custom unique identifier, such as 'myOrder_123'. |
| `reversal` | `tax_product_resource_tax_transaction_resource_reversal` |  | If `type=reversal`, contains information about what was reversed. |
| `shipping_cost` | `tax_product_resource_tax_transaction_shipping_cost` |  | The shipping cost details for the transaction. |
| `tax_date` | timestamp (Unix seconds) | yes | Timestamp of date at which the tax rules and rates in effect applies for the calculation. |
| `type` | enum: `reversal`, `transaction` | yes | If `reversal`, this transaction reverses an earlier transaction. |

