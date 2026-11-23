# Stripe API 2023-10-16 — `legal_entity_company` object

Expandable fields (pass `expand[]=<field>`): `address`, `address_kana`, `address_kanji`, `ownership_declaration`, `verification`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  |  |
| `address_kana` | `legal_entity_japan_address` |  | The Kana variation of the company's primary address (Japan only). |
| `address_kanji` | `legal_entity_japan_address` |  | The Kanji variation of the company's primary address (Japan only). |
| `directors_provided` | boolean |  | Whether the company's directors have been provided. This Boolean will be `true` if you've manually indicated that all directors are provided via [the `directors_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-directors_provided). |
| `executives_provided` | boolean |  | Whether the company's executives have been provided. This Boolean will be `true` if you've manually indicated that all executives are provided via [the `executives_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided. |
| `export_license_id` | string |  | The export license ID number of the company, also referred as Import Export Code (India only). |
| `export_purpose_code` | string |  | The purpose code to use for export transactions (India only). |
| `name` | string |  | The company's legal name. |
| `name_kana` | string |  | The Kana variation of the company's legal name (Japan only). |
| `name_kanji` | string |  | The Kanji variation of the company's legal name (Japan only). |
| `owners_provided` | boolean |  | Whether the company's owners have been provided. This Boolean will be `true` if you've manually indicated that all owners are provided via [the `owners_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together). |
| `ownership_declaration` | `legal_entity_ubo_declaration` |  | This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct. |
| `phone` | string |  | The company's phone number (used for verification). |
| `structure` | enum: `free_zone_establishment`, `free_zone_llc`, `government_instrumentality`, `governmental_unit`, `incorporated_non_profit`, `incorporated_partnership`, `limited_liability_partnership`, `llc`, `multi_member_llc`, `private_company`, `private_corporation`, `private_partnership`, `public_company`, `public_corporation`, `public_partnership`, `registered_charity`, `single_member_llc`, `sole_establishment`, `sole_proprietorship`, `tax_exempt_government_instrumentality`, `unincorporated_association`, `unincorporated_non_profit`, `unincorporated_partnership` |  | The category identifying the legal structure of the company or legal entity. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details. |
| `tax_id_provided` | boolean |  | Whether the company's business ID number was provided. |
| `tax_id_registrar` | string |  | The jurisdiction in which the `tax_id` is registered (Germany-based companies only). |
| `vat_id_provided` | boolean |  | Whether the company's business VAT number was provided. |
| `verification` | `legal_entity_company_verification` |  | Information on the verification state of the company. |

