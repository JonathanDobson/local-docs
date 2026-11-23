# Stripe API 2023-10-16 — payment intents

Operations under `/v1/payment_intents` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payment_intents

operationId: `GetPaymentIntents`

Returns a list of PaymentIntents.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return PaymentIntents for the customer that this customer ID specifies. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/payment_intents

operationId: `PostPaymentIntents`

Creates a PaymentIntent object.

After the PaymentIntent is created, attach a payment method and [confirm](https://stripe.com/docs/api/payment_intents/confirm)
to continue the payment. Learn more about [the available payment flows
with the Payment Intents API](https://stripe.com/docs/payments/payment-intents).

When you use `confirm=true` during creation, it’s equivalent to creating
and confirming the PaymentIntent in the same call. You can use any parameters
available in the [confirm API](https://stripe.com/docs/api/payment_intents/confirm) when you supply
`confirm=true`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `automatic_payment_methods` | object |  | When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters. |
| `automatic_payment_methods.allow_redirects` | enum: `always`, `never` |  |  |
| `automatic_payment_methods.enabled` | boolean | yes |  |
| `capture_method` | enum: `automatic`, `automatic_async`, `manual` |  | Controls when the funds will be captured from the customer's account. |
| `confirm` | boolean |  | Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm). |
| `confirmation_method` | enum: `automatic`, `manual` |  | Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment. |
| `confirmation_token` | string |  | ID of the ConfirmationToken used to confirm this PaymentIntent.<br>If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | ID of the Customer this PaymentIntent belongs to, if one exists.<br>Payment methods attached to other Customers cannot be used with this PaymentIntent.<br>If present in combination with [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage), this PaymentIntent's payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `error_on_requires_action` | boolean |  | Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `mandate` | string |  | ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm). |
| `mandate_data` | object or "" (to unset) |  | This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm). |
| `mandate_data.customer_acceptance` | object | yes |  |
| `mandate_data.customer_acceptance.accepted_at` | timestamp (Unix seconds) |  |  |
| `mandate_data.customer_acceptance.offline` | object |  |  |
| `mandate_data.customer_acceptance.online` | object |  |  |
| `mandate_data.customer_acceptance.online.ip_address` | string | yes |  |
| `mandate_data.customer_acceptance.online.user_agent` | string | yes |  |
| `mandate_data.customer_acceptance.type` | enum: `offline`, `online` | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean or enum: `one_off`, `recurring` |  | Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm). |
| `on_behalf_of` | string |  | The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.<br>If you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward. |
| `payment_method_configuration` | string |  | The ID of the payment method configuration to use with this PaymentIntent. |
| `payment_method_data` | object |  | If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method) property on the PaymentIntent. |
| `payment_method_data.acss_debit` | object |  |  |
| `payment_method_data.acss_debit.account_number` | string | yes |  |
| `payment_method_data.acss_debit.institution_number` | string | yes |  |
| `payment_method_data.acss_debit.transit_number` | string | yes |  |
| `payment_method_data.affirm` | object |  |  |
| `payment_method_data.afterpay_clearpay` | object |  |  |
| `payment_method_data.alipay` | object |  |  |
| `payment_method_data.au_becs_debit` | object |  |  |
| `payment_method_data.au_becs_debit.account_number` | string | yes |  |
| `payment_method_data.au_becs_debit.bsb_number` | string | yes |  |
| `payment_method_data.bacs_debit` | object |  |  |
| `payment_method_data.bacs_debit.account_number` | string |  |  |
| `payment_method_data.bacs_debit.sort_code` | string |  |  |
| `payment_method_data.bancontact` | object |  |  |
| `payment_method_data.billing_details` | object |  |  |
| `payment_method_data.billing_details.address` | object or "" (to unset) |  |  |
| `payment_method_data.billing_details.address.city` | string |  |  |
| `payment_method_data.billing_details.address.country` | string |  |  |
| `payment_method_data.billing_details.address.line1` | string |  |  |
| `payment_method_data.billing_details.address.line2` | string |  |  |
| `payment_method_data.billing_details.address.postal_code` | string |  |  |
| `payment_method_data.billing_details.address.state` | string |  |  |
| `payment_method_data.billing_details.email` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.name` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.phone` | string or "" (to unset) |  |  |
| `payment_method_data.blik` | object |  |  |
| `payment_method_data.boleto` | object |  |  |
| `payment_method_data.boleto.tax_id` | string | yes |  |
| `payment_method_data.cashapp` | object |  |  |
| `payment_method_data.customer_balance` | object |  |  |
| `payment_method_data.eps` | object |  |  |
| `payment_method_data.eps.bank` | enum: `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, `vr_bank_braunau` |  |  |
| `payment_method_data.fpx` | object |  |  |
| `payment_method_data.fpx.bank` | enum: `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_of_china`, `bank_rakyat`, `bsn`, `cimb`, `deutsche_bank`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2e`, `maybank2u`, `ocbc`, `pb_enterprise`, `public_bank`, `rhb`, `standard_chartered`, `uob` | yes |  |
| `payment_method_data.giropay` | object |  |  |
| `payment_method_data.grabpay` | object |  |  |
| `payment_method_data.ideal` | object |  |  |
| `payment_method_data.ideal.bank` | enum: `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, `yoursafe` |  |  |
| `payment_method_data.interac_present` | object |  |  |
| `payment_method_data.klarna` | object |  |  |
| `payment_method_data.klarna.dob` | object |  |  |
| `payment_method_data.klarna.dob.day` | integer | yes |  |
| `payment_method_data.klarna.dob.month` | integer | yes |  |
| `payment_method_data.klarna.dob.year` | integer | yes |  |
| `payment_method_data.konbini` | object |  |  |
| `payment_method_data.link` | object |  |  |
| `payment_method_data.metadata` | map (key → value) |  |  |
| `payment_method_data.mobilepay` | object |  |  |
| `payment_method_data.oxxo` | object |  |  |
| `payment_method_data.p24` | object |  |  |
| `payment_method_data.p24.bank` | enum: `alior_bank`, `bank_millennium`, `bank_nowy_bfg_sa`, `bank_pekao_sa`, `banki_spbdzielcze`, `blik`, `bnp_paribas`, `boz`, `citi_handlowy`, `credit_agricole`, `envelobank`, `etransfer_pocztowy24`, `getin_bank`, `ideabank`, `ing`, `inteligo`, `mbank_mtransfer`, `nest_przelew`, `noble_pay`, `pbac_z_ipko`, `plus_bank`, `santander_przelew24`, `tmobile_usbugi_bankowe`, `toyota_bank`, `velobank`, `volkswagen_bank` |  |  |
| `payment_method_data.paynow` | object |  |  |
| `payment_method_data.paypal` | object |  |  |
| `payment_method_data.pix` | object |  |  |
| `payment_method_data.promptpay` | object |  |  |
| `payment_method_data.radar_options` | object |  |  |
| `payment_method_data.radar_options.session` | string |  |  |
| `payment_method_data.revolut_pay` | object |  |  |
| `payment_method_data.sepa_debit` | object |  |  |
| `payment_method_data.sepa_debit.iban` | string | yes |  |
| `payment_method_data.sofort` | object |  |  |
| `payment_method_data.sofort.country` | enum: `AT`, `BE`, `DE`, `ES`, `IT`, `NL` | yes |  |
| `payment_method_data.swish` | object |  |  |
| `payment_method_data.type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` | yes |  |
| `payment_method_data.us_bank_account` | object |  |  |
| `payment_method_data.us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `payment_method_data.us_bank_account.account_number` | string |  |  |
| `payment_method_data.us_bank_account.account_type` | enum: `checking`, `savings` |  |  |
| `payment_method_data.us_bank_account.financial_connections_account` | string |  |  |
| `payment_method_data.us_bank_account.routing_number` | string |  |  |
| `payment_method_data.wechat_pay` | object |  |  |
| `payment_method_data.zip` | object |  |  |
| `payment_method_options` | object |  | Payment method-specific configuration for this PaymentIntent. |
| `payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.affirm` | object or "" (to unset) |  |  |
| `payment_method_options.affirm.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.affirm.preferred_locale` | string |  |  |
| `payment_method_options.affirm.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.afterpay_clearpay` | object or "" (to unset) |  |  |
| `payment_method_options.afterpay_clearpay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.afterpay_clearpay.reference` | string |  |  |
| `payment_method_options.afterpay_clearpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.alipay` | object or "" (to unset) |  |  |
| `payment_method_options.alipay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.au_becs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.au_becs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bacs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.bacs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_method_options.bancontact.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.blik` | object or "" (to unset) |  |  |
| `payment_method_options.blik.code` | string |  |  |
| `payment_method_options.blik.setup_future_usage` | enum: ``, `none` |  |  |
| `payment_method_options.boleto` | object or "" (to unset) |  |  |
| `payment_method_options.boleto.expires_after_days` | integer |  |  |
| `payment_method_options.boleto.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_method_options.card.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.card.cvc_token` | string |  |  |
| `payment_method_options.card.installments` | object |  |  |
| `payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_method_options.card.installments.plan` | object or "" (to unset) |  |  |
| `payment_method_options.card.installments.plan.count` | integer | yes |  |
| `payment_method_options.card.installments.plan.interval` | enum: `month` | yes |  |
| `payment_method_options.card.installments.plan.type` | enum: `fixed_count` | yes |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_extended_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_incremental_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_multicapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_overcapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.require_cvc_recollection` | boolean |  |  |
| `payment_method_options.card.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kana` | string or "" (to unset) |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kanji` | string or "" (to unset) |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string | yes |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.exemption_indicator` | enum: `low_risk`, `none` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string | yes |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` | yes |  |
| `payment_method_options.card_present` | object or "" (to unset) |  |  |
| `payment_method_options.card_present.request_extended_authorization` | boolean |  |  |
| `payment_method_options.card_present.request_incremental_authorization_support` | boolean |  |  |
| `payment_method_options.cashapp` | object or "" (to unset) |  |  |
| `payment_method_options.cashapp.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.cashapp.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_method_options.customer_balance.bank_transfer.requested_address_types` | array of enum: `aba`, `iban`, `sepa`, `sort_code`, `spei`, `swift`, `zengin` |  |  |
| `payment_method_options.customer_balance.bank_transfer.type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes |  |
| `payment_method_options.customer_balance.funding_type` | enum: `bank_transfer` |  |  |
| `payment_method_options.customer_balance.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.eps` | object or "" (to unset) |  |  |
| `payment_method_options.eps.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.fpx` | object or "" (to unset) |  |  |
| `payment_method_options.fpx.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.giropay` | object or "" (to unset) |  |  |
| `payment_method_options.giropay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.grabpay` | object or "" (to unset) |  |  |
| `payment_method_options.grabpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.ideal` | object or "" (to unset) |  |  |
| `payment_method_options.ideal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.interac_present` | object or "" (to unset) |  |  |
| `payment_method_options.klarna` | object or "" (to unset) |  |  |
| `payment_method_options.klarna.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.klarna.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-CH`, `de-DE`, `el-GR`, `en-AT`, `en-AU`, `en-BE`, `en-CA`, `en-CH`, `en-CZ`, `en-DE`, `en-DK`, `en-ES`, `en-FI`, `en-FR`, `en-GB`, `en-GR`, `en-IE`, `en-IT`, `en-NL`, `en-NO`, `en-NZ`, `en-PL`, `en-PT`, `en-SE`, `en-US`, `es-ES`, `es-US`, `fi-FI`, `fr-BE`, `fr-CA`, `fr-CH`, `fr-FR`, `it-CH`, `it-IT`, `nb-NO`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sv-FI`, `sv-SE` |  |  |
| `payment_method_options.klarna.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_method_options.konbini.confirmation_number` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_after_days` | integer or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `payment_method_options.konbini.product_description` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.link` | object or "" (to unset) |  |  |
| `payment_method_options.link.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.link.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.mobilepay` | object or "" (to unset) |  |  |
| `payment_method_options.mobilepay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.mobilepay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.oxxo` | object or "" (to unset) |  |  |
| `payment_method_options.oxxo.expires_after_days` | integer |  |  |
| `payment_method_options.oxxo.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24` | object or "" (to unset) |  |  |
| `payment_method_options.p24.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24.tos_shown_and_accepted` | boolean |  |  |
| `payment_method_options.paynow` | object or "" (to unset) |  |  |
| `payment_method_options.paynow.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.paypal` | object or "" (to unset) |  |  |
| `payment_method_options.paypal.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.paypal.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-DE`, `de-LU`, `el-GR`, `en-GB`, `en-US`, `es-ES`, `fi-FI`, `fr-BE`, `fr-FR`, `fr-LU`, `hu-HU`, `it-IT`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sk-SK`, `sv-SE` |  |  |
| `payment_method_options.paypal.reference` | string |  |  |
| `payment_method_options.paypal.risk_correlation_id` | string |  |  |
| `payment_method_options.paypal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.pix` | object or "" (to unset) |  |  |
| `payment_method_options.pix.expires_after_seconds` | integer |  |  |
| `payment_method_options.pix.expires_at` | timestamp (Unix seconds) |  |  |
| `payment_method_options.pix.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.promptpay` | object or "" (to unset) |  |  |
| `payment_method_options.promptpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.revolut_pay` | object or "" (to unset) |  |  |
| `payment_method_options.revolut_pay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.sepa_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.sofort` | object or "" (to unset) |  |  |
| `payment_method_options.sofort.preferred_language` | enum: ``, `de`, `en`, `es`, `fr`, `it`, `nl`, `pl` |  |  |
| `payment_method_options.sofort.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.swish` | object or "" (to unset) |  |  |
| `payment_method_options.swish.reference` | string or "" (to unset) |  |  |
| `payment_method_options.swish.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.preferred_settlement_speed` | enum: ``, `fastest`, `standard` |  |  |
| `payment_method_options.us_bank_account.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.wechat_pay` | object or "" (to unset) |  |  |
| `payment_method_options.wechat_pay.app_id` | string |  |  |
| `payment_method_options.wechat_pay.client` | enum: `android`, `ios`, `web` | yes |  |
| `payment_method_options.wechat_pay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.zip` | object or "" (to unset) |  |  |
| `payment_method_options.zip.setup_future_usage` | enum: `none` |  |  |
| `payment_method_types` | array of string |  | The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, it defaults to ["card"]. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). |
| `radar_options` | object |  | Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session). |
| `radar_options.session` | string |  |  |
| `receipt_email` | string |  | Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails). |
| `return_url` | string |  | The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm). |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |
| `shipping` | object |  | Shipping information for this PaymentIntent. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.carrier` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `shipping.tracking_number` | string |  |  |
| `statement_descriptor` | string |  | For card charges, use [statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic). Otherwise, you can use this value as the complete description of a charge on your customers' statements. It must contain at least one letter and be 1–22 characters long. |
| `statement_descriptor_suffix` | string |  | Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. The concatenated descriptor must contain 1-22 characters. |
| `transfer_data` | object |  | The parameters that you can use to automatically create a Transfer. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.destination` | string | yes |  |
| `transfer_group` | string |  | A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers). |
| `use_stripe_sdk` | boolean |  | Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions. |

Returns: `payment_intent`

## GET /v1/payment_intents/search

operationId: `GetPaymentIntentsSearch`

Search for PaymentIntents you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents). |

Returns: object

## GET /v1/payment_intents/{intent}

operationId: `GetPaymentIntentsIntent`

Retrieves the details of a PaymentIntent that has previously been created. 

You can retrieve a PaymentIntent client-side using a publishable key when the `client_secret` is in the query string. 

If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the [payment intent](#payment_intent_object) object reference for more details.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_secret` | string |  | The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `intent (path)` | string | yes |  |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}

