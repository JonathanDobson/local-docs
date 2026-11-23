# Stripe API 2023-10-16 — `issuing_transaction_purchase_details` object

Expandable fields (pass `expand[]=<field>`): `flight`, `fuel`, `lodging`, `receipt`

| Field | Type | Required | Description |
|---|---|---|---|
| `flight` | `issuing_transaction_flight_data` |  | Information about the flight that was purchased with this transaction. |
| `fuel` | `issuing_transaction_fuel_data` |  | Information about fuel that was purchased with this transaction. |
| `lodging` | `issuing_transaction_lodging_data` |  | Information about lodging that was purchased with this transaction. |
| `receipt` | array of `issuing_transaction_receipt_data` |  | The line items in the purchase. |
| `reference` | string |  | A merchant-specific order number. |

