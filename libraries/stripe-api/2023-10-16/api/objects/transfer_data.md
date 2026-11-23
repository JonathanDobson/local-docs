# Stripe API 2023-10-16 — `transfer_data` object

Expandable fields (pass `expand[]=<field>`): `destination`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `destination` | string or `account` | yes | The account (if any) that the payment is attributed to for tax reporting, and where funds from the payment are transferred to after payment success. |