operationId: `PostPaymentIntentsIntent`

Updates properties on a PaymentIntent object without confirming.

Depending on which properties you update, you might need to confirm the
PaymentIntent again. For example, updating the `payment_method`
always requires you to confirm the PaymentIntent again. If you prefer to
update and confirm at the same time, we recommend updating properties through
the [confirm API](https://stripe.com/docs/api/payment_intents/confirm) instead.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amount` | integer |  | Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `application_fee_amount` | integer or "" (to unset) |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `capture_method` | enum: `automatic`, `automatic_async`, `manual` |  | Controls when the funds will be captured from the customer's account. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | ID of the Customer this PaymentIntent belongs to, if one exists.<br>Payment methods attached to other Customers cannot be used with this PaymentIntent.<br>If present in combination with [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage), this PaymentIntent's payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent. |
| `payment_method_configuration` | string |  | The ID of the payment method configuration to use with this PaymentIntent. |
| `payment_method_data` | object |  | If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method) property on the PaymentIntent. |
| `payment_method_data.acss_debit` | object |  |  |
| `payment_method_data.acss_debit.account_number` | string | yes |  |
| `payment_method_data.acss_debit.institution_number` | string | yes |  |
| `payment_method_data.acss_debit.transit_number` | string | yes |  |
| `payment_method_data.affirm` | object |  |  |
| `payment_method_data.afterpay_clearpay` | object |  |  |
| `payment_method_data.alipay` | object |  |  |
| `payment_method_data.au_becs_debit` | object |  |  |
| `payment_method_data.au_becs_debit.account_number` | string | yes |  |
| `payment_method_data.au_becs_debit.bsb_number` | string | yes |  |
| `payment_method_data.bacs_debit` | object |  |  |
| `payment_method_data.bacs_debit.account_number` | string |  |  |
| `payment_method_data.bacs_debit.sort_code` | string |  |  |
| `payment_method_data.bancontact` | object |  |  |
| `payment_method_data.billing_details` | object |  |  |
| `payment_method_data.billing_details.address` | object or "" (to unset) |  |  |
| `payment_method_data.billing_details.address.city` | string |  |  |
| `payment_method_data.billing_details.address.country` | string |  |  |
| `payment_method_data.billing_details.address.line1` | string |  |  |
| `payment_method_data.billing_details.address.line2` | string |  |  |
| `payment_method_data.billing_details.address.postal_code` | string |  |  |
| `payment_method_data.billing_details.address.state` | string |  |  |
| `payment_method_data.billing_details.email` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.name` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.phone` | string or "" (to unset) |  |  |
| `payment_method_data.blik` | object |  |  |
| `payment_method_data.boleto` | object |  |  |
| `payment_method_data.boleto.tax_id` | string | yes |  |
| `payment_method_data.cashapp` | object |  |  |
| `payment_method_data.customer_balance` | object |  |  |
| `payment_method_data.eps` | object |  |  |
| `payment_method_data.eps.bank` | enum: `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, `vr_bank_braunau` |  |  |
| `payment_method_data.fpx` | object |  |  |
| `payment_method_data.fpx.bank` | enum: `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_of_china`, `bank_rakyat`, `bsn`, `cimb`, `deutsche_bank`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2e`, `maybank2u`, `ocbc`, `pb_enterprise`, `public_bank`, `rhb`, `standard_chartered`, `uob` | yes |  |
| `payment_method_data.giropay` | object |  |  |
| `payment_method_data.grabpay` | object |  |  |
| `payment_method_data.ideal` | object |  |  |
| `payment_method_data.ideal.bank` | enum: `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, `yoursafe` |  |  |
| `payment_method_data.interac_present` | object |  |  |
| `payment_method_data.klarna` | object |  |  |
| `payment_method_data.klarna.dob` | object |  |  |
| `payment_method_data.klarna.dob.day` | integer | yes |  |
| `payment_method_data.klarna.dob.month` | integer | yes |  |
| `payment_method_data.klarna.dob.year` | integer | yes |  |
| `payment_method_data.konbini` | object |  |  |
| `payment_method_data.link` | object |  |  |
| `payment_method_data.metadata` | map (key → value) |  |  |
| `payment_method_data.mobilepay` | object |  |  |
| `payment_method_data.oxxo` | object |  |  |
| `payment_method_data.p24` | object |  |  |
| `payment_method_data.p24.bank` | enum: `alior_bank`, `bank_millennium`, `bank_nowy_bfg_sa`, `bank_pekao_sa`, `banki_spbdzielcze`, `blik`, `bnp_paribas`, `boz`, `citi_handlowy`, `credit_agricole`, `envelobank`, `etransfer_pocztowy24`, `getin_bank`, `ideabank`, `ing`, `inteligo`, `mbank_mtransfer`, `nest_przelew`, `noble_pay`, `pbac_z_ipko`, `plus_bank`, `santander_przelew24`, `tmobile_usbugi_bankowe`, `toyota_bank`, `velobank`, `volkswagen_bank` |  |  |
| `payment_method_data.paynow` | object |  |  |
| `payment_method_data.paypal` | object |  |  |
| `payment_method_data.pix` | object |  |  |
| `payment_method_data.promptpay` | object |  |  |
| `payment_method_data.radar_options` | object |  |  |
| `payment_method_data.radar_options.session` | string |  |  |
| `payment_method_data.revolut_pay` | object |  |  |
| `payment_method_data.sepa_debit` | object |  |  |
| `payment_method_data.sepa_debit.iban` | string | yes |  |
| `payment_method_data.sofort` | object |  |  |
| `payment_method_data.sofort.country` | enum: `AT`, `BE`, `DE`, `ES`, `IT`, `NL` | yes |  |
| `payment_method_data.swish` | object |  |  |
| `payment_method_data.type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` | yes |  |
| `payment_method_data.us_bank_account` | object |  |  |
| `payment_method_data.us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `payment_method_data.us_bank_account.account_number` | string |  |  |
| `payment_method_data.us_bank_account.account_type` | enum: `checking`, `savings` |  |  |
| `payment_method_data.us_bank_account.financial_connections_account` | string |  |  |
| `payment_method_data.us_bank_account.routing_number` | string |  |  |
| `payment_method_data.wechat_pay` | object |  |  |
| `payment_method_data.zip` | object |  |  |
| `payment_method_options` | object |  | Payment-method-specific configuration for this PaymentIntent. |
| `payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.affirm` | object or "" (to unset) |  |  |
| `payment_method_options.affirm.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.affirm.preferred_locale` | string |  |  |
| `payment_method_options.affirm.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.afterpay_clearpay` | object or "" (to unset) |  |  |
| `payment_method_options.afterpay_clearpay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.afterpay_clearpay.reference` | string |  |  |
| `payment_method_options.afterpay_clearpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.alipay` | object or "" (to unset) |  |  |
| `payment_method_options.alipay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.au_becs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.au_becs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bacs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.bacs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_method_options.bancontact.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.blik` | object or "" (to unset) |  |  |
| `payment_method_options.blik.code` | string |  |  |
| `payment_method_options.blik.setup_future_usage` | enum: ``, `none` |  |  |
| `payment_method_options.boleto` | object or "" (to unset) |  |  |
| `payment_method_options.boleto.expires_after_days` | integer |  |  |
| `payment_method_options.boleto.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_method_options.card.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.card.cvc_token` | string |  |  |
| `payment_method_options.card.installments` | object |  |  |
| `payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_method_options.card.installments.plan` | object or "" (to unset) |  |  |
| `payment_method_options.card.installments.plan.count` | integer | yes |  |
| `payment_method_options.card.installments.plan.interval` | enum: `month` | yes |  |
| `payment_method_options.card.installments.plan.type` | enum: `fixed_count` | yes |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_extended_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_incremental_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_multicapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_overcapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.require_cvc_recollection` | boolean |  |  |
| `payment_method_options.card.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kana` | string or "" (to unset) |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kanji` | string or "" (to unset) |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string | yes |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.exemption_indicator` | enum: `low_risk`, `none` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string | yes |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` | yes |  |
| `payment_method_options.card_present` | object or "" (to unset) |  |  |
| `payment_method_options.card_present.request_extended_authorization` | boolean |  |  |
| `payment_method_options.card_present.request_incremental_authorization_support` | boolean |  |  |
| `payment_method_options.cashapp` | object or "" (to unset) |  |  |
| `payment_method_options.cashapp.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.cashapp.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_method_options.customer_balance.bank_transfer.requested_address_types` | array of enum: `aba`, `iban`, `sepa`, `sort_code`, `spei`, `swift`, `zengin` |  |  |
| `payment_method_options.customer_balance.bank_transfer.type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes |  |
| `payment_method_options.customer_balance.funding_type` | enum: `bank_transfer` |  |  |
| `payment_method_options.customer_balance.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.eps` | object or "" (to unset) |  |  |
| `payment_method_options.eps.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.fpx` | object or "" (to unset) |  |  |
| `payment_method_options.fpx.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.giropay` | object or "" (to unset) |  |  |
| `payment_method_options.giropay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.grabpay` | object or "" (to unset) |  |  |
| `payment_method_options.grabpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.ideal` | object or "" (to unset) |  |  |
| `payment_method_options.ideal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.interac_present` | object or "" (to unset) |  |  |
| `payment_method_options.klarna` | object or "" (to unset) |  |  |
| `payment_method_options.klarna.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.klarna.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-CH`, `de-DE`, `el-GR`, `en-AT`, `en-AU`, `en-BE`, `en-CA`, `en-CH`, `en-CZ`, `en-DE`, `en-DK`, `en-ES`, `en-FI`, `en-FR`, `en-GB`, `en-GR`, `en-IE`, `en-IT`, `en-NL`, `en-NO`, `en-NZ`, `en-PL`, `en-PT`, `en-SE`, `en-US`, `es-ES`, `es-US`, `fi-FI`, `fr-BE`, `fr-CA`, `fr-CH`, `fr-FR`, `it-CH`, `it-IT`, `nb-NO`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sv-FI`, `sv-SE` |  |  |
| `payment_method_options.klarna.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_method_options.konbini.confirmation_number` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_after_days` | integer or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `payment_method_options.konbini.product_description` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.link` | object or "" (to unset) |  |  |
| `payment_method_options.link.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.link.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.mobilepay` | object or "" (to unset) |  |  |
| `payment_method_options.mobilepay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.mobilepay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.oxxo` | object or "" (to unset) |  |  |
| `payment_method_options.oxxo.expires_after_days` | integer |  |  |
| `payment_method_options.oxxo.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24` | object or "" (to unset) |  |  |
| `payment_method_options.p24.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24.tos_shown_and_accepted` | boolean |  |  |
| `payment_method_options.paynow` | object or "" (to unset) |  |  |
| `payment_method_options.paynow.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.paypal` | object or "" (to unset) |  |  |
| `payment_method_options.paypal.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.paypal.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-DE`, `de-LU`, `el-GR`, `en-GB`, `en-US`, `es-ES`, `fi-FI`, `fr-BE`, `fr-FR`, `fr-LU`, `hu-HU`, `it-IT`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sk-SK`, `sv-SE` |  |  |
| `payment_method_options.paypal.reference` | string |  |  |
| `payment_method_options.paypal.risk_correlation_id` | string |  |  |
| `payment_method_options.paypal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.pix` | object or "" (to unset) |  |  |
| `payment_method_options.pix.expires_after_seconds` | integer |  |  |
| `payment_method_options.pix.expires_at` | timestamp (Unix seconds) |  |  |
| `payment_method_options.pix.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.promptpay` | object or "" (to unset) |  |  |
| `payment_method_options.promptpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.revolut_pay` | object or "" (to unset) |  |  |
| `payment_method_options.revolut_pay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.sepa_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.sofort` | object or "" (to unset) |  |  |
| `payment_method_options.sofort.preferred_language` | enum: ``, `de`, `en`, `es`, `fr`, `it`, `nl`, `pl` |  |  |
| `payment_method_options.sofort.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.swish` | object or "" (to unset) |  |  |
| `payment_method_options.swish.reference` | string or "" (to unset) |  |  |
| `payment_method_options.swish.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.preferred_settlement_speed` | enum: ``, `fastest`, `standard` |  |  |
| `payment_method_options.us_bank_account.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.wechat_pay` | object or "" (to unset) |  |  |
| `payment_method_options.wechat_pay.app_id` | string |  |  |
| `payment_method_options.wechat_pay.client` | enum: `android`, `ios`, `web` | yes |  |
| `payment_method_options.wechat_pay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.zip` | object or "" (to unset) |  |  |
| `payment_method_options.zip.setup_future_usage` | enum: `none` |  |  |
| `payment_method_types` | array of string |  | The list of payment method types (for example, card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). |
| `receipt_email` | string or "" (to unset) |  | Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails). |
| `setup_future_usage` | enum: ``, `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).<br>If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`. |
| `shipping` | object or "" (to unset) |  | Shipping information for this PaymentIntent. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.carrier` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `shipping.tracking_number` | string |  |  |
| `statement_descriptor` | string |  | For card charges, use [statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic). Otherwise, you can use this value as the complete description of a charge on your customers' statements. It must contain at least one letter and be 1–22 characters long. |
| `statement_descriptor_suffix` | string |  | Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `transfer_data` | object |  | Use this parameter to automatically create a Transfer when the payment succeeds. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `transfer_data.amount` | integer |  |  |
| `transfer_group` | string |  | A string that identifies the resulting payment as part of a group. You can only provide `transfer_group` if it hasn't been set. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/apply_customer_balance

