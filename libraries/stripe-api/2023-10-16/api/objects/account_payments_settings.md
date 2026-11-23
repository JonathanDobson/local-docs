# Stripe API 2023-10-16 — `account_payments_settings` object

| Field | Type | Required | Description |
|---|---|---|---|
| `statement_descriptor` | string |  | The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. |
| `statement_descriptor_kana` | string |  | The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only) |
| `statement_descriptor_kanji` | string |  | The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only) |
| `statement_descriptor_prefix_kana` | string |  | The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion. |
| `statement_descriptor_prefix_kanji` | string |  | The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion. |

