---
source: https://www.postgresql.org/docs/18/catalog-pg-attrdef.html
title: "52.6. pg_attrdef"
---


## 52.6. `pg_attrdef`

The catalog `pg_attrdef` stores column default expressions and generation expressions. The main information about columns is stored in [`pg_attribute`](catalog-pg-attribute.html "52.7. pg_attribute"). Only columns for which a default expression or generation expression has been explicitly set will have an entry here.

**Table 52.6. `pg_attrdef` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `adrelid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The table this column belongs to |
| `adnum` `int2` (references [`pg_attribute`](catalog-pg-attribute.html "52.7. pg_attribute").`attnum`)  The number of the column |
| `adbin` `pg_node_tree`  The column default or generation expression, in `nodeToString()` representation. Use `pg_get_expr(adbin, adrelid)` to convert it to an SQL expression. |
