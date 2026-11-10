---
source: https://www.postgresql.org/docs/18/catalog-pg-conversion.html
title: "52.14. pg_conversion"
---


## 52.14. `pg_conversion`

The catalog `pg_conversion` describes encoding conversion functions. See [CREATE CONVERSION](sql-createconversion.html "CREATE CONVERSION") for more information.

**Table 52.14. `pg_conversion` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `conname` `name`  Conversion name (unique within a namespace) |
| `connamespace` `oid` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`oid`)  The OID of the namespace that contains this conversion |
| `conowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the conversion |
| `conforencoding` `int4`  Source encoding ID ([`pg_encoding_to_char()`](functions-info.html#PG-ENCODING-TO-CHAR) can translate this number to the encoding name) |
| `contoencoding` `int4`  Destination encoding ID ([`pg_encoding_to_char()`](functions-info.html#PG-ENCODING-TO-CHAR) can translate this number to the encoding name) |
| `conproc` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  Conversion function |
| `condefault` `bool`  True if this is the default conversion |
