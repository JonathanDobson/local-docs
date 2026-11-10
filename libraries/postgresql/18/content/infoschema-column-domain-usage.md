---
source: https://www.postgresql.org/docs/18/infoschema-column-domain-usage.html
title: "35.13. column_domain_usage"
---


## 35.13. `column_domain_usage`

The view `column_domain_usage` identifies all columns (of a table or a view) that make use of some domain defined in the current database and owned by a currently enabled role.

**Table 35.11. `column_domain_usage` Columns**

| Column Type  Description |
| --- |
| `domain_catalog` `sql_identifier`  Name of the database containing the domain (always the current database) |
| `domain_schema` `sql_identifier`  Name of the schema containing the domain |
| `domain_name` `sql_identifier`  Name of the domain |
| `table_catalog` `sql_identifier`  Name of the database containing the table (always the current database) |
| `table_schema` `sql_identifier`  Name of the schema containing the table |
| `table_name` `sql_identifier`  Name of the table |
| `column_name` `sql_identifier`  Name of the column |
