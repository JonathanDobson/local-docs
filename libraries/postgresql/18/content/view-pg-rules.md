---
source: https://www.postgresql.org/docs/18/view-pg-rules.html
title: "53.22. pg_rules"
---


## 53.22. `pg_rules`

The view `pg_rules` provides access to useful information about query rewrite rules.

**Table 53.22. `pg_rules` Columns**

| Column Type  Description |
| --- |
| `schemaname` `name` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)  Name of schema containing table |
| `tablename` `name` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`relname`)  Name of table the rule is for |
| `rulename` `name` (references [`pg_rewrite`](catalog-pg-rewrite.html "52.45. pg_rewrite").`rulename`)  Name of rule |
| `definition` `text`  Rule definition (a reconstructed creation command) |

  

The `pg_rules` view excludes the `ON SELECT` rules of views and materialized views; those can be seen in [`pg_views`](view-pg-views.html "53.37. pg_views") and [`pg_matviews`](view-pg-matviews.html "53.14. pg_matviews").
