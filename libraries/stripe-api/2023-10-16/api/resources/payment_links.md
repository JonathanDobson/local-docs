# Stripe API 2023-10-16 — payment links

Operations under `/v1/payment_links` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payment_links

operationId: `GetPaymentLinks`

Returns a list of your payment links.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links). |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/payment_links

operationId: `PostPaymentLinks`

Creates a payment link.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `after_completion` | object |  | Behavior after the purchase is complete. |
| `after_completion.hosted_confirmation` | object |  |  |
| `after_completion.hosted_confirmation.custom_message` | string |  |  |
| `after_completion.redirect` | object |  |  |
| `after_completion.redirect.url` | string | yes |  |
| `after_completion.type` | enum: `hosted_confirmation`, `redirect` | yes |  |
| `allow_promotion_codes` | boolean |  | Enables user redeemable promotion codes. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices. |
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field. |
| `automatic_tax` | object |  | Configuration for automatic tax collection. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `billing_address_collection` | enum: `auto`, `required` |  | Configuration for collecting the customer's billing address. Defaults to `auto`. |
| `consent_collection` | object |  | Configure fields to gather active consent from customers. |
| `consent_collection.payment_method_reuse_agreement` | object |  |  |
| `consent_collection.payment_method_reuse_agreement.position` | enum: `auto`, `hidden` | yes |  |
| `consent_collection.promotions` | enum: `auto`, `none` |  |  |
| `consent_collection.terms_of_service` | enum: `none`, `required` |  |  |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price. |
| `custom_fields` | array of object |  | Collect additional information from your customer using custom fields. Up to 3 fields are supported. |
| `custom_fields[].dropdown` | object |  |  |
| `custom_fields[].dropdown.options` | array of object | yes |  |
| `custom_fields[].dropdown.options[].label` | string | yes |  |
| `custom_fields[].dropdown.options[].value` | string | yes |  |
| `custom_fields[].key` | string | yes |  |
| `custom_fields[].label` | object | yes |  |
| `custom_fields[].label.custom` | string | yes |  |
| `custom_fields[].label.type` | enum: `custom` | yes |  |
| `custom_fields[].numeric` | object |  |  |
| `custom_fields[].numeric.maximum_length` | integer |  |  |
| `custom_fields[].numeric.minimum_length` | integer |  |  |
| `custom_fields[].optional` | boolean |  |  |
| `custom_fields[].text` | object |  |  |
| `custom_fields[].text.maximum_length` | integer |  |  |
| `custom_fields[].text.minimum_length` | integer |  |  |
| `custom_fields[].type` | enum: `dropdown`, `numeric`, `text` | yes |  |
| `custom_text` | object |  | Display additional text for your customers using custom text. |
| `custom_text.after_submit` | object or "" (to unset) |  |  |
| `custom_text.after_submit.message` | string | yes |  |
| `custom_text.shipping_address` | object or "" (to unset) |  |  |
| `custom_text.shipping_address.message` | string | yes |  |
| `custom_text.submit` | object or "" (to unset) |  |  |
| `custom_text.submit.message` | string | yes |  |
| `custom_text.terms_of_service_acceptance` | object or "" (to unset) |  |  |
| `custom_text.terms_of_service_acceptance.message` | string | yes |  |
| `customer_creation` | enum: `always`, `if_required` |  | Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `inactive_message` | string |  | The custom message to be displayed to a customer when a payment link is no longer active. |
| `invoice_creation` | object |  | Generate a post-purchase Invoice for one-time payments. |
| `invoice_creation.enabled` | boolean | yes |  |
| `invoice_creation.invoice_data` | object |  |  |
| `invoice_creation.invoice_data.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_creation.invoice_data.custom_fields` | array of object or "" (to unset) |  |  |
| `invoice_creation.invoice_data.custom_fields[].name` | string | yes |  |
| `invoice_creation.invoice_data.custom_fields[].value` | string | yes |  |
| `invoice_creation.invoice_data.description` | string |  |  |
| `invoice_creation.invoice_data.footer` | string |  |  |
| `invoice_creation.invoice_data.issuer` | object |  |  |
| `invoice_creation.invoice_data.issuer.account` | string |  |  |
| `invoice_creation.invoice_data.issuer.type` | enum: `account`, `self` | yes |  |
| `invoice_creation.invoice_data.metadata` | map (key → value) or "" (to unset) |  |  |
| `invoice_creation.invoice_data.rendering_options` | object or "" (to unset) |  |  |
| `invoice_creation.invoice_data.rendering_options.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `line_items` | array of object | yes | The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported. |
| `line_items[].adjustable_quantity` | object |  |  |
| `line_items[].adjustable_quantity.enabled` | boolean | yes |  |
| `line_items[].adjustable_quantity.maximum` | integer |  |  |
| `line_items[].adjustable_quantity.minimum` | integer |  |  |
| `line_items[].price` | string | yes |  |
| `line_items[].quantity` | integer | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link. |
| `on_behalf_of` | string |  | The account on behalf of which to charge. |
| `payment_intent_data` | object |  | A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode. |
| `payment_intent_data.capture_method` | enum: `automatic`, `automatic_async`, `manual` |  |  |
| `payment_intent_data.description` | string |  |  |
| `payment_intent_data.metadata` | map (key → value) |  |  |
| `payment_intent_data.setup_future_usage` | enum: `off_session`, `on_session` |  |  |
| `payment_intent_data.statement_descriptor` | string |  |  |
| `payment_intent_data.statement_descriptor_suffix` | string |  |  |
| `payment_intent_data.transfer_group` | string |  |  |
| `payment_method_collection` | enum: `always`, `if_required` |  | Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.<br>Can only be set in `subscription` mode. Defaults to `always`.<br>If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials). |
| `payment_method_types` | array of enum: `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay` |  | The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)). |
| `phone_number_collection` | object |  | Controls phone number collection settings during checkout.<br>We recommend that you review your privacy policy and check with your legal contacts. |
| `phone_number_collection.enabled` | boolean | yes |  |
| `restrictions` | object |  | Settings that restrict the usage of a payment link. |
| `restrictions.completed_sessions` | object | yes |  |
| `restrictions.completed_sessions.limit` | integer | yes |  |
| `shipping_address_collection` | object |  | Configuration for collecting the customer's shipping address. |
| `shipping_address_collection.allowed_countries` | array of enum: `AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AO`, `AQ`, `AR`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CR`, `CV`, `CW`, `CY`, `CZ`, `DE`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `FI`, `FJ`, `FK`, `FO`, `FR`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HN`, `HR`, `HT`, `HU`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MK`, `ML`, `MM`, `MN`, `MO`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SE`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SV`, `SX`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TH`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `ZA`, `ZM`, `ZW`, `ZZ` | yes |  |
| `shipping_options` | array of object |  | The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link. |
| `shipping_options[].shipping_rate` | string |  |  |
| `submit_type` | enum: `auto`, `book`, `donate`, `pay` |  | Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`). |
| `subscription_data` | object |  | When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`. |
| `subscription_data.description` | string |  |  |
| `subscription_data.invoice_settings` | object |  |  |
| `subscription_data.invoice_settings.issuer` | object |  |  |
| `subscription_data.invoice_settings.issuer.account` | string |  |  |
| `subscription_data.invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `subscription_data.metadata` | map (key → value) |  |  |
| `subscription_data.trial_period_days` | integer |  |  |
| `subscription_data.trial_settings` | object |  |  |
| `subscription_data.trial_settings.end_behavior` | object | yes |  |
| `subscription_data.trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |
| `tax_id_collection` | object |  | Controls tax ID collection during checkout. |
| `tax_id_collection.enabled` | boolean | yes |  |
| `transfer_data` | object |  | The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.destination` | string | yes |  |

