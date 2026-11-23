# Stripe API 2023-10-16 — `payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `ach_credit_transfer`, `ach_debit`, `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `card_present`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `interac_present`, `klarna`, `konbini`, `link`, `mobilepay`, `multibanco`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `stripe_account`, `swish`, `us_bank_account`, `wechat`, `wechat_pay`, `zip`

| Field | Type | Required | Description |
|---|---|---|---|
| `ach_credit_transfer` | `payment_method_details_ach_credit_transfer` |  |  |
| `ach_debit` | `payment_method_details_ach_debit` |  |  |
| `acss_debit` | `payment_method_details_acss_debit` |  |  |
| `affirm` | `payment_method_details_affirm` |  |  |
| `afterpay_clearpay` | `payment_method_details_afterpay_clearpay` |  |  |
| `alipay` | `payment_flows_private_payment_methods_alipay_details` |  |  |
| `au_becs_debit` | `payment_method_details_au_becs_debit` |  |  |
| `bacs_debit` | `payment_method_details_bacs_debit` |  |  |
| `bancontact` | `payment_method_details_bancontact` |  |  |
| `blik` | `payment_method_details_blik` |  |  |
| `boleto` | `payment_method_details_boleto` |  |  |
| `card` | `payment_method_details_card` |  |  |
| `card_present` | `payment_method_details_card_present` |  |  |
| `cashapp` | `payment_method_details_cashapp` |  |  |
| `customer_balance` | `payment_method_details_customer_balance` |  |  |
| `eps` | `payment_method_details_eps` |  |  |
| `fpx` | `payment_method_details_fpx` |  |  |
| `giropay` | `payment_method_details_giropay` |  |  |
| `grabpay` | `payment_method_details_grabpay` |  |  |
| `ideal` | `payment_method_details_ideal` |  |  |
| `interac_present` | `payment_method_details_interac_present` |  |  |
| `klarna` | `payment_method_details_klarna` |  |  |
| `konbini` | `payment_method_details_konbini` |  |  |
| `link` | `payment_method_details_link` |  |  |
| `mobilepay` | `payment_method_details_mobilepay` |  |  |
| `multibanco` | `payment_method_details_multibanco` |  |  |
| `oxxo` | `payment_method_details_oxxo` |  |  |
| `p24` | `payment_method_details_p24` |  |  |
| `paynow` | `payment_method_details_paynow` |  |  |
| `paypal` | `payment_method_details_paypal` |  |  |
| `pix` | `payment_method_details_pix` |  |  |
| `promptpay` | `payment_method_details_promptpay` |  |  |
| `revolut_pay` | `payment_method_details_revolut_pay` |  |  |
| `sepa_debit` | `payment_method_details_sepa_debit` |  |  |
| `sofort` | `payment_method_details_sofort` |  |  |
| `stripe_account` | `payment_method_details_stripe_account` |  |  |
| `swish` | `payment_method_details_swish` |  |  |
| `type` | string | yes | The type of transaction-specific details of the payment method used in the payment, one of `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `stripe_account`, or `wechat`. An additional hash is included on `payment_method_details` with a name matching this value. It contains information specific to the payment method. |
| `us_bank_account` | `payment_method_details_us_bank_account` |  |  |
| `wechat` | `payment_method_details_wechat` |  |  |
| `wechat_pay` | `payment_method_details_wechat_pay` |  |  |
| `zip` | `payment_method_details_zip` |  |  |

