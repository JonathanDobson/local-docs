# Stripe API 2023-10-16 — `connect_embedded_payouts_features` object

| Field | Type | Required | Description |
|---|---|---|---|
| `edit_payout_schedule` | boolean | yes | Whether to allow payout schedule to be changed. Default `true` when Stripe owns Loss Liability, default `false` otherwise. |
| `instant_payouts` | boolean | yes | Whether to allow creation of instant payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise. |
| `standard_payouts` | boolean | yes | Whether to allow creation of standard payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise. |

