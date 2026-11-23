# Stripe API 2023-10-16 — `issuing_authorization_verification_data` object

Expandable fields (pass `expand[]=<field>`): `authentication_exemption`, `three_d_secure`

| Field | Type | Required | Description |
|---|---|---|---|
| `address_line1_check` | enum: `match`, `mismatch`, `not_provided` | yes | Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`. |
| `address_postal_code_check` | enum: `match`, `mismatch`, `not_provided` | yes | Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`. |
| `authentication_exemption` | `issuing_authorization_authentication_exemption` |  | The exemption applied to this authorization. |
| `cvc_check` | enum: `match`, `mismatch`, `not_provided` | yes | Whether the cardholder provided a CVC and if it matched Stripe’s record. |
| `expiry_check` | enum: `match`, `mismatch`, `not_provided` | yes | Whether the cardholder provided an expiry date and if it matched Stripe’s record. |
| `postal_code` | string |  | The postal code submitted as part of the authorization used for postal code verification. |
| `three_d_secure` | `issuing_authorization_three_d_secure` |  | 3D Secure details. |

