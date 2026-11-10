---
source: https://www.postgresql.org/docs/18/view-pg-indexes.html
title: "53.12. pg_indexes"
---


## 53.12. `pg_indexes`

The view `pg_indexes` provides access to useful information about each index in the database.

**Table 53.12. `pg_indexes` Columns**

| Column Type  Description |
| --- |
| `schemaname` `name` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)  Name of schema containing table and index |
| `tablename` `name` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relname`)  Name of table the index is for |
| `indexname` `name` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relname`)  Name of index |
| `tablespace` `name` (references [`pg_tablespace`](catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)  Name of tablespace containing index (null if default for database) |
| `indexdef` `text`  Index definition (a reconstructed [CREATE INDEX](sql-createindex.html "CREATE INDEX") command) |
