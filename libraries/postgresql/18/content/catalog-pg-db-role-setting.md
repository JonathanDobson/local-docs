---
source: https://www.postgresql.org/docs/18/catalog-pg-db-role-setting.html
title: "52.16. pg_db_role_setting"
---


## 52.16. `pg_db_role_setting`

The catalog `pg_db_role_setting` records the default values that have been set for run-time configuration variables, for each role and database combination.

Unlike most system catalogs, `pg_db_role_setting` is shared across all databases of a cluster: there is only one copy of `pg_db_role_setting` per cluster, not one per database.

**Table 52.16. `pg_db_role_setting` Columns**

| Column Type  Description |
| --- |
| `setdatabase` `oid` (references [`pg_database`](catalog-pg-database.html "52.15. pg_database").`oid`)  The OID of the database the setting is applicable to, or zero if not database-specific |
| `setrole` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  The OID of the role the setting is applicable to, or zero if not role-specific |
| `setconfig` `text[]`  Defaults for run-time configuration variables |
