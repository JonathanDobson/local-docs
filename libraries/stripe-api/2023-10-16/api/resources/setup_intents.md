# Stripe API 2023-10-16 — setup intents

Operations under `/v1/setup_intents` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/setup_intents

operationId: `GetSetupIntents`

Returns a list of SetupIntents.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `attach_to_self` | boolean |  | If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.<br>It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer. |
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return SetupIntents for the customer specified by this customer ID. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_method` | string |  | Only return SetupIntents that associate with the specified payment method. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/setup_intents

operationId: `PostSetupIntents`

Creates a SetupIntent object.

After you create the SetupIntent, attach a payment method and [confirm](https://stripe.com/docs/api/setup_intents/confirm)
it to collect any required permissions to charge the payment method later.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `attach_to_self` | boolean |  | If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.<br>It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer. |
| `automatic_payment_methods` | object |  | When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters. |
| `automatic_payment_methods.allow_redirects` | enum: `always`, `never` |  |  |
| `automatic_payment_methods.enabled` | boolean | yes |  |
| `confirm` | boolean |  | Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary. |
| `confirmation_token` | string |  | ID of the ConfirmationToken used to confirm this SetupIntent.<br>If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence. |
| `customer` | string |  | ID of the Customer this SetupIntent belongs to, if one exists.<br>If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `flow_directions` | array of enum: `inbound`, `outbound` |  | Indicates the directions of money movement for which this payment method is intended to be used.<br>Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes. |
| `mandate_data` | object or "" (to unset) |  | This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm). |
| `mandate_data.customer_acceptance` | object | yes |  |
| `mandate_data.customer_acceptance.accepted_at` | timestamp (Unix seconds) |  |  |
| `mandate_data.customer_acceptance.offline` | object |  |  |
| `mandate_data.customer_acceptance.online` | object |  |  |
| `mandate_data.customer_acceptance.online.ip_address` | string | yes |  |
| `mandate_data.customer_acceptance.online.user_agent` | string | yes |  |
| `mandate_data.customer_acceptance.type` | enum: `offline`, `online` | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `on_behalf_of` | string |  | The Stripe account ID created for this SetupIntent. |
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. |
| `payment_method_configuration` | string |  | The ID of the payment method configuration to use with this SetupIntent. |
| `payment_method_data` | object |  | When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method) value in the SetupIntent. |
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
| `payment_method_options` | object |  | Payment method-specific configuration for this SetupIntent. |
| `payment_method_options.acss_debit` | object |  |  |
| `payment_method_options.acss_debit.currency` | enum: `cad`, `usd` |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.default_for` | array of enum: `invoice`, `subscription` |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.card` | object |  |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.currency` | string | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string |  |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string |  |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` |  |  |
| `payment_method_options.card_present` | object |  |  |
| `payment_method_options.link` | object |  |  |
| `payment_method_options.paypal` | object |  |  |
| `payment_method_options.paypal.billing_agreement_id` | string |  |  |
| `payment_method_options.sepa_debit` | object |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_types` | array of string |  | The list of payment method types (for example, card) that this SetupIntent can use. If you don't provide this, it defaults to ["card"]. |
| `return_url` | string |  | The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm). |
| `single_use` | object |  | If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion. |
| `single_use.amount` | integer | yes |  |
| `single_use.currency` | string | yes |  |
| `usage` | enum: `off_session`, `on_session` |  | Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`. |
| `use_stripe_sdk` | boolean |  | Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions. |

Returns: `setup_intent`

## GET /v1/setup_intents/{intent}

operationId: `GetSetupIntentsIntent`

Retrieves the details of a SetupIntent that has previously been created. 

Client-side retrieval using a publishable key is allowed when the `client_secret` is provided in the query string. 

When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the [SetupIntent](#setup_intent_object) object reference for more details.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_secret` | string |  | The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `intent (path)` | string | yes |  |

Returns: `setup_intent`

## POST /v1/setup_intents/{intent}

operationId: `PostSetupIntentsIntent`

