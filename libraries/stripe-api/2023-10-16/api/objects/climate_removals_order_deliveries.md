# Stripe API 2023-10-16 — `climate_removals_order_deliveries` object

The delivery of a specified quantity of carbon for an order.

Expandable fields (pass `expand[]=<field>`): `location`, `supplier`

| Field | Type | Required | Description |
|---|---|---|---|
| `delivered_at` | timestamp (Unix seconds) | yes | Time at which the delivery occurred. Measured in seconds since the Unix epoch. |
| `location` | `climate_removals_location` |  | Specific location of this delivery. |
| `metric_tons` | string | yes | Quantity of carbon removal supplied by this delivery. |
| `registry_url` | string |  | Once retired, a URL to the registry entry for the tons from this delivery. |
| `supplier` | `climate.supplier` | yes |  |

