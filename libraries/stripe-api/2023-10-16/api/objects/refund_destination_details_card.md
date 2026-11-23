# Stripe API 2023-10-16 — `refund_destination_details_card` object

| Field | Type | Required | Description |
|---|---|---|---|
| `reference` | string |  | Value of the reference number assigned to the refund. |
| `reference_status` | string |  | Status of the reference number on the refund. This can be `pending`, `available` or `unavailable`. |
| `reference_type` | string |  | Type of the reference number assigned to the refund. |
| `type` | enum: `pending`, `refund`, `reversal` | yes | The type of refund. This can be `refund`, `reversal`, or `pending`. |

