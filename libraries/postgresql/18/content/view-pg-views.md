---
source: https://www.postgresql.org/docs/18/view-pg-views.html
title: "53.37. pg_views"
---


## 53.37. `pg_views`

The view `pg_views` provides access to useful information about each view in the database.

**Table 53.37. `pg_views` Columns**

| Column Type  Description |
| --- |
| `schemaname` `name` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)  Name of schema containing view |
| `viewname` `name` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relname`)  Name of view |
| `viewowner` `name` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`rolname`)  Name of view's owner |
| `definition` `text`  View definition (a reconstructed [SELECT](sql-select.html "SELECT") query) |
