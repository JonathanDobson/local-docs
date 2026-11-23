# Stripe API 2023-10-16 — `tax_deducted_at_source` object

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `tax_deducted_at_source` | yes | String representing the object's type. Objects of the same type share the same value. |
| `period_end` | timestamp (Unix seconds) | yes | The end of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period. |
| `period_start` | timestamp (Unix seconds) | yes | The start of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period. |
| `tax_deduction_account_number` | string | yes | The TAN that was supplied to Stripe when TDS was assessed |

