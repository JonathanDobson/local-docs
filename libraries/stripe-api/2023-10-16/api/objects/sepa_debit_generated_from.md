# Stripe API 2023-10-16 — `sepa_debit_generated_from` object

Expandable fields (pass `expand[]=<field>`): `charge`, `setup_attempt`

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string or `charge` |  | The ID of the Charge that generated this PaymentMethod, if any. |
| `setup_attempt` | string or `setup_attempt` |  | The ID of the SetupAttempt that generated this PaymentMethod, if any. |

