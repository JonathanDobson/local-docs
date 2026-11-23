# Stripe API 2023-10-16 — `platform_tax_fee` object

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The Connected account that incurred this charge. |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `platform_tax_fee` | yes | String representing the object's type. Objects of the same type share the same value. |
| `source_transaction` | string | yes | The payment object that caused this tax to be inflicted. |
| `type` | string | yes | The type of tax (VAT). |

