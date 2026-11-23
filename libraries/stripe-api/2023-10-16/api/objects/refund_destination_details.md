# Stripe API 2023-10-16 — `refund_destination_details` object

Expandable fields (pass `expand[]=<field>`): `affirm`, `afterpay_clearpay`, `alipay`, `au_bank_transfer`, `blik`, `br_bank_transfer`, `card`, `cashapp`, `customer_cash_balance`, `eps`, `eu_bank_transfer`, `gb_bank_transfer`, `giropay`, `grabpay`, `jp_bank_transfer`, `klarna`, `mx_bank_transfer`, `p24`, `paynow`, `paypal`, `pix`, `revolut`, `sofort`, `swish`, `th_bank_transfer`, `us_bank_transfer`, `wechat_pay`, `zip`

| Field | Type | Required | Description |
|---|---|---|---|
| `affirm` | `destination_details_unimplemented` |  |  |
| `afterpay_clearpay` | `destination_details_unimplemented` |  |  |
| `alipay` | `destination_details_unimplemented` |  |  |
| `au_bank_transfer` | `destination_details_unimplemented` |  |  |
| `blik` | `refund_destination_details_generic` |  |  |
| `br_bank_transfer` | `refund_destination_details_generic` |  |  |
| `card` | `refund_destination_details_card` |  |  |
| `cashapp` | `destination_details_unimplemented` |  |  |
| `customer_cash_balance` | `destination_details_unimplemented` |  |  |
| `eps` | `destination_details_unimplemented` |  |  |
| `eu_bank_transfer` | `refund_destination_details_generic` |  |  |
| `gb_bank_transfer` | `refund_destination_details_generic` |  |  |
| `giropay` | `destination_details_unimplemented` |  |  |
| `grabpay` | `destination_details_unimplemented` |  |  |
| `jp_bank_transfer` | `refund_destination_details_generic` |  |  |
| `klarna` | `destination_details_unimplemented` |  |  |
| `mx_bank_transfer` | `refund_destination_details_generic` |  |  |
| `p24` | `refund_destination_details_generic` |  |  |
| `paynow` | `destination_details_unimplemented` |  |  |
| `paypal` | `destination_details_unimplemented` |  |  |
| `pix` | `destination_details_unimplemented` |  |  |
| `revolut` | `destination_details_unimplemented` |  |  |
| `sofort` | `destination_details_unimplemented` |  |  |
| `swish` | `refund_destination_details_generic` |  |  |
| `th_bank_transfer` | `refund_destination_details_generic` |  |  |
| `type` | string | yes | The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction. |
| `us_bank_transfer` | `refund_destination_details_generic` |  |  |
| `wechat_pay` | `destination_details_unimplemented` |  |  |
| `zip` | `destination_details_unimplemented` |  |  |