Returns: `payment_link`

## GET /v1/payment_links/{payment_link}

operationId: `GetPaymentLinksPaymentLink`

Retrieve a payment link.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_link (path)` | string | yes |  |

Returns: `payment_link`

## POST /v1/payment_links/{payment_link}

operationId: `PostPaymentLinksPaymentLink`

Updates a payment link.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_link (path)` | string | yes |  |
| `active` | boolean |  | Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated. |
| `after_completion` | object |  | Behavior after the purchase is complete. |
| `after_completion.hosted_confirmation` | object |  |  |
| `after_completion.hosted_confirmation.custom_message` | string |  |  |
| `after_completion.redirect` | object |  |  |
| `after_completion.redirect.url` | string | yes |  |
| `after_completion.type` | enum: `hosted_confirmation`, `redirect` | yes |  |
| `allow_promotion_codes` | boolean |  | Enables user redeemable promotion codes. |
| `automatic_tax` | object |  | Configuration for automatic tax collection. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `billing_address_collection` | enum: `auto`, `required` |  | Configuration for collecting the customer's billing address. Defaults to `auto`. |
| `custom_fields` | array of object or "" (to unset) |  | Collect additional information from your customer using custom fields. Up to 3 fields are supported. |
| `custom_fields[].dropdown` | object |  |  |
| `custom_fields[].dropdown.options` | array of object | yes |  |
| `custom_fields[].dropdown.options[].label` | string | yes |  |
| `custom_fields[].dropdown.options[].value` | string | yes |  |
| `custom_fields[].key` | string | yes |  |
| `custom_fields[].label` | object | yes |  |
| `custom_fields[].label.custom` | string | yes |  |
| `custom_fields[].label.type` | enum: `custom` | yes |  |
| `custom_fields[].numeric` | object |  |  |
| `custom_fields[].numeric.maximum_length` | integer |  |  |
| `custom_fields[].numeric.minimum_length` | integer |  |  |
| `custom_fields[].optional` | boolean |  |  |
| `custom_fields[].text` | object |  |  |
| `custom_fields[].text.maximum_length` | integer |  |  |
| `custom_fields[].text.minimum_length` | integer |  |  |
| `custom_fields[].type` | enum: `dropdown`, `numeric`, `text` | yes |  |
| `custom_text` | object |  | Display additional text for your customers using custom text. |
| `custom_text.after_submit` | object or "" (to unset) |  |  |
| `custom_text.after_submit.message` | string | yes |  |
| `custom_text.shipping_address` | object or "" (to unset) |  |  |
| `custom_text.shipping_address.message` | string | yes |  |
| `custom_text.submit` | object or "" (to unset) |  |  |
| `custom_text.submit.message` | string | yes |  |
| `custom_text.terms_of_service_acceptance` | object or "" (to unset) |  |  |
| `custom_text.terms_of_service_acceptance.message` | string | yes |  |
| `customer_creation` | enum: `always`, `if_required` |  | Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `inactive_message` | string or "" (to unset) |  | The custom message to be displayed to a customer when a payment link is no longer active. |
| `invoice_creation` | object |  | Generate a post-purchase Invoice for one-time payments. |
| `invoice_creation.enabled` | boolean | yes |  |
| `invoice_creation.invoice_data` | object |  |  |
| `invoice_creation.invoice_data.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_creation.invoice_data.custom_fields` | array of object or "" (to unset) |  |  |
| `invoice_creation.invoice_data.custom_fields[].name` | string | yes |  |
| `invoice_creation.invoice_data.custom_fields[].value` | string | yes |  |
| `invoice_creation.invoice_data.description` | string |  |  |
| `invoice_creation.invoice_data.footer` | string |  |  |
| `invoice_creation.invoice_data.issuer` | object |  |  |
| `invoice_creation.invoice_data.issuer.account` | string |  |  |
| `invoice_creation.invoice_data.issuer.type` | enum: `account`, `self` | yes |  |
| `invoice_creation.invoice_data.metadata` | map (key → value) or "" (to unset) |  |  |
| `invoice_creation.invoice_data.rendering_options` | object or "" (to unset) |  |  |
| `invoice_creation.invoice_data.rendering_options.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `line_items` | array of object |  | The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported. |
| `line_items[].adjustable_quantity` | object |  |  |
| `line_items[].adjustable_quantity.enabled` | boolean | yes |  |
| `line_items[].adjustable_quantity.maximum` | integer |  |  |
| `line_items[].adjustable_quantity.minimum` | integer |  |  |
| `line_items[].id` | string | yes |  |
| `line_items[].quantity` | integer |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link. |
| `payment_intent_data` | object |  | A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode. |
| `payment_intent_data.description` | string or "" (to unset) |  |  |
| `payment_intent_data.metadata` | map (key → value) or "" (to unset) |  |  |
| `payment_intent_data.statement_descriptor` | string or "" (to unset) |  |  |
| `payment_intent_data.statement_descriptor_suffix` | string or "" (to unset) |  |  |
| `payment_intent_data.transfer_group` | string or "" (to unset) |  |  |
| `payment_method_collection` | enum: `always`, `if_required` |  | Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.<br>Can only be set in `subscription` mode. Defaults to `always`.<br>If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials). |
| `payment_method_types` | array of enum: `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay` or "" (to unset) |  | The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). |
| `restrictions` | object or "" (to unset) |  | Settings that restrict the usage of a payment link. |
| `restrictions.completed_sessions` | object | yes |  |
| `restrictions.completed_sessions.limit` | integer | yes |  |
| `shipping_address_collection` | object or "" (to unset) |  | Configuration for collecting the customer's shipping address. |
| `shipping_address_collection.allowed_countries` | array of enum: `AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AO`, `AQ`, `AR`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CR`, `CV`, `CW`, `CY`, `CZ`, `DE`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `FI`, `FJ`, `FK`, `FO`, `FR`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HN`, `HR`, `HT`, `HU`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MK`, `ML`, `MM`, `MN`, `MO`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SE`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SV`, `SX`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TH`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `ZA`, `ZM`, `ZW`, `ZZ` | yes |  |
| `subscription_data` | object |  | When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`. |
| `subscription_data.invoice_settings` | object |  |  |
| `subscription_data.invoice_settings.issuer` | object |  |  |
| `subscription_data.invoice_settings.issuer.account` | string |  |  |
| `subscription_data.invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `subscription_data.metadata` | map (key → value) or "" (to unset) |  |  |
| `subscription_data.trial_settings` | object or "" (to unset) |  |  |
| `subscription_data.trial_settings.end_behavior` | object | yes |  |
| `subscription_data.trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |

