---
source: https://www.postgresql.org/docs/18/catalog-pg-publication-namespace.html
title: "52.41. pg_publication_namespace"
---


## 52.41. `pg_publication_namespace`

The catalog `pg_publication_namespace` contains the mapping between schemas and publications in the database. This is a many-to-many mapping.

**Table 52.41. `pg_publication_namespace` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `pnpubid` `oid` (references [`pg_publication`](catalog-pg-publication.html "52.40. pg_publication").`oid`)  Reference to publication |
| `pnnspid` `oid` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`oid`)  Reference to schema |
