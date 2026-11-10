---
source: https://www.postgresql.org/docs/18/catalog-pg-am.html
title: "52.3. pg_am"
---


## 52.3. `pg_am`

The catalog `pg_am` stores information about relation access methods. There is one row for each access method supported by the system. Currently, only tables and indexes have access methods. The requirements for table and index access methods are discussed in detail in [Chapter 62](tableam.html "Chapter 62. Table Access Method Interface Definition") and [Chapter 63](indexam.html "Chapter 63. Index Access Method Interface Definition") respectively.

**Table 52.3. `pg_am` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `amname` `name`  Name of the access method |
| `amhandler` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of a handler function that is responsible for supplying information about the access method |
| `amtype` `char`  `t` = table (including materialized views), `i` = index. |

  

### Note

Before PostgreSQL 9.6, `pg_am` contained many additional columns representing properties of index access methods. That data is now only directly visible at the C code level. However, `pg_index_column_has_property()` and related functions have been added to allow SQL queries to inspect index access method properties; see [Table 9.76](functions-info.html#FUNCTIONS-INFO-CATALOG-TABLE "Table 9.76. System Catalog Information Functions").