Returns: `payment_link`

## GET /v1/payment_links/{payment_link}/line_items

operationId: `GetPaymentLinksPaymentLinkLineItems`

When retrieving a payment link, there is an includable **line_items** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_link (path)` | string | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

# Objects returned

## The `payment_link` object

A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

When a customer opens a payment link it will open a new [checkout session](https://stripe.com/docs/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://stripe.com/docs/api/events/types#event_types-checkout.session.completed) to track payments through payment links.

Related guide: [Payment Links API](https://stripe.com/docs/payment-links)

Expandable fields (pass `expand[]=<field>`): `after_completion`, `application`, `automatic_tax`, `consent_collection`, `custom_fields`, `custom_text`, `invoice_creation`, `line_items`, `on_behalf_of`, `payment_intent_data`, `phone_number_collection`, `restrictions`, `shipping_address_collection`, `shipping_options`, `subscription_data`, `tax_id_collection`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated. |
| `after_completion` | `payment_links_resource_after_completion` | yes |  |
| `allow_promotion_codes` | boolean | yes | Whether user redeemable promotion codes are enabled. |
| `application` | string or `application` or `deleted_application` |  | The ID of the Connect application that created the Payment Link. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. |
| `application_fee_percent` | number |  | This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. |
| `automatic_tax` | `payment_links_resource_automatic_tax` | yes |  |
| `billing_address_collection` | enum: `auto`, `required` | yes | Configuration for collecting the customer's billing address. Defaults to `auto`. |
| `consent_collection` | `payment_links_resource_consent_collection` |  | When set, provides configuration to gather active consent from customers. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `custom_fields` | array of `payment_links_resource_custom_fields` | yes | Collect additional information from your customer using custom fields. Up to 3 fields are supported. |
| `custom_text` | `payment_links_resource_custom_text` | yes |  |
| `customer_creation` | enum: `always`, `if_required` | yes | Configuration for Customer creation during checkout. |
| `id` | string | yes | Unique identifier for the object. |
| `inactive_message` | string |  | The custom message to be displayed to a customer when a payment link is no longer active. |
| `invoice_creation` | `payment_links_resource_invoice_creation` |  | Configuration for creating invoice for payment mode payment links. |
| `line_items` | object |  | The line items representing what is being sold. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `payment_link` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details. |
| `payment_intent_data` | `payment_links_resource_payment_intent_data` |  | Indicates the parameters to be passed to PaymentIntent creation during checkout. |
| `payment_method_collection` | enum: `always`, `if_required` | yes | Configuration for collecting a payment method during checkout. Defaults to `always`. |
| `payment_method_types` | array of enum: `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay` |  | The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you've enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). |
| `phone_number_collection` | `payment_links_resource_phone_number_collection` | yes |  |
| `restrictions` | `payment_links_resource_restrictions` |  | Settings that restrict the usage of a payment link. |
| `shipping_address_collection` | `payment_links_resource_shipping_address_collection` |  | Configuration for collecting the customer's shipping address. |
| `shipping_options` | array of `payment_links_resource_shipping_option` | yes | The shipping rate options applied to the session. |
| `submit_type` | enum: `auto`, `book`, `donate`, `pay` | yes | Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button. |
| `subscription_data` | `payment_links_resource_subscription_data` |  | When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`. |
| `tax_id_collection` | `payment_links_resource_tax_id_collection` | yes |  |
| `transfer_data` | `payment_links_resource_transfer_data` |  | The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to. |
| `url` | string | yes | The public URL that can be shared with customers. |