Updates a SetupIntent object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `attach_to_self` | boolean |  | If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.<br>It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer. |
| `customer` | string |  | ID of the Customer this SetupIntent belongs to, if one exists.<br>If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `flow_directions` | array of enum: `inbound`, `outbound` |  | Indicates the directions of money movement for which this payment method is intended to be used.<br>Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. |
| `payment_method_configuration` | string |  | The ID of the payment method configuration to use with this SetupIntent. |
| `payment_method_data` | object |  | When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method) value in the SetupIntent. |
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
| `payment_method_options` | object |  | Payment method-specific configuration for this SetupIntent. |
| `payment_method_options.acss_debit` | object |  |  |
| `payment_method_options.acss_debit.currency` | enum: `cad`, `usd` |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.default_for` | array of enum: `invoice`, `subscription` |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.card` | object |  |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.currency` | string | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string |  |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string |  |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` |  |  |
| `payment_method_options.card_present` | object |  |  |
| `payment_method_options.link` | object |  |  |
| `payment_method_options.paypal` | object |  |  |
| `payment_method_options.paypal.billing_agreement_id` | string |  |  |
| `payment_method_options.sepa_debit` | object |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_types` | array of string |  | The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this array, it defaults to ["card"]. |

Returns: `setup_intent`

## POST /v1/setup_intents/{intent}/cancel

operationId: `PostSetupIntentsIntentCancel`

You can cancel a SetupIntent object when it’s in one of these statuses: `requires_payment_method`, `requires_confirmation`, or `requires_action`. 

After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `cancellation_reason` | enum: `abandoned`, `duplicate`, `requested_by_customer` |  | Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate` |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `setup_intent`

## POST /v1/setup_intents/{intent}/confirm

operationId: `PostSetupIntentsIntentConfirm`

Confirm that your customer intends to set up the current or
provided payment method. For example, you would confirm a SetupIntent
when a customer hits the “Save” button on a payment method management
page on your website.

If the selected payment method does not require any additional
steps from the customer, the SetupIntent will transition to the
`succeeded` status.

