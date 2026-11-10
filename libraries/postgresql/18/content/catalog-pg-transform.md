---
source: https://www.postgresql.org/docs/18/catalog-pg-transform.html
title: "52.57. pg_transform"
---


## 52.57. `pg_transform`

The catalog `pg_transform` stores information about transforms, which are a mechanism to adapt data types to procedural languages. See [CREATE TRANSFORM](sql-createtransform.html "CREATE TRANSFORM") for more information.

**Table 52.57. `pg_transform` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `trftype` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  OID of the data type this transform is for |
| `trflang` `oid` (references [`pg_language`](catalog-pg-language.html "52.29. pg_language").`oid`)  OID of the language this transform is for |
| `trffromsql` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  The OID of the function to use when converting the data type for input to the procedural language (e.g., function parameters). Zero is stored if the default behavior should be used. |
| `trftosql` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  The OID of the function to use when converting output from the procedural language (e.g., return values) to the data type. Zero is stored if the default behavior should be used. |
