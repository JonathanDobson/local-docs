---
source: https://www.postgresql.org/docs/18/catalog-pg-shseclabel.html
title: "52.50. pg_shseclabel"
---


## 52.50. `pg_shseclabel`

The catalog `pg_shseclabel` stores security labels on shared database objects. Security labels can be manipulated with the [`SECURITY LABEL`](sql-security-label.html "SECURITY LABEL") command. For an easier way to view security labels, see [Section 53.23](view-pg-seclabels.html "53.23. pg_seclabels").

See also [`pg_seclabel`](catalog-pg-seclabel.html "52.46. pg_seclabel"), which performs a similar function for security labels involving objects within a single database.

Unlike most system catalogs, `pg_shseclabel` is shared across all databases of a cluster: there is only one copy of `pg_shseclabel` per cluster, not one per database.

**Table 52.50. `pg_shseclabel` Columns**

| Column Type  Description |
| --- |
| `objoid` `oid` (references any OID column)  The OID of the object this security label pertains to |
| `classoid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the system catalog this object appears in |
| `provider` `text`  The label provider associated with this label. |
| `label` `text`  The security label applied to this object. |
