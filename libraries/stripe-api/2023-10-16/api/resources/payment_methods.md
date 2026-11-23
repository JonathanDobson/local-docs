# Stripe API 2023-10-16 — payment methods

Operations under `/v1/payment_methods` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payment_methods

operationId: `GetPaymentMethods`

Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the [List a Customer’s PaymentMethods](https://stripe.com/docs/api/payment_methods/customer_list) API instead.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer` | string |  | The ID of the customer whose PaymentMethods will be retrieved. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` |  | An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request. |

Returns: object

## POST /v1/payment_methods

operationId: `PostPaymentMethods`

Creates a PaymentMethod object. Read the [Stripe.js reference](https://stripe.com/docs/stripe-js/reference#stripe-create-payment-method) to learn how to create PaymentMethods via Stripe.js.

Instead of creating a PaymentMethod directly, we recommend using the [PaymentIntents](https://stripe.com/docs/payments/accept-a-payment) API to accept a payment immediately or the [SetupIntent](https://stripe.com/docs/payments/save-and-reuse) API to collect payment method details ahead of a future payment.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | object |  | If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method. |
| `acss_debit.account_number` | string | yes |  |
| `acss_debit.institution_number` | string | yes |  |
| `acss_debit.transit_number` | string | yes |  |
| `affirm` | object |  | If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method. |
| `afterpay_clearpay` | object |  | If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method. |
| `alipay` | object |  | If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method. |
| `au_becs_debit` | object |  | If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account. |
| `au_becs_debit.account_number` | string | yes |  |
| `au_becs_debit.bsb_number` | string | yes |  |
| `bacs_debit` | object |  | If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account. |
| `bacs_debit.account_number` | string |  |  |
| `bacs_debit.sort_code` | string |  |  |
| `bancontact` | object |  | If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method. |
| `billing_details` | object |  | Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods. |
| `billing_details.address` | object or "" (to unset) |  |  |
| `billing_details.address.city` | string |  |  |
| `billing_details.address.country` | string |  |  |
| `billing_details.address.line1` | string |  |  |
| `billing_details.address.line2` | string |  |  |
| `billing_details.address.postal_code` | string |  |  |
| `billing_details.address.state` | string |  |  |
| `billing_details.email` | string or "" (to unset) |  |  |
| `billing_details.name` | string or "" (to unset) |  |  |
| `billing_details.phone` | string or "" (to unset) |  |  |
| `blik` | object |  | If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method. |
| `boleto` | object |  | If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method. |
| `boleto.tax_id` | string | yes |  |
| `card` | object |  | If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly. |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.networks` | object |  |  |
| `card.networks.preferred` | enum: `cartes_bancaires`, `mastercard`, `visa` |  |  |
| `card.number` | string | yes |  |
| `card.token` | string | yes |  |
| `cashapp` | object |  | If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method. |
| `customer` | string |  | The `Customer` to whom the original PaymentMethod is attached. |
| `customer_balance` | object |  | If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method. |
| `eps` | object |  | If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method. |
| `eps.bank` | enum: `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, `vr_bank_braunau` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fpx` | object |  | If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method. |
| `fpx.bank` | enum: `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_of_china`, `bank_rakyat`, `bsn`, `cimb`, `deutsche_bank`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2e`, `maybank2u`, `ocbc`, `pb_enterprise`, `public_bank`, `rhb`, `standard_chartered`, `uob` | yes |  |
| `giropay` | object |  | If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method. |
| `grabpay` | object |  | If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method. |
| `ideal` | object |  | If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method. |
| `ideal.bank` | enum: `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, `yoursafe` |  |  |
| `interac_present` | object |  | If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method. |
| `klarna` | object |  | If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method. |
| `klarna.dob` | object |  |  |
| `klarna.dob.day` | integer | yes |  |
| `klarna.dob.month` | integer | yes |  |
| `klarna.dob.year` | integer | yes |  |
| `konbini` | object |  | If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method. |
| `link` | object |  | If this is an `Link` PaymentMethod, this hash contains details about the Link payment method. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `mobilepay` | object |  | If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method. |
| `oxxo` | object |  | If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method. |
| `p24` | object |  | If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method. |
| `p24.bank` | enum: `alior_bank`, `bank_millennium`, `bank_nowy_bfg_sa`, `bank_pekao_sa`, `banki_spbdzielcze`, `blik`, `bnp_paribas`, `boz`, `citi_handlowy`, `credit_agricole`, `envelobank`, `etransfer_pocztowy24`, `getin_bank`, `ideabank`, `ing`, `inteligo`, `mbank_mtransfer`, `nest_przelew`, `noble_pay`, `pbac_z_ipko`, `plus_bank`, `santander_przelew24`, `tmobile_usbugi_bankowe`, `toyota_bank`, `velobank`, `volkswagen_bank` |  |  |
| `payment_method` | string |  | The PaymentMethod to share. |
| `paynow` | object |  | If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method. |
| `paypal` | object |  | If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method. |
| `pix` | object |  | If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method. |
| `promptpay` | object |  | If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method. |
| `radar_options` | object |  | Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information. |
| `radar_options.session` | string |  |  |
| `revolut_pay` | object |  | If this is a `Revolut Pay` PaymentMethod, this hash contains details about the Revolut Pay payment method. |
| `sepa_debit` | object |  | If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account. |
| `sepa_debit.iban` | string | yes |  |
| `sofort` | object |  | If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method. |
| `sofort.country` | enum: `AT`, `BE`, `DE`, `ES`, `IT`, `NL` | yes |  |
| `swish` | object |  | If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method. |
| `type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` |  | The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type. |
| `us_bank_account` | object |  | If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method. |
| `us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `us_bank_account.account_number` | string |  |  |
| `us_bank_account.account_type` | enum: `checking`, `savings` |  |  |
| `us_bank_account.financial_connections_account` | string |  |  |
| `us_bank_account.routing_number` | string |  |  |
| `wechat_pay` | object |  | If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method. |
| `zip` | object |  | If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method. |

Returns: `payment_method`

## GET /v1/payment_methods/{payment_method}

operationId: `GetPaymentMethodsPaymentMethod`

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer’s PaymentMethods](https://stripe.com/docs/api/payment_methods/customer)

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_method (path)` | string | yes |  |

Returns: `payment_method`

## POST /v1/payment_methods/{payment_method}

operationId: `PostPaymentMethodsPaymentMethod`

Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method (path)` | string | yes |  |
| `billing_details` | object |  | Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods. |
| `billing_details.address` | object or "" (to unset) |  |  |
| `billing_details.address.city` | string |  |  |
| `billing_details.address.country` | string |  |  |
| `billing_details.address.line1` | string |  |  |
| `billing_details.address.line2` | string |  |  |
| `billing_details.address.postal_code` | string |  |  |
| `billing_details.address.state` | string |  |  |
| `billing_details.email` | string or "" (to unset) |  |  |
| `billing_details.name` | string or "" (to unset) |  |  |
| `billing_details.phone` | string or "" (to unset) |  |  |
| `card` | object |  | If this is a `card` PaymentMethod, this hash contains the user's card details. |
| `card.exp_month` | integer |  |  |
| `card.exp_year` | integer |  |  |
| `card.networks` | object |  |  |
| `card.networks.preferred` | enum: ``, `cartes_bancaires`, `mastercard`, `visa` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `link` | object |  | If this is an `Link` PaymentMethod, this hash contains details about the Link payment method. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `us_bank_account` | object |  | If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method. |
| `us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `us_bank_account.account_type` | enum: `checking`, `savings` |  |  |

Returns: `payment_method`

## POST /v1/payment_methods/{payment_method}/attach

operationId: `PostPaymentMethodsPaymentMethodAttach`

Attaches a PaymentMethod object to a Customer.

To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://stripe.com/docs/api/setup_intents)
or a PaymentIntent with [setup_future_usage](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the `/v1/payment_methods/:id/attach`
endpoint without first using a SetupIntent or PaymentIntent with `setup_future_usage` does not optimize the PaymentMethod for
future use, which makes later declines and payment friction more likely.
See [Optimizing cards for future payments](https://stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
future payments.

To use this PaymentMethod as the default for invoice or subscription payments,
set [`invoice_settings.default_payment_method`](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
on the Customer to the PaymentMethod’s ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method (path)` | string | yes |  |
| `customer` | string | yes | The ID of the customer to which to attach the PaymentMethod. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method`

## POST /v1/payment_methods/{payment_method}/detach

operationId: `PostPaymentMethodsPaymentMethodDetach`

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method`

# Objects returned

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

