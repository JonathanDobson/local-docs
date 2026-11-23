# Stripe API 2023-10-16 — `payment_method_details_giropay` object

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_code` | string |  | Bank code of bank associated with the bank account. |
| `bank_name` | string |  | Name of the bank associated with the bank account. |
| `bic` | string |  | Bank Identifier Code of the bank associated with the bank account. |
| `verified_name` | string |  | Owner's verified full name. Values are verified or provided by Giropay directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. Giropay rarely provides this information so the attribute is usually empty. |

