# Stripe API 2023-10-16 — `account_requirements_alternative` object

| Field | Type | Required | Description |
|---|---|---|---|
| `alternative_fields_due` | array of string | yes | Fields that can be provided to satisfy all fields in `original_fields_due`. |
| `original_fields_due` | array of string | yes | Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`. |

