---
source: https://www.postgresql.org/docs/18/catalog-pg-foreign-server.html
title: "52.24. pg_foreign_server"
---


## 52.24. `pg_foreign_server`

The catalog `pg_foreign_server` stores foreign server definitions. A foreign server describes a source of external data, such as a remote server. Foreign servers are accessed via foreign-data wrappers.

**Table 52.24. `pg_foreign_server` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `srvname` `name`  Name of the foreign server |
| `srvowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the foreign server |
| `srvfdw` `oid` (references [`pg_foreign_data_wrapper`](catalog-pg-foreign-data-wrapper.html "52.23. pg_foreign_data_wrapper").`oid`)  OID of the foreign-data wrapper of this foreign server |
| `srvtype` `text`  Type of the server (optional) |
| `srvversion` `text`  Version of the server (optional) |
| `srvacl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
| `srvoptions` `text[]`  Foreign server specific options, as “keyword=value” strings |
