---
source: https://www.postgresql.org/docs/18/catalog-pg-foreign-data-wrapper.html
title: "52.23. pg_foreign_data_wrapper"
---


## 52.23. `pg_foreign_data_wrapper`

The catalog `pg_foreign_data_wrapper` stores foreign-data wrapper definitions. A foreign-data wrapper is the mechanism by which external data, residing on foreign servers, is accessed.

**Table 52.23. `pg_foreign_data_wrapper` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `fdwname` `name`  Name of the foreign-data wrapper |
| `fdwowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the foreign-data wrapper |
| `fdwhandler` `oid` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  References a handler function that is responsible for supplying execution routines for the foreign-data wrapper. Zero if no handler is provided |
| `fdwvalidator` `oid` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  References a validator function that is responsible for checking the validity of the options given to the foreign-data wrapper, as well as options for foreign servers and user mappings using the foreign-data wrapper. Zero if no validator is provided |
| `fdwacl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
| `fdwoptions` `text[]`  Foreign-data wrapper specific options, as “keyword=value” strings |
