---
source: https://www.postgresql.org/docs/18/catalog-pg-shdescription.html
title: "52.49. pg_shdescription"
---


## 52.49. `pg_shdescription`

The catalog `pg_shdescription` stores optional descriptions (comments) for shared database objects. Descriptions can be manipulated with the [`COMMENT`](sql-comment.html "COMMENT") command and viewed with psql's `\d` commands.

See also [`pg_description`](catalog-pg-description.html "52.19. pg_description"), which performs a similar function for descriptions involving objects within a single database.

Unlike most system catalogs, `pg_shdescription` is shared across all databases of a cluster: there is only one copy of `pg_shdescription` per cluster, not one per database.

**Table 52.49. `pg_shdescription` Columns**

| Column Type  Description |
| --- |
| `objoid` `oid` (references any OID column)  The OID of the object this description pertains to |
| `classoid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the system catalog this object appears in |
| `description` `text`  Arbitrary text that serves as the description of this object |
