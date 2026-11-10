---
source: https://www.postgresql.org/docs/18/catalog-pg-namespace.html
title: "52.32. pg_namespace"
---


## 52.32. `pg_namespace`

The catalog `pg_namespace` stores namespaces. A namespace is the structure underlying SQL schemas: each namespace can have a separate collection of relations, types, etc. without name conflicts.

**Table 52.32. `pg_namespace` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `nspname` `name`  Name of the namespace |
| `nspowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the namespace |
| `nspacl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
