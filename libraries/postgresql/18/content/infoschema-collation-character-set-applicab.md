---
source: https://www.postgresql.org/docs/18/infoschema-collation-character-set-applicab.html
title: "35.11. collation_character_set_​applicability"
---


## 35.11. `collation_character_set_​applicability`

The view `collation_character_set_applicability` identifies which character set the available collations are applicable to. In PostgreSQL, there is only one character set per database (see explanation in [Section 35.7](infoschema-character-sets.html "35.7. character_sets")), so this view does not provide much useful information.

**Table 35.9. `collation_character_set_applicability` Columns**

| Column Type  Description |
| --- |
| `collation_catalog` `sql_identifier`  Name of the database containing the collation (always the current database) |
| `collation_schema` `sql_identifier`  Name of the schema containing the collation |
| `collation_name` `sql_identifier`  Name of the default collation |
| `character_set_catalog` `sql_identifier`  Character sets are currently not implemented as schema objects, so this column is null |
| `character_set_schema` `sql_identifier`  Character sets are currently not implemented as schema objects, so this column is null |
| `character_set_name` `sql_identifier`  Name of the character set |