operationId: `PostPaymentIntentsIntentApplyCustomerBalance`

Manually reconcile the remaining amount for a `customer_balance` PaymentIntent.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amount` | integer |  | Amount that you intend to apply to this PaymentIntent from the customer’s cash balance.<br>A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency).<br>The maximum amount is the amount of the PaymentIntent.<br>When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/cancel

operationId: `PostPaymentIntentsIntentCancel`

You can cancel a PaymentIntent object when it’s in one of these statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_action` or, [in rare cases](https://stripe.com/docs/payments/intents), `processing`. 

After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a `status` of `requires_capture`, the remaining `amount_capturable` is automatically refunded. 

You can’t cancel the PaymentIntent for a Checkout Session. [Expire the Checkout Session](https://stripe.com/docs/api/checkout/sessions/expire) instead.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `cancellation_reason` | enum: `abandoned`, `duplicate`, `fraudulent`, `requested_by_customer` |  | Reason for canceling this PaymentIntent. Possible values are: `duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned` |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/capture

operationId: `PostPaymentIntentsIntentCapture`

Capture the funds of an existing uncaptured PaymentIntent when its status is `requires_capture`.

Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.

Learn more about [separate authorization and capture](https://stripe.com/docs/payments/capture-later).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amount_to_capture` | integer |  | The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Any additional amount is automatically refunded. Defaults to the full `amount_capturable` if it's not provided. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `final_capture` | boolean |  | Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they're captured in future requests. You can only use this setting when [multicapture](https://stripe.com/docs/payments/multicapture) is available for PaymentIntents. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `statement_descriptor` | string |  | For card charges, use [statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic). Otherwise, you can use this value as the complete description of a charge on your customers' statements. It must contain at least one letter and be 1–22 characters long. |
| `statement_descriptor_suffix` | string |  | Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. The concatenated descriptor must be 1-22 characters long. |
| `transfer_data` | object |  | The parameters that you can use to automatically create a transfer after the payment is captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `transfer_data.amount` | integer |  |  |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/confirm

operationId: `PostPaymentIntentsIntentConfirm`

Confirm that your customer intends to pay with current or provided
payment method. Upon confirmation, the PaymentIntent will attempt to initiate
a payment.
If the selected payment method requires additional authentication steps, the
PaymentIntent will transition to the `requires_action` status and
suggest additional actions via `next_action`. If payment fails,
the PaymentIntent transitions to the `requires_payment_method` status or the
`canceled` status if the confirmation limit is reached. If
payment succeeds, the PaymentIntent will transition to the `succeeded`
status (or `requires_capture`, if `capture_method` is set to `manual`).
If the `confirmation_method` is `automatic`, payment may be attempted
using our [client SDKs](https://stripe.com/docs/stripe-js/reference#stripe-handle-card-payment)
and the PaymentIntent’s [client_secret](#payment_intent_object-client_secret).
After `next_action`s are handled by the client, no additional
confirmation is required to complete the payment.
If the `confirmation_method` is `manual`, all payment attempts must be
initiated using a secret key.
If any actions are required for the payment, the PaymentIntent will
return to the `requires_confirmation` state
after those actions are completed. Your server needs to then
explicitly re-confirm the PaymentIntent to initiate the next payment
attempt.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `capture_method` | enum: `automatic`, `automatic_async`, `manual` |  | Controls when the funds will be captured from the customer's account. |
| `client_secret` | string |  | The client secret of the PaymentIntent. |
| `confirmation_token` | string |  | ID of the ConfirmationToken used to confirm this PaymentIntent.<br>If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence. |
| `error_on_requires_action` | boolean |  | Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `mandate` | string |  | ID of the mandate that's used for this payment. |
| `mandate_data` | object or "" (to unset) |  |  |
| `mandate_data.customer_acceptance` | object | yes |  |
| `mandate_data.customer_acceptance.accepted_at` | timestamp (Unix seconds) |  |  |
| `mandate_data.customer_acceptance.offline` | object |  |  |
| `mandate_data.customer_acceptance.online` | object |  |  |
| `mandate_data.customer_acceptance.online.ip_address` | string | yes |  |
| `mandate_data.customer_acceptance.online.user_agent` | string | yes |  |
| `mandate_data.customer_acceptance.type` | enum: `offline`, `online` | yes |  |
| `mandate_data.customer_acceptance` | object | yes |  |
| `mandate_data.customer_acceptance.online` | object | yes |  |
| `mandate_data.customer_acceptance.online.ip_address` | string |  |  |
| `mandate_data.customer_acceptance.online.user_agent` | string |  |  |
| `mandate_data.customer_acceptance.type` | enum: `online` | yes |  |
| `off_session` | boolean or enum: `one_off`, `recurring` |  | Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). |
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent. |
| `payment_method_data` | object |  | If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method) property on the PaymentIntent. |
| `payment_method_data.acss_debit` | object |  |  |
| `payment_method_data.acss_debit.account_number` | string | yes |  |
| `payment_method_data.acss_debit.institution_number` | string | yes |  |
| `payment_method_data.acss_debit.transit_number` | string | yes |  |
| `payment_method_data.affirm` | object |  |  |
| `payment_method_data.afterpay_clearpay` | object |  |  |
| `payment_method_data.alipay` | object |  |  |
| `payment_method_data.au_becs_debit` | object |  |  |
| `payment_method_data.au_becs_debit.account_number` | string | yes |  |
| `payment_method_data.au_becs_debit.bsb_number` | string | yes |  |
| `payment_method_data.bacs_debit` | object |  |  |
| `payment_method_data.bacs_debit.account_number` | string |  |  |
| `payment_method_data.bacs_debit.sort_code` | string |  |  |
| `payment_method_data.bancontact` | object |  |  |
| `payment_method_data.billing_details` | object |  |  |
| `payment_method_data.billing_details.address` | object or "" (to unset) |  |  |
| `payment_method_data.billing_details.address.city` | string |  |  |
| `payment_method_data.billing_details.address.country` | string |  |  |
| `payment_method_data.billing_details.address.line1` | string |  |  |
| `payment_method_data.billing_details.address.line2` | string |  |  |
| `payment_method_data.billing_details.address.postal_code` | string |  |  |
| `payment_method_data.billing_details.address.state` | string |  |  |
| `payment_method_data.billing_details.email` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.name` | string or "" (to unset) |  |  |
| `payment_method_data.billing_details.phone` | string or "" (to unset) |  |  |
| `payment_method_data.blik` | object |  |  |
| `payment_method_data.boleto` | object |  |  |
| `payment_method_data.boleto.tax_id` | string | yes |  |
| `payment_method_data.cashapp` | object |  |  |
| `payment_method_data.customer_balance` | object |  |  |
| `payment_method_data.eps` | object |  |  |
| `payment_method_data.eps.bank` | enum: `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, `vr_bank_braunau` |  |  |
| `payment_method_data.fpx` | object |  |  |
| `payment_method_data.fpx.bank` | enum: `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_of_china`, `bank_rakyat`, `bsn`, `cimb`, `deutsche_bank`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2e`, `maybank2u`, `ocbc`, `pb_enterprise`, `public_bank`, `rhb`, `standard_chartered`, `uob` | yes |  |
| `payment_method_data.giropay` | object |  |  |
| `payment_method_data.grabpay` | object |  |  |
| `payment_method_data.ideal` | object |  |  |
| `payment_method_data.ideal.bank` | enum: `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, `yoursafe` |  |  |
| `payment_method_data.interac_present` | object |  |  |
| `payment_method_data.klarna` | object |  |  |
| `payment_method_data.klarna.dob` | object |  |  |
| `payment_method_data.klarna.dob.day` | integer | yes |  |
| `payment_method_data.klarna.dob.month` | integer | yes |  |
| `payment_method_data.klarna.dob.year` | integer | yes |  |
| `payment_method_data.konbini` | object |  |  |
| `payment_method_data.link` | object |  |  |
| `payment_method_data.metadata` | map (key → value) |  |  |
| `payment_method_data.mobilepay` | object |  |  |
| `payment_method_data.oxxo` | object |  |  |
| `payment_method_data.p24` | object |  |  |
| `payment_method_data.p24.bank` | enum: `alior_bank`, `bank_millennium`, `bank_nowy_bfg_sa`, `bank_pekao_sa`, `banki_spbdzielcze`, `blik`, `bnp_paribas`, `boz`, `citi_handlowy`, `credit_agricole`, `envelobank`, `etransfer_pocztowy24`, `getin_bank`, `ideabank`, `ing`, `inteligo`, `mbank_mtransfer`, `nest_przelew`, `noble_pay`, `pbac_z_ipko`, `plus_bank`, `santander_przelew24`, `tmobile_usbugi_bankowe`, `toyota_bank`, `velobank`, `volkswagen_bank` |  |  |
| `payment_method_data.paynow` | object |  |  |
| `payment_method_data.paypal` | object |  |  |
| `payment_method_data.pix` | object |  |  |
| `payment_method_data.promptpay` | object |  |  |
| `payment_method_data.radar_options` | object |  |  |
| `payment_method_data.radar_options.session` | string |  |  |
| `payment_method_data.revolut_pay` | object |  |  |
| `payment_method_data.sepa_debit` | object |  |  |
| `payment_method_data.sepa_debit.iban` | string | yes |  |
| `payment_method_data.sofort` | object |  |  |
| `payment_method_data.sofort.country` | enum: `AT`, `BE`, `DE`, `ES`, `IT`, `NL` | yes |  |
| `payment_method_data.swish` | object |  |  |
| `payment_method_data.type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` | yes |  |
| `payment_method_data.us_bank_account` | object |  |  |
| `payment_method_data.us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `payment_method_data.us_bank_account.account_number` | string |  |  |
| `payment_method_data.us_bank_account.account_type` | enum: `checking`, `savings` |  |  |
| `payment_method_data.us_bank_account.financial_connections_account` | string |  |  |
| `payment_method_data.us_bank_account.routing_number` | string |  |  |
| `payment_method_data.wechat_pay` | object |  |  |
| `payment_method_data.zip` | object |  |  |
| `payment_method_options` | object |  | Payment method-specific configuration for this PaymentIntent. |
| `payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.affirm` | object or "" (to unset) |  |  |
| `payment_method_options.affirm.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.affirm.preferred_locale` | string |  |  |
| `payment_method_options.affirm.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.afterpay_clearpay` | object or "" (to unset) |  |  |
| `payment_method_options.afterpay_clearpay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.afterpay_clearpay.reference` | string |  |  |
| `payment_method_options.afterpay_clearpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.alipay` | object or "" (to unset) |  |  |
| `payment_method_options.alipay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.au_becs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.au_becs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bacs_debit` | object or "" (to unset) |  |  |
| `payment_method_options.bacs_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_method_options.bancontact.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.blik` | object or "" (to unset) |  |  |
| `payment_method_options.blik.code` | string |  |  |
| `payment_method_options.blik.setup_future_usage` | enum: ``, `none` |  |  |
| `payment_method_options.boleto` | object or "" (to unset) |  |  |
| `payment_method_options.boleto.expires_after_days` | integer |  |  |
| `payment_method_options.boleto.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_method_options.card.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.card.cvc_token` | string |  |  |
| `payment_method_options.card.installments` | object |  |  |
| `payment_method_options.card.installments.enabled` | boolean |  |  |
| `payment_method_options.card.installments.plan` | object or "" (to unset) |  |  |
| `payment_method_options.card.installments.plan.count` | integer | yes |  |
| `payment_method_options.card.installments.plan.interval` | enum: `month` | yes |  |
| `payment_method_options.card.installments.plan.type` | enum: `fixed_count` | yes |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_extended_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_incremental_authorization` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_multicapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_overcapture` | enum: `if_available`, `never` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.require_cvc_recollection` | boolean |  |  |
| `payment_method_options.card.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kana` | string or "" (to unset) |  |  |
| `payment_method_options.card.statement_descriptor_suffix_kanji` | string or "" (to unset) |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string | yes |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.exemption_indicator` | enum: `low_risk`, `none` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string | yes |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` | yes |  |
| `payment_method_options.card_present` | object or "" (to unset) |  |  |
| `payment_method_options.card_present.request_extended_authorization` | boolean |  |  |
| `payment_method_options.card_present.request_incremental_authorization_support` | boolean |  |  |
| `payment_method_options.cashapp` | object or "" (to unset) |  |  |
| `payment_method_options.cashapp.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.cashapp.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_method_options.customer_balance.bank_transfer.requested_address_types` | array of enum: `aba`, `iban`, `sepa`, `sort_code`, `spei`, `swift`, `zengin` |  |  |
| `payment_method_options.customer_balance.bank_transfer.type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes |  |
| `payment_method_options.customer_balance.funding_type` | enum: `bank_transfer` |  |  |
| `payment_method_options.customer_balance.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.eps` | object or "" (to unset) |  |  |
| `payment_method_options.eps.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.fpx` | object or "" (to unset) |  |  |
| `payment_method_options.fpx.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.giropay` | object or "" (to unset) |  |  |
| `payment_method_options.giropay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.grabpay` | object or "" (to unset) |  |  |
| `payment_method_options.grabpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.ideal` | object or "" (to unset) |  |  |
| `payment_method_options.ideal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.interac_present` | object or "" (to unset) |  |  |
| `payment_method_options.klarna` | object or "" (to unset) |  |  |
| `payment_method_options.klarna.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.klarna.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-CH`, `de-DE`, `el-GR`, `en-AT`, `en-AU`, `en-BE`, `en-CA`, `en-CH`, `en-CZ`, `en-DE`, `en-DK`, `en-ES`, `en-FI`, `en-FR`, `en-GB`, `en-GR`, `en-IE`, `en-IT`, `en-NL`, `en-NO`, `en-NZ`, `en-PL`, `en-PT`, `en-SE`, `en-US`, `es-ES`, `es-US`, `fi-FI`, `fr-BE`, `fr-CA`, `fr-CH`, `fr-FR`, `it-CH`, `it-IT`, `nb-NO`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sv-FI`, `sv-SE` |  |  |
| `payment_method_options.klarna.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_method_options.konbini.confirmation_number` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_after_days` | integer or "" (to unset) |  |  |
| `payment_method_options.konbini.expires_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `payment_method_options.konbini.product_description` | string or "" (to unset) |  |  |
| `payment_method_options.konbini.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.link` | object or "" (to unset) |  |  |
| `payment_method_options.link.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.link.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.mobilepay` | object or "" (to unset) |  |  |
| `payment_method_options.mobilepay.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.mobilepay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.oxxo` | object or "" (to unset) |  |  |
| `payment_method_options.oxxo.expires_after_days` | integer |  |  |
| `payment_method_options.oxxo.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24` | object or "" (to unset) |  |  |
| `payment_method_options.p24.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.p24.tos_shown_and_accepted` | boolean |  |  |
| `payment_method_options.paynow` | object or "" (to unset) |  |  |
| `payment_method_options.paynow.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.paypal` | object or "" (to unset) |  |  |
| `payment_method_options.paypal.capture_method` | enum: ``, `manual` |  |  |
| `payment_method_options.paypal.preferred_locale` | enum: `cs-CZ`, `da-DK`, `de-AT`, `de-DE`, `de-LU`, `el-GR`, `en-GB`, `en-US`, `es-ES`, `fi-FI`, `fr-BE`, `fr-FR`, `fr-LU`, `hu-HU`, `it-IT`, `nl-BE`, `nl-NL`, `pl-PL`, `pt-PT`, `sk-SK`, `sv-SE` |  |  |
| `payment_method_options.paypal.reference` | string |  |  |
| `payment_method_options.paypal.risk_correlation_id` | string |  |  |
| `payment_method_options.paypal.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.pix` | object or "" (to unset) |  |  |
| `payment_method_options.pix.expires_after_seconds` | integer |  |  |
| `payment_method_options.pix.expires_at` | timestamp (Unix seconds) |  |  |
| `payment_method_options.pix.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.promptpay` | object or "" (to unset) |  |  |
| `payment_method_options.promptpay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.revolut_pay` | object or "" (to unset) |  |  |
| `payment_method_options.revolut_pay.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.sepa_debit.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.sofort` | object or "" (to unset) |  |  |
| `payment_method_options.sofort.preferred_language` | enum: ``, `de`, `en`, `es`, `fr`, `it`, `nl`, `pl` |  |  |
| `payment_method_options.sofort.setup_future_usage` | enum: ``, `none`, `off_session` |  |  |
| `payment_method_options.swish` | object or "" (to unset) |  |  |
| `payment_method_options.swish.reference` | string or "" (to unset) |  |  |
| `payment_method_options.swish.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.preferred_settlement_speed` | enum: ``, `fastest`, `standard` |  |  |
| `payment_method_options.us_bank_account.setup_future_usage` | enum: ``, `none`, `off_session`, `on_session` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.wechat_pay` | object or "" (to unset) |  |  |
| `payment_method_options.wechat_pay.app_id` | string |  |  |
| `payment_method_options.wechat_pay.client` | enum: `android`, `ios`, `web` | yes |  |
| `payment_method_options.wechat_pay.setup_future_usage` | enum: `none` |  |  |
| `payment_method_options.zip` | object or "" (to unset) |  |  |
| `payment_method_options.zip.setup_future_usage` | enum: `none` |  |  |
| `payment_method_types` | array of string |  | The list of payment method types (for example, a card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). |
| `radar_options` | object |  | Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session). |
| `radar_options.session` | string |  |  |
| `receipt_email` | string or "" (to unset) |  | Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails). |
| `return_url` | string |  | The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter is only used for cards and other redirect-based payment methods. |
| `setup_future_usage` | enum: ``, `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).<br>If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`. |
| `shipping` | object or "" (to unset) |  | Shipping information for this PaymentIntent. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.carrier` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `shipping.tracking_number` | string |  |  |
| `use_stripe_sdk` | boolean |  | Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions. |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/increment_authorization

operationId: `PostPaymentIntentsIntentIncrementAuthorization`

Perform an incremental authorization on an eligible
[PaymentIntent](https://stripe.com/docs/api/payment_intents/object). To be eligible, the
PaymentIntent’s status must be `requires_capture` and
[incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)
must be `true`.

Incremental authorizations attempt to increase the authorized amount on
your customer’s card to the new, higher `amount` provided. Similar to the
initial authorization, incremental authorizations can be declined. A
single PaymentIntent can call this endpoint multiple times to further
increase the authorized amount.

If the incremental authorization succeeds, the PaymentIntent object
returns with the updated
[amount](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-amount).
If the incremental authorization fails, a
[card_declined](https://stripe.com/docs/error-codes#card-declined) error returns, and no other
fields on the PaymentIntent or Charge update. The PaymentIntent
object remains capturable for the previously authorized amount.

Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.
After it’s captured, a PaymentIntent can no longer be incremented.

Learn more about [incremental authorizations](https://stripe.com/docs/terminal/features/incremental-authorizations).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amount` | integer | yes | The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `statement_descriptor` | string |  | For card charges, use [statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic). Otherwise, you can use this value as the complete description of a charge on your customers' statements. It must contain at least one letter and be 1–22 characters long. |
| `transfer_data` | object |  | The parameters used to automatically create a transfer after the payment is captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `transfer_data.amount` | integer |  |  |

Returns: `payment_intent`

## POST /v1/payment_intents/{intent}/verify_microdeposits

operationId: `PostPaymentIntentsIntentVerifyMicrodeposits`

Verifies microdeposits on a PaymentIntent object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amounts` | array of integer |  | Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account. |
| `client_secret` | string |  | The client secret of the PaymentIntent. |
| `descriptor_code` | string |  | A six-character code starting with SM present in the microdeposit sent to the bank account. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_intent`

# Objects returned

## The `payment_intent` object

A PaymentIntent guides you through the process of collecting a payment from your customer.
We recommend that you create exactly one PaymentIntent for each order or
customer session in your system. You can reference the PaymentIntent later to
see the history of payment attempts for a particular session.

A PaymentIntent transitions through
[multiple statuses](https://stripe.com/docs/payments/intents#intent-statuses)
throughout its lifetime as it interfaces with Stripe.js to perform
authentication flows and ultimately creates at most one successful charge.

Related guide: [Payment Intents API](https://stripe.com/docs/payments/payment-intents)

Expandable fields (pass `expand[]=<field>`): `amount_details`, `application`, `automatic_payment_methods`, `customer`, `invoice`, `last_payment_error`, `latest_charge`, `next_action`, `on_behalf_of`, `payment_method`, `payment_method_configuration_details`, `payment_method_options`, `processing`, `review`, `shipping`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `amount_capturable` | integer |  | Amount that can be captured from this PaymentIntent. |
| `amount_details` | `payment_flows_amount_details` |  |  |
| `amount_received` | integer |  | Amount that this PaymentIntent collects. |
| `application` | string or `application` |  | ID of the Connect application that created the PaymentIntent. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `automatic_payment_methods` | `payment_flows_automatic_payment_methods_payment_intent` |  | Settings to configure compatible payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) |
| `canceled_at` | timestamp (Unix seconds) |  | Populated when `status` is `canceled`, this is the time at which the PaymentIntent was canceled. Measured in seconds since the Unix epoch. |
| `cancellation_reason` | enum: `abandoned`, `automatic`, `duplicate`, `failed_invoice`, `fraudulent`, `requested_by_customer`, `void_invoice` |  | Reason for cancellation of this PaymentIntent, either user-provided (`duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`) or generated by Stripe internally (`failed_invoice`, `void_invoice`, or `automatic`). |
| `capture_method` | enum: `automatic`, `automatic_async`, `manual` | yes | Controls when the funds will be captured from the customer's account. |
| `client_secret` | string |  | The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key. <br>The client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.<br>Refer to our docs to [accept a payment](https://stripe.com/docs/payments/accept-a-payment?ui=elements) and learn about how `client_secret` should be handled. |
| `confirmation_method` | enum: `automatic`, `manual` | yes | Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` or `deleted_customer` |  | ID of the Customer this PaymentIntent belongs to, if one exists.<br>Payment methods attached to other Customers cannot be used with this PaymentIntent.<br>If present in combination with [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage), this PaymentIntent's payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` |  | ID of the invoice that created this PaymentIntent, if it exists. |
| `last_payment_error` | `api_errors` |  | The payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason. |
| `latest_charge` | string or `charge` |  | The latest charge created by this PaymentIntent. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Learn more about [storing information in metadata](https://stripe.com/docs/payments/payment-intents/creating-payment-intents#storing-information-in-metadata). |
| `next_action` | `payment_intent_next_action` |  | If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source. |
| `object` | enum: `payment_intent` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) for which the funds of the PaymentIntent are intended. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts) for details. |
| `payment_method` | string or `payment_method` |  | ID of the payment method used in this PaymentIntent. |
| `payment_method_configuration_details` | `payment_method_config_biz_payment_method_configuration_details` |  | Information about the payment method configuration used for this PaymentIntent. |
| `payment_method_options` | `payment_intent_payment_method_options` |  | Payment-method-specific configuration for this PaymentIntent. |
| `payment_method_types` | array of string | yes | The list of payment method types (e.g. card) that this PaymentIntent is allowed to use. |
| `processing` | `payment_intent_processing` |  | If present, this property tells you about the processing state of the payment. |
| `receipt_email` | string |  | Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails). |
| `review` | string or `review` |  | ID of the review associated with this PaymentIntent, if any. |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |
| `shipping` | `shipping` |  | Shipping information for this PaymentIntent. |
| `statement_descriptor` | string |  | For card charges, use [statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic). Otherwise, you can use this value as the complete description of a charge on your customers' statements. It must contain at least one letter and be 1–22 characters long. |
| `statement_descriptor_suffix` | string |  | Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `status` | enum: `canceled`, `processing`, `requires_action`, `requires_capture`, `requires_confirmation`, `requires_payment_method`, `succeeded` | yes | Status of this PaymentIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `requires_capture`, `canceled`, or `succeeded`. Read more about each PaymentIntent [status](https://stripe.com/docs/payments/intents#intent-statuses). |
| `transfer_data` | `transfer_data` |  | The data that automatically creates a Transfer after the payment finalizes. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| `transfer_group` | string |  | A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers). |

