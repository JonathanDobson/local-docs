# Stripe API 2023-10-16 — `invoice_mandate_options_card` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | Amount to be charged for future payments. |
| `amount_type` | enum: `fixed`, `maximum` |  | One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param. |
| `description` | string |  | A description of the mandate or subscription that is meant to be displayed to the customer. |

