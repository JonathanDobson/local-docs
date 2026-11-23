# Stripe API 2023-10-16 — `connect_collection_transfer` object

Expandable fields (pass `expand[]=<field>`): `destination`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount transferred, in cents (or local equivalent). |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `destination` | string or `account` | yes | ID of the account that funds are being collected for. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `connect_collection_transfer` | yes | String representing the object's type. Objects of the same type share the same value. |

