# Stripe API 2023-10-16 — `payment_intent_processing_customer_notification` object

| Field | Type | Required | Description |
|---|---|---|---|
| `approval_requested` | boolean |  | Whether customer approval has been requested for this payment. For payments greater than INR 15000 or mandate amount, the customer must provide explicit approval of the payment with their bank. |
| `completes_at` | timestamp (Unix seconds) |  | If customer approval is required, they need to provide approval before this time. |

