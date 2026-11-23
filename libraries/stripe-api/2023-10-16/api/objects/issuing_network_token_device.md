# Stripe API 2023-10-16 — `issuing_network_token_device` object

| Field | Type | Required | Description |
|---|---|---|---|
| `device_fingerprint` | string |  | An obfuscated ID derived from the device ID. |
| `ip_address` | string |  | The IP address of the device at provisioning time. |
| `location` | string |  | The geographic latitude/longitude coordinates of the device at provisioning time. The format is [+-]decimal/[+-]decimal. |
| `name` | string |  | The name of the device used for tokenization. |
| `phone_number` | string |  | The phone number of the device used for tokenization. |
| `type` | enum: `other`, `phone`, `watch` |  | The type of device used for tokenization. |

