# Stripe API 2023-10-16 — `account_card_payments_settings` object

Expandable fields (pass `expand[]=<field>`): `decline_on`

| Field | Type | Required | Description |
|---|---|---|---|
| `decline_on` | `account_decline_charge_on` |  |  |
| `statement_descriptor_prefix` | string |  | The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion. |
| `statement_descriptor_prefix_kana` | string |  | The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion. |
| `statement_descriptor_prefix_kanji` | string |  | The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion. |

