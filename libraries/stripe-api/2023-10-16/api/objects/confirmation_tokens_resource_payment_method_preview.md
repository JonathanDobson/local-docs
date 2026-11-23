# Stripe API 2023-10-16 — `confirmation_tokens_resource_payment_method_preview` object

Details of the PaymentMethod collected by Payment Element

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billing_details`, `blik`, `boleto`, `card`, `card_present`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `interac_present`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip`

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
| `customer_balance` | `payment_method_customer_balance` |  |  |
| `eps` | `payment_method_eps` |  |  |
| `fpx` | `payment_method_fpx` |  |  |
| `giropay` | `payment_method_giropay` |  |  |
| `grabpay` | `payment_method_grabpay` |  |  |
| `ideal` | `payment_method_ideal` |  |  |
| `interac_present` | `payment_method_interac_present` |  |  |
| `klarna` | `payment_method_klarna` |  |  |
| `konbini` | `payment_method_konbini` |  |  |
| `link` | `payment_method_link` |  |  |
| `mobilepay` | `payment_method_mobilepay` |  |  |
| `oxxo` | `payment_method_oxxo` |  |  |
| `p24` | `payment_method_p24` |  |  |
| `paynow` | `payment_method_paynow` |  |  |
| `paypal` | `payment_method_paypal` |  |  |
| `pix` | `payment_method_pix` |  |  |
| `promptpay` | `payment_method_promptpay` |  |  |
| `revolut_pay` | `payment_method_revolut_pay` |  |  |
| `sepa_debit` | `payment_method_sepa_debit` |  |  |
| `sofort` | `payment_method_sofort` |  |  |
| `swish` | `payment_method_swish` |  |  |
| `type` | enum: `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `card_present`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `interac_present`, `klarna`, `konbini`, `link`, `mobilepay`, `oxxo`, `p24`, `paynow`, `paypal`, `pix`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `swish`, `us_bank_account`, `wechat_pay`, `zip` | yes | The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type. |
| `us_bank_account` | `payment_method_us_bank_account` |  |  |
| `wechat_pay` | `payment_method_wechat_pay` |  |  |
| `zip` | `payment_method_zip` |  |  |

