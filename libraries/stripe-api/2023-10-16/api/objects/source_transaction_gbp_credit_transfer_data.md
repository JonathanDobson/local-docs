# Stripe API 2023-10-16 — `source_transaction_gbp_credit_transfer_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `fingerprint` | string |  | Bank account fingerprint associated with the Stripe owned bank account receiving the transfer. |
| `funding_method` | string |  | The credit transfer rails the sender used to push this transfer. The possible rails are: Faster Payments, BACS, CHAPS, and wire transfers. Currently only Faster Payments is supported. |
| `last4` | string |  | Last 4 digits of sender account number associated with the transfer. |
| `reference` | string |  | Sender entered arbitrary information about the transfer. |
| `sender_account_number` | string |  | Sender account number associated with the transfer. |
| `sender_name` | string |  | Sender name associated with the transfer. |
| `sender_sort_code` | string |  | Sender sort code associated with the transfer. |

