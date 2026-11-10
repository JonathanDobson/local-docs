---
source: https://www.postgresql.org/docs/18/catalog-pg-seclabel.html
title: "52.46. pg_seclabel"
---


## 52.46. `pg_seclabel`

The catalog `pg_seclabel` stores security labels on database objects. Security labels can be manipulated with the [`SECURITY LABEL`](sql-security-label.html "SECURITY LABEL") command. For an easier way to view security labels, see [Section 53.23](view-pg-seclabels.html "53.23. pg_seclabels").

See also [`pg_shseclabel`](catalog-pg-shseclabel.html "52.50. pg_shseclabel"), which performs a similar function for security labels of database objects that are shared across a database cluster.

**Table 52.46. `pg_seclabel` Columns**

| Column Type  Description |
| --- |
| `objoid` `oid` (references any OID column)  The OID of the object this security label pertains to |
| `classoid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the system catalog this object appears in |
| `objsubid` `int4`  For a security label on a table column, this is the column number (the `objoid` and `classoid` refer to the table itself). For all other object types, this column is zero. |
| `provider` `text`  The label provider associated with this label. |
| `label` `text`  The security label applied to this object. |
