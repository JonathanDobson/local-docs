# Stripe API 2023-10-16 — `issuing_transaction_flight_data` object

Expandable fields (pass `expand[]=<field>`): `segments`

| Field | Type | Required | Description |
|---|---|---|---|
| `departure_at` | integer |  | The time that the flight departed. |
| `passenger_name` | string |  | The name of the passenger. |
| `refundable` | boolean |  | Whether the ticket is refundable. |
| `segments` | array of `issuing_transaction_flight_data_leg` |  | The legs of the trip. |
| `travel_agency` | string |  | The travel agency that issued the ticket. |

