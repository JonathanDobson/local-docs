# Stripe API 2023-10-16 — `dispute_evidence_details` object

| Field | Type | Required | Description |
|---|---|---|---|
| `due_by` | timestamp (Unix seconds) |  | Date by which evidence must be submitted in order to successfully challenge dispute. Will be 0 if the customer's bank or credit card company doesn't allow a response for this particular dispute. |
| `has_evidence` | boolean | yes | Whether evidence has been staged for this dispute. |
| `past_due` | boolean | yes | Whether the last evidence submission was submitted past the due date. Defaults to `false` if no evidence submissions have occurred. If `true`, then delivery of the latest evidence is *not* guaranteed. |
| `submission_count` | integer | yes | The number of times evidence has been submitted. Typically, you may only submit evidence once. |

