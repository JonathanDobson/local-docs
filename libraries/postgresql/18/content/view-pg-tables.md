---
source: https://www.postgresql.org/docs/18/view-pg-tables.html
title: "53.32. pg_tables"
---


## 53.32. `pg_tables`

The view `pg_tables` provides access to useful information about each table in the database.

**Table 53.32. `pg_tables` Columns**

| Column Type  Description |
| --- |
| `schemaname` `name` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)  Name of schema containing table |
| `tablename` `name` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relname`)  Name of table |
| `tableowner` `name` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`rolname`)  Name of table's owner |
| `tablespace` `name` (references [`pg_tablespace`](catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)  Name of tablespace containing table (null if default for database) |
| `hasindexes` `bool` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relhasindex`)  True if table has (or recently had) any indexes |
| `hasrules` `bool` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relhasrules`)  True if table has (or once had) rules |
| `hastriggers` `bool` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relhastriggers`)  True if table has (or once had) triggers |
| `rowsecurity` `bool` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relrowsecurity`)  True if row security is enabled on the table |
