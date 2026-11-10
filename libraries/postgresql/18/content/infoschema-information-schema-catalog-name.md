---
source: https://www.postgresql.org/docs/18/infoschema-information-schema-catalog-name.html
title: "35.3. information_schema_catalog_name"
---


## 35.3. `information_schema_catalog_name`

`information_schema_catalog_name` is a table that always contains one row and one column containing the name of the current database (current catalog, in SQL terminology).

**Table 35.1. `information_schema_catalog_name` Columns**

| Column Type  Description |
| --- |
| `catalog_name` `sql_identifier`  Name of the database that contains this information schema |
