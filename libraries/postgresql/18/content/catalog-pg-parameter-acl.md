---
source: https://www.postgresql.org/docs/18/catalog-pg-parameter-acl.html
title: "52.36. pg_parameter_acl"
---


## 52.36. `pg_parameter_acl`

The catalog `pg_parameter_acl` records configuration parameters for which privileges have been granted to one or more roles. No entry is made for parameters that have default privileges.

Unlike most system catalogs, `pg_parameter_acl` is shared across all databases of a cluster: there is only one copy of `pg_parameter_acl` per cluster, not one per database.

**Table 52.36. `pg_parameter_acl` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `parname` `text`  The name of a configuration parameter for which privileges are granted |
| `paracl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
