# Stripe API 2023-10-16 — `dispute_payment_method_details_card` object

| Field | Type | Required | Description |
|---|---|---|---|
| `brand` | string | yes | Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `network_reason_code` | string |  | The card network's specific dispute reason code, which maps to one of Stripe's primary dispute categories to simplify response guidance. The [Network code map](https://stripe.com/docs/disputes/categories#network-code-map) lists all available dispute reason codes by network. |

