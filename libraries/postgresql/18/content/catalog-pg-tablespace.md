---
source: https://www.postgresql.org/docs/18/catalog-pg-tablespace.html
title: "52.56. pg_tablespace"
---


## 52.56. `pg_tablespace`

The catalog `pg_tablespace` stores information about the available tablespaces. Tables can be placed in particular tablespaces to aid administration of disk layout.

Unlike most system catalogs, `pg_tablespace` is shared across all databases of a cluster: there is only one copy of `pg_tablespace` per cluster, not one per database.

**Table 52.56. `pg_tablespace` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `spcname` `name`  Tablespace name |
| `spcowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the tablespace, usually the user who created it |
| `spcacl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
| `spcoptions` `text[]`  Tablespace-level options, as “keyword=value” strings |
