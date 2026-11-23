# Stripe API 2023-10-16 — `mandate_bacs_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `network_status` | enum: `accepted`, `pending`, `refused`, `revoked` | yes | The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`. |
| `reference` | string | yes | The unique reference identifying the mandate on the Bacs network. |
| `revocation_reason` | enum: `account_closed`, `bank_account_restricted`, `bank_ownership_changed`, `could_not_process`, `debit_not_authorized` |  | When the mandate is revoked on the Bacs network this field displays the reason for the revocation. |
| `url` | string | yes | The URL that will contain the mandate that the customer has signed. |

