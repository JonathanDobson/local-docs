# Stripe API 2023-10-16 — test helpers / confirmation tokens

Operations under `/v1/test_helpers/confirmation_tokens` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/test_helpers/confirmation_tokens

operationId: `PostTestHelpersConfirmationTokens`

Creates a test mode Confirmation Token server side for your integration tests.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_method` | string |  | ID of an existing PaymentMethod. |
| `payment_method_data` | object |  | If provided, this hash will be used to create a PaymentMethod. |
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
| `return_url` | string |  | Return URL used to confirm the Intent. |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with this ConfirmationToken's payment method.<br>The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. |
| `shipping` | object |  | Shipping information for this ConfirmationToken. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string or "" (to unset) |  |  |

Returns: `confirmation_token`

# Objects returned

## The `confirmation_token` object

ConfirmationTokens help transport client side data collected by Stripe JS over
to your server for confirming a PaymentIntent or SetupIntent. If the confirmation
is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:
- [Finalize payments on the server](https://stripe.com/docs/payments/finalize-payments-on-the-server)
- [Build two-step confirmation](https://stripe.com/docs/payments/build-a-two-step-confirmation).

Expandable fields (pass `expand[]=<field>`): `mandate_data`, `payment_method_preview`, `shipping`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires_at` | timestamp (Unix seconds) |  | Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent. This is set to null once this ConfirmationToken has been used. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `mandate_data` | `confirmation_tokens_resource_mandate_data` |  | Data used for generating a Mandate. |
| `object` | enum: `confirmation_token` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string |  | ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used. |
| `payment_method_preview` | `confirmation_tokens_resource_payment_method_preview` |  | Payment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken. |
| `return_url` | string |  | Return URL used to confirm the Intent. |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with this ConfirmationToken's payment method.<br>The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. |
| `setup_intent` | string |  | ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used. |
| `shipping` | `confirmation_tokens_resource_shipping` |  | Shipping information collected on this ConfirmationToken. |
| `use_stripe_sdk` | boolean | yes | Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to `true` on ConfirmationToken. |

