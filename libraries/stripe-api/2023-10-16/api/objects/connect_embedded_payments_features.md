# Stripe API 2023-10-16 — `connect_embedded_payments_features` object

| Field | Type | Required | Description |
|---|---|---|---|
| `capture_payments` | boolean | yes | Whether to allow capturing and cancelling payment intents. This is `true` by default. |
| `destination_on_behalf_of_charge_management` | boolean |  | Whether to allow connected accounts to manage destination charges that are created on behalf of them. This is `false` by default. |
| `dispute_management` | boolean | yes | Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default. |
| `refund_management` | boolean | yes | Whether to allow sending refunds. This is `true` by default. |

