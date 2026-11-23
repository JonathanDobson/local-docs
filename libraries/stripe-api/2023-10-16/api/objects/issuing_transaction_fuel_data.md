# Stripe API 2023-10-16 — `issuing_transaction_fuel_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | yes | The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`. |
| `unit` | string | yes | The units for `volume_decimal`. One of `us_gallon` or `liter`. |
| `unit_cost_decimal` | string | yes | The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places. |
| `volume_decimal` | string |  | The volume of the fuel that was pumped, represented as a decimal string with at most 12 decimal places. |

