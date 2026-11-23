# Stripe API 2023-10-16 — `price_tier` object

| Field | Type | Required | Description |
|---|---|---|---|
| `flat_amount` | integer |  | Price for the entire tier. |
| `flat_amount_decimal` | string |  | Same as `flat_amount`, but contains a decimal value with at most 12 decimal places. |
| `unit_amount` | integer |  | Per unit price for units relevant to the tier. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but contains a decimal value with at most 12 decimal places. |
| `up_to` | integer |  | Up to and including to this quantity will be contained in the tier. |

