# Stripe API 2023-10-16 — `setup_intent_payment_method_options_card` object

Expandable fields (pass `expand[]=<field>`): `mandate_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `mandate_options` | `setup_intent_payment_method_options_card_mandate_options` |  | Configuration options for setting up an eMandate for cards issued in India. |
| `network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  | Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the setup intent. Can be only set confirm-time. |
| `request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  | We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine. |

