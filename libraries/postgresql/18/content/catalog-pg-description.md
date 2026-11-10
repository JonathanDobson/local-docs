---
source: https://www.postgresql.org/docs/18/catalog-pg-description.html
title: "52.19. pg_description"
---


## 52.19. `pg_description`

The catalog `pg_description` stores optional descriptions (comments) for each database object. Descriptions can be manipulated with the [`COMMENT`](sql-comment.html "COMMENT") command and viewed with psql's `\d` commands. Descriptions of many built-in system objects are provided in the initial contents of `pg_description`.

See also [`pg_shdescription`](catalog-pg-shdescription.html "52.49. pg_shdescription"), which performs a similar function for descriptions involving objects that are shared across a database cluster.

**Table 52.19. `pg_description` Columns**

| Column Type  Description |
| --- |
| `objoid` `oid` (references any OID column)  The OID of the object this description pertains to |
| `classoid` `oid` (references [`pg_class`](catalog-pg-class.html "52.11. pg_class").`oid`)  The OID of the system catalog this object appears in |
| `objsubid` `int4`  For a comment on a table column, this is the column number (the `objoid` and `classoid` refer to the table itself). For all other object types, this column is zero. |
| `description` `text`  Arbitrary text that serves as the description of this object |
