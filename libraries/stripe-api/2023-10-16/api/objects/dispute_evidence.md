# Stripe API 2023-10-16 — `dispute_evidence` object

Expandable fields (pass `expand[]=<field>`): `cancellation_policy`, `customer_communication`, `customer_signature`, `duplicate_charge_documentation`, `receipt`, `refund_policy`, `service_documentation`, `shipping_documentation`, `uncategorized_file`

| Field | Type | Required | Description |
|---|---|---|---|
| `access_activity_log` | string |  | Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity. |
| `billing_address` | string |  | The billing address provided by the customer. |
| `cancellation_policy` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer. |
| `cancellation_policy_disclosure` | string |  | An explanation of how and when the customer was shown your refund policy prior to purchase. |
| `cancellation_rebuttal` | string |  | A justification for why the customer's subscription was not canceled. |
| `customer_communication` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service. |
| `customer_email_address` | string |  | The email address of the customer. |
| `customer_name` | string |  | The name of the customer. |
| `customer_purchase_ip` | string |  | The IP address that the customer used when making the purchase. |
| `customer_signature` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer's signature. |
| `duplicate_charge_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate. |
| `duplicate_charge_explanation` | string |  | An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate. |
| `duplicate_charge_id` | string |  | The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge. |
| `product_description` | string |  | A description of the product or service that was sold. |
| `receipt` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge. |
| `refund_policy` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer. |
| `refund_policy_disclosure` | string |  | Documentation demonstrating that the customer was shown your refund policy prior to purchase. |
| `refund_refusal_explanation` | string |  | A justification for why the customer is not entitled to a refund. |
| `service_date` | string |  | The date on which the customer received or began receiving the purchased service, in a clear human-readable format. |
| `service_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement. |
| `shipping_address` | string |  | The address to which a physical product was shipped. You should try to include as complete address information as possible. |
| `shipping_carrier` | string |  | The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas. |
| `shipping_date` | string |  | The date on which a physical product began its route to the shipping address, in a clear human-readable format. |
| `shipping_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer's full shipping address, if possible. |
| `shipping_tracking_number` | string |  | The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas. |
| `uncategorized_file` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements. |
| `uncategorized_text` | string |  | Any additional evidence or statements. |

