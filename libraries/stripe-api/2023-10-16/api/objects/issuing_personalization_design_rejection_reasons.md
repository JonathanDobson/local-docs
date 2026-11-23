# Stripe API 2023-10-16 — `issuing_personalization_design_rejection_reasons` object

| Field | Type | Required | Description |
|---|---|---|---|
| `card_logo` | array of enum: `geographic_location`, `inappropriate`, `network_name`, `non_binary_image`, `non_fiat_currency`, `other`, `other_entity`, `promotional_material` |  | The reason(s) the card logo was rejected. |
| `carrier_text` | array of enum: `geographic_location`, `inappropriate`, `network_name`, `non_fiat_currency`, `other`, `other_entity`, `promotional_material` |  | The reason(s) the carrier text was rejected. |