Otherwise, it will transition to the `requires_action` status and
suggest additional actions via `next_action`. If setup fails,
the SetupIntent will transition to the
`requires_payment_method` status or the `canceled` status if the
confirmation limit is reached.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `client_secret` | string |  | The client secret of the SetupIntent. |
| `confirmation_token` | string |  | ID of the ConfirmationToken used to confirm this SetupIntent.<br>If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
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
| `payment_method` | string |  | ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. |
| `payment_method_data` | object |  | When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method) value in the SetupIntent. |
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
| `payment_method_options` | object |  | Payment method-specific configuration for this SetupIntent. |
| `payment_method_options.acss_debit` | object |  |  |
| `payment_method_options.acss_debit.currency` | enum: `cad`, `usd` |  |  |
| `payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_method_options.acss_debit.mandate_options.custom_mandate_url` | string or "" (to unset) |  |  |
| `payment_method_options.acss_debit.mandate_options.default_for` | array of enum: `invoice`, `subscription` |  |  |
| `payment_method_options.acss_debit.mandate_options.interval_description` | string |  |  |
| `payment_method_options.acss_debit.mandate_options.payment_schedule` | enum: `combined`, `interval`, `sporadic` |  |  |
| `payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_method_options.card` | object |  |  |
| `payment_method_options.card.mandate_options` | object |  |  |
| `payment_method_options.card.mandate_options.amount` | integer | yes |  |
| `payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` | yes |  |
| `payment_method_options.card.mandate_options.currency` | string | yes |  |
| `payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_method_options.card.mandate_options.end_date` | timestamp (Unix seconds) |  |  |
| `payment_method_options.card.mandate_options.interval` | enum: `day`, `month`, `sporadic`, `week`, `year` | yes |  |
| `payment_method_options.card.mandate_options.interval_count` | integer |  |  |
| `payment_method_options.card.mandate_options.reference` | string | yes |  |
| `payment_method_options.card.mandate_options.start_date` | timestamp (Unix seconds) | yes |  |
| `payment_method_options.card.mandate_options.supported_types` | array of enum: `india` |  |  |
| `payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_method_options.card.three_d_secure` | object |  |  |
| `payment_method_options.card.three_d_secure.ares_trans_status` | enum: `A`, `C`, `I`, `N`, `R`, `U`, `Y` |  |  |
| `payment_method_options.card.three_d_secure.cryptogram` | string |  |  |
| `payment_method_options.card.three_d_secure.electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  |  |
| `payment_method_options.card.three_d_secure.network_options` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires` | object |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_avalgo` | enum: `0`, `1`, `2`, `3`, `4`, `A` | yes |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_exemption` | string |  |  |
| `payment_method_options.card.three_d_secure.network_options.cartes_bancaires.cb_score` | integer |  |  |
| `payment_method_options.card.three_d_secure.requestor_challenge_indicator` | string |  |  |
| `payment_method_options.card.three_d_secure.transaction_id` | string |  |  |
| `payment_method_options.card.three_d_secure.version` | enum: `1.0.2`, `2.1.0`, `2.2.0` |  |  |
| `payment_method_options.card_present` | object |  |  |
| `payment_method_options.link` | object |  |  |
| `payment_method_options.paypal` | object |  |  |
| `payment_method_options.paypal.billing_agreement_id` | string |  |  |
| `payment_method_options.sepa_debit` | object |  |  |
| `payment_method_options.sepa_debit.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_method_options.us_bank_account.financial_connections.return_url` | string |  |  |
| `payment_method_options.us_bank_account.mandate_options` | object |  |  |
| `payment_method_options.us_bank_account.mandate_options.collection_method` | enum: ``, `paper` |  |  |
| `payment_method_options.us_bank_account.networks` | object |  |  |
| `payment_method_options.us_bank_account.networks.requested` | array of enum: `ach`, `us_domestic_wire` |  |  |
| `payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `return_url` | string |  | The URL to redirect your customer back to after they authenticate on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter is only used for cards and other redirect-based payment methods. |
| `use_stripe_sdk` | boolean |  | Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions. |

Returns: `setup_intent`

## POST /v1/setup_intents/{intent}/verify_microdeposits

operationId: `PostSetupIntentsIntentVerifyMicrodeposits`

Verifies microdeposits on a SetupIntent object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `intent (path)` | string | yes |  |
| `amounts` | array of integer |  | Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account. |
| `client_secret` | string |  | The client secret of the SetupIntent. |
| `descriptor_code` | string |  | A six-character code starting with SM present in the microdeposit sent to the bank account. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `setup_intent`

# Objects returned

## The `setup_intent` object

A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.

Create a SetupIntent when you're ready to collect your customer's payment credentials.
Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
The SetupIntent transitions through multiple [statuses](https://stripe.com/docs/payments/intents#intent-statuses) as it guides
you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for future payments.
For example, cardholders in [certain regions](/guides/strong-customer-authentication) might need to be run through
[Strong Customer Authentication](https://stripe.com/docs/strong-customer-authentication) during payment method collection
to streamline later [off-session payments](https://stripe.com/docs/payments/setup-intents).
If you use the SetupIntent with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer),
it automatically attaches the resulting payment method to that Customer after successful setup.
We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide: [Setup Intents API](https://stripe.com/docs/payments/setup-intents)

Expandable fields (pass `expand[]=<field>`): `application`, `automatic_payment_methods`, `customer`, `last_setup_error`, `latest_attempt`, `mandate`, `next_action`, `on_behalf_of`, `payment_method`, `payment_method_configuration_details`, `payment_method_options`, `single_use_mandate`

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or `application` |  | ID of the Connect application that created the SetupIntent. |
| `attach_to_self` | boolean |  | If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.<br>It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer. |
| `automatic_payment_methods` | `payment_flows_automatic_payment_methods_setup_intent` |  | Settings for dynamic payment methods compatible with this Setup Intent |
| `cancellation_reason` | enum: `abandoned`, `duplicate`, `requested_by_customer` |  | Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`. |
| `client_secret` | string |  | The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.<br>The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` or `deleted_customer` |  | ID of the Customer this SetupIntent belongs to, if one exists.<br>If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `flow_directions` | array of enum: `inbound`, `outbound` |  | Indicates the directions of money movement for which this payment method is intended to be used.<br>Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes. |
| `id` | string | yes | Unique identifier for the object. |
| `last_setup_error` | `api_errors` |  | The error encountered in the previous SetupIntent confirmation. |
| `latest_attempt` | string or `setup_attempt` |  | The most recent SetupAttempt for this SetupIntent. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `mandate` | string or `mandate` |  | ID of the multi use Mandate generated by the SetupIntent. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `next_action` | `setup_intent_next_action` |  | If present, this property tells you what actions you need to take in order for your customer to continue payment setup. |
| `object` | enum: `setup_intent` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) for which the setup is intended. |
| `payment_method` | string or `payment_method` |  | ID of the payment method used with this SetupIntent. |
| `payment_method_configuration_details` | `payment_method_config_biz_payment_method_configuration_details` |  | Information about the payment method configuration used for this Setup Intent. |
| `payment_method_options` | `setup_intent_payment_method_options` |  | Payment method-specific configuration for this SetupIntent. |
| `payment_method_types` | array of string | yes | The list of payment method types (e.g. card) that this SetupIntent is allowed to set up. |
| `single_use_mandate` | string or `mandate` |  | ID of the single_use Mandate generated by the SetupIntent. |
| `status` | enum: `canceled`, `processing`, `requires_action`, `requires_confirmation`, `requires_payment_method`, `succeeded` | yes | [Status](https://stripe.com/docs/payments/intents#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`. |
| `usage` | string | yes | Indicates how the payment method is intended to be used in the future.<br>Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`. |

