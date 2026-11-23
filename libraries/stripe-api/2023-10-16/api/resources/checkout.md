# Stripe API 2023-10-16 — checkout

Operations under `/v1/checkout` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/checkout/sessions

operationId: `GetCheckoutSessions`

Returns a list of Checkout Sessions.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return Checkout Sessions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return the Checkout Sessions for the Customer specified. |
| `customer_details` | object |  | Only return the Checkout Sessions for the Customer details specified. |
| `customer_details.email` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_intent` | string |  | Only return the Checkout Session for the PaymentIntent specified. |
| `payment_link` | string |  | Only return the Checkout Sessions for the Payment Link specified. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `complete`, `expired`, `open` |  | Only return the Checkout Sessions matching the given status. |
| `subscription` | string |  | Only return the Checkout Session for the subscription specified. |

Returns: object

## POST /v1/checkout/sessions

operationId: `PostCheckoutSessions`

Creates a Session object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `after_expiration` | object |  | Configure actions after a Checkout Session has expired. |
| `after_expiration.recovery` | object |  |  |
| `after_expiration.recovery.allow_promotion_codes` | boolean |  |  |
| `after_expiration.recovery.enabled` | boolean | yes |  |
| `allow_promotion_codes` | boolean |  | Enables user redeemable promotion codes. |
| `automatic_tax` | object |  | Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `billing_address_collection` | enum: `auto`, `required` |  | Specify whether Checkout should collect the customer's billing address. Defaults to `auto`. |
| `cancel_url` | string |  | If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. |
| `client_reference_id` | string |  | A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems. |
| `consent_collection` | object |  | Configure fields for the Checkout Session to gather active consent from customers. |
| `consent_collection.payment_method_reuse_agreement` | object |  |  |
| `consent_collection.payment_method_reuse_agreement.position` | enum: `auto`, `hidden` | yes |  |
| `consent_collection.promotions` | enum: `auto`, `none` |  |  |
| `consent_collection.terms_of_service` | enum: `none`, `required` |  |  |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Required in `setup` mode when `payment_method_types` is not set. |
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
| `customer` | string |  | ID of an existing Customer, if one exists. In `payment` mode, the customer’s most recently saved card payment method will be used to prefill the email, name, card details, and billing address on the Checkout page. In `subscription` mode, the customer’s [default payment method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer's card details.<br>If the Customer already has a valid [email](https://stripe.com/docs/api/customers/object#customer_object-email) set, the email will be prefilled and not editable in Checkout. If the Customer does not have a valid `email`, Checkout will set the email entered during the session on the Customer.<br>If blank for Checkout Sessions in `subscription` mode or with `customer_creation` set as `always` in `payment` mode, Checkout will create a new Customer object based on information provided during the payment flow.<br>You can set [`payment_intent_data.setup_future_usage`](https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) to have Checkout automatically attach the payment method to the Customer you pass in for future reuse. |
| `customer_creation` | enum: `always`, `if_required` |  | Configure whether a Checkout Session creates a [Customer](https://stripe.com/docs/api/customers) during Session confirmation.<br>When a Customer is not created, you can still retrieve email, address, and other customer data entered in Checkout with [customer_details](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-customer_details).<br>Sessions that don't create Customers instead are grouped by [guest customers](https://stripe.com/docs/payments/checkout/guest-customers) in the Dashboard. Promotion codes limited to first time customers will return invalid for these Sessions.<br>Can only be set in `payment` and `setup` mode. |
| `customer_email` | string |  | If provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once a session is complete, use the `customer` field. |
| `customer_update` | object |  | Controls what fields on Customer can be updated by the Checkout Session. Can only be provided when `customer` is provided. |
| `customer_update.address` | enum: `auto`, `never` |  |  |
| `customer_update.name` | enum: `auto`, `never` |  |  |
| `customer_update.shipping` | enum: `auto`, `never` |  |  |
| `discounts` | array of object |  | The coupon or promotion code to apply to this Session. Currently, only up to one may be specified. |
| `discounts[].coupon` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | The Epoch time in seconds at which the Checkout Session will expire. It can be anywhere from 30 minutes to 24 hours after Checkout Session creation. By default, this value is 24 hours from creation. |
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
| `invoice_creation.invoice_data.metadata` | map (key → value) |  |  |
| `invoice_creation.invoice_data.rendering_options` | object or "" (to unset) |  |  |
| `invoice_creation.invoice_data.rendering_options.amount_tax_display` | enum: ``, `exclude_tax`, `include_inclusive_tax` |  |  |
| `line_items` | array of object |  | A list of items the customer is purchasing. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).<br>For `payment` mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.<br>For `subscription` mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only. |
| `line_items[].adjustable_quantity` | object |  |  |
| `line_items[].adjustable_quantity.enabled` | boolean | yes |  |
| `line_items[].adjustable_quantity.maximum` | integer |  |  |
| `line_items[].adjustable_quantity.minimum` | integer |  |  |
| `line_items[].dynamic_tax_rates` | array of string |  |  |
| `line_items[].price` | string |  |  |
| `line_items[].price_data` | object |  |  |
| `line_items[].price_data.currency` | string | yes |  |
| `line_items[].price_data.product` | string |  |  |
| `line_items[].price_data.product_data` | object |  |  |
| `line_items[].price_data.product_data.description` | string |  |  |
| `line_items[].price_data.product_data.images` | array of string |  |  |
| `line_items[].price_data.product_data.metadata` | map (key → value) |  |  |
| `line_items[].price_data.product_data.name` | string | yes |  |
| `line_items[].price_data.product_data.tax_code` | string |  |  |
| `line_items[].price_data.recurring` | object |  |  |
| `line_items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `line_items[].price_data.recurring.interval_count` | integer |  |  |
| `line_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `line_items[].price_data.unit_amount` | integer |  |  |
| `line_items[].price_data.unit_amount_decimal` | string |  |  |
| `line_items[].quantity` | integer |  |  |
| `line_items[].tax_rates` | array of string |  |  |
| `locale` | enum: `auto`, `bg`, `cs`, `da`, `de`, `el`, `en`, `en-GB`, `es`, `es-419`, `et`, `fi`, `fil`, `fr`, `fr-CA`, `hr`, `hu`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `ms`, `mt`, `nb`, `nl`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `tr`, `vi`, `zh`, `zh-HK`, `zh-TW` |  | The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `mode` | enum: `payment`, `setup`, `subscription` |  | The mode of the Checkout Session. Pass `subscription` if the Checkout Session includes at least one recurring item. |
| `payment_intent_data` | object |  | A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode. |
| `payment_intent_data.application_fee_amount` | integer |  |  |
| `payment_intent_data.capture_method` | enum: `automatic`, `automatic_async`, `manual` |  |  |
| `payment_intent_data.description` | string |  |  |
| `payment_intent_data.metadata` | map (key → value) |  |  |
| `payment_intent_data.on_behalf_of` | string |  |  |
| `payment_intent_data.receipt_email` | string |  |  |
| `payment_intent_data.setup_future_usage` | enum: `off_session`, `on_session` |  |  |
| `payment_intent_data.shipping` | object |  |  |
| `payment_intent_data.shipping.address` | object | yes |  |
| `payment_intent_data.shipping.address.city` | string |  |  |
| `payment_intent_data.shipping.address.country` | string |  |  |
| `payment_intent_data.shipping.address.line1` | string | yes |  |
| `payment_intent_data.shipping.address.line2` | string |  |  |
| `payment_intent_data.shipping.address.postal_code` | string |  |  |
| `payment_intent_data.shipping.address.state` | string |  |  |
| `payment_intent_data.shipping.carrier` | string |  |  |
| `payment_intent_data.shipping.name` | string | yes |  |
| `payment_intent_data.shipping.phone` | string |  |  |
| `payment_intent_data.shipping.tracking_number` | string |  |  |
| `payment_intent_data.statement_descriptor` | string |  |  |
| `payment_intent_data.statement_descriptor_suffix` | string |  |  |
| `payment_intent_data.transfer_data` | object |  |  |
| `payment_intent_data.transfer_data.amount` | integer |  |  |
| `payment_intent_data.transfer_data.destination` | string | yes |  |
| `payment_intent_data.transfer_group` | string |  |  |
| `payment_method_collection` | enum: `always`, `if_required` |  | Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0. This may occur if the Checkout Session includes a free trial or a discount.<br>Can only be set in `subscription` mode. Defaults to `always`.<br>If you'd like information on how to collect a payment method outside of Checkout, read the guide on configuring [subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials). |
| `payment_method_configuration` | string |  | The ID of the payment method configuration to use with this Checkout session. |
| `payment_method_options` | object |  | Payment-method-specific configuration. |
| `payment_method_options.acss_debit` | object |  |  |
| `payment_method_options.acss_debit.currency` | enum: `cad`, `usd` |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.default_for` | array of enum: `invoice`, `subscription` |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.affirm` | object |  |  |
| `payment_method_options.affirm.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.afterpay_clearpay` | object |  |  |
| `payment_method_options.afterpay_clearpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.alipay` | object |  |  |
| `payment_method_options.alipay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.au_becs_debit` | object |  |  |
| `payment_method_options.au_becs_debit.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.bacs_debit` | object |  |  |
| `payment_method_options.bacs_debit.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bancontact` | object |  |  |
| `payment_method_options.bancontact.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.boleto` | object |  |  |
| `payment_method_options.boleto.expires_after_days` | integer |  |  |
| `payment_method_options.boleto.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card` | object |  |  |
| `payment_method_options.card.installments` | object |  |  |
| `payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.setup_future_usage` | enum: `off_session`, `on_session` |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kana` | string |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kanji` | string |  |  |
| `payment_method_options.cashapp` | object |  |  |
| `payment_method_options.cashapp.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.customer_balance` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_method_options.customer_balance.bank_transfer.requested_address_types` | array of enum: `aba`, `iban`, `sepa`, `sort_code`, `spei`, `swift`, `zengin` |  |  |
| `payment_method_options.customer_balance.bank_transfer.type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes |  |
| `payment_method_options.customer_balance.funding_type` | enum: `bank_transfer` |  |  |
| `payment_method_options.customer_balance.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.eps` | object |  |  |
| `payment_method_options.eps.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.fpx` | object |  |  |
| `payment_method_options.fpx.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.giropay` | object |  |  |
| `payment_method_options.giropay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.grabpay` | object |  |  |
| `payment_method_options.grabpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.ideal` | object |  |  |
| `payment_method_options.ideal.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.klarna` | object |  |  |
| `payment_method_options.klarna.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.konbini` | object |  |  |
| `payment_method_options.konbini.expires_after_days` | integer |  |  |
| `payment_method_options.konbini.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.link` | object |  |  |
| `payment_method_options.link.setup_future_usage` | enum: `none`, `off_session` |  |  |
| `payment_method_options.oxxo` | object |  |  |
| `payment_method_options.oxxo.expires_after_days` | integer |  |  |
| `payment_method_options.oxxo.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24` | object |  |  |
| `payment_method_options.p24.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24.tos_shown_and_accepted` | boolean |  |  |
| `payment_method_options.paynow` | object |  |  |
| `payment_method_options.paynow.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.paypal` | object |  |  |
| `payment_method_options.paypal.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.paypal.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-DE`, `de-LU`, `el-GR`, `en-GB`, `en-US`, `es-ES`, `fi-FI`, `fr-BE`, `fr-FR`, `fr-LU`, `hu-HU`, `it-IT`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sk-SK`, `sv-SE` |  |  |
| `payment_method_options.paypal.reference` | string |  |  |
| `payment_method_options.paypal.risk_correlation_id` | string |  |  |
| `payment_method_options.paypal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.pix` | object |  |  |
| `payment_method_options.pix.expires_after_seconds` | integer |  |  |
| `payment_method_options.revolut_pay` | object |  |  |
| `payment_method_options.revolut_pay.setup_future_usage` | enum: `none`, `off_session` |  |  |
| `payment_method_options.sepa_debit` | object |  |  |
| `payment_method_options.sepa_debit.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.sofort` | object |  |  |
| `payment_method_options.sofort.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.swish` | object |  |  |
| `payment_method_options.swish.reference` | string |  |  |
| `payment_method_options.us_bank_account` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.setup_future_usage` | enum: `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant` |  |  |
| `payment_method_options.wechat_pay` | object |  |  |
| `payment_method_options.wechat_pay.app_id` | string |  |  |
| `payment_method_options.wechat_pay.client` | enum: `android`, `ios`, `web` | yes |  |
| `payment_method_options.wechat_pay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_types` | array of enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` |  | A list of the types of payment methods (e.g., `card`) this Checkout Session can accept.<br>You can omit this attribute to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). See [Dynamic Payment Methods](https://stripe.com/docs/payments/payment-methods/integration-options#using-dynamic-payment-methods) for more details.<br>Read more about the supported payment methods and their requirements in our [payment method details guide](https://stripe.com/docs/payments/checkout/payment-methods).<br>If multiple payment methods are passed, Checkout will dynamically reorder them to prioritize the most relevant payment methods based on the customer's location and other characteristics. |
| `phone_number_collection` | object |  | Controls phone number collection settings for the session.<br>We recommend that you review your privacy policy and check with your legal contacts before using this feature. Learn more about [collecting phone numbers with Checkout](https://stripe.com/docs/payments/checkout/phone-numbers). |
| `phone_number_collection.enabled` | boolean | yes |  |
| `redirect_on_completion` | enum: `always`, `if_required`, `never` |  | This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-redirect-behavior) of embedded sessions. Defaults to `always`. |
| `return_url` | string |  | The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. This parameter is required if ui_mode is `embedded` and redirect-based payment methods are enabled on the session. |
| `setup_intent_data` | object |  | A subset of parameters to be passed to SetupIntent creation for Checkout Sessions in `setup` mode. |
| `setup_intent_data.description` | string |  |  |
| `setup_intent_data.metadata` | map (key → value) |  |  |
| `setup_intent_data.on_behalf_of` | string |  |  |
| `shipping_address_collection` | object |  | When set, provides configuration for Checkout to collect a shipping address from a customer. |
| `shipping_address_collection.allowed_countries` | array of enum: `AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AO`, `AQ`, `AR`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CR`, `CV`, `CW`, `CY`, `CZ`, `DE`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `FI`, `FJ`, `FK`, `FO`, `FR`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HN`, `HR`, `HT`, `HU`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MK`, `ML`, `MM`, `MN`, `MO`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SE`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SV`, `SX`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TH`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `ZA`, `ZM`, `ZW`, `ZZ` | yes |  |
| `shipping_options` | array of object |  | The shipping rate options to apply to this Session. Up to a maximum of 5. |
| `shipping_options[].shipping_rate` | string |  |  |
| `shipping_options[].shipping_rate_data` | object |  |  |
| `shipping_options[].shipping_rate_data.delivery_estimate` | object |  |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.maximum` | object |  |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.maximum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.maximum.value` | integer | yes |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.minimum` | object |  |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.minimum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `shipping_options[].shipping_rate_data.delivery_estimate.minimum.value` | integer | yes |  |
| `shipping_options[].shipping_rate_data.display_name` | string | yes |  |
| `shipping_options[].shipping_rate_data.fixed_amount` | object |  |  |
| `shipping_options[].shipping_rate_data.fixed_amount.amount` | integer | yes |  |
| `shipping_options[].shipping_rate_data.fixed_amount.currency` | string | yes |  |
| `shipping_options[].shipping_rate_data.fixed_amount.currency_options` | map (key → value) |  |  |
| `shipping_options[].shipping_rate_data.metadata` | map (key → value) |  |  |
| `shipping_options[].shipping_rate_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `shipping_options[].shipping_rate_data.tax_code` | string |  |  |
| `shipping_options[].shipping_rate_data.type` | enum: `fixed_amount` |  |  |
| `submit_type` | enum: `auto`, `book`, `donate`, `pay` |  | Describes the type of transaction being performed by Checkout in order to customize relevant text on the page, such as the submit button. `submit_type` can only be specified on Checkout Sessions in `payment` mode. If blank or `auto`, `pay` is used. |
| `subscription_data` | object |  | A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode. |
| `subscription_data.application_fee_percent` | number |  |  |
| `subscription_data.billing_cycle_anchor` | timestamp (Unix seconds) |  |  |
| `subscription_data.default_tax_rates` | array of string |  |  |
| `subscription_data.description` | string |  |  |
| `subscription_data.invoice_settings` | object |  |  |
| `subscription_data.invoice_settings.issuer` | object |  |  |
| `subscription_data.invoice_settings.issuer.account` | string |  |  |
| `subscription_data.invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `subscription_data.metadata` | map (key → value) |  |  |
| `subscription_data.on_behalf_of` | string |  |  |
| `subscription_data.proration_behavior` | enum: `create_prorations`, `none` |  |  |
| `subscription_data.transfer_data` | object |  |  |
| `subscription_data.transfer_data.amount_percent` | number |  |  |
| `subscription_data.transfer_data.destination` | string | yes |  |
| `subscription_data.trial_end` | timestamp (Unix seconds) |  |  |
| `subscription_data.trial_period_days` | integer |  |  |
| `subscription_data.trial_settings` | object |  |  |
| `subscription_data.trial_settings.end_behavior` | object | yes |  |
| `subscription_data.trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |
| `success_url` | string |  | The URL to which Stripe should send customers when payment or setup is complete. This parameter is not allowed if ui_mode is `embedded`. If you’d like to use information from the successful Checkout Session on your page, read the guide on [customizing your success page](https://stripe.com/docs/payments/checkout/custom-success-page). |
| `tax_id_collection` | object |  | Controls tax ID collection settings for the session. |
| `tax_id_collection.enabled` | boolean | yes |  |
| `ui_mode` | enum: `embedded`, `hosted` |  | The UI mode of the Session. Defaults to `hosted`. |

Returns: `checkout.session`

## GET /v1/checkout/sessions/{session}

operationId: `GetCheckoutSessionsSession`

Retrieves a Session object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `session (path)` | string | yes |  |

Returns: `checkout.session`

## POST /v1/checkout/sessions/{session}/expire

operationId: `PostCheckoutSessionsSessionExpire`

A Session can be expired when it is in one of these statuses: `open` 

After it expires, a customer can’t complete a Session and customers loading the Session see a message saying the Session is expired.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `session (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `checkout.session`

## GET /v1/checkout/sessions/{session}/line_items

operationId: `GetCheckoutSessionsSessionLineItems`

When retrieving a Checkout Session, there is an includable **line_items** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `session (path)` | string | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

# Objects returned

## The `checkout.session` object

A Checkout Session represents your customer's session as they pay for
one-time purchases or subscriptions through [Checkout](https://stripe.com/docs/payments/checkout)
or [Payment Links](https://stripe.com/docs/payments/payment-links). We recommend creating a
new Session each time your customer attempts to pay.

Once payment is successful, the Checkout Session will contain a reference
to the [Customer](https://stripe.com/docs/api/customers), and either the successful
[PaymentIntent](https://stripe.com/docs/api/payment_intents) or an active
[Subscription](https://stripe.com/docs/api/subscriptions).

You can create a Checkout Session on your server and redirect to its URL
to begin Checkout.

Related guide: [Checkout quickstart](https://stripe.com/docs/checkout/quickstart)

Expandable fields (pass `expand[]=<field>`): `after_expiration`, `automatic_tax`, `consent`, `consent_collection`, `currency_conversion`, `custom_fields`, `custom_text`, `customer`, `customer_details`, `invoice`, `invoice_creation`, `line_items`, `payment_intent`, `payment_link`, `payment_method_configuration_details`, `payment_method_options`, `phone_number_collection`, `setup_intent`, `shipping_address_collection`, `shipping_cost`, `shipping_details`, `shipping_options`, `subscription`, `tax_id_collection`, `total_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `after_expiration` | `payment_pages_checkout_session_after_expiration` |  | When set, provides configuration for actions to take if this Checkout Session expires. |
| `allow_promotion_codes` | boolean |  | Enables user redeemable promotion codes. |
| `amount_subtotal` | integer |  | Total of all items before discounts or taxes are applied. |
| `amount_total` | integer |  | Total of all items after discounts and taxes are applied. |
| `automatic_tax` | `payment_pages_checkout_session_automatic_tax` | yes |  |
| `billing_address_collection` | enum: `auto`, `required` |  | Describes whether Checkout should collect the customer's billing address. Defaults to `auto`. |
| `cancel_url` | string |  | If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. |
| `client_reference_id` | string |  | A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the Session with your internal systems. |
| `client_secret` | string |  | Client secret to be used when initializing Stripe.js embedded checkout. |
| `consent` | `payment_pages_checkout_session_consent` |  | Results of `consent_collection` for this session. |
| `consent_collection` | `payment_pages_checkout_session_consent_collection` |  | When set, provides configuration for the Checkout Session to gather active consent from customers. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `currency_conversion` | `payment_pages_checkout_session_currency_conversion` |  | Currency conversion details for automatic currency conversion sessions |
| `custom_fields` | array of `payment_pages_checkout_session_custom_fields` | yes | Collect additional information from your customer using custom fields. Up to 3 fields are supported. |
| `custom_text` | `payment_pages_checkout_session_custom_text` | yes |  |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer for this Session. For Checkout Sessions in `subscription` mode or Checkout Sessions with `customer_creation` set as `always` in `payment` mode, Checkout will create a new customer object based on information provided during the payment flow unless an existing customer was provided when the Session was created. |
| `customer_creation` | enum: `always`, `if_required` |  | Configure whether a Checkout Session creates a Customer when the Checkout Session completes. |
| `customer_details` | `payment_pages_checkout_session_customer_details` |  | The customer details including the customer's tax exempt status and the customer's tax IDs. Customer's address details are not present on Sessions in `setup` mode. |
| `customer_email` | string |  | If provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once the payment flow is complete, use the `customer` attribute. |
| `expires_at` | timestamp (Unix seconds) | yes | The timestamp at which the Checkout Session will expire. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` |  | ID of the invoice created by the Checkout Session, if it exists. |
| `invoice_creation` | `payment_pages_checkout_session_invoice_creation` |  | Details on the state of invoice creation for the Checkout Session. |
| `line_items` | object |  | The line items purchased by the customer. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `locale` | enum: `auto`, `bg`, `cs`, `da`, `de`, `el`, `en`, `en-GB`, `es`, `es-419`, `et`, `fi`, `fil`, `fr`, `fr-CA`, `hr`, `hu`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `ms`, `mt`, `nb`, `nl`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `tr`, `vi`, `zh`, `zh-HK`, `zh-TW` |  | The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `mode` | enum: `payment`, `setup`, `subscription` | yes | The mode of the Checkout Session. |
| `object` | enum: `checkout.session` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string or `payment_intent` |  | The ID of the PaymentIntent for Checkout Sessions in `payment` mode. |
| `payment_link` | string or `payment_link` |  | The ID of the Payment Link that created this Session. |
| `payment_method_collection` | enum: `always`, `if_required` |  | Configure whether a Checkout Session should collect a payment method. Defaults to `always`. |
| `payment_method_configuration_details` | `payment_method_config_biz_payment_method_configuration_details` |  | Information about the payment method configuration used for this Checkout session if using dynamic payment methods. |
| `payment_method_options` | `checkout_session_payment_method_options` |  | Payment-method-specific configuration for the PaymentIntent or SetupIntent of this CheckoutSession. |
| `payment_method_types` | array of string | yes | A list of the types of payment methods (e.g. card) this Checkout Session is allowed to accept. |
| `payment_status` | enum: `no_payment_required`, `paid`, `unpaid` | yes | The payment status of the Checkout Session, one of `paid`, `unpaid`, or `no_payment_required`. You can use this value to decide when to fulfill your customer's order. |
| `phone_number_collection` | `payment_pages_checkout_session_phone_number_collection` |  |  |
| `recovered_from` | string |  | The ID of the original expired Checkout Session that triggered the recovery flow. |
| `redirect_on_completion` | enum: `always`, `if_required`, `never` |  | This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-redirect-behavior) of embedded sessions. Defaults to `always`. |
| `return_url` | string |  | Applies to Checkout Sessions with `ui_mode: embedded`. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. |
| `setup_intent` | string or `setup_intent` |  | The ID of the SetupIntent for Checkout Sessions in `setup` mode. |
| `shipping_address_collection` | `payment_pages_checkout_session_shipping_address_collection` |  | When set, provides configuration for Checkout to collect a shipping address from a customer. |
| `shipping_cost` | `payment_pages_checkout_session_shipping_cost` |  | The details of the customer cost of shipping, including the customer chosen ShippingRate. |
| `shipping_details` | `shipping` |  | Shipping information for this Checkout Session. |
| `shipping_options` | array of `payment_pages_checkout_session_shipping_option` | yes | The shipping rate options applied to this Session. |
| `status` | enum: `complete`, `expired`, `open` |  | The status of the Checkout Session, one of `open`, `complete`, or `expired`. |
| `submit_type` | enum: `auto`, `book`, `donate`, `pay` |  | Describes the type of transaction being performed by Checkout in order to customize relevant text on the page, such as the submit button. `submit_type` can only be specified on Checkout Sessions in `payment` mode. If blank or `auto`, `pay` is used. |
| `subscription` | string or `subscription` |  | The ID of the subscription for Checkout Sessions in `subscription` mode. |
| `success_url` | string |  | The URL the customer will be directed to after the payment or subscription creation is successful. |
| `tax_id_collection` | `payment_pages_checkout_session_tax_id_collection` |  |  |
| `total_details` | `payment_pages_checkout_session_total_details` |  | Tax and discount details for the computed total amount. |
| `ui_mode` | enum: `embedded`, `hosted` |  | The UI mode of the Session. Defaults to `hosted`. |
| `url` | string |  | The URL to the Checkout Session. Redirect customers to this URL to take them to Checkout. If you’re using [Custom Domains](https://stripe.com/docs/payments/checkout/custom-domains), the URL will use your subdomain. Otherwise, it’ll use `checkout.stripe.com.` This value is only present when the session is active. |

