---
source: https://www.postgresql.org/docs/18/infoschema-foreign-table-options.html
title: "35.30. foreign_table_options"
---


## 35.30. `foreign_table_options`

The view `foreign_table_options` contains all the options defined for foreign tables in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.28. `foreign_table_options` Columns**

| Column Type  Description |
| --- |
| `foreign_table_catalog` `sql_identifier`  Name of the database that contains the foreign table (always the current database) |
| `foreign_table_schema` `sql_identifier`  Name of the schema that contains the foreign table |
| `foreign_table_name` `sql_identifier`  Name of the foreign table |
| `option_name` `sql_identifier`  Name of an option |
| `option_value` `character_data`  Value of the option |
