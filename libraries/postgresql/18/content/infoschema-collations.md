---
source: https://www.postgresql.org/docs/18/infoschema-collations.html
title: "35.10. collations"
---


## 35.10. `collations`

The view `collations` contains the collations available in the current database.

**Table 35.8. `collations` Columns**

| Column Type  Description |
| --- |
| `collation_catalog` `sql_identifier`  Name of the database containing the collation (always the current database) |
| `collation_schema` `sql_identifier`  Name of the schema containing the collation |
| `collation_name` `sql_identifier`  Name of the default collation |
| `pad_attribute` `character_data`  Always `NO PAD` (The alternative `PAD SPACE` is not supported by PostgreSQL.) |
