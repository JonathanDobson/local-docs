# Stripe API 2023-10-16 — `payment_method_card_checks` object

| Field | Type | Required | Description |
|---|---|---|---|
| `address_line1_check` | string |  | If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`. |
| `address_postal_code_check` | string |  | If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`. |
| `cvc_check` | string |  | If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`. |

