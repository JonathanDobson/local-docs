---
source: https://www.postgresql.org/docs/18/catalog-pg-inherits.html
title: "52.27. pg_inherits"
---


## 52.27. `pg_inherits`

The catalog `pg_inherits` records information about table and index inheritance hierarchies. There is one entry for each direct parent-child table or index relationship in the database. (Indirect inheritance can be determined by following chains of entries.)

**Table 52.27. `pg_inherits` Columns**

| Column Type  Description |
| --- |
| `inhrelid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the child table or index |
| `inhparent` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the parent table or index |
| `inhseqno` `int4`  If there is more than one direct parent for a child table (multiple inheritance), this number tells the order in which the inherited columns are to be arranged. The count starts at 1.  Indexes cannot have multiple inheritance, since they can only inherit when using declarative partitioning. |
| `inhdetachpending` `bool`  `true` for a partition that is in the process of being detached; `false` otherwise. |
