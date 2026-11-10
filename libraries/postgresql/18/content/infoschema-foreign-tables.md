---
source: https://www.postgresql.org/docs/18/infoschema-foreign-tables.html
title: "35.31. foreign_tables"
---


## 35.31. `foreign_tables`

The view `foreign_tables` contains all foreign tables defined in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.29. `foreign_tables` Columns**

| Column Type  Description |
| --- |
| `foreign_table_catalog` `sql_identifier`  Name of the database that the foreign table is defined in (always the current database) |
| `foreign_table_schema` `sql_identifier`  Name of the schema that contains the foreign table |
| `foreign_table_name` `sql_identifier`  Name of the foreign table |
| `foreign_server_catalog` `sql_identifier`  Name of the database that the foreign server is defined in (always the current database) |
| `foreign_server_name` `sql_identifier`  Name of the foreign server |
